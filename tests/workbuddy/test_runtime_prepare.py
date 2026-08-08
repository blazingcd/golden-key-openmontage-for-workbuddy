from __future__ import annotations

import json
import hashlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]


def _copy_runtime_contract(repo_root: Path) -> None:
    shutil.copy2(
        ROOT / "WORKBUDDY-PRODUCTION-RUNTIME.lock.json",
        repo_root / "WORKBUDDY-PRODUCTION-RUNTIME.lock.json",
    )
    shutil.copytree(
        ROOT / "workbuddy-runtime",
        repo_root / "workbuddy-runtime",
    )
    composer = repo_root / "remotion-composer"
    composer.mkdir()
    shutil.copy2(ROOT / "remotion-composer" / "package.json", composer / "package.json")
    shutil.copy2(
        ROOT / "remotion-composer" / "package-lock.json",
        composer / "package-lock.json",
    )


def _seed_managed_non_python_components(repo_root: Path, data_root: Path) -> None:
    lock_path = repo_root / "WORKBUDDY-PRODUCTION-RUNTIME.lock.json"
    lock_sha = __import__("hashlib").sha256(lock_path.read_bytes()).hexdigest()
    runtime = data_root / "Runtime"
    targets = {
        "ffmpeg": runtime / "FFmpeg",
        "node": runtime / "Node",
        "remotion": runtime / "Composition" / "Remotion",
        "hyperframes": runtime / "Composition" / "HyperFrames",
        "browser": runtime / "Browsers" / "HyperFrames",
    }
    for name, target in targets.items():
        target.mkdir(parents=True)
        (target / "WORKBUDDY-RUNTIME-COMPONENT.json").write_text(
            json.dumps(
                {
                    "schema_version": "golden-key-workbuddy-runtime-component-v1",
                    "component": name,
                    "runtime_lock_sha256": lock_sha,
                }
            ),
            encoding="utf-8",
        )
    for executable in (
        targets["ffmpeg"] / "bin" / "ffmpeg.exe",
        targets["ffmpeg"] / "bin" / "ffprobe.exe",
        targets["node"] / "node.exe",
        targets["node"] / "npm.cmd",
        targets["node"] / "npx.cmd",
        targets["remotion"] / "node_modules" / ".bin" / "remotion.cmd",
        targets["hyperframes"] / "node_modules" / ".bin" / "hyperframes.cmd",
        targets["browser"] / "chrome-headless-shell.exe",
    ):
        executable.parent.mkdir(parents=True, exist_ok=True)
        executable.write_text("fixture", encoding="utf-8")
    browser = targets["browser"] / "chrome-headless-shell.exe"
    browser_marker = json.loads(
        (targets["browser"] / "WORKBUDDY-RUNTIME-COMPONENT.json").read_text(
            encoding="utf-8"
        )
    )
    browser_marker["executable"] = str(browser)
    browser_marker["executable_sha256"] = hashlib.sha256(browser.read_bytes()).hexdigest()
    (targets["browser"] / "WORKBUDDY-RUNTIME-COMPONENT.json").write_text(
        json.dumps(browser_marker), encoding="utf-8"
    )
    (runtime / "WORKBUDDY-PRODUCTION-RUNTIME.json").write_text(
        json.dumps(
            {
                "schema_version": "golden-key-workbuddy-production-runtime-v1",
                "runtime_lock_sha256": lock_sha,
                "components": {
                    "browser": {
                        "executable": str(browser),
                        "sha256": hashlib.sha256(browser.read_bytes()).hexdigest(),
                    }
                },
            }
        ),
        encoding="utf-8",
    )


def _runtime_environment(repo_root: Path, data_root: Path) -> dict[str, str]:
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(repo_root)
    environment["OPENMONTAGE_WORKBUDDY_ROOT"] = str(repo_root)
    environment["OPENMONTAGE_WORKBUDDY_DATA_ROOT"] = str(data_root)
    return environment


def _run_runtime_command(
    repo_root: Path, data_root: Path, *arguments: str
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "golden_key_openmontage_workbuddy",
            "runtime",
            *arguments,
            "--repo-root",
            str(repo_root),
            "--data-root",
            str(data_root),
            "--json",
        ],
        cwd=repo_root,
        env=_runtime_environment(ROOT, data_root),
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )


def test_runtime_plan_requires_confirmation_without_changing_the_machine(
    tmp_path: Path,
) -> None:
    repo_root = tmp_path / "app"
    repo_root.mkdir()
    (repo_root / "requirements.txt").write_text("\n", encoding="utf-8")
    _copy_runtime_contract(repo_root)
    data_root = tmp_path / "data"

    result = _run_runtime_command(repo_root, data_root, "plan")

    assert result.returncode == 0, result.stderr
    report = json.loads(result.stdout)
    assert report["status"] == "needs_confirmation"
    assert report["profile"] == {
        "id": "complete_video_production",
        "display_name_zh": "完整视频制作环境",
        "default_recommendation": "prepare_complete_environment",
    }
    assert report["targets"] == {
        "python": str(data_root / "Runtime" / "Python"),
        "ffmpeg": str(data_root / "Runtime" / "FFmpeg"),
        "node": str(data_root / "Runtime" / "Node"),
        "remotion": str(data_root / "Runtime" / "Composition" / "Remotion"),
        "hyperframes": str(
            data_root / "Runtime" / "Composition" / "HyperFrames"
        ),
        "browser": str(data_root / "Runtime" / "Browsers" / "HyperFrames"),
    }
    assert list(report["components"]) == [
        "python",
        "ffmpeg",
        "node",
        "remotion",
        "hyperframes",
    ]
    assert all(
        component["required_for_complete_environment"] is True
        for component in report["components"].values()
    )
    assert report["components"]["remotion"]["license_notice_required"] is True
    assert report["components"]["hyperframes"]["license"] == "Apache-2.0"
    assert report["components"]["hyperframes"]["managed_browser"] == {
        "name": "chrome-headless-shell",
        "version": "152.0.7928.2",
        "source_sha256": "ec7d7cfbc9d97093c9269d6a26de78a3244a49f3112ff9616e2ccb5ac3afeb24",
    }
    assert report["downloads_required"] is True
    assert report["single_user_confirmation"] is True
    assert report["estimated_download_bytes"] == {
        "minimum": 500_000_000,
        "maximum": 1_200_000_000,
        "kind": "planning_estimate",
    }
    assert report["estimated_installed_bytes"] == {
        "minimum": 1_200_000_000,
        "maximum": 3_000_000_000,
        "kind": "planning_estimate",
    }
    assert report["system_python_modified"] is False
    assert report["system_path_modified"] is False
    assert report["provider_calls_attempted"] == 0
    assert report["network_calls_attempted"] == 0
    assert not data_root.exists()


def test_runtime_prepare_refuses_download_without_explicit_confirmation(
    tmp_path: Path,
) -> None:
    repo_root = tmp_path / "app"
    repo_root.mkdir()
    (repo_root / "requirements.txt").write_text("\n", encoding="utf-8")
    _copy_runtime_contract(repo_root)
    data_root = tmp_path / "data"

    result = _run_runtime_command(repo_root, data_root, "prepare")

    assert result.returncode == 1
    report = json.loads(result.stdout)
    assert report["status"] == "fail"
    assert "--confirm-download" in report["errors"][0]
    assert report["provider_calls_attempted"] == 0
    assert report["network_calls_attempted"] == 0
    assert not data_root.exists()


@pytest.mark.skipif(os.name != "nt", reason="managed browser profile is Windows-only")
def test_runtime_plan_rejects_a_tampered_managed_browser(tmp_path: Path) -> None:
    repo_root = tmp_path / "app"
    repo_root.mkdir()
    (repo_root / "requirements.txt").write_text("\n", encoding="utf-8")
    _copy_runtime_contract(repo_root)
    data_root = tmp_path / "data"
    _seed_managed_non_python_components(repo_root, data_root)

    before = json.loads(_run_runtime_command(repo_root, data_root, "plan").stdout)
    browser = data_root / "Runtime" / "Browsers" / "HyperFrames" / "chrome-headless-shell.exe"
    browser.write_text("tampered", encoding="utf-8")
    after = json.loads(_run_runtime_command(repo_root, data_root, "plan").stdout)

    assert before["components"]["hyperframes"]["ready"] is True
    assert after["components"]["hyperframes"]["ready"] is False


@pytest.mark.skipif(os.name != "nt", reason="managed production profile is Windows-only")
def test_runtime_prepare_creates_an_idempotent_data_scoped_python(
    tmp_path: Path,
) -> None:
    repo_root = tmp_path / "app"
    repo_root.mkdir()
    (repo_root / "requirements.txt").write_text("\n", encoding="utf-8")
    data_root = tmp_path / "data"
    _copy_runtime_contract(repo_root)
    _seed_managed_non_python_components(repo_root, data_root)

    first = _run_runtime_command(
        repo_root, data_root, "prepare", "--confirm-download"
    )
    remotion_link = repo_root / "remotion-composer" / "node_modules"
    assert remotion_link.exists()
    if os.name == "nt":
        subprocess.run(
            ["cmd.exe", "/d", "/c", "rmdir", str(remotion_link)],
            check=True,
            capture_output=True,
            text=True,
        )
    else:
        remotion_link.unlink()
    assert not remotion_link.exists()
    second = _run_runtime_command(
        repo_root, data_root, "prepare", "--confirm-download"
    )

    assert first.returncode == 0, first.stderr
    assert second.returncode == 0, second.stderr
    first_report = json.loads(first.stdout)
    second_report = json.loads(second.stdout)
    interpreter = Path(first_report["interpreter"])
    assert interpreter.is_file()
    assert first_report["status"] == "pass"
    assert first_report["created"] is True
    assert first_report["system_python_modified"] is False
    assert first_report["provider_calls_attempted"] == 0
    assert second_report["status"] == "pass"
    assert second_report["created"] is False
    assert second_report["reused"] is True
    assert second_report["interpreter"] == str(interpreter)
    assert remotion_link.resolve() == (
        data_root / "Runtime" / "Composition" / "Remotion" / "node_modules"
    ).resolve()


@pytest.mark.skipif(os.name != "nt", reason="managed production profile is Windows-only")
def test_registered_launcher_prefers_the_prepared_data_scoped_python(
    tmp_path: Path,
) -> None:
    powershell = shutil.which("pwsh") or shutil.which("powershell")
    assert powershell is not None
    app_root = tmp_path / "app"
    data_root = tmp_path / "data"
    shutil.copytree(ROOT / "golden_key_openmontage_workbuddy", app_root / "golden_key_openmontage_workbuddy")
    shutil.copytree(ROOT / "config", app_root / "config")
    (app_root / "pipeline_defs").mkdir()
    for name in (
        "golden-key-brand-company",
        "golden-key-lead-conversion",
        "golden-key-product-marketing",
        "golden-key-subject-ip",
    ):
        shutil.copy2(
            ROOT / "pipeline_defs" / f"{name}.yaml",
            app_root / "pipeline_defs" / f"{name}.yaml",
        )
    shutil.copy2(
        ROOT / "packaging" / "workbuddy" / "golden-key-workbuddy.ps1",
        app_root / "golden-key-workbuddy.ps1",
    )
    (app_root / "requirements.txt").write_text("\n", encoding="utf-8")
    _copy_runtime_contract(app_root)
    _seed_managed_non_python_components(app_root, data_root)
    (app_root / "WORKBUDDY-INSTALL.json").write_text(
        json.dumps({"data_root": str(data_root)}), encoding="utf-8"
    )
    environment = os.environ.copy()
    environment["PATH"] = (
        str(Path(sys.executable).parent)
        + os.pathsep
        + environment.get("PATH", "")
    )

    prepared = subprocess.run(
        [
            powershell,
            "-NoProfile",
            "-File",
            str(app_root / "golden-key-workbuddy.ps1"),
            "runtime",
            "prepare",
            "--confirm-download",
            "--json",
        ],
        cwd=tmp_path,
        env=environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    doctor = subprocess.run(
        [
            powershell,
            "-NoProfile",
            "-File",
            str(app_root / "golden-key-workbuddy.ps1"),
            "doctor",
            "--json",
        ],
        cwd=tmp_path,
        env=environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )

    assert prepared.returncode == 0, prepared.stderr
    report = json.loads(doctor.stdout)
    expected = data_root / "Runtime" / "Python"
    expected_interpreter = (
        expected / "Scripts" / "python.exe"
        if os.name == "nt"
        else expected / "bin" / "python"
    )
    assert Path(report["runtime"]["python"]["executable"]) == expected_interpreter
    assert report["provider_calls_attempted"] == 0


def test_registered_launcher_exposes_the_managed_composition_environment() -> None:
    launcher = (
        ROOT / "packaging" / "workbuddy" / "golden-key-workbuddy.ps1"
    ).read_text(encoding="utf-8")

    assert "Runtime\\FFmpeg\\bin" in launcher
    assert "Runtime\\Node" in launcher
    assert "Runtime\\Composition\\HyperFrames\\node_modules\\.bin" in launcher
    assert "WORKBUDDY-PRODUCTION-RUNTIME.json" in launcher
    assert "HYPERFRAMES_BROWSER_PATH" in launcher
    assert "REMOTION_BROWSER_EXECUTABLE" in launcher
    assert "HYPERFRAMES_EXTRACT_CACHE_DIR" in launcher
    assert "HYPERFRAMES_FONT_CACHE_DIR" in launcher
    assert "NPM_CONFIG_CACHE" in launcher
    assert "SetEnvironmentVariable('Path'" not in launcher


@pytest.mark.skipif(os.name == "nt", reason="unsupported-platform contract")
def test_runtime_prepare_fails_closed_on_an_unsupported_platform(
    tmp_path: Path,
) -> None:
    repo_root = tmp_path / "app"
    repo_root.mkdir()
    (repo_root / "requirements.txt").write_text("\n", encoding="utf-8")
    _copy_runtime_contract(repo_root)
    data_root = tmp_path / "data"

    result = _run_runtime_command(
        repo_root, data_root, "prepare", "--confirm-download"
    )

    assert result.returncode == 1
    report = json.loads(result.stdout)
    assert report["status"] == "fail"
    assert "not available" in report["errors"][0]
    assert report["provider_calls_attempted"] == 0
    assert not data_root.exists()
