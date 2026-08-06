from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import stat
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any, Iterable


PACKAGE_VERSION = "0.1.0-prealpha.1"
PACKAGE_DIRECTORY = f"golden-key-openmontage-for-workbuddy-{PACKAGE_VERSION}"
EXPECTED_CONTRACT_ID = "golden-key-workbuddy-callable-core-v1"
EXPECTED_CORE_TAG = "golden-key-v0.3.21"
EXPECTED_SOURCE_COMMIT = "757ea3822e5f2eef7f341389983119021e827c8d"
EXPECTED_AUTHORITY = {
    "invocation_model": "direct_agent",
    "nested_agent_host_allowed": False,
}
EXPECTED_CONSUMER_REMOVE_PATHS = {
    "lib/agent_host_authority.py",
    "lib/model_driven_agent_host.py",
    "lib/openai_compatible_transport.py",
    "tests/contracts/test_agent_host_authority.py",
    "tests/contracts/test_model_driven_agent_host.py",
    "tests/contracts/test_openai_compatible_transport.py",
}

CONSUMER_FILES = (
    ".workbuddy/README.md",
    "config/openmontage.sync.json",
    "docs/workbuddy/QUICK-START.md",
    "requirements.txt",
    "setup.py",
    "workbuddy-skill/golden-key-openmontage/SKILL.md",
    "workbuddy-skill/golden-key-openmontage-onboarding/SKILL.md",
)
CONSUMER_SOURCE_PREFIX = "golden_key_openmontage_workbuddy"
BOOTSTRAP_FILES = {
    "packaging/workbuddy/golden-key-workbuddy.ps1": "golden-key-workbuddy.ps1",
    "packaging/workbuddy/install-workbuddy.ps1": "install-workbuddy.ps1",
}


class PortableBundleContractError(RuntimeError):
    pass


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _safe_relative(value: str) -> str:
    normalized = PurePosixPath(value)
    if (
        normalized.is_absolute()
        or ".." in normalized.parts
        or "\\" in value
        or value in {"", "."}
    ):
        raise PortableBundleContractError(f"unsafe package path: {value}")
    return normalized.as_posix()


def _read_lock(lock_path: Path) -> dict[str, Any]:
    try:
        lock = json.loads(lock_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PortableBundleContractError(f"cannot read Core lock: {exc}") from exc

    identity = (
        lock.get("contract_id"),
        lock.get("source_ref"),
        lock.get("source_commit"),
    )
    if identity != (
        EXPECTED_CONTRACT_ID,
        EXPECTED_CORE_TAG,
        EXPECTED_SOURCE_COMMIT,
    ):
        raise PortableBundleContractError("Core lock identity is not v0.3.21")
    authority = lock.get("authority") or {}
    if any(authority.get(key) != value for key, value in EXPECTED_AUTHORITY.items()):
        raise PortableBundleContractError("Core lock authority is not direct_agent")
    remove_paths = set((lock.get("managed_scope") or {}).get("consumer_remove_paths", []))
    if remove_paths != EXPECTED_CONSUMER_REMOVE_PATHS:
        raise PortableBundleContractError("consumer_remove_paths contract drifted")
    return lock


def _core_entries(lock: dict[str, Any]) -> list[dict[str, Any]]:
    entries = lock.get("files")
    if not isinstance(entries, list) or not entries:
        raise PortableBundleContractError("Core lock has no file inventory")
    seen: set[str] = set()
    normalized: list[dict[str, Any]] = []
    for raw in entries:
        source_path = _safe_relative(str(raw.get("source_path", "")))
        archive_path = _safe_relative(str(raw.get("path", "")))
        if archive_path != f"workbuddy-core/{source_path}":
            raise PortableBundleContractError(
                f"Core lock path mapping drifted: {archive_path}"
            )
        if source_path in seen:
            raise PortableBundleContractError(f"duplicate Core path: {source_path}")
        seen.add(source_path)
        normalized.append({**raw, "source_path": source_path})
    return sorted(normalized, key=lambda entry: entry["source_path"])


def _copy_verified(
    source: Path,
    destination: Path,
    *,
    expected_sha256: str | None = None,
    expected_size: int | None = None,
) -> dict[str, Any]:
    if not source.is_file() or source.is_symlink():
        raise PortableBundleContractError(f"required file missing: {source}")
    if expected_size is not None and source.stat().st_size != expected_size:
        raise PortableBundleContractError(f"size mismatch: {source}")
    actual_sha256 = _sha256(source)
    if expected_sha256 is not None and actual_sha256 != expected_sha256.lower():
        raise PortableBundleContractError(f"hash mismatch: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    return {
        "path": destination.as_posix(),
        "sha256": actual_sha256,
        "size": source.stat().st_size,
    }


def _consumer_python_files(repo_root: Path) -> Iterable[Path]:
    package_root = repo_root / CONSUMER_SOURCE_PREFIX
    if not package_root.is_dir():
        raise PortableBundleContractError("WorkBuddy consumer package is missing")
    for path in sorted(package_root.rglob("*")):
        if path.is_symlink():
            raise PortableBundleContractError(f"consumer symlink is forbidden: {path}")
        if path.is_file() and path.suffix in {".py", ".cjs"}:
            yield path


def build_portable_staging(
    *, repo_root: Path, lock_path: Path, output_root: Path
) -> Path:
    repo_root = Path(repo_root).resolve()
    lock_path = Path(lock_path).resolve()
    output_root = Path(output_root).resolve()
    staging = output_root / PACKAGE_DIRECTORY
    if staging.exists():
        raise PortableBundleContractError(f"output already exists: {staging}")
    staging.mkdir(parents=True)

    lock = _read_lock(lock_path)
    inventory: list[dict[str, Any]] = []
    try:
        for entry in _core_entries(lock):
            relative = entry["source_path"]
            if relative in EXPECTED_CONSUMER_REMOVE_PATHS:
                raise PortableBundleContractError(
                    f"forbidden Core path entered the package: {relative}"
                )
            copied = _copy_verified(
                repo_root / relative,
                staging / relative,
                expected_sha256=str(entry["sha256"]),
                expected_size=int(entry["size"]),
            )
            copied["path"] = relative
            copied["owner"] = "managed_core"
            inventory.append(copied)

        for relative in CONSUMER_FILES:
            copied = _copy_verified(repo_root / relative, staging / relative)
            copied["path"] = relative
            copied["owner"] = "workbuddy_consumer"
            inventory.append(copied)

        for source in _consumer_python_files(repo_root):
            relative = source.relative_to(repo_root).as_posix()
            copied = _copy_verified(source, staging / relative)
            copied["path"] = relative
            copied["owner"] = "workbuddy_consumer"
            inventory.append(copied)

        for source_relative, target_relative in BOOTSTRAP_FILES.items():
            copied = _copy_verified(
                repo_root / source_relative, staging / target_relative
            )
            copied["path"] = target_relative
            copied["owner"] = "workbuddy_bootstrap"
            inventory.append(copied)

        lock_target = staging / "GOLDEN_KEY_WORKBUDDY_CORE.lock.json"
        copied_lock = _copy_verified(lock_path, lock_target)
        copied_lock["path"] = lock_target.name
        copied_lock["owner"] = "core_contract"
        inventory.append(copied_lock)

        manifest = {
            "schema_version": "golden-key-workbuddy-portable-bundle-v1",
            "distribution": {
                "channel": "pre-alpha",
                "format": "portable_zip",
                "package_version": PACKAGE_VERSION,
                "status": "first_installer_build_validation_only",
            },
            "core": {
                "contract_id": EXPECTED_CONTRACT_ID,
                "file_count": len(_core_entries(lock)),
                "source_commit": EXPECTED_SOURCE_COMMIT,
                "tag": EXPECTED_CORE_TAG,
                "usage": "temporary_first_package_build_baseline_not_final_core",
            },
            "authority": EXPECTED_AUTHORITY,
            "installation": {
                "archive_may_be_extracted_anywhere": True,
                "registration_required_for_workbuddy": True,
                "mcp": "optional_not_enabled_by_default",
            },
            "files": sorted(inventory, key=lambda item: item["path"]),
        }
        (staging / "BUNDLE-MANIFEST.json").write_text(
            json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        return staging
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        raise


def build_portable_zip(staging: Path, output_zip: Path) -> dict[str, Any]:
    staging = Path(staging).resolve()
    output_zip = Path(output_zip).resolve()
    if output_zip.exists():
        raise PortableBundleContractError(f"archive already exists: {output_zip}")
    output_zip.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        output_zip, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
    ) as archive:
        for source in sorted(path for path in staging.rglob("*") if path.is_file()):
            relative = source.relative_to(staging.parent).as_posix()
            info = zipfile.ZipInfo(relative, date_time=(2026, 8, 6, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(info, source.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)
    return {
        "archive": str(output_zip),
        "sha256": _sha256(output_zip),
        "size": output_zip.stat().st_size,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--lock", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()
    try:
        staging = build_portable_staging(
            repo_root=args.repo_root,
            lock_path=args.lock,
            output_root=args.output_root,
        )
        report = build_portable_zip(
            staging, args.output_root / f"{PACKAGE_DIRECTORY}.zip"
        )
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0
    except (OSError, PortableBundleContractError) as exc:
        print(json.dumps({"status": "fail", "error": str(exc)}, ensure_ascii=False))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
