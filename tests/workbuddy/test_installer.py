from __future__ import annotations

import os
import zipfile
from pathlib import Path
from types import SimpleNamespace

import pytest

from golden_key_openmontage_workbuddy import fixed_child, installer, package_registration
from golden_key_openmontage_workbuddy.installer import InstallerError


def _registry_with_pointer(data_root: Path, registration_sha256: str) -> bytes:
    paths = package_registration._registry_paths(data_root)
    package_registration._ensure_register_lock(paths)
    raw = package_registration._pointer_bytes(registration_sha256)
    package_registration._atomic_replace_active(paths.active, raw, None)
    return raw


def test_archive_listing_and_member_names_fail_closed(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    for member in ("../escape", "C:/escape", "folder:stream", "folder/name. ", "CON"):
        with pytest.raises(InstallerError):
            installer._safe_member(member)

    seven_zip = tmp_path / "7z.exe"
    archive = tmp_path / "ffmpeg.7z"
    seven_zip.write_bytes(b"7z")
    archive.write_bytes(b"archive")
    monkeypatch.setattr(installer, "_verified_seven_zip", lambda path: seven_zip)
    monkeypatch.setattr(installer, "_sha256", lambda path: installer.FFMPEG_ARCHIVE_SHA256)
    monkeypatch.setattr(
        installer.subprocess,
        "run",
        lambda *args, **kwargs: SimpleNamespace(
            stdout="----------\nPath = ffmpeg\nAttributes = L\n\n", stderr="", returncode=0
        ),
    )
    with pytest.raises(InstallerError):
        installer._seven_zip_listing(seven_zip, archive)


def test_install_failure_restores_previous_pointer_and_removes_new_root(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    old_root = tmp_path / "old-package"
    old_root.mkdir()
    old_sha = "a" * 64
    previous_raw = _registry_with_pointer(data_root, old_sha)
    archive = tmp_path / "release.zip"
    archive.write_bytes(b"release")
    archive.with_name(archive.name + ".sha256").write_text("x\n", encoding="utf-8")
    package_root = tmp_path / "new-package"

    def fake_extract(_archive: Path, destination: Path) -> None:
        (destination / "created.txt").write_bytes(b"new")

    monkeypatch.setattr(installer, "_extract_release", fake_extract)
    monkeypatch.setattr(
        package_registration,
        "_load_registration",
        lambda _paths, _sha: {"package_root": str(old_root)},
    )
    monkeypatch.setattr(
        package_registration,
        "_build_registration",
        lambda **_kwargs: (_ for _ in ()).throw(InstallerError("forced-registration-failure")),
    )
    with pytest.raises(InstallerError, match="forced-registration-failure"):
        installer.install_release(
            data_root=data_root,
            release_archive=archive,
            package_root=package_root,
        )
    active = data_root / "State" / "PackageRegistration" / "v1" / "active.json"
    assert active.read_bytes() == previous_raw
    assert not package_root.exists()
    assert not list(tmp_path.glob(".new-package.install-*"))


def test_uninstall_failure_restores_pointer_and_package_root(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    package_root = tmp_path / "package"
    package_root.mkdir()
    (package_root / "owned.txt").write_bytes(b"owned")
    registration_sha = "b" * 64
    previous_raw = _registry_with_pointer(data_root, registration_sha)
    monkeypatch.setattr(
        package_registration,
        "_load_registration",
        lambda _paths, _sha: {"package_root": str(package_root)},
    )
    monkeypatch.setattr(installer.shutil, "rmtree", lambda _path: (_ for _ in ()).throw(OSError("forced-delete-failure")))
    with pytest.raises(OSError, match="forced-delete-failure"):
        installer.uninstall_release(
            data_root=data_root,
            package_root=package_root,
            registration_sha256=registration_sha,
        )
    active = data_root / "State" / "PackageRegistration" / "v1" / "active.json"
    assert active.read_bytes() == previous_raw
    assert package_root.is_dir()
    assert (package_root / "owned.txt").read_bytes() == b"owned"


def test_handoff_rejects_precreated_reparse_and_skill_is_opaque(tmp_path: Path) -> None:
    result_root = tmp_path / "results"
    result_root.mkdir()
    outside = tmp_path / "outside"
    outside.mkdir()
    handoff = result_root / "fixed-child-handoff"
    try:
        os.symlink(outside, handoff, target_is_directory=True)
    except (OSError, NotImplementedError):
        pytest.skip("symlink creation is unavailable")
    request = {
        "session_id": "session-1",
        "request_id": "request-1",
        "message": "literal",
        "timeout_seconds": 5,
        "result_root": result_root,
        "provider_environment_names": [],
        "registration_sha256": "a" * 64,
        "openmontage_release": "0.3.25",
        "openmontage_commit": "0" * 40,
        "tool_definition_sha256": "b" * 64,
        "local_capability_evidence_identities": [],
    }
    with pytest.raises(fixed_child._InputError):
        fixed_child._write_handoff(request)
    skill = (Path(__file__).resolve().parents[2] / "workbuddy-skill/golden-key-openmontage/SKILL.md").read_text(encoding="utf-8")
    cli_source = (Path(__file__).resolve().parents[2] / "golden_key_openmontage_workbuddy/workbuddy_entry_cli.py").read_text(encoding="utf-8")
    assert "GOLDEN_KEY_WORKBUDDY_INTERPRETER_PATH" not in cli_source
    assert "GOLDEN_KEY_WORKBUDDY_INTERPRETER_PATH" not in skill
    assert "JSON request" not in skill
    assert "GOLDEN_KEY_WORKBUDDY_PACKAGE_TOOL_DEFINITION_SHA256" not in skill


def test_handoff_result_is_not_a_hardlink(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    result_root = tmp_path / "results"
    result_root.mkdir()
    request = {
        "session_id": "session-1",
        "request_id": "request-1",
        "message": "literal",
        "timeout_seconds": 5,
        "result_root": result_root,
        "provider_environment_names": [],
        "registration_sha256": "a" * 64,
        "openmontage_release": "0.3.25",
        "openmontage_commit": "0" * 40,
        "tool_definition_sha256": "b" * 64,
        "local_capability_evidence_identities": [],
    }

    monkeypatch.setattr(Path, "unlink", lambda self, missing_ok=False: None)
    relative, _, _ = fixed_child._write_handoff(request)

    assert os.stat(result_root / relative, follow_symlinks=False).st_nlink == 1


def test_installer_builds_stamped_workbuddy_skill_zip(tmp_path: Path) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    package_root = tmp_path / "installed package"
    skill_root = package_root / "shell-adapter/workbuddy-skill/golden-key-openmontage"
    (skill_root / "scripts").mkdir(parents=True)
    (package_root / "bootstrap/python").mkdir(parents=True)
    (skill_root / "SKILL.md").write_text(
        "GOLDEN_KEY_WORKBUDDY_SKILL_IDENTITY=golden-key-openmontage\n"
        'description: exact phrase "金钥匙智能体"\n',
        encoding="utf-8",
    )
    (skill_root / "scripts/run.ps1").write_text(
        "param([Parameter(ValueFromPipeline = $true)][string]$UserMessage)\n"
        "$packageRoot = <installer:package_root>\n"
        "$python = <installer:private_python>\n"
        "$UserMessage | & $python -I -m golden_key_openmontage_workbuddy.user_entry\n",
        encoding="utf-8",
    )
    (package_root / "bootstrap/python/python.exe").write_bytes(b"python")

    result = installer._build_workbuddy_skill_archive(data_root, package_root)

    archive = Path(result["path"])
    assert archive == data_root / "Integrations/WorkBuddy/golden-key-openmontage-0.3.25.zip"
    assert result["sha256"] == installer._sha256(archive)
    with zipfile.ZipFile(archive) as stream:
        assert stream.namelist() == ["SKILL.md", "scripts/run.ps1"]
        skill = stream.read("SKILL.md").decode("utf-8")
        payload = stream.read("scripts/run.ps1").decode("utf-8")
    assert 'exact phrase "金钥匙智能体"' in skill
    assert "<installer:" not in payload
    assert str(package_root) in payload
    assert str(package_root / "bootstrap/python/python.exe") in payload
    assert "ValueFromPipeline = $true" in payload
    assert "$UserMessage | & $python -I -m golden_key_openmontage_workbuddy.user_entry" in payload
    assert "System.Diagnostics.Process" not in payload


def test_workbuddy_skill_keeps_harness_flexible_with_cold_foreground_entry() -> None:
    skill = (Path(__file__).resolve().parents[2] / "workbuddy-skill/golden-key-openmontage/SKILL.md").read_text(encoding="utf-8")
    script = (Path(__file__).resolve().parents[2] / "workbuddy-skill/golden-key-openmontage/scripts/run.ps1").read_text(encoding="utf-8")

    assert "up to `300000`" in skill
    assert "decides its own reasoning, tools, questions, retries" in skill
    assert "does not prescribe an internal script" in skill
    assert "exactly once" not in skill
    assert "if ($LASTEXITCODE -ne 0)" in script
    assert "\n    exit $LASTEXITCODE\n" not in script
