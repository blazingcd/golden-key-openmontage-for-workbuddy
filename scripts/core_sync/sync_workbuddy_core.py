"""Verify and mirror a Golden Key WorkBuddy callable-core release bundle.

The ZIP and lock are the only synchronization inputs.  This module never reads
or merges the Golden Key source repository and never calls a Provider.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import stat
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any


EMBEDDED_LOCK_NAME = "GOLDEN_KEY_WORKBUDDY_CORE.lock.json"
CONSUMER_OWNED_PACKAGE_PATHS = ("requirements.txt", "setup.py")
REQUIRED_CONSUMER_REMOVE_PATHS = (
    "lib/agent_host_authority.py",
    "lib/model_driven_agent_host.py",
    "lib/openai_compatible_transport.py",
    "tests/contracts/test_agent_host_authority.py",
    "tests/contracts/test_model_driven_agent_host.py",
    "tests/contracts/test_openai_compatible_transport.py",
)
EXPECTED_AUTHORITY = {
    "consumer": "workbuddy",
    "consumer_direct_official_sync_allowed": False,
    "invocation_model": "direct_agent",
    "nested_agent_host_allowed": False,
    "official_openmontage_role": "reviewed_upstream_baseline_only",
    "source": "golden-key-core",
}


class SyncContractError(RuntimeError):
    """The release bundle, lock, or destination violates the sync contract."""


@dataclass(frozen=True)
class VerifiedBundle:
    zip_path: Path
    lock: dict[str, Any]
    entries: tuple[dict[str, Any], ...]


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _normalized_relative(value: str, *, label: str) -> str:
    if not isinstance(value, str) or not value or "\\" in value:
        raise SyncContractError(f"unsafe {label}: {value!r}")
    pure = PurePosixPath(value)
    if pure.is_absolute() or any(part in {"", ".", ".."} for part in pure.parts):
        raise SyncContractError(f"unsafe {label}: {value!r}")
    normalized = pure.as_posix()
    if normalized != value or ":" in pure.parts[0]:
        raise SyncContractError(f"non-canonical {label}: {value!r}")
    return normalized


def _normalized_prefix(value: str) -> str:
    if not isinstance(value, str) or not value.endswith("/"):
        raise SyncContractError(f"managed prefix must end with '/': {value!r}")
    normalized = _normalized_relative(value[:-1], label="managed prefix") + "/"
    if normalized != value:
        raise SyncContractError(f"non-canonical managed prefix: {value!r}")
    return normalized


def _is_managed(path: str, managed_paths: set[str], managed_prefixes: tuple[str, ...]) -> bool:
    return path in managed_paths or any(path.startswith(prefix) for prefix in managed_prefixes)


def _bundle_digest(entries: list[dict[str, Any]]) -> str:
    canonical = json.dumps(
        entries, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return _sha256(canonical)


def _read_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SyncContractError(f"cannot read JSON lock {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise SyncContractError("lock root must be an object")
    return payload


def verify_bundle(
    *,
    zip_path: Path,
    lock_path: Path,
    expected_zip_sha256: str,
    expected_contract_id: str,
    expected_source_ref: str,
    expected_source_commit: str,
) -> VerifiedBundle:
    zip_path = Path(zip_path)
    lock_path = Path(lock_path)
    actual_zip_sha256 = _sha256(zip_path.read_bytes())
    if actual_zip_sha256.lower() != expected_zip_sha256.lower():
        raise SyncContractError(
            f"ZIP SHA-256 mismatch: expected {expected_zip_sha256.lower()}, "
            f"got {actual_zip_sha256}"
        )

    lock_bytes = lock_path.read_bytes()
    lock = _read_json(lock_path)
    if lock.get("schema_version") != 2:
        raise SyncContractError("unsupported lock schema_version")
    if lock.get("contract_id") != expected_contract_id:
        raise SyncContractError("lock contract_id mismatch")
    if lock.get("source_ref") != expected_source_ref:
        raise SyncContractError("lock source_ref mismatch")
    if lock.get("source_commit") != expected_source_commit:
        raise SyncContractError("lock source_commit mismatch")
    if lock.get("authority") != EXPECTED_AUTHORITY:
        raise SyncContractError("lock authority is not the direct_agent contract")

    scope = lock.get("managed_scope")
    if not isinstance(scope, dict) or scope.get("destination_root") != "workbuddy-core":
        raise SyncContractError("invalid managed_scope destination_root")
    managed_paths = {
        _normalized_relative(path, label="managed path")
        for path in scope.get("managed_paths", [])
    }
    managed_prefixes = tuple(
        _normalized_prefix(prefix) for prefix in scope.get("managed_prefixes", [])
    )
    required_paths = {
        _normalized_relative(path, label="required path")
        for path in scope.get("required_paths", [])
    }
    forbidden_paths = {
        _normalized_relative(path, label="forbidden path")
        for path in scope.get("forbidden_paths", [])
    }
    consumer_remove_paths = [
        _normalized_relative(path, label="consumer remove path")
        for path in scope.get("consumer_remove_paths", [])
    ]
    if len(consumer_remove_paths) != len(set(consumer_remove_paths)):
        raise SyncContractError("duplicate consumer_remove_paths")
    if tuple(consumer_remove_paths) != REQUIRED_CONSUMER_REMOVE_PATHS:
        raise SyncContractError("consumer_remove_paths must be the exact six-path contract")
    if not set(consumer_remove_paths) <= forbidden_paths:
        raise SyncContractError("consumer_remove_paths must be forbidden")
    if any(path in consumer_remove_paths for path in CONSUMER_OWNED_PACKAGE_PATHS):
        raise SyncContractError("consumer-owned package files cannot be removed")
    if not set(CONSUMER_OWNED_PACKAGE_PATHS) <= forbidden_paths:
        raise SyncContractError("consumer-owned package files must be forbidden to the bundle")
    for path in consumer_remove_paths:
        if not _is_managed(path, managed_paths, managed_prefixes):
            raise SyncContractError(f"consumer remove path is outside managed scope: {path}")

    entries = lock.get("files")
    if not isinstance(entries, list) or not entries:
        raise SyncContractError("lock files must be a non-empty array")
    if _bundle_digest(entries) != lock.get("bundle_sha256"):
        raise SyncContractError("bundle inventory digest mismatch")

    source_paths: set[str] = set()
    bundle_paths: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise SyncContractError("lock file entry must be an object")
        source_path = _normalized_relative(entry.get("source_path"), label="source path")
        bundle_path = _normalized_relative(entry.get("path"), label="bundle path")
        if bundle_path != f"workbuddy-core/{source_path}":
            raise SyncContractError(f"bundle/source path mismatch: {bundle_path}")
        if source_path in source_paths or bundle_path in bundle_paths:
            raise SyncContractError(f"duplicate file entry: {source_path}")
        if source_path in forbidden_paths:
            raise SyncContractError(f"forbidden path in bundle: {source_path}")
        if not _is_managed(source_path, managed_paths, managed_prefixes):
            raise SyncContractError(f"file outside managed scope: {source_path}")
        if entry.get("apply_mode") != "replace":
            raise SyncContractError(f"unsupported apply_mode for {source_path}")
        if entry.get("classification") != "workbuddy_callable":
            raise SyncContractError(f"invalid classification for {source_path}")
        if entry.get("source_mode") not in {"100644", "100755"}:
            raise SyncContractError(f"invalid source_mode for {source_path}")
        if not isinstance(entry.get("size"), int) or entry["size"] < 0:
            raise SyncContractError(f"invalid size for {source_path}")
        if not isinstance(entry.get("sha256"), str) or len(entry["sha256"]) != 64:
            raise SyncContractError(f"invalid sha256 for {source_path}")
        source_paths.add(source_path)
        bundle_paths.add(bundle_path)
    if not required_paths <= source_paths:
        raise SyncContractError(
            f"required paths missing from bundle: {sorted(required_paths - source_paths)}"
        )

    try:
        archive = zipfile.ZipFile(zip_path)
    except (OSError, zipfile.BadZipFile) as exc:
        raise SyncContractError(f"invalid ZIP: {exc}") from exc
    with archive:
        file_infos = [info for info in archive.infolist() if not info.is_dir()]
        names = [info.filename for info in file_infos]
        if len(names) != len(set(names)):
            raise SyncContractError("ZIP contains duplicate file members")
        for info in archive.infolist():
            candidate = info.filename.rstrip("/") if info.is_dir() else info.filename
            if candidate:
                _normalized_relative(candidate, label="ZIP member")
        expected_members = bundle_paths | {EMBEDDED_LOCK_NAME}
        actual_members = set(names)
        if actual_members != expected_members:
            raise SyncContractError(
                "bundle inventory mismatch; "
                f"extra={sorted(actual_members - expected_members)}, "
                f"missing={sorted(expected_members - actual_members)}"
            )
        if archive.read(EMBEDDED_LOCK_NAME) != lock_bytes:
            raise SyncContractError("embedded and external lock files differ")
        info_by_name = {info.filename: info for info in file_infos}
        for entry in entries:
            info = info_by_name[entry["path"]]
            data = archive.read(info)
            if len(data) != entry["size"]:
                raise SyncContractError(f"file size mismatch: {entry['source_path']}")
            if _sha256(data) != entry["sha256"]:
                raise SyncContractError(f"file hash mismatch: {entry['source_path']}")
            archive_mode = (info.external_attr >> 16) & 0o177777
            if archive_mode != int(entry["source_mode"], 8):
                raise SyncContractError(f"file mode mismatch: {entry['source_path']}")

    return VerifiedBundle(zip_path=zip_path, lock=lock, entries=tuple(entries))


def validate_configured_bundle(
    *, bundle: VerifiedBundle, lock_path: Path, config: dict[str, Any]
) -> dict[str, Any]:
    """Verify lock identity values that are pinned outside the downloaded assets."""
    actual_lock_sha256 = _sha256(Path(lock_path).read_bytes())
    if actual_lock_sha256 != config.get("golden_key_core_lock_sha256"):
        raise SyncContractError("external lock SHA-256 mismatch")
    if bundle.lock.get("bundle_sha256") != config.get("golden_key_core_bundle_sha256"):
        raise SyncContractError("configured bundle digest mismatch")
    if bundle.lock.get("upstream_base") != config.get("upstream_base_commit"):
        raise SyncContractError("configured upstream baseline mismatch")
    configured_authority = config.get("authority")
    if not isinstance(configured_authority, dict):
        raise SyncContractError("configured authority is missing")
    for key, value in configured_authority.items():
        if bundle.lock["authority"].get(key) != value:
            raise SyncContractError(f"configured authority mismatch: {key}")
    return {
        "configured_identity_match": True,
        "lock_sha256": actual_lock_sha256,
        "bundle_sha256": bundle.lock["bundle_sha256"],
        "upstream_base": bundle.lock["upstream_base"],
    }


def _destination_path(root: Path, relative: str) -> Path:
    target = root.joinpath(*PurePosixPath(relative).parts)
    resolved_root = root.resolve()
    try:
        target.resolve(strict=False).relative_to(resolved_root)
    except ValueError as exc:
        raise SyncContractError(f"destination escapes repository: {relative}") from exc
    return target


def _managed_destination_files(
    root: Path, managed_paths: set[str], managed_prefixes: tuple[str, ...]
) -> set[str]:
    found: set[str] = set()
    for relative in managed_paths:
        target = _destination_path(root, relative)
        if target.is_symlink():
            raise SyncContractError(f"managed destination is a symlink: {relative}")
        if target.is_file():
            found.add(relative)
        elif target.exists():
            raise SyncContractError(f"managed file path is not a file: {relative}")
    for prefix in managed_prefixes:
        prefix_path = _destination_path(root, prefix[:-1])
        if prefix_path.is_symlink():
            raise SyncContractError(f"managed prefix is a symlink: {prefix}")
        if not prefix_path.exists():
            continue
        if not prefix_path.is_dir():
            raise SyncContractError(f"managed prefix is not a directory: {prefix}")
        for current_root, dir_names, file_names in os.walk(prefix_path, followlinks=False):
            current = Path(current_root)
            for name in list(dir_names):
                child = current / name
                if child.is_symlink():
                    raise SyncContractError(
                        f"symlink inside managed scope: {child.relative_to(root).as_posix()}"
                    )
            for name in file_names:
                child = current / name
                if child.is_symlink():
                    raise SyncContractError(
                        f"symlink inside managed scope: {child.relative_to(root).as_posix()}"
                    )
                found.add(child.relative_to(root).as_posix())
    return found


def _write_replacement(path: Path, data: bytes, source_mode: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        mode="wb", prefix=f".{path.name}.", suffix=".workbuddy-sync", dir=path.parent, delete=False
    )
    temp_path = Path(handle.name)
    try:
        with handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        if os.name != "nt":
            os.chmod(temp_path, int(source_mode, 8) & 0o777)
        os.replace(temp_path, path)
    finally:
        if temp_path.exists():
            temp_path.unlink()


def verify_destination(bundle: VerifiedBundle, destination_root: Path) -> dict[str, Any]:
    """Verify the on-disk managed scope without changing the destination."""
    destination_root = Path(destination_root)
    scope = bundle.lock["managed_scope"]
    managed_paths = set(scope["managed_paths"])
    managed_prefixes = tuple(scope["managed_prefixes"])
    expected_paths = {entry["source_path"] for entry in bundle.entries}
    actual_paths = _managed_destination_files(
        destination_root, managed_paths, managed_prefixes
    )
    if actual_paths != expected_paths:
        raise SyncContractError(
            "destination managed inventory mismatch; "
            f"extra={sorted(actual_paths - expected_paths)}, "
            f"missing={sorted(expected_paths - actual_paths)}"
        )
    for entry in bundle.entries:
        target = _destination_path(destination_root, entry["source_path"])
        if _sha256(target.read_bytes()) != entry["sha256"]:
            raise SyncContractError(f"destination hash mismatch: {entry['source_path']}")
    for relative in scope["consumer_remove_paths"]:
        if _destination_path(destination_root, relative).exists():
            raise SyncContractError(f"consumer remove path remains: {relative}")
    preserved_consumer_paths = [
        relative
        for relative in CONSUMER_OWNED_PACKAGE_PATHS
        if _destination_path(destination_root, relative).is_file()
    ]
    return {
        "verified_file_count": len(bundle.entries),
        "managed_inventory_exact": True,
        "consumer_remove_paths_absent": list(scope["consumer_remove_paths"]),
        "preserved_consumer_paths": preserved_consumer_paths,
    }


def apply_verified_bundle(bundle: VerifiedBundle, destination_root: Path) -> dict[str, Any]:
    destination_root = Path(destination_root)
    destination_root.mkdir(parents=True, exist_ok=True)
    scope = bundle.lock["managed_scope"]
    managed_paths = set(scope["managed_paths"])
    managed_prefixes = tuple(scope["managed_prefixes"])
    expected_paths = {entry["source_path"] for entry in bundle.entries}
    current_managed = _managed_destination_files(
        destination_root, managed_paths, managed_prefixes
    )

    changed: list[str] = []
    with zipfile.ZipFile(bundle.zip_path) as archive:
        for entry in bundle.entries:
            relative = entry["source_path"]
            target = _destination_path(destination_root, relative)
            data = archive.read(entry["path"])
            if target.is_file() and _sha256(target.read_bytes()) == entry["sha256"]:
                continue
            if target.exists() and not target.is_file():
                raise SyncContractError(f"destination is not a regular file: {relative}")
            _write_replacement(target, data, entry["source_mode"])
            changed.append(relative)

    consumer_remove_paths = list(scope["consumer_remove_paths"])
    removed_existing = [
        relative for relative in consumer_remove_paths if relative in current_managed
    ]
    stale_paths = sorted(current_managed - expected_paths)
    deleted: list[str] = []
    for relative in stale_paths:
        target = _destination_path(destination_root, relative)
        if target.exists():
            target.unlink()
            deleted.append(relative)

    for relative in consumer_remove_paths:
        target = _destination_path(destination_root, relative)
        if target.exists():
            if not target.is_file() or target.is_symlink():
                raise SyncContractError(f"consumer remove path is not a regular file: {relative}")
            target.unlink()
            if relative not in deleted:
                deleted.append(relative)

    destination_verification = verify_destination(bundle, destination_root)
    return {
        "contract_id": bundle.lock["contract_id"],
        "source_ref": bundle.lock["source_ref"],
        "source_commit": bundle.lock["source_commit"],
        "authority": bundle.lock["authority"],
        "verified_file_count": len(bundle.entries),
        "changed_file_count": len(changed),
        "changed_files": sorted(changed),
        "deleted_file_count": len(deleted),
        "deleted_files": sorted(deleted),
        "consumer_remove_paths": consumer_remove_paths,
        "removed_existing_paths": sorted(removed_existing),
        "preserved_consumer_paths": destination_verification["preserved_consumer_paths"],
        "bundle_sha256": bundle.lock["bundle_sha256"],
    }


def synchronize(
    *,
    zip_path: Path,
    lock_path: Path,
    destination_root: Path,
    expected_zip_sha256: str,
    expected_contract_id: str,
    expected_source_ref: str,
    expected_source_commit: str,
) -> dict[str, Any]:
    bundle = verify_bundle(
        zip_path=zip_path,
        lock_path=lock_path,
        expected_zip_sha256=expected_zip_sha256,
        expected_contract_id=expected_contract_id,
        expected_source_ref=expected_source_ref,
        expected_source_commit=expected_source_commit,
    )
    return apply_verified_bundle(bundle, destination_root)


def _load_config(path: Path) -> dict[str, Any]:
    config = _read_json(path)
    required = {
        "golden_key_core_tag",
        "golden_key_core_source_commit",
        "golden_key_core_zip_sha256",
        "golden_key_core_lock_sha256",
        "golden_key_core_contract_id",
        "golden_key_core_bundle_sha256",
        "upstream_base_commit",
        "authority",
    }
    missing = sorted(required - set(config))
    if missing:
        raise SyncContractError(f"sync config missing keys: {missing}")
    if config.get("official_direct_sync_allowed") is not False:
        raise SyncContractError("official direct sync must be disabled")
    if config.get("private_git_ancestry_merge_allowed") is not False:
        raise SyncContractError("private Git ancestry merge must be disabled")
    return config


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=("verify", "apply"))
    parser.add_argument("--zip", required=True, type=Path)
    parser.add_argument("--lock", required=True, type=Path)
    parser.add_argument("--config", type=Path, default=Path("config/openmontage.sync.json"))
    parser.add_argument("--destination", type=Path, default=Path.cwd())
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    try:
        config = _load_config(args.config)
        bundle = verify_bundle(
            zip_path=args.zip,
            lock_path=args.lock,
            expected_zip_sha256=config["golden_key_core_zip_sha256"],
            expected_contract_id=config["golden_key_core_contract_id"],
            expected_source_ref=config["golden_key_core_tag"],
            expected_source_commit=config["golden_key_core_source_commit"],
        )
        validate_configured_bundle(bundle=bundle, lock_path=args.lock, config=config)
        report = (
            apply_verified_bundle(bundle, args.destination)
            if args.command == "apply"
            else {
                "contract_id": bundle.lock["contract_id"],
                "source_ref": bundle.lock["source_ref"],
                "source_commit": bundle.lock["source_commit"],
                "authority": bundle.lock["authority"],
                "verified_file_count": len(bundle.entries),
                "bundle_sha256": bundle.lock["bundle_sha256"],
            }
        )
    except (OSError, SyncContractError, zipfile.BadZipFile) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False))
        return 2
    payload = {"ok": True, **report}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
