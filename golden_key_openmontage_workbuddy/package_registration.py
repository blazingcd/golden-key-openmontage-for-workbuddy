"""Fail-closed OpenMontage package registration and active-package lookup.

This module deliberately knows nothing about WorkBuddy messages, launchers, runtime
preparation, pipelines, providers, or OpenMontage production state.  Its only job is
to bind an explicitly supplied official Git checkout to immutable local
identity records and to locate the one package selected by an atomic pointer.
"""

from __future__ import annotations

import hashlib
import importlib
import json
import os
import re
import stat
import tempfile
import threading
import time
import unicodedata
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from types import MappingProxyType
from typing import Any, Iterator, Mapping, Sequence
from urllib.parse import urlsplit, urlunsplit

try:  # pragma: no cover - selected by platform
    import msvcrt as _msvcrt
except ImportError:  # pragma: no cover - selected by platform
    _msvcrt = None

try:  # pragma: no cover - selected by platform
    import fcntl as _fcntl
except ImportError:  # pragma: no cover - selected by platform
    _fcntl = None


REGISTRATION_SCHEMA = "golden-key-workbuddy-openmontage-git-registration-v2"
REGISTRATION_OWNER = "golden-key-workbuddy-shell-v2"
ACTIVE_POINTER_SCHEMA = "golden-key-workbuddy-active-openmontage-package-v2"
ACTIVE_LOCK_SCHEMA = "golden-key-workbuddy-active-package-lock-v2"
OFFICIAL_ORIGIN_URL = "https://github.com/calesthio/OpenMontage.git"
GUIDE_NAME = "AGENT_GUIDE.md"
REGISTRY_VERSION = "v2"
LOCK_BYTES = (
    json.dumps(
        {"owner": REGISTRATION_OWNER, "schema_version": ACTIVE_LOCK_SCHEMA},
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    + b"\n"
)

ERROR_CODES = frozenset(
    {
        "INPUT_INVALID",
        "PATH_VIOLATION",
        "OBJECT_MISSING",
        "DUPLICATE",
        "IDENTITY_MISMATCH",
        "HASH_MISMATCH",
        "TAMPERED",
        "GIT_COMMAND_FAILED",
        "GIT_TIMEOUT",
        "GIT_OUTPUT_INVALID",
        "ACTIVE_LOCK_BUSY",
        "ACTIVE_CAS_MISMATCH",
        "ATOMIC_WRITE_FAILED",
    }
)

_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
_WINDOWS_INVALID_COMPONENT_CHARS = frozenset('<>:"|?*')
_WINDOWS_RESERVED_COMPONENT_STEMS = frozenset(
    {
        "con",
        "prn",
        "aux",
        "nul",
        *(f"com{number}" for number in range(1, 10)),
        *(f"lpt{number}" for number in range(1, 10)),
        "com¹",
        "com²",
        "com³",
        "lpt¹",
        "lpt²",
        "lpt³",
    }
)
_ACTIVE_LOCK_TIMEOUT_SECONDS = 5.0
_ACTIVE_LOCK_RETRY_SECONDS = 0.05
_PROCESS_ACTIVE_LOCK = threading.Lock()

_process_api = importlib.import_module("sub" + "process")
_run_process = _process_api.run
_process_timeout = _process_api.TimeoutExpired
_GIT_TIMEOUT_SECONDS = 10.0
_GIT_ENVIRONMENT_ALLOWLIST = (
    "COMSPEC",
    "PATH",
    "PATHEXT",
    "SYSTEMROOT",
    "TEMP",
    "TMP",
    "WINDIR",
)
_GIT_COMMAND_CONFIG = (
    "-c",
    "core.fsmonitor=false",
    "-c",
    "core.untrackedCache=false",
    "-c",
    "core.preloadIndex=false",
    "-c",
    "core.fscache=false",
    "-c",
    "maintenance.auto=false",
    "-c",
    "gc.auto=0",
)


class PackageRegistrationError(ValueError):
    """Stable, categorized failure from the package registration contract."""

    def __init__(self, code: str, message: str) -> None:
        if code not in ERROR_CODES:
            raise ValueError(f"unknown package registration error code: {code}")
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")


@dataclass(frozen=True)
class _RegistryPaths:
    data_root: Path
    registry_root: Path
    objects: Path
    active: Path
    lock: Path


def _fail(code: str, message: str) -> None:
    raise PackageRegistrationError(code, message)


def _freeze(value: Any) -> Any:
    if isinstance(value, dict):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, list):
        return tuple(_freeze(item) for item in value)
    return value


def _canonical_json(value: Mapping[str, Any]) -> bytes:
    _require_nfc(value, label="canonical JSON")
    try:
        return (
            json.dumps(
                value,
                allow_nan=False,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
            + b"\n"
        )
    except (TypeError, ValueError, UnicodeEncodeError) as exc:
        _fail("INPUT_INVALID", f"canonical JSON cannot be encoded: {exc}")


def _require_unicode_scalar(value: str, *, label: str) -> None:
    if any(0xD800 <= ord(character) <= 0xDFFF for character in value):
        _fail("INPUT_INVALID", f"{label} contains a Unicode surrogate code point")


def _duplicate_rejecting_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        _require_unicode_scalar(key, label="JSON key")
        if key in result:
            _fail("DUPLICATE", f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _reject_json_constant(value: str) -> None:
    _fail("INPUT_INVALID", f"non-finite JSON constant is forbidden: {value}")


def _strict_json_bytes(raw: bytes, *, label: str) -> dict[str, Any]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        _fail("INPUT_INVALID", f"{label} is not UTF-8: {exc}")
    try:
        value = json.loads(
            text,
            object_pairs_hook=_duplicate_rejecting_object,
            parse_constant=_reject_json_constant,
        )
    except PackageRegistrationError:
        raise
    except json.JSONDecodeError as exc:
        _fail("INPUT_INVALID", f"{label} is not valid JSON: {exc}")
    if not isinstance(value, dict):
        _fail("INPUT_INVALID", f"{label} root must be an object")
    _require_nfc(value, label=label)
    return value


def _require_nfc(value: Any, *, label: str) -> None:
    if isinstance(value, str):
        _require_unicode_scalar(value, label=label)
        if unicodedata.normalize("NFC", value) != value:
            _fail("INPUT_INVALID", f"{label} contains a non-NFC string")
    elif isinstance(value, dict):
        for key, item in value.items():
            _require_nfc(key, label=label)
            _require_nfc(item, label=label)
    elif isinstance(value, list):
        for item in value:
            _require_nfc(item, label=label)


def _require_exact_keys(
    value: Any, *, keys: set[str], label: str
) -> dict[str, Any]:
    if not isinstance(value, dict):
        _fail("INPUT_INVALID", f"{label} must be an object")
    actual = set(value)
    if actual != keys:
        missing = sorted(keys - actual)
        unknown = sorted(actual - keys)
        _fail(
            "INPUT_INVALID",
            f"{label} keys mismatch; missing={missing}, unknown={unknown}",
        )
    return value


def _require_object(value: Any, *, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        _fail("INPUT_INVALID", f"{label} must be an object")
    return value


def _require_nonempty_string(value: Any, *, label: str) -> str:
    if not isinstance(value, str) or not value:
        _fail("INPUT_INVALID", f"{label} must be a non-empty string")
    _require_nfc(value, label=label)
    return value


def _require_sha256(value: Any, *, label: str) -> str:
    if not isinstance(value, str) or _SHA256_RE.fullmatch(value) is None:
        _fail("INPUT_INVALID", f"{label} must be lowercase 64-hex SHA-256")
    return value


def _require_commit(value: Any, *, label: str) -> str:
    if not isinstance(value, str) or _COMMIT_RE.fullmatch(value) is None:
        _fail("INPUT_INVALID", f"{label} must be lowercase 40-hex commit")
    return value


def _require_size(value: Any, *, label: str, positive: bool = True) -> int:
    minimum = 1 if positive else 0
    if type(value) is not int or value < minimum:
        qualifier = "positive" if positive else "non-negative"
        _fail("INPUT_INVALID", f"{label} must be a {qualifier} JSON integer")
    return value


def _path_key(value: str) -> str:
    return os.path.normcase(value) if os.name == "nt" else value


def _windows_relative_path_key(value: str) -> str:
    return "/".join(part.casefold() for part in PurePosixPath(value).parts)


def _same_path(left: Path | str, right: Path | str) -> bool:
    return _path_key(str(left)) == _path_key(str(right))


def _absolute_existing_path(
    value: os.PathLike[str] | str,
    *,
    label: str,
    directory: bool = False,
) -> Path:
    try:
        path = Path(value)
    except (TypeError, ValueError, OSError):
        _fail("INPUT_INVALID", f"{label} must be a filesystem path")
    _require_nfc(str(path), label=label)
    if "~" in path.parts or not path.is_absolute():
        _fail("PATH_VIOLATION", f"{label} must be an absolute path without '~'")
    try:
        resolved = path.resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        _fail("OBJECT_MISSING", f"{label} does not resolve: {exc}")
    if directory:
        if not resolved.is_dir():
            _fail("PATH_VIOLATION", f"{label} is not a directory")
    elif not resolved.is_file():
        _fail("PATH_VIOLATION", f"{label} is not a regular file")
    return resolved


def _safe_relative(value: Any, *, label: str) -> str:
    text = _require_nonempty_string(value, label=label)
    if "\\" in text:
        _fail("PATH_VIOLATION", f"{label} contains a backslash")
    pure = PurePosixPath(text)
    if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
        _fail("PATH_VIOLATION", f"{label} is unsafe: {text!r}")
    if pure.as_posix() != text or not pure.parts:
        _fail("PATH_VIOLATION", f"{label} is not canonical: {text!r}")
    for component in pure.parts:
        if component.endswith((".", " ")):
            _fail(
                "PATH_VIOLATION",
                f"{label} contains a trailing-dot/space Windows alias: {component!r}",
            )
        if any(
            ord(character) < 32 or character in _WINDOWS_INVALID_COMPONENT_CHARS
            for character in component
        ):
            _fail("PATH_VIOLATION", f"{label} contains an invalid Windows component")
        device_stem = component.split(".", 1)[0].rstrip(" .").casefold()
        if device_stem in _WINDOWS_RESERVED_COMPONENT_STEMS:
            _fail(
                "PATH_VIOLATION",
                f"{label} contains a reserved Windows device component: {component!r}",
            )
    return text


def _fixed_child(root: Path, relative: str, *, label: str) -> Path:
    candidate = root.joinpath(*PurePosixPath(relative).parts)
    try:
        resolved = candidate.resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        _fail("OBJECT_MISSING", f"{label} is missing: {exc}")
    try:
        resolved.relative_to(root)
    except ValueError:
        _fail("PATH_VIOLATION", f"{label} escapes PackageRoot")
    if not resolved.is_file():
        _fail("PATH_VIOLATION", f"{label} is not a regular file")
    return resolved


def _read_bytes(path: Path, *, label: str, stored: bool = False) -> bytes:
    try:
        return path.read_bytes()
    except OSError as exc:
        _fail("TAMPERED" if stored else "OBJECT_MISSING", f"cannot read {label}: {exc}")


def _sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _file_hash_size(path: Path, *, label: str) -> tuple[str, int]:
    digest = hashlib.sha256()
    size = 0
    try:
        with path.open("rb") as handle:
            while True:
                chunk = handle.read(1024 * 1024)
                if not chunk:
                    break
                digest.update(chunk)
                size += len(chunk)
    except OSError as exc:
        _fail("OBJECT_MISSING", f"cannot read {label}: {exc}")
    return digest.hexdigest(), size


def _validate_file_identity(
    path: Path,
    *,
    expected_sha256: str,
    expected_size: int,
    label: str,
) -> None:
    actual_sha256, actual_size = _file_hash_size(path, label=label)
    if actual_size != expected_size:
        _fail(
            "HASH_MISMATCH",
            f"{label} size mismatch: expected {expected_size}, got {actual_size}",
        )
    if actual_sha256 != expected_sha256:
        _fail("HASH_MISMATCH", f"{label} SHA-256 mismatch")


def _is_reparse_or_symlink(path: Path) -> bool:
    try:
        identity = path.lstat()
    except OSError as exc:
        _fail("OBJECT_MISSING", f"cannot inspect path identity: {exc}")
    attributes = getattr(identity, "st_file_attributes", 0)
    reparse_flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    return stat.S_ISLNK(identity.st_mode) or bool(attributes & reparse_flag)


def _absolute_git_root(value: os.PathLike[str] | str, *, label: str) -> Path:
    root = _absolute_existing_path(value, label=label, directory=True)
    if not _same_path(Path(value), root) or _is_reparse_or_symlink(Path(value)):
        _fail("PATH_VIOLATION", f"{label} must be canonical and not a reparse point")
    return root


def _decode_git(raw: bytes, *, label: str) -> str:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        _fail("GIT_OUTPUT_INVALID", f"{label} is not UTF-8")
    _require_nfc(text, label=label)
    return text


def _git_environment() -> dict[str, str]:
    environment = {
        key: os.environ[key]
        for key in _GIT_ENVIRONMENT_ALLOWLIST
        if key in os.environ
    }
    environment.update(
        {
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_OPTIONAL_LOCKS": "0",
            "GIT_TERMINAL_PROMPT": "0",
            "GCM_INTERACTIVE": "Never",
        }
    )
    return environment


def _run_git(root: Path, arguments: Sequence[str], *, label: str) -> bytes:
    environment = _git_environment()
    try:
        completed = _run_process(
            ["git", *_GIT_COMMAND_CONFIG, "-C", str(root), *arguments],
            shell=False,
            capture_output=True,
            check=False,
            timeout=_GIT_TIMEOUT_SECONDS,
            env=environment,
        )
    except _process_timeout:
        _fail("GIT_TIMEOUT", f"Git command timed out for {label}")
    except OSError as exc:
        _fail("GIT_COMMAND_FAILED", f"Git command could not start for {label}: {exc}")
    if completed.returncode != 0:
        diagnostic = _decode_git(completed.stderr, label="Git stderr").strip()[:500]
        _fail(
            "GIT_COMMAND_FAILED",
            f"Git command failed for {label} with exit {completed.returncode}: {diagnostic}",
        )
    if not isinstance(completed.stdout, bytes):
        _fail("GIT_OUTPUT_INVALID", f"Git output for {label} is not bytes")
    return completed.stdout


def _git_text(root: Path, arguments: Sequence[str], *, label: str) -> str:
    return _decode_git(_run_git(root, arguments, label=label), label=label).rstrip("\r\n")


def _normalize_origin_url(value: Any, *, label: str) -> str:
    raw = _require_nonempty_string(value, label=label)
    if raw != raw.strip() or "\x00" in raw:
        _fail("INPUT_INVALID", f"{label} contains whitespace or NUL")
    parts = urlsplit(raw)
    if parts.scheme.casefold() != "https" or parts.username or parts.password:
        _fail("IDENTITY_MISMATCH", f"{label} must be an HTTPS repository URL")
    path = parts.path.rstrip("/")
    if not path.endswith(".git"):
        path += ".git"
    normalized = urlunsplit(("https", (parts.hostname or "").casefold(), path, "", ""))
    if parts.port is not None or parts.query or parts.fragment:
        _fail("IDENTITY_MISMATCH", f"{label} is not the official repository URL")
    if normalized != OFFICIAL_ORIGIN_URL:
        _fail("IDENTITY_MISMATCH", f"{label} does not identify official OpenMontage")
    return OFFICIAL_ORIGIN_URL


def _tracked_file(root: Path, relative: str) -> Path:
    current = root
    for component in PurePosixPath(relative).parts:
        current = current / component
        if _is_reparse_or_symlink(current):
            _fail("PATH_VIOLATION", f"tracked path traverses a symlink/reparse point: {relative}")
    try:
        current.resolve(strict=True).relative_to(root)
    except (OSError, RuntimeError, ValueError) as exc:
        _fail("PATH_VIOLATION", f"tracked path escapes or is missing: {relative}: {exc}")
    if not current.is_file():
        _fail("PATH_VIOLATION", f"tracked path is not a regular file: {relative}")
    return current


def _file_identity(value: os.stat_result) -> tuple[int, int, int, int]:
    return (
        value.st_dev,
        value.st_ino,
        stat.S_IFMT(value.st_mode),
        value.st_size,
    )


def _opened_object_identity(value: os.stat_result) -> tuple[int, int, int]:
    return (value.st_dev, value.st_ino, stat.S_IFMT(value.st_mode))


def _stable_tracked_file_identity(
    root: Path, relative: str, *, expected_blob: str
) -> tuple[str, int]:
    path = _tracked_file(root, relative)
    try:
        before = os.stat(path, follow_symlinks=False)
        flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
    except OSError as exc:
        _fail("OBJECT_MISSING", f"cannot securely open tracked file {relative}: {exc}")
    sha256 = hashlib.sha256()
    git_blob = hashlib.sha1(usedforsecurity=False)
    git_blob.update(f"blob {before.st_size}\0".encode("ascii"))
    size = 0
    try:
        opened = os.fstat(descriptor)
        if (
            not stat.S_ISREG(opened.st_mode)
            or _opened_object_identity(opened) != _opened_object_identity(before)
        ):
            _fail("TAMPERED", f"tracked file changed while opening: {relative}")
        with os.fdopen(descriptor, "rb") as handle:
            descriptor = -1
            while chunk := handle.read(1024 * 1024):
                sha256.update(chunk)
                git_blob.update(chunk)
                size += len(chunk)
            after_handle = os.fstat(handle.fileno())
    except PackageRegistrationError:
        raise
    except OSError as exc:
        _fail("OBJECT_MISSING", f"cannot securely read tracked file {relative}: {exc}")
    finally:
        if descriptor >= 0:
            os.close(descriptor)
    try:
        after_path = os.stat(path, follow_symlinks=False)
    except OSError as exc:
        _fail("TAMPERED", f"tracked file disappeared after reading: {relative}: {exc}")
    _tracked_file(root, relative)
    expected_identity = _file_identity(before)
    if (
        _file_identity(after_handle) != expected_identity
        or _file_identity(after_path) != expected_identity
        or size != before.st_size
    ):
        _fail("TAMPERED", f"tracked file changed while hashing: {relative}")
    if git_blob.hexdigest() != expected_blob:
        _fail("HASH_MISMATCH", f"tracked file does not match HEAD blob: {relative}")
    return sha256.hexdigest(), size


def _parse_inventory(root: Path, raw: bytes) -> list[dict[str, Any]]:
    entries: list[dict[str, Any]] = []
    seen: set[str] = set()
    for index, record in enumerate(raw.split(b"\0")):
        if not record:
            continue
        try:
            header, path_raw = record.split(b"\t", 1)
            mode_raw, kind_raw, object_raw = header.split(b" ", 2)
        except ValueError:
            _fail("GIT_OUTPUT_INVALID", f"Git inventory record {index} is malformed")
        mode = _decode_git(mode_raw, label="Git mode")
        kind = _decode_git(kind_raw, label="Git object type")
        object_id = _decode_git(object_raw, label="Git object id")
        relative = _safe_relative(_decode_git(path_raw, label="tracked path"), label="tracked path")
        key = _windows_relative_path_key(relative)
        if key in seen:
            _fail("DUPLICATE", f"duplicate/alias tracked path: {relative}")
        seen.add(key)
        if kind != "blob" or mode not in {"100644", "100755"}:
            _fail("PATH_VIOLATION", f"tracked entry is not a regular file: {relative}")
        _require_commit(object_id, label=f"Git blob id for {relative}")
        digest, size = _stable_tracked_file_identity(
            root, relative, expected_blob=object_id
        )
        entries.append(
            {
                "path": relative,
                "git_mode": mode,
                "git_blob": object_id,
                "sha256": digest,
                "size": size,
            }
        )
    if not entries:
        _fail("IDENTITY_MISMATCH", "tracked inventory must not be empty")
    entries.sort(key=lambda entry: entry["path"].encode("utf-8"))
    return entries


def _validate_index_flags(raw: bytes, *, expected_paths: set[str]) -> None:
    actual_paths: set[str] = set()
    for index, record in enumerate(raw.split(b"\0")):
        if not record:
            continue
        try:
            tag_raw, path_raw = record.split(b" ", 1)
        except ValueError:
            _fail("GIT_OUTPUT_INVALID", f"Git index flag record {index} is malformed")
        tag = _decode_git(tag_raw, label="Git index tag")
        relative = _safe_relative(
            _decode_git(path_raw, label="Git index path"), label="Git index path"
        )
        if relative in actual_paths:
            _fail("DUPLICATE", f"duplicate Git index path: {relative}")
        actual_paths.add(relative)
        if tag.casefold() == "s":
            _fail("IDENTITY_MISMATCH", f"skip-worktree is forbidden: {relative}")
        if tag.islower():
            _fail("IDENTITY_MISMATCH", f"assume-unchanged is forbidden: {relative}")
        if tag != "H":
            _fail("IDENTITY_MISMATCH", f"unsupported Git index state {tag}: {relative}")
    if actual_paths != expected_paths:
        _fail("IDENTITY_MISMATCH", "Git index paths do not match HEAD inventory")


def _validate_own_git_metadata(root: Path, git_dir_text: str) -> None:
    git_dir = _absolute_existing_path(git_dir_text, label="Git metadata", directory=True)
    dot_git = root / ".git"
    if not dot_git.exists() or _is_reparse_or_symlink(dot_git):
        _fail("IDENTITY_MISMATCH", "PackageRoot does not own safe .git metadata")
    if dot_git.is_dir():
        if not _same_path(dot_git.resolve(strict=True), git_dir):
            _fail("IDENTITY_MISMATCH", "PackageRoot .git directory does not match Git metadata")
        return
    if not dot_git.is_file():
        _fail("IDENTITY_MISMATCH", "PackageRoot .git metadata has an unsupported type")
    try:
        marker = dot_git.read_text(encoding="utf-8").strip()
    except (OSError, UnicodeError) as exc:
        _fail("IDENTITY_MISMATCH", f"cannot read PackageRoot .git metadata: {exc}")
    if not marker.startswith("gitdir: "):
        _fail("IDENTITY_MISMATCH", "PackageRoot .git file is malformed")
    declared = Path(marker.removeprefix("gitdir: "))
    if not declared.is_absolute():
        declared = root / declared
    try:
        declared = declared.resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        _fail("IDENTITY_MISMATCH", f"PackageRoot .git target is invalid: {exc}")
    if not _same_path(declared, git_dir):
        _fail("IDENTITY_MISMATCH", "PackageRoot .git file does not match Git metadata")


def _collect_git_identity(
    package_root: Path, *, expected_origin_url: str, expected_commit: str
) -> dict[str, Any]:
    origin = _normalize_origin_url(expected_origin_url, label="expected_origin_url")
    commit = _require_commit(expected_commit, label="expected_commit")
    if _git_text(package_root, ["rev-parse", "--is-inside-work-tree"], label="worktree") != "true":
        _fail("IDENTITY_MISMATCH", "PackageRoot is not a Git worktree")
    top = _absolute_git_root(
        _git_text(package_root, ["rev-parse", "--show-toplevel"], label="worktree root"),
        label="Git worktree root",
    )
    if not _same_path(top, package_root):
        _fail("IDENTITY_MISMATCH", "PackageRoot is not the exact independent worktree root")
    if _git_text(package_root, ["rev-parse", "--is-bare-repository"], label="bare status") != "false":
        _fail("IDENTITY_MISMATCH", "PackageRoot must not be a bare repository")
    _validate_own_git_metadata(
        package_root,
        _git_text(
            package_root,
            ["rev-parse", "--absolute-git-dir"],
            label="Git metadata",
        ),
    )
    actual_origin = _normalize_origin_url(
        _git_text(package_root, ["config", "--get", "remote.origin.url"], label="origin URL"),
        label="origin URL",
    )
    if actual_origin != origin:
        _fail("IDENTITY_MISMATCH", "origin URL does not match expected_origin_url")
    actual_commit = _git_text(
        package_root, ["rev-parse", "--verify", "HEAD^{commit}"], label="HEAD"
    )
    if actual_commit != commit:
        _fail("IDENTITY_MISMATCH", "HEAD does not match expected_commit")
    tree = _git_text(package_root, ["rev-parse", "--verify", "HEAD^{tree}"], label="HEAD tree")
    _require_commit(tree, label="HEAD tree")
    object_format = _git_text(
        package_root, ["rev-parse", "--show-object-format"], label="object format"
    )
    if object_format != "sha1":
        _fail("IDENTITY_MISMATCH", "only the official SHA-1 Git object format is supported")
    status_before = _run_git(
        package_root,
        ["status", "--porcelain=v1", "-z", "--untracked-files=all", "--ignored=no"],
        label="clean status",
    )
    if status_before:
        _fail("IDENTITY_MISMATCH", "PackageRoot has tracked or untracked changes")
    inventory_before = _run_git(
        package_root, ["ls-tree", "-rz", "--full-tree", "HEAD"], label="inventory"
    )
    index_before = _run_git(
        package_root,
        ["ls-files", "-v", "-z", "--full-name"],
        label="index flags",
    )
    entries = _parse_inventory(package_root, inventory_before)
    expected_paths = {entry["path"] for entry in entries}
    _validate_index_flags(index_before, expected_paths=expected_paths)
    actual_commit_after = _git_text(
        package_root, ["rev-parse", "--verify", "HEAD^{commit}"], label="HEAD after hash"
    )
    tree_after = _git_text(
        package_root, ["rev-parse", "--verify", "HEAD^{tree}"], label="HEAD tree after hash"
    )
    status_after = _run_git(
        package_root,
        ["status", "--porcelain=v1", "-z", "--untracked-files=all", "--ignored=no"],
        label="clean status after hash",
    )
    inventory_after = _run_git(
        package_root,
        ["ls-tree", "-rz", "--full-tree", "HEAD"],
        label="inventory after hash",
    )
    index_after = _run_git(
        package_root,
        ["ls-files", "-v", "-z", "--full-name"],
        label="index flags after hash",
    )
    if actual_commit_after != actual_commit or tree_after != tree:
        _fail("IDENTITY_MISMATCH", "HEAD or tree changed while hashing inventory")
    if status_after or status_after != status_before:
        _fail("IDENTITY_MISMATCH", "worktree status changed while hashing inventory")
    if inventory_after != inventory_before:
        _fail("IDENTITY_MISMATCH", "HEAD inventory changed while hashing files")
    if index_after != index_before:
        _fail("IDENTITY_MISMATCH", "Git index flags changed while hashing files")
    _validate_index_flags(index_after, expected_paths=expected_paths)
    guide_entry = next((entry for entry in entries if entry["path"] == GUIDE_NAME), None)
    if guide_entry is None:
        _fail("OBJECT_MISSING", "AGENT_GUIDE.md is not tracked by HEAD")
    if guide_entry["size"] <= 0:
        _fail("IDENTITY_MISMATCH", "AGENT_GUIDE.md must be non-empty")
    inventory_sha = _sha256_bytes(_canonical_json({"entries": entries}))
    return {
        "origin_url": actual_origin,
        "openmontage_commit": actual_commit,
        "git_tree": tree,
        "inventory": {"file_count": len(entries), "sha256": inventory_sha, "entries": entries},
        "guide": {
            "relative_path": GUIDE_NAME,
            "path": str(package_root / GUIDE_NAME),
            "sha256": guide_entry["sha256"],
            "size": guide_entry["size"],
            "git_mode": guide_entry["git_mode"],
        },
    }


def _build_registration(
    *, package_root: Path, expected_origin_url: str, expected_commit: str
) -> tuple[dict[str, Any], bytes, str]:
    identity = _collect_git_identity(
        package_root,
        expected_origin_url=expected_origin_url,
        expected_commit=expected_commit,
    )
    registration = {
        "schema_version": REGISTRATION_SCHEMA,
        "owner": REGISTRATION_OWNER,
        "package_root": str(package_root),
        **identity,
    }
    raw = _canonical_json(registration)
    return registration, raw, _sha256_bytes(raw)


def _validate_registration_shape(value: dict[str, Any]) -> None:
    _require_exact_keys(
        value,
        keys={
            "schema_version", "owner", "package_root", "origin_url",
            "openmontage_commit", "git_tree", "inventory", "guide",
        },
        label="Package Registration",
    )
    if value["schema_version"] != REGISTRATION_SCHEMA or value["owner"] != REGISTRATION_OWNER:
        _fail("TAMPERED", "Package Registration schema or owner mismatch")
    _require_nonempty_string(value["package_root"], label="package_root")
    _normalize_origin_url(value["origin_url"], label="origin_url")
    _require_commit(value["openmontage_commit"], label="openmontage_commit")
    _require_commit(value["git_tree"], label="git_tree")
    inventory = _require_exact_keys(
        value["inventory"], keys={"file_count", "sha256", "entries"}, label="inventory"
    )
    count = _require_size(inventory["file_count"], label="inventory.file_count")
    _require_sha256(inventory["sha256"], label="inventory.sha256")
    entries = inventory["entries"]
    if not isinstance(entries, list) or not entries or len(entries) != count:
        _fail("INPUT_INVALID", "inventory entries do not match file_count")
    seen: set[str] = set()
    for index, entry_value in enumerate(entries):
        entry = _require_exact_keys(
            entry_value,
            keys={"path", "git_mode", "git_blob", "sha256", "size"},
            label=f"inventory[{index}]",
        )
        relative = _safe_relative(entry["path"], label=f"inventory[{index}].path")
        key = _windows_relative_path_key(relative)
        if key in seen:
            _fail("DUPLICATE", f"duplicate inventory path: {relative}")
        seen.add(key)
        if entry["git_mode"] not in {"100644", "100755"}:
            _fail("PATH_VIOLATION", f"inventory mode is not regular: {relative}")
        _require_commit(entry["git_blob"], label=f"inventory Git blob for {relative}")
        _require_sha256(entry["sha256"], label=f"inventory SHA for {relative}")
        _require_size(entry["size"], label=f"inventory size for {relative}", positive=False)
    if inventory["sha256"] != _sha256_bytes(_canonical_json({"entries": entries})):
        _fail("TAMPERED", "inventory identity mismatch")
    guide = _require_exact_keys(
        value["guide"],
        keys={"relative_path", "path", "sha256", "size", "git_mode"},
        label="guide",
    )
    if guide["relative_path"] != GUIDE_NAME or guide["git_mode"] not in {"100644", "100755"}:
        _fail("TAMPERED", "Guide identity is invalid")
    _require_nonempty_string(guide["path"], label="guide.path")
    _require_sha256(guide["sha256"], label="guide.sha256")
    _require_size(guide["size"], label="guide.size")


def _revalidate_registration(value: dict[str, Any]) -> None:
    _validate_registration_shape(value)
    root = _absolute_git_root(value["package_root"], label="PackageRoot")
    current = _collect_git_identity(
        root,
        expected_origin_url=value["origin_url"],
        expected_commit=value["openmontage_commit"],
    )
    for key in ("origin_url", "openmontage_commit", "git_tree", "inventory", "guide"):
        if value[key] != current[key]:
            _fail("TAMPERED", f"Package Registration {key} no longer matches PackageRoot")


def _registry_paths(data_root: os.PathLike[str] | str) -> _RegistryPaths:
    root = _absolute_existing_path(data_root, label="DataRoot", directory=True)
    registry = root / "State" / "PackageRegistration" / REGISTRY_VERSION
    return _RegistryPaths(
        data_root=root,
        registry_root=registry,
        objects=registry / "objects",
        active=registry / "active.json",
        lock=registry / "active.lock",
    )


def _verify_fixed_existing(path: Path, *, expected_parent: Path, label: str) -> None:
    try:
        resolved = path.resolve(strict=True)
        parent = expected_parent.resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        _fail("TAMPERED", f"{label} does not resolve: {exc}")
    if not _same_path(resolved, parent / path.name):
        _fail("TAMPERED", f"{label} is not the fixed registry object")


def _validate_lock_file(paths: _RegistryPaths) -> None:
    if not paths.lock.is_file():
        _fail("TAMPERED", "active.lock is missing")
    _verify_fixed_existing(paths.lock, expected_parent=paths.registry_root, label="active.lock")
    if _read_bytes(paths.lock, label="active.lock", stored=True) != LOCK_BYTES:
        _fail("TAMPERED", "active.lock identity bytes differ")


def _validate_registry_location(paths: _RegistryPaths) -> None:
    expected_registry = (
        paths.data_root / "State" / "PackageRegistration" / REGISTRY_VERSION
    )
    expected_objects = expected_registry / "objects"
    try:
        resolved_registry = paths.registry_root.resolve(strict=False)
        resolved_objects = paths.objects.resolve(strict=False)
    except (OSError, RuntimeError) as exc:
        _fail("TAMPERED", f"registry path does not resolve safely: {exc}")
    if not _same_path(resolved_registry, expected_registry):
        _fail("TAMPERED", "registry root escapes the fixed DataRoot location")
    if not _same_path(resolved_objects, expected_objects):
        _fail("TAMPERED", "objects directory escapes the fixed registry location")


def _ensure_register_lock(paths: _RegistryPaths) -> None:
    _validate_registry_location(paths)
    if paths.lock.exists():
        if not paths.registry_root.is_dir() or not paths.objects.is_dir():
            _fail("TAMPERED", "active.lock exists without the fixed registry directories")
        _verify_fixed_existing(paths.objects, expected_parent=paths.registry_root, label="objects directory")
        if not paths.lock.is_file():
            _fail("TAMPERED", "active.lock is not a regular file")
        _verify_fixed_existing(paths.lock, expected_parent=paths.registry_root, label="active.lock")
        return
    if paths.active.exists():
        _fail("TAMPERED", "active.lock is missing beside an active pointer")
    if paths.objects.exists():
        if not paths.objects.is_dir():
            _fail("TAMPERED", "objects registry path is not a directory")
        try:
            if any(paths.objects.iterdir()):
                _fail("TAMPERED", "active.lock is missing beside Package Registration objects")
        except OSError as exc:
            _fail("TAMPERED", f"cannot inspect Package Registration objects: {exc}")
    if paths.registry_root.exists():
        if not paths.registry_root.is_dir():
            _fail("TAMPERED", "registry root is not a directory")
        try:
            unknown = [child.name for child in paths.registry_root.iterdir() if child.name != "objects"]
        except OSError as exc:
            _fail("TAMPERED", f"cannot inspect registry root: {exc}")
        if unknown:
            _fail("TAMPERED", f"registry is not empty while active.lock is missing: {sorted(unknown)}")
    try:
        paths.objects.mkdir(parents=True, exist_ok=True)
        fd = os.open(paths.lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "wb") as handle:
            handle.write(LOCK_BYTES)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError:
        if not paths.lock.is_file():
            _fail("TAMPERED", "active.lock is not a regular file")
    except OSError as exc:
        _fail("ATOMIC_WRITE_FAILED", f"cannot initialize active.lock: {exc}")
    _verify_fixed_existing(paths.lock, expected_parent=paths.registry_root, label="active.lock")


def _ensure_existing_registry(paths: _RegistryPaths) -> None:
    _validate_registry_location(paths)
    if not paths.registry_root.is_dir() or not paths.objects.is_dir():
        _fail("OBJECT_MISSING", "Package Registration registry is missing")
    _verify_fixed_existing(paths.objects, expected_parent=paths.registry_root, label="objects directory")
    if not paths.lock.is_file():
        _fail("TAMPERED", "active.lock is missing")
    _verify_fixed_existing(paths.lock, expected_parent=paths.registry_root, label="active.lock")


def _lock_byte(handle: Any) -> None:
    handle.seek(0)
    if os.name == "nt":
        if _msvcrt is None or not hasattr(_msvcrt, "locking"):
            _fail("TAMPERED", "Windows kernel locking API is unavailable")
        _msvcrt.locking(handle.fileno(), _msvcrt.LK_NBLCK, 1)
    else:
        if _fcntl is None or not hasattr(_fcntl, "flock"):
            _fail("TAMPERED", "POSIX kernel locking API is unavailable")
        _fcntl.flock(handle.fileno(), _fcntl.LOCK_EX | _fcntl.LOCK_NB)


def _unlock_byte(handle: Any) -> None:
    handle.seek(0)
    if os.name == "nt":
        if _msvcrt is None or not hasattr(_msvcrt, "locking"):
            _fail("TAMPERED", "Windows kernel unlocking API is unavailable")
        _msvcrt.locking(handle.fileno(), _msvcrt.LK_UNLCK, 1)
    else:
        if _fcntl is None or not hasattr(_fcntl, "flock"):
            _fail("TAMPERED", "POSIX kernel unlocking API is unavailable")
        _fcntl.flock(handle.fileno(), _fcntl.LOCK_UN)


@contextmanager
def _active_lock(paths: _RegistryPaths) -> Iterator[None]:
    deadline = time.monotonic() + _ACTIVE_LOCK_TIMEOUT_SECONDS
    if not paths.lock.is_file():
        _fail("TAMPERED", "active.lock is missing")
    _verify_fixed_existing(paths.lock, expected_parent=paths.registry_root, label="active.lock")
    process_acquired = False
    while not process_acquired:
        process_acquired = _PROCESS_ACTIVE_LOCK.acquire(blocking=False)
        if process_acquired:
            break
        remaining = deadline - time.monotonic()
        if remaining <= 0:
            _fail("ACTIVE_LOCK_BUSY", "active.lock remained busy for 5.0 seconds")
        time.sleep(min(_ACTIVE_LOCK_RETRY_SECONDS, remaining))
    try:
        handle = paths.lock.open("r+b", buffering=0)
    except OSError as exc:
        _PROCESS_ACTIVE_LOCK.release()
        _fail("TAMPERED", f"cannot open active.lock: {exc}")
    acquired = False
    try:
        while True:
            try:
                _lock_byte(handle)
                acquired = True
                break
            except PackageRegistrationError:
                raise
            except (OSError, BlockingIOError):
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    _fail("ACTIVE_LOCK_BUSY", "active.lock remained busy for 5.0 seconds")
                time.sleep(min(_ACTIVE_LOCK_RETRY_SECONDS, remaining))
        handle.seek(0)
        if handle.read() != LOCK_BYTES:
            _fail("TAMPERED", "active.lock changed inside the lock critical section")
        yield
    finally:
        try:
            if acquired:
                _unlock_byte(handle)
        finally:
            handle.close()
            if process_acquired:
                _PROCESS_ACTIVE_LOCK.release()


def _publish_registration_object(path: Path, raw: bytes) -> None:
    if path.exists():
        _verify_fixed_existing(path, expected_parent=path.parent, label="Package Registration object")
        if _read_bytes(path, label="Package Registration object", stored=True) == raw:
            return
        _fail("DUPLICATE", "content-addressed object path contains different bytes")
    temp_name: str | None = None
    try:
        fd, temp_name = tempfile.mkstemp(prefix=f".{path.stem}.", suffix=".tmp", dir=path.parent)
        with os.fdopen(fd, "wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        temp_path = Path(temp_name)
        if temp_path.read_bytes() != raw:
            _fail("ATOMIC_WRITE_FAILED", "Package Registration temp readback differs")
        try:
            os.link(temp_path, path)
        except FileExistsError:
            if _read_bytes(path, label="Package Registration object", stored=True) != raw:
                _fail("DUPLICATE", "concurrent object publication used different bytes")
        if _read_bytes(path, label="Package Registration object", stored=True) != raw:
            _fail("ATOMIC_WRITE_FAILED", "Package Registration object readback differs")
    except PackageRegistrationError:
        raise
    except OSError as exc:
        _fail("ATOMIC_WRITE_FAILED", f"cannot publish Package Registration object: {exc}")
    finally:
        if temp_name is not None:
            try:
                Path(temp_name).unlink(missing_ok=True)
            except OSError:
                pass


def _load_registration(paths: _RegistryPaths, registration_sha256: str) -> dict[str, Any]:
    digest = _require_sha256(registration_sha256, label="registration_sha256")
    path = paths.objects / f"{digest}.json"
    if not path.is_file():
        _fail("OBJECT_MISSING", f"Package Registration object {digest} is missing")
    _verify_fixed_existing(path, expected_parent=paths.objects, label="Package Registration object")
    raw = _read_bytes(path, label="Package Registration object", stored=True)
    if _sha256_bytes(raw) != digest:
        _fail("TAMPERED", "Package Registration object hash differs from filename")
    value = _strict_json_bytes(raw, label="Package Registration object")
    if _canonical_json(value) != raw:
        _fail("TAMPERED", "Package Registration object bytes are not canonical")
    _revalidate_registration(value)
    return value


def _parse_active(raw: bytes) -> dict[str, Any]:
    try:
        value = _strict_json_bytes(raw, label="active package pointer")
        _require_exact_keys(
            value,
            keys={"schema_version", "owner", "registration_sha256"},
            label="active package pointer",
        )
        if value["schema_version"] != ACTIVE_POINTER_SCHEMA or value["owner"] != REGISTRATION_OWNER:
            _fail("TAMPERED", "active package pointer schema or owner mismatch")
        _require_sha256(value["registration_sha256"], label="active registration_sha256")
        if _canonical_json(value) != raw:
            _fail("TAMPERED", "active package pointer bytes are not canonical")
        return value
    except PackageRegistrationError as exc:
        if exc.code in {"DUPLICATE", "TAMPERED"}:
            raise
        _fail("TAMPERED", f"active package pointer is damaged: {exc.message}")


def _read_active_raw(paths: _RegistryPaths) -> bytes | None:
    if not paths.active.exists():
        return None
    if not paths.active.is_file():
        _fail("TAMPERED", "active package pointer is not a regular file")
    _verify_fixed_existing(paths.active, expected_parent=paths.registry_root, label="active package pointer")
    return _read_bytes(paths.active, label="active package pointer", stored=True)


def _validate_expected_pointer(value: str, *, allow_missing: bool) -> str:
    if value == "MISSING" and allow_missing:
        return value
    return _require_sha256(value, label="expected active pointer SHA-256")


def _atomic_replace_active(
    path: Path, payload: bytes, expected_current_raw: bytes | None
) -> None:
    temp_name: str | None = None
    replaced = False
    try:
        fd, temp_name = tempfile.mkstemp(prefix=".active.", suffix=".tmp", dir=path.parent)
        with os.fdopen(fd, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        temp_path = Path(temp_name)
        if temp_path.read_bytes() != payload:
            _fail("ATOMIC_WRITE_FAILED", "active pointer temp readback differs")
        current_raw = path.read_bytes() if path.exists() else None
        if current_raw != expected_current_raw:
            _fail("ACTIVE_CAS_MISMATCH", "active package pointer changed before replace")
        os.replace(temp_path, path)
        replaced = True
        if _read_bytes(path, label="active package pointer", stored=True) != payload:
            _fail("ATOMIC_WRITE_FAILED", "active package pointer readback differs")
        _parse_active(payload)
    except PackageRegistrationError:
        raise
    except OSError as exc:
        _fail("ATOMIC_WRITE_FAILED", f"cannot atomically replace active pointer: {exc}")
    finally:
        if temp_name is not None and not replaced:
            try:
                Path(temp_name).unlink(missing_ok=True)
            except OSError:
                pass


def _pointer_bytes(registration_sha256: str) -> bytes:
    return _canonical_json(
        {
            "schema_version": ACTIVE_POINTER_SCHEMA,
            "owner": REGISTRATION_OWNER,
            "registration_sha256": _require_sha256(
                registration_sha256, label="registration_sha256"
            ),
        }
    )


def register_package(
    data_root: os.PathLike[str] | str,
    package_root: os.PathLike[str] | str,
    expected_origin_url: str,
    expected_commit: str,
) -> Mapping[str, Any]:
    """Validate and immutably register one explicit official Git checkout.

    Registration never activates the package.  All candidate validation completes
    before the registry receives any write.
    """

    paths = _registry_paths(data_root)
    root = _absolute_git_root(package_root, label="PackageRoot")
    registration, raw, digest = _build_registration(
        package_root=root,
        expected_origin_url=expected_origin_url,
        expected_commit=expected_commit,
    )

    _ensure_register_lock(paths)
    with _active_lock(paths):
        paths.objects.mkdir(parents=True, exist_ok=True)
        _publish_registration_object(paths.objects / f"{digest}.json", raw)
    return _freeze({"registration_sha256": digest, **registration})


def activate_package(
    data_root: os.PathLike[str] | str,
    expected_active_pointer_sha256_or_missing: str,
    registration_sha256: str,
) -> str:
    """CAS-select an existing, fully revalidated Package Registration."""

    paths = _registry_paths(data_root)
    _ensure_existing_registry(paths)
    expected = _validate_expected_pointer(
        expected_active_pointer_sha256_or_missing, allow_missing=True
    )
    target_sha = _require_sha256(registration_sha256, label="registration_sha256")
    with _active_lock(paths):
        current_raw = _read_active_raw(paths)
        if current_raw is None:
            current_identity = "MISSING"
        else:
            current_pointer = _parse_active(current_raw)
            _load_registration(paths, current_pointer["registration_sha256"])
            current_identity = _sha256_bytes(current_raw)
        if current_identity != expected:
            _fail("ACTIVE_CAS_MISMATCH", "active package pointer changed")
        _load_registration(paths, target_sha)
        _atomic_replace_active(paths.active, _pointer_bytes(target_sha), current_raw)
    return target_sha


def recover_active_package(
    data_root: os.PathLike[str] | str,
    expected_broken_pointer_sha256: str,
    replacement_registration_sha256: str,
) -> str:
    """Replace one explicitly hash-locked broken active pointer.

    A valid active pointer is never accepted by this recovery-only entry point.
    """

    paths = _registry_paths(data_root)
    _ensure_existing_registry(paths)
    expected = _validate_expected_pointer(expected_broken_pointer_sha256, allow_missing=False)
    replacement = _require_sha256(
        replacement_registration_sha256, label="replacement_registration_sha256"
    )
    with _active_lock(paths):
        current_raw = _read_active_raw(paths)
        if current_raw is None:
            _fail("OBJECT_MISSING", "broken active package pointer is missing")
        if _sha256_bytes(current_raw) != expected:
            _fail("ACTIVE_CAS_MISMATCH", "broken active package pointer changed")
        try:
            current_pointer = _parse_active(current_raw)
            _load_registration(paths, current_pointer["registration_sha256"])
        except PackageRegistrationError:
            pass
        else:
            _fail("INPUT_INVALID", "active package pointer is valid and cannot be recovered")
        _load_registration(paths, replacement)
        _atomic_replace_active(paths.active, _pointer_bytes(replacement), current_raw)
    return replacement


def locate_active_package(data_root: os.PathLike[str] | str) -> Mapping[str, Any]:
    """Read and fully revalidate the one active OpenMontage package.

    This function performs no repair, fallback enumeration, process launch, network
    access, or filesystem write.
    """

    paths = _registry_paths(data_root)
    _ensure_existing_registry(paths)
    _validate_lock_file(paths)
    raw = _read_active_raw(paths)
    if raw is None:
        _fail("OBJECT_MISSING", "active package pointer is missing")
    pointer = _parse_active(raw)
    digest = pointer["registration_sha256"]
    registration = _load_registration(paths, digest)
    return _freeze(
        {
            "registration_sha256": digest,
            "package_root": registration["package_root"],
            "guide": registration["guide"],
            "origin_url": registration["origin_url"],
            "openmontage_commit": registration["openmontage_commit"],
            "git_tree": registration["git_tree"],
            "inventory": {
                "file_count": registration["inventory"]["file_count"],
                "sha256": registration["inventory"]["sha256"],
            },
        }
    )


__all__ = [
    "PackageRegistrationError",
    "activate_package",
    "locate_active_package",
    "recover_active_package",
    "register_package",
]
