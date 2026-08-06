from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_doctor_reports_locked_core_and_four_pipelines(tmp_path: Path) -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "golden_key_openmontage_workbuddy",
            "doctor",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(tmp_path / "data"),
            "--json",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode == 0, result.stderr
    report = json.loads(result.stdout)
    assert report["status"] == "pass"
    assert report["core"] == {
        "contract_id": "golden-key-workbuddy-callable-core-v1",
        "source_commit": "757ea3822e5f2eef7f341389983119021e827c8d",
        "tag": "golden-key-v0.3.21",
    }
    assert report["authority"] == {
        "invocation_model": "direct_agent",
        "nested_agent_host_allowed": False,
    }
    assert report["pipelines"]["available"] == [
        "golden-key-brand-company",
        "golden-key-lead-conversion",
        "golden-key-product-marketing",
        "golden-key-subject-ip",
    ]
    assert report["pipelines"]["expected_count"] == 4
    assert report["mcp"] == {
        "status": "optional",
        "role": "optional deterministic local stdio execution adapter",
        "canonical_fallback": "golden-key-workbuddy CLI",
        "real_workbuddy_comparison": "pass",
    }
    assert report["claims"]["offline_adapter_ready"] is False


def test_doctor_can_create_the_declared_data_directories(tmp_path: Path) -> None:
    data_root = tmp_path / "WorkBuddyData"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "golden_key_openmontage_workbuddy",
            "doctor",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--create-dirs",
            "--json",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode == 0, result.stderr
    report = json.loads(result.stdout)
    assert report["storage"]["created"] is True
    assert report["storage"]["directories"] == {
        "caches": str(data_root / "Caches"),
        "jobs": str(data_root / "Jobs"),
        "logs": str(data_root / "Logs"),
        "models": str(data_root / "Models"),
        "projects": str(data_root / "Projects"),
        "temp": str(data_root / "Temp"),
    }
    assert all(Path(path).is_dir() for path in report["storage"]["directories"].values())


def test_doctor_reports_local_runtime_without_contacting_providers(tmp_path: Path) -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "golden_key_openmontage_workbuddy",
            "doctor",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(tmp_path / "data"),
            "--json",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode == 0, result.stderr
    report = json.loads(result.stdout)
    assert report["runtime"]["python"]["supported"] is True
    assert report["runtime"]["python"]["minimum"] == "3.10"
    assert set(report["runtime"]) == {"ffmpeg", "node", "python"}
    assert report["provider_calls_attempted"] == 0


def test_distribution_has_a_unique_workbuddy_identity_and_console_entrypoint() -> None:
    name = subprocess.run(
        [sys.executable, "setup.py", "--name"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    ).stdout.strip()
    version = subprocess.run(
        [sys.executable, "setup.py", "--version"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    ).stdout.strip()

    assert name == "golden-key-openmontage-workbuddy"
    assert version == "0.1.0a0"
    setup_text = (ROOT / "setup.py").read_text(encoding="utf-8")
    assert "golden-key-workbuddy" in setup_text
    assert "golden-key-workbuddy-mcp" in setup_text


def test_gate_checks_the_public_w1_runtime_boundary(tmp_path: Path) -> None:
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "golden_key_openmontage_workbuddy",
            "gate",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(tmp_path / "data"),
            "--json",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode == 0, result.stderr
    report = json.loads(result.stdout)
    assert report["status"] == "pass"
    assert report["doctor_status"] == "pass"
    assert report["skill"]["status"] == "present"
    assert report["forbidden_paths"]["present"] == []
    assert report["mcp"]["active_config_present"] is False
    assert report["mcp"]["decision_status"] == "optional"
    assert report["provider_calls_attempted"] == 0


def test_gate_rejects_a_forbidden_nested_agent_import(tmp_path: Path) -> None:
    candidate = tmp_path / "candidate"
    (candidate / "config").mkdir(parents=True)
    shutil.copy2(
        ROOT / "config" / "openmontage.sync.json",
        candidate / "config" / "openmontage.sync.json",
    )
    (candidate / "pipeline_defs").mkdir()
    for name in (
        "golden-key-brand-company",
        "golden-key-lead-conversion",
        "golden-key-product-marketing",
        "golden-key-subject-ip",
    ):
        shutil.copy2(
            ROOT / "pipeline_defs" / f"{name}.yaml",
            candidate / "pipeline_defs" / f"{name}.yaml",
        )
    skill_dir = candidate / "workbuddy-skill" / "golden-key-openmontage"
    skill_dir.mkdir(parents=True)
    shutil.copy2(
        ROOT / "workbuddy-skill" / "golden-key-openmontage" / "SKILL.md",
        skill_dir / "SKILL.md",
    )
    runtime_dir = candidate / "golden_key_openmontage_workbuddy"
    runtime_dir.mkdir()
    (runtime_dir / "bad.py").write_text(
        "from lib import model_driven_agent_host\n", encoding="utf-8"
    )

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "golden_key_openmontage_workbuddy",
            "gate",
            "--repo-root",
            str(candidate),
            "--data-root",
            str(tmp_path / "data"),
            "--json",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode == 1
    report = json.loads(result.stdout)
    assert report["static_isolation"]["violations"] == [
        {
            "line": 1,
            "module": "lib.model_driven_agent_host",
            "path": "golden_key_openmontage_workbuddy/bad.py",
        }
    ]
