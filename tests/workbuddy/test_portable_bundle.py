from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import os
import sys
import time
import zipfile
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


def _bootstrap_python_fixture(
    tmp_path: Path, *, python_payload: bytes = b"fixture-portable-python"
) -> tuple[Path, Path, Path]:
    archive = tmp_path / "python-3.13.15-embed-amd64.zip"
    with zipfile.ZipFile(archive, "w") as bundle:
        bundle.writestr("python.exe", python_payload)
        bundle.writestr("python313._pth", "python313.zip\n.\n")
        bundle.writestr("LICENSE.txt", "Python fixture licence\n")
    pip_wheel = tmp_path / "pip-26.1.2-py3-none-any.whl"
    pip_wheel.write_bytes(b"fixture-pip-wheel")
    runtime_lock = tmp_path / "WORKBUDDY-BOOTSTRAP-RUNTIME.lock.json"
    runtime_lock.write_text(
        json.dumps(
            {
                "schema_version": "golden-key-workbuddy-bootstrap-runtime-v1",
                "components": {
                    "python": {
                        "version": "3.13.15",
                        "archive": archive.name,
                        "url": "https://www.python.org/ftp/python/3.13.15/python-3.13.15-embed-amd64.zip",
                        "sha256": _sha256(archive),
                        "required_paths": [
                            "python.exe",
                            "python313._pth",
                            "LICENSE.txt",
                        ],
                    },
                    "pip": {
                        "version": "26.1.2",
                        "archive": pip_wheel.name,
                        "url": "https://files.pythonhosted.org/packages/fixture/pip-26.1.2-py3-none-any.whl",
                        "sha256": _sha256(pip_wheel),
                    },
                },
            }
        ),
        encoding="utf-8",
    )
    return archive, pip_wheel, runtime_lock


def test_portable_bundle_contains_hash_verified_private_python_runtime(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    archive, _, runtime_lock = _bootstrap_python_fixture(tmp_path)
    staging = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path),
        output_root=tmp_path / "output",
        bootstrap_python_archive=archive,
        bootstrap_runtime_lock_path=runtime_lock,
    )

    manifest = json.loads(
        (staging / "BUNDLE-MANIFEST.json").read_text(encoding="utf-8")
    )
    assert (staging / "bootstrap" / "python" / "python.exe").read_bytes() == (
        b"fixture-portable-python"
    )
    assert manifest["installation"]["runtime_roles"]["python"] == (
        "bundled_private_interpreter"
    )
    assert manifest["bootstrap_runtime"]["python"] == {
        "version": "3.13.15",
        "source": "python.org_windows_embeddable_x64",
        "archive_sha256": _sha256(archive),
        "system_python_required": False,
    }


def test_bundled_python_is_scoped_to_package_and_managed_site_packages(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    archive, _, runtime_lock = _bootstrap_python_fixture(tmp_path)
    staging = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path),
        output_root=tmp_path / "output",
        bootstrap_python_archive=archive,
        bootstrap_runtime_lock_path=runtime_lock,
    )

    path_config = (
        staging / "bootstrap" / "python" / "python313._pth"
    ).read_text(encoding="utf-8")
    sitecustomize = staging / "bootstrap" / "python" / "sitecustomize.py"
    assert path_config.splitlines() == [
        "python313.zip",
        ".",
        "../../..",
        "import site",
    ]
    assert sitecustomize.is_file()
    assert "OPENMONTAGE_WORKBUDDY_DATA_ROOT" in sitecustomize.read_text(
        encoding="utf-8"
    )


def test_portable_bundle_contains_hash_verified_pip_bootstrap(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    archive, pip_wheel, runtime_lock = _bootstrap_python_fixture(tmp_path)
    staging = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path),
        output_root=tmp_path / "output",
        bootstrap_python_archive=archive,
        bootstrap_pip_wheel=pip_wheel,
        bootstrap_runtime_lock_path=runtime_lock,
    )

    bundled_wheel = staging / "bootstrap" / "python" / pip_wheel.name
    manifest = json.loads(
        (staging / "BUNDLE-MANIFEST.json").read_text(encoding="utf-8")
    )
    assert bundled_wheel.read_bytes() == b"fixture-pip-wheel"
    path_config = (
        staging / "bootstrap" / "python" / "python313._pth"
    ).read_text(encoding="utf-8")
    assert pip_wheel.name in path_config.splitlines()
    path_config_entry = next(
        entry
        for entry in manifest["files"]
        if entry["path"] == "bootstrap/python/python313._pth"
    )
    assert path_config_entry["sha256"] == _sha256(
        staging / "bootstrap" / "python" / "python313._pth"
    )
    assert manifest["bootstrap_runtime"]["pip"] == {
        "version": "26.1.2",
        "archive_sha256": _sha256(pip_wheel),
        "source": "pypi_official_wheel",
    }


@pytest.mark.skipif(os.name != "nt", reason="Windows portable package contract")
def test_launcher_attempts_bundled_python_when_system_python_is_absent(
    tmp_path: Path,
) -> None:
    from scripts.workbuddy.build_portable_bundle import build_portable_staging

    powershell = shutil.which("pwsh") or shutil.which("powershell")
    assert powershell is not None
    command_processor = Path(os.environ["SystemRoot"]) / "System32" / "cmd.exe"
    archive, _, runtime_lock = _bootstrap_python_fixture(
        tmp_path, python_payload=command_processor.read_bytes()
    )
    staging = build_portable_staging(
        repo_root=ROOT,
        lock_path=_minimal_lock(tmp_path),
        output_root=tmp_path / "output",
        bootstrap_python_archive=archive,
        bootstrap_runtime_lock_path=runtime_lock,
    )
    empty_path = tmp_path / "empty-path"
    empty_path.mkdir()
    environment = os.environ.copy()
    environment["PATH"] = str(empty_path)
    environment["LOCALAPPDATA"] = str(tmp_path / "local-app-data")

    launched = subprocess.run(
        [
            powershell,
            "-NoProfile",
            "-File",
            str(staging / "golden-key-workbuddy.ps1"),
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

    assert "Python 3.10 or newer was not found" not in launched.stdout


def test_portable_builder_cli_fails_closed_without_bootstrap_python_asset(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    from scripts.workbuddy.build_portable_bundle import main

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "build_portable_bundle.py",
            "--repo-root",
            str(ROOT),
            "--lock",
            str(_minimal_lock(tmp_path)),
            "--output-root",
            str(tmp_path / "output"),
        ],
    )

    assert main() == 1
    report = json.loads(capsys.readouterr().out)
    assert "bootstrap Python archive is required" in report["error"]


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
    result = subprocess.run(
        command,
        cwd=staging.parent,
        env=environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )
    # Windows PowerShell can occasionally close one redirected stream without
    # returning an empty string after long, multi-suite runs.  Keep failure
    # assertions deterministic and preserve whichever captured stream carries
    # the actionable installer message.
    if result.stderr is None:
        result.stderr = result.stdout or ""
    return result


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
        # Windows executes the installed CMD from inside the program directory,
        # which is the self-uninstall case this helper must reproduce.  Other
        # platforms invoke the PowerShell contract directly and must keep the
        # caller outside InstallRoot so the directory can be moved normally.
        cwd=staging if os.name == "nt" else staging.parent,
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
    assert manifest["installation"]["production_environment"] == {
        "profile_id": "complete_video_production",
        "display_name_zh": "完整视频制作环境",
        "mode": "managed_after_single_user_confirmation",
        "target": "<data_root>/Runtime",
        "system_python_modified": False,
        "system_path_modified": False,
    }
    assert manifest["installation"]["runtime_roles"] == {
        "python": "required",
        "ffmpeg": "required",
        "node": "required",
        "remotion": "standard_agent_selected_composition_engine",
        "hyperframes": "standard_agent_selected_composition_engine",
    }
    assert (staging / "WORKBUDDY-PRODUCTION-RUNTIME.lock.json").is_file()
    assert (staging / "workbuddy-runtime" / "hyperframes" / "package.json").is_file()
    assert (
        staging / "workbuddy-runtime" / "hyperframes" / "package-lock.json"
    ).is_file()
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
    assert (staging / "configure-provider-keys.ps1").is_file()
    assert (staging / "配置API密钥.cmd").is_file()
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


def test_installed_launcher_ignores_shadow_package_in_callers_working_directory(
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

    caller_root = tmp_path / "caller"
    shadow_package = caller_root / "golden_key_openmontage_workbuddy"
    shadow_package.mkdir(parents=True)
    (shadow_package / "__main__.py").write_text(
        "raise SystemExit('CALLER SHADOW PACKAGE WAS IMPORTED')\n",
        encoding="utf-8",
    )
    powershell = shutil.which("pwsh") or shutil.which("powershell")
    assert powershell is not None
    result = subprocess.run(
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
        cwd=caller_root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode in (0, 1), result.stderr
    assert "CALLER SHADOW PACKAGE WAS IMPORTED" not in result.stderr
    report = json.loads(result.stdout)
    assert Path(report["repo_root"]) == install_root


@pytest.mark.skipif(os.name != "nt", reason="Windows DPAPI contract")
def test_installed_launcher_decrypts_dpapi_provider_key_without_returning_it(
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

    dummy_secret = "dpapi-test-secret-must-not-leak"
    powershell = shutil.which("pwsh") or shutil.which("powershell")
    assert powershell is not None
    encryption_environment = os.environ.copy()
    encryption_environment["GOLDEN_KEY_DPAPI_TEST_SECRET"] = dummy_secret
    encrypted = subprocess.run(
        [
            powershell,
            "-NoProfile",
            "-Command",
            (
                "$value=ConvertTo-SecureString $env:GOLDEN_KEY_DPAPI_TEST_SECRET -AsPlainText -Force; "
                "ConvertFrom-SecureString $value"
            ),
        ],
        env=encryption_environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=True,
    ).stdout.strip()
    store = data_root / "Config" / "golden-key-provider-credentials.json"
    store.parent.mkdir(parents=True, exist_ok=True)
    store.write_text(
        json.dumps(
            {
                "schema_version": "golden-key-provider-credentials-v1",
                "protection": "windows_dpapi_current_user",
                "credentials": {"DASHSCOPE_API_KEY": encrypted},
            }
        ),
        encoding="utf-8",
    )
    environment = os.environ.copy()
    environment.pop("DASHSCOPE_API_KEY", None)
    fake_bin = tmp_path / "fake-bin"
    fake_bin.mkdir()
    (fake_bin / "python.cmd").write_text(
        "@echo off\r\n"
        'if not "%PYTHONUTF8%"=="1" (\r\n'
        '  echo {"status":"fail","utf8_mode":false}\r\n'
        "  exit /b 8\r\n"
        ")\r\n"
        f'if "%DASHSCOPE_API_KEY%"=="{dummy_secret}" (\r\n'
        '  echo {"status":"pass","credential_injected":true,"utf8_mode":true}\r\n'
        "  exit /b 0\r\n"
        ")\r\n"
        'echo {"status":"fail","credential_injected":false}\r\n'
        "exit /b 7\r\n",
        encoding="ascii",
    )
    environment["PATH"] = str(fake_bin) + os.pathsep + environment.get("PATH", "")
    guided = subprocess.run(
        [
            powershell,
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(install_root / "golden-key-workbuddy.ps1"),
            "credential-injection-test",
        ],
        cwd=tmp_path,
        env=environment,
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )

    assert guided.returncode == 0, guided.stdout + guided.stderr
    assert dummy_secret not in guided.stdout
    report = json.loads(guided.stdout)
    assert report == {
        "status": "pass",
        "credential_injected": True,
        "utf8_mode": True,
    }


@pytest.mark.skipif(os.name != "nt", reason="Windows API-key wizard contract")
def test_api_key_wizard_survives_launcher_exit_and_allows_cancel(tmp_path: Path) -> None:
    package_root = tmp_path / "package"
    package_root.mkdir()
    data_root = tmp_path / "user-data"
    shutil.copy2(
        ROOT / "packaging" / "workbuddy" / "configure-provider-keys.ps1",
        package_root / "configure-provider-keys.ps1",
    )
    (package_root / "WORKBUDDY-INSTALL.json").write_text(
        json.dumps({"data_root": str(data_root)}), encoding="utf-8"
    )
    (package_root / "golden-key-workbuddy.ps1").write_text(
        "@{\n"
        "  status = 'pass'\n"
        "  credential_store = @{ path = '"
        + str(data_root / "Config" / "golden-key-provider-credentials.json").replace(
            "'", "''"
        )
        + "' }\n"
        "  capability_choices = @(@{ capability = 'tts'; label_zh = '中文配音'; "
        "description_zh = '把脚本合成为中文旁白'; recommended_providers = @('dashscope') })\n"
        "  providers = @(@{ provider = 'dashscope'; service = 'DashScope'; "
        "display_name_zh = '阿里云百炼'; summary_zh = '中文配音'; "
        "availability_notice_zh = '需要已开通服务'; access_path = 'direct_vendor_api'; "
        "capabilities = @('tts'); capability_labels_zh = @('中文配音'); "
        "credential_state = 'not_configured'; credential_options = @(@('DASHSCOPE_API_KEY')); "
        "credential_option_guidance = @(@{ access_name_zh = '阿里云百炼官方'; "
        "obtain_url = 'https://example.invalid/key'; documentation_url = 'https://example.invalid/docs'; "
        "billing_notice_zh = '可能产生费用'; fields = @(@{ env_var = 'DASHSCOPE_API_KEY'; label_zh = 'API Key' }) }); "
        "present_env_vars = @() })\n"
        "} | ConvertTo-Json -Depth 6\n"
        "exit 0\n",
        encoding="utf-8",
    )
    powershell = shutil.which("pwsh") or shutil.which("powershell")
    assert powershell is not None
    result = subprocess.run(
        [
            powershell,
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(package_root / "configure-provider-keys.ps1"),
        ],
        input="\n",
        capture_output=True,
        text=True,
        encoding="utf-8",
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert "Golden Key OpenMontage API" in result.stdout
    assert "这次需要哪类能力" in result.stdout
    assert "中文配音" in result.stdout
    assert not (data_root / "Config").exists()


def test_api_key_wizard_is_goal_first_and_explains_provider_setup() -> None:
    body = (
        ROOT / "packaging" / "workbuddy" / "configure-provider-keys.ps1"
    ).read_text(encoding="utf-8")

    assert "这次需要哪类能力" in body
    assert "推荐" in body
    assert "官方申请或管理入口" in body
    assert "费用提醒" in body
    assert "账户可用性" in body
    assert "credential_option_guidance" in body
    assert "capability_choices" in body


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
