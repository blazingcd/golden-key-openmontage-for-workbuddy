"""Fail-closed OpenMontage package registration and active-package lookup.

This module deliberately knows nothing about WorkBuddy messages, launchers, runtime
preparation, pipelines, providers, or OpenMontage production state.  Its only job is
to bind an explicitly supplied, already-installed portable package to immutable local
identity records and to locate the one package selected by an atomic pointer.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
import tempfile
import threading
import time
import unicodedata
import zipfile
from contextlib import contextmanager
from dataclasses import dataclass
from email.parser import BytesParser
from email.policy import compat32
from pathlib import Path, PurePosixPath
from types import MappingProxyType
from typing import Any, Iterator, Mapping

try:  # pragma: no cover - selected by platform
    import msvcrt as _msvcrt
except ImportError:  # pragma: no cover - selected by platform
    _msvcrt = None

try:  # pragma: no cover - selected by platform
    import fcntl as _fcntl
except ImportError:  # pragma: no cover - selected by platform
    _fcntl = None


REGISTRATION_SCHEMA = "golden-key-workbuddy-openmontage-package-registration-v2"
REGISTRATION_OWNER = "golden-key-workbuddy-shell-v2"
ACTIVE_POINTER_SCHEMA = "golden-key-workbuddy-active-openmontage-package-v1"
ACTIVE_LOCK_SCHEMA = "golden-key-workbuddy-active-package-lock-v1"
MANIFEST_SCHEMA = "golden-key-workbuddy-portable-bundle-v2"
LOCK_SCHEMA = 2
DEPENDENCY_LOCK_SCHEMA = "golden-key-workbuddy-python-core-dependencies-v1"

MANIFEST_NAME = "BUNDLE-MANIFEST.json"
LOCK_NAME = "GOLDEN_KEY_WORKBUDDY_CORE.lock.json"
GUIDE_NAME = "AGENT_GUIDE.md"
PYTHON_RELATIVE_PATH = "bootstrap/python/python.exe"
PYTHON_DEPENDENCY_LOCK_RELATIVE_PATH = "bootstrap/python/CORE-DEPENDENCIES.lock.json"
FFMPEG_RELATIVE_PATH = "bootstrap/ffmpeg/bin/ffmpeg.exe"
FFPROBE_RELATIVE_PATH = "bootstrap/ffmpeg/bin/ffprobe.exe"
NODE_RELATIVE_PATH = "bootstrap/node/node.exe"
NPM_RELATIVE_PATH = "bootstrap/node/npm.cmd"
NPX_RELATIVE_PATH = "bootstrap/node/npx.cmd"
REQUIRED_TOOLCHAIN_OWNER = "workbuddy_required_toolchain"
REQUIRED_TOOLCHAIN_ROOTS = (
    "bootstrap/python",
    "bootstrap/ffmpeg",
    "bootstrap/node",
)

MANIFEST_AUTHORITY = {
    "invocation_model": "direct_agent",
    "nested_agent_host_allowed": False,
}
LOCK_AUTHORITY = {
    "consumer": "workbuddy",
    "consumer_direct_official_sync_allowed": False,
    "invocation_model": "direct_agent",
    "nested_agent_host_allowed": False,
    "official_openmontage_role": "reviewed_upstream_baseline_only",
    "source": "golden-key-core",
}
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


def _parse_sidecar(raw: bytes, *, archive_name: str) -> str:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        _fail("INPUT_INVALID", f"SHA sidecar is not UTF-8: {exc}")
    if text.startswith("\ufeff"):
        _fail("INPUT_INVALID", "SHA sidecar must not contain a BOM")
    match = re.fullmatch(
        r"([0-9A-Fa-f]{64})(?:[ \t]+(?:\*)?([^ \t\r\n]+))?[ \t]*(?:\r?\n)?",
        text,
    )
    if match is None:
        _fail("INPUT_INVALID", "SHA sidecar must contain exactly one digest")
    named_asset = match.group(2)
    if named_asset is not None and named_asset != archive_name:
        _fail("IDENTITY_MISMATCH", "SHA sidecar asset name does not match archive")
    return match.group(1).lower()


def _validate_authorities(manifest: dict[str, Any], lock: dict[str, Any]) -> None:
    manifest_authority = _require_exact_keys(
        manifest.get("authority"),
        keys=set(MANIFEST_AUTHORITY),
        label="Manifest authority",
    )
    lock_authority = _require_exact_keys(
        lock.get("authority"),
        keys=set(LOCK_AUTHORITY),
        label="Lock authority",
    )
    if manifest_authority != MANIFEST_AUTHORITY:
        _fail("IDENTITY_MISMATCH", "Manifest authority is not direct_agent")
    if lock_authority != LOCK_AUTHORITY:
        _fail("IDENTITY_MISMATCH", "Lock authority is not the WorkBuddy contract")
    for key in ("invocation_model", "nested_agent_host_allowed"):
        if manifest_authority[key] != lock_authority[key]:
            _fail("IDENTITY_MISMATCH", f"authority {key} mismatch")


def _validate_manifest_inventory(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    entries = manifest.get("files")
    if not isinstance(entries, list) or not entries:
        _fail("INPUT_INVALID", "Manifest files must be a non-empty array")
    result: dict[str, dict[str, Any]] = {}
    seen: set[str] = set()
    for index, entry_value in enumerate(entries):
        entry = _require_object(entry_value, label=f"Manifest files[{index}]")
        relative = _safe_relative(entry.get("path"), label=f"Manifest files[{index}].path")
        key = _windows_relative_path_key(relative)
        if key in seen:
            _fail("DUPLICATE", f"duplicate Manifest path: {relative}")
        seen.add(key)
        _require_sha256(entry.get("sha256"), label=f"Manifest file {relative} sha256")
        _require_size(entry.get("size"), label=f"Manifest file {relative} size", positive=False)
        _require_nonempty_string(entry.get("owner"), label=f"Manifest file {relative} owner")
        result[relative] = entry
    return result


def _validate_lock_inventory(lock: dict[str, Any]) -> list[dict[str, Any]]:
    entries = lock.get("files")
    if not isinstance(entries, list) or not entries:
        _fail("INPUT_INVALID", "Lock files must be a non-empty array")
    expected_digest = _require_sha256(lock.get("bundle_sha256"), label="Lock bundle_sha256")
    actual_digest = _sha256_bytes(
        json.dumps(
            entries,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    )
    if actual_digest != expected_digest:
        _fail("HASH_MISMATCH", "Lock bundle_sha256 mismatch")
    seen: set[str] = set()
    normalized: list[dict[str, Any]] = []
    for index, entry_value in enumerate(entries):
        entry = _require_object(entry_value, label=f"Lock files[{index}]")
        relative = _safe_relative(entry.get("source_path"), label=f"Lock files[{index}].source_path")
        key = _windows_relative_path_key(relative)
        if key in seen:
            _fail("DUPLICATE", f"duplicate Lock source_path: {relative}")
        seen.add(key)
        _require_sha256(entry.get("sha256"), label=f"Lock file {relative} sha256")
        _require_size(entry.get("size"), label=f"Lock file {relative} size", positive=False)
        normalized.append(entry)
    return normalized


def _normalized_distribution_name(value: str) -> str:
    return re.sub(r"[-_.]+", "-", value).lower()


def _required_tool_identity(
    *,
    package_root: Path,
    manifest_files: Mapping[str, dict[str, Any]],
    relative: Any,
    expected_relative: str,
    label: str,
) -> dict[str, Any]:
    normalized = _safe_relative(relative, label=f"{label} relative path")
    if normalized != expected_relative:
        _fail("IDENTITY_MISMATCH", f"{label} is not at its fixed Package path")
    entry = manifest_files.get(normalized)
    if entry is None or entry.get("owner") != REQUIRED_TOOLCHAIN_OWNER:
        _fail("IDENTITY_MISMATCH", f"{label} is not owned by required toolchain")
    path = _fixed_child(package_root, normalized, label=label)
    _validate_file_identity(
        path,
        expected_sha256=entry["sha256"],
        expected_size=entry["size"],
        label=label,
    )
    return {
        "relative_path": normalized,
        "path": str(path),
        "sha256": entry["sha256"],
        "size": entry["size"],
    }


def _reject_required_toolchain_reparse(path: Path, *, label: str) -> None:
    try:
        status = path.lstat()
        is_junction = getattr(path, "is_junction", None)
        junction = bool(is_junction()) if callable(is_junction) else False
    except (OSError, RuntimeError) as exc:
        _fail("PATH_VIOLATION", f"{label} cannot be inspected safely: {exc}")
    reparse_flag = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    file_attributes = getattr(status, "st_file_attributes", 0)
    if path.is_symlink() or junction or bool(file_attributes & reparse_flag):
        _fail("PATH_VIOLATION", f"{label} must not be a symlink, junction, or reparse point")


def _resolve_required_toolchain_path(
    path: Path, *, package_root: Path, label: str
) -> Path:
    _reject_required_toolchain_reparse(path, label=label)
    try:
        resolved = path.resolve(strict=True)
        resolved.relative_to(package_root)
    except (OSError, RuntimeError, ValueError) as exc:
        _fail("PATH_VIOLATION", f"{label} does not resolve inside PackageRoot: {exc}")
    return resolved


def _actual_toolchain_files(package_root: Path) -> set[str]:
    actual: set[str] = set()
    seen_keys: set[str] = set()
    for root_relative in REQUIRED_TOOLCHAIN_ROOTS:
        root = package_root.joinpath(*PurePosixPath(root_relative).parts)
        resolved_root = _resolve_required_toolchain_path(
            root,
            package_root=package_root,
            label=f"required toolchain root {root_relative}",
        )
        if not resolved_root.is_dir():
            _fail("PATH_VIOLATION", f"required toolchain root is not a directory: {root_relative}")
        try:
            def walk_error(error: OSError) -> None:
                _fail("PATH_VIOLATION", f"required toolchain cannot be enumerated: {error}")

            walker = os.walk(resolved_root, followlinks=False, onerror=walk_error)
            for directory, directory_names, file_names in walker:
                directory_path = Path(directory)
                _resolve_required_toolchain_path(
                    directory_path,
                    package_root=package_root,
                    label="required toolchain directory",
                )
                for child_name in directory_names:
                    child = directory_path / child_name
                    _resolve_required_toolchain_path(
                        child,
                        package_root=package_root,
                        label="required toolchain child directory",
                    )
                for file_name in file_names:
                    path = directory_path / file_name
                    resolved = _resolve_required_toolchain_path(
                        path,
                        package_root=package_root,
                        label="required toolchain file",
                    )
                    relative = resolved.relative_to(package_root).as_posix()
                    if not resolved.is_file():
                        _fail("PATH_VIOLATION", f"required toolchain object is not a file: {relative}")
                    key = _windows_relative_path_key(relative)
                    if key in seen_keys:
                        _fail("DUPLICATE", f"required toolchain file alias collision: {relative}")
                    seen_keys.add(key)
                    actual.add(relative)
        except PackageRegistrationError:
            raise
        except OSError as exc:
            _fail("OBJECT_MISSING", f"cannot enumerate required toolchain: {exc}")
    return actual


def _validate_dependency_lock(
    *,
    package_root: Path,
    lock_identity: Mapping[str, Any],
    expected_python_version: str,
    managed_files: set[str],
) -> tuple[dict[str, Any], ...]:
    raw = _read_bytes(Path(lock_identity["path"]), label="Python dependency lock")
    dependency_lock = _strict_json_bytes(raw, label="Python dependency lock")
    _require_exact_keys(
        dependency_lock,
        keys={"schema_version", "python_version", "requirements", "packages"},
        label="Python dependency lock",
    )
    if dependency_lock["schema_version"] != DEPENDENCY_LOCK_SCHEMA:
        _fail("IDENTITY_MISMATCH", "unsupported Python dependency lock schema")
    if dependency_lock["python_version"] != expected_python_version:
        _fail("IDENTITY_MISMATCH", "Python dependency lock version differs from interpreter")
    requirements = dependency_lock["requirements"]
    if not isinstance(requirements, list) or not requirements:
        _fail("INPUT_INVALID", "Python dependency lock requirements must be non-empty")
    for index, requirement in enumerate(requirements):
        _require_nonempty_string(requirement, label=f"Python dependency requirement[{index}]")
    packages = dependency_lock["packages"]
    if not isinstance(packages, list) or not packages:
        _fail("INPUT_INVALID", "Python dependency lock packages must be non-empty")
    seen_names: set[str] = set()
    metadata_paths: set[str] = set()
    normalized_packages: list[dict[str, Any]] = []
    for index, package_value in enumerate(packages):
        package = _require_exact_keys(
            package_value,
            keys={"name", "version", "metadata_path"},
            label=f"Python dependency lock packages[{index}]",
        )
        name = _require_nonempty_string(package["name"], label="dependency package name")
        version = _require_nonempty_string(package["version"], label="dependency package version")
        name_key = _normalized_distribution_name(name)
        if name_key in seen_names:
            _fail("DUPLICATE", f"duplicate locked Python distribution: {name}")
        seen_names.add(name_key)
        metadata_relative = _safe_relative(
            package["metadata_path"], label=f"dependency {name} metadata_path"
        )
        if not metadata_relative.startswith("bootstrap/python/Lib/site-packages/") or not metadata_relative.endswith(
            ".dist-info/METADATA"
        ):
            _fail("PATH_VIOLATION", f"dependency {name} metadata_path is outside fixed site-packages")
        metadata_key = _windows_relative_path_key(metadata_relative)
        if any(_windows_relative_path_key(item) == metadata_key for item in metadata_paths):
            _fail("DUPLICATE", f"duplicate dependency metadata path: {metadata_relative}")
        metadata_paths.add(metadata_relative)
        if metadata_relative not in managed_files:
            _fail("IDENTITY_MISMATCH", f"dependency {name} metadata is not managed")
        metadata_path = _fixed_child(package_root, metadata_relative, label=f"dependency {name} metadata")
        try:
            message = BytesParser(policy=compat32).parsebytes(
                _read_bytes(metadata_path, label=f"dependency {name} metadata")
            )
        except (ValueError, TypeError) as exc:
            _fail("INPUT_INVALID", f"dependency {name} metadata cannot be parsed: {exc}")
        actual_name = message.get("Name")
        actual_version = message.get("Version")
        if not isinstance(actual_name, str) or _normalized_distribution_name(actual_name) != name_key:
            _fail("IDENTITY_MISMATCH", f"dependency {name} installed metadata name differs")
        if actual_version != version:
            _fail("IDENTITY_MISMATCH", f"dependency {name} installed version differs")
        normalized_packages.append(
            {"name": name, "version": version, "metadata_path": metadata_relative}
        )
    actual_metadata = {
        item
        for item in managed_files
        if item.startswith("bootstrap/python/Lib/site-packages/")
        and item.endswith(".dist-info/METADATA")
    }
    if actual_metadata != metadata_paths:
        _fail("IDENTITY_MISMATCH", "Python dependency lock does not cover installed distributions")
    return tuple(normalized_packages)


def _validate_manifest_and_lock(
    *,
    package_root: Path,
    package_python: Path,
    manifest_bytes: bytes,
    lock_bytes: bytes,
) -> dict[str, Any]:
    manifest = _strict_json_bytes(manifest_bytes, label="Manifest")
    lock = _strict_json_bytes(lock_bytes, label="Lock")
    if manifest.get("schema_version") != MANIFEST_SCHEMA:
        _fail("IDENTITY_MISMATCH", "unsupported Manifest schema_version")
    if type(lock.get("schema_version")) is not int or lock["schema_version"] != LOCK_SCHEMA:
        _fail("IDENTITY_MISMATCH", "unsupported Lock schema_version")

    _validate_authorities(manifest, lock)
    core = _require_object(manifest.get("core"), label="Manifest core")
    contract_id = _require_nonempty_string(core.get("contract_id"), label="Manifest core.contract_id")
    openmontage_release = _require_nonempty_string(core.get("tag"), label="Manifest core.tag")
    openmontage_commit = _require_commit(core.get("source_commit"), label="Manifest core.source_commit")
    file_count = _require_size(core.get("file_count"), label="Manifest core.file_count")

    if lock.get("contract_id") != contract_id:
        _fail("IDENTITY_MISMATCH", "Manifest and Lock contract_id differ")
    if lock.get("source_ref") != openmontage_release:
        _fail("IDENTITY_MISMATCH", "Manifest tag and Lock source_ref differ")
    if lock.get("source_commit") != openmontage_commit:
        _fail("IDENTITY_MISMATCH", "Manifest and Lock source_commit differ")

    manifest_files = _validate_manifest_inventory(manifest)
    lock_files = _validate_lock_inventory(lock)
    if file_count != len(lock_files):
        _fail("IDENTITY_MISMATCH", "Manifest core.file_count does not match Lock files")

    for entry in lock_files:
        relative = entry["source_path"]
        manifest_entry = manifest_files.get(relative)
        if manifest_entry is None or manifest_entry.get("owner") != "managed_core":
            _fail("IDENTITY_MISMATCH", f"managed_core Manifest entry missing for {relative}")
        if manifest_entry["sha256"] != entry["sha256"] or manifest_entry["size"] != entry["size"]:
            _fail("IDENTITY_MISMATCH", f"Manifest and Lock identity differ for {relative}")
        installed = _fixed_child(package_root, relative, label=f"managed file {relative}")
        _validate_file_identity(
            installed,
            expected_sha256=entry["sha256"],
            expected_size=entry["size"],
            label=f"managed file {relative}",
        )

    guide_entry = manifest_files.get(GUIDE_NAME)
    if guide_entry is None or guide_entry.get("owner") != "managed_core":
        _fail("IDENTITY_MISMATCH", "Guide must be a unique managed_core Manifest file")
    if not any(entry["source_path"] == GUIDE_NAME for entry in lock_files):
        _fail("IDENTITY_MISMATCH", "Guide must be locked by the Lock inventory")

    lock_entry = manifest_files.get(LOCK_NAME)
    if lock_entry is None or lock_entry.get("owner") != "core_contract":
        _fail("IDENTITY_MISMATCH", "Lock must be a unique core_contract Manifest file")
    actual_lock_path = _fixed_child(package_root, LOCK_NAME, label="installed Lock")
    _validate_file_identity(
        actual_lock_path,
        expected_sha256=lock_entry["sha256"],
        expected_size=lock_entry["size"],
        label="installed Lock",
    )

    installation = _require_object(manifest.get("installation"), label="Manifest installation")
    roles = _require_exact_keys(
        installation.get("runtime_roles"),
        keys={"python", "ffmpeg", "node"},
        label="Manifest installation.runtime_roles",
    )
    if roles != {
        "python": "bundled_private_interpreter",
        "ffmpeg": "bundled_media_toolchain",
        "node": "bundled_javascript_toolchain",
    }:
        _fail("IDENTITY_MISMATCH", "Manifest required toolchain runtime roles differ")

    toolchain = _require_exact_keys(
        manifest.get("required_toolchain"),
        keys={"python", "ffmpeg", "node", "managed_files"},
        label="Manifest required_toolchain",
    )
    managed_values = toolchain["managed_files"]
    if not isinstance(managed_values, list) or not managed_values:
        _fail("INPUT_INVALID", "required_toolchain.managed_files must be non-empty")
    managed_files: set[str] = set()
    managed_keys: set[str] = set()
    for index, value in enumerate(managed_values):
        relative = _safe_relative(value, label=f"required toolchain managed_files[{index}]")
        key = _windows_relative_path_key(relative)
        if key in managed_keys:
            _fail("DUPLICATE", f"duplicate required toolchain managed file: {relative}")
        managed_keys.add(key)
        managed_files.add(relative)
    manifest_owned = {
        relative
        for relative, entry in manifest_files.items()
        if entry.get("owner") == REQUIRED_TOOLCHAIN_OWNER
    }
    if managed_files != manifest_owned:
        _fail("IDENTITY_MISMATCH", "required toolchain managed list differs from Manifest ownership")
    actual_files = _actual_toolchain_files(package_root)
    if actual_files != managed_files:
        missing = sorted(managed_files - actual_files)
        unknown = sorted(actual_files - managed_files)
        _fail(
            "IDENTITY_MISMATCH",
            f"required toolchain file closure differs; missing={missing}, unknown={unknown}",
        )
    for relative in sorted(managed_files):
        entry = manifest_files[relative]
        path = _fixed_child(package_root, relative, label=f"required toolchain file {relative}")
        _validate_file_identity(
            path,
            expected_sha256=entry["sha256"],
            expected_size=entry["size"],
            label=f"required toolchain file {relative}",
        )

    python_metadata = _require_exact_keys(
        toolchain["python"],
        keys={
            "version",
            "source",
            "source_archive_sha256",
            "source_archive_size",
            "system_python_required",
            "executable",
            "dependency_lock",
        },
        label="Manifest required_toolchain.python",
    )
    python_version = _require_nonempty_string(
        python_metadata["version"], label="bundled Python version"
    )
    if python_metadata["source"] != "python.org_windows_embeddable_x64":
        _fail("IDENTITY_MISMATCH", "bundled Python source is not python.org Windows embeddable")
    python_archive_sha256 = _require_sha256(
        python_metadata["source_archive_sha256"], label="bundled Python source archive SHA-256"
    )
    python_archive_size = _require_size(
        python_metadata["source_archive_size"], label="bundled Python source archive size"
    )
    if python_metadata["system_python_required"] is not False:
        _fail("IDENTITY_MISMATCH", "bundled Python must not require system Python")
    python_identity = _required_tool_identity(
        package_root=package_root,
        manifest_files=manifest_files,
        relative=python_metadata["executable"],
        expected_relative=PYTHON_RELATIVE_PATH,
        label="bundled Python",
    )
    if not _same_path(package_python, python_identity["path"]):
        _fail("IDENTITY_MISMATCH", "package_python is not the Manifest bundled Python")
    dependency_lock_identity = _required_tool_identity(
        package_root=package_root,
        manifest_files=manifest_files,
        relative=python_metadata["dependency_lock"],
        expected_relative=PYTHON_DEPENDENCY_LOCK_RELATIVE_PATH,
        label="Python dependency lock",
    )
    dependencies = _validate_dependency_lock(
        package_root=package_root,
        lock_identity=dependency_lock_identity,
        expected_python_version=python_version,
        managed_files=managed_files,
    )

    ffmpeg_metadata = _require_exact_keys(
        toolchain["ffmpeg"],
        keys={
            "version",
            "source",
            "source_archive_sha256",
            "source_archive_size",
            "ffmpeg",
            "ffprobe",
        },
        label="Manifest required_toolchain.ffmpeg",
    )
    ffmpeg_version = _require_nonempty_string(
        ffmpeg_metadata["version"], label="bundled FFmpeg version"
    )
    if ffmpeg_metadata["source"] != "gyan.dev_ffmpeg_release_essentials_x64":
        _fail("IDENTITY_MISMATCH", "bundled FFmpeg source differs")
    ffmpeg_archive_sha256 = _require_sha256(
        ffmpeg_metadata["source_archive_sha256"], label="FFmpeg source archive SHA-256"
    )
    ffmpeg_archive_size = _require_size(
        ffmpeg_metadata["source_archive_size"], label="FFmpeg source archive size"
    )
    ffmpeg_identity = _required_tool_identity(
        package_root=package_root,
        manifest_files=manifest_files,
        relative=ffmpeg_metadata["ffmpeg"],
        expected_relative=FFMPEG_RELATIVE_PATH,
        label="bundled FFmpeg",
    )
    ffprobe_identity = _required_tool_identity(
        package_root=package_root,
        manifest_files=manifest_files,
        relative=ffmpeg_metadata["ffprobe"],
        expected_relative=FFPROBE_RELATIVE_PATH,
        label="bundled ffprobe",
    )

    node_metadata = _require_exact_keys(
        toolchain["node"],
        keys={
            "version",
            "source",
            "source_archive_sha256",
            "source_archive_size",
            "node",
            "npm",
            "npx",
        },
        label="Manifest required_toolchain.node",
    )
    node_version = _require_nonempty_string(node_metadata["version"], label="bundled Node version")
    if node_metadata["source"] != "npmmirror_node_windows_x64":
        _fail("IDENTITY_MISMATCH", "bundled Node source differs")
    node_archive_sha256 = _require_sha256(
        node_metadata["source_archive_sha256"], label="Node source archive SHA-256"
    )
    node_archive_size = _require_size(
        node_metadata["source_archive_size"], label="Node source archive size"
    )
    node_identity = _required_tool_identity(
        package_root=package_root,
        manifest_files=manifest_files,
        relative=node_metadata["node"],
        expected_relative=NODE_RELATIVE_PATH,
        label="bundled Node",
    )
    npm_identity = _required_tool_identity(
        package_root=package_root,
        manifest_files=manifest_files,
        relative=node_metadata["npm"],
        expected_relative=NPM_RELATIVE_PATH,
        label="bundled npm",
    )
    npx_identity = _required_tool_identity(
        package_root=package_root,
        manifest_files=manifest_files,
        relative=node_metadata["npx"],
        expected_relative=NPX_RELATIVE_PATH,
        label="bundled npx",
    )

    manifest_path = _fixed_child(package_root, MANIFEST_NAME, label="installed Manifest")
    guide_path = _fixed_child(package_root, GUIDE_NAME, label="installed Guide")
    manifest_sha256, manifest_size = _file_hash_size(manifest_path, label="installed Manifest")
    lock_sha256, lock_size = _file_hash_size(actual_lock_path, label="installed Lock")
    guide_sha256, guide_size = _file_hash_size(guide_path, label="installed Guide")
    if min(manifest_size, lock_size, guide_size, python_identity["size"]) <= 0:
        _fail("INPUT_INVALID", "Manifest, Lock, Guide, and required toolchain must be non-empty")

    return {
        "contract_id": contract_id,
        "openmontage_release": openmontage_release,
        "openmontage_commit": openmontage_commit,
        "authority": {
            "manifest": dict(MANIFEST_AUTHORITY),
            "lock": dict(LOCK_AUTHORITY),
        },
        "package_python": {
            **python_identity,
            "version": python_version,
            "source": python_metadata["source"],
            "source_archive_sha256": python_archive_sha256,
        },
        "required_toolchain": {
            "python": {
                **python_identity,
                "version": python_version,
                "source": python_metadata["source"],
                "source_archive_sha256": python_archive_sha256,
                "source_archive_size": python_archive_size,
                "dependency_lock": dependency_lock_identity,
                "dependencies": list(dependencies),
            },
            "ffmpeg": {
                "version": ffmpeg_version,
                "source": ffmpeg_metadata["source"],
                "source_archive_sha256": ffmpeg_archive_sha256,
                "source_archive_size": ffmpeg_archive_size,
                "ffmpeg": ffmpeg_identity,
                "ffprobe": ffprobe_identity,
            },
            "node": {
                "version": node_version,
                "source": node_metadata["source"],
                "source_archive_sha256": node_archive_sha256,
                "source_archive_size": node_archive_size,
                "node": node_identity,
                "npm": npm_identity,
                "npx": npx_identity,
            },
        },
        "manifest": {
            "relative_path": MANIFEST_NAME,
            "path": str(manifest_path),
            "schema_version": MANIFEST_SCHEMA,
            "sha256": manifest_sha256,
            "size": manifest_size,
        },
        "lock": {
            "relative_path": LOCK_NAME,
            "path": str(actual_lock_path),
            "schema_version": LOCK_SCHEMA,
            "sha256": lock_sha256,
            "size": lock_size,
            "bundle_sha256": lock["bundle_sha256"],
        },
        "guide": {
            "relative_path": GUIDE_NAME,
            "path": str(guide_path),
            "sha256": guide_sha256,
            "size": guide_size,
        },
    }


def _validate_archive_members(
    archive_path: Path, *, manifest_bytes: bytes, lock_bytes: bytes
) -> None:
    try:
        archive = zipfile.ZipFile(archive_path)
    except (OSError, zipfile.BadZipFile) as exc:
        _fail("INPUT_INVALID", f"invalid Release archive: {exc}")
    with archive:
        seen: set[str] = set()
        manifest_infos: list[zipfile.ZipInfo] = []
        lock_infos: list[zipfile.ZipInfo] = []
        for info in archive.infolist():
            candidate = info.filename[:-1] if info.is_dir() and info.filename.endswith("/") else info.filename
            if not candidate:
                continue
            relative = _safe_relative(candidate, label="Release archive member")
            key = _windows_relative_path_key(relative)
            if key in seen:
                _fail("DUPLICATE", f"duplicate Release archive member: {relative}")
            seen.add(key)
            mode = (info.external_attr >> 16) & 0xFFFF
            if mode and stat.S_ISLNK(mode):
                _fail("PATH_VIOLATION", f"Release archive symlink is forbidden: {relative}")
            if not info.is_dir() and PurePosixPath(relative).name == MANIFEST_NAME:
                manifest_infos.append(info)
            if not info.is_dir() and PurePosixPath(relative).name == LOCK_NAME:
                lock_infos.append(info)
        if len(manifest_infos) != 1 or len(lock_infos) != 1:
            code = "DUPLICATE" if len(manifest_infos) > 1 or len(lock_infos) > 1 else "OBJECT_MISSING"
            _fail(code, "Release archive must contain exactly one Manifest and one Lock")
        try:
            archived_manifest = archive.read(manifest_infos[0])
            archived_lock = archive.read(lock_infos[0])
        except (OSError, RuntimeError, zipfile.BadZipFile) as exc:
            _fail("INPUT_INVALID", f"cannot read Release archive identities: {exc}")
        if archived_manifest != manifest_bytes:
            _fail("HASH_MISMATCH", "archived Manifest differs from installed Manifest")
        if archived_lock != lock_bytes:
            _fail("HASH_MISMATCH", "archived Lock differs from installed Lock")


def _build_registration(
    *,
    release_archive: Path,
    release_sha256_sidecar: Path,
    package_root: Path,
    package_python: Path,
) -> tuple[dict[str, Any], bytes, str]:
    if release_archive.suffix.lower() != ".zip" or release_archive.name != Path(release_archive.name).name:
        _fail("INPUT_INVALID", "Release archive must have a basename ending in .zip")
    if release_sha256_sidecar.name != f"{release_archive.name}.sha256":
        _fail("IDENTITY_MISMATCH", "Release SHA sidecar basename is not archive.zip.sha256")

    manifest_path = _fixed_child(package_root, MANIFEST_NAME, label="installed Manifest")
    lock_path = _fixed_child(package_root, LOCK_NAME, label="installed Lock")
    manifest_bytes = _read_bytes(manifest_path, label="installed Manifest")
    lock_bytes = _read_bytes(lock_path, label="installed Lock")
    facts = _validate_manifest_and_lock(
        package_root=package_root,
        package_python=package_python,
        manifest_bytes=manifest_bytes,
        lock_bytes=lock_bytes,
    )
    _validate_archive_members(
        release_archive, manifest_bytes=manifest_bytes, lock_bytes=lock_bytes
    )
    archive_sha256, archive_size = _file_hash_size(release_archive, label="Release archive")
    if archive_size <= 0:
        _fail("INPUT_INVALID", "Release archive must be non-empty")
    sidecar_digest = _parse_sidecar(
        _read_bytes(release_sha256_sidecar, label="Release SHA sidecar"),
        archive_name=release_archive.name,
    )
    if sidecar_digest != archive_sha256:
        _fail("HASH_MISMATCH", "Release archive and SHA sidecar differ")

    registration: dict[str, Any] = {
        "schema_version": REGISTRATION_SCHEMA,
        "owner": REGISTRATION_OWNER,
        "contract_id": facts["contract_id"],
        "openmontage_release": facts["openmontage_release"],
        "openmontage_commit": facts["openmontage_commit"],
        "authority": facts["authority"],
        "release": {
            "asset_name": release_archive.name,
            "archive_sha256": archive_sha256,
            "sha256_sidecar_name": release_sha256_sidecar.name,
        },
        "package_root": str(package_root),
        "package_python": facts["package_python"],
        "required_toolchain": facts["required_toolchain"],
        "manifest": facts["manifest"],
        "lock": facts["lock"],
        "guide": facts["guide"],
    }
    raw = _canonical_json(registration)
    return registration, raw, _sha256_bytes(raw)


def _validate_stored_file_identity_shape(
    value: Any, *, expected_relative: str, label: str
) -> dict[str, Any]:
    identity = _require_exact_keys(
        value,
        keys={"relative_path", "path", "sha256", "size"},
        label=f"Package Registration {label}",
    )
    if identity["relative_path"] != expected_relative:
        _fail("TAMPERED", f"Package Registration {label} relative path differs")
    _require_nonempty_string(identity["path"], label=f"registered {label} path")
    _require_sha256(identity["sha256"], label=f"registered {label} SHA-256")
    _require_size(identity["size"], label=f"registered {label} size")
    return identity


def _validate_registration_shape(value: dict[str, Any]) -> None:
    _require_exact_keys(
        value,
        keys={
            "schema_version",
            "owner",
            "contract_id",
            "openmontage_release",
            "openmontage_commit",
            "authority",
            "release",
            "package_root",
            "package_python",
            "required_toolchain",
            "manifest",
            "lock",
            "guide",
        },
        label="Package Registration",
    )
    if value["schema_version"] != REGISTRATION_SCHEMA or value["owner"] != REGISTRATION_OWNER:
        _fail("TAMPERED", "Package Registration schema or owner mismatch")
    _require_nonempty_string(value["contract_id"], label="Package Registration contract_id")
    _require_nonempty_string(value["openmontage_release"], label="Package Registration openmontage_release")
    _require_commit(value["openmontage_commit"], label="Package Registration openmontage_commit")
    authority = _require_exact_keys(
        value["authority"], keys={"manifest", "lock"}, label="Package Registration authority"
    )
    manifest_authority = _require_exact_keys(
        authority["manifest"], keys=set(MANIFEST_AUTHORITY), label="Package Registration Manifest authority"
    )
    lock_authority = _require_exact_keys(
        authority["lock"], keys=set(LOCK_AUTHORITY), label="Package Registration Lock authority"
    )
    if manifest_authority != MANIFEST_AUTHORITY or lock_authority != LOCK_AUTHORITY:
        _fail("TAMPERED", "Package Registration authority mismatch")

    release = _require_exact_keys(
        value["release"],
        keys={"asset_name", "archive_sha256", "sha256_sidecar_name"},
        label="Package Registration release",
    )
    asset_name = _require_nonempty_string(release["asset_name"], label="release asset_name")
    if Path(asset_name).name != asset_name or not asset_name.lower().endswith(".zip"):
        _fail("TAMPERED", "release asset_name is not a ZIP basename")
    _require_sha256(release["archive_sha256"], label="release archive_sha256")
    if release["sha256_sidecar_name"] != f"{asset_name}.sha256":
        _fail("TAMPERED", "release sidecar name mismatch")

    python_value = _require_exact_keys(
        value["package_python"],
        keys={
            "relative_path",
            "path",
            "sha256",
            "size",
            "version",
            "source",
            "source_archive_sha256",
        },
        label="Package Registration package_python",
    )
    if python_value["relative_path"] != PYTHON_RELATIVE_PATH:
        _fail("TAMPERED", "package_python relative_path mismatch")
    _require_nonempty_string(python_value["path"], label="package_python path")
    _require_sha256(python_value["sha256"], label="package_python sha256")
    _require_size(python_value["size"], label="package_python size")
    _require_nonempty_string(python_value["version"], label="package_python version")
    if python_value["source"] != "python.org_windows_embeddable_x64":
        _fail("TAMPERED", "package_python source mismatch")
    _require_sha256(python_value["source_archive_sha256"], label="package_python source_archive_sha256")

    toolchain_value = _require_exact_keys(
        value["required_toolchain"],
        keys={"python", "ffmpeg", "node"},
        label="Package Registration required_toolchain",
    )
    toolchain_python = _require_exact_keys(
        toolchain_value["python"],
        keys={
            "relative_path",
            "path",
            "sha256",
            "size",
            "version",
            "source",
            "source_archive_sha256",
            "source_archive_size",
            "dependency_lock",
            "dependencies",
        },
        label="Package Registration required_toolchain.python",
    )
    for key in ("relative_path", "path", "sha256", "size", "version", "source", "source_archive_sha256"):
        if toolchain_python[key] != python_value[key]:
            _fail("TAMPERED", "required_toolchain Python differs from package_python compatibility field")
    _require_size(toolchain_python["source_archive_size"], label="Python source archive size")
    dependency_lock = _validate_stored_file_identity_shape(
        toolchain_python["dependency_lock"],
        expected_relative=PYTHON_DEPENDENCY_LOCK_RELATIVE_PATH,
        label="Python dependency lock",
    )
    dependencies = toolchain_python["dependencies"]
    if not isinstance(dependencies, list) or not dependencies:
        _fail("INPUT_INVALID", "registered Python dependencies must be non-empty")
    seen_dependencies: set[str] = set()
    for index, dependency_value in enumerate(dependencies):
        dependency = _require_exact_keys(
            dependency_value,
            keys={"name", "version", "metadata_path"},
            label=f"registered Python dependency[{index}]",
        )
        name = _require_nonempty_string(dependency["name"], label="registered dependency name")
        _require_nonempty_string(dependency["version"], label="registered dependency version")
        normalized_name = _normalized_distribution_name(name)
        if normalized_name in seen_dependencies:
            _fail("DUPLICATE", f"duplicate registered Python dependency: {name}")
        seen_dependencies.add(normalized_name)
        _safe_relative(dependency["metadata_path"], label="registered dependency metadata_path")

    ffmpeg_value = _require_exact_keys(
        toolchain_value["ffmpeg"],
        keys={
            "version",
            "source",
            "source_archive_sha256",
            "source_archive_size",
            "ffmpeg",
            "ffprobe",
        },
        label="Package Registration required_toolchain.ffmpeg",
    )
    _require_nonempty_string(ffmpeg_value["version"], label="registered FFmpeg version")
    if ffmpeg_value["source"] != "gyan.dev_ffmpeg_release_essentials_x64":
        _fail("TAMPERED", "registered FFmpeg source differs")
    _require_sha256(ffmpeg_value["source_archive_sha256"], label="FFmpeg source archive SHA-256")
    _require_size(ffmpeg_value["source_archive_size"], label="FFmpeg source archive size")
    _validate_stored_file_identity_shape(
        ffmpeg_value["ffmpeg"], expected_relative=FFMPEG_RELATIVE_PATH, label="FFmpeg"
    )
    _validate_stored_file_identity_shape(
        ffmpeg_value["ffprobe"], expected_relative=FFPROBE_RELATIVE_PATH, label="ffprobe"
    )

    node_value = _require_exact_keys(
        toolchain_value["node"],
        keys={
            "version",
            "source",
            "source_archive_sha256",
            "source_archive_size",
            "node",
            "npm",
            "npx",
        },
        label="Package Registration required_toolchain.node",
    )
    _require_nonempty_string(node_value["version"], label="registered Node version")
    if node_value["source"] != "npmmirror_node_windows_x64":
        _fail("TAMPERED", "registered Node source differs")
    _require_sha256(node_value["source_archive_sha256"], label="Node source archive SHA-256")
    _require_size(node_value["source_archive_size"], label="Node source archive size")
    _validate_stored_file_identity_shape(
        node_value["node"], expected_relative=NODE_RELATIVE_PATH, label="Node"
    )
    _validate_stored_file_identity_shape(
        node_value["npm"], expected_relative=NPM_RELATIVE_PATH, label="npm"
    )
    _validate_stored_file_identity_shape(
        node_value["npx"], expected_relative=NPX_RELATIVE_PATH, label="npx"
    )

    manifest_value = _require_exact_keys(
        value["manifest"],
        keys={"relative_path", "path", "schema_version", "sha256", "size"},
        label="Package Registration manifest",
    )
    if manifest_value["relative_path"] != MANIFEST_NAME or manifest_value["schema_version"] != MANIFEST_SCHEMA:
        _fail("TAMPERED", "Package Registration Manifest identity mismatch")
    _require_nonempty_string(manifest_value["path"], label="manifest path")
    _require_sha256(manifest_value["sha256"], label="manifest sha256")
    _require_size(manifest_value["size"], label="manifest size")

    lock_value = _require_exact_keys(
        value["lock"],
        keys={"relative_path", "path", "schema_version", "sha256", "size", "bundle_sha256"},
        label="Package Registration lock",
    )
    if lock_value["relative_path"] != LOCK_NAME or type(lock_value["schema_version"]) is not int or lock_value["schema_version"] != LOCK_SCHEMA:
        _fail("TAMPERED", "Package Registration Lock identity mismatch")
    _require_nonempty_string(lock_value["path"], label="lock path")
    _require_sha256(lock_value["sha256"], label="lock sha256")
    _require_size(lock_value["size"], label="lock size")
    _require_sha256(lock_value["bundle_sha256"], label="lock bundle_sha256")

    guide_value = _require_exact_keys(
        value["guide"],
        keys={"relative_path", "path", "sha256", "size"},
        label="Package Registration guide",
    )
    if guide_value["relative_path"] != GUIDE_NAME:
        _fail("TAMPERED", "Package Registration Guide identity mismatch")
    _require_nonempty_string(guide_value["path"], label="guide path")
    _require_sha256(guide_value["sha256"], label="guide sha256")
    _require_size(guide_value["size"], label="guide size")


def _revalidate_registration(value: dict[str, Any]) -> None:
    _validate_registration_shape(value)
    package_root_text = _require_nonempty_string(value["package_root"], label="package_root")
    package_root = _absolute_existing_path(package_root_text, label="PackageRoot", directory=True)
    if not _same_path(package_root_text, package_root):
        _fail("TAMPERED", "Package Registration PackageRoot is not canonical")
    package_python = _absolute_existing_path(
        value["package_python"]["path"], label="Package Python"
    )
    if not _same_path(value["package_python"]["path"], package_python):
        _fail("TAMPERED", "Package Registration package_python path is not canonical")

    expected_paths = {
        "package_python": _fixed_child(package_root, PYTHON_RELATIVE_PATH, label="bundled Python"),
        "manifest": _fixed_child(package_root, MANIFEST_NAME, label="installed Manifest"),
        "lock": _fixed_child(package_root, LOCK_NAME, label="installed Lock"),
        "guide": _fixed_child(package_root, GUIDE_NAME, label="installed Guide"),
    }
    for key, path in expected_paths.items():
        stored_path = value["package_python"]["path"] if key == "package_python" else value[key]["path"]
        if not _same_path(stored_path, path):
            _fail("TAMPERED", f"Package Registration {key} path mismatch")
        stored = value["package_python"] if key == "package_python" else value[key]
        _validate_file_identity(
            path,
            expected_sha256=stored["sha256"],
            expected_size=stored["size"],
            label=f"Package Registration {key}",
        )

    manifest_bytes = _read_bytes(expected_paths["manifest"], label="installed Manifest", stored=True)
    lock_bytes = _read_bytes(expected_paths["lock"], label="installed Lock", stored=True)
    facts = _validate_manifest_and_lock(
        package_root=package_root,
        package_python=package_python,
        manifest_bytes=manifest_bytes,
        lock_bytes=lock_bytes,
    )
    comparisons = {
        "contract_id": facts["contract_id"],
        "openmontage_release": facts["openmontage_release"],
        "openmontage_commit": facts["openmontage_commit"],
        "authority": facts["authority"],
        "package_python": facts["package_python"],
        "required_toolchain": facts["required_toolchain"],
        "manifest": facts["manifest"],
        "lock": facts["lock"],
        "guide": facts["guide"],
    }
    for key, expected in comparisons.items():
        if value[key] != expected:
            _fail("TAMPERED", f"Package Registration {key} no longer matches package")


def _registry_paths(data_root: os.PathLike[str] | str) -> _RegistryPaths:
    root = _absolute_existing_path(data_root, label="DataRoot", directory=True)
    registry = root / "State" / "PackageRegistration" / "v1"
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
    expected_registry = paths.data_root / "State" / "PackageRegistration" / "v1"
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


def _remove_active_locked(paths: _RegistryPaths, expected_current_raw: bytes) -> None:
    """CAS-remove the active pointer; caller must already hold _active_lock."""

    current_raw = _read_active_raw(paths)
    if current_raw != expected_current_raw:
        _fail("ACTIVE_CAS_MISMATCH", "active package pointer changed")
    try:
        paths.active.unlink()
    except OSError as exc:
        _fail("ATOMIC_WRITE_FAILED", f"cannot remove active package pointer: {exc}")
    if paths.active.exists():
        _fail("ATOMIC_WRITE_FAILED", "active package pointer remained after removal")


def _restore_active_locked(
    paths: _RegistryPaths,
    previous_raw: bytes | None,
    expected_current_raw: bytes | None,
) -> None:
    """Restore an exact pointer image while retaining a CAS boundary."""

    current_raw = _read_active_raw(paths)
    if current_raw != expected_current_raw:
        _fail("ACTIVE_CAS_MISMATCH", "active package pointer changed during rollback")
    if previous_raw is None:
        if current_raw is not None:
            _remove_active_locked(paths, current_raw)
        return
    _parse_active(previous_raw)
    _atomic_replace_active(paths.active, previous_raw, current_raw)


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
    release_archive: os.PathLike[str] | str,
    release_sha256_sidecar: os.PathLike[str] | str,
    package_root: os.PathLike[str] | str,
    package_python: os.PathLike[str] | str,
) -> Mapping[str, Any]:
    """Validate and immutably register one explicit OpenMontage package.

    Registration never activates the package.  All candidate validation completes
    before the registry receives any write.
    """

    paths = _registry_paths(data_root)
    archive = _absolute_existing_path(release_archive, label="Release archive")
    sidecar = _absolute_existing_path(release_sha256_sidecar, label="Release SHA sidecar")
    root = _absolute_existing_path(package_root, label="PackageRoot", directory=True)
    python = _absolute_existing_path(package_python, label="Package Python")
    registration, raw, digest = _build_registration(
        release_archive=archive,
        release_sha256_sidecar=sidecar,
        package_root=root,
        package_python=python,
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


def _deactivate_package(
    data_root: os.PathLike[str] | str,
    expected_active_pointer_sha256: str,
    registration_sha256: str,
) -> str:
    """Remove one active pointer under the same CAS/lock boundary as activation.

    The registration object and user DataRoot remain untouched; this is the
    lifecycle boundary used by the installer before removing package assets.
    """

    paths = _registry_paths(data_root)
    _ensure_existing_registry(paths)
    expected = _validate_expected_pointer(
        expected_active_pointer_sha256, allow_missing=False
    )
    target_sha = _require_sha256(registration_sha256, label="registration_sha256")
    with _active_lock(paths):
        current_raw = _read_active_raw(paths)
        if current_raw is None or _sha256_bytes(current_raw) != expected:
            _fail("ACTIVE_CAS_MISMATCH", "active package pointer changed")
        current_pointer = _parse_active(current_raw)
        if current_pointer["registration_sha256"] != target_sha:
            _fail("ACTIVE_CAS_MISMATCH", "active registration differs")
        _load_registration(paths, target_sha)
        _remove_active_locked(paths, current_raw)
        return "MISSING"


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
            "contract_id": registration["contract_id"],
            "openmontage_release": registration["openmontage_release"],
            "openmontage_commit": registration["openmontage_commit"],
            "authority": registration["authority"],
            "release": registration["release"],
            "package_root": registration["package_root"],
            "package_python": registration["package_python"],
            "required_toolchain": registration["required_toolchain"],
            "guide": registration["guide"],
            "manifest": registration["manifest"],
            "lock": registration["lock"],
        }
    )


__all__ = [
    "PackageRegistrationError",
    "activate_package",
    "locate_active_package",
    "recover_active_package",
    "register_package",
]
