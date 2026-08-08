from __future__ import annotations

import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import time
import urllib.request
import uuid
import zipfile
from pathlib import Path, PurePosixPath
from typing import Any


MANAGED_RUNTIME_SCHEMA = "golden-key-workbuddy-managed-python-v1"
PRODUCTION_RUNTIME_SCHEMA = "golden-key-workbuddy-production-runtime-v1"
COMPONENT_MARKER_SCHEMA = "golden-key-workbuddy-runtime-component-v1"
PRODUCTION_RUNTIME_LOCK_SCHEMA = "golden-key-workbuddy-production-runtime-lock-v1"
PRODUCTION_PROFILE_ID = "complete_video_production"
RUNTIME_LOCK_NAME = "WORKBUDDY-PRODUCTION-RUNTIME.lock.json"


class ProductionRuntimeError(RuntimeError):
    pass


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _requirements_sha256(path: Path) -> str:
    return _sha256(path)


def _relative_interpreter() -> Path:
    if os.name == "nt":
        return Path("Scripts") / "python.exe"
    return Path("bin") / "python"


def _locations(repo_root: Path, data_root: Path) -> tuple[Path, Path, Path, Path]:
    repo_root = Path(repo_root).resolve()
    data_root = Path(data_root).resolve()
    requirements = repo_root / "requirements.txt"
    target = data_root / "Runtime" / "Python"
    record = target / "WORKBUDDY-MANAGED-PYTHON.json"
    return requirements, target, record, target / _relative_interpreter()


def _runtime_paths(data_root: Path) -> dict[str, Path]:
    runtime_root = Path(data_root).resolve() / "Runtime"
    return {
        "python": runtime_root / "Python",
        "ffmpeg": runtime_root / "FFmpeg",
        "node": runtime_root / "Node",
        "remotion": runtime_root / "Composition" / "Remotion",
        "hyperframes": runtime_root / "Composition" / "HyperFrames",
        "browser": runtime_root / "Browsers" / "HyperFrames",
    }


def _platform_id() -> str:
    machine = platform.machine().lower()
    if os.name == "nt" and machine in {"amd64", "x86_64"}:
        return "windows-x64"
    return f"{sys.platform}-{machine or 'unknown'}"


def _read_runtime_lock(repo_root: Path) -> tuple[dict[str, Any], Path]:
    path = Path(repo_root).resolve() / RUNTIME_LOCK_NAME
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ProductionRuntimeError(f"cannot read production runtime lock: {exc}") from exc
    if payload.get("schema_version") != PRODUCTION_RUNTIME_LOCK_SCHEMA:
        raise ProductionRuntimeError("production runtime lock schema is unsupported")
    profile = payload.get("profile") or {}
    if profile.get("id") != PRODUCTION_PROFILE_ID:
        raise ProductionRuntimeError("production runtime profile identity drifted")
    for field in ("estimated_download_bytes", "estimated_installed_bytes"):
        estimate = profile.get(field) or {}
        if (
            estimate.get("kind") != "planning_estimate"
            or not isinstance(estimate.get("minimum"), int)
            or not isinstance(estimate.get("maximum"), int)
            or estimate["minimum"] <= 0
            or estimate["maximum"] < estimate["minimum"]
        ):
            raise ProductionRuntimeError(f"production runtime lock has invalid {field}")
    browser = (payload.get("components") or {}).get("browser") or {}
    if not all(browser.get(field) for field in ("name", "version", "url", "sha256")):
        raise ProductionRuntimeError("production runtime lock is missing browser asset integrity metadata")
    return payload, path


def _verify_locked_file(repo_root: Path, component: dict[str, Any], key: str) -> Path:
    relative = str(component.get(key, ""))
    expected = str(component.get(f"{key}_sha256", "")).lower()
    if not relative or not expected:
        raise ProductionRuntimeError(f"runtime lock is missing {key} integrity metadata")
    path = (Path(repo_root).resolve() / relative).resolve()
    if not path.is_file() or _sha256(path) != expected:
        raise ProductionRuntimeError(f"locked runtime file mismatch: {relative}")
    return path


def _component_marker(target: Path) -> Path:
    return target / "WORKBUDDY-RUNTIME-COMPONENT.json"


def _read_component_marker(target: Path, name: str, lock_sha256: str) -> dict[str, Any] | None:
    marker_path = _component_marker(target)
    try:
        marker = json.loads(marker_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if (
        marker.get("schema_version") != COMPONENT_MARKER_SCHEMA
        or marker.get("component") != name
        or marker.get("runtime_lock_sha256") != lock_sha256
    ):
        return None
    return marker


def _write_component_marker(
    target: Path,
    name: str,
    lock_sha256: str,
    **metadata: Any,
) -> None:
    marker = {
        "schema_version": COMPONENT_MARKER_SCHEMA,
        "component": name,
        "runtime_lock_sha256": lock_sha256,
        **metadata,
    }
    _component_marker(target).write_text(
        json.dumps(marker, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _python_ready(repo_root: Path, data_root: Path) -> bool:
    requirements, _, record_path, interpreter = _locations(repo_root, data_root)
    if not (record_path.is_file() and interpreter.is_file() and requirements.is_file()):
        return False
    try:
        record = json.loads(record_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False
    return (
        record.get("schema_version") == MANAGED_RUNTIME_SCHEMA
        and record.get("requirements_sha256") == _requirements_sha256(requirements)
        and record.get("interpreter_relative") == _relative_interpreter().as_posix()
    )


def _production_record(data_root: Path) -> Path:
    return Path(data_root).resolve() / "Runtime" / "WORKBUDDY-PRODUCTION-RUNTIME.json"


def _production_component_readiness(
    repo_root: Path,
    data_root: Path,
    lock: dict[str, Any],
    lock_sha256: str,
) -> dict[str, bool]:
    paths = _runtime_paths(data_root)
    suffix = ".cmd" if os.name == "nt" else ""
    ffmpeg_exe = paths["ffmpeg"] / "bin" / ("ffmpeg.exe" if os.name == "nt" else "ffmpeg")
    ffprobe_exe = paths["ffmpeg"] / "bin" / ("ffprobe.exe" if os.name == "nt" else "ffprobe")
    node_exe = paths["node"] / ("node.exe" if os.name == "nt" else "bin/node")
    npm_exe = paths["node"] / ("npm.cmd" if os.name == "nt" else "bin/npm")
    npx_exe = paths["node"] / ("npx.cmd" if os.name == "nt" else "bin/npx")
    remotion_cli = paths["remotion"] / "node_modules" / ".bin" / f"remotion{suffix}"
    hyperframes_cli = paths["hyperframes"] / "node_modules" / ".bin" / f"hyperframes{suffix}"

    record: dict[str, Any] = {}
    try:
        record = json.loads(_production_record(data_root).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        pass
    browser_record = (record.get("components") or {}).get("browser", {})
    browser_path = Path(str(browser_record.get("executable", "")))
    browser_marker = _read_component_marker(paths["browser"], "browser", lock_sha256)
    marker_executable = Path(str((browser_marker or {}).get("executable", "")))
    browser_hash = _sha256(browser_path) if browser_path.is_file() else ""
    browser_ready = (
        record.get("schema_version") == PRODUCTION_RUNTIME_SCHEMA
        and record.get("runtime_lock_sha256") == lock_sha256
        and browser_path.is_file()
        and browser_path.resolve().is_relative_to(paths["browser"].resolve())
        and marker_executable.resolve() == browser_path.resolve()
        and browser_hash == str(browser_record.get("sha256", "")).lower()
        and browser_hash == str((browser_marker or {}).get("executable_sha256", "")).lower()
    )
    return {
        "python": _python_ready(repo_root, data_root),
        "ffmpeg": (
            _read_component_marker(paths["ffmpeg"], "ffmpeg", lock_sha256) is not None
            and ffmpeg_exe.is_file()
            and ffprobe_exe.is_file()
        ),
        "node": (
            _read_component_marker(paths["node"], "node", lock_sha256) is not None
            and node_exe.is_file()
            and npm_exe.is_file()
            and npx_exe.is_file()
        ),
        "remotion": (
            _read_component_marker(paths["remotion"], "remotion", lock_sha256) is not None
            and remotion_cli.is_file()
        ),
        "hyperframes": (
            _read_component_marker(paths["hyperframes"], "hyperframes", lock_sha256) is not None
            and hyperframes_cli.is_file()
            and browser_ready
        ),
    }


def build_runtime_plan(repo_root: Path, data_root: Path) -> dict[str, Any]:
    repo_root = Path(repo_root).resolve()
    data_root = Path(data_root).resolve()
    requirements, target, _, interpreter = _locations(repo_root, data_root)
    errors: list[str] = []
    if not requirements.is_file():
        errors.append(f"requirements file is missing: {requirements}")
    python_supported = sys.version_info >= (3, 10)
    if not python_supported:
        errors.append("Python 3.10 or newer is required to prepare the runtime")

    lock: dict[str, Any] = {}
    lock_path = repo_root / RUNTIME_LOCK_NAME
    lock_sha256 = ""
    try:
        lock, lock_path = _read_runtime_lock(repo_root)
        lock_sha256 = _sha256(lock_path)
        _verify_locked_file(repo_root, lock["components"]["remotion"], "package_json")
        _verify_locked_file(repo_root, lock["components"]["remotion"], "package_lock")
        _verify_locked_file(repo_root, lock["components"]["hyperframes"], "package_json")
        _verify_locked_file(repo_root, lock["components"]["hyperframes"], "package_lock")
    except (KeyError, ProductionRuntimeError) as exc:
        errors.append(str(exc))

    readiness = {name: False for name in ("python", "ffmpeg", "node", "remotion", "hyperframes")}
    if lock and lock_sha256:
        readiness = _production_component_readiness(repo_root, data_root, lock, lock_sha256)
    runtime_paths = _runtime_paths(data_root)
    component_lock = lock.get("components") or {}
    components = {
        "python": {
            "ready": readiness["python"],
            "required_for_complete_environment": True,
            "license": "PSF and dependency-specific",
            "license_notice_required": False,
        },
        "ffmpeg": {
            "ready": readiness["ffmpeg"],
            "required_for_complete_environment": True,
            "version": (component_lock.get("ffmpeg") or {}).get("version"),
            "license": (component_lock.get("ffmpeg") or {}).get("license", "GPL-3.0"),
            "license_notice_required": True,
        },
        "node": {
            "ready": readiness["node"],
            "required_for_complete_environment": True,
            "version": (component_lock.get("node") or {}).get("version"),
            "license": (component_lock.get("node") or {}).get("license", "Node.js license"),
            "license_notice_required": False,
        },
        "remotion": {
            "ready": readiness["remotion"],
            "required_for_complete_environment": True,
            "version": (component_lock.get("remotion") or {}).get("version"),
            "license": (component_lock.get("remotion") or {}).get("license", "Remotion License"),
            "license_notice_required": True,
            "license_url": (component_lock.get("remotion") or {}).get("license_url"),
        },
        "hyperframes": {
            "ready": readiness["hyperframes"],
            "required_for_complete_environment": True,
            "version": (component_lock.get("hyperframes") or {}).get("version"),
            "license": (component_lock.get("hyperframes") or {}).get("license", "Apache-2.0"),
            "license_notice_required": False,
            "managed_browser": {
                "name": (component_lock.get("browser") or {}).get("name"),
                "version": (component_lock.get("browser") or {}).get("version"),
                "source_sha256": (component_lock.get("browser") or {}).get("sha256"),
            },
        },
    }
    complete = all(component["ready"] for component in components.values())
    status = "fail" if errors else ("ready" if complete else "needs_confirmation")
    return {
        "status": status,
        "profile": {
            "id": PRODUCTION_PROFILE_ID,
            "display_name_zh": "完整视频制作环境",
            "default_recommendation": "prepare_complete_environment",
        },
        "platform": _platform_id(),
        "supported_platforms": lock.get("supported_platforms", ["windows-x64"]),
        "runtime_lock": str(lock_path),
        "runtime_lock_sha256": lock_sha256,
        "targets": {name: str(path) for name, path in runtime_paths.items()},
        "components": components,
        "target": str(target),
        "interpreter": str(interpreter),
        "requirements_file": str(requirements),
        "downloads_required": not complete,
        "single_user_confirmation": True,
        "estimated_download_bytes": (lock.get("profile") or {}).get(
            "estimated_download_bytes"
        ),
        "estimated_installed_bytes": (lock.get("profile") or {}).get(
            "estimated_installed_bytes"
        ),
        "confirmation_flag": "--confirm-download",
        "system_python_modified": False,
        "system_path_modified": False,
        "storage_policy": "managed_under_selected_data_root",
        "provider_calls_attempted": 0,
        "network_calls_attempted": 0,
        "license_notices": [
            "The managed FFmpeg Windows essentials build is GPLv3.",
            "Remotion licensing depends on team size and automation use; review the linked terms before preparation.",
        ],
        "errors": errors,
    }


def _owned_target_or_absent(target: Path, component: str, lock_sha256: str) -> None:
    if not target.exists():
        return
    marker = _read_component_marker(target, component, lock_sha256)
    if marker is None:
        raise ProductionRuntimeError(
            f"managed {component} target exists without matching ownership and was not overwritten: {target}"
        )
    shutil.rmtree(target)


def _download_verified(
    url: str,
    expected_sha256: str,
    cache_path: Path,
    *,
    total_timeout_seconds: int = 900,
) -> Path:
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    if cache_path.is_file() and _sha256(cache_path) == expected_sha256.lower():
        return cache_path
    temporary = cache_path.with_name(f".{cache_path.name}.{uuid.uuid4().hex}.download")
    try:
        request = urllib.request.Request(url, headers={"User-Agent": "GoldenKeyWorkBuddy/0.1"})
        started = time.monotonic()
        with urllib.request.urlopen(request, timeout=120) as response, temporary.open("wb") as output:
            while True:
                if time.monotonic() - started > total_timeout_seconds:
                    raise ProductionRuntimeError(
                        f"download exceeded {total_timeout_seconds} seconds: {url}"
                    )
                block = response.read(1024 * 1024)
                if not block:
                    break
                output.write(block)
        actual = _sha256(temporary)
        if actual != expected_sha256.lower():
            raise ProductionRuntimeError(
                f"download hash mismatch for {url}: expected {expected_sha256}, got {actual}"
            )
        os.replace(temporary, cache_path)
        return cache_path
    finally:
        if temporary.exists():
            temporary.unlink()


def _safe_extract_zip(archive_path: Path, destination: Path) -> None:
    with zipfile.ZipFile(archive_path) as archive:
        for entry in archive.infolist():
            relative = PurePosixPath(entry.filename)
            if relative.is_absolute() or ".." in relative.parts:
                raise ProductionRuntimeError(f"unsafe archive member: {entry.filename}")
        archive.extractall(destination)


def _prepare_archive_component(
    *,
    name: str,
    locked: dict[str, Any],
    target: Path,
    cache_root: Path,
    lock_sha256: str,
) -> bool:
    if _read_component_marker(target, name, lock_sha256) is not None:
        return False
    _owned_target_or_absent(target, name, lock_sha256)
    url = str(locked["url"])
    expected = str(locked["sha256"]).lower()
    archive_name = url.rsplit("/", 1)[-1]
    archive = _download_verified(url, expected, cache_root / archive_name)
    staging_root = target.parent / f".{target.name}-staging-{uuid.uuid4().hex}"
    try:
        staging_root.mkdir(parents=True)
        _safe_extract_zip(archive, staging_root)
        source = staging_root / str(locked["archive_root"])
        if not source.is_dir():
            raise ProductionRuntimeError(f"{name} archive root is missing: {source.name}")
        _write_component_marker(
            source,
            name,
            lock_sha256,
            source_url=url,
            source_sha256=expected,
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        os.replace(source, target)
    finally:
        if staging_root.exists():
            shutil.rmtree(staging_root, ignore_errors=True)
    return True


def _managed_environment(data_root: Path) -> tuple[dict[str, str], Path, Path, Path]:
    paths = _runtime_paths(data_root)
    node_dir = paths["node"]
    ffmpeg_bin = paths["ffmpeg"] / "bin"
    node_exe = node_dir / ("node.exe" if os.name == "nt" else "bin/node")
    npm_exe = node_dir / ("npm.cmd" if os.name == "nt" else "bin/npm")
    npx_exe = node_dir / ("npx.cmd" if os.name == "nt" else "bin/npx")
    environment = os.environ.copy()
    environment["PATH"] = os.pathsep.join(
        [str(node_dir), str(ffmpeg_bin), environment.get("PATH", "")]
    )
    cache_root = Path(data_root).resolve() / "Caches"
    environment["NPM_CONFIG_CACHE"] = str(cache_root / "npm")
    environment["npm_config_cache"] = str(cache_root / "npm")
    environment["PUPPETEER_SKIP_DOWNLOAD"] = "true"
    environment["HYPERFRAMES_EXTRACT_CACHE_DIR"] = str(cache_root / "HyperFrames" / "ExtractedFrames")
    environment["HYPERFRAMES_FONT_CACHE_DIR"] = str(cache_root / "HyperFrames" / "Fonts")
    return environment, node_exe, npm_exe, npx_exe


def _run_checked(
    command: list[str],
    *,
    cwd: Path,
    env: dict[str, str],
    label: str,
    timeout_seconds: int = 900,
) -> subprocess.CompletedProcess[str]:
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout_seconds,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise ProductionRuntimeError(
            f"{label} exceeded {timeout_seconds} seconds"
        ) from exc
    if result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise ProductionRuntimeError(f"{label} failed: {detail}")
    return result


def _prepare_npm_component(
    *,
    name: str,
    repo_root: Path,
    data_root: Path,
    component: dict[str, Any],
    target: Path,
    lock_sha256: str,
) -> bool:
    suffix = ".cmd" if os.name == "nt" else ""
    expected_cli = target / "node_modules" / ".bin" / f"{name}{suffix}"
    if _read_component_marker(target, name, lock_sha256) is not None and expected_cli.is_file():
        return False
    _owned_target_or_absent(target, name, lock_sha256)
    package_json = _verify_locked_file(repo_root, component, "package_json")
    package_lock = _verify_locked_file(repo_root, component, "package_lock")
    environment, _, npm_exe, _ = _managed_environment(data_root)
    if not npm_exe.is_file():
        raise ProductionRuntimeError("managed npm is missing after Node preparation")
    staging = target.parent / f".{target.name}-staging-{uuid.uuid4().hex}"
    try:
        staging.mkdir(parents=True)
        shutil.copy2(package_json, staging / "package.json")
        shutil.copy2(package_lock, staging / "package-lock.json")
        _run_checked(
            [str(npm_exe), "ci", "--no-audit", "--no-fund", "--no-input"],
            cwd=staging,
            env=environment,
            label=f"{name} dependency installation",
        )
        _write_component_marker(
            staging,
            name,
            lock_sha256,
            package_lock_sha256=_sha256(package_lock),
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        os.replace(staging, target)
    finally:
        if staging.exists():
            shutil.rmtree(staging, ignore_errors=True)
    return True


def _ensure_remotion_link(repo_root: Path, target: Path) -> None:
    link = Path(repo_root).resolve() / "remotion-composer" / "node_modules"
    desired = (target / "node_modules").resolve()
    if os.path.lexists(link):
        if link.resolve() == desired:
            return
        raise ProductionRuntimeError(
            f"Remotion node_modules already exists outside the managed runtime and was not overwritten: {link}"
        )
    link.parent.mkdir(parents=True, exist_ok=True)
    if os.name == "nt":
        result = subprocess.run(
            ["cmd.exe", "/d", "/c", "mklink", "/J", str(link), str(desired)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        if result.returncode != 0:
            raise ProductionRuntimeError(
                "cannot link the managed Remotion dependencies into the installed composer: "
                + (result.stderr or result.stdout).strip()
            )
    else:
        link.symlink_to(desired, target_is_directory=True)


def _prepare_browser(
    *,
    data_root: Path,
    component: dict[str, Any],
    target: Path,
    lock_sha256: str,
) -> tuple[Path, bool]:
    marker = _read_component_marker(target, "browser", lock_sha256)
    if marker:
        executable = Path(str(marker.get("executable", "")))
        if executable.is_file():
            return executable, False
    _owned_target_or_absent(target, "browser", lock_sha256)
    paths = _runtime_paths(data_root)
    hyperframes_root = paths["hyperframes"]
    environment, node_exe, _, _ = _managed_environment(data_root)
    browser_cli = hyperframes_root / "node_modules" / "@puppeteer" / "browsers" / "lib" / "main-cli.js"
    if not (node_exe.is_file() and browser_cli.is_file()):
        raise ProductionRuntimeError("HyperFrames browser installer is missing")
    version = str(component["version"])
    url = str(component["url"])
    archive_name = url.rsplit("/", 1)[-1]
    cached_archive = _download_verified(
        url,
        str(component["sha256"]).lower(),
        Path(data_root).resolve() / "Caches" / "Downloads" / archive_name,
    )
    staging = target.parent / f".{target.name}-staging-{uuid.uuid4().hex}"
    try:
        archive_root = staging / "chrome-headless-shell"
        archive_root.mkdir(parents=True)
        shutil.copy2(
            cached_archive,
            archive_root / f"{version}-{archive_name}",
        )
        result = _run_checked(
            [
                str(node_exe),
                str(browser_cli),
                "install",
                f"chrome-headless-shell@{version}",
                "--platform",
                "win64",
                "--path",
                str(staging),
                "--format",
                "{{path}}",
            ],
            cwd=hyperframes_root,
            env=environment,
            label="HyperFrames browser extraction",
            timeout_seconds=300,
        )
        candidates = [Path(line.strip()) for line in result.stdout.splitlines() if line.strip()]
        executable = next((path for path in reversed(candidates) if path.is_file()), None)
        if executable is None:
            executable = next(staging.rglob("chrome-headless-shell.exe"), None)
        if executable is None or not executable.is_file():
            raise ProductionRuntimeError("HyperFrames browser extraction returned no executable")
        relative_executable = executable.relative_to(staging)
        final_executable = target / relative_executable
        _write_component_marker(
            staging,
            "browser",
            lock_sha256,
            executable=str(final_executable),
            executable_sha256=_sha256(executable),
            source_url=url,
            source_sha256=str(component["sha256"]).lower(),
            version=version,
        )
        target.parent.mkdir(parents=True, exist_ok=True)
        os.replace(staging, target)
        return final_executable, True
    finally:
        if staging.exists():
            shutil.rmtree(staging, ignore_errors=True)


def _prepare_python(repo_root: Path, data_root: Path) -> bool:
    if _python_ready(repo_root, data_root):
        return False
    requirements, target, _, _ = _locations(repo_root, data_root)
    if target.exists():
        try:
            record = json.loads((target / "WORKBUDDY-MANAGED-PYTHON.json").read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            record = {}
        if record.get("schema_version") != MANAGED_RUNTIME_SCHEMA:
            raise ProductionRuntimeError(
                f"managed Python target exists without matching ownership and was not overwritten: {target}"
            )
        shutil.rmtree(target)
    runtime_root = target.parent
    runtime_root.mkdir(parents=True, exist_ok=True)
    staging = runtime_root / f".python-staging-{uuid.uuid4().hex}"
    cache_root = Path(data_root).resolve() / "Caches" / "pip"
    cache_root.mkdir(parents=True, exist_ok=True)
    environment = os.environ.copy()
    environment["PIP_CACHE_DIR"] = str(cache_root)
    try:
        _run_checked(
            [sys.executable, "-m", "venv", str(staging)],
            cwd=runtime_root,
            env=environment,
            label="managed Python environment creation",
        )
        staging_interpreter = staging / _relative_interpreter()
        _run_checked(
            [
                str(staging_interpreter),
                "-m",
                "pip",
                "install",
                "--disable-pip-version-check",
                "--no-input",
                "-r",
                str(requirements),
            ],
            cwd=runtime_root,
            env=environment,
            label="managed Python dependency installation",
        )
        record = {
            "schema_version": MANAGED_RUNTIME_SCHEMA,
            "requirements_sha256": _requirements_sha256(requirements),
            "interpreter_relative": _relative_interpreter().as_posix(),
            "source_python": sys.executable,
            "system_python_modified": False,
        }
        (staging / "WORKBUDDY-MANAGED-PYTHON.json").write_text(
            json.dumps(record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        os.replace(staging, target)
    finally:
        if staging.exists():
            shutil.rmtree(staging, ignore_errors=True)
    return True


def prepare_managed_runtime(
    repo_root: Path, data_root: Path, *, confirm_download: bool
) -> dict[str, Any]:
    repo_root = Path(repo_root).resolve()
    data_root = Path(data_root).resolve()
    plan = build_runtime_plan(repo_root, data_root)
    if plan["status"] == "fail":
        return plan
    if plan["status"] == "ready":
        try:
            _ensure_remotion_link(repo_root, _runtime_paths(data_root)["remotion"])
        except (OSError, ProductionRuntimeError, subprocess.SubprocessError) as exc:
            return {
                **plan,
                "status": "fail",
                "created": False,
                "reused": False,
                "errors": [str(exc)],
            }
        return {**plan, "status": "pass", "created": False, "reused": True}
    if not confirm_download:
        return {
            **plan,
            "status": "fail",
            "downloads_required": True,
            "errors": [
                "complete production environment preparation downloads local runtimes and packages; "
                "rerun with --confirm-download only after the user accepts the download, storage, "
                "and third-party license notices"
            ],
        }
    if plan["platform"] not in plan["supported_platforms"]:
        return {
            **plan,
            "status": "fail",
            "errors": [f"managed complete production environment is not available for {plan['platform']}"],
        }

    lock, lock_path = _read_runtime_lock(repo_root)
    lock_sha256 = _sha256(lock_path)
    paths = _runtime_paths(data_root)
    cache_root = data_root / "Caches" / "Downloads"
    created_components: list[str] = []
    network_calls = 0
    try:
        if _prepare_python(repo_root, data_root):
            created_components.append("python")
            network_calls += 1
        platform_lock = plan["platform"]
        if _prepare_archive_component(
            name="ffmpeg",
            locked=lock["components"]["ffmpeg"][platform_lock],
            target=paths["ffmpeg"],
            cache_root=cache_root,
            lock_sha256=lock_sha256,
        ):
            created_components.append("ffmpeg")
            network_calls += 1
        if _prepare_archive_component(
            name="node",
            locked=lock["components"]["node"][platform_lock],
            target=paths["node"],
            cache_root=cache_root,
            lock_sha256=lock_sha256,
        ):
            created_components.append("node")
            network_calls += 1
        if _prepare_npm_component(
            name="remotion",
            repo_root=repo_root,
            data_root=data_root,
            component=lock["components"]["remotion"],
            target=paths["remotion"],
            lock_sha256=lock_sha256,
        ):
            created_components.append("remotion")
            network_calls += 1
        _ensure_remotion_link(repo_root, paths["remotion"])
        if _prepare_npm_component(
            name="hyperframes",
            repo_root=repo_root,
            data_root=data_root,
            component=lock["components"]["hyperframes"],
            target=paths["hyperframes"],
            lock_sha256=lock_sha256,
        ):
            created_components.append("hyperframes")
            network_calls += 1
        browser, browser_created = _prepare_browser(
            data_root=data_root,
            component=lock["components"]["browser"],
            target=paths["browser"],
            lock_sha256=lock_sha256,
        )
        if browser_created:
            created_components.append("browser")
            network_calls += 1
        record = {
            "schema_version": PRODUCTION_RUNTIME_SCHEMA,
            "profile_id": PRODUCTION_PROFILE_ID,
            "runtime_lock_sha256": lock_sha256,
            "components": {
                "browser": {
                    "executable": str(browser),
                    "sha256": _sha256(browser),
                }
            },
            "system_python_modified": False,
            "system_path_modified": False,
        }
        _production_record(data_root).write_text(
            json.dumps(record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        final_plan = build_runtime_plan(repo_root, data_root)
        if final_plan["status"] != "ready":
            raise ProductionRuntimeError("production runtime preparation completed but readiness verification failed")
    except (OSError, KeyError, ProductionRuntimeError, subprocess.SubprocessError, zipfile.BadZipFile) as exc:
        return {
            **build_runtime_plan(repo_root, data_root),
            "status": "fail",
            "created_components": created_components,
            "network_calls_attempted": network_calls,
            "provider_calls_attempted": 0,
            "errors": [str(exc)],
        }

    return {
        **final_plan,
        "status": "pass",
        "downloads_required": False,
        "created": bool(created_components),
        "created_components": created_components,
        "reused": not created_components,
        "network_calls_attempted": network_calls,
        "provider_calls_attempted": 0,
        "errors": [],
    }
