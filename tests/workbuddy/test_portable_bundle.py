from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import os
import sys
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[2]


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _minimal_lock(tmp_path: Path, *, include_pipelines: bool = False) -> Path:
    source_paths = ["AGENT_GUIDE.md"]
    if include_pipelines:
        source_paths.extend(
            f"pipeline_defs/{name}.yaml"
            for name in (
                "golden-key-brand-company",
                "golden-key-lead-conversion",
                "golden-key-product-marketing",
                "golden-key-subject-ip",
            )
        )
    lock = {
        "schema_version": "1",
        "contract_id": "golden-key-workbuddy-callable-core-v1",
        "source_ref": "golden-key-v0.3.21",
        "source_commit": "757ea3822e5f2eef7f341389983119021e827c8d",
        "bundle_sha256": "fixture-bundle-digest",
        "authority": {
            "invocation_model": "direct_agent",
            "nested_agent_host_allowed": False,
        },
        "managed_scope": {
            "managed_paths": ["AGENT_GUIDE.md"],
            "managed_prefixes": ["pipeline_defs/"] if include_pipelines else [],
            "consumer_remove_paths": [
                "lib/agent_host_authority.py",
                "lib/model_driven_agent_host.py",
                "lib/openai_compatible_transport.py",
                "tests/contracts/test_agent_host_authority.py",
                "tests/contracts/test_model_driven_agent_host.py",
                "tests/contracts/test_openai_compatible_transport.py",
            ],
            "forbidden_paths": [],
        },
        "files": [
            {
                "path": f"workbuddy-core/{relative}",
                "source_path": relative,
                "sha256": _sha256(ROOT / relative),
                "size": (ROOT / relative).stat().st_size,
                "source_mode": "100644",
            }
            for relative in source_paths
        ],
    }
    lock_path = tmp_path / "GOLDEN_KEY_WORKBUDDY_CORE.lock.json"
    lock_path.write_text(json.dumps(lock), encoding="utf-8")
    return lock_path


def test_portable_bundle_contains_core_consumer_skills_and_first_build_label(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    staging = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path),
        output_root=tmp_path / "output",
    )

    manifest = json.loads(
        (staging / "BUNDLE-MANIFEST.json").read_text(encoding="utf-8")
    )
    assert manifest["distribution"] == {
        "channel": "pre-alpha",
        "format": "portable_zip",
        "package_version": "0.1.0-prealpha.1",
        "status": "first_installer_build_validation_only",
    }
    assert manifest["core"] == {
        "contract_id": "golden-key-workbuddy-callable-core-v1",
        "file_count": 1,
        "source_commit": "757ea3822e5f2eef7f341389983119021e827c8d",
        "tag": "golden-key-v0.3.21",
        "usage": "temporary_first_package_build_baseline_not_final_core",
    }
    assert (staging / "AGENT_GUIDE.md").is_file()
    assert (
        staging
        / "workbuddy-skill"
        / "golden-key-openmontage-onboarding"
        / "SKILL.md"
    ).is_file()
    assert (
        staging / "workbuddy-skill" / "golden-key-openmontage" / "SKILL.md"
    ).is_file()
    assert (staging / "install-workbuddy.ps1").is_file()
    assert (staging / "安装到WorkBuddy.cmd").is_file()
    assert (staging / "golden-key-workbuddy.ps1").is_file()
    assert not (staging / "setup.py").exists()
    assert (ROOT / "setup.py").is_file()
    assert not (staging / ".git").exists()
    assert not (staging / "projects").exists()


def test_portable_bundle_rejects_a_managed_core_hash_mismatch(tmp_path: Path) -> None:
    from scripts.workbuddy.build_portable_bundle import (
        PortableBundleContractError,
        build_portable_staging,
    )

    lock_path = _minimal_lock(tmp_path)
    lock = json.loads(lock_path.read_text(encoding="utf-8"))
    lock["files"][0]["sha256"] = "0" * 64
    lock_path.write_text(json.dumps(lock), encoding="utf-8")

    with pytest.raises(PortableBundleContractError, match="hash mismatch"):
        build_portable_staging(
            repo_root=ROOT,
            lock_path=lock_path,
            output_root=tmp_path / "output",
        )


def test_zip_bootstrap_registers_both_skills_and_launcher_runs_doctor(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    powershell = shutil.which("pwsh") or shutil.which("powershell")
    assert powershell is not None
    staging = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path, include_pipelines=True),
        output_root=tmp_path / "output",
    )
    install_root = tmp_path / "installed" / "app"
    data_root = tmp_path / "user-data"
    skill_root = tmp_path / "workbuddy-profile" / "skills"

    install_environment = os.environ.copy()
    install_environment["OPENMONTAGE_WORKBUDDY_NO_PAUSE"] = "1"
    install_environment["PATH"] = (
        str(Path(sys.executable).parent)
        + os.pathsep
        + install_environment.get("PATH", "")
    )
    installed = subprocess.run(
        [
            "cmd.exe",
            "/d",
            "/c",
            str(staging / "bootstrap" / "install-to-workbuddy.cmd"),
            "-InstallRoot",
            str(install_root),
            "-DataRoot",
            str(data_root),
            "-WorkBuddySkillsRoot",
            str(skill_root),
        ],
        cwd=tmp_path,
        env=install_environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert installed.returncode == 0, installed.stderr
    record = json.loads(
        (install_root / "WORKBUDDY-INSTALL.json").read_text(encoding="utf-8-sig")
    )
    assert record["mcp_enabled"] is False
    assert record["core"]["usage"] == (
        "temporary_first_package_build_baseline_not_final_core"
    )
    assert record["doctor_exit_code"] == 0
    assert record["doctor"]["status"] == "pass"
    assert record["doctor"]["provider_calls_attempted"] == 0
    assert record["doctor"]["network_calls_attempted"] == 0
    for directory in ("Caches", "Config", "Jobs", "Logs", "Models", "Projects", "Temp"):
        assert (data_root / directory).is_dir()

    for skill_name in (
        "golden-key-openmontage",
        "golden-key-openmontage-onboarding",
    ):
        runtime = json.loads(
            (skill_root / skill_name / "WORKBUDDY-RUNTIME.json").read_text(
                encoding="utf-8-sig"
            )
        )
        assert Path(runtime["install_root"]) == install_root
        assert Path(runtime["data_root"]) == data_root
        assert Path(runtime["launcher"]) == (
            install_root / "golden-key-workbuddy.ps1"
        )

    doctor_environment = os.environ.copy()
    doctor_environment["PATH"] = (
        str(Path(sys.executable).parent)
        + os.pathsep
        + doctor_environment.get("PATH", "")
    )
    doctor = subprocess.run(
        [
            powershell,
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(install_root / "golden-key-workbuddy.ps1"),
            "doctor",
            "--json",
        ],
        cwd=tmp_path,
        env=doctor_environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    assert doctor.returncode == 0, doctor.stderr
    report = json.loads(doctor.stdout)
    assert Path(report["repo_root"]) == install_root
    assert Path(report["storage"]["data_root"]) == data_root
    assert report["provider_calls_attempted"] == 0
