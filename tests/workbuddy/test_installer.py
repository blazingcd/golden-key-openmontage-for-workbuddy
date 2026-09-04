from __future__ import annotations

import json
import os
import sys
import uuid
import zipfile
from pathlib import Path
from types import ModuleType, SimpleNamespace

import pytest

from golden_key_openmontage_workbuddy import fixed_child, installer, package_registration, user_entry
from golden_key_openmontage_workbuddy.installer import InstallerError


def test_installer_binds_verified_m13_package_commit_and_tree() -> None:
    assert installer.OPENMONTAGE_COMMIT == "201675c0e550d417654b752f3945f229fb5ceeee"
    assert installer.OPENMONTAGE_TREE == "f5915fdda3448fed509ed8741563643493c1613f"
    assert "golden_key_openmontage_workbuddy/installer.py" in installer.SHELL_FILES


def _registry_with_pointer(data_root: Path, registration_sha256: str) -> bytes:
    paths = package_registration._registry_paths(data_root)
    package_registration._ensure_register_lock(paths)
    raw = package_registration._pointer_bytes(registration_sha256)
    package_registration._atomic_replace_active(paths.active, raw, None)
    return raw


def _write_release_archive(path: Path) -> None:
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("GoldenKeyOpenMontageForWorkBuddy/placeholder", b"release")
    path.with_name(path.name + ".sha256").write_text(
        f"{installer._sha256(path)} *{path.name}\n", encoding="utf-8"
    )


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
    _write_release_archive(archive)
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
    assert handoff["schema_version"] == "golden-key-workbuddy-fixed-child-handoff-v2"
    assert handoff["decision_owner"] == "WorkBuddy"
    assert handoff["production_decision_made"] is False
    assert handoff["provider_selected"] is False
    assert handoff["renderer_selected"] is False
    assert handoff["media_executed"] is False


def _configuration_action(definition: dict[str, str], **overrides: object) -> dict[str, object]:
    value: dict[str, object] = {
        "schema_version": "golden-key-workbuddy-configuration-action-v1",
        "action": "configure_provider",
        "capability": "video_generation",
        "provider": "seedance_ark",
        "package_release": definition["package_release"],
        "package_commit": definition["package_commit"],
        "package_definition_sha256": definition["definition_sha256"],
        "consent": "confirmed",
        "capability_definitions": None,
        "user_decisions": None,
    }
    value.update(overrides)
    return value


def test_private_configuration_action_binds_package_and_reuses_local_prepare(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    definition = {
        "package_release": "0.3.25",
        "package_commit": "1" * 40,
        "definition_sha256": "2" * 64,
    }
    local = _configuration_action(
        definition,
        action="prepare_optional_capabilities",
        capability="composition_runtime",
        provider=None,
        consent="inspect",
        capability_definitions=[{"capability": "remotion"}, {"capability": "hyperframes"}],
    )
    message = user_entry._canonical(local).decode("utf-8")
    assert user_entry._configuration_action(message, definition) == local
    captured: dict[str, object] = {}

    def fake_prepare(data_root, definitions, decisions):
        captured.update(data_root=data_root, definitions=definitions, decisions=decisions)
        return {"result": "CONSENT_REQUIRED", "capabilities": [], "plans": []}

    monkeypatch.setattr(user_entry.runtime_prepare, "prepare_optional_capabilities", fake_prepare)
    secret, result, evidence = user_entry._prepare_action(local, tmp_path)

    assert secret is None
    assert result == {"result": "CONSENT_REQUIRED", "capabilities": [], "plans": []}
    assert evidence == []
    assert captured == {
        "data_root": tmp_path,
        "definitions": local["capability_definitions"],
        "decisions": None,
    }


def test_provider_configuration_uses_native_credential_boundaries_without_chat_secret(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    definition = {
        "package_release": "0.3.25",
        "package_commit": "1" * 40,
        "definition_sha256": "2" * 64,
        "authority_owner": "managed_core",
        "definition_id": "fixture-definition",
        "definition_relative_path": "shell-adapter/package-tool-definition.json",
    }
    action = _configuration_action(definition)
    writes: list[str] = []
    monkeypatch.setattr(user_entry, "_prompt_api_key", lambda: "secret-canary")
    monkeypatch.setattr(user_entry, "_write_credential", writes.append)

    secret, result, evidence = user_entry._prepare_action(action, Path("D:/bounded-data"))

    assert secret == "secret-canary"
    assert result is None
    assert evidence == []
    assert writes == ["secret-canary"]
    assert "secret-canary" not in user_entry._canonical(action).decode("utf-8")
    data_root = tmp_path / "data"
    data_root.mkdir()
    monkeypatch.setattr(user_entry.bridge, "_runtime_environment_names", lambda: ())
    environment, payload = user_entry._request(
        tmp_path,
        data_root,
        definition,
        "unused",
        action=action,
        provider_secret=secret,
    )
    assert environment["ARK_API_KEY"] == "secret-canary"
    assert b"secret-canary" not in payload
    assert "secret-canary" not in user_entry.bridge._FIXED_ARGV_TEXT
    assert json.loads(payload)["executor_controls"]["provider_environment_names"] == [
        "ARK_API_KEY"
    ]


def test_package_declaration_is_validated_before_configuration_side_effects(
    tmp_path: Path,
) -> None:
    declaration = {
        "action": "provider_connection_test",
        "capability": "video_generation",
        "provider": "seedance_ark",
        "credential_environment_name": "ARK_API_KEY",
        "implementation": "tools.video.seedance_ark:SeedanceArkVideo.connection_test",
        "request_kind": "READ_ONLY_NON_MEDIA",
        "endpoint_contract": "GET https://ark.cn-beijing.volces.com/ping",
        "official_documentation": "https://www.volcengine.com/docs/82379/1339360?lang=zh",
        "success_proves": "ark_documented_ping_succeeded",
        "retry": "forbidden",
    }
    release = {
        "release_version": "0.3.25",
        "workbuddy_configuration_actions": [declaration],
        "workbuddy_optional_capability_definitions": [],
    }
    (tmp_path / "GOLDEN_KEY_OPENMONTAGE_RELEASE.json").write_text(
        json.dumps(release), encoding="utf-8"
    )
    definition = {
        "package_release": "0.3.25",
        "package_commit": "1" * 40,
        "definition_sha256": "2" * 64,
        "allowed_environment_names": ["ARK_API_KEY"],
        "secret_environment_names": ["ARK_API_KEY"],
    }
    provider = _configuration_action(definition)
    user_entry._validate_package_action(tmp_path, definition, provider)
    local = _configuration_action(
        definition,
        action="prepare_optional_capabilities",
        capability="composition_runtime",
        provider=None,
        consent="inspect",
        capability_definitions=[],
    )
    user_entry._validate_package_action(tmp_path, definition, local)

    local["capability_definitions"] = [{"capability": "invented"}]
    with pytest.raises(ValueError, match="configuration-package-definition"):
        user_entry._validate_package_action(tmp_path, definition, local)
    definition["allowed_environment_names"] = []
    with pytest.raises(ValueError, match="configuration-package-declaration"):
        user_entry._validate_package_action(tmp_path, definition, provider)


def test_configuration_handoff_keeps_ark_secret_out_and_dispatches_once(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    package_root = tmp_path / "package"
    result_root = tmp_path / "results"
    package_root.mkdir()
    result_root.mkdir()
    monkeypatch.chdir(package_root)
    monkeypatch.setenv("ARK_API_KEY", "secret-canary")
    request = _handoff_request(result_root, ["ARK_API_KEY"])
    definition = {
        "package_release": request["openmontage_release"],
        "package_commit": request["openmontage_commit"],
        "definition_sha256": request["tool_definition_sha256"],
    }
    action = _configuration_action(definition)
    request["message"] = fixed_child._canonical(
        {
            "schema_version": "golden-key-workbuddy-configuration-dispatch-v1",
            "request_id": request["request_id"],
            "action": action,
            "configuration_result": None,
        },
        newline=False,
    ).decode("utf-8")
    calls: list[dict[str, object]] = []

    def fake_connection(_request, selected):
        calls.append(selected)
        return {
            "status": "CHECK_SUCCEEDED",
            "error_code": None,
            "check": "ARK_DOCUMENTED_PING",
            "request_kind": "READ_ONLY_NON_MEDIA",
            "media_executed": False,
            "paid_task_created": False,
            "proves": ["ark_documented_ping_succeeded"],
            "does_not_prove": ["seedance_generation"],
        }

    monkeypatch.setattr(fixed_child, "_package_connection_test", fake_connection)
    relative, _, _ = fixed_child._write_handoff(request)

    payload = (result_root / relative).read_bytes()
    handoff = json.loads(payload)
    assert len(calls) == 1
    assert b"secret-canary" not in payload
    assert handoff["configuration_result"]["outcome"]["status"] == "CHECK_SUCCEEDED"
    assert handoff["configuration_result"]["outcome"]["media_executed"] is False


def test_package_declaration_owns_the_fixed_non_media_dispatch(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    package_root = tmp_path / "package"
    module_path = package_root / "tools" / "video" / "seedance_ark.py"
    module_path.parent.mkdir(parents=True)
    module_path.write_text("# package-owned test double\n", encoding="utf-8")
    declaration = {
        "action": "provider_connection_test",
        "capability": "video_generation",
        "provider": "seedance_ark",
        "credential_environment_name": "ARK_API_KEY",
        "implementation": "tools.video.seedance_ark:SeedanceArkVideo.connection_test",
        "request_kind": "READ_ONLY_NON_MEDIA",
        "endpoint_contract": "GET https://ark.cn-beijing.volces.com/ping",
        "official_documentation": "https://www.volcengine.com/docs/82379/1339360?lang=zh",
        "success_proves": "ark_documented_ping_succeeded",
        "retry": "forbidden",
    }
    (package_root / "GOLDEN_KEY_OPENMONTAGE_RELEASE.json").write_text(
        json.dumps({"workbuddy_configuration_actions": [declaration]}),
        encoding="utf-8",
    )
    monkeypatch.chdir(package_root)
    monkeypatch.setenv("ARK_API_KEY", "secret-canary")
    calls = 0

    class FakeSeedance:
        def connection_test(self):
            nonlocal calls
            calls += 1
            return {
                "status": "CHECK_SUCCEEDED",
                "error_code": None,
                "check": "ARK_DOCUMENTED_PING",
                "request_kind": "READ_ONLY_NON_MEDIA",
                "media_executed": False,
                "paid_task_created": False,
                "proves": ["ark_documented_ping_succeeded"],
                "does_not_prove": ["seedance_generation"],
            }

    monkeypatch.setattr(
        fixed_child.importlib,
        "import_module",
        lambda name: SimpleNamespace(__file__=str(module_path), SeedanceArkVideo=FakeSeedance),
    )
    request = _handoff_request(tmp_path / "results", ["ARK_API_KEY"])
    action = _configuration_action(
        {
            "package_release": request["openmontage_release"],
            "package_commit": request["openmontage_commit"],
            "definition_sha256": request["tool_definition_sha256"],
        }
    )

    result = fixed_child._package_connection_test(request, action)

    assert calls == 1
    assert result["status"] == "CHECK_SUCCEEDED"
    assert "secret-canary" not in repr(result)


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


def test_installer_builds_guidance_only_workbuddy_skill_zip(tmp_path: Path) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    package_root = tmp_path / "installed package"
    skill_root = package_root / "shell-adapter/workbuddy-skill/golden-key-openmontage"
    skill_root.mkdir(parents=True)
    (package_root / "AGENT_GUIDE.md").write_text("guide\n", encoding="utf-8")
    (skill_root / "SKILL.md").write_text(
        'description: exact phrase "金钥匙智能体"\n'
        f"data={installer.WORKBUDDY_DATA_ROOT_PLACEHOLDER}\n"
        f"guide={installer.WORKBUDDY_GUIDE_PATH_PLACEHOLDER}\n"
        f"package={installer.WORKBUDDY_PACKAGE_ROOT_PLACEHOLDER}\n"
        "WorkBuddy performs the live check.\n",
        encoding="utf-8",
    )

    result = installer._build_workbuddy_skill_archive(data_root, package_root)

    archive = Path(result["path"])
    assert archive == data_root / "Integrations/WorkBuddy/golden-key-openmontage-0.3.25.zip"
    assert result["sha256"] == installer._sha256(archive)
    with zipfile.ZipFile(archive) as stream:
        assert stream.namelist() == ["SKILL.md"]
        skill = stream.read("SKILL.md").decode("utf-8")
    assert 'exact phrase "金钥匙智能体"' in skill
    assert "WorkBuddy performs the live check" in skill
    assert f"package={package_root.resolve()}" in skill
    assert f"data={data_root.resolve()}" in skill
    assert f"guide={package_root.resolve() / 'AGENT_GUIDE.md'}" in skill
    assert installer.WORKBUDDY_DATA_ROOT_PLACEHOLDER not in skill
    assert installer.WORKBUDDY_GUIDE_PATH_PLACEHOLDER not in skill
    assert installer.WORKBUDDY_PACKAGE_ROOT_PLACEHOLDER not in skill


def test_package_assembly_accepts_guidance_only_skill(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    files = {
        "shell-adapter/golden_key_openmontage_workbuddy/fixed_child.py": b"child",
        "shell-adapter/golden_key_openmontage_workbuddy/workbuddy_entry_cli.py": b"entry",
        "shell-adapter/golden_key_openmontage_workbuddy/user_entry.py": b"user",
        "bootstrap/python/python.exe": b"python",
    }
    for relative, payload in files.items():
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
    skill = tmp_path / "shell-adapter/workbuddy-skill/golden-key-openmontage/SKILL.md"
    skill.parent.mkdir(parents=True)
    source = "---\nname: golden-key-openmontage\n---\nWorkBuddy executes live.\n"
    skill.write_text(source, encoding="utf-8")
    monkeypatch.setattr(installer, "_bridge_schema_hashes", lambda _root: ("1" * 64, "2" * 64))

    result = installer._definition_and_skill(tmp_path)

    assert skill.read_text(encoding="utf-8") == source
    assert result["skill_sha256"] == installer._sha256(skill)


def test_installer_can_build_repository_guidance_skill(tmp_path: Path) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    package_root = tmp_path / "installed package"
    package_root.mkdir()
    (package_root / "AGENT_GUIDE.md").write_text("guide\n", encoding="utf-8")
    source_root = Path(__file__).resolve().parents[2] / "workbuddy-skill/golden-key-openmontage"

    result = installer._build_workbuddy_skill_archive(
        data_root,
        package_root,
        skill_source_root=source_root,
    )

    with zipfile.ZipFile(result["path"]) as stream:
        assert stream.namelist() == ["SKILL.md"]
        skill = stream.read("SKILL.md").decode("utf-8")
    source = (source_root / "SKILL.md").read_text(encoding="utf-8")
    expected = source.replace(
        installer.WORKBUDDY_DATA_ROOT_PLACEHOLDER, str(data_root.resolve())
    ).replace(
        installer.WORKBUDDY_GUIDE_PATH_PLACEHOLDER,
        str(package_root.resolve() / "AGENT_GUIDE.md"),
    ).replace(installer.WORKBUDDY_PACKAGE_ROOT_PLACEHOLDER, str(package_root.resolve()))
    assert skill == expected
    assert "<installer:" not in skill
    assert "registry.npmmirror.com" in skill
    assert str(data_root.resolve()) in skill
    assert str(package_root.resolve()) in skill
    assert installer.WORKBUDDY_DATA_ROOT_PLACEHOLDER not in skill
    assert installer.WORKBUDDY_GUIDE_PATH_PLACEHOLDER not in skill
    assert installer.WORKBUDDY_PACKAGE_ROOT_PLACEHOLDER not in skill
    assert "completed `AGENT_GUIDE.md` read event" in skill
    assert "before any runtime check" in skill
    assert set(result) == {"path", "archive_name", "sha256", "size"}


def test_skill_candidate_archive_preserves_existing_baseline(tmp_path: Path) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    package_root = tmp_path / "installed package"
    skill_root = package_root / "shell-adapter/workbuddy-skill/golden-key-openmontage"
    skill_root.mkdir(parents=True)
    (package_root / "AGENT_GUIDE.md").write_text("guide\n", encoding="utf-8")
    (skill_root / "SKILL.md").write_text(
        "skill\n"
        f"{installer.WORKBUDDY_DATA_ROOT_PLACEHOLDER}\n"
        f"{installer.WORKBUDDY_GUIDE_PATH_PLACEHOLDER}\n"
        f"{installer.WORKBUDDY_PACKAGE_ROOT_PLACEHOLDER}\n",
        encoding="utf-8",
    )

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


@pytest.mark.parametrize(
    "guide_binding",
    ["", f"{installer.WORKBUDDY_GUIDE_PATH_PLACEHOLDER}\n" * 2],
)
def test_skill_archive_requires_one_installation_binding_each(
    tmp_path: Path, guide_binding: str
) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    package_root = tmp_path / "package"
    skill_root = package_root / "shell-adapter/workbuddy-skill/golden-key-openmontage"
    skill_root.mkdir(parents=True)
    (package_root / "AGENT_GUIDE.md").write_text("guide\n", encoding="utf-8")
    (skill_root / "SKILL.md").write_text(
        "skill\n"
        f"{installer.WORKBUDDY_DATA_ROOT_PLACEHOLDER}\n"
        f"{guide_binding}"
        f"{installer.WORKBUDDY_PACKAGE_ROOT_PLACEHOLDER}\n",
        encoding="utf-8",
    )

    with pytest.raises(InstallerError, match="installation_placeholder_invalid"):
        installer._build_workbuddy_skill_archive(data_root, package_root)


def test_skill_archive_requires_guide_file(tmp_path: Path) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    package_root = tmp_path / "package"
    skill_root = package_root / "shell-adapter/workbuddy-skill/golden-key-openmontage"
    skill_root.mkdir(parents=True)
    (package_root / "AGENT_GUIDE.md").mkdir()
    (skill_root / "SKILL.md").write_text(
        "skill\n"
        f"{installer.WORKBUDDY_DATA_ROOT_PLACEHOLDER}\n"
        f"{installer.WORKBUDDY_GUIDE_PATH_PLACEHOLDER}\n"
        f"{installer.WORKBUDDY_PACKAGE_ROOT_PLACEHOLDER}\n",
        encoding="utf-8",
    )

    with pytest.raises(InstallerError, match="workbuddy_guide_not_file"):
        installer._build_workbuddy_skill_archive(data_root, package_root)


def test_formal_release_contains_only_cmd_inner_release_and_sidecar(tmp_path: Path) -> None:
    inner = tmp_path / "golden-key-openmontage-for-workbuddy-0.3.25-test.zip"
    inner.write_bytes(b"inner release")
    sidecar = inner.with_name(inner.name + ".sha256")
    sidecar.write_text(
        f"{installer._sha256(inner)} *{inner.name}\n",
        encoding="utf-8",
        newline="",
    )
    command = tmp_path / installer.INSTALLER_CMD_NAME
    command.write_bytes(b"@echo off\r\n")

    result = installer._build_formal_release(inner, command)

    formal = Path(result["path"])
    assert result["sha256"] == installer._sha256(formal)
    assert result["members"] == [installer.INSTALLER_CMD_NAME, inner.name, sidecar.name]
    with zipfile.ZipFile(formal) as archive:
        assert archive.namelist() == result["members"]
        assert archive.read(installer.INSTALLER_CMD_NAME) == command.read_bytes()
        assert archive.read(inner.name) == inner.read_bytes()
        assert archive.read(sidecar.name) == sidecar.read_bytes()


def test_release_validation_reads_every_member_for_crc(tmp_path: Path) -> None:
    release = tmp_path / "release.zip"
    _write_release_archive(release)
    with zipfile.ZipFile(release) as archive:
        member = archive.infolist()[0]
    raw = bytearray(release.read_bytes())
    name_size = int.from_bytes(raw[member.header_offset + 26 : member.header_offset + 28], "little")
    extra_size = int.from_bytes(raw[member.header_offset + 28 : member.header_offset + 30], "little")
    raw[member.header_offset + 30 + name_size + extra_size] ^= 1
    release.write_bytes(raw)
    release.with_name(release.name + ".sha256").write_text(
        f"{installer._sha256(release)} *{release.name}\n", encoding="utf-8"
    )

    with pytest.raises(InstallerError, match="release_archive_invalid"):
        installer._validate_release_archive(release)


def test_install_prepares_new_and_recovery_skills_without_activation(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    old_root = tmp_path / "old-package"
    new_root = tmp_path / "new-package"
    old_registration_sha = "a" * 64
    new_registration_sha = "b" * 64
    previous_raw = _registry_with_pointer(data_root, old_registration_sha)
    archive = tmp_path / "release.zip"
    _write_release_archive(archive)

    def make_package(root: Path) -> None:
        skill = root / installer.WORKBUDDY_SKILL_ROOT_RELATIVE_PATH / "SKILL.md"
        skill.parent.mkdir(parents=True)
        (root / "AGENT_GUIDE.md").write_text("guide\n", encoding="utf-8")
        skill.write_text(
            f"{installer.WORKBUDDY_DATA_ROOT_PLACEHOLDER}\n"
            f"{installer.WORKBUDDY_GUIDE_PATH_PLACEHOLDER}\n"
            f"{installer.WORKBUDDY_PACKAGE_ROOT_PLACEHOLDER}\n",
            encoding="utf-8",
        )

    make_package(old_root)

    def fake_extract(_archive: Path, destination: Path) -> None:
        make_package(destination)

    monkeypatch.setattr(installer, "_extract_release", fake_extract)
    monkeypatch.setattr(
        package_registration,
        "_load_registration",
        lambda _paths, _sha: {"package_root": str(old_root)},
    )
    monkeypatch.setattr(
        package_registration,
        "_build_registration",
        lambda **_kwargs: ({}, b"registration\n", new_registration_sha),
    )
    monkeypatch.setattr(
        package_registration,
        "_atomic_replace_active",
        lambda *_args, **_kwargs: pytest.fail("prepare must not activate"),
    )

    result = installer.install_release(
        data_root=data_root,
        release_archive=archive,
        package_root=new_root,
    )

    active = data_root / "State" / "PackageRegistration" / "v1" / "active.json"
    assert active.read_bytes() == previous_raw
    assert result["activated"] is False
    assert result["active_pointer_sha256"] is None
    assert result["previous_registration_sha256"] == old_registration_sha
    assert Path(result["workbuddy_skill"]["path"]).is_file()
    assert Path(result["recovery_workbuddy_skill"]["path"]).is_file()
    with zipfile.ZipFile(result["workbuddy_skill"]["path"]) as stream:
        assert str(new_root.resolve()) in stream.read("SKILL.md").decode("utf-8")
    with zipfile.ZipFile(result["recovery_workbuddy_skill"]["path"]) as stream:
        assert str(old_root.resolve()) in stream.read("SKILL.md").decode("utf-8")


def test_identical_skill_candidate_can_be_reused_for_resume(tmp_path: Path) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    package_root = tmp_path / "package"
    skill = package_root / installer.WORKBUDDY_SKILL_ROOT_RELATIVE_PATH / "SKILL.md"
    skill.parent.mkdir(parents=True)
    (package_root / "AGENT_GUIDE.md").write_text("guide\n", encoding="utf-8")
    skill.write_text(
        f"{installer.WORKBUDDY_DATA_ROOT_PLACEHOLDER}\n"
        f"{installer.WORKBUDDY_GUIDE_PATH_PLACEHOLDER}\n"
        f"{installer.WORKBUDDY_PACKAGE_ROOT_PLACEHOLDER}\n",
        encoding="utf-8",
    )

    first = installer._build_workbuddy_skill_archive(
        data_root,
        package_root,
        archive_name="resume.zip",
    )
    second = installer._build_workbuddy_skill_archive(
        data_root,
        package_root,
        archive_name="resume.zip",
        reuse_if_identical=True,
    )

    assert second == first


def test_locator_postcheck_failure_restores_previous_pointer(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    package_root = tmp_path / "package"
    package_root.mkdir()
    new_registration_sha = "b" * 64
    old_registration_sha = "a" * 64
    calls: list[tuple[str, str]] = []

    monkeypatch.setattr(
        package_registration,
        "activate_package",
        lambda _data, expected, target: calls.append((expected, target)) or target,
    )
    monkeypatch.setattr(
        package_registration,
        "locate_active_package",
        lambda _data: (_ for _ in ()).throw(InstallerError("forced-postcheck")),
    )
    expected_old = installer._sha256_bytes(
        package_registration._pointer_bytes(old_registration_sha)
    )
    monkeypatch.setattr(
        installer,
        "_active_installation",
        lambda _data: {
            "pointer_sha256": expected_old,
            "registration_sha256": old_registration_sha,
            "package_root": str(package_root),
        },
    )

    with pytest.raises(
        InstallerError,
        match="PACKAGE_ROLLBACK_COMPLETE:WORKBUDDY_SKILL_RESTORE_REQUIRED",
    ):
        installer.activate_prepared_release(
            data_root=data_root,
            package_root=package_root,
            registration_sha256=new_registration_sha,
            expected_active_pointer_sha256_or_missing=expected_old,
            previous_registration_sha256=old_registration_sha,
        )

    expected_new = installer._sha256_bytes(
        package_registration._pointer_bytes(new_registration_sha)
    )
    assert calls == [
        (expected_old, new_registration_sha),
        (expected_new, old_registration_sha),
    ]


def test_clean_install_postcheck_failure_deactivates_new_pointer(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    package_root = tmp_path / "package"
    package_root.mkdir()
    registration_sha = "b" * 64
    calls: list[tuple[str, str]] = []

    monkeypatch.setattr(package_registration, "activate_package", lambda *_args: registration_sha)
    monkeypatch.setattr(
        package_registration,
        "locate_active_package",
        lambda _data: (_ for _ in ()).throw(InstallerError("forced-postcheck")),
    )
    monkeypatch.setattr(
        package_registration,
        "_deactivate_package",
        lambda _data, expected, target: calls.append((expected, target)) or "MISSING",
    )

    with pytest.raises(InstallerError, match="PACKAGE_ROLLBACK_COMPLETE"):
        installer.activate_prepared_release(
            data_root=data_root,
            package_root=package_root,
            registration_sha256=registration_sha,
            expected_active_pointer_sha256_or_missing="MISSING",
            previous_registration_sha256=None,
        )

    assert calls == [
        (
            installer._sha256_bytes(package_registration._pointer_bytes(registration_sha)),
            registration_sha,
        )
    ]


def test_activation_error_after_pointer_write_restores_previous_pointer(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    data_root = tmp_path / "data"
    data_root.mkdir()
    package_root = tmp_path / "package"
    package_root.mkdir()
    old_registration_sha = "a" * 64
    new_registration_sha = "b" * 64
    calls: list[tuple[str, str]] = []

    def activate(_data: Path, expected: str, target: str) -> str:
        calls.append((expected, target))
        if target == new_registration_sha:
            raise InstallerError("forced-readback-failure")
        return target

    monkeypatch.setattr(package_registration, "activate_package", activate)
    def active(_data: Path) -> dict[str, str]:
        registration = new_registration_sha if len(calls) == 1 else old_registration_sha
        return {
            "pointer_sha256": "c" * 64 if len(calls) == 1 else "d" * 64,
            "registration_sha256": registration,
            "package_root": str(package_root),
        }

    monkeypatch.setattr(installer, "_active_installation", active)

    with pytest.raises(InstallerError, match="PACKAGE_ROLLBACK_COMPLETE"):
        installer.activate_prepared_release(
            data_root=data_root,
            package_root=package_root,
            registration_sha256=new_registration_sha,
            expected_active_pointer_sha256_or_missing="d" * 64,
            previous_registration_sha256=old_registration_sha,
        )

    assert calls == [
        ("d" * 64, new_registration_sha),
        (
            installer._sha256_bytes(package_registration._pointer_bytes(new_registration_sha)),
            old_registration_sha,
        ),
    ]


def test_standard_windows_paths_are_release_bound_and_not_drive_fixed(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    program_files = tmp_path / "Program Files"
    local_app_data = tmp_path / "Local App Data"
    program_files.mkdir()
    local_app_data.mkdir()
    release = tmp_path / "release.zip"
    _write_release_archive(release)
    monkeypatch.setenv("ProgramFiles", str(program_files))
    monkeypatch.setenv("LOCALAPPDATA", str(local_app_data))

    data_root, package_root = installer._standard_install_paths(release)

    assert data_root == (
        local_app_data / installer.INSTALL_PRODUCT_DIRECTORY / "data" / "production"
    ).resolve()
    assert package_root.parent == (
        program_files / installer.INSTALL_PRODUCT_DIRECTORY / "Packages"
    ).resolve()
    assert package_root.name.endswith(installer._sha256(release)[:12])


def test_top_level_installer_cmd_uses_only_verified_ui_assisted_route() -> None:
    command = (
        Path(__file__).resolve().parents[2] / installer.INSTALLER_CMD_NAME
    ).read_text(encoding="utf-8")

    assert "Get-FileHash" in command
    assert "Expand-Archive" in command
    assert "ui-install --release-archive" in command
    assert "golden_key_openmontage_workbuddy.installer" in command
    assert '\\"' not in command
    assert "if errorlevel 1 (" not in command
    assert "exit /b %errorlevel%" in command
    assert ".workbuddy\\skills" not in command
    assert "Remotion" not in command
    assert "ARK_API_KEY" not in command
