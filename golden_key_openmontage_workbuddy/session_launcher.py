"""One fail-closed launch of a release-bound OpenMontage Package tool.

The launcher deliberately implements no provider, renderer, Agent, Pipeline, or
retry policy.  It validates one immutable tool definition against the active
Package Registration, starts that fixed tool once, and returns process facts.
"""

from __future__ import annotations

import ctypes
import hashlib
import json
import math
import os
import re
import signal
import stat
import subprocess
import threading
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from types import MappingProxyType
from typing import Any, Mapping, Sequence
from urllib.parse import urlsplit

from .package_registration import PackageRegistrationError, locate_active_package


_DEFINITION_SCHEMA = "golden-key-workbuddy-package-tool-definition-v1"
_CONTROLS_SCHEMA = "golden-key-workbuddy-launcher-executor-controls-v1"
_LOCAL_EVIDENCE_SCHEMA = "golden-key-workbuddy-local-capability-evidence-v1"
_REQUEST_SCHEMA = "golden-key-workbuddy-package-tool-request-v1"
_RESULT_SCHEMA = "golden-key-workbuddy-package-tool-result-v1"
_RECEIPT_SCHEMA = "golden-key-workbuddy-launcher-receipt-v1"
_REQUEST_SCHEMA_SHA256 = "c5b196bfe69c6a6db7073fb7fa7503a58837907e939fceeb5436fa7d19f80ce1"
_RESULT_SCHEMA_SHA256 = "8a96aceb463da2ea39549de44b06a765a3ac859260001ae277b99dbf2a8ca1b3"
_EMPTY_SHA256 = hashlib.sha256(b"").hexdigest()
_MAX_CAPTURE = 1024 * 1024
_MAX_RESULT_OUTPUT = 64 * 1024
_WINDOWS_PROCESS_PLATFORM = os.name == "nt"

_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
_IDENTIFIER_RE = re.compile(r"^[A-Za-z0-9._-]{1,128}$")
_ENV_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_VERSION_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9.+_-]{0,127}$")
_LICENSE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 .()+_-]{0,127}$")
_RESERVED_ENV = frozenset(
    name.casefold()
    for name in (
        "SystemRoot", "WINDIR", "COMSPEC", "PATHEXT", "TEMP", "TMP", "PATH",
        "PYTHONNOUSERSITE", "PYTHONUTF8", "PYTHONUNBUFFERED",
    )
)
_WINDOWS_INVALID_COMPONENT_CHARS = frozenset('<>:"|?*')
_WINDOWS_RESERVED_STEMS = frozenset(
    {
        "con", "prn", "aux", "nul",
        *(f"com{number}" for number in range(1, 10)),
        *(f"lpt{number}" for number in range(1, 10)),
        "com¹", "com²", "com³", "lpt¹", "lpt²", "lpt³",
    }
)

_DEFINITION_FIELDS = frozenset(
    {
        "schema_version", "definition_id", "definition_sha256",
        "definition_relative_path", "authority_owner", "package_release",
        "package_commit", "tool_id", "relative_path", "sha256", "size", "owner",
        "execution_kind", "interpreter_binding", "fixed_argv_template",
        "fixed_argv_placeholders", "request_schema_sha256", "result_schema_sha256",
        "allowed_environment_names", "secret_environment_names",
        "required_local_capabilities",
    }
)
_CONTROLS_FIELDS = frozenset(
    {
        "schema_version", "session_id", "request_id", "timeout_seconds",
        "termination_grace_seconds", "result_root", "provider_environment",
    }
)
_REQUIREMENT_FIELDS = frozenset(
    {"evidence_schema_version", "capability_id", "definition_sha256", "compatibility_basis"}
)
_LOCAL_EVIDENCE_FIELDS = frozenset(
    {
        "schema_version", "approved_capability_definition",
        "approved_capability_definition_sha256", "original_stage3_fact",
        "original_stage3_fact_sha256",
    }
)
_CAPABILITY_DEFINITION_REQUIRED = frozenset(
    {"capability", "definition_sha256", "version", "verified_entrypoint", "approved_mainland_sources", "assets"}
)
_CAPABILITY_DEFINITION_OPTIONAL = frozenset(
    {"explicit_registered_or_configured_candidate_paths", "normal_command_name"}
)
_SOURCE_FIELDS = frozenset({"filename", "url"})
_ASSET_FIELDS = frozenset({"filename", "size", "sha256", "license", "managed_target"})
_PRESENT_FACT_FIELDS = frozenset({"capability", "status", "evidence"})
_PRESENT_EVIDENCE_FIELDS = frozenset(
    {"status", "capability", "definition_sha256", "runtime_root", "verified_entrypoint", "version_evidence", "asset_evidence", "source"}
)
_INTEGRATED_FACT_FIELDS = frozenset(
    {"status", "capability", "definition_sha256", "runtime_root", "verified_entrypoint", "version_evidence", "asset_evidence", "source", "plan_sha256", "reused"}
)
_RESULT_FIELDS = frozenset({"schema_version", "session_id", "request_id", "outcome", "result_pointer", "error"})
_OUTCOMES = frozenset(
    {"PRELAUNCH_BLOCKED", "SPAWN_FAILED", "EXITED_SUCCESS", "EXITED_NONZERO", "CHILD_REPORTED_FAILURE", "TIMED_OUT", "CANCELLED", "INCOMPLETE", "RESIDUAL_PROCESS"}
)
_REASON_CODES = frozenset(
    {
        "NONE", "INVALID_INPUT", "CANCELLED_BEFORE_SPAWN", "LOCATOR_FAILED", "REGISTRATION_DRIFT",
        "TOOL_DEFINITION_INVALID", "TOOL_DEFINITION_UNBOUND", "TOOL_PATH_VIOLATION",
        "TOOL_IDENTITY_MISMATCH", "INTERPRETER_IDENTITY_MISMATCH",
        "LOCAL_CAPABILITY_EVIDENCE_REQUIRED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH",
        "ENVIRONMENT_NOT_ALLOWED", "SPAWN_OS_ERROR", "EXITED_NONZERO", "TIMEOUT", "CANCELLED",
        "CHILD_REPORTED_FAILURE", "OUTPUT_INVALID", "RESULT_POINTER_INVALID",
        "SECRET_DISCLOSURE_DETECTED", "EVIDENCE_INCOMPLETE", "RESIDUAL_PROCESS_DETECTED",
    }
)


class _LaunchError(Exception):
    def __init__(self, reason_code: str, origin: str) -> None:
        self.reason_code = reason_code
        self.origin = origin
        super().__init__(reason_code)


def _fail(reason_code: str, origin: str = "PREFLIGHT") -> None:
    raise _LaunchError(reason_code, origin)


def _freeze(value: Any) -> Any:
    if isinstance(value, Mapping):
        return MappingProxyType({key: _freeze(item) for key, item in value.items()})
    if isinstance(value, (list, tuple)):
        return tuple(_freeze(item) for item in value)
    return value


def _thaw(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {key: _thaw(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_thaw(item) for item in value]
    return value


def _canonical_json(value: Mapping[str, Any], *, newline: bool = True) -> bytes:
    try:
        raw = json.dumps(
            value, allow_nan=False, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
    except (TypeError, ValueError, UnicodeEncodeError):
        _fail("INVALID_INPUT")
    return raw + (b"\n" if newline else b"")


def _canonical_hash(value: Mapping[str, Any], *, newline: bool = False) -> str:
    return hashlib.sha256(_canonical_json(value, newline=newline)).hexdigest()


def _mapping(value: Any, fields: frozenset[str], reason: str = "INVALID_INPUT") -> Mapping[str, Any]:
    if not isinstance(value, Mapping) or not all(isinstance(key, str) for key in value):
        _fail(reason)
    try:
        keys = frozenset(value)
    except Exception:
        _fail(reason)
    if keys != fields:
        _fail(reason)
    return value


def _sequence(value: Any, reason: str) -> Sequence[Any]:
    if isinstance(value, (str, bytes, bytearray)) or not isinstance(value, Sequence):
        _fail(reason)
    return value


def _scalar_text(value: Any, *, nonempty: bool = True, max_length: int | None = None, reason: str) -> str:
    if not isinstance(value, str) or (nonempty and not value) or (max_length is not None and len(value) > max_length):
        _fail(reason)
    if any(0xD800 <= ord(character) <= 0xDFFF for character in value):
        _fail(reason)
    if unicodedata.normalize("NFC", value) != value:
        _fail(reason)
    try:
        value.encode("utf-8")
    except UnicodeEncodeError:
        _fail(reason)
    return value


def _sha256(value: Any, reason: str) -> str:
    if not isinstance(value, str) or _SHA256_RE.fullmatch(value) is None:
        _fail(reason)
    return value


def _safe_relative(value: Any, reason: str) -> str:
    text = _scalar_text(value, reason=reason)
    if "\\" in text or "\x00" in text:
        _fail(reason)
    pure = PurePosixPath(text)
    if pure.is_absolute() or pure.as_posix() != text or not pure.parts:
        _fail(reason)
    for component in pure.parts:
        if component in {"", ".", ".."} or component.endswith((".", " ")):
            _fail(reason)
        if any(ord(character) < 32 or character in _WINDOWS_INVALID_COMPONENT_CHARS for character in component):
            _fail(reason)
        if component.split(".", 1)[0].rstrip(" .").casefold() in _WINDOWS_RESERVED_STEMS:
            _fail(reason)
    return text


def _is_reparse(path: Path) -> bool:
    metadata = path.lstat()
    attributes = getattr(metadata, "st_file_attributes", 0)
    junction_method = getattr(path, "is_junction", None)
    junction = bool(junction_method()) if callable(junction_method) else False
    return path.is_symlink() or junction or bool(attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))


def _lexical_component_paths(path: Path) -> tuple[Path, ...]:
    if not path.is_absolute() or path == Path(path.anchor) or "~" in path.parts:
        _fail("TOOL_PATH_VIOLATION")
    paths: list[Path] = [Path(path.anchor)]
    current = Path(path.anchor)
    for component in path.parts[1:]:
        if (
            component in {"", ".", ".."}
            or component.endswith((".", " "))
            or any(
                ord(character) < 32 or character in _WINDOWS_INVALID_COMPONENT_CHARS
                for character in component
            )
            or component.split(".", 1)[0].rstrip(" .").casefold() in _WINDOWS_RESERVED_STEMS
        ):
            _fail("TOOL_PATH_VIOLATION")
        current = current / component
        paths.append(current)
    return tuple(paths)


def _path_object_identity(metadata: os.stat_result) -> tuple[int, int, int]:
    return metadata.st_dev, metadata.st_ino, stat.S_IFMT(metadata.st_mode)


def _path_stable_identity(metadata: os.stat_result) -> tuple[int, int, int, int, int]:
    return (
        metadata.st_dev,
        metadata.st_ino,
        metadata.st_size,
        metadata.st_mtime_ns,
        getattr(metadata, "st_ctime_ns", 0),
    )


def _regular_unaliased(metadata: os.stat_result) -> bool:
    attributes = getattr(metadata, "st_file_attributes", 0)
    return (
        stat.S_ISREG(metadata.st_mode)
        and not bool(attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))
        and getattr(metadata, "st_nlink", 1) == 1
    )


def _safe_existing_absolute_directory(value: Any, *, within: Path | None = None) -> Path:
    if not isinstance(value, (str, os.PathLike)):
        _fail("INVALID_INPUT")
    try:
        path = Path(value)
        try:
            _validate_components(path, stop=within)
        except _LaunchError:
            _fail("INVALID_INPUT")
        resolved = path.resolve(strict=True)
        if not resolved.is_dir():
            _fail("INVALID_INPUT")
        if within is not None:
            resolved.relative_to(within.resolve(strict=True))
        return resolved
    except _LaunchError:
        raise
    except (OSError, RuntimeError, ValueError):
        _fail("INVALID_INPUT")


def _validate_components(path: Path, *, stop: Path | None = None) -> None:
    raw_paths = _lexical_component_paths(path)
    stop_paths: tuple[Path, ...] = ()
    if stop is not None:
        stop_paths = _lexical_component_paths(stop)
    try:
        # This intentionally runs before resolve(): resolving first erases the
        # symlink/junction component that the contract requires us to reject.
        if any(_is_reparse(item) for item in (*stop_paths, *raw_paths)):
            _fail("TOOL_PATH_VIOLATION")
        resolved = path.resolve(strict=True)
        if stop is not None:
            resolved.relative_to(stop.resolve(strict=True))
    except (OSError, RuntimeError):
        _fail("TOOL_PATH_VIOLATION")
    except ValueError:
        _fail("TOOL_PATH_VIOLATION")


def _bound_file(root: Path, relative: str, reason: str) -> Path:
    candidate = root.joinpath(*PurePosixPath(relative).parts)
    try:
        _validate_components(candidate, stop=root)
        resolved = candidate.resolve(strict=True)
        resolved.relative_to(root)
        metadata = os.stat(candidate, follow_symlinks=False)
        if not resolved.is_file() or not _regular_unaliased(metadata):
            _fail(reason)
        return candidate
    except _LaunchError:
        raise
    except (OSError, RuntimeError, ValueError):
        _fail(reason)


def _hash_file(
    path: Path,
    *,
    reason: str = "EVIDENCE_INCOMPLETE",
    stop: Path | None = None,
) -> tuple[str, int]:
    digest = hashlib.sha256()
    total = 0
    handle: Any = None
    try:
        _validate_components(path, stop=stop)
        canonical_before = path.resolve(strict=True)
        stop_canonical_before: Path | None = None
        stop_identity_before: tuple[int, int, int] | None = None
        if stop is not None:
            stop_canonical_before = stop.resolve(strict=True)
            canonical_before.relative_to(stop_canonical_before)
            stop_identity_before = _path_object_identity(os.stat(stop, follow_symlinks=False))
        pathname_before = os.stat(path, follow_symlinks=False)
        if not _regular_unaliased(pathname_before):
            _fail(reason)
        flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOINHERIT", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
        handle = os.fdopen(descriptor, "rb", closefd=True)
        handle_before = os.fstat(handle.fileno())
        if (
            not _regular_unaliased(handle_before)
            or _path_object_identity(pathname_before) != _path_object_identity(handle_before)
        ):
            _fail(reason)
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
            total += len(chunk)
        handle_after = os.fstat(handle.fileno())
        _validate_components(path, stop=stop)
        pathname_after = os.stat(path, follow_symlinks=False)
        canonical_after = path.resolve(strict=True)
        if stop is not None:
            stop_canonical_after = stop.resolve(strict=True)
            canonical_after.relative_to(stop_canonical_after)
            if (
                stop_canonical_after != stop_canonical_before
                or _path_object_identity(os.stat(stop, follow_symlinks=False)) != stop_identity_before
            ):
                _fail(reason)
        if (
            canonical_after != canonical_before
            or not _regular_unaliased(pathname_after)
            or _path_object_identity(handle_after) != _path_object_identity(pathname_after)
            or _path_stable_identity(handle_before) != _path_stable_identity(handle_after)
            or total != handle_after.st_size
        ):
            _fail(reason)
    except _LaunchError:
        raise
    except (OSError, RuntimeError, ValueError):
        _fail(reason)
    finally:
        if handle is not None:
            try:
                handle.close()
            except OSError:
                _fail(reason)
    return digest.hexdigest(), total


def _read_file_bytes(path: Path, *, reason: str, stop: Path | None = None) -> bytes:
    chunks: list[bytes] = []
    handle: Any = None
    try:
        _validate_components(path, stop=stop)
        canonical_before = path.resolve(strict=True)
        stop_canonical_before: Path | None = None
        stop_identity_before: tuple[int, int, int] | None = None
        if stop is not None:
            stop_canonical_before = stop.resolve(strict=True)
            canonical_before.relative_to(stop_canonical_before)
            stop_identity_before = _path_object_identity(os.stat(stop, follow_symlinks=False))
        pathname_before = os.stat(path, follow_symlinks=False)
        if not _regular_unaliased(pathname_before):
            _fail(reason)
        flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NOINHERIT", 0) | getattr(os, "O_NOFOLLOW", 0)
        descriptor = os.open(path, flags)
        handle = os.fdopen(descriptor, "rb", closefd=True)
        handle_before = os.fstat(handle.fileno())
        if _path_object_identity(pathname_before) != _path_object_identity(handle_before):
            _fail(reason)
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        handle_after = os.fstat(handle.fileno())
        _validate_components(path, stop=stop)
        pathname_after = os.stat(path, follow_symlinks=False)
        canonical_after = path.resolve(strict=True)
        if stop is not None:
            stop_canonical_after = stop.resolve(strict=True)
            canonical_after.relative_to(stop_canonical_after)
            if (
                stop_canonical_after != stop_canonical_before
                or _path_object_identity(os.stat(stop, follow_symlinks=False)) != stop_identity_before
            ):
                _fail(reason)
        if (
            canonical_after != canonical_before
            or not _regular_unaliased(pathname_after)
            or not _regular_unaliased(handle_after)
            or _path_object_identity(handle_after) != _path_object_identity(pathname_after)
            or _path_stable_identity(handle_before) != _path_stable_identity(handle_after)
            or sum(map(len, chunks)) != handle_after.st_size
        ):
            _fail(reason)
        return b"".join(chunks)
    except _LaunchError:
        raise
    except (OSError, RuntimeError, ValueError):
        _fail(reason)
    finally:
        if handle is not None:
            try:
                handle.close()
            except OSError:
                _fail(reason)


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _empty_receipt(start_ns: int) -> dict[str, Any]:
    return {
        "schema_version": _RECEIPT_SCHEMA,
        "outcome": "PRELAUNCH_BLOCKED",
        "reason_code": "EVIDENCE_INCOMPLETE",
        "session": {"session_id": None},
        "request": {"request_id": None},
        "registration": {"registration_sha256": None},
        "package": {"openmontage_release": None, "openmontage_commit": None, "package_root": None},
        "manifest": {"sha256": None, "size": None},
        "lock": {"sha256": None, "size": None, "bundle_sha256": None},
        "tool_definition": {"definition_id": None, "definition_sha256": None, "authority_owner": None},
        "tool_file": {"tool_id": None, "relative_path": None, "path": None, "sha256": None, "size": None, "owner": None},
        "interpreter": {"binding": None, "path": None, "sha256": None, "size": None},
        "user_message": {"sha256": None, "byte_length": None},
        "provider_environment_names": (),
        "local_capability_evidence_identities": (),
        "launched": False,
        "spawn_count": 0,
        "pid": None,
        "started_at_utc": None,
        "ended_at_utc": _utc_now(),
        "duration_ms": max(0, (time.monotonic_ns() - start_ns) // 1_000_000),
        "exit_code": None,
        "timed_out": False,
        "cancelled": False,
        "retry_count": 0,
        "stdout": {"size": 0, "sha256": _EMPTY_SHA256, "truncated": False},
        "stderr": {"size": 0, "sha256": _EMPTY_SHA256, "truncated": False},
        "result_pointer": {"path": None, "sha256": None, "size": None, "valid": False},
        "error": {"code": "EVIDENCE_INCOMPLETE", "origin": "PREFLIGHT", "sanitized_message": "EVIDENCE_INCOMPLETE"},
        "residual_process": {"detected": False, "termination_attempted": False, "termination_succeeded": None, "observed_pids": ()},
    }


def _set_failure(receipt: dict[str, Any], outcome: str, reason: str, origin: str) -> None:
    if outcome not in _OUTCOMES or reason not in _REASON_CODES:
        raise RuntimeError("closed LauncherReceiptV1 outcome/reason violation")
    receipt["outcome"] = outcome
    receipt["reason_code"] = reason
    receipt["error"] = {"code": reason, "origin": origin, "sanitized_message": reason}


def _finish(
    receipt: dict[str, Any], start_ns: int, provider_canaries: Sequence[str] = ()
) -> Mapping[str, Any]:
    receipt["ended_at_utc"] = _utc_now()
    receipt["duration_ms"] = max(0, (time.monotonic_ns() - start_ns) // 1_000_000)
    propagated = _sanitize_dynamic_receipt_fields(receipt, provider_canaries)
    if propagated and receipt["spawn_count"] == 0:
        if not (
            receipt["outcome"] == "CANCELLED"
            and receipt["reason_code"] == "CANCELLED_BEFORE_SPAWN"
        ):
            _set_failure(receipt, "PRELAUNCH_BLOCKED", "INVALID_INPUT", "PREFLIGHT")
    elif propagated and receipt["outcome"] != "RESIDUAL_PROCESS":
        _set_failure(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", "OUTPUT")
    return _freeze(receipt)


def _strict_json_file(
    path: Path, reason: str, *, stop: Path | None = None
) -> Mapping[str, Any]:
    try:
        raw = _read_file_bytes(path, reason=reason, stop=stop)
        text = raw.decode("utf-8")
        seen_error: list[str] = []

        def object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
            result: dict[str, Any] = {}
            for key, value in pairs:
                if key in result:
                    seen_error.append(key)
                result[key] = value
            return result

        value = json.loads(
            text,
            object_pairs_hook=object_pairs,
            parse_constant=lambda _value: (_ for _ in ()).throw(ValueError("constant")),
        )
        if seen_error or not isinstance(value, Mapping):
            _fail(reason)
        return value
    except _LaunchError:
        raise
    except (OSError, UnicodeError, ValueError, TypeError, json.JSONDecodeError):
        _fail(reason)


def _inventory(package_root: Path, located: Mapping[str, Any]) -> tuple[dict[str, Mapping[str, Any]], dict[str, Mapping[str, Any]]]:
    manifest_path = _bound_file(package_root, located["manifest"]["relative_path"], "REGISTRATION_DRIFT")
    lock_path = _bound_file(package_root, located["lock"]["relative_path"], "REGISTRATION_DRIFT")
    manifest = _strict_json_file(manifest_path, "REGISTRATION_DRIFT", stop=package_root)
    lock = _strict_json_file(lock_path, "REGISTRATION_DRIFT", stop=package_root)
    manifest_entries = manifest.get("files")
    lock_entries = lock.get("files")
    if not isinstance(manifest_entries, list) or not isinstance(lock_entries, list):
        _fail("REGISTRATION_DRIFT")
    manifest_by_path: dict[str, Mapping[str, Any]] = {}
    lock_by_path: dict[str, Mapping[str, Any]] = {}
    for raw in manifest_entries:
        if not isinstance(raw, Mapping) or not isinstance(raw.get("path"), str):
            _fail("REGISTRATION_DRIFT")
        relative = raw["path"]
        if relative in manifest_by_path:
            _fail("REGISTRATION_DRIFT")
        manifest_by_path[relative] = raw
    for raw in lock_entries:
        if not isinstance(raw, Mapping) or not isinstance(raw.get("source_path"), str):
            _fail("REGISTRATION_DRIFT")
        relative = raw["source_path"]
        if relative in lock_by_path:
            _fail("REGISTRATION_DRIFT")
        lock_by_path[relative] = raw
    return manifest_by_path, lock_by_path


def _env_names(value: Any, reason: str) -> tuple[str, ...]:
    raw = _sequence(value, reason)
    names: list[str] = []
    folded: set[str] = set()
    for item in raw:
        if not isinstance(item, str) or _ENV_RE.fullmatch(item) is None:
            _fail(reason)
        key = item.casefold()
        if key in folded or key in _RESERVED_ENV:
            _fail(reason)
        folded.add(key)
        names.append(item)
    if names != sorted(names):
        _fail(reason)
    return tuple(names)


def _validate_definition(
    value: Any,
    located: Mapping[str, Any],
    package_root: Path,
    manifest_by_path: Mapping[str, Mapping[str, Any]],
    lock_by_path: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    if value is None:
        _fail("TOOL_DEFINITION_UNBOUND")
    definition = _mapping(value, _DEFINITION_FIELDS, "TOOL_DEFINITION_INVALID")
    if definition["schema_version"] != _DEFINITION_SCHEMA:
        _fail("TOOL_DEFINITION_INVALID")
    definition_id = _scalar_text(definition["definition_id"], max_length=128, reason="TOOL_DEFINITION_INVALID")
    definition_digest = _sha256(definition["definition_sha256"], "TOOL_DEFINITION_INVALID")
    definition_relative = _safe_relative(definition["definition_relative_path"], "TOOL_DEFINITION_INVALID")
    authority_owner = _scalar_text(definition["authority_owner"], reason="TOOL_DEFINITION_INVALID")
    package_release = _scalar_text(definition["package_release"], reason="TOOL_DEFINITION_INVALID")
    package_commit = definition["package_commit"]
    if not isinstance(package_commit, str) or _COMMIT_RE.fullmatch(package_commit) is None:
        _fail("TOOL_DEFINITION_INVALID")
    tool_id = _scalar_text(definition["tool_id"], max_length=128, reason="TOOL_DEFINITION_INVALID")
    relative_path = _safe_relative(definition["relative_path"], "TOOL_PATH_VIOLATION")
    tool_sha256 = _sha256(definition["sha256"], "TOOL_DEFINITION_INVALID")
    size = definition["size"]
    if type(size) is not int or size <= 0:
        _fail("TOOL_DEFINITION_INVALID")
    owner = _scalar_text(definition["owner"], reason="TOOL_DEFINITION_INVALID")
    execution_kind = definition["execution_kind"]
    binding = definition["interpreter_binding"]
    template_raw = _sequence(definition["fixed_argv_template"], "TOOL_DEFINITION_INVALID")
    template: list[str] = []
    for token in template_raw:
        if not isinstance(token, str) or not token or "\x00" in token:
            _fail("TOOL_DEFINITION_INVALID")
        _scalar_text(token, reason="TOOL_DEFINITION_INVALID")
        template.append(token)
    placeholders_raw = _sequence(definition["fixed_argv_placeholders"], "TOOL_DEFINITION_INVALID")
    placeholders = tuple(placeholders_raw)
    if execution_kind == "PACKAGE_PYTHON_SCRIPT":
        if binding != "LOCATOR_PACKAGE_PYTHON" or placeholders != ("{verified_tool_path}",) or template.count("{verified_tool_path}") != 1:
            _fail("TOOL_DEFINITION_INVALID")
    elif execution_kind == "DIRECT_EXECUTABLE":
        if binding != "SELF" or placeholders != () or "{verified_tool_path}" in template:
            _fail("TOOL_DEFINITION_INVALID")
    else:
        _fail("TOOL_DEFINITION_INVALID")
    if definition["request_schema_sha256"] != _REQUEST_SCHEMA_SHA256 or definition["result_schema_sha256"] != _RESULT_SCHEMA_SHA256:
        _fail("TOOL_DEFINITION_INVALID")
    allowed = _env_names(definition["allowed_environment_names"], "TOOL_DEFINITION_INVALID")
    secrets = _env_names(definition["secret_environment_names"], "TOOL_DEFINITION_INVALID")
    if not {name.casefold() for name in secrets}.issubset({name.casefold() for name in allowed}):
        _fail("TOOL_DEFINITION_INVALID")
    raw_requirements = _sequence(definition["required_local_capabilities"], "TOOL_DEFINITION_INVALID")
    requirements: list[dict[str, Any]] = []
    seen_requirements: set[str] = set()
    for raw_requirement in raw_requirements:
        requirement = _mapping(raw_requirement, _REQUIREMENT_FIELDS, "TOOL_DEFINITION_INVALID")
        if requirement["evidence_schema_version"] != _LOCAL_EVIDENCE_SCHEMA or requirement["compatibility_basis"] != "EXACT_ASSET_IDENTITY":
            _fail("TOOL_DEFINITION_INVALID")
        capability = _safe_relative(requirement["capability_id"], "TOOL_DEFINITION_INVALID")
        if "/" in capability or capability in seen_requirements:
            _fail("TOOL_DEFINITION_INVALID")
        seen_requirements.add(capability)
        requirements.append(
            {
                "evidence_schema_version": _LOCAL_EVIDENCE_SCHEMA,
                "capability_id": capability,
                "definition_sha256": _sha256(requirement["definition_sha256"], "TOOL_DEFINITION_INVALID"),
                "compatibility_basis": "EXACT_ASSET_IDENTITY",
            }
        )
    if requirements != sorted(requirements, key=lambda item: (item["capability_id"], item["definition_sha256"])):
        _fail("TOOL_DEFINITION_INVALID")
    body = _thaw(definition)
    del body["definition_sha256"]
    if _canonical_hash(body, newline=True) != definition_digest:
        _fail("TOOL_DEFINITION_INVALID")
    if package_release != located["openmontage_release"] or package_commit != located["openmontage_commit"]:
        _fail("TOOL_DEFINITION_UNBOUND")

    definition_entry = manifest_by_path.get(definition_relative)
    definition_lock = lock_by_path.get(definition_relative)
    if (
        definition_entry is None
        or definition_lock is None
        or definition_entry.get("owner") != authority_owner
        or definition_entry.get("sha256") != definition_lock.get("sha256")
        or definition_entry.get("size") != definition_lock.get("size")
    ):
        _fail("TOOL_DEFINITION_UNBOUND")
    definition_path = _bound_file(package_root, definition_relative, "TOOL_PATH_VIOLATION")
    definition_bytes = _read_file_bytes(
        definition_path, reason="TOOL_DEFINITION_UNBOUND", stop=package_root
    )
    if definition_bytes != _canonical_json(_thaw(definition), newline=True):
        _fail("TOOL_DEFINITION_UNBOUND")
    if hashlib.sha256(definition_bytes).hexdigest() != definition_entry.get("sha256") or len(definition_bytes) != definition_entry.get("size"):
        _fail("TOOL_DEFINITION_UNBOUND")

    tool_entry = manifest_by_path.get(relative_path)
    tool_lock = lock_by_path.get(relative_path)
    if tool_entry is None or tool_lock is None:
        _fail("TOOL_IDENTITY_MISMATCH")
    if (
        tool_entry.get("owner") != owner
        or tool_entry.get("sha256") != tool_sha256
        or tool_entry.get("size") != size
        or tool_lock.get("sha256") != tool_sha256
        or tool_lock.get("size") != size
    ):
        _fail("TOOL_IDENTITY_MISMATCH")
    tool_path = _bound_file(package_root, relative_path, "TOOL_PATH_VIOLATION")
    if _hash_file(tool_path, reason="TOOL_IDENTITY_MISMATCH", stop=package_root) != (tool_sha256, size):
        _fail("TOOL_IDENTITY_MISMATCH")

    interpreter: dict[str, Any]
    if execution_kind == "PACKAGE_PYTHON_SCRIPT":
        package_python = located["package_python"]
        interpreter_path = Path(package_python["path"])
        try:
            _validate_components(interpreter_path, stop=package_root)
        except _LaunchError:
            _fail("INTERPRETER_IDENTITY_MISMATCH")
        if _hash_file(
            interpreter_path,
            reason="INTERPRETER_IDENTITY_MISMATCH",
            stop=package_root,
        ) != (package_python["sha256"], package_python["size"]):
            _fail("INTERPRETER_IDENTITY_MISMATCH")
        interpreter = {
            "binding": binding,
            "path": str(interpreter_path),
            "sha256": package_python["sha256"],
            "size": package_python["size"],
        }
        argv = [str(interpreter_path)] + [str(tool_path) if token == "{verified_tool_path}" else token for token in template]
    else:
        interpreter = {"binding": binding, "path": str(tool_path), "sha256": tool_sha256, "size": size}
        argv = [str(tool_path), *template]
    return {
        "mapping": _thaw(definition),
        "definition_id": definition_id,
        "definition_sha256": definition_digest,
        "definition_relative_path": definition_relative,
        "definition_path": definition_path,
        "authority_owner": authority_owner,
        "tool_id": tool_id,
        "relative_path": relative_path,
        "tool_path": tool_path,
        "tool_sha256": tool_sha256,
        "tool_size": size,
        "owner": owner,
        "execution_kind": execution_kind,
        "allowed_environment_names": allowed,
        "secret_environment_names": secrets,
        "requirements": requirements,
        "interpreter": interpreter,
        "argv": argv,
    }


def _validate_capability_definition(value: Any, expected_capability: str, expected_digest: str) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    keys = frozenset(value)
    if not _CAPABILITY_DEFINITION_REQUIRED.issubset(keys) or keys - _CAPABILITY_DEFINITION_REQUIRED - _CAPABILITY_DEFINITION_OPTIONAL:
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    capability = _scalar_text(value.get("capability"), reason="LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    if capability != expected_capability:
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    definition_digest = _sha256(value.get("definition_sha256"), "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    if definition_digest != expected_digest:
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    version = value.get("version")
    if not isinstance(version, str) or _VERSION_RE.fullmatch(version) is None:
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    entrypoint = _safe_relative(value.get("verified_entrypoint"), "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    raw_sources = _sequence(value.get("approved_mainland_sources"), "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    sources: dict[str, str] = {}
    for raw_source in raw_sources:
        source = _mapping(raw_source, _SOURCE_FIELDS, "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        filename = _safe_relative(source["filename"], "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        if "/" in filename or filename in sources:
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        source_url = source["url"]
        if not isinstance(source_url, str):
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        parsed = urlsplit(source_url)
        try:
            port = parsed.port
        except ValueError:
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        if (
            parsed.scheme != "https"
            or parsed.hostname != "registry.npmmirror.com"
            or port not in {None, 443}
            or parsed.username is not None
            or parsed.password is not None
            or not parsed.path.startswith("/")
            or parsed.query
            or parsed.fragment
        ):
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        sources[filename] = source_url
    raw_assets = _sequence(value.get("assets"), "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    assets: list[dict[str, Any]] = []
    targets: set[str] = set()
    for raw_asset in raw_assets:
        asset = _mapping(raw_asset, _ASSET_FIELDS, "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        filename = _safe_relative(asset["filename"], "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        target = _safe_relative(asset["managed_target"], "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        size = asset["size"]
        if "/" in filename or filename not in sources or target in targets or type(size) is not int or size < 0:
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        digest = _sha256(asset["sha256"], "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        license_name = asset["license"]
        if not isinstance(license_name, str) or _LICENSE_RE.fullmatch(license_name) is None:
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        targets.add(target)
        assets.append({"filename": filename, "size": size, "sha256": digest, "license": license_name, "managed_target": target})
    assets.sort(key=lambda item: (item["managed_target"], item["filename"]))
    if not assets or set(sources) != {item["filename"] for item in assets} or entrypoint not in targets:
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    explicit_raw = value.get("explicit_registered_or_configured_candidate_paths", [])
    explicit_values = _sequence(explicit_raw, "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    explicit: list[str] = []
    for candidate in explicit_values:
        if not isinstance(candidate, str) or not Path(candidate).is_absolute():
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        explicit.append(str(Path(candidate)))
    if len(set(explicit)) != len(explicit):
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    explicit.sort()
    command = value.get("normal_command_name")
    if command is not None:
        if not isinstance(command, str) or command.casefold() not in {capability.casefold(), f"{capability}.cmd".casefold(), f"{capability}.exe".casefold()}:
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    body = {
        "capability": capability,
        "version": version,
        "verified_entrypoint": entrypoint,
        "approved_mainland_sources": [{"filename": name, "url": sources[name]} for name in sorted(sources)],
        "assets": assets,
        "explicit_registered_or_configured_candidate_paths": explicit,
        "normal_command_name": command,
    }
    if _canonical_hash(body) != definition_digest:
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    return {"mapping": _thaw(value), "capability": capability, "definition_sha256": definition_digest, "version": version, "entrypoint": entrypoint, "assets": assets, "explicit": explicit, "command": command}


def _asset_file(path: Path, asset: Mapping[str, Any], *, stop: Path | None = None) -> bool:
    try:
        if not path.is_file() or _is_reparse(path):
            return False
        return _hash_file(
            path, reason="LOCAL_CAPABILITY_EVIDENCE_MISMATCH", stop=stop
        ) == (
            asset["sha256"], asset["size"]
        )
    except (_LaunchError, OSError, RuntimeError):
        return False


def _fact_identity(
    original: Any, definition: Mapping[str, Any]
) -> tuple[str, str, str | None, str, str, Path]:
    if not isinstance(original, Mapping):
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    status = original.get("status")
    if status == "PRESENT":
        fact = _mapping(original, _PRESENT_FACT_FIELDS, "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        evidence = _mapping(fact["evidence"], _PRESENT_EVIDENCE_FIELDS, "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        if evidence["status"] != "PRESENT":
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        plan_sha256 = None
    elif status == "INTEGRATED":
        evidence = _mapping(original, _INTEGRATED_FACT_FIELDS, "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        plan_sha256 = _sha256(evidence["plan_sha256"], "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        if evidence["source"] != "managed" or type(evidence["reused"]) is not bool:
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    else:
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    if evidence.get("capability") != definition["capability"] or evidence.get("definition_sha256") != definition["definition_sha256"]:
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    source = evidence.get("source")
    if source not in {"managed", "explicit", "PATH"}:
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    version_evidence = evidence.get("version_evidence")
    asset_evidence = evidence.get("asset_evidence")
    if not isinstance(version_evidence, Mapping) or frozenset(version_evidence) != frozenset({"reason", "entrypoint", "exit_code", "version_output"}):
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    if (
        version_evidence.get("reason") != "COMPATIBLE"
        or version_evidence.get("exit_code") != 0
        or not isinstance(version_evidence.get("entrypoint"), str)
        or not isinstance(version_evidence.get("version_output"), str)
    ):
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    try:
        raw_asset_evidence = _sequence(asset_evidence, "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    except _LaunchError:
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    runtime_text = evidence.get("runtime_root")
    entrypoint_text = evidence.get("verified_entrypoint")
    if not isinstance(runtime_text, str) or not isinstance(entrypoint_text, str):
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    if version_evidence["entrypoint"] != entrypoint_text:
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    expected_assets = {asset["managed_target"]: asset for asset in definition["assets"]}
    if len(raw_asset_evidence) != (1 if source == "PATH" else len(expected_assets)):
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    seen_assets: set[str] = set()
    for raw_asset in raw_asset_evidence:
        fields = frozenset({"managed_target", "expected_size", "expected_sha256", "license", "exists", "size", "sha256", "reason"})
        asset_fact = _mapping(raw_asset, fields, "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        target = asset_fact["managed_target"]
        expected = expected_assets.get(target)
        if expected is None or target in seen_assets:
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        seen_assets.add(target)
        if source == "PATH" and target != definition["entrypoint"]:
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        if asset_fact != {
            "managed_target": target, "expected_size": expected["size"],
            "expected_sha256": expected["sha256"], "license": expected["license"],
            "exists": True, "size": expected["size"], "sha256": expected["sha256"],
            "reason": "IDENTITY_MATCH",
        }:
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    try:
        runtime_root = Path(runtime_text)
        entrypoint_path = Path(entrypoint_text)
        if not runtime_root.is_absolute() or not entrypoint_path.is_absolute():
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    except (OSError, ValueError):
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
    return status, source, plan_sha256, runtime_text, entrypoint_text, runtime_root


def _validate_source_assets(
    *,
    data_root: Path,
    definition: Mapping[str, Any],
    source: str,
    runtime_root: Path,
    entrypoint_text: str,
) -> tuple[str, int]:
    try:
        if source == "managed":
            expected_root = data_root / "Runtime" / "Composition" / definition["capability"] / definition["definition_sha256"]
            _validate_components(runtime_root, stop=data_root)
            if runtime_root.resolve(strict=True) != expected_root.resolve(strict=True):
                _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
            if not runtime_root.is_dir():
                _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
            expected_files = {asset["managed_target"] for asset in definition["assets"]}
            expected_directories = {
                parent.as_posix()
                for target in expected_files
                for parent in PurePosixPath(target).parents
                if parent.as_posix() != "."
            }
            actual_files: set[str] = set()
            actual_directories: set[str] = set()
            for current_text, directories, files in os.walk(runtime_root, followlinks=False):
                current = Path(current_text)
                for name in list(directories):
                    child = current / name
                    if _is_reparse(child):
                        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
                    actual_directories.add(child.relative_to(runtime_root).as_posix())
                for name in files:
                    child = current / name
                    if _is_reparse(child):
                        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
                    actual_files.add(child.relative_to(runtime_root).as_posix())
            if actual_files != expected_files or actual_directories != expected_directories:
                _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
            for asset in definition["assets"]:
                asset_path = runtime_root.joinpath(*PurePosixPath(asset["managed_target"]).parts)
                _validate_components(asset_path, stop=runtime_root)
                if not _asset_file(asset_path, asset, stop=runtime_root):
                    _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
            entrypoint_candidate = runtime_root.joinpath(*PurePosixPath(definition["entrypoint"]).parts)
            _validate_components(entrypoint_candidate, stop=runtime_root)
            expected_entrypoint = entrypoint_candidate.resolve(strict=True)
        elif source == "explicit":
            _validate_components(runtime_root)
            resolved_root = runtime_root.resolve(strict=True)
            approved_roots: set[str] = set()
            for item in definition["explicit"]:
                configured = Path(item)
                _validate_components(configured)
                approved_roots.add(str(configured.resolve(strict=True)))
            if str(resolved_root) not in approved_roots:
                _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
            if not runtime_root.is_dir():
                _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
            for asset in definition["assets"]:
                asset_path = runtime_root.joinpath(*PurePosixPath(asset["managed_target"]).parts)
                _validate_components(asset_path, stop=runtime_root)
                if not _asset_file(asset_path, asset, stop=runtime_root):
                    _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
            entrypoint_candidate = runtime_root.joinpath(*PurePosixPath(definition["entrypoint"]).parts)
            _validate_components(entrypoint_candidate, stop=runtime_root)
            expected_entrypoint = entrypoint_candidate.resolve(strict=True)
        else:
            entrypoint_candidate = Path(entrypoint_text)
            _validate_components(runtime_root)
            _validate_components(entrypoint_candidate)
            if not definition["command"] or runtime_root.resolve(strict=True) != entrypoint_candidate.resolve(strict=True):
                _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
            command = runtime_root
            if not command.is_file():
                _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
            matches = [asset for asset in definition["assets"] if asset["managed_target"] == definition["entrypoint"]]
            if len(matches) != 1 or not _asset_file(command, matches[0]):
                _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
            expected_entrypoint = command.resolve(strict=True)
        _validate_components(Path(entrypoint_text))
        if expected_entrypoint != Path(entrypoint_text).resolve(strict=True):
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        entrypoint_asset = next(asset for asset in definition["assets"] if asset["managed_target"] == definition["entrypoint"])
        identity_root = runtime_root if source in {"managed", "explicit"} else None
        identity_path = entrypoint_candidate if source in {"managed", "explicit"} else runtime_root
        if not _asset_file(identity_path, entrypoint_asset, stop=identity_root):
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        return entrypoint_asset["sha256"], entrypoint_asset["size"]
    except _LaunchError as exc:
        if exc.reason_code != "LOCAL_CAPABILITY_EVIDENCE_MISMATCH":
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        raise
    except (OSError, RuntimeError, ValueError):
        _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")


def _validate_local_evidence(
    value: Any,
    requirements: Sequence[Mapping[str, Any]],
    data_root: Path,
    provider_canaries: Sequence[str] = (),
) -> tuple[dict[str, Any], ...]:
    raw_items = _sequence(value, "INVALID_INPUT")
    if not requirements:
        if raw_items:
            _fail("INVALID_INPUT")
        return ()
    if len(raw_items) != len(requirements):
        _fail("LOCAL_CAPABILITY_EVIDENCE_REQUIRED")
    by_requirement = {(item["capability_id"], item["definition_sha256"]): item for item in requirements}
    result: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for raw in raw_items:
        item = _mapping(raw, _LOCAL_EVIDENCE_FIELDS, "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        if item["schema_version"] != _LOCAL_EVIDENCE_SCHEMA:
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        approved = item["approved_capability_definition"]
        if not isinstance(approved, Mapping):
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        capability = approved.get("capability")
        definition_digest = approved.get("definition_sha256")
        key = (capability, definition_digest)
        requirement = by_requirement.get(key)
        if requirement is None or key in seen:
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        seen.add(key)
        definition = _validate_capability_definition(approved, capability, definition_digest)
        approved_digest = _sha256(item["approved_capability_definition_sha256"], "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        if approved_digest != definition_digest:
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        original = item["original_stage3_fact"]
        original_digest = _sha256(item["original_stage3_fact_sha256"], "LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        if not isinstance(original, Mapping):
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        if _dynamic_value_contains_secret(
            {
                "original_stage3_fact": original,
                "original_stage3_fact_sha256": original_digest,
            },
            provider_canaries,
        ):
            _fail("INVALID_INPUT")
        if _canonical_hash(_thaw(original)) != original_digest:
            _fail("LOCAL_CAPABILITY_EVIDENCE_MISMATCH")
        status, source, plan_digest, _runtime_text, entrypoint_text, runtime_root = _fact_identity(original, definition)
        entrypoint_digest, entrypoint_size = _validate_source_assets(
            data_root=data_root,
            definition=definition,
            source=source,
            runtime_root=runtime_root,
            entrypoint_text=entrypoint_text,
        )
        identity = {
            "capability_id": capability,
            "definition_sha256": definition_digest,
            "approved_capability_definition_sha256": approved_digest,
            "original_stage3_fact_sha256": original_digest,
            "status": status,
            "source": source,
            "plan_sha256": plan_digest,
            "entrypoint_sha256": entrypoint_digest,
            "entrypoint_size": entrypoint_size,
        }
        # Every receipt identity mixes original-fact-derived values with asset
        # facts, so it is one dynamic object rather than a field-level Package
        # authority.  A Provider value in either the fact or the reconstructed
        # identity invalidates the whole item before stdin construction.
        if _dynamic_value_contains_secret(identity, provider_canaries):
            _fail("INVALID_INPUT")
        result.append(identity)
    if seen != set(by_requirement):
        _fail("LOCAL_CAPABILITY_EVIDENCE_REQUIRED")
    return tuple(sorted(result, key=lambda item: (item["capability_id"], item["definition_sha256"])))


def _validate_controls(value: Any, definition: Mapping[str, Any], data_root: Path) -> dict[str, Any]:
    controls = _mapping(value, _CONTROLS_FIELDS)
    if controls["schema_version"] != _CONTROLS_SCHEMA:
        _fail("INVALID_INPUT")
    session_id = controls["session_id"]
    request_id = controls["request_id"]
    if not isinstance(session_id, str) or _IDENTIFIER_RE.fullmatch(session_id) is None:
        _fail("INVALID_INPUT")
    if not isinstance(request_id, str) or _IDENTIFIER_RE.fullmatch(request_id) is None:
        _fail("INVALID_INPUT")
    timeout = controls["timeout_seconds"]
    grace = controls["termination_grace_seconds"]
    if type(timeout) is not int or not 1 <= timeout <= 3600 or type(grace) is not int or not 1 <= grace <= 30:
        _fail("INVALID_INPUT")
    result_root = _safe_existing_absolute_directory(controls["result_root"], within=data_root)
    provider = controls["provider_environment"]
    if not isinstance(provider, Mapping) or not all(isinstance(key, str) for key in provider):
        _fail("INVALID_INPUT")
    allowed_by_fold = {name.casefold(): name for name in definition["allowed_environment_names"]}
    validated_provider: dict[str, str] = {}
    seen: set[str] = set()
    for name, raw_value in provider.items():
        if _ENV_RE.fullmatch(name) is None or name.casefold() in seen:
            _fail("INVALID_INPUT")
        seen.add(name.casefold())
        if name.casefold() not in allowed_by_fold:
            _fail("ENVIRONMENT_NOT_ALLOWED")
        if not isinstance(raw_value, str) or "\x00" in raw_value or any(0xD800 <= ord(character) <= 0xDFFF for character in raw_value):
            _fail("INVALID_INPUT")
        try:
            raw_value.encode("utf-8")
        except UnicodeEncodeError:
            _fail("INVALID_INPUT")
        validated_provider[allowed_by_fold[name.casefold()]] = raw_value
    return {
        "session_id": session_id,
        "request_id": request_id,
        "timeout_seconds": timeout,
        "termination_grace_seconds": grace,
        "result_root": result_root,
        "result_root_input": Path(controls["result_root"]),
        "provider_environment": validated_provider,
        "provider_environment_names": tuple(sorted(validated_provider)),
    }


def _provider_canaries(
    controls: Mapping[str, Any]
) -> tuple[tuple[str, ...], tuple[bytes, ...]]:
    # Every provider value is confidential regardless of the optional
    # secret_environment_names metadata.  That field controls Package intent;
    # it never narrows the Launcher's disclosure boundary.
    canary_text = tuple(
        value for value in controls["provider_environment"].values() if value
    )
    return canary_text, tuple(value.encode("utf-8") for value in canary_text)


def _raw_provider_canaries(
    executor_controls: Any,
) -> tuple[tuple[str, ...], tuple[bytes, ...], bool]:
    """Read raw Provider values before producing any dynamic receipt hint.

    The boolean is false when the raw mapping could not be read completely;
    callers then suppress all unverified hints.  No exception text or object
    representation from an untrusted Mapping crosses this boundary.
    """

    if not isinstance(executor_controls, Mapping):
        return (), (), False
    try:
        provider = executor_controls.get("provider_environment")
    except Exception:
        return (), (), False
    if not isinstance(provider, Mapping):
        return (), (), provider is None
    text_values: list[str] = []
    byte_values: list[bytes] = []
    complete = True
    try:
        items = provider.items()
        for _name, value in items:
            if not isinstance(value, str) or not value:
                continue
            if value not in text_values:
                text_values.append(value)
            try:
                encoded = value.encode("utf-8")
            except UnicodeEncodeError:
                complete = False
                continue
            if encoded not in byte_values:
                byte_values.append(encoded)
    except Exception:
        complete = False
    return tuple(text_values), tuple(byte_values), complete


def _contains_secret(secrets: Sequence[bytes], *materials: bytes) -> bool:
    return any(secret in material for secret in secrets for material in materials)


def _dynamic_value_contains_secret(value: Any, secrets: Sequence[str]) -> bool:
    """Scan a dynamic value using the scalar spelling canonical JSON emits.

    Mapping keys are data too.  Strings are inspected after JSON decoding, so
    ``ensure_ascii`` escapes cannot conceal a Provider value.  Boolean handling
    must precede integer handling because ``bool`` subclasses ``int``.
    """

    if isinstance(value, str):
        scalar = value
    elif value is True:
        scalar = "true"
    elif value is False:
        scalar = "false"
    elif type(value) is int:
        scalar = str(value)
    elif value is None:
        scalar = "null"
    elif type(value) is float:
        if not math.isfinite(value):
            return False
        scalar = json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=False,
            separators=(",", ":"),
        )
    elif isinstance(value, Mapping):
        return any(
            _dynamic_value_contains_secret(key, secrets)
            or _dynamic_value_contains_secret(item, secrets)
            for key, item in value.items()
        )
    elif isinstance(value, (list, tuple)):
        return any(_dynamic_value_contains_secret(item, secrets) for item in value)
    else:
        return False
    return any(secret and secret in scalar for secret in secrets)


def _suppressed_stream_facts() -> dict[str, Any]:
    return {"size": 0, "sha256": _EMPTY_SHA256, "truncated": True}


def _sanitize_dynamic_receipt_fields(
    receipt: dict[str, Any], provider_canaries: Sequence[str]
) -> bool:
    """Clear only caller/child-derived receipt domains.

    Fixed protocol tokens and the closed Package/definition authority fields
    are deliberately absent: accidental substring equality is not data flow.
    """

    canaries = tuple(value for value in provider_canaries if value)
    if not canaries:
        return False
    propagated = False
    for section_name, field in (("session", "session_id"), ("request", "request_id")):
        if _dynamic_value_contains_secret(receipt[section_name][field], canaries):
            receipt[section_name][field] = None
            propagated = True
    if _dynamic_value_contains_secret(receipt["user_message"], canaries):
        receipt["user_message"] = {"sha256": None, "byte_length": None}
        propagated = True
    if _dynamic_value_contains_secret(receipt["local_capability_evidence_identities"], canaries):
        receipt["local_capability_evidence_identities"] = ()
        propagated = True
    if _dynamic_value_contains_secret(receipt["result_pointer"], canaries):
        receipt["result_pointer"] = {
            "path": None, "sha256": None, "size": None, "valid": False,
        }
        propagated = True
    for stream_name in ("stdout", "stderr"):
        if _dynamic_value_contains_secret(receipt[stream_name], canaries):
            receipt[stream_name] = _suppressed_stream_facts()
            propagated = True
    return propagated


def _reject_dynamic_secret_values(
    provider_canaries: Sequence[str], *dynamic_values: Any
) -> None:
    if any(
        _dynamic_value_contains_secret(value, provider_canaries)
        for value in dynamic_values
    ):
        _fail("INVALID_INPUT")


def _located_snapshot(located: Mapping[str, Any]) -> bytes:
    return _canonical_json(_thaw(located), newline=True)


def _preflight(
    *,
    data_root: Any,
    user_message: Any,
    executor_controls: Any,
    package_tool_definition: Any,
    local_capability_evidence: Any,
    receipt: dict[str, Any],
    canary_state: dict[str, Any],
) -> dict[str, Any]:
    message = _scalar_text(user_message, nonempty=False, reason="INVALID_INPUT")
    message_bytes = message.encode("utf-8")
    try:
        data_path = _safe_existing_absolute_directory(data_root)
    except _LaunchError:
        _fail("INVALID_INPUT")
    try:
        located = locate_active_package(data_path)
    except PackageRegistrationError:
        _fail("LOCATOR_FAILED")
    except Exception:
        _fail("LOCATOR_FAILED")
    package_root = Path(located["package_root"])
    receipt["registration"] = {"registration_sha256": located["registration_sha256"]}
    receipt["package"] = {
        "openmontage_release": located["openmontage_release"],
        "openmontage_commit": located["openmontage_commit"],
        "package_root": str(package_root),
    }
    receipt["manifest"] = {"sha256": located["manifest"]["sha256"], "size": located["manifest"]["size"]}
    receipt["lock"] = {
        "sha256": located["lock"]["sha256"], "size": located["lock"]["size"],
        "bundle_sha256": located["lock"]["bundle_sha256"],
    }
    manifest_by_path, lock_by_path = _inventory(package_root, located)
    definition = _validate_definition(package_tool_definition, located, package_root, manifest_by_path, lock_by_path)
    receipt["tool_definition"] = {
        "definition_id": definition["definition_id"], "definition_sha256": definition["definition_sha256"],
        "authority_owner": definition["authority_owner"],
    }
    receipt["tool_file"] = {
        "tool_id": definition["tool_id"], "relative_path": definition["relative_path"],
        "path": str(definition["tool_path"]), "sha256": definition["tool_sha256"],
        "size": definition["tool_size"], "owner": definition["owner"],
    }
    receipt["interpreter"] = dict(definition["interpreter"])
    controls = _validate_controls(executor_controls, definition, data_path)
    secret_text, secret_bytes = _provider_canaries(controls)
    canary_state["text"] = secret_text
    canary_state["bytes"] = secret_bytes
    receipt["provider_environment_names"] = controls["provider_environment_names"]
    _reject_dynamic_secret_values(
        secret_text,
        message,
        controls["session_id"],
        controls["request_id"],
        controls["timeout_seconds"],
        str(controls["result_root"]),
    )
    message_identity = {
        "sha256": hashlib.sha256(message_bytes).hexdigest(),
        "byte_length": len(message_bytes),
    }
    _reject_dynamic_secret_values(secret_text, message_identity)
    receipt["user_message"] = message_identity
    receipt["session"] = {"session_id": controls["session_id"]}
    receipt["request"] = {"request_id": controls["request_id"]}
    local_identities = _validate_local_evidence(
        local_capability_evidence,
        definition["requirements"],
        data_path,
        secret_text,
    )
    receipt["local_capability_evidence_identities"] = local_identities
    return {
        "data_root": data_path, "data_root_input": Path(data_root),
        "message": message, "message_bytes": message_bytes,
        "located": located, "located_snapshot": _located_snapshot(located),
        "package_root": package_root, "definition": definition, "controls": controls,
        "local_identities": local_identities, "local_evidence_input": _thaw(local_capability_evidence),
        "secret_text": secret_text, "secret_bytes": secret_bytes,
    }


def _second_preflight(first: Mapping[str, Any]) -> None:
    try:
        second_data_root = _safe_existing_absolute_directory(first["data_root_input"])
        if second_data_root != first["data_root"]:
            _fail("REGISTRATION_DRIFT")
        second = locate_active_package(first["data_root"])
    except Exception:
        _fail("REGISTRATION_DRIFT")
    if _located_snapshot(second) != first["located_snapshot"]:
        _fail("REGISTRATION_DRIFT")
    definition = first["definition"]
    try:
        definition_bytes = _read_file_bytes(
            definition["definition_path"], reason="REGISTRATION_DRIFT", stop=first["package_root"]
        )
        if definition_bytes != _canonical_json(definition["mapping"], newline=True):
            _fail("REGISTRATION_DRIFT")
        if _hash_file(
            definition["tool_path"], reason="REGISTRATION_DRIFT", stop=first["package_root"]
        ) != (definition["tool_sha256"], definition["tool_size"]):
            _fail("REGISTRATION_DRIFT")
        interpreter = definition["interpreter"]
        if _hash_file(
            Path(interpreter["path"]), reason="REGISTRATION_DRIFT", stop=first["package_root"]
        ) != (interpreter["sha256"], interpreter["size"]):
            _fail("REGISTRATION_DRIFT")
        result_root = _safe_existing_absolute_directory(
            first["controls"]["result_root_input"], within=first["data_root"]
        )
        if result_root != first["controls"]["result_root"]:
            _fail("REGISTRATION_DRIFT")
        local_identities = _validate_local_evidence(
            first["local_evidence_input"],
            definition["requirements"],
            first["data_root"],
            first["secret_text"],
        )
        if local_identities != first["local_identities"]:
            _fail("REGISTRATION_DRIFT")
    except _LaunchError:
        _fail("REGISTRATION_DRIFT")
    except (OSError, RuntimeError):
        _fail("REGISTRATION_DRIFT")


class _StreamCapture:
    def __init__(self, secrets: Sequence[bytes], *, parse_output: bool) -> None:
        self.digest = hashlib.sha256()
        self.size = 0
        self.retained = bytearray()
        self.parse_bytes = bytearray()
        self.parse_output = parse_output
        self.secret_found = False
        self._secrets = tuple(secret for secret in secrets if secret)
        self._overlap = b""
        self.error = False

    def feed(self, chunk: bytes) -> None:
        self.digest.update(chunk)
        self.size += len(chunk)
        if len(self.retained) < _MAX_CAPTURE:
            self.retained.extend(chunk[: _MAX_CAPTURE - len(self.retained)])
        if self.parse_output and len(self.parse_bytes) <= _MAX_RESULT_OUTPUT:
            remaining = _MAX_RESULT_OUTPUT + 1 - len(self.parse_bytes)
            self.parse_bytes.extend(chunk[:remaining])
        combined = self._overlap + chunk
        if any(secret in combined for secret in self._secrets):
            self.secret_found = True
        overlap_length = max((len(secret) - 1 for secret in self._secrets), default=0)
        self._overlap = combined[-overlap_length:] if overlap_length else b""

    def facts(self) -> dict[str, Any]:
        return {"size": self.size, "sha256": self.digest.hexdigest(), "truncated": self.size > _MAX_CAPTURE}


def _read_pipe(pipe: Any, capture: _StreamCapture) -> None:
    try:
        while True:
            chunk = pipe.read(64 * 1024)
            if not chunk:
                break
            capture.feed(chunk)
    except Exception:
        capture.error = True
    finally:
        try:
            pipe.close()
        except Exception:
            capture.error = True


def _write_stdin(pipe: Any, payload: bytes, state: dict[str, bool]) -> None:
    try:
        pipe.write(payload)
        pipe.flush()
    except (BrokenPipeError, OSError, ValueError):
        state["error"] = True
    finally:
        try:
            pipe.close()
        except Exception:
            state["error"] = True


class _WindowsJob:
    """A private kill-on-close Job Object for the one launched process tree."""

    def __init__(self) -> None:
        self.handle: int | None = None
        if os.name != "nt":
            return
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel32.CreateJobObjectW.restype = ctypes.c_void_p
        kernel32.CreateJobObjectW.argtypes = (ctypes.c_void_p, ctypes.c_wchar_p)
        kernel32.SetInformationJobObject.restype = ctypes.c_int
        kernel32.SetInformationJobObject.argtypes = (ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32)
        kernel32.CloseHandle.argtypes = (ctypes.c_void_p,)
        handle = kernel32.CreateJobObjectW(None, None)
        if not handle:
            raise OSError(ctypes.get_last_error(), "CreateJobObjectW")

        class IO_COUNTERS(ctypes.Structure):
            _fields_ = [
                ("ReadOperationCount", ctypes.c_ulonglong), ("WriteOperationCount", ctypes.c_ulonglong),
                ("OtherOperationCount", ctypes.c_ulonglong), ("ReadTransferCount", ctypes.c_ulonglong),
                ("WriteTransferCount", ctypes.c_ulonglong), ("OtherTransferCount", ctypes.c_ulonglong),
            ]

        class BASIC_LIMIT(ctypes.Structure):
            _fields_ = [
                ("PerProcessUserTimeLimit", ctypes.c_longlong), ("PerJobUserTimeLimit", ctypes.c_longlong),
                ("LimitFlags", ctypes.c_uint32), ("MinimumWorkingSetSize", ctypes.c_size_t),
                ("MaximumWorkingSetSize", ctypes.c_size_t), ("ActiveProcessLimit", ctypes.c_uint32),
                ("Affinity", ctypes.c_size_t), ("PriorityClass", ctypes.c_uint32),
                ("SchedulingClass", ctypes.c_uint32),
            ]

        class EXTENDED_LIMIT(ctypes.Structure):
            _fields_ = [
                ("BasicLimitInformation", BASIC_LIMIT), ("IoInfo", IO_COUNTERS),
                ("ProcessMemoryLimit", ctypes.c_size_t), ("JobMemoryLimit", ctypes.c_size_t),
                ("PeakProcessMemoryUsed", ctypes.c_size_t), ("PeakJobMemoryUsed", ctypes.c_size_t),
            ]

        information = EXTENDED_LIMIT()
        information.BasicLimitInformation.LimitFlags = 0x00002000  # JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE
        if not kernel32.SetInformationJobObject(handle, 9, ctypes.byref(information), ctypes.sizeof(information)):
            error = ctypes.get_last_error()
            kernel32.CloseHandle(handle)
            raise OSError(error, "SetInformationJobObject")
        self.handle = int(handle)

    def assign(self, process: subprocess.Popen[bytes]) -> None:
        if os.name != "nt":
            return
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel32.AssignProcessToJobObject.restype = ctypes.c_int
        kernel32.AssignProcessToJobObject.argtypes = (ctypes.c_void_p, ctypes.c_void_p)
        process_handle = ctypes.c_void_p(int(getattr(process, "_handle")))
        if not kernel32.AssignProcessToJobObject(self.handle, process_handle):
            raise OSError(ctypes.get_last_error(), "AssignProcessToJobObject")

    def resume(self, process: subprocess.Popen[bytes]) -> None:
        if os.name != "nt":
            return
        # subprocess closes the primary-thread handle after CreateProcess.  The
        # process handle remains owned by Popen, so NtResumeProcess is the only
        # bounded resume operation here and requires no system thread scan.
        ntdll = ctypes.WinDLL("ntdll", use_last_error=True)
        ntdll.NtResumeProcess.restype = ctypes.c_long
        ntdll.NtResumeProcess.argtypes = (ctypes.c_void_p,)
        status = int(ntdll.NtResumeProcess(ctypes.c_void_p(int(getattr(process, "_handle")))))
        if status != 0:
            raise OSError(status, "NtResumeProcess")

    def active_count(self) -> int:
        if os.name != "nt" or self.handle is None:
            return 0
        kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
        kernel32.QueryInformationJobObject.restype = ctypes.c_int
        kernel32.QueryInformationJobObject.argtypes = (ctypes.c_void_p, ctypes.c_int, ctypes.c_void_p, ctypes.c_uint32, ctypes.c_void_p)

        class BASIC_ACCOUNTING(ctypes.Structure):
            _fields_ = [
                ("TotalUserTime", ctypes.c_longlong), ("TotalKernelTime", ctypes.c_longlong),
                ("ThisPeriodTotalUserTime", ctypes.c_longlong), ("ThisPeriodTotalKernelTime", ctypes.c_longlong),
                ("TotalPageFaultCount", ctypes.c_uint32), ("TotalProcesses", ctypes.c_uint32),
                ("ActiveProcesses", ctypes.c_uint32), ("TotalTerminatedProcesses", ctypes.c_uint32),
            ]

        information = BASIC_ACCOUNTING()
        returned = ctypes.c_uint32()
        if not kernel32.QueryInformationJobObject(self.handle, 1, ctypes.byref(information), ctypes.sizeof(information), ctypes.byref(returned)):
            raise OSError(ctypes.get_last_error(), "QueryInformationJobObject")
        return int(information.ActiveProcesses)

    def terminate(self) -> None:
        if os.name == "nt" and self.handle is not None:
            kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
            kernel32.TerminateJobObject.restype = ctypes.c_int
            kernel32.TerminateJobObject.argtypes = (ctypes.c_void_p, ctypes.c_uint32)
            if not kernel32.TerminateJobObject(self.handle, 1):
                raise OSError(ctypes.get_last_error(), "TerminateJobObject")

    def close(self) -> None:
        if os.name == "nt" and self.handle is not None:
            kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
            kernel32.CloseHandle.argtypes = (ctypes.c_void_p,)
            kernel32.CloseHandle(self.handle)
            self.handle = None


def _group_exists(pid: int, job: _WindowsJob) -> bool:
    if _WINDOWS_PROCESS_PLATFORM:
        return job.active_count() > 0
    try:
        os.killpg(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


def _terminate_group(process: subprocess.Popen[bytes], job: _WindowsJob, *, force: bool) -> None:
    if _WINDOWS_PROCESS_PLATFORM:
        job.terminate()
        return
    try:
        os.killpg(process.pid, signal.SIGKILL if force else signal.SIGTERM)
    except ProcessLookupError:
        return


def _terminate_setup_failure(
    process: subprocess.Popen[bytes],
    job: _WindowsJob,
    *,
    assigned: bool,
    seconds: int,
) -> tuple[bool, int | None]:
    if assigned:
        try:
            job.terminate()
        except Exception:
            pass
    # Assign may have failed, so the Job can be empty.  Always terminate the
    # actual Popen handle as well; never claim cleanup from an unbound Job.
    if process.poll() is None:
        try:
            process.kill()
        except OSError:
            pass
    try:
        process.wait(timeout=seconds)
    except subprocess.TimeoutExpired:
        pass
    residual = process.poll() is None
    if assigned:
        try:
            residual = residual or job.active_count() > 0
        except OSError:
            residual = True
    return not residual, process.poll()


def _wait_group_gone(pid: int, job: _WindowsJob, seconds: int) -> bool:
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        try:
            if not _group_exists(pid, job):
                return True
        except OSError:
            return False
        time.sleep(0.01)
    try:
        return not _group_exists(pid, job)
    except OSError:
        return False


def _safe_environment(first: Mapping[str, Any]) -> dict[str, str]:
    located = first["located"]
    environment: dict[str, str] = {}
    for name in ("SystemRoot", "WINDIR", "COMSPEC", "PATHEXT", "TEMP", "TMP"):
        value = os.environ.get(name)
        if value and "\x00" not in value:
            environment[name] = value
    toolchain = located["required_toolchain"]
    directories = [
        str(Path(located["package_python"]["path"]).parent),
        str(Path(toolchain["ffmpeg"]["ffmpeg"]["path"]).parent),
        str(Path(toolchain["node"]["node"]["path"]).parent),
    ]
    environment["PATH"] = os.pathsep.join(dict.fromkeys(directories))
    environment["PYTHONNOUSERSITE"] = "1"
    environment["PYTHONUTF8"] = "1"
    environment["PYTHONUNBUFFERED"] = "1"
    environment.update(first["controls"]["provider_environment"])
    return environment


def _request_payload(first: Mapping[str, Any]) -> bytes:
    located = first["located"]
    controls = first["controls"]
    request = {
        "schema_version": _REQUEST_SCHEMA,
        "session_id": controls["session_id"],
        "request_id": controls["request_id"],
        "user_message": first["message"],
        "executor_controls": {
            "timeout_seconds": controls["timeout_seconds"],
            "result_root": str(controls["result_root"]),
            "provider_environment_names": list(controls["provider_environment_names"]),
        },
        "package": {
            "registration_sha256": located["registration_sha256"],
            "openmontage_release": located["openmontage_release"],
            "openmontage_commit": located["openmontage_commit"],
        },
        "tool_definition_sha256": first["definition"]["definition_sha256"],
        "local_capability_evidence_identities": [_thaw(item) for item in first["local_identities"]],
    }
    return _canonical_json(request, newline=True)


def _canonical_output_json(value: Any) -> bytes:
    """Canonicalize child output without using preflight error semantics."""

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
    except (TypeError, ValueError, UnicodeEncodeError):
        _fail("OUTPUT_INVALID", "OUTPUT")


def _parse_result(raw: bytes, first: Mapping[str, Any]) -> Mapping[str, Any]:
    if len(raw) > _MAX_RESULT_OUTPUT:
        _fail("OUTPUT_INVALID", "OUTPUT")
    pair_secret_found = False
    try:
        text = raw.decode("utf-8")
        duplicates: list[str] = []

        def object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
            nonlocal pair_secret_found
            result: dict[str, Any] = {}
            for key, value in pairs:
                # Inspect every original pair before dictionary assignment can
                # overwrite a duplicate.  Nested objects pass through this
                # same hook before their parent receives the reconstructed map.
                if _dynamic_value_contains_secret(
                    (key, value), first["secret_text"]
                ):
                    pair_secret_found = True
                if key in result:
                    duplicates.append(key)
                result[key] = value
            return result

        def finite_float(value: str) -> float:
            parsed = float(value)
            if not math.isfinite(parsed):
                raise ValueError
            return parsed

        decoder = json.JSONDecoder(
            object_pairs_hook=object_pairs,
            parse_constant=lambda _x: (_ for _ in ()).throw(ValueError()),
            parse_float=finite_float,
        )
        value, end = decoder.raw_decode(text)
    except (UnicodeError, ValueError, TypeError, json.JSONDecodeError):
        if pair_secret_found:
            _fail("SECRET_DISCLOSURE_DETECTED", "OUTPUT")
        _fail("OUTPUT_INVALID", "OUTPUT")
    # The complete decoded child object is untrusted dynamic data.  Scan it
    # before canonical-shape or closed-schema rejection so an escaped secret in
    # an unknown key/value or invalid protocol field still suppresses stdout.
    if pair_secret_found or _dynamic_value_contains_secret(
        value, first["secret_text"]
    ):
        _fail("SECRET_DISCLOSURE_DETECTED", "OUTPUT")
    if text[end:].strip():
        _fail("OUTPUT_INVALID", "OUTPUT")
    if (
        duplicates
        or not isinstance(value, Mapping)
        or _canonical_output_json(value) != raw
    ):
        _fail("OUTPUT_INVALID", "OUTPUT")
    result = _mapping(value, _RESULT_FIELDS, "OUTPUT_INVALID")
    controls = first["controls"]
    if result["schema_version"] != _RESULT_SCHEMA or result["session_id"] != controls["session_id"] or result["request_id"] != controls["request_id"]:
        _fail("OUTPUT_INVALID", "OUTPUT")
    if result["outcome"] == "SUCCEEDED":
        if result["error"] is not None or not isinstance(result["result_pointer"], Mapping):
            _fail("OUTPUT_INVALID", "OUTPUT")
    elif result["outcome"] == "FAILED":
        if result["result_pointer"] is not None:
            _fail("OUTPUT_INVALID", "OUTPUT")
        error = _mapping(result["error"], frozenset({"code", "origin", "message"}), "OUTPUT_INVALID")
        if not all(isinstance(error[field], str) for field in ("code", "origin", "message")):
            _fail("OUTPUT_INVALID", "OUTPUT")
    else:
        _fail("OUTPUT_INVALID", "OUTPUT")
    return result


def _validate_result_pointer(value: Any, result_root: Path) -> dict[str, Any]:
    pointer = _mapping(value, frozenset({"relative_path", "sha256", "size"}), "RESULT_POINTER_INVALID")
    relative = _safe_relative(pointer["relative_path"], "RESULT_POINTER_INVALID")
    expected_digest = _sha256(pointer["sha256"], "RESULT_POINTER_INVALID")
    expected_size = pointer["size"]
    if type(expected_size) is not int or expected_size < 0:
        _fail("RESULT_POINTER_INVALID", "RESULT")
    try:
        path = result_root.joinpath(*PurePosixPath(relative).parts)
        _validate_components(path, stop=result_root)
        resolved = path.resolve(strict=True)
        resolved.relative_to(result_root.resolve(strict=True))
        pathname = os.stat(path, follow_symlinks=False)
        if not _regular_unaliased(pathname):
            _fail("RESULT_POINTER_INVALID", "RESULT")
        digest, total = _hash_file(
            path, reason="RESULT_POINTER_INVALID", stop=result_root
        )
        # Revalidate the lexical path once more after the same-handle hash
        # checks.  The receipt path is emitted only for the still-current name.
        _validate_components(path, stop=result_root)
        if (
            path.resolve(strict=True) != resolved
            or total != expected_size
            or digest != expected_digest
        ):
            _fail("RESULT_POINTER_INVALID", "RESULT")
        return {"path": str(resolved), "sha256": expected_digest, "size": expected_size, "valid": True}
    except _LaunchError:
        raise
    except (OSError, RuntimeError, ValueError):
        _fail("RESULT_POINTER_INVALID", "RESULT")


def launch_session_tool(
    data_root: str | os.PathLike[str],
    user_message: str,
    executor_controls: Mapping[str, Any],
    package_tool_definition: Mapping[str, Any],
    local_capability_evidence: Sequence[Mapping[str, Any]] = (),
    cancel_event: threading.Event | None = None,
) -> Mapping[str, Any]:
    """Launch one definition-bound Package tool and always return a frozen receipt."""

    start_ns = time.monotonic_ns()
    receipt = _empty_receipt(start_ns)
    process: subprocess.Popen[bytes] | None = None
    job: _WindowsJob | None = None
    job_assigned = False
    first: dict[str, Any] | None = None
    raw_secret_text, raw_secret_bytes, raw_secret_complete = _raw_provider_canaries(
        executor_controls
    )
    canary_state: dict[str, Any] = {
        "text": raw_secret_text,
        "bytes": raw_secret_bytes,
        "raw_complete": raw_secret_complete,
    }
    try:
        if cancel_event is not None and not isinstance(cancel_event, threading.Event):
            _fail("INVALID_INPUT")

        # Safely recover only non-authoritative receipt hints before the entry-cancel gate.
        if raw_secret_complete and isinstance(executor_controls, Mapping):
            try:
                session_hint = executor_controls.get("session_id")
                request_hint = executor_controls.get("request_id")
            except Exception:
                session_hint = request_hint = None
            if (
                isinstance(session_hint, str)
                and _IDENTIFIER_RE.fullmatch(session_hint)
                and not _dynamic_value_contains_secret(session_hint, raw_secret_text)
            ):
                receipt["session"] = {"session_id": session_hint}
            if (
                isinstance(request_hint, str)
                and _IDENTIFIER_RE.fullmatch(request_hint)
                and not _dynamic_value_contains_secret(request_hint, raw_secret_text)
            ):
                receipt["request"] = {"request_id": request_hint}
        if raw_secret_complete and isinstance(user_message, str):
            try:
                message_hint = user_message.encode("utf-8")
            except UnicodeEncodeError:
                pass
            else:
                if (
                    not any(0xD800 <= ord(character) <= 0xDFFF for character in user_message)
                    and not _contains_secret(raw_secret_bytes, message_hint)
                ):
                    receipt["user_message"] = {
                        "sha256": hashlib.sha256(message_hint).hexdigest(),
                        "byte_length": len(message_hint),
                    }

        if cancel_event is not None and cancel_event.is_set():
            receipt["cancelled"] = True
            _set_failure(receipt, "CANCELLED", "CANCELLED_BEFORE_SPAWN", "CANCEL")
            return _finish(receipt, start_ns, canary_state["text"])

        first = _preflight(
            data_root=data_root,
            user_message=user_message,
            executor_controls=executor_controls,
            package_tool_definition=package_tool_definition,
            local_capability_evidence=local_capability_evidence,
            receipt=receipt,
            canary_state=canary_state,
        )
        _second_preflight(first)
        request_bytes = _request_payload(first)
        _reject_dynamic_secret_values(
            first["secret_text"],
            first["message"],
            first["controls"]["session_id"],
            first["controls"]["request_id"],
            first["controls"]["timeout_seconds"],
            str(first["controls"]["result_root"]),
            first["local_identities"],
        )
        stdout_capture = _StreamCapture(first["secret_bytes"], parse_output=True)
        stderr_capture = _StreamCapture(first["secret_bytes"], parse_output=False)
        stdin_state = {"error": False}

        popen_kwargs: dict[str, Any] = {
            "args": first["definition"]["argv"],
            "stdin": subprocess.PIPE,
            "stdout": subprocess.PIPE,
            "stderr": subprocess.PIPE,
            "cwd": str(first["package_root"]),
            "env": _safe_environment(first),
            "shell": False,
            "bufsize": 0,
        }
        if _WINDOWS_PROCESS_PLATFORM:
            popen_kwargs["creationflags"] = (
                getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0x00000200)
                | getattr(subprocess, "CREATE_SUSPENDED", 0x00000004)
            )
        else:
            popen_kwargs["start_new_session"] = True
        try:
            job = _WindowsJob()
        except OSError:
            _fail("EVIDENCE_INCOMPLETE")
        try:
            process = subprocess.Popen(**popen_kwargs)
        except OSError:
            _set_failure(receipt, "SPAWN_FAILED", "SPAWN_OS_ERROR", "SPAWN")
            return _finish(receipt, start_ns, canary_state["text"])
        receipt["launched"] = True
        receipt["spawn_count"] = 1
        receipt["pid"] = process.pid
        receipt["started_at_utc"] = _utc_now()
        try:
            job.assign(process)
            job_assigned = _WINDOWS_PROCESS_PLATFORM
            job.resume(process)
        except Exception:
            receipt["residual_process"]["termination_attempted"] = True
            succeeded, exit_code = _terminate_setup_failure(
                process,
                job,
                assigned=job_assigned,
                seconds=first["controls"]["termination_grace_seconds"],
            )
            receipt["residual_process"]["termination_succeeded"] = succeeded
            receipt["residual_process"]["detected"] = not succeeded
            receipt["exit_code"] = exit_code
            if succeeded:
                _set_failure(receipt, "INCOMPLETE", "EVIDENCE_INCOMPLETE", "RESIDUAL")
            else:
                _set_failure(
                    receipt,
                    "RESIDUAL_PROCESS",
                    "RESIDUAL_PROCESS_DETECTED",
                    "RESIDUAL",
                )
            return _finish(receipt, start_ns, canary_state["text"])

        assert process.stdin is not None and process.stdout is not None and process.stderr is not None
        stdout_thread = threading.Thread(target=_read_pipe, args=(process.stdout, stdout_capture), daemon=True)
        stderr_thread = threading.Thread(target=_read_pipe, args=(process.stderr, stderr_capture), daemon=True)
        stdin_thread = threading.Thread(target=_write_stdin, args=(process.stdin, request_bytes, stdin_state), daemon=True)
        stdout_thread.start()
        stderr_thread.start()
        stdin_thread.start()

        deadline_ns = time.monotonic_ns() + first["controls"]["timeout_seconds"] * 1_000_000_000
        event_kind: str | None = None
        while True:
            observed_ns = time.monotonic_ns()
            if cancel_event is not None and cancel_event.is_set():
                event_kind = "cancel"
                receipt["cancelled"] = True
                break
            if observed_ns >= deadline_ns:
                event_kind = "timeout"
                receipt["timed_out"] = True
                break
            if process.poll() is not None:
                break
            time.sleep(0.005)

        if event_kind is not None:
            receipt["residual_process"]["termination_attempted"] = True
            try:
                _terminate_group(process, job, force=False)
            except OSError:
                pass
            gone = _wait_group_gone(process.pid, job, first["controls"]["termination_grace_seconds"])
            if not gone:
                try:
                    _terminate_group(process, job, force=True)
                except OSError:
                    pass
                gone = _wait_group_gone(process.pid, job, first["controls"]["termination_grace_seconds"])
            receipt["residual_process"]["termination_succeeded"] = gone
        try:
            process.wait(timeout=first["controls"]["termination_grace_seconds"])
        except subprocess.TimeoutExpired:
            pass
        receipt["exit_code"] = process.poll()

        stdin_thread.join(timeout=first["controls"]["termination_grace_seconds"])
        stdout_thread.join(timeout=first["controls"]["termination_grace_seconds"])
        stderr_thread.join(timeout=first["controls"]["termination_grace_seconds"])
        receipt["stdout"] = (
            _suppressed_stream_facts()
            if stdout_capture.secret_found
            else stdout_capture.facts()
        )
        receipt["stderr"] = (
            _suppressed_stream_facts()
            if stderr_capture.secret_found
            else stderr_capture.facts()
        )
        if stdout_capture.secret_found:
            stdout_capture.retained.clear()
            stdout_capture.parse_bytes.clear()
        if stderr_capture.secret_found:
            stderr_capture.retained.clear()
            stderr_capture.parse_bytes.clear()

        residual = False
        try:
            residual = _group_exists(process.pid, job)
        except OSError:
            residual = True
        if residual:
            receipt["residual_process"]["detected"] = True
            receipt["residual_process"]["termination_attempted"] = True
            receipt["residual_process"]["observed_pids"] = ()
            try:
                _terminate_group(process, job, force=True)
            except OSError:
                pass
            gone = _wait_group_gone(process.pid, job, first["controls"]["termination_grace_seconds"])
            receipt["residual_process"]["termination_succeeded"] = gone
            _set_failure(receipt, "RESIDUAL_PROCESS", "RESIDUAL_PROCESS_DETECTED", "RESIDUAL")
            return _finish(receipt, start_ns, canary_state["text"])
        if stdout_capture.secret_found or stderr_capture.secret_found:
            _set_failure(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", "OUTPUT")
            return _finish(receipt, start_ns, canary_state["text"])
        if event_kind == "cancel":
            _set_failure(receipt, "CANCELLED", "CANCELLED", "CANCEL")
            return _finish(receipt, start_ns, canary_state["text"])
        if event_kind == "timeout":
            _set_failure(receipt, "TIMED_OUT", "TIMEOUT", "TIMEOUT")
            return _finish(receipt, start_ns, canary_state["text"])
        if receipt["exit_code"] is not None and receipt["exit_code"] != 0:
            _set_failure(receipt, "EXITED_NONZERO", "EXITED_NONZERO", "CHILD")
            return _finish(receipt, start_ns, canary_state["text"])
        if (
            receipt["exit_code"] is None
            or stdin_state["error"]
            or stdout_capture.error
            or stderr_capture.error
            or stdout_thread.is_alive()
            or stderr_thread.is_alive()
            or stdin_thread.is_alive()
        ):
            _set_failure(receipt, "INCOMPLETE", "EVIDENCE_INCOMPLETE", "OUTPUT")
            return _finish(receipt, start_ns, canary_state["text"])
        try:
            child_result = _parse_result(bytes(stdout_capture.parse_bytes), first)
        except _LaunchError as exc:
            if exc.reason_code == "SECRET_DISCLOSURE_DETECTED":
                receipt["stdout"] = _suppressed_stream_facts()
                stdout_capture.retained.clear()
                stdout_capture.parse_bytes.clear()
            _set_failure(receipt, "INCOMPLETE", exc.reason_code, exc.origin)
            return _finish(receipt, start_ns, canary_state["text"])
        if child_result["outcome"] == "FAILED":
            _set_failure(receipt, "CHILD_REPORTED_FAILURE", "CHILD_REPORTED_FAILURE", "CHILD")
            return _finish(receipt, start_ns, canary_state["text"])
        try:
            receipt["result_pointer"] = _validate_result_pointer(
                child_result["result_pointer"], first["controls"]["result_root"]
            )
        except _LaunchError:
            _set_failure(receipt, "INCOMPLETE", "RESULT_POINTER_INVALID", "RESULT")
            return _finish(receipt, start_ns, canary_state["text"])
        receipt["outcome"] = "EXITED_SUCCESS"
        receipt["reason_code"] = "NONE"
        receipt["error"] = None
        return _finish(receipt, start_ns, canary_state["text"])
    except _LaunchError as exc:
        _set_failure(receipt, "PRELAUNCH_BLOCKED" if process is None else "INCOMPLETE", exc.reason_code, exc.origin)
        return _finish(receipt, start_ns, canary_state["text"])
    except Exception:
        _set_failure(receipt, "PRELAUNCH_BLOCKED" if process is None else "INCOMPLETE", "EVIDENCE_INCOMPLETE", "PREFLIGHT" if process is None else "OUTPUT")
        return _finish(receipt, start_ns, canary_state["text"])
    finally:
        if process is not None and process.poll() is None:
            try:
                if _WINDOWS_PROCESS_PLATFORM and not job_assigned:
                    process.kill()
                elif job is not None:
                    _terminate_group(process, job, force=True)
                process.wait(timeout=1)
            except Exception:
                pass
        if job is not None:
            try:
                job.close()
            except Exception:
                pass


__all__ = ["launch_session_tool"]
