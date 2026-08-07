from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import os
import sys
import time
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


def _run_portable_installer(
    staging: Path,
    *,
    install_root: Path | None,
    data_root: Path,
    skill_root: Path,
) -> subprocess.CompletedProcess[str]:
    powershell = shutil.which("pwsh") or shutil.which("powershell")
    assert powershell is not None
    environment = os.environ.copy()
    environment["PATH"] = (
        str(Path(sys.executable).parent)
        + os.pathsep
        + environment.get("PATH", "")
    )
    command = [
        powershell,
        "-NoProfile",
        "-File",
        str(staging / "install-workbuddy.ps1"),
    ]
    if install_root is not None:
        command.extend(["-InstallRoot", str(install_root)])
    command.extend(
        [
            "-DataRoot",
            str(data_root),
            "-WorkBuddySkillsRoot",
            str(skill_root),
        ]
    )
    return subprocess.run(
        command,
        cwd=staging.parent,
        env=environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )


def _run_portable_uninstaller(
    staging: Path,
    *,
    install_root: Path,
    data_root: Path,
    skill_root: Path,
) -> subprocess.CompletedProcess[str]:
    powershell = shutil.which("pwsh") or shutil.which("powershell")
    assert powershell is not None
    environment = os.environ.copy()
    environment["OPENMONTAGE_WORKBUDDY_NO_PAUSE"] = "1"
    if os.name == "nt":
        command = [
            "cmd.exe",
            "/d",
            "/c",
            str(staging / "从WorkBuddy卸载.cmd"),
        ]
    else:
        command = [
            powershell,
            "-NoProfile",
            "-File",
            str(staging / "uninstall-workbuddy.ps1"),
        ]
    result = subprocess.run(
        command
        + [
            "-InstallRoot",
            str(install_root),
            "-DataRoot",
            str(data_root),
            "-WorkBuddySkillsRoot",
            str(skill_root),
        ],
        cwd=staging.parent,
        env=environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    if os.name == "nt" and staging.resolve() == install_root.resolve():
        for _ in range(50):
            if not install_root.exists():
                break
            time.sleep(0.1)
    return result


def _copy_package_with_version(
    source: Path,
    destination: Path,
    *,
    package_version: str,
) -> Path:
    shutil.copytree(source, destination)
    manifest_path = destination / "BUNDLE-MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["distribution"]["package_version"] = package_version
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    return destination


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
    assert manifest["installation"]["python_dependencies"] == {
        "mode": "managed_after_user_confirmation",
        "target": "<data_root>/Runtime/Python",
        "system_python_modified": False,
    }
    assert manifest["installation"]["runtime_roles"] == {
        "python": "required",
        "ffmpeg": "required_for_compose_and_media_tools",
        "node": "optional_for_remotion_or_hyperframes",
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
    assert (staging / "uninstall-workbuddy.ps1").is_file()
    assert (staging / "从WorkBuddy卸载.cmd").is_file()
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


def test_cover_extract_ignores_old_files_and_installs_only_manifest_entries(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    staging = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path, include_pipelines=True),
        output_root=tmp_path / "covered-extract",
    )
    stale_file = staging / "removed-in-new-version.txt"
    stale_nested = staging / "old-version-only" / "stale.py"
    stale_file.write_text("old", encoding="utf-8")
    stale_nested.parent.mkdir()
    stale_nested.write_text("old", encoding="utf-8")
    install_root = tmp_path / "installed" / "app"
    data_root = tmp_path / "user-data"
    skill_root = tmp_path / "workbuddy-profile" / "skills"

    result = _run_portable_installer(
        staging,
        install_root=install_root,
        data_root=data_root,
        skill_root=skill_root,
    )

    assert result.returncode == 0, result.stderr
    assert not (install_root / stale_file.name).exists()
    assert not (install_root / "old-version-only").exists()
    record = json.loads(
        (install_root / "WORKBUDDY-INSTALL.json").read_text(encoding="utf-8-sig")
    )
    assert record["source_package"] == {
        "copy_mode": "manifest_allowlist",
        "extra_files_ignored": [
            "old-version-only/stale.py",
            "removed-in-new-version.txt",
        ],
    }


def test_repeat_install_repairs_deleted_app_or_skill_and_preserves_user_data(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    first_extract = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path, include_pipelines=True),
        output_root=tmp_path / "first-extract",
    )
    second_extract = tmp_path / "second-extract" / first_extract.name
    shutil.copytree(first_extract, second_extract)
    install_root = tmp_path / "installed" / "app"
    data_root = tmp_path / "user-data"
    skill_root = tmp_path / "workbuddy-profile" / "skills"

    first = _run_portable_installer(
        first_extract,
        install_root=install_root,
        data_root=data_root,
        skill_root=skill_root,
    )
    assert first.returncode == 0, first.stderr
    sentinel = data_root / "Projects" / "keep-me.txt"
    sentinel.write_text("user-owned", encoding="utf-8")

    deleted_skill = skill_root / "golden-key-openmontage-onboarding"
    shutil.rmtree(deleted_skill)
    repeated = _run_portable_installer(
        first_extract,
        install_root=install_root,
        data_root=data_root,
        skill_root=skill_root,
    )
    assert repeated.returncode == 0, repeated.stderr
    assert (deleted_skill / "SKILL.md").is_file()
    assert sentinel.read_text(encoding="utf-8") == "user-owned"

    shutil.rmtree(install_root)
    repaired = _run_portable_installer(
        second_extract,
        install_root=install_root,
        data_root=data_root,
        skill_root=skill_root,
    )
    assert repaired.returncode == 0, repaired.stderr
    assert (install_root / "golden-key-workbuddy.ps1").is_file()
    assert sentinel.read_text(encoding="utf-8") == "user-owned"
    record = json.loads(
        (install_root / "WORKBUDDY-INSTALL.json").read_text(encoding="utf-8-sig")
    )
    assert record["operation"] == "repair"
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


def test_newer_package_upgrades_owned_install_and_preserves_user_data(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    first_package = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path, include_pipelines=True),
        output_root=tmp_path / "first-package",
    )
    newer_package = _copy_package_with_version(
        first_package,
        tmp_path / "newer-package",
        package_version="0.2.0-prealpha.1",
    )
    first_install = tmp_path / "installed" / "0.1.0-prealpha.1"
    newer_install = tmp_path / "installed" / "0.2.0-prealpha.1"
    data_root = tmp_path / "user-data"
    skill_root = tmp_path / "workbuddy-profile" / "skills"
    first = _run_portable_installer(
        first_package,
        install_root=first_install,
        data_root=data_root,
        skill_root=skill_root,
    )
    assert first.returncode == 0, first.stderr
    sentinel = data_root / "Projects" / "keep-on-upgrade.txt"
    sentinel.write_text("user-owned", encoding="utf-8")

    upgraded = _run_portable_installer(
        newer_package,
        install_root=newer_install,
        data_root=data_root,
        skill_root=skill_root,
    )

    assert upgraded.returncode == 0, upgraded.stderr
    assert not first_install.exists()
    assert (newer_install / "golden-key-workbuddy.ps1").is_file()
    assert sentinel.read_text(encoding="utf-8") == "user-owned"
    record = json.loads(
        (newer_install / "WORKBUDDY-INSTALL.json").read_text(encoding="utf-8-sig")
    )
    assert record["operation"] == "upgrade"
    assert record["previous_install"] == {
        "install_root": str(first_install),
        "package_version": "0.1.0-prealpha.1",
    }
    for skill_name in (
        "golden-key-openmontage",
        "golden-key-openmontage-onboarding",
    ):
        runtime = json.loads(
            (skill_root / skill_name / "WORKBUDDY-RUNTIME.json").read_text(
                encoding="utf-8-sig"
            )
        )
        assert runtime["package_version"] == "0.2.0-prealpha.1"
        assert Path(runtime["install_root"]) == newer_install


def test_default_install_root_follows_manifest_package_version(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    first_package = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path, include_pipelines=True),
        output_root=tmp_path / "first-package",
    )
    newer_package = _copy_package_with_version(
        first_package,
        tmp_path / "newer-package",
        package_version="0.2.0-prealpha.1",
    )
    local_app_data = tmp_path / "local-app-data"
    data_root = tmp_path / "user-data"
    skill_root = tmp_path / "workbuddy-profile" / "skills"
    expected_install = (
        local_app_data
        / "GoldenKeyOpenMontageForWorkBuddy"
        / "App"
        / "0.2.0-prealpha.1"
    )
    environment_value = os.environ.get("LOCALAPPDATA")
    os.environ["LOCALAPPDATA"] = str(local_app_data)
    try:
        installed = _run_portable_installer(
            newer_package,
            install_root=None,
            data_root=data_root,
            skill_root=skill_root,
        )
    finally:
        if environment_value is None:
            os.environ.pop("LOCALAPPDATA", None)
        else:
            os.environ["LOCALAPPDATA"] = environment_value

    assert installed.returncode == 0, installed.stderr
    assert (expected_install / "WORKBUDDY-INSTALL.json").is_file()


def test_failed_upgrade_restores_previous_program_and_skills(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    first_package = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path, include_pipelines=True),
        output_root=tmp_path / "first-package",
    )
    broken_package = _copy_package_with_version(
        first_package,
        tmp_path / "broken-newer-package",
        package_version="0.2.0-prealpha.1",
    )
    missing_pipeline = "pipeline_defs/golden-key-product-marketing.yaml"
    manifest_path = broken_package / "BUNDLE-MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["files"] = [
        entry for entry in manifest["files"] if entry["path"] != missing_pipeline
    ]
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
    (broken_package / missing_pipeline).unlink()
    first_install = tmp_path / "installed" / "0.1.0-prealpha.1"
    broken_install = tmp_path / "installed" / "0.2.0-prealpha.1"
    data_root = tmp_path / "user-data"
    skill_root = tmp_path / "workbuddy-profile" / "skills"
    first = _run_portable_installer(
        first_package,
        install_root=first_install,
        data_root=data_root,
        skill_root=skill_root,
    )
    assert first.returncode == 0, first.stderr
    sentinel = data_root / "Projects" / "keep-on-rollback.txt"
    sentinel.write_text("user-owned", encoding="utf-8")

    failed = _run_portable_installer(
        broken_package,
        install_root=broken_install,
        data_root=data_root,
        skill_root=skill_root,
    )

    assert failed.returncode != 0
    assert "previous installation was restored" in failed.stderr
    assert first_install.is_dir()
    assert not broken_install.exists()
    assert sentinel.read_text(encoding="utf-8") == "user-owned"
    for skill_name in (
        "golden-key-openmontage",
        "golden-key-openmontage-onboarding",
    ):
        runtime = json.loads(
            (skill_root / skill_name / "WORKBUDDY-RUNTIME.json").read_text(
                encoding="utf-8-sig"
            )
        )
        assert runtime["package_version"] == "0.1.0-prealpha.1"
        assert Path(runtime["install_root"]) == first_install


def test_upgrade_refuses_data_root_change_and_preserves_existing_install(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    first_package = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path, include_pipelines=True),
        output_root=tmp_path / "first-package",
    )
    newer_package = _copy_package_with_version(
        first_package,
        tmp_path / "newer-package",
        package_version="0.2.0-prealpha.1",
    )
    first_install = tmp_path / "installed" / "0.1.0-prealpha.1"
    newer_install = tmp_path / "installed" / "0.2.0-prealpha.1"
    existing_data = tmp_path / "existing-user-data"
    wrong_data = tmp_path / "wrong-user-data"
    skill_root = tmp_path / "workbuddy-profile" / "skills"
    first = _run_portable_installer(
        first_package,
        install_root=first_install,
        data_root=existing_data,
        skill_root=skill_root,
    )
    assert first.returncode == 0, first.stderr
    sentinel = existing_data / "Projects" / "keep-me.txt"
    sentinel.write_text("user-owned", encoding="utf-8")

    refused = _run_portable_installer(
        newer_package,
        install_root=newer_install,
        data_root=wrong_data,
        skill_root=skill_root,
    )

    assert refused.returncode != 0
    assert "DataRoot does not match" in refused.stderr
    assert first_install.is_dir()
    assert not newer_install.exists()
    assert not wrong_data.exists()
    assert sentinel.read_text(encoding="utf-8") == "user-owned"


def test_uninstall_removes_owned_program_and_skills_but_preserves_user_data(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    staging = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path, include_pipelines=True),
        output_root=tmp_path / "package",
    )
    install_root = tmp_path / "installed" / "app"
    data_root = tmp_path / "user-data"
    skill_root = tmp_path / "workbuddy-profile" / "skills"
    installed = _run_portable_installer(
        staging,
        install_root=install_root,
        data_root=data_root,
        skill_root=skill_root,
    )
    assert installed.returncode == 0, installed.stderr
    sentinel = data_root / "Projects" / "keep-after-uninstall.txt"
    sentinel.write_text("user-owned", encoding="utf-8")

    uninstalled = _run_portable_uninstaller(
        install_root,
        install_root=install_root,
        data_root=data_root,
        skill_root=skill_root,
    )

    assert uninstalled.returncode == 0, uninstalled.stderr
    report = json.loads(uninstalled.stdout)
    assert report["status"] == "uninstalled"
    assert report["user_data_preserved"] is True
    assert report["removed_skills"] == [
        "golden-key-openmontage",
        "golden-key-openmontage-onboarding",
    ]
    for _ in range(50):
        if not install_root.exists():
            break
        time.sleep(0.1)
    assert not install_root.exists()
    assert not (skill_root / "golden-key-openmontage").exists()
    assert not (skill_root / "golden-key-openmontage-onboarding").exists()
    assert sentinel.read_text(encoding="utf-8") == "user-owned"


def test_uninstall_preserves_skill_without_matching_ownership_marker(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    staging = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path, include_pipelines=True),
        output_root=tmp_path / "package",
    )
    install_root = tmp_path / "installed" / "app"
    data_root = tmp_path / "user-data"
    skill_root = tmp_path / "workbuddy-profile" / "skills"
    installed = _run_portable_installer(
        staging,
        install_root=install_root,
        data_root=data_root,
        skill_root=skill_root,
    )
    assert installed.returncode == 0, installed.stderr
    protected_skill = skill_root / "golden-key-openmontage-onboarding"
    runtime_path = protected_skill / "WORKBUDDY-RUNTIME.json"
    runtime = json.loads(runtime_path.read_text(encoding="utf-8-sig"))
    runtime["schema_version"] = "foreign-skill-v1"
    runtime_path.write_text(json.dumps(runtime), encoding="utf-8")
    protected_file = protected_skill / "KEEP.txt"
    protected_file.write_text("preserve", encoding="utf-8")

    uninstalled = _run_portable_uninstaller(
        install_root,
        install_root=install_root,
        data_root=data_root,
        skill_root=skill_root,
    )

    assert uninstalled.returncode == 0, uninstalled.stderr
    report = json.loads(uninstalled.stdout)
    assert report["removed_skills"] == ["golden-key-openmontage"]
    assert report["protected_skills"] == [
        "golden-key-openmontage-onboarding"
    ]
    assert protected_file.read_text(encoding="utf-8") == "preserve"
    assert not install_root.exists()


def test_foreign_skill_name_conflict_is_preserved_and_install_fails_closed(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    staging = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path, include_pipelines=True),
        output_root=tmp_path / "extract",
    )
    install_root = tmp_path / "installed" / "app"
    data_root = tmp_path / "user-data"
    skill_root = tmp_path / "workbuddy-profile" / "skills"
    foreign_skill = skill_root / "golden-key-openmontage"
    foreign_skill.mkdir(parents=True)
    foreign_file = foreign_skill / "FOREIGN.txt"
    foreign_file.write_text("do not replace", encoding="utf-8")

    result = _run_portable_installer(
        staging,
        install_root=install_root,
        data_root=data_root,
        skill_root=skill_root,
    )

    assert result.returncode != 0
    assert "foreign WorkBuddy Skill" in result.stderr
    assert foreign_file.read_text(encoding="utf-8") == "do not replace"
    assert not install_root.exists()


def test_older_package_cannot_downgrade_owned_install(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    staging = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path, include_pipelines=True),
        output_root=tmp_path / "extract",
    )
    install_root = tmp_path / "installed" / "app"
    data_root = tmp_path / "user-data"
    skill_root = tmp_path / "workbuddy-profile" / "skills"
    first = _run_portable_installer(
        staging,
        install_root=install_root,
        data_root=data_root,
        skill_root=skill_root,
    )
    assert first.returncode == 0, first.stderr
    record_path = install_root / "WORKBUDDY-INSTALL.json"
    record = json.loads(record_path.read_text(encoding="utf-8-sig"))
    record["package_version"] = "0.2.0-prealpha.1"
    record_path.write_text(json.dumps(record), encoding="utf-8")
    protected = install_root / "keep-existing-version.txt"
    protected.write_text("newer-install", encoding="utf-8")

    result = _run_portable_installer(
        staging,
        install_root=install_root,
        data_root=data_root,
        skill_root=skill_root,
    )

    assert result.returncode != 0
    assert "Package downgrade is not allowed" in result.stderr
    assert protected.read_text(encoding="utf-8") == "newer-install"


def test_deleted_app_does_not_allow_cross_version_skill_downgrade(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    staging = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path, include_pipelines=True),
        output_root=tmp_path / "extract",
    )
    install_root = tmp_path / "installed" / "app"
    data_root = tmp_path / "user-data"
    skill_root = tmp_path / "workbuddy-profile" / "skills"
    first = _run_portable_installer(
        staging,
        install_root=install_root,
        data_root=data_root,
        skill_root=skill_root,
    )
    assert first.returncode == 0, first.stderr
    runtime_path = (
        skill_root / "golden-key-openmontage" / "WORKBUDDY-RUNTIME.json"
    )
    runtime = json.loads(runtime_path.read_text(encoding="utf-8-sig"))
    runtime["package_version"] = "0.2.0-prealpha.1"
    runtime_path.write_text(json.dumps(runtime), encoding="utf-8")
    protected = skill_root / "golden-key-openmontage" / "keep-newer-skill.txt"
    protected.write_text("newer-skill", encoding="utf-8")
    shutil.rmtree(install_root)

    result = _run_portable_installer(
        staging,
        install_root=install_root,
        data_root=data_root,
        skill_root=skill_root,
    )

    assert result.returncode != 0
    assert "Package downgrade is not allowed" in result.stderr
    assert protected.read_text(encoding="utf-8") == "newer-skill"
    assert not install_root.exists()


@pytest.mark.parametrize(
    ("mutation", "expected_error"),
    (("missing", "Package file is missing"), ("tampered", "hash mismatch")),
)
def test_installer_rejects_missing_or_tampered_declared_files_before_writes(
    tmp_path: Path,
    mutation: str,
    expected_error: str,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    staging = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path, include_pipelines=True),
        output_root=tmp_path / "extract",
    )
    declared = staging / "AGENT_GUIDE.md"
    if mutation == "missing":
        declared.unlink()
    else:
        declared.write_text("tampered", encoding="utf-8")
    install_root = tmp_path / "installed" / "app"
    data_root = tmp_path / "user-data"
    skill_root = tmp_path / "workbuddy-profile" / "skills"

    result = _run_portable_installer(
        staging,
        install_root=install_root,
        data_root=data_root,
        skill_root=skill_root,
    )

    assert result.returncode != 0
    assert expected_error in result.stderr
    assert not install_root.exists()
    assert not data_root.exists()
    assert not skill_root.exists()


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
    if os.name == "nt":
        install_command = [
            "cmd.exe",
            "/d",
            "/c",
            str(staging / "bootstrap" / "install-to-workbuddy.cmd"),
        ]
    else:
        install_command = [
            powershell,
            "-NoProfile",
            "-File",
            str(staging / "install-to-workbuddy.ps1"),
        ]
    installed = subprocess.run(
        install_command
        + [
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
    assert record["doctor_exit_code"] in (0, 1)
    assert record["doctor"]["status"] in ("pass", "degraded")
    assert record["doctor"]["errors"] == []
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
    assert doctor.returncode in (0, 1), doctor.stderr
    report = json.loads(doctor.stdout)
    assert report["status"] in ("pass", "degraded")
    assert report["errors"] == []
    assert Path(report["repo_root"]) == install_root
    assert Path(report["storage"]["data_root"]) == data_root
    assert report["provider_calls_attempted"] == 0
