from __future__ import annotations

import json
import socket
from pathlib import Path

from golden_key_openmontage_workbuddy.cli import main


ROOT = Path(__file__).resolve().parents[2]


def test_config_inspect_separates_workbuddy_model_from_production_providers(
    capsys, monkeypatch
) -> None:
    from tools.tool_registry import ToolRegistry

    monkeypatch.setenv("DASHSCOPE_API_KEY", "must-not-leak-dashscope")
    monkeypatch.setenv("KLING_API_KEY", "must-not-leak-kling")
    network_attempts: list[str] = []

    def reject_network(*args, **kwargs):
        network_attempts.append(repr(args))
        raise AssertionError("configuration discovery must stay offline")

    monkeypatch.setattr(socket, "create_connection", reject_network)
    monkeypatch.setattr(socket.socket, "connect", reject_network)
    monkeypatch.setattr(
        ToolRegistry,
        "_load_dotenv",
        staticmethod(lambda: (_ for _ in ()).throw(AssertionError("must not load .env"))),
    )

    assert main(["config", "inspect", "--repo-root", str(ROOT), "--json"]) == 0

    raw = capsys.readouterr().out
    payload = json.loads(raw)
    assert payload["status"] == "pass"
    assert payload["workbuddy_conversation_model"] == {
        "managed_by": "workbuddy_host",
        "configured_by_adapter": False,
        "adapter_uses_model_credentials": False,
        "invocation_model": "direct_agent",
        "nested_agent_host_allowed": False,
        "configuration_guidance": (
            "Configure the conversation model in WorkBuddy itself; this adapter "
            "does not define or proxy it."
        ),
    }
    assert payload["production_provider_layer"]["managed_by"] == (
        "golden_key_tool_registry"
    )
    assert payload["production_provider_layer"]["credentials"] == (
        "environment_variable_names_only"
    )
    assert payload["provider_calls_attempted"] == 0
    assert payload["network_calls_attempted"] == 0
    assert network_attempts == []
    assert "must-not-leak-dashscope" not in raw
    assert "must-not-leak-kling" not in raw


def test_config_inspect_reports_only_registry_backed_china_ecosystem_profiles(
    capsys,
) -> None:
    assert main(["config", "inspect", "--repo-root", str(ROOT), "--json"]) == 0
    payload = json.loads(capsys.readouterr().out)

    profiles = {item["provider"]: item for item in payload["production_providers"]}
    assert set(profiles) == {
        "dashscope",
        "doubao",
        "volcengine",
        "kling_official",
        "seedance",
        "minimax",
    }
    assert profiles["dashscope"]["access_path"] == "direct_vendor_api"
    assert profiles["dashscope"]["credential_env_vars"] == ["DASHSCOPE_API_KEY"]
    assert profiles["dashscope"]["tools"] == [
        "dashscope_asr",
        "dashscope_image",
        "dashscope_tts",
    ]
    assert profiles["doubao"]["credential_env_vars"] == [
        "DOUBAO_SPEECH_API_KEY"
    ]
    assert profiles["volcengine"]["credential_env_vars"] == [
        "VOLC_ACCESSKEY",
        "VOLC_SECRETKEY",
    ]
    assert profiles["kling_official"]["access_path"] == "direct_vendor_api"
    assert profiles["seedance"]["access_path"] == "third_party_gateway"
    assert profiles["minimax"]["access_path"] == "third_party_gateway"
    assert all(item["registry_verified"] is True for item in profiles.values())
    assert all(item["runtime"] == "api" for item in profiles.values())
    assert all(item["network_required"] is True for item in profiles.values())


def test_config_template_writes_only_safe_references_under_d_data_root(
    tmp_path: Path, capsys, monkeypatch
) -> None:
    monkeypatch.setenv("VOLC_SECRETKEY", "must-not-be-written")

    assert main(
        [
            "config",
            "template",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(tmp_path),
            "--json",
        ]
    ) == 0
    result = json.loads(capsys.readouterr().out)
    target = tmp_path / "Config" / "golden-key-production-providers.json"
    assert result["path"] == str(target.resolve())
    assert result["created"] is True
    assert result["provider_calls_attempted"] == 0
    assert target.is_file()

    raw = target.read_text(encoding="utf-8")
    template = json.loads(raw)
    assert template["schema_version"] == "1.0"
    assert template["workbuddy_conversation_model"]["configured_by_adapter"] is False
    assert template["production_provider_credentials"]["storage"] == "environment"
    assert "must-not-be-written" not in raw
    assert '"api_key":' not in raw.lower()
    assert '"secret_key":' not in raw.lower()
    assert "VOLC_SECRETKEY" in raw

    assert main(
        [
            "config",
            "template",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(tmp_path),
            "--json",
        ]
    ) == 0
    repeated = json.loads(capsys.readouterr().out)
    assert repeated["created"] is False
    assert repeated["unchanged"] is True


def test_config_template_refuses_to_overwrite_user_changes(tmp_path: Path, capsys) -> None:
    target = tmp_path / "Config" / "golden-key-production-providers.json"
    target.parent.mkdir(parents=True)
    target.write_text('{"user_owned": true}\n', encoding="utf-8")

    assert main(
        [
            "config",
            "template",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(tmp_path),
            "--json",
        ]
    ) == 1
    payload = json.loads(capsys.readouterr().out)
    assert payload["status"] == "fail"
    assert "refuses to overwrite" in payload["errors"][0]
    assert target.read_text(encoding="utf-8") == '{"user_owned": true}\n'
