from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import uuid
import zipfile
from pathlib import Path
from types import ModuleType, SimpleNamespace

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


def test_ffmpeg_distribution_prunes_only_unused_player_and_docs(tmp_path: Path) -> None:
    root = tmp_path / "ffmpeg"
    retained = (
        root / "bin" / "ffmpeg.exe",
        root / "bin" / "ffprobe.exe",
        root / "LICENSE",
        root / "README.txt",
        root / "presets" / "libx264.ffpreset",
    )
    removed = (root / "bin" / "ffplay.exe", root / "doc" / "ffmpeg.html")
    for path in (*retained, *removed):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"x")

    installer._prune_ffmpeg_distribution(root)

    assert all(path.is_file() for path in retained)
    assert all(not path.exists() for path in removed)
    assert not (root / "doc").exists()


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


def _fake_package_registry(package_root: Path, summary_expression: str, statement: str = "") -> None:
    tools = package_root / "tools"
    tools.mkdir(parents=True)
    (tools / "__init__.py").write_text("", encoding="utf-8")
    statement_line = f"        {statement}\n" if statement else ""
    (tools / "tool_registry.py").write_text(
        "import os\n"
        "class Registry:\n"
        "    def provider_menu_summary(self):\n"
        + statement_line
        + f"        return {summary_expression}\n"
        "registry = Registry()\n",
        encoding="utf-8",
    )


def _handoff_request(result_root: Path, provider_environment_names: list[str] | None = None) -> dict[str, object]:
    return {
        "session_id": "session-1",
        "request_id": str(uuid.uuid4()),
        "message": "literal",
        "timeout_seconds": 5,
        "result_root": result_root,
        "provider_environment_names": provider_environment_names or [],
        "registration_sha256": "a" * 64,
        "openmontage_release": "0.3.25",
        "openmontage_commit": "0" * 40,
        "tool_definition_sha256": "b" * 64,
        "local_capability_evidence_identities": [],
    }


def test_handoff_relays_package_summary_without_changing_ownership(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    package_root = tmp_path / "package"
    result_root = tmp_path / "results"
    result_root.mkdir()
    summary = {
        "composition_runtimes": {"ffmpeg": True, "remotion": False, "hyperframes": False},
        "capabilities": [{"capability": "video_generation", "configured": 0, "total": 3}],
        "setup_offers": [{"env_vars": ["SEEDANCE_API_KEY"]}],
        "runtime_warnings": [],
    }
    _fake_package_registry(package_root, repr(summary))
    monkeypatch.chdir(package_root)
    monkeypatch.setenv("SEEDANCE_API_KEY", "secret-value-that-must-not-appear")

    relative, digest, size = fixed_child._write_handoff(
        _handoff_request(result_root, ["SEEDANCE_API_KEY"])
    )

    payload = (result_root / relative).read_bytes()
    handoff = json.loads(payload)
    assert payload == fixed_child._canonical(handoff)
    assert len(payload) == size
    assert installer._sha256(result_root / relative) == digest
    assert b"secret-value-that-must-not-appear" not in payload
    assert handoff["package_capability_summary"] == {
        "source": "registry.provider_menu_summary",
        "status": "REPORTED",
        "facts": summary,
        "error_code": None,
    }
    assert handoff["schema_version"] == "golden-key-workbuddy-fixed-child-handoff-v1"
    assert handoff["decision_owner"] == "WorkBuddy"
    assert handoff["production_decision_made"] is False
    assert handoff["provider_selected"] is False
    assert handoff["renderer_selected"] is False
    assert handoff["media_executed"] is False


def test_handoff_reports_unverified_when_package_summary_is_unavailable(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    package_root = tmp_path / "package"
    result_root = tmp_path / "results"
    package_root.mkdir()
    result_root.mkdir()
    monkeypatch.chdir(package_root)

    relative, _, _ = fixed_child._write_handoff(_handoff_request(result_root))

    handoff = json.loads((result_root / relative).read_bytes())
    assert handoff["package_capability_summary"] == {
        "source": "registry.provider_menu_summary",
        "status": "NOT_VERIFIED",
        "facts": None,
        "error_code": "UNAVAILABLE",
    }


@pytest.mark.parametrize(
    "environment_value,oversized",
    [
        ("secret-value-that-must-not-appear", False),
        ('quote"slash\\line\nsecret', False),
        ("", True),
    ],
)
def test_handoff_suppresses_unsafe_package_summary(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    environment_value: str,
    oversized: bool,
) -> None:
    package_root = tmp_path / "package"
    result_root = tmp_path / "results"
    result_root.mkdir()
    summary_expression = "{'oversized': 'x' * (512 * 1024)}" if oversized else repr({"leak": environment_value})
    _fake_package_registry(package_root, summary_expression)
    monkeypatch.chdir(package_root)
    names: list[str] = []
    if environment_value:
        monkeypatch.setenv("SEEDANCE_API_KEY", environment_value)
        names.append("SEEDANCE_API_KEY")

    relative, _, _ = fixed_child._write_handoff(_handoff_request(result_root, names))

    payload = (result_root / relative).read_bytes()
    if environment_value:
        assert environment_value.encode("utf-8") not in payload
    assert json.loads(payload)["package_capability_summary"] == {
        "source": "registry.provider_menu_summary",
        "status": "NOT_VERIFIED",
        "facts": None,
        "error_code": "REJECTED",
    }


def test_package_summary_restores_environment(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    package_root = tmp_path / "package"
    result_root = tmp_path / "results"
    result_root.mkdir()
    monkeypatch.delenv("PACKAGE_ONLY_TOKEN", raising=False)
    _fake_package_registry(
        package_root,
        "{'composition_runtimes': {'ffmpeg': True}}",
        "os.environ['PACKAGE_ONLY_TOKEN'] = 'temporary-secret-value'",
    )
    monkeypatch.chdir(package_root)

    fixed_child._write_handoff(_handoff_request(result_root))

    assert "PACKAGE_ONLY_TOKEN" not in os.environ


def test_package_summary_rejects_module_outside_package_root(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    package_root = tmp_path / "package"
    result_root = tmp_path / "results"
    result_root.mkdir()
    _fake_package_registry(package_root, "{}")
    outside = tmp_path / "outside_tool_registry.py"
    outside.write_text("", encoding="utf-8")
    tools_module = ModuleType("tools")
    tools_module.__path__ = [str(package_root / "tools")]
    registry_module = ModuleType("tools.tool_registry")
    registry_module.__file__ = str(outside)
    registry_module.registry = SimpleNamespace(provider_menu_summary=lambda: {})
    monkeypatch.setitem(sys.modules, "tools", tools_module)
    monkeypatch.setitem(sys.modules, "tools.tool_registry", registry_module)
    monkeypatch.chdir(package_root)

    with pytest.raises(fixed_child._InputError, match="package-summary-source"):
        fixed_child._write_handoff(_handoff_request(result_root))


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


def test_installer_can_stamp_repository_skill_for_current_package(tmp_path: Path) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    package_root = tmp_path / "installed package"
    (package_root / "bootstrap/python").mkdir(parents=True)
    (package_root / "bootstrap/python/python.exe").write_bytes(b"python")
    source_root = Path(__file__).resolve().parents[2] / "workbuddy-skill/golden-key-openmontage"

    result = installer._build_workbuddy_skill_archive(
        data_root,
        package_root,
        skill_source_root=source_root,
    )

    with zipfile.ZipFile(result["path"]) as stream:
        script = stream.read("scripts/run.ps1").decode("utf-8")
        skill = stream.read("SKILL.md").decode("utf-8")
    assert "<installer:" not in script
    assert "<installer:" not in skill
    assert str(data_root) in script
    receipt_path = data_root / "Results/golden-key-openmontage/latest-launcher-receipt.json"
    assert str(receipt_path) in script
    assert result["receipt_path"] == str(receipt_path)
    assert "'MISSING'" in script


def test_skill_candidate_archive_preserves_existing_baseline(tmp_path: Path) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    package_root = tmp_path / "installed package"
    skill_root = package_root / "shell-adapter/workbuddy-skill/golden-key-openmontage"
    (skill_root / "scripts").mkdir(parents=True)
    (package_root / "bootstrap/python").mkdir(parents=True)
    (skill_root / "SKILL.md").write_text("skill\n", encoding="utf-8")
    (skill_root / "scripts/run.ps1").write_text(
        "$packageRoot = <installer:package_root>\n"
        "$python = <installer:private_python>\n",
        encoding="utf-8",
    )
    (package_root / "bootstrap/python/python.exe").write_bytes(b"python")

    baseline = installer._build_workbuddy_skill_archive(data_root, package_root)
    baseline_path = Path(baseline["path"])
    baseline_bytes = baseline_path.read_bytes()
    candidate = installer._build_workbuddy_skill_archive(
        data_root,
        package_root,
        archive_name="golden-key-openmontage-0.3.25-delivery-v4.zip",
    )

    assert Path(candidate["path"]).name == "golden-key-openmontage-0.3.25-delivery-v4.zip"
    assert Path(candidate["path"]) != baseline_path
    assert baseline_path.read_bytes() == baseline_bytes
    with pytest.raises(InstallerError, match="archive_already_exists"):
        installer._build_workbuddy_skill_archive(
            data_root,
            package_root,
            archive_name="golden-key-openmontage-0.3.25-delivery-v4.zip",
        )


def test_skill_archive_name_is_a_single_zip_basename() -> None:
    for name in ("nested/candidate.zip", "candidate", "../candidate.zip", "C:/candidate.zip"):
        with pytest.raises(InstallerError, match="archive_name_invalid"):
            installer._skill_archive_name(name)


def test_skill_archive_rejects_non_active_package_root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    data_root = tmp_path / "data"
    active_path = data_root / "State/PackageRegistration/v1/active.json"
    active_path.parent.mkdir(parents=True)
    active_path.write_bytes(b"active")
    package_root = tmp_path / "stale package"
    active_root = tmp_path / "active package"
    package_root.mkdir()
    active_root.mkdir()
    monkeypatch.setattr(
        package_registration,
        "locate_active_package",
        lambda _data_root: {"package_root": str(active_root)},
    )
    source_root = Path(__file__).resolve().parents[2] / "workbuddy-skill/golden-key-openmontage"

    with pytest.raises(InstallerError, match="package_root_not_active"):
        installer._build_workbuddy_skill_archive(
            data_root,
            package_root,
            skill_source_root=source_root,
        )


def test_workbuddy_skill_wrapper_records_controlled_failure_with_real_pwsh() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    skill = (repo_root / "workbuddy-skill/golden-key-openmontage/SKILL.md").read_text(encoding="utf-8")
    template = (repo_root / "workbuddy-skill/golden-key-openmontage/scripts/run.ps1").read_text(encoding="utf-8")
    pwsh = shutil.which("pwsh")
    assert pwsh is not None

    task_root = Path("D:/BlazingCD/Temp") / f"workbuddy-v3-pwsh-{uuid.uuid4().hex}"
    results_root = task_root / "results"
    receipt_path = results_root / "latest-launcher-receipt.json"
    probe_message = "用户原文 secret message"
    missing_package = task_root / probe_message
    data_root = task_root / "data"
    script_path = task_root / "run.ps1"

    def ps_literal(path: Path) -> str:
        return "'" + str(path).replace("'", "''") + "'"

    task_root.mkdir(parents=True)
    data_root.mkdir()
    script = (
        template.replace("<installer:package_root>", ps_literal(missing_package))
        .replace("<installer:private_python>", ps_literal(task_root / "python.exe"))
        .replace("<installer:data_root>", ps_literal(data_root))
        .replace("<installer:active_pointer_sha256>", "MISSING")
        .replace("<installer:receipt_path>", ps_literal(receipt_path))
    )
    script_path.write_text(script, encoding="utf-8")
    try:
        result = subprocess.run(
            [pwsh, "-NoProfile", "-NonInteractive", "-File", str(script_path), "-UserMessage", probe_message],
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=False,
        )
        failure_path = results_root / "latest-launcher-failure.json"
        assert result.returncode != 0
        assert failure_path.is_file(), f"stdout={result.stdout!r} stderr={result.stderr!r}"
        payload = json.loads(failure_path.read_text(encoding="utf-8"))
        assert payload["schema_version"] == "golden-key-workbuddy-failure-diagnostic-v1"
        assert payload["exit_code"] == result.returncode
        assert payload["stage"] == "preflight"
        assert probe_message not in failure_path.read_text(encoding="utf-8")
        assert not receipt_path.exists()
        assert "Split-Path -Parent -LiteralPath" not in script
        assert "latest-launcher-failure.json" in skill
        assert "never replay" in skill
        assert "decides its own reasoning, tools, questions, retries" in skill
        assert "Do not delay user-visible delivery for optional workspace memory" in skill
        assert "routine result is not a new\nworkflow to persist" in skill
        assert script.count("golden_key_openmontage_workbuddy.user_entry") == 1
    finally:
        shutil.rmtree(task_root, ignore_errors=True)
