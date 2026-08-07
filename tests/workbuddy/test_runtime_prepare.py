from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


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
    data_root = tmp_path / "data"

    result = _run_runtime_command(repo_root, data_root, "plan")

    assert result.returncode == 0, result.stderr
    report = json.loads(result.stdout)
    assert report["status"] == "needs_confirmation"
    assert report["target"] == str(data_root / "Runtime" / "Python")
    assert report["downloads_required"] is True
    assert report["system_python_modified"] is False
    assert report["provider_calls_attempted"] == 0
    assert report["network_calls_attempted"] == 0
    assert not data_root.exists()


def test_runtime_prepare_refuses_download_without_explicit_confirmation(
    tmp_path: Path,
) -> None:
    repo_root = tmp_path / "app"
    repo_root.mkdir()
    (repo_root / "requirements.txt").write_text("\n", encoding="utf-8")
    data_root = tmp_path / "data"

    result = _run_runtime_command(repo_root, data_root, "prepare")

    assert result.returncode == 1
    report = json.loads(result.stdout)
    assert report["status"] == "fail"
    assert "--confirm-download" in report["errors"][0]
    assert report["provider_calls_attempted"] == 0
    assert report["network_calls_attempted"] == 0
    assert not data_root.exists()


def test_runtime_prepare_creates_an_idempotent_data_scoped_python(
    tmp_path: Path,
) -> None:
    repo_root = tmp_path / "app"
    repo_root.mkdir()
    (repo_root / "requirements.txt").write_text("\n", encoding="utf-8")
    data_root = tmp_path / "data"

    first = _run_runtime_command(
        repo_root, data_root, "prepare", "--confirm-download"
    )
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
