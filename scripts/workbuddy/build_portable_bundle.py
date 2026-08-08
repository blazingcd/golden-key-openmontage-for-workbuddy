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
    "WORKBUDDY-BOOTSTRAP-RUNTIME.lock.json",
    "WORKBUDDY-PRODUCTION-RUNTIME.lock.json",
    "config/openmontage.sync.json",
    "docs/workbuddy/QUICK-START.md",
    "requirements.txt",
    "workbuddy-runtime/hyperframes/package.json",
    "workbuddy-runtime/hyperframes/package-lock.json",
    "workbuddy-skill/golden-key-openmontage/SKILL.md",
    "workbuddy-skill/golden-key-openmontage-onboarding/SKILL.md",
)
CONSUMER_SOURCE_PREFIX = "golden_key_openmontage_workbuddy"
BOOTSTRAP_FILES = {
    "packaging/workbuddy/golden-key-workbuddy.ps1": "golden-key-workbuddy.ps1",
    "packaging/workbuddy/install-workbuddy.ps1": "install-workbuddy.ps1",
    "packaging/workbuddy/install-to-workbuddy.ps1": "install-to-workbuddy.ps1",
    "packaging/workbuddy/uninstall-workbuddy.ps1": "uninstall-workbuddy.ps1",
    "packaging/workbuddy/configure-provider-keys.ps1": "configure-provider-keys.ps1",
    "packaging/workbuddy/安装到WorkBuddy.cmd": "安装到WorkBuddy.cmd",
    "packaging/workbuddy/从WorkBuddy卸载.cmd": "从WorkBuddy卸载.cmd",
    "packaging/workbuddy/配置API密钥.cmd": "配置API密钥.cmd",
    "packaging/workbuddy/bootstrap/install-to-workbuddy.cmd": "bootstrap/install-to-workbuddy.cmd",
    "packaging/workbuddy/bootstrap/sitecustomize.py": "bootstrap/python/sitecustomize.py",
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


def _stage_bootstrap_python(
    *,
    archive_path: Path,
    runtime_lock_path: Path,
    staging: Path,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    try:
        runtime_lock = json.loads(runtime_lock_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PortableBundleContractError(
            f"cannot read bootstrap runtime lock: {exc}"
        ) from exc
    if (
        runtime_lock.get("schema_version")
        != "golden-key-workbuddy-bootstrap-runtime-v1"
    ):
        raise PortableBundleContractError("bootstrap runtime lock schema drifted")
    python = (runtime_lock.get("components") or {}).get("python") or {}
    expected_hash = str(python.get("sha256", "")).lower()
    actual_hash = _sha256(archive_path)
    if len(expected_hash) != 64 or actual_hash != expected_hash:
        raise PortableBundleContractError("bootstrap Python archive hash mismatch")
    if archive_path.name != python.get("archive"):
        raise PortableBundleContractError("bootstrap Python archive name drifted")

    target_root = staging / "bootstrap" / "python"
    inventory: list[dict[str, Any]] = []
    extracted: set[str] = set()
    try:
        with zipfile.ZipFile(archive_path) as archive:
            for info in sorted(archive.infolist(), key=lambda item: item.filename):
                if info.is_dir():
                    continue
                relative = _safe_relative(info.filename)
                if stat.S_ISLNK((info.external_attr >> 16) & 0xFFFF):
                    raise PortableBundleContractError(
                        f"bootstrap Python symlink is forbidden: {relative}"
                    )
                destination = target_root / Path(*PurePosixPath(relative).parts)
                destination.parent.mkdir(parents=True, exist_ok=True)
                if relative.endswith("._pth"):
                    zip_name = f"{Path(relative).stem}.zip"
                    destination.write_text(
                        f"{zip_name}\n.\n../../..\nimport site\n",
                        encoding="utf-8",
                    )
                else:
                    with archive.open(info) as source, destination.open("wb") as output:
                        shutil.copyfileobj(source, output)
                extracted.add(relative)
                inventory.append(
                    {
                        "path": destination.relative_to(staging).as_posix(),
                        "sha256": _sha256(destination),
                        "size": destination.stat().st_size,
                        "owner": "workbuddy_bootstrap_runtime",
                    }
                )
    except (OSError, zipfile.BadZipFile) as exc:
        raise PortableBundleContractError(
            f"cannot extract bootstrap Python archive: {exc}"
        ) from exc

    required = {_safe_relative(str(value)) for value in python.get("required_paths", [])}
    missing = sorted(required - extracted)
    if missing:
        raise PortableBundleContractError(
            f"bootstrap Python required paths missing: {missing}"
        )
    metadata = {
        "version": str(python.get("version", "")),
        "source": "python.org_windows_embeddable_x64",
        "archive_sha256": actual_hash,
        "system_python_required": False,
    }
    return inventory, metadata


def _stage_bootstrap_pip(
    *, wheel_path: Path, runtime_lock_path: Path, staging: Path
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    try:
        runtime_lock = json.loads(runtime_lock_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise PortableBundleContractError(
            f"cannot read bootstrap runtime lock: {exc}"
        ) from exc
    pip = (runtime_lock.get("components") or {}).get("pip") or {}
    if wheel_path.name != pip.get("archive"):
        raise PortableBundleContractError("bootstrap pip wheel name drifted")
    expected_hash = str(pip.get("sha256", "")).lower()
    if len(expected_hash) != 64 or _sha256(wheel_path) != expected_hash:
        raise PortableBundleContractError("bootstrap pip wheel hash mismatch")
    destination = staging / "bootstrap" / "python" / wheel_path.name
    copied = _copy_verified(
        wheel_path, destination, expected_sha256=expected_hash
    )
    copied["path"] = destination.relative_to(staging).as_posix()
    copied["owner"] = "workbuddy_bootstrap_runtime"

    path_configs = sorted((staging / "bootstrap" / "python").glob("*._pth"))
    if len(path_configs) != 1:
        raise PortableBundleContractError(
            "bundled Python must contain exactly one embedded path config"
        )
    path_config = path_configs[0]
    path_lines = path_config.read_text(encoding="utf-8").splitlines()
    if wheel_path.name in path_lines:
        raise PortableBundleContractError("bootstrap pip wheel path is duplicated")
    try:
        site_index = path_lines.index("import site")
    except ValueError as exc:
        raise PortableBundleContractError(
            "bundled Python path config does not enable site"
        ) from exc
    path_lines.insert(site_index, wheel_path.name)
    path_config.write_text(
        "\n".join(path_lines) + "\n",
        encoding="utf-8",
    )
    path_config_inventory = {
        "path": path_config.relative_to(staging).as_posix(),
        "sha256": _sha256(path_config),
        "size": path_config.stat().st_size,
        "owner": "workbuddy_bootstrap_runtime",
    }
    metadata = {
        "version": str(pip.get("version", "")),
        "archive_sha256": expected_hash,
        "source": "pypi_official_wheel",
    }
    return copied, metadata, path_config_inventory


def build_portable_staging(
    *,
    repo_root: Path,
    lock_path: Path,
    output_root: Path,
    bootstrap_python_archive: Path | None = None,
    bootstrap_pip_wheel: Path | None = None,
    bootstrap_runtime_lock_path: Path | None = None,
) -> Path:
    repo_root = Path(repo_root).resolve()
    lock_path = Path(lock_path).resolve()
    output_root = Path(output_root).resolve()
    if (bootstrap_python_archive is None) != (bootstrap_runtime_lock_path is None):
        raise PortableBundleContractError(
            "bootstrap Python archive and runtime lock must be supplied together"
        )
    if bootstrap_python_archive is not None:
        bootstrap_python_archive = Path(bootstrap_python_archive).resolve()
        bootstrap_runtime_lock_path = Path(bootstrap_runtime_lock_path).resolve()
    if bootstrap_pip_wheel is not None:
        if bootstrap_python_archive is None:
            raise PortableBundleContractError(
                "bootstrap pip wheel requires the bundled Python runtime"
            )
        bootstrap_pip_wheel = Path(bootstrap_pip_wheel).resolve()
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

        bootstrap_runtime: dict[str, Any] | None = None
        if bootstrap_python_archive is not None:
            bootstrap_inventory, bootstrap_python = _stage_bootstrap_python(
                archive_path=bootstrap_python_archive,
                runtime_lock_path=bootstrap_runtime_lock_path,
                staging=staging,
            )
            inventory.extend(bootstrap_inventory)
            bootstrap_runtime = {"python": bootstrap_python}
            if bootstrap_pip_wheel is not None:
                (
                    pip_inventory,
                    bootstrap_pip,
                    path_config_inventory,
                ) = _stage_bootstrap_pip(
                    wheel_path=bootstrap_pip_wheel,
                    runtime_lock_path=bootstrap_runtime_lock_path,
                    staging=staging,
                )
                inventory = [
                    item
                    for item in inventory
                    if item["path"] != path_config_inventory["path"]
                ]
                inventory.extend([path_config_inventory, pip_inventory])
                bootstrap_runtime["pip"] = bootstrap_pip

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
                "production_environment": {
                    "profile_id": "complete_video_production",
                    "display_name_zh": "完整视频制作环境",
                    "mode": "managed_after_single_user_confirmation",
                    "target": "<data_root>/Runtime",
                    "system_python_modified": False,
                    "system_path_modified": False,
                },
                "runtime_roles": {
                    "python": (
                        "bundled_private_interpreter"
                        if bootstrap_runtime is not None
                        else "required"
                    ),
                    "ffmpeg": "required",
                    "node": "required",
                    "remotion": "standard_agent_selected_composition_engine",
                    "hyperframes": "standard_agent_selected_composition_engine",
                },
            },
            "files": sorted(inventory, key=lambda item: item["path"]),
        }
        if bootstrap_runtime is not None:
            manifest["bootstrap_runtime"] = bootstrap_runtime
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
    parser.add_argument("--bootstrap-python-archive", type=Path)
    parser.add_argument("--bootstrap-pip-wheel", type=Path)
    parser.add_argument("--bootstrap-runtime-lock", type=Path)
    args = parser.parse_args()
    try:
        if args.bootstrap_python_archive is None:
            raise PortableBundleContractError(
                "bootstrap Python archive is required for a distributable package"
            )
        if args.bootstrap_pip_wheel is None:
            raise PortableBundleContractError(
                "bootstrap pip wheel is required for a distributable package"
            )
        bootstrap_runtime_lock = (
            args.bootstrap_runtime_lock
            or args.repo_root / "WORKBUDDY-BOOTSTRAP-RUNTIME.lock.json"
        )
        staging = build_portable_staging(
            repo_root=args.repo_root,
            lock_path=args.lock,
            output_root=args.output_root,
            bootstrap_python_archive=args.bootstrap_python_archive,
            bootstrap_pip_wheel=args.bootstrap_pip_wheel,
            bootstrap_runtime_lock_path=bootstrap_runtime_lock,
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
