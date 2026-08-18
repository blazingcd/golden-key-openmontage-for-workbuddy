"""Bounded preparation of optional OpenMontage composition capabilities.

Only Remotion and HyperFrames are in this module's catalog.  Detection is read-only
and limited to a managed DataRoot target, explicit candidate paths, and normal
command resolution.  Integration is possible only after a decision bound to the
exact deterministic plan returned by an earlier call.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import tempfile
import time
import urllib.request
import unicodedata
import uuid
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence
from urllib.parse import urlsplit


_CAPABILITIES = ("remotion", "hyperframes")
_RESULTS = frozenset(
    {"DETECTION_REPORT", "CONSENT_REQUIRED", "INTEGRATED", "SKIPPED", "BLOCKED"}
)
_FACTS = frozenset({"PRESENT", "MISSING", "INCOMPATIBLE", "NOT_INTEGRATED"})
_DECISIONS = frozenset({"approve", "decline", "defer"})
_DEFINITION_REQUIRED = frozenset(
    {
        "capability",
        "definition_sha256",
        "version",
        "verified_entrypoint",
        "approved_mainland_sources",
        "assets",
    }
)
_DEFINITION_OPTIONAL = frozenset(
    {"explicit_registered_or_configured_candidate_paths", "normal_command_name"}
)
_SOURCE_FIELDS = frozenset({"filename", "url"})
_ASSET_FIELDS = frozenset(
    {"filename", "size", "sha256", "license", "managed_target"}
)
_DECISION_FIELDS = frozenset(
    {"decision", "capability", "definition_sha256", "plan_sha256"}
)
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_VERSION_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9.+_-]{0,127}$")
_LICENSE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 .()+_-]{0,127}$")
_LOCK_TIMEOUT_SECONDS = 5.0
_LOCK_RETRY_SECONDS = 0.05
_WINDOWS_RESERVED_STEMS = frozenset(
    {
        "con",
        "prn",
        "aux",
        "nul",
        *(f"com{number}" for number in range(1, 10)),
        *(f"lpt{number}" for number in range(1, 10)),
    }
)


class _ContractError(ValueError):
    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[no-untyped-def]
        return None


def _fail(code: str, message: str) -> None:
    raise _ContractError(code, message)


def _blocked(code: str, message: str) -> dict[str, Any]:
    return {"result": "BLOCKED", "reason_code": code, "message": message}


def _canonical_hash(value: Mapping[str, Any]) -> str:
    try:
        encoded = json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError, UnicodeEncodeError) as exc:
        _fail("INVALID_DEFINITION", f"value is not canonical JSON: {exc}")
    return hashlib.sha256(encoded).hexdigest()


def _require_mapping(value: Any, label: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        _fail("INVALID_DEFINITION", f"{label} must be an object")
    if not all(isinstance(key, str) for key in value):
        _fail("INVALID_DEFINITION", f"{label} keys must be strings")
    return value


def _require_exact_fields(
    value: Mapping[str, Any], required: frozenset[str], optional: frozenset[str], label: str
) -> None:
    keys = frozenset(value)
    missing = required - keys
    unknown = keys - required - optional
    if missing:
        _fail("INVALID_DEFINITION", f"{label} is missing fields: {sorted(missing)}")
    if unknown:
        _fail("INVALID_DEFINITION", f"{label} has unknown fields: {sorted(unknown)}")


def _relative_path(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        _fail("PATH_VIOLATION", f"{label} must be a non-empty POSIX relative path")
    path = PurePosixPath(value)
    if path.is_absolute() or value != path.as_posix():
        _fail("PATH_VIOLATION", f"{label} must be a normalized relative path")
    if not path.parts or not unicodedata.is_normalized("NFC", value):
        _fail("PATH_VIOLATION", f"{label} is empty or not Unicode-normalized")
    if any(
        part in {"", ".", ".."}
        or ":" in part
        or part.endswith((" ", "."))
        or part.split(".", 1)[0].casefold() in _WINDOWS_RESERVED_STEMS
        for part in path.parts
    ):
        _fail("PATH_VIOLATION", f"{label} escapes or aliases its managed root")
    return value


def _approved_command(capability: str, value: Any) -> str:
    if not isinstance(value, str) or not value:
        _fail("INVALID_DEFINITION", "normal_command_name must be a non-empty string")
    allowed = {capability, f"{capability}.cmd", f"{capability}.exe"}
    if value.casefold() not in allowed:
        _fail("INVALID_DEFINITION", f"normal command is not fixed for {capability}")
    return value


def _approved_url(value: Any) -> str:
    if not isinstance(value, str):
        _fail("INVALID_DEFINITION", "source URL must be a string")
    parsed = urlsplit(value)
    try:
        port = parsed.port
    except ValueError:
        _fail("UNAPPROVED_SOURCE", "optional asset URL has an invalid port")
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
        _fail("UNAPPROVED_SOURCE", "optional assets require an exact npmmirror HTTPS URL")
    return value


def _validate_definitions(value: Any) -> dict[str, dict[str, Any]]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        _fail("INVALID_DEFINITION", "capability_definitions must be a two-item sequence")
    definitions: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(value):
        definition = _require_mapping(raw, f"capability_definitions[{index}]")
        _require_exact_fields(
            definition,
            _DEFINITION_REQUIRED,
            _DEFINITION_OPTIONAL,
            f"capability_definitions[{index}]",
        )
        capability = definition["capability"]
        if capability not in _CAPABILITIES:
            _fail("INVALID_CAPABILITY", "catalog contains only remotion and hyperframes")
        if capability in definitions:
            _fail("INVALID_DEFINITION", f"duplicate capability: {capability}")
        definition_sha256 = definition["definition_sha256"]
        if not isinstance(definition_sha256, str) or not _SHA256_RE.fullmatch(
            definition_sha256
        ):
            _fail("INVALID_DEFINITION", "definition_sha256 must be lowercase SHA-256")
        version = definition["version"]
        if not isinstance(version, str) or not _VERSION_RE.fullmatch(version):
            _fail("INVALID_DEFINITION", "version is missing or unsafe")
        entrypoint = _relative_path(definition["verified_entrypoint"], "verified_entrypoint")

        raw_sources = definition["approved_mainland_sources"]
        if isinstance(raw_sources, (str, bytes)) or not isinstance(raw_sources, Sequence):
            _fail("INVALID_DEFINITION", "approved_mainland_sources must be a sequence")
        sources: dict[str, str] = {}
        for source_index, raw_source in enumerate(raw_sources):
            source = _require_mapping(raw_source, f"approved_mainland_sources[{source_index}]")
            _require_exact_fields(source, _SOURCE_FIELDS, frozenset(), "mainland source")
            filename = _relative_path(source["filename"], "source filename")
            if "/" in filename:
                _fail("INVALID_DEFINITION", "source filename cannot contain directories")
            if filename in sources:
                _fail("INVALID_DEFINITION", f"duplicate source filename: {filename}")
            sources[filename] = _approved_url(source["url"])

        raw_assets = definition["assets"]
        if isinstance(raw_assets, (str, bytes)) or not isinstance(raw_assets, Sequence):
            _fail("INVALID_DEFINITION", "assets must be a non-empty sequence")
        assets: list[dict[str, Any]] = []
        targets: set[str] = set()
        for asset_index, raw_asset in enumerate(raw_assets):
            asset = _require_mapping(raw_asset, f"assets[{asset_index}]")
            _require_exact_fields(asset, _ASSET_FIELDS, frozenset(), "asset")
            filename = _relative_path(asset["filename"], "asset filename")
            if "/" in filename or filename not in sources:
                _fail("INVALID_DEFINITION", "each asset needs one same-named approved source")
            size = asset["size"]
            if isinstance(size, bool) or not isinstance(size, int) or size < 0:
                _fail("INVALID_DEFINITION", "asset size must be a non-negative integer")
            sha256 = asset["sha256"]
            if not isinstance(sha256, str) or not _SHA256_RE.fullmatch(sha256):
                _fail("INVALID_DEFINITION", "asset sha256 must be lowercase SHA-256")
            license_name = asset["license"]
            if not isinstance(license_name, str) or not _LICENSE_RE.fullmatch(license_name):
                _fail("INVALID_DEFINITION", "asset license is missing or unsafe")
            managed_target = _relative_path(asset["managed_target"], "asset managed_target")
            if managed_target in targets:
                _fail("INVALID_DEFINITION", f"duplicate managed target: {managed_target}")
            targets.add(managed_target)
            assets.append(
                {
                    "filename": filename,
                    "size": size,
                    "sha256": sha256,
                    "license": license_name,
                    "managed_target": managed_target,
                    "source_url": sources[filename],
                }
            )
        assets.sort(key=lambda item: (item["managed_target"], item["filename"]))
        if not assets or set(sources) != {asset["filename"] for asset in assets}:
            _fail("INVALID_DEFINITION", "sources and assets must form a non-empty one-to-one set")
        if entrypoint not in targets:
            _fail("INVALID_DEFINITION", "verified_entrypoint must be one managed asset")

        explicit_raw = definition.get("explicit_registered_or_configured_candidate_paths", [])
        if isinstance(explicit_raw, (str, bytes)) or not isinstance(explicit_raw, Sequence):
            _fail("INVALID_DEFINITION", "explicit candidate paths must be a sequence")
        explicit: list[str] = []
        for candidate in explicit_raw:
            if not isinstance(candidate, (str, os.PathLike)):
                _fail("INVALID_DEFINITION", "explicit candidate path must be path-like")
            path = Path(candidate)
            if not path.is_absolute():
                _fail("PATH_VIOLATION", "explicit candidate paths must be absolute")
            explicit.append(str(path))

        command = None
        if "normal_command_name" in definition:
            command = _approved_command(capability, definition["normal_command_name"])
        definitions[capability] = {
            "capability": capability,
            "definition_sha256": definition_sha256,
            "version": version,
            "verified_entrypoint": entrypoint,
            "assets": assets,
            "explicit_paths": explicit,
            "normal_command_name": command,
        }
    if set(definitions) != set(_CAPABILITIES):
        _fail("INVALID_DEFINITION", "definitions must contain remotion and hyperframes exactly once")
    return definitions


def _validate_decisions(value: Any) -> dict[str, dict[str, str]]:
    if value is None:
        return {}
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        _fail("INVALID_DECISION", "user_decisions must be a sequence")
    decisions: dict[str, dict[str, str]] = {}
    for index, raw in enumerate(value):
        decision = _require_mapping(raw, f"user_decisions[{index}]")
        keys = frozenset(decision)
        if keys != _DECISION_FIELDS:
            _fail("INVALID_DECISION", "decision fields must be exact and complete")
        capability = decision["capability"]
        if capability not in _CAPABILITIES or capability in decisions:
            _fail("INVALID_DECISION", "decision capability is invalid or duplicated")
        action = decision["decision"]
        if action not in _DECISIONS:
            _fail("INVALID_DECISION", "decision must be approve, decline, or defer")
        for field in ("definition_sha256", "plan_sha256"):
            if not isinstance(decision[field], str) or not _SHA256_RE.fullmatch(decision[field]):
                _fail("INVALID_DECISION", f"{field} must be lowercase SHA-256")
        decisions[capability] = dict(decision)
    return decisions


def _managed_root(data_root: Path, definition: Mapping[str, Any]) -> Path:
    return (
        data_root
        / "Runtime"
        / "Composition"
        / definition["capability"]
        / definition["definition_sha256"]
    )


def _ensure_managed_descendant(data_root: Path, path: Path) -> None:
    resolved_root = data_root.resolve(strict=False)
    resolved_path = path.resolve(strict=False)
    try:
        resolved_path.relative_to(resolved_root)
    except ValueError:
        _fail("PATH_VIOLATION", "managed path escapes DataRoot")
    relative = path.relative_to(data_root)
    current = data_root
    for component in relative.parts:
        current = current / component
        if not current.exists() and not current.is_symlink():
            continue
        try:
            metadata = current.lstat()
        except OSError as exc:
            _fail("PATH_VIOLATION", f"managed path cannot be inspected: {exc}")
        attributes = getattr(metadata, "st_file_attributes", 0)
        if current.is_symlink() or attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0):
            _fail("PATH_VIOLATION", "managed path contains a link or reparse point")


def _entrypoint_for(candidate: Path, relative_entrypoint: str) -> Path:
    if candidate.is_file():
        return candidate
    return candidate / Path(*PurePosixPath(relative_entrypoint).parts)


def _probe(entrypoint: Path, expected_version: str) -> tuple[bool, dict[str, Any]]:
    if not entrypoint.is_file():
        return False, {"reason": "ENTRYPOINT_MISSING", "entrypoint": str(entrypoint)}
    try:
        completed = subprocess.run(
            [str(entrypoint), "--version"],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
            shell=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return False, {"reason": "PROBE_FAILED", "entrypoint": str(entrypoint), "detail": str(exc)}
    output = (completed.stdout + "\n" + completed.stderr).strip()
    version_pattern = re.compile(
        rf"(?<![A-Za-z0-9]){re.escape(expected_version)}(?![A-Za-z0-9])"
    )
    compatible = completed.returncode == 0 and version_pattern.search(output) is not None
    return compatible, {
        "reason": "COMPATIBLE" if compatible else "VERSION_OR_PROBE_MISMATCH",
        "entrypoint": str(entrypoint.resolve(strict=False)),
        "exit_code": completed.returncode,
        "version_output": output[:512],
    }


def _asset_evidence(root: Path, definition: Mapping[str, Any]) -> tuple[bool, list[dict[str, Any]]]:
    evidence: list[dict[str, Any]] = []
    valid = True
    expected_targets = {asset["managed_target"] for asset in definition["assets"]}
    actual_targets: set[str] = set()
    if root.is_dir():
        for current_root, child_directories, child_files in os.walk(root, followlinks=False):
            current = Path(current_root)
            for name in list(child_directories):
                child = current / name
                try:
                    metadata = child.lstat()
                except OSError:
                    valid = False
                    continue
                attributes = getattr(metadata, "st_file_attributes", 0)
                if child.is_symlink() or attributes & getattr(
                    stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0
                ):
                    valid = False
                    child_directories.remove(name)
            for name in child_files:
                child = current / name
                relative = child.relative_to(root).as_posix()
                actual_targets.add(relative)
                try:
                    metadata = child.lstat()
                except OSError:
                    valid = False
                    continue
                attributes = getattr(metadata, "st_file_attributes", 0)
                if child.is_symlink() or attributes & getattr(
                    stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0
                ):
                    valid = False
    if actual_targets != expected_targets:
        valid = False
    for asset in definition["assets"]:
        path = root / Path(*PurePosixPath(asset["managed_target"]).parts)
        item: dict[str, Any] = {
            "managed_target": asset["managed_target"],
            "expected_size": asset["size"],
            "expected_sha256": asset["sha256"],
            "license": asset["license"],
            "exists": path.is_file(),
        }
        if path.is_file():
            try:
                payload = path.read_bytes()
            except OSError as exc:
                item["error"] = str(exc)
                valid = False
            else:
                item["size"] = len(payload)
                item["sha256"] = hashlib.sha256(payload).hexdigest()
                if item["size"] != asset["size"] or item["sha256"] != asset["sha256"]:
                    valid = False
        else:
            valid = False
        evidence.append(item)
    return valid, evidence


def _detect_one(data_root: Path, definition: Mapping[str, Any]) -> dict[str, Any]:
    managed = _managed_root(data_root, definition)
    _ensure_managed_descendant(data_root, managed)
    candidates: list[tuple[str, Path, Path]] = [
        ("managed", managed, _entrypoint_for(managed, definition["verified_entrypoint"]))
    ]
    for candidate_text in definition["explicit_paths"]:
        candidate = Path(candidate_text)
        candidates.append(("explicit", candidate, _entrypoint_for(candidate, definition["verified_entrypoint"])))
    if definition["normal_command_name"]:
        resolved = shutil.which(definition["normal_command_name"])
        if resolved:
            command = Path(resolved)
            candidates.append(("PATH", command, command))

    incompatible: list[dict[str, Any]] = []
    for source, root, entrypoint in candidates:
        if not entrypoint.is_file():
            continue
        compatible, probe = _probe(entrypoint, definition["version"])
        assets_valid = True
        asset_evidence: list[dict[str, Any]] = []
        if source == "managed":
            assets_valid, asset_evidence = _asset_evidence(root, definition)
        if compatible and assets_valid:
            evidence = {
                "status": "PRESENT",
                "capability": definition["capability"],
                "definition_sha256": definition["definition_sha256"],
                "runtime_root": str(root.resolve(strict=False)),
                "verified_entrypoint": probe["entrypoint"],
                "version_evidence": probe,
                "asset_evidence": asset_evidence,
                "source": source,
            }
            return {"capability": definition["capability"], "status": "PRESENT", "evidence": evidence}
        incompatible.append(
            {"source": source, "runtime_root": str(root.resolve(strict=False)), "probe": probe, "asset_evidence": asset_evidence}
        )
    if incompatible:
        return {
            "capability": definition["capability"],
            "status": "INCOMPATIBLE",
            "candidates": incompatible,
        }
    return {"capability": definition["capability"], "status": "MISSING"}


def _make_plan(data_root: Path, definition: Mapping[str, Any], fact: Mapping[str, Any]) -> dict[str, Any]:
    target_root = _managed_root(data_root, definition)
    assets = [
        {
            "filename": asset["filename"],
            "source_url": asset["source_url"],
            "size": asset["size"],
            "sha256": asset["sha256"],
            "license": asset["license"],
            "managed_target": asset["managed_target"],
            "preparation": "verified_asset_copy",
        }
        for asset in definition["assets"]
    ]
    body: dict[str, Any] = {
        "capability": definition["capability"],
        "definition_sha256": definition["definition_sha256"],
        "detected_status": fact["status"],
        "detection_sha256": _canonical_hash(dict(fact)),
        "version": definition["version"],
        "verified_entrypoint": definition["verified_entrypoint"],
        "managed_runtime_root": str(target_root),
        "assets": assets,
        "total_download_size": sum(asset["size"] for asset in assets),
    }
    return {**body, "plan_sha256": _canonical_hash(body)}


def _download_asset(url: str, destination: Path) -> str:
    """Download one exact asset; tests replace this private transport boundary."""
    request = urllib.request.Request(url, headers={"User-Agent": "golden-key-workbuddy-shell-v2"})
    opener = urllib.request.build_opener(_NoRedirect)
    with opener.open(request, timeout=30) as response:
        final_url = response.geturl()
        with destination.open("xb") as output:
            shutil.copyfileobj(response, output)
    return final_url


def _remove_owned_lock(lock_path: Path, token: str) -> None:
    try:
        if lock_path.read_text(encoding="ascii") == token:
            lock_path.unlink()
    except (FileNotFoundError, OSError, UnicodeError):
        pass


def _acquire_lock(
    lock_path: Path,
    token: str,
    data_root: Path,
    definition: Mapping[str, Any],
) -> bool:
    deadline = time.monotonic() + _LOCK_TIMEOUT_SECONDS
    while True:
        try:
            descriptor = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError:
            current = _detect_one(data_root, definition)
            if current["status"] == "PRESENT" and current["evidence"]["source"] == "managed":
                return False
            if time.monotonic() >= deadline:
                _fail("INTEGRATION_FAILED", "capability preparation lock remained busy")
            time.sleep(_LOCK_RETRY_SECONDS)
            continue
        except OSError as exc:
            _fail("INTEGRATION_FAILED", f"cannot acquire preparation lock: {exc}")
        else:
            with os.fdopen(descriptor, "w", encoding="ascii") as lock_file:
                lock_file.write(token)
            return True


def _cleanup_empty_directories(paths: Sequence[Path]) -> None:
    for path in paths:
        try:
            path.rmdir()
        except OSError:
            pass


def _integrate_one(data_root: Path, definition: Mapping[str, Any], plan: Mapping[str, Any]) -> dict[str, Any]:
    target = _managed_root(data_root, definition)
    cache_root = data_root / "Caches" / "optional-runtime"
    _ensure_managed_descendant(data_root, target)
    _ensure_managed_descendant(data_root, cache_root)
    lock_path = cache_root / f"{definition['capability']}-{definition['definition_sha256']}.lock"
    token = uuid.uuid4().hex
    staging: Path | None = None
    lock_owned = False
    created_cleanup = [
        target.parent,
        target.parent.parent,
        target.parent.parent.parent,
    ]
    try:
        cache_root.mkdir(parents=True, exist_ok=True)
        lock_owned = _acquire_lock(lock_path, token, data_root, definition)
        current = _detect_one(data_root, definition)
        if current["status"] == "PRESENT" and current["evidence"]["source"] == "managed":
            evidence = dict(current["evidence"])
            evidence["status"] = "INTEGRATED"
            evidence["plan_sha256"] = plan["plan_sha256"]
            evidence["reused"] = True
            return evidence
        if _canonical_hash(current) != plan["detection_sha256"]:
            _fail("STALE_DECISION", "capability facts changed after consent")
        if target.exists():
            _fail("FOREIGN_TARGET", "managed target exists but is not the exact verified capability")

        staging = Path(tempfile.mkdtemp(prefix=f"{definition['capability']}-", dir=cache_root))
        for asset in definition["assets"]:
            destination = staging / Path(*PurePosixPath(asset["managed_target"]).parts)
            destination.parent.mkdir(parents=True, exist_ok=True)
            final_url = _download_asset(asset["source_url"], destination)
            if final_url != asset["source_url"]:
                _fail("UNAPPROVED_SOURCE", "transport redirected outside the exact approved source")
            payload = destination.read_bytes()
            if len(payload) != asset["size"]:
                _fail("SIZE_MISMATCH", f"size mismatch for {asset['filename']}")
            if hashlib.sha256(payload).hexdigest() != asset["sha256"]:
                _fail("HASH_MISMATCH", f"hash mismatch for {asset['filename']}")

        entrypoint = staging / Path(*PurePosixPath(definition["verified_entrypoint"]).parts)
        try:
            entrypoint.chmod(entrypoint.stat().st_mode | 0o111)
        except OSError as exc:
            _fail("INTEGRATION_FAILED", f"cannot make entrypoint executable: {exc}")
        assets_valid, _ = _asset_evidence(staging, definition)
        compatible, probe = _probe(entrypoint, definition["version"])
        if not assets_valid or not compatible:
            _fail("PROBE_FAILED", f"staged capability probe failed: {probe['reason']}")

        target.parent.mkdir(parents=True, exist_ok=True)
        if os.stat(staging).st_dev != os.stat(target.parent).st_dev:
            _fail("PATH_VIOLATION", "staging and managed target are not on the same volume")
        try:
            os.replace(staging, target)
        except OSError as exc:
            if target.exists():
                raced = _detect_one(data_root, definition)
                if raced["status"] == "PRESENT" and raced["evidence"]["source"] == "managed":
                    shutil.rmtree(staging, ignore_errors=True)
                    staging = None
                else:
                    _fail("FOREIGN_TARGET", "concurrent publication left an unverified target")
            else:
                _fail("PUBLISH_FAILED", f"atomic publication failed: {exc}")
        else:
            staging = None

        final = _detect_one(data_root, definition)
        if final["status"] != "PRESENT" or final["evidence"]["source"] != "managed":
            _fail("PROBE_FAILED", "published capability did not pass final managed probe")
        evidence = dict(final["evidence"])
        evidence["status"] = "INTEGRATED"
        evidence["plan_sha256"] = plan["plan_sha256"]
        evidence["reused"] = False
        return evidence
    finally:
        if staging is not None:
            shutil.rmtree(staging, ignore_errors=True)
        if lock_owned:
            _remove_owned_lock(lock_path, token)
        _cleanup_empty_directories(created_cleanup)


def prepare_optional_capabilities(
    data_root: str | os.PathLike[str],
    capability_definitions: Sequence[Mapping[str, Any]],
    user_decisions: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Detect optional capabilities and integrate only exactly approved plans.

    Invalid inputs and authorized preparation failures are returned as ``BLOCKED``;
    ordinary absence and decline/defer decisions are not failures.
    """
    try:
        if not isinstance(data_root, (str, os.PathLike)):
            _fail("PATH_VIOLATION", "data_root must be path-like")
        root = Path(data_root)
        if not root.is_absolute() or root == Path(root.anchor):
            _fail("PATH_VIOLATION", "data_root must be an absolute non-root path")
        if root.exists():
            metadata = root.lstat()
            attributes = getattr(metadata, "st_file_attributes", 0)
            if root.is_symlink() or attributes & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0):
                _fail("PATH_VIOLATION", "data_root cannot be a link or reparse point")
            if not root.is_dir():
                _fail("PATH_VIOLATION", "data_root must be a directory")
        root = root.resolve(strict=False)
        definitions = _validate_definitions(capability_definitions)
        decisions = _validate_decisions(user_decisions)
    except _ContractError as exc:
        return _blocked(exc.code, exc.message)
    except (OSError, ValueError, UnicodeError) as exc:
        return _blocked("PATH_VIOLATION", f"input path cannot be validated: {exc}")

    try:
        facts = {
            capability: _detect_one(root, definitions[capability])
            for capability in _CAPABILITIES
        }
        plans = {
            capability: _make_plan(root, definitions[capability], facts[capability])
            for capability in _CAPABILITIES
            if facts[capability]["status"] in {"MISSING", "INCOMPATIBLE"}
        }
    except _ContractError as exc:
        return _blocked(exc.code, exc.message)
    except (OSError, ValueError, UnicodeError) as exc:
        return _blocked("DETECTION_FAILED", f"bounded detection failed: {exc}")
    if not plans:
        return {"result": "DETECTION_REPORT", "capabilities": list(facts.values()), "plans": []}
    if not decisions:
        return {
            "result": "CONSENT_REQUIRED",
            "capabilities": list(facts.values()),
            "plans": list(plans.values()),
        }

    integrated: list[dict[str, Any]] = []
    skipped = False
    undecided = False
    for capability in _CAPABILITIES:
        if capability not in plans:
            continue
        decision = decisions.get(capability)
        if decision is None:
            undecided = True
            continue
        definition = definitions[capability]
        plan = plans[capability]
        if (
            decision["definition_sha256"] != definition["definition_sha256"]
            or decision["plan_sha256"] != plan["plan_sha256"]
        ):
            return _blocked("STALE_DECISION", f"decision no longer matches {capability} definition and plan")
        if decision["decision"] in {"decline", "defer"}:
            facts[capability] = {
                "capability": capability,
                "status": "NOT_INTEGRATED",
                "decision": decision["decision"],
                "definition_sha256": definition["definition_sha256"],
                "plan_sha256": plan["plan_sha256"],
            }
            skipped = True
            continue
        try:
            integrated.append(_integrate_one(root, definition, plan))
        except _ContractError as exc:
            result = _blocked(exc.code, exc.message)
            result["capability"] = capability
            result["capabilities"] = list(facts.values())
            if integrated:
                result["integrated"] = integrated
            return result
        except Exception as exc:  # keep the public result set closed on transport/filesystem failure
            result = _blocked("INTEGRATION_FAILED", f"authorized integration failed: {exc}")
            result["capability"] = capability
            result["capabilities"] = list(facts.values())
            if integrated:
                result["integrated"] = integrated
            return result

    if integrated:
        try:
            refreshed = {
                capability: _detect_one(root, definitions[capability])
                for capability in _CAPABILITIES
            }
        except (_ContractError, OSError, ValueError, UnicodeError) as exc:
            result = _blocked("DETECTION_FAILED", f"final bounded detection failed: {exc}")
            result["integrated"] = integrated
            return result
        for capability, fact in facts.items():
            if fact["status"] == "NOT_INTEGRATED":
                refreshed[capability] = fact
        return {
            "result": "CONSENT_REQUIRED" if undecided else "INTEGRATED",
            "capabilities": list(refreshed.values()),
            "integrated": integrated,
            "plans": (
                [plans[name] for name in _CAPABILITIES if name in plans and name not in decisions]
                if undecided
                else list(plans.values())
            ),
        }
    if undecided:
        return {
            "result": "CONSENT_REQUIRED",
            "capabilities": list(facts.values()),
            "plans": [plans[name] for name in _CAPABILITIES if name in plans and name not in decisions],
        }
    if skipped:
        return {"result": "SKIPPED", "capabilities": list(facts.values()), "plans": list(plans.values())}
    return _blocked("INVALID_DECISION", "decisions did not address a missing capability")


assert _RESULTS == frozenset(
    {"DETECTION_REPORT", "CONSENT_REQUIRED", "INTEGRATED", "SKIPPED", "BLOCKED"}
)
assert _FACTS == frozenset({"PRESENT", "MISSING", "INCOMPATIBLE", "NOT_INTEGRATED"})
