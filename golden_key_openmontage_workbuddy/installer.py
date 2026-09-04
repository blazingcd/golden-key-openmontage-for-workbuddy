"""Final Shell assembly and lifecycle helpers.

This module is the Installer-owned boundary.  It assembles the immutable
OpenMontage release from its exact checkout, adds the independent Shell
adapter and private toolchain, stamps the binding, and then delegates package
identity checks to the existing Registration/Locator implementation.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import stat
import subprocess
import sys
import tarfile
import uuid
import zipfile
from email.parser import Parser
from pathlib import Path, PurePosixPath
from typing import Any


OPENMONTAGE_RELEASE = "0.3.25"
OPENMONTAGE_COMMIT = "201675c0e550d417654b752f3945f229fb5ceeee"
OPENMONTAGE_TREE = "f5915fdda3448fed509ed8741563643493c1613f"
RELEASE_IDENTITY = f"golden-key-openmontage-{OPENMONTAGE_RELEASE}"
DEFINITION_ID = f"{RELEASE_IDENTITY}-fixed-child-v1"
MANIFEST_NAME = "BUNDLE-MANIFEST.json"
LOCK_NAME = "GOLDEN_KEY_WORKBUDDY_CORE.lock.json"
DEPENDENCY_LOCK_NAME = "bootstrap/python/CORE-DEPENDENCIES.lock.json"
CORE_CONTRACT_ID = "golden-key-workbuddy-callable-core-v1"
DEFINITION_SCHEMA = "golden-key-workbuddy-package-tool-definition-v1"
DEFINITION_REQUEST_HASH = "c5b196bfe69c6a6db7073fb7fa7503a58837907e939fceeb5436fa7d19f80ce1"
DEFINITION_RESULT_HASH = "8a96aceb463da2ea39549de44b06a765a3ac859260001ae277b99dbf2a8ca1b3"
RUNTIME_BINDING_RELATIVE_PATH = "shell-adapter/package-runtime-binding.json"
USER_ENTRY_MODULE = "golden_key_openmontage_workbuddy.user_entry"
USER_ENTRY_RELATIVE_PATH = "shell-adapter/golden_key_openmontage_workbuddy/user_entry.py"
WORKBUDDY_SKILL_ARCHIVE_RELATIVE_PATH = f"Integrations/WorkBuddy/{RELEASE_IDENTITY}.zip"
WORKBUDDY_SKILL_ROOT_RELATIVE_PATH = "shell-adapter/workbuddy-skill/golden-key-openmontage"
WORKBUDDY_DATA_ROOT_PLACEHOLDER = "{{WORKBUDDY_DATA_ROOT}}"
WORKBUDDY_GUIDE_PATH_PLACEHOLDER = "{{WORKBUDDY_GUIDE_PATH}}"
WORKBUDDY_PACKAGE_ROOT_PLACEHOLDER = "{{WORKBUDDY_PACKAGE_ROOT}}"
INSTALLER_CMD_NAME = "安装到WorkBuddy.cmd"
INSTALL_PRODUCT_DIRECTORY = "GoldenKeyOpenMontageForWorkBuddy"
SEVEN_ZIP_SHA256 = "83967f1b02b43c4efeda302795722c809e0e81b8307de73558d10484d5676a7d"
FFMPEG_ARCHIVE_SHA256 = "49a73bdf0850092a252ac4641d922f3048d63ed113e196cc65ce1e4f7fb33e85"
MANAGED_CORE_OWNER = "managed_core"
TOOLCHAIN_OWNER = "workbuddy_required_toolchain"
CONTRACT_OWNER = "core_contract"
SHELL_FILES = (
    "golden_key_openmontage_workbuddy/__init__.py",
    "golden_key_openmontage_workbuddy/installer.py",
    "golden_key_openmontage_workbuddy/package_registration.py",
    "golden_key_openmontage_workbuddy/runtime_prepare.py",
    "golden_key_openmontage_workbuddy/session_launcher.py",
    "golden_key_openmontage_workbuddy/workbuddy_entry_cli.py",
    "golden_key_openmontage_workbuddy/fixed_child.py",
    "golden_key_openmontage_workbuddy/user_entry.py",
    "workbuddy-skill/golden-key-openmontage/SKILL.md",
    "workbuddy-skill/golden-key-openmontage/scripts/run.ps1",
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


class InstallerError(RuntimeError):
    """Fail-closed assembly or lifecycle error."""


def _canonical(value: Any, *, newline: bool = True) -> bytes:
    try:
        raw = json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    except (TypeError, ValueError, UnicodeEncodeError, RecursionError) as exc:
        raise InstallerError(f"canonical_json:{exc}") from exc
    return raw + (b"\n" if newline else b"")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
    except OSError as exc:
        raise InstallerError(f"read_hash:{path}") from exc
    return digest.hexdigest()


def _sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _write_json(path: Path, value: Any) -> bytes:
    payload = _canonical(value)
    path.write_bytes(payload)
    return payload


def _git(checkout: Path, *args: str) -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(checkout), *args], text=True, stderr=subprocess.STDOUT
        ).strip()
    except subprocess.CalledProcessError as exc:
        raise InstallerError(f"git_failed:{' '.join(args)}:{exc.output[-400:]}") from exc


def _safe_member(name: str) -> Path:
    pure = PurePosixPath(name.replace("\\", "/"))
    if pure.is_absolute() or not pure.parts or any(part in {"", ".", ".."} for part in pure.parts):
        raise InstallerError(f"unsafe_archive_member:{name}")
    for part in pure.parts:
        # Archive names are later materialized on Windows. Reject ADS,
        # device aliases, and names whose Win32 spelling is not stable.
        if any(ord(char) < 32 for char in part) or ":" in part:
            raise InstallerError(f"unsafe_archive_member:{name}")
        if part.endswith((".", " ")):
            raise InstallerError(f"unsafe_archive_member:{name}")
        stem = part.rstrip(". ").split(".", 1)[0].casefold()
        if stem in {
            "con",
            "prn",
            "aux",
            "nul",
            *(f"com{number}" for number in range(1, 10)),
            *(f"lpt{number}" for number in range(1, 10)),
        }:
            raise InstallerError(f"unsafe_archive_member:{name}")
    return Path(*pure.parts)


def _assert_no_reparse_chain(path: Path, *, boundary: Path | None = None) -> None:
    """Check every existing component without following a reparse point."""

    path = Path(path)
    if boundary is not None:
        boundary = Path(boundary)
        try:
            path.relative_to(boundary)
        except ValueError as exc:
            raise InstallerError(f"path_outside_root:{path}") from exc
    current = path
    while True:
        try:
            status = current.lstat()
        except FileNotFoundError:
            status = None
        except OSError as exc:
            raise InstallerError(f"path_lstat_failed:{current}") from exc
        if status is not None:
            attrs = getattr(status, "st_file_attributes", 0)
            if stat.S_ISLNK(status.st_mode) or bool(attrs & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)):
                raise InstallerError(f"reparse_asset:{current}")
        if boundary is not None and current == boundary:
            break
        parent = current.parent
        if parent == current:
            break
        current = parent


def _verify_tree_boundary(root: Path) -> None:
    """Ensure an extracted tree contains only regular files/directories."""

    root = Path(root)
    _assert_regular(root)
    _assert_no_reparse_chain(root)
    root_resolved = root.resolve(strict=True)
    for path in root.rglob("*"):
        _assert_no_reparse_chain(path, boundary=root)
        _assert_regular(path)
        try:
            path.resolve(strict=True).relative_to(root_resolved)
        except (OSError, RuntimeError, ValueError) as exc:
            raise InstallerError(f"path_outside_root:{path}") from exc


def _assert_regular(path: Path) -> None:
    try:
        status = path.lstat()
    except OSError as exc:
        raise InstallerError(f"asset_missing:{path}") from exc
    mode = status.st_mode
    attrs = getattr(status, "st_file_attributes", 0)
    if path.is_symlink() or bool(attrs & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)):
        raise InstallerError(f"reparse_asset:{path}")
    if not (stat.S_ISREG(mode) or stat.S_ISDIR(mode)):
        raise InstallerError(f"non_regular_asset:{path}")


def _inventory(root: Path) -> list[Path]:
    if not root.is_dir():
        raise InstallerError(f"package_root_missing:{root}")
    paths: list[Path] = []
    for path in root.rglob("*"):
        _assert_regular(path)
        if path.is_file():
            paths.append(path)
    return sorted(paths, key=lambda item: item.relative_to(root).as_posix().casefold())


def _relative(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError as exc:
        raise InstallerError(f"path_outside_root:{path}") from exc


def _extract_tar(archive: Path, destination: Path) -> None:
    seen: set[str] = set()
    try:
        stream = tarfile.open(archive, "r")
    except (OSError, tarfile.TarError) as exc:
        raise InstallerError(f"invalid_git_archive:{archive}") from exc
    with stream:
        for member in stream.getmembers():
            relative = _safe_member(member.name).as_posix()
            if relative.casefold() in seen:
                raise InstallerError(f"duplicate_archive_member:{relative}")
            seen.add(relative.casefold())
            target = destination.joinpath(*PurePosixPath(relative).parts)
            if member.issym() or member.islnk() or not (member.isdir() or member.isfile()):
                raise InstallerError(f"unsafe_git_archive_member:{relative}")
            if member.isdir():
                _assert_no_reparse_chain(target, boundary=destination)
                target.mkdir(parents=True, exist_ok=True)
                continue
            source = stream.extractfile(member)
            if source is None:
                raise InstallerError(f"git_archive_read_failed:{relative}")
            _assert_no_reparse_chain(target.parent, boundary=destination)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read())
    _verify_tree_boundary(destination)


def _extract_zip(archive: Path, destination: Path) -> None:
    seen: set[str] = set()
    try:
        stream = zipfile.ZipFile(archive)
    except (OSError, zipfile.BadZipFile) as exc:
        raise InstallerError(f"invalid_zip:{archive}") from exc
    with stream:
        for member in stream.infolist():
            relative_path = _safe_member(member.filename.rstrip("/") if member.is_dir() else member.filename)
            relative = relative_path.as_posix()
            if relative.casefold() in seen:
                raise InstallerError(f"duplicate_zip_member:{relative}")
            seen.add(relative.casefold())
            mode = (member.external_attr >> 16) & 0xFFFF
            if mode and stat.S_ISLNK(mode):
                raise InstallerError(f"zip_symlink:{relative}")
            target = destination.joinpath(*relative_path.parts)
            if member.is_dir():
                _assert_no_reparse_chain(target, boundary=destination)
                target.mkdir(parents=True, exist_ok=True)
            else:
                _assert_no_reparse_chain(target.parent, boundary=destination)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(stream.read(member))
    _verify_tree_boundary(destination)


def _flatten_single_directory(stage: Path, destination: Path) -> None:
    _verify_tree_boundary(stage)
    children = [child for child in stage.iterdir()]
    if len(children) != 1 or not children[0].is_dir() or children[0].is_symlink():
        raise InstallerError(f"archive_top_level_not_single_directory:{stage}")
    source = children[0]
    _assert_no_reparse_chain(destination)
    destination.mkdir(parents=True, exist_ok=True)
    _assert_no_reparse_chain(destination)
    for child in source.iterdir():
        _assert_regular(child)
        target = destination / child.name
        _assert_no_reparse_chain(target, boundary=destination)
        if target.exists() or target.is_symlink():
            raise InstallerError(f"archive_destination_collision:{target}")
        shutil.move(str(child), str(target))
    _verify_tree_boundary(destination)


def _prune_ffmpeg_distribution(root: Path) -> None:
    # The product registers ffmpeg/ffprobe; ffplay and upstream HTML docs add about 110 MiB installed.
    (root / "bin" / "ffplay.exe").unlink(missing_ok=True)
    docs = root / "doc"
    if docs.exists():
        shutil.rmtree(docs)


def _verify_package_checkout(checkout: Path) -> dict[str, Any]:
    head = _git(checkout, "rev-parse", "HEAD")
    tree = _git(checkout, "rev-parse", "HEAD^{tree}")
    status = _git(checkout, "status", "--porcelain")
    if head != OPENMONTAGE_COMMIT or tree != OPENMONTAGE_TREE or status:
        raise InstallerError("openmontage_identity_or_clean_state_mismatch")
    release_path = checkout / "GOLDEN_KEY_OPENMONTAGE_RELEASE.json"
    lock_path = checkout / "GOLDEN_KEY_OPENMONTAGE.lock.json"
    if not release_path.is_file() or not lock_path.is_file():
        raise InstallerError("openmontage_release_lock_missing")
    release = json.loads(release_path.read_text(encoding="utf-8"))
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    if release.get("release_version") != OPENMONTAGE_RELEASE:
        raise InstallerError("openmontage_release_mismatch")
    entries = lock.get("files")
    if not isinstance(entries, list) or lock.get("file_count") != len(entries):
        raise InstallerError("openmontage_lock_shape_mismatch")
    if _sha256_bytes(_canonical(entries, newline=False)) != lock.get("bundle_sha256"):
        raise InstallerError("openmontage_lock_bundle_mismatch")
    for item in entries:
        relative = _safe_member(item.get("path"))
        path = checkout.joinpath(*relative.parts)
        if not path.is_file() or path.is_symlink() or path.stat().st_size != item.get("size") or _sha256(path) != item.get("sha256"):
            raise InstallerError(f"openmontage_source_lock_mismatch:{relative.as_posix()}")
    return {
        "checkout": str(checkout.resolve()),
        "commit": head,
        "tree": tree,
        "release_version": release["release_version"],
        "source_lock_file_count": len(entries),
        "source_lock_bundle_sha256": lock["bundle_sha256"],
        "source_lock": lock,
    }


def _copy_shell_source(shell_source: Path, root: Path) -> None:
    adapter_root = root / "shell-adapter"
    for relative_text in SHELL_FILES:
        source = shell_source.joinpath(*PurePosixPath(relative_text).parts)
        if not source.is_file() or source.is_symlink():
            raise InstallerError(f"shell_source_missing:{relative_text}")
        destination = adapter_root.joinpath(*PurePosixPath(relative_text).parts)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def _verify_materialized_source(root: Path, source_lock: dict[str, Any]) -> None:
    """Recheck immutable OpenMontage bytes after archive extraction."""

    for item in source_lock.get("files", []):
        relative = _safe_member(item.get("path"))
        path = root.joinpath(*relative.parts)
        if not path.is_file() or path.is_symlink() or path.stat().st_size != item.get("size") or _sha256(path) != item.get("sha256"):
            raise InstallerError(f"materialized_source_mismatch:{relative.as_posix()}")


def _install_wheelhouse(wheelhouse: Path, site_packages: Path) -> int:
    wheels = sorted(wheelhouse.glob("*.whl"), key=lambda path: path.name.casefold())
    if not wheels:
        raise InstallerError("wheelhouse_empty")
    site_packages.mkdir(parents=True, exist_ok=True)
    for wheel in wheels:
        _extract_zip(wheel, site_packages)
    return len(wheels)


def _verified_seven_zip(seven_zip: Path) -> Path:
    """Return the fixed local 7-Zip executable after no-follow checks."""

    seven_zip = Path(seven_zip)
    _assert_regular(seven_zip)
    if not seven_zip.is_file():
        raise InstallerError(f"seven_zip_missing:{seven_zip}")
    try:
        resolved = seven_zip.resolve(strict=True)
        # The installer accepts only the installed fixed tool, never a
        # caller-supplied executable selected from PATH.
        fixed = Path(r"C:\Program Files\7-Zip\7z.exe").resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        raise InstallerError("seven_zip_identity_unavailable") from exc
    if resolved != fixed:
        raise InstallerError(f"seven_zip_not_fixed:{seven_zip}")
    if _sha256(resolved) != SEVEN_ZIP_SHA256:
        raise InstallerError("seven_zip_identity_mismatch")
    return resolved


def _seven_zip_listing(seven_zip: Path, archive: Path) -> list[dict[str, str]]:
    """List and validate every 7z member before allowing external extraction."""

    seven_zip = _verified_seven_zip(seven_zip)
    _assert_regular(archive)
    if not archive.is_file():
        raise InstallerError(f"ffmpeg_archive_missing:{archive}")
    if _sha256(archive) != FFMPEG_ARCHIVE_SHA256:
        raise InstallerError("ffmpeg_archive_identity_mismatch")
    try:
        completed = subprocess.run(
            [str(seven_zip), "l", "-slt", str(archive)],
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="strict",
        )
    except (OSError, UnicodeError, subprocess.CalledProcessError) as exc:
        raise InstallerError("ffmpeg_archive_listing_failed") from exc

    records: list[dict[str, str]] = []
    current: dict[str, str] = {}

    def finish() -> None:
        if not current or "Attributes" not in current:
            return
        member_name = current.get("Path")
        attributes = current.get("Attributes", "")
        if not member_name or "L" in attributes.upper():
            raise InstallerError("ffmpeg_archive_link_member")
        for key, value in current.items():
            if key.casefold() in {"symbolic link", "hard link", "reparse point", "junction"} and value:
                raise InstallerError("ffmpeg_archive_link_member")
        relative = _safe_member(member_name).as_posix()
        key = relative.casefold()
        if any(item["path"].casefold() == key for item in records):
            raise InstallerError(f"duplicate_archive_member:{relative}")
        records.append({"path": relative, "attributes": attributes})

    for line in completed.stdout.replace("\r\n", "\n").split("\n"):
        if not line.strip():
            finish()
            current = {}
            continue
        if line.strip() == "----------":
            finish()
            current = {}
            continue
        if " = " not in line:
            continue
        key, value = line.split(" = ", 1)
        if key in current:
            raise InstallerError("ffmpeg_archive_listing_malformed")
        current[key] = value
    finish()
    if not records:
        raise InstallerError("ffmpeg_archive_listing_empty")
    return records


def _install_toolchain(
    root: Path,
    *,
    python_archive: Path,
    ffmpeg_archive: Path,
    node_archive: Path,
    wheelhouse: Path,
    seven_zip: Path,
) -> dict[str, Any]:
    bootstrap = root / "bootstrap"
    python_root = bootstrap / "python"
    node_root = bootstrap / "node"
    ffmpeg_root = bootstrap / "ffmpeg"
    _extract_zip(python_archive, python_root)
    pth_files = sorted(python_root.glob("python*._pth"), key=lambda path: path.name.casefold())
    if len(pth_files) != 1:
        raise InstallerError("python_embedded_path_file_mismatch")
    lines = [line.strip() for line in pth_files[0].read_text(encoding="utf-8").splitlines() if line.strip()]
    for required in ("Lib/site-packages", "../../shell-adapter"):
        if required not in lines:
            lines.append(required)
    if "import site" not in lines:
        lines.append("import site")
    pth_files[0].write_text("\n".join(lines) + "\n", encoding="utf-8", newline="")
    site_packages = python_root / "Lib" / "site-packages"
    wheel_count = _install_wheelhouse(wheelhouse, site_packages)
    # Keep imported shell modules from creating bytecode inside the locked root.
    (site_packages / "golden_key_workbuddy_runtime_guard.pth").write_text(
        "import sys; sys.dont_write_bytecode = True\n", encoding="utf-8", newline=""
    )

    node_stage = root / ".node-stage"
    _extract_zip(node_archive, node_stage)
    try:
        _flatten_single_directory(node_stage, node_root)
    finally:
        shutil.rmtree(node_stage, ignore_errors=True)

    seven_zip = _verified_seven_zip(seven_zip)
    _seven_zip_listing(seven_zip, ffmpeg_archive)
    ffmpeg_stage = root / ".ffmpeg-stage"
    _assert_no_reparse_chain(ffmpeg_stage, boundary=root)
    ffmpeg_stage.mkdir()
    try:
        subprocess.run(
            [str(seven_zip), "x", "-y", str(ffmpeg_archive), f"-o{ffmpeg_stage}"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
        )
        _verify_tree_boundary(ffmpeg_stage)
        _flatten_single_directory(ffmpeg_stage, ffmpeg_root)
        _prune_ffmpeg_distribution(ffmpeg_root)
    except (OSError, subprocess.CalledProcessError) as exc:
        raise InstallerError("ffmpeg_archive_extract_failed") from exc
    finally:
        shutil.rmtree(ffmpeg_stage, ignore_errors=True)
    _verify_tree_boundary(ffmpeg_root)

    interpreter = python_root / "python.exe"
    ffmpeg = ffmpeg_root / "bin" / "ffmpeg.exe"
    ffprobe = ffmpeg_root / "bin" / "ffprobe.exe"
    node = node_root / "node.exe"
    npm = node_root / "npm.cmd"
    npx = node_root / "npx.cmd"
    for path in (interpreter, ffmpeg, ffprobe, node, npm, npx):
        if not path.is_file():
            raise InstallerError(f"required_toolchain_file_missing:{path}")
    try:
        python_version = subprocess.check_output([str(interpreter), "--version"], text=True, stderr=subprocess.STDOUT).strip()
        node_version = subprocess.check_output([str(node), "--version"], text=True, stderr=subprocess.STDOUT).strip().lstrip("v")
    except (OSError, subprocess.CalledProcessError) as exc:
        raise InstallerError("private_toolchain_probe_failed") from exc
    if not python_version.startswith("Python ") or tuple(int(part) for part in python_version.split()[1].split(".")[:2]) < (3, 10):
        raise InstallerError("private_python_version_below_3_10")
    if not node_version or int(node_version.split(".", 1)[0]) < 22:
        raise InstallerError("private_node_version_below_22")
    return {
        "python_version": python_version.removeprefix("Python "),
        "node_version": node_version,
        "wheel_count": wheel_count,
        "source_archives": {
            "python": {"sha256": _sha256(python_archive), "size": python_archive.stat().st_size},
            "ffmpeg": {"sha256": _sha256(ffmpeg_archive), "size": ffmpeg_archive.stat().st_size},
            "node": {"sha256": _sha256(node_archive), "size": node_archive.stat().st_size},
        },
    }


def _file_entry(root: Path, path: Path, owner: str) -> dict[str, Any]:
    return {
        "path": _relative(root, path),
        "owner": owner,
        "sha256": _sha256(path),
        "size": path.stat().st_size,
    }


def _dependency_lock(root: Path, package_checkout: Path, python_version: str) -> dict[str, Any]:
    site = root / "bootstrap" / "python" / "Lib" / "site-packages"
    packages: list[dict[str, str]] = []
    for metadata_path in sorted(site.glob("*.dist-info/METADATA"), key=lambda path: path.as_posix().casefold()):
        metadata = Parser().parsestr(metadata_path.read_text(encoding="utf-8"))
        name = metadata.get("Name")
        version = metadata.get("Version")
        if not name or not version:
            raise InstallerError(f"dependency_metadata_incomplete:{metadata_path}")
        packages.append({"name": name, "version": version, "metadata_path": _relative(root, metadata_path)})
    if not packages:
        raise InstallerError("dependency_metadata_missing")
    requirements = [
        line.strip()
        for line in (package_checkout / "requirements.txt").read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]
    value = {
        "schema_version": "golden-key-workbuddy-python-core-dependencies-v1",
        "python_version": python_version,
        "requirements": requirements,
        "packages": sorted(packages, key=lambda item: item["name"].casefold()),
    }
    path = root / DEPENDENCY_LOCK_NAME
    payload = _write_json(path, value)
    return {"path": _relative(root, path), "sha256": _sha256_bytes(payload), "size": len(payload), "distribution_count": len(packages), "packages": value["packages"]}


def _bridge_schema_hashes(root: Path) -> tuple[str, str]:
    """Load the staged adapter under an alias so its computed descriptors bind."""

    # Assembly imports the staged adapter only to bind its closed-wire hashes;
    # bytecode in the immutable PackageRoot would be an unbound generated file.
    previous_dont_write_bytecode = sys.dont_write_bytecode
    sys.dont_write_bytecode = True
    package_dir = root / "shell-adapter" / "golden_key_openmontage_workbuddy"
    alias = f"_golden_key_staged_{uuid.uuid4().hex}"
    package_spec = importlib.util.spec_from_file_location(
        alias,
        package_dir / "__init__.py",
        submodule_search_locations=[str(package_dir)],
    )
    if package_spec is None or package_spec.loader is None:
        raise InstallerError("staged_adapter_package_spec_missing")
    package = importlib.util.module_from_spec(package_spec)
    sys.modules[alias] = package
    try:
        package_spec.loader.exec_module(package)
        entry_spec = importlib.util.spec_from_file_location(
            f"{alias}.workbuddy_entry_cli",
            package_dir / "workbuddy_entry_cli.py",
        )
        if entry_spec is None or entry_spec.loader is None:
            raise InstallerError("staged_adapter_entry_spec_missing")
        entry = importlib.util.module_from_spec(entry_spec)
        sys.modules[entry_spec.name] = entry
        entry_spec.loader.exec_module(entry)
        return entry._REQUEST_SCHEMA_SHA256, entry._RESULT_SCHEMA_SHA256
    finally:
        for name in tuple(sys.modules):
            if name == alias or name.startswith(alias + "."):
                sys.modules.pop(name, None)
        sys.dont_write_bytecode = previous_dont_write_bytecode


def _definition_and_skill(root: Path) -> dict[str, Any]:
    child = root / "shell-adapter" / "golden_key_openmontage_workbuddy" / "fixed_child.py"
    module = root / "shell-adapter" / "golden_key_openmontage_workbuddy" / "workbuddy_entry_cli.py"
    user_entry = root / USER_ENTRY_RELATIVE_PATH
    interpreter = root / "bootstrap" / "python" / "python.exe"
    if not all(path.is_file() for path in (child, module, user_entry, interpreter)):
        raise InstallerError("binding_asset_missing")
    definition = {
        "schema_version": DEFINITION_SCHEMA,
        "definition_id": DEFINITION_ID,
        "definition_relative_path": "shell-adapter/package-tool-definition.json",
        "authority_owner": MANAGED_CORE_OWNER,
        # Stage 4 binds this value to Locator.openmontage_release (0.3.25);
        # the Skill's separate release identity remains the full asset name.
        "package_release": OPENMONTAGE_RELEASE,
        "package_commit": OPENMONTAGE_COMMIT,
        "tool_id": DEFINITION_ID,
        "relative_path": "shell-adapter/golden_key_openmontage_workbuddy/fixed_child.py",
        "sha256": _sha256(child),
        "size": child.stat().st_size,
        "owner": MANAGED_CORE_OWNER,
        "execution_kind": "PACKAGE_PYTHON_SCRIPT",
        "interpreter_binding": "LOCATOR_PACKAGE_PYTHON",
        "fixed_argv_template": ["{verified_tool_path}"],
        "fixed_argv_placeholders": ["{verified_tool_path}"],
        "request_schema_sha256": DEFINITION_REQUEST_HASH,
        "result_schema_sha256": DEFINITION_RESULT_HASH,
        "allowed_environment_names": ["ARK_API_KEY"],
        "secret_environment_names": ["ARK_API_KEY"],
        "required_local_capabilities": [],
    }
    definition["definition_sha256"] = _sha256_bytes(_canonical(definition))
    definition_path = root / "shell-adapter" / "package-tool-definition.json"
    _write_json(definition_path, definition)
    bridge_request_hash, bridge_result_hash = _bridge_schema_hashes(root)
    fixed_argv = ["-I", "-m", "golden_key_openmontage_workbuddy.workbuddy_entry_cli"]
    fixed_argv_text = json.dumps(fixed_argv, ensure_ascii=False, separators=(",", ":"))
    skill_path = root / "shell-adapter" / "workbuddy-skill" / "golden-key-openmontage" / "SKILL.md"
    skill = skill_path.read_text(encoding="utf-8")
    if "<installer:" in skill:
        raise InstallerError("skill_placeholder_remaining")
    binding = {
        "schema_version": "golden-key-workbuddy-user-entry-binding-v1",
        "data_root_relative": "../../data/production",
        "entry_module": USER_ENTRY_MODULE,
        "entry_argv": fixed_argv,
        "entry_module_sha256": _sha256(user_entry),
        "bridge_module": "golden_key_openmontage_workbuddy.workbuddy_entry_cli",
        "bridge_module_sha256": _sha256(module),
        "fixed_argv_sha256": _sha256_bytes(fixed_argv_text.encode("utf-8")),
        "request_schema_sha256": bridge_request_hash,
        "result_schema_sha256": bridge_result_hash,
        "definition_relative_path": definition["definition_relative_path"],
        "definition_sha256": definition["definition_sha256"],
    }
    binding_path = root / RUNTIME_BINDING_RELATIVE_PATH
    binding_payload = _write_json(binding_path, binding)
    return {
        "definition_relative_path": _relative(root, definition_path),
        "definition_id": definition["definition_id"],
        "definition_sha256": definition["definition_sha256"],
        "definition_size": definition_path.stat().st_size,
        "child_relative_path": _relative(root, child),
        "child_sha256": _sha256(child),
        "child_size": child.stat().st_size,
        "module_relative_path": _relative(root, module),
        "module_sha256": _sha256(module),
        "skill_relative_path": _relative(root, skill_path),
        "skill_sha256": _sha256(skill_path),
        "fixed_argv": fixed_argv,
        "fixed_argv_sha256": _sha256_bytes(fixed_argv_text.encode("utf-8")),
        "binding_relative_path": _relative(root, binding_path),
        "binding_sha256": _sha256_bytes(binding_payload),
        "entry_module": USER_ENTRY_MODULE,
        "entry_module_relative_path": _relative(root, user_entry),
        "entry_module_sha256": _sha256(user_entry),
        "interpreter_relative_path": _relative(root, interpreter),
        "interpreter_sha256": _sha256(interpreter),
    }


def _build_manifest_and_lock(root: Path, toolchain: dict[str, Any], dependency_lock: dict[str, Any]) -> dict[str, Any]:
    all_paths = _inventory(root)
    toolchain_prefixes = ("bootstrap/python/", "bootstrap/ffmpeg/", "bootstrap/node/")
    toolchain_paths = [path for path in all_paths if _relative(root, path).startswith(toolchain_prefixes)]
    excluded = {MANIFEST_NAME, LOCK_NAME}
    core_paths = [path for path in all_paths if _relative(root, path) not in excluded and path not in toolchain_paths]
    if not any(_relative(root, path) == "AGENT_GUIDE.md" for path in core_paths):
        raise InstallerError("package_guide_missing")
    lock_files = [
        {
            "path": f"workbuddy-core/{_relative(root, path)}",
            "source_path": _relative(root, path),
            "sha256": _sha256(path),
            "size": path.stat().st_size,
            "source_mode": "100644",
            "apply_mode": "replace",
            "classification": "workbuddy_callable",
        }
        for path in core_paths
    ]
    lock = {
        "schema_version": 2,
        "contract_id": CORE_CONTRACT_ID,
        "source_ref": OPENMONTAGE_RELEASE,
        "source_commit": OPENMONTAGE_COMMIT,
        "authority": LOCK_AUTHORITY,
        "files": lock_files,
        "bundle_sha256": _sha256_bytes(_canonical(lock_files, newline=False)),
    }
    lock_path = root / LOCK_NAME
    _write_json(lock_path, lock)
    manifest_files = [_file_entry(root, path, MANAGED_CORE_OWNER) for path in core_paths]
    manifest_files.extend(_file_entry(root, path, TOOLCHAIN_OWNER) for path in toolchain_paths)
    manifest_files.append(_file_entry(root, lock_path, CONTRACT_OWNER))
    manifest = {
        "schema_version": "golden-key-workbuddy-portable-bundle-v2",
        "distribution": {"channel": "golden-key-final-delivery", "format": "portable_zip"},
        "core": {
            "contract_id": CORE_CONTRACT_ID,
            "tag": OPENMONTAGE_RELEASE,
            "source_commit": OPENMONTAGE_COMMIT,
            "file_count": len(lock_files),
            "usage": "workbuddy_shell_v2_final_package",
        },
        "authority": MANIFEST_AUTHORITY,
        "installation": {"runtime_roles": {"python": "bundled_private_interpreter", "ffmpeg": "bundled_media_toolchain", "node": "bundled_javascript_toolchain"}},
        "required_toolchain": {
            "python": {
                "version": toolchain["python_version"],
                "source": "python.org_windows_embeddable_x64",
                "source_archive_sha256": toolchain["source_archives"]["python"]["sha256"],
                "source_archive_size": toolchain["source_archives"]["python"]["size"],
                "system_python_required": False,
                "executable": "bootstrap/python/python.exe",
                "dependency_lock": DEPENDENCY_LOCK_NAME,
            },
            "ffmpeg": {
                "version": "9.0.1-essentials_build",
                "source": "gyan.dev_ffmpeg_release_essentials_x64",
                "source_archive_sha256": toolchain["source_archives"]["ffmpeg"]["sha256"],
                "source_archive_size": toolchain["source_archives"]["ffmpeg"]["size"],
                "ffmpeg": "bootstrap/ffmpeg/bin/ffmpeg.exe",
                "ffprobe": "bootstrap/ffmpeg/bin/ffprobe.exe",
            },
            "node": {
                "version": toolchain["node_version"],
                "source": "npmmirror_node_windows_x64",
                "source_archive_sha256": toolchain["source_archives"]["node"]["sha256"],
                "source_archive_size": toolchain["source_archives"]["node"]["size"],
                "node": "bootstrap/node/node.exe",
                "npm": "bootstrap/node/npm.cmd",
                "npx": "bootstrap/node/npx.cmd",
            },
            "managed_files": sorted(_relative(root, path) for path in toolchain_paths),
        },
        "files": sorted(manifest_files, key=lambda item: item["path"].casefold()),
    }
    manifest_path = root / MANIFEST_NAME
    _write_json(manifest_path, manifest)
    manifest["files"] = [
        _file_entry(root, lock_path, CONTRACT_OWNER) if item["path"] == LOCK_NAME else item
        for item in manifest["files"]
    ]
    _write_json(manifest_path, manifest)
    return {
        "manifest_path": str(manifest_path),
        "manifest_sha256": _sha256(manifest_path),
        "manifest_size": manifest_path.stat().st_size,
        "lock_path": str(lock_path),
        "lock_sha256": _sha256(lock_path),
        "lock_size": lock_path.stat().st_size,
        "lock_bundle_sha256": lock["bundle_sha256"],
        "core_file_count": len(lock_files),
        "toolchain_file_count": len(toolchain_paths),
        "dependency_lock": dependency_lock,
    }


def _build_release(root: Path, destination: Path) -> dict[str, Any]:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        raise InstallerError(f"release_already_exists:{destination}")
    prefix = "GoldenKeyOpenMontageForWorkBuddy/"
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in _inventory(root):
            info = zipfile.ZipInfo(prefix + _relative(root, path), date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 0
            info.external_attr = 0
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    digest = _sha256(destination)
    sidecar = destination.with_name(destination.name + ".sha256")
    sidecar.write_text(f"{digest} *{destination.name}\n", encoding="utf-8", newline="")
    return {"path": str(destination), "sha256": digest, "size": destination.stat().st_size, "sidecar": str(sidecar)}


def _build_formal_release(inner_release: Path, installer_cmd: Path) -> dict[str, Any]:
    sidecar = inner_release.with_name(inner_release.name + ".sha256")
    for path in (inner_release, sidecar, installer_cmd):
        if not path.is_file() or path.is_symlink():
            raise InstallerError(f"formal_release_input_invalid:{path.name}")
    destination = inner_release.with_name(f"{inner_release.stem}-installer.zip")
    if destination.exists() or destination.is_symlink():
        raise InstallerError(f"formal_release_already_exists:{destination}")
    entries = (
        (INSTALLER_CMD_NAME, installer_cmd),
        (inner_release.name, inner_release),
        (sidecar.name, sidecar),
    )
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, path in entries:
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 0
            info.external_attr = 0
            info.compress_type = zipfile.ZIP_DEFLATED
            with path.open("rb") as source, archive.open(info, "w", force_zip64=True) as target:
                shutil.copyfileobj(source, target, length=1024 * 1024)
    return {
        "path": str(destination),
        "sha256": _sha256(destination),
        "size": destination.stat().st_size,
        "members": [name for name, _path in entries],
    }


def assemble_package(
    *,
    package_checkout: os.PathLike[str] | str,
    shell_source: os.PathLike[str] | str,
    python_archive: os.PathLike[str] | str,
    ffmpeg_archive: os.PathLike[str] | str,
    node_archive: os.PathLike[str] | str,
    wheelhouse: os.PathLike[str] | str,
    seven_zip: os.PathLike[str] | str,
    package_root: os.PathLike[str] | str,
    release_archive: os.PathLike[str] | str,
) -> dict[str, Any]:
    """Build one deterministic final PackageRoot and release ZIP."""

    checkout = Path(package_checkout).resolve(strict=True)
    shell = Path(shell_source).resolve(strict=True)
    root = Path(package_root).resolve()
    release = Path(release_archive).resolve()
    inputs = [Path(p).resolve(strict=True) for p in (python_archive, ffmpeg_archive, node_archive, wheelhouse, seven_zip)]
    if root.exists() or release.exists():
        raise InstallerError("assembly_destination_already_exists")
    source = _verify_package_checkout(checkout)
    staging = root.with_name(f".{root.name}.staging-{uuid.uuid4().hex}")
    staging.mkdir(parents=True)
    git_tar = staging.parent / f".{staging.name}.openmontage.tar"
    try:
        subprocess.run(["git", "-C", str(checkout), "archive", "--format=tar", f"--output={git_tar}", OPENMONTAGE_COMMIT], check=True)
        _extract_tar(git_tar, staging)
        _verify_materialized_source(staging, source["source_lock"])
        _copy_shell_source(shell, staging)
        toolchain = _install_toolchain(
            staging,
            python_archive=inputs[0],
            ffmpeg_archive=inputs[1],
            node_archive=inputs[2],
            wheelhouse=inputs[3],
            seven_zip=inputs[4],
        )
        binding = _definition_and_skill(staging)
        dependency_lock = _dependency_lock(staging, checkout, toolchain["python_version"])
        manifest_lock = _build_manifest_and_lock(staging, toolchain, dependency_lock)
        release_info = _build_release(staging, release)
        formal_release = _build_formal_release(release, shell / INSTALLER_CMD_NAME)
        os.replace(staging, root)
        return {
            "schema_version": "golden-key-workbuddy-final-assembly-v1",
            "package_root": str(root),
            "release": release_info,
            "formal_release": formal_release,
            "package": {key: value for key, value in source.items() if key != "source_lock"},
            "toolchain": toolchain,
            "binding": binding,
            "manifest_lock": manifest_lock,
        }
    finally:
        git_tar.unlink(missing_ok=True)
        if staging.exists():
            shutil.rmtree(staging, ignore_errors=True)


def _release_members(archive: Path) -> list[tuple[zipfile.ZipInfo, Path]]:
    prefix = "GoldenKeyOpenMontageForWorkBuddy/"
    seen: set[str] = set()
    members: list[tuple[zipfile.ZipInfo, Path]] = []
    with zipfile.ZipFile(archive) as stream:
        for member in stream.infolist():
            name = member.filename
            if member.is_dir():
                name = name.rstrip("/")
            if not name.startswith(prefix):
                raise InstallerError(f"release_prefix_mismatch:{name}")
            relative = _safe_member(name[len(prefix):])
            key = relative.as_posix().casefold()
            if key in seen:
                raise InstallerError(f"release_duplicate_member:{relative}")
            seen.add(key)
            mode = (member.external_attr >> 16) & 0xFFFF
            if mode and stat.S_ISLNK(mode):
                raise InstallerError(f"release_symlink:{relative}")
            if not member.is_dir():
                with stream.open(member) as payload:
                    for _chunk in iter(lambda: payload.read(1024 * 1024), b""):
                        pass
            members.append((member, relative))
    return members


def _extract_release(archive: Path, destination: Path) -> None:
    with zipfile.ZipFile(archive) as stream:
        for member, relative in _release_members(archive):
            target = destination.joinpath(*relative.parts)
            if member.is_dir():
                _assert_no_reparse_chain(target, boundary=destination)
                target.mkdir(parents=True, exist_ok=True)
            else:
                _assert_no_reparse_chain(target.parent, boundary=destination)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(stream.read(member))
    _verify_tree_boundary(destination)


def _skill_archive_name(value: os.PathLike[str] | str | None) -> str:
    name = Path(WORKBUDDY_SKILL_ARCHIVE_RELATIVE_PATH).name if value is None else os.fspath(value)
    if not isinstance(name, str):
        raise InstallerError("workbuddy_skill_archive_name_invalid")
    try:
        relative = _safe_member(name)
    except InstallerError as exc:
        raise InstallerError("workbuddy_skill_archive_name_invalid") from exc
    if len(relative.parts) != 1 or relative.name != name or relative.suffix.casefold() != ".zip":
        raise InstallerError("workbuddy_skill_archive_name_invalid")
    return name


def _build_workbuddy_skill_archive(
    data_root: Path,
    package_root: Path,
    *,
    skill_source_root: Path | None = None,
    archive_name: os.PathLike[str] | str | None = None,
    reuse_if_identical: bool = False,
) -> dict[str, Any]:
    data_root = Path(data_root).resolve(strict=True)
    package_root = Path(package_root).resolve(strict=True)
    skill_root = package_root / WORKBUDDY_SKILL_ROOT_RELATIVE_PATH
    if skill_source_root is not None:
        skill_root = Path(skill_source_root).resolve(strict=True)
    skill_path = skill_root / "SKILL.md"
    _assert_regular(skill_path)
    _assert_no_reparse_chain(skill_path, boundary=skill_root)
    guide_path = package_root / "AGENT_GUIDE.md"
    _assert_regular(guide_path)
    _assert_no_reparse_chain(guide_path, boundary=package_root)
    if not guide_path.is_file():
        raise InstallerError("workbuddy_guide_not_file")
    skill = skill_path.read_text(encoding="utf-8")
    if "<installer:" in skill:
        raise InstallerError("workbuddy_skill_placeholder_remaining")
    replacements = {
        WORKBUDDY_DATA_ROOT_PLACEHOLDER: str(data_root),
        WORKBUDDY_GUIDE_PATH_PLACEHOLDER: str(guide_path),
        WORKBUDDY_PACKAGE_ROOT_PLACEHOLDER: str(package_root),
    }
    if any(skill.count(placeholder) != 1 for placeholder in replacements):
        raise InstallerError("workbuddy_skill_installation_placeholder_invalid")
    for placeholder, value in replacements.items():
        skill = skill.replace(placeholder, value)

    candidate_archive = archive_name is not None
    destination = data_root / "Integrations" / "WorkBuddy" / _skill_archive_name(archive_name)
    _assert_no_reparse_chain(destination.parent, boundary=data_root)
    destination.parent.mkdir(parents=True, exist_ok=True)
    _assert_no_reparse_chain(destination.parent, boundary=data_root)
    temporary = destination.with_name(f".{destination.name}.{uuid.uuid4().hex}.tmp")
    try:
        with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
            info = zipfile.ZipInfo("SKILL.md", date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 0
            info.external_attr = 0
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, skill.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
        digest = _sha256(temporary)
        size = temporary.stat().st_size
        if candidate_archive and (destination.exists() or destination.is_symlink()):
            if (
                reuse_if_identical
                and destination.is_file()
                and not destination.is_symlink()
                and destination.stat().st_size == size
                and _sha256(destination) == digest
            ):
                return {
                    "path": str(destination),
                    "archive_name": destination.name,
                    "sha256": digest,
                    "size": size,
                }
            raise InstallerError(f"workbuddy_skill_archive_already_exists:{destination.name}")
        os.replace(temporary, destination)
        return {
            "path": str(destination),
            "archive_name": destination.name,
            "sha256": digest,
            "size": size,
        }
    finally:
        temporary.unlink(missing_ok=True)


def install_release(
    *,
    data_root: os.PathLike[str] | str,
    release_archive: os.PathLike[str] | str,
    package_root: os.PathLike[str] | str,
) -> dict[str, Any]:
    """Install and register one stamped release without activating it."""

    from .package_registration import (
        _active_lock,
        _build_registration,
        _ensure_register_lock,
        _load_registration,
        _parse_active,
        _publish_registration_object,
        _read_active_raw,
        _registry_paths,
        _restore_active_locked,
        _verify_fixed_existing,
    )

    data = Path(data_root).resolve(strict=True)
    archive = _validate_release_archive(Path(release_archive))
    sidecar = archive.with_name(archive.name + ".sha256")
    root = Path(package_root).resolve()
    if root.exists():
        raise InstallerError("install_destination_or_sidecar_invalid")
    _assert_no_reparse_chain(root.parent)
    paths = _registry_paths(data)
    _ensure_register_lock(paths)
    staging = root.with_name(f".{root.name}.install-{uuid.uuid4().hex}")
    try:
        staging.mkdir(parents=True)
        with _active_lock(paths):
            previous_active_raw = _read_active_raw(paths)
            root_installed = False
            registration_path: Path | None = None
            registration_raw: bytes | None = None
            registration_created = False
            created_skill_paths: list[Path] = []
            previous_registration_sha: str | None = None
            previous_root: Path | None = None
            if previous_active_raw is not None:
                previous_pointer = _parse_active(previous_active_raw)
                previous_registration_sha = previous_pointer["registration_sha256"]
                previous_registration = _load_registration(paths, previous_registration_sha)
                previous_root = Path(previous_registration["package_root"])
            try:
                # The destination check belongs inside the lifecycle lock too.
                if root.exists() or root.is_symlink():
                    raise InstallerError("install_destination_or_sidecar_invalid")
                _extract_release(archive, staging)
                _verify_tree_boundary(staging)
                os.replace(staging, root)
                root_installed = True
                _verify_tree_boundary(root)
                _registration, registration_raw, registration_sha = _build_registration(
                    release_archive=archive,
                    release_sha256_sidecar=sidecar,
                    package_root=root,
                    package_python=root / "bootstrap" / "python" / "python.exe",
                )
                registration_path = paths.objects / f"{registration_sha}.json"
                registration_created = not registration_path.exists()
                _publish_registration_object(registration_path, registration_raw)
                new_skill_name = f"{RELEASE_IDENTITY}-install-{registration_sha[:12]}.zip"
                new_skill_path = data / "Integrations" / "WorkBuddy" / _skill_archive_name(new_skill_name)
                new_skill_existed = new_skill_path.exists()
                workbuddy_skill = _build_workbuddy_skill_archive(
                    data,
                    root,
                    archive_name=new_skill_name,
                    reuse_if_identical=True,
                )
                if not new_skill_existed:
                    created_skill_paths.append(Path(workbuddy_skill["path"]))
                recovery_workbuddy_skill = None
                if previous_root is not None and previous_registration_sha is not None:
                    recovery_name = f"{RELEASE_IDENTITY}-recovery-{previous_registration_sha[:12]}.zip"
                    recovery_path = data / "Integrations" / "WorkBuddy" / _skill_archive_name(recovery_name)
                    recovery_existed = recovery_path.exists()
                    recovery_workbuddy_skill = _build_workbuddy_skill_archive(
                        data,
                        previous_root,
                        archive_name=recovery_name,
                        reuse_if_identical=True,
                    )
                    if not recovery_existed:
                        created_skill_paths.append(Path(recovery_workbuddy_skill["path"]))
                return {
                    "package_root": str(root),
                    "registration_sha256": registration_sha,
                    "active_pointer_sha256": None,
                    "registered": True,
                    "activated": False,
                    "previous_active_pointer_sha256": _sha256_bytes(previous_active_raw) if previous_active_raw else "MISSING",
                    "previous_registration_sha256": previous_registration_sha,
                    "previous_package_root": str(previous_root) if previous_root else None,
                    "workbuddy_skill": workbuddy_skill,
                    "recovery_workbuddy_skill": recovery_workbuddy_skill,
                }
            except Exception:
                # Roll back every write made by this transaction while the
                # same registry lock is still held, even with no old pointer.
                rollback_error: Exception | None = None
                try:
                    current_active_raw = _read_active_raw(paths)
                    if current_active_raw != previous_active_raw:
                        _restore_active_locked(paths, previous_active_raw, current_active_raw)
                    if registration_created and registration_path is not None and registration_raw is not None and registration_path.exists():
                        _verify_fixed_existing(
                            registration_path,
                            expected_parent=paths.objects,
                            label="Package Registration rollback object",
                        )
                        if registration_path.read_bytes() != registration_raw:
                            raise InstallerError("install_rollback_registration_drift")
                        registration_path.unlink()
                    for skill_path in created_skill_paths:
                        _assert_no_reparse_chain(skill_path.parent, boundary=data)
                        if skill_path.exists() or skill_path.is_symlink():
                            if not skill_path.is_file() or skill_path.is_symlink():
                                raise InstallerError("install_rollback_skill_drift")
                            skill_path.unlink()
                    if root_installed and root.exists():
                        _verify_tree_boundary(root)
                        shutil.rmtree(root)
                        if root.exists():
                            raise InstallerError("install_rollback_root_remained")
                except Exception as exc:
                    rollback_error = exc
                if rollback_error is not None:
                    raise InstallerError(f"install_rollback_failed:{rollback_error}") from rollback_error
                raise
    finally:
        if staging.exists():
            shutil.rmtree(staging, ignore_errors=True)


def _active_installation(data_root: Path) -> dict[str, Any]:
    from .package_registration import (
        _active_lock,
        _ensure_register_lock,
        _load_registration,
        _parse_active,
        _read_active_raw,
        _registry_paths,
    )

    paths = _registry_paths(data_root)
    _ensure_register_lock(paths)
    with _active_lock(paths):
        raw = _read_active_raw(paths)
        if raw is None:
            return {
                "pointer_sha256": "MISSING",
                "registration_sha256": None,
                "package_root": None,
            }
        pointer = _parse_active(raw)
        registration_sha = pointer["registration_sha256"]
        registration = _load_registration(paths, registration_sha)
        return {
            "pointer_sha256": _sha256_bytes(raw),
            "registration_sha256": registration_sha,
            "package_root": registration["package_root"],
        }


def _validate_release_archive(archive: Path) -> Path:
    from .package_registration import _parse_sidecar

    archive = Path(archive).resolve(strict=True)
    sidecar = archive.with_name(archive.name + ".sha256")
    if not archive.is_file() or archive.is_symlink() or not sidecar.is_file() or sidecar.is_symlink():
        raise InstallerError("release_archive_or_sidecar_invalid")
    try:
        digest = _parse_sidecar(sidecar.read_bytes(), archive_name=archive.name)
    except Exception as exc:
        raise InstallerError("release_sidecar_invalid") from exc
    if digest != _sha256(archive):
        raise InstallerError("release_archive_sidecar_mismatch")
    try:
        _release_members(archive)
    except (OSError, zipfile.BadZipFile) as exc:
        raise InstallerError("release_archive_invalid") from exc
    return archive


def _standard_install_paths(release_archive: Path) -> tuple[Path, Path]:
    archive = _validate_release_archive(release_archive)
    program_files = os.environ.get("ProgramFiles")
    local_app_data = os.environ.get("LOCALAPPDATA")
    if os.name != "nt" or not program_files or not local_app_data:
        raise InstallerError("windows_standard_location_unavailable")
    program_root = Path(program_files).resolve(strict=True)
    data_parent = Path(local_app_data).resolve(strict=True) / INSTALL_PRODUCT_DIRECTORY / "data"
    _assert_no_reparse_chain(program_root)
    _assert_no_reparse_chain(data_parent.parent)
    data_parent.mkdir(parents=True, exist_ok=True)
    data_root = data_parent / "production"
    data_root.mkdir(exist_ok=True)
    _assert_no_reparse_chain(data_root, boundary=data_parent.parent)
    if not data_root.is_dir() or data_root.is_symlink():
        raise InstallerError("data_root_invalid")
    package_root = (
        program_root
        / INSTALL_PRODUCT_DIRECTORY
        / "Packages"
        / f"{RELEASE_IDENTITY}-{_sha256(archive)[:12]}"
    )
    _assert_no_reparse_chain(package_root.parent)
    return data_root.resolve(strict=True), package_root.resolve()


def prepare_ui_install(
    *,
    data_root: os.PathLike[str] | str,
    release_archive: os.PathLike[str] | str,
    package_root: os.PathLike[str] | str,
) -> dict[str, Any]:
    """Publish and register a release while leaving the active pointer unchanged."""

    from .package_registration import register_package

    data = Path(data_root).resolve(strict=True)
    archive = _validate_release_archive(Path(release_archive))
    root = Path(package_root).resolve()
    if not root.exists():
        return install_release(
            data_root=data,
            release_archive=archive,
            package_root=root,
        )
    if not root.is_dir() or root.is_symlink():
        raise InstallerError("install_destination_or_sidecar_invalid")
    registration = register_package(
        data,
        archive,
        archive.with_name(archive.name + ".sha256"),
        root,
        root / "bootstrap" / "python" / "python.exe",
    )
    registration_sha = registration["registration_sha256"]
    previous = _active_installation(data)
    new_skill = _build_workbuddy_skill_archive(
        data,
        root,
        archive_name=f"{RELEASE_IDENTITY}-install-{registration_sha[:12]}.zip",
        reuse_if_identical=True,
    )
    recovery_skill = None
    previous_registration_sha = previous["registration_sha256"]
    previous_root = previous["package_root"]
    if previous_registration_sha is not None and previous_registration_sha != registration_sha:
        recovery_skill = _build_workbuddy_skill_archive(
            data,
            Path(previous_root),
            archive_name=f"{RELEASE_IDENTITY}-recovery-{previous_registration_sha[:12]}.zip",
            reuse_if_identical=True,
        )
    return {
        "package_root": str(root),
        "registration_sha256": registration_sha,
        "active_pointer_sha256": registration_sha if previous_registration_sha == registration_sha else None,
        "registered": True,
        "activated": previous_registration_sha == registration_sha,
        "previous_active_pointer_sha256": previous["pointer_sha256"],
        "previous_registration_sha256": previous_registration_sha,
        "previous_package_root": previous_root,
        "workbuddy_skill": new_skill,
        "recovery_workbuddy_skill": recovery_skill,
    }


def _rollback_prepared_activation(
    data_root: Path,
    registration_sha256: str,
    previous_registration_sha256: str | None,
    previous_active_pointer_sha256_or_missing: str,
) -> None:
    from .package_registration import _deactivate_package, _pointer_bytes, activate_package

    expected_new_pointer = _sha256_bytes(_pointer_bytes(registration_sha256))
    if previous_registration_sha256 is None:
        _deactivate_package(data_root, expected_new_pointer, registration_sha256)
    else:
        activate_package(data_root, expected_new_pointer, previous_registration_sha256)
    restored = _active_installation(data_root)
    if (
        restored["pointer_sha256"] != previous_active_pointer_sha256_or_missing
        or restored["registration_sha256"] != previous_registration_sha256
    ):
        raise InstallerError("activation_rollback_readback_failed")


def activate_prepared_release(
    *,
    data_root: os.PathLike[str] | str,
    package_root: os.PathLike[str] | str,
    registration_sha256: str,
    expected_active_pointer_sha256_or_missing: str,
    previous_registration_sha256: str | None,
) -> dict[str, Any]:
    """Activate only after UI import, then restore the prior pointer on post-check failure."""

    from .package_registration import _pointer_bytes, activate_package, locate_active_package

    data = Path(data_root).resolve(strict=True)
    root = Path(package_root).resolve(strict=True)
    try:
        activate_package(
            data,
            expected_active_pointer_sha256_or_missing,
            registration_sha256,
        )
    except Exception as exc:
        try:
            active = _active_installation(data)
            if active["registration_sha256"] == registration_sha256:
                _rollback_prepared_activation(
                    data,
                    registration_sha256,
                    previous_registration_sha256,
                    expected_active_pointer_sha256_or_missing,
                )
                raise InstallerError(
                    f"activation_failed:PACKAGE_ROLLBACK_COMPLETE:"
                    f"WORKBUDDY_SKILL_RESTORE_REQUIRED:{exc}"
                ) from exc
            if active["pointer_sha256"] != expected_active_pointer_sha256_or_missing:
                raise InstallerError(
                    f"activation_state_changed:WORKBUDDY_SKILL_RESTORE_REQUIRED:{exc}"
                ) from exc
        except InstallerError:
            raise
        except Exception as state_exc:
            raise InstallerError(
                f"activation_state_unknown:WORKBUDDY_SKILL_RESTORE_REQUIRED:{state_exc}"
            ) from state_exc
        raise InstallerError(f"activation_failed:WORKBUDDY_SKILL_RESTORE_REQUIRED:{exc}") from exc
    already_active = (
        previous_registration_sha256 == registration_sha256
        and expected_active_pointer_sha256_or_missing
        == _sha256_bytes(_pointer_bytes(registration_sha256))
    )
    try:
        located = locate_active_package(data)
        if (
            located["registration_sha256"] != registration_sha256
            or Path(located["package_root"]) != root
            or Path(located["guide"]["path"]) != root / "AGENT_GUIDE.md"
        ):
            raise InstallerError("locator_postcheck_identity_mismatch")
        return {
            "registration_sha256": registration_sha256,
            "package_root": str(root),
            "guide": located["guide"],
            "manifest": located["manifest"],
            "lock": located["lock"],
            "required_toolchain": located["required_toolchain"],
        }
    except Exception as exc:
        if already_active:
            raise InstallerError(f"locator_postcheck_failed_existing_active:{exc}") from exc
        try:
            _rollback_prepared_activation(
                data,
                registration_sha256,
                previous_registration_sha256,
                expected_active_pointer_sha256_or_missing,
            )
        except Exception as rollback_exc:
            raise InstallerError(
                f"postcheck_rollback_failed:WORKBUDDY_SKILL_RESTORE_REQUIRED:{rollback_exc}"
            ) from rollback_exc
        raise InstallerError(
            f"locator_postcheck_failed:PACKAGE_ROLLBACK_COMPLETE:"
            f"WORKBUDDY_SKILL_RESTORE_REQUIRED:{exc}"
        ) from exc


def _show_skill_archive(path: Path) -> None:
    if os.name != "nt":
        raise InstallerError("workbuddy_ui_handoff_requires_windows")
    subprocess.Popen(["explorer.exe", f"/select,{path}"])


def _run_ui_install(release_archive: Path) -> int:
    data_root, package_root = _standard_install_paths(release_archive)
    prepared = prepare_ui_install(
        data_root=data_root,
        release_archive=release_archive,
        package_root=package_root,
    )
    skill_path = Path(prepared["workbuddy_skill"]["path"])
    _show_skill_archive(skill_path)
    if prepared["recovery_workbuddy_skill"] is None:
        print("请在 WorkBuddy 的“专家·技能·连接器”中上传已选中的金钥匙 Skill。")
    else:
        print("请先在 WorkBuddy 中卸载同名旧 Skill，再上传已选中的新版 Skill。")
        print("旧版恢复包已保留；新版导入失败时请重新导入恢复包。")
    print("导入完成前请不要开始 WorkBuddy 任务。")
    if input("导入成功后输入 1 并回车；取消请输入 2：").strip() != "1":
        print("安装已暂停，新 Package 未激活，原有 Package 和用户数据保持不变。")
        return 2
    activate_prepared_release(
        data_root=data_root,
        package_root=package_root,
        registration_sha256=prepared["registration_sha256"],
        expected_active_pointer_sha256_or_missing=prepared["previous_active_pointer_sha256"],
        previous_registration_sha256=prepared["previous_registration_sha256"],
    )
    print("安装完成。重新打开 WorkBuddy 后即可使用“金钥匙智能体”。")
    return 0


def uninstall_release(
    *,
    data_root: os.PathLike[str] | str,
    package_root: os.PathLike[str] | str,
    registration_sha256: str,
) -> dict[str, Any]:
    """Remove one selected package with pointer/root rollback on failure."""

    from .package_registration import (
        _active_lock,
        _ensure_existing_registry,
        _load_registration,
        _parse_active,
        _read_active_raw,
        _registry_paths,
        _remove_active_locked,
        _restore_active_locked,
    )

    data = Path(data_root).resolve(strict=True)
    root = Path(package_root).resolve(strict=True)
    paths = _registry_paths(data)
    _ensure_existing_registry(paths)
    registration_sha256 = registration_sha256.lower()
    quarantine: Path | None = None
    try:
        with _active_lock(paths):
            previous_active_raw = _read_active_raw(paths)
            if previous_active_raw is None:
                raise InstallerError("uninstall_active_identity_mismatch")
            pointer = _parse_active(previous_active_raw)
            if pointer["registration_sha256"] != registration_sha256:
                raise InstallerError("uninstall_active_identity_mismatch")
            located = _load_registration(paths, registration_sha256)
            located_root = Path(located["package_root"]).resolve(strict=True)
            if located_root != root:
                raise InstallerError("uninstall_active_identity_mismatch")
            if root.is_symlink() or not root.is_dir():
                raise InstallerError("uninstall_package_root_invalid")
            _verify_tree_boundary(root)
            quarantine = root.with_name(f".{root.name}.uninstall-{uuid.uuid4().hex}")
            _assert_no_reparse_chain(quarantine.parent)
            if quarantine.exists() or quarantine.is_symlink():
                raise InstallerError("uninstall_quarantine_collision")
            os.replace(root, quarantine)
            try:
                _remove_active_locked(paths, previous_active_raw)
            except Exception:
                if quarantine.exists() and not root.exists():
                    os.replace(quarantine, root)
                raise
            try:
                _verify_tree_boundary(quarantine)
                shutil.rmtree(quarantine)
                if quarantine.exists():
                    raise InstallerError("uninstall_quarantine_remained")
            except Exception as exc:
                # Keep the old registration and exact pointer. The package is
                # restored before the pointer is made visible again.
                if quarantine.exists() and not root.exists():
                    os.replace(quarantine, root)
                current_active_raw = _read_active_raw(paths)
                if current_active_raw is None:
                    _restore_active_locked(paths, previous_active_raw, None)
                raise exc
            return {
                "package_root": str(root),
                "registration_sha256": registration_sha256,
                "active_pointer": "MISSING",
                "package_root_removed": not root.exists(),
                "data_root_preserved": data.is_dir(),
                "registration_history_retained": (paths.objects / f"{registration_sha256}.json").is_file(),
            }
    except Exception:
        if quarantine is not None and quarantine.exists() and not root.exists():
            try:
                os.replace(quarantine, root)
            except OSError:
                pass
        raise


def _main() -> int:
    parser = argparse.ArgumentParser(prog="golden-key-shell-installer")
    parser.add_argument("--version", action="version", version="1")
    commands = parser.add_subparsers(dest="command")
    ui_install = commands.add_parser("ui-install")
    ui_install.add_argument("--release-archive", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "ui-install":
        try:
            return _run_ui_install(args.release_archive)
        except Exception as exc:
            if "PACKAGE_ROLLBACK_COMPLETE" in str(exc):
                print("安装未完成。Package 已恢复；请在 WorkBuddy 中恢复旧 Skill，或移除刚导入的新 Skill。")
            elif "WORKBUDDY_SKILL_RESTORE_REQUIRED" in str(exc):
                print("安装未完成，Package 状态未能确认。请勿继续使用，并在 WorkBuddy 中恢复旧 Skill。")
            else:
                print("安装未完成，现有 Package 和用户数据未被删除。")
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
