from __future__ import annotations

import importlib
import json
import os
import pkgutil
from pathlib import Path
from typing import Any


class ModelProviderConfigError(ValueError):
    """The consumer-owned model/provider configuration contract is invalid."""


# This consumer-owned index does not claim that every China-ecosystem model has
# a mainland endpoint. It records the access path actually implemented by the
# locked Tool Registry so WorkBuddy can distinguish direct vendor APIs from
# third-party gateways.
CHINA_ECOSYSTEM_PROVIDER_SPECS: tuple[dict[str, Any], ...] = (
    {
        "provider": "dashscope",
        "service": "Alibaba Cloud Bailian / DashScope",
        "access_path": "direct_vendor_api",
        "credential_env_vars": ["DASHSCOPE_API_KEY"],
        "credential_groups": [["DASHSCOPE_API_KEY"]],
        "configuration_env_vars": [],
        "tools": ["dashscope_asr", "dashscope_image", "dashscope_tts"],
        "guide_capabilities": ["analysis", "image_generation", "tts"],
    },
    {
        "provider": "doubao",
        "service": "Volcengine Doubao Speech",
        "access_path": "direct_vendor_api",
        "credential_env_vars": ["DOUBAO_SPEECH_API_KEY"],
        "credential_groups": [["DOUBAO_SPEECH_API_KEY"]],
        "configuration_env_vars": ["DOUBAO_SPEECH_VOICE_TYPE"],
        "tools": ["doubao_tts"],
        "guide_capabilities": ["tts"],
    },
    {
        "provider": "volcengine",
        "service": "Volcengine Jimeng",
        "access_path": "direct_vendor_api",
        "credential_env_vars": ["VOLC_ACCESSKEY", "VOLC_SECRETKEY"],
        "credential_groups": [["VOLC_ACCESSKEY", "VOLC_SECRETKEY"]],
        "configuration_env_vars": [],
        "tools": ["jimeng_video"],
        "guide_capabilities": ["video_generation"],
    },
    {
        "provider": "kling_official",
        "service": "Kling official API",
        "access_path": "direct_vendor_api",
        "credential_env_vars": ["KLING_API_KEY"],
        "credential_groups": [["KLING_API_KEY"]],
        "configuration_env_vars": ["KLING_API_BASE_URL"],
        "tools": [
            "kling_avatar",
            "kling_lip_sync",
            "kling_official_image",
            "kling_official_video",
            "kling_tts",
        ],
        "guide_capabilities": [
            "avatar",
            "image_generation",
            "tts",
            "video_generation",
        ],
    },
    {
        "provider": "seedance",
        "service": "Seedance through configured gateways",
        "access_path": "third_party_gateway",
        "credential_env_vars": [
            "FAL_KEY",
            "FAL_AI_API_KEY",
            "REPLICATE_API_TOKEN",
        ],
        "credential_groups": [
            ["FAL_KEY"],
            ["FAL_AI_API_KEY"],
            ["REPLICATE_API_TOKEN"],
        ],
        "configuration_env_vars": [],
        "tools": ["seedance_replicate", "seedance_video"],
        "guide_capabilities": ["video_generation"],
    },
    {
        "provider": "minimax",
        "service": "MiniMax / Hailuo through fal.ai",
        "access_path": "third_party_gateway",
        "credential_env_vars": ["FAL_KEY", "FAL_AI_API_KEY"],
        "credential_groups": [["FAL_KEY"], ["FAL_AI_API_KEY"]],
        "configuration_env_vars": [],
        "tools": ["minimax_video"],
        "guide_capabilities": ["video_generation"],
    },
)

GUIDE_FALLBACK_DEPENDENCIES = {
    "dotenv",
    "google",
    "httpx",
    "jsonschema",
    "openai",
    "PIL",
    "pydantic",
    "requests",
    "yaml",
}


def _conversation_model_contract() -> dict[str, Any]:
    return {
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


def _build_static_tool_registry():
    """Discover tool classes without loading `.env` or probing live status."""

    from tools.tool_registry import ToolRegistry

    registry = ToolRegistry()
    package = importlib.import_module("tools")
    for module_info in pkgutil.walk_packages(package.__path__, "tools."):
        if module_info.name.endswith((".base_tool", ".tool_registry")):
            continue
        registry.register_module(importlib.import_module(module_info.name))
    return registry


def build_model_provider_report(repo_root: Path) -> dict[str, Any]:
    """Verify consumer metadata against Tool Registry class contracts offline."""

    repo_root = Path(repo_root).resolve()
    if not (repo_root / "tools" / "tool_registry.py").is_file():
        raise ModelProviderConfigError(
            f"Tool Registry not found under repository root: {repo_root}"
        )

    registry = _build_static_tool_registry()
    providers: list[dict[str, Any]] = []
    errors: list[str] = []
    for spec in CHINA_ECOSYSTEM_PROVIDER_SPECS:
        verified_tools: list[Any] = []
        for name in spec["tools"]:
            tool = registry.get(name)
            if tool is None:
                errors.append(f"Tool Registry is missing {name!r}")
                continue
            if tool.provider != spec["provider"]:
                errors.append(
                    f"Tool {name!r} provider drifted from {spec['provider']!r} "
                    f"to {tool.provider!r}"
                )
                continue
            verified_tools.append(tool)

        runtimes = {
            str(getattr(tool.runtime, "value", tool.runtime)) for tool in verified_tools
        }
        network_flags = {
            bool(tool.resource_profile.network_required) for tool in verified_tools
        }
        if verified_tools and runtimes != {"api"}:
            errors.append(
                f"Provider {spec['provider']!r} no longer has a uniform API runtime"
            )
        if verified_tools and network_flags != {True}:
            errors.append(
                f"Provider {spec['provider']!r} no longer has a uniform network boundary"
            )

        capabilities = sorted({tool.capability for tool in verified_tools})
        if verified_tools and capabilities != sorted(spec["guide_capabilities"]):
            errors.append(
                f"Provider {spec['provider']!r} guide capability index drifted from "
                f"Tool Registry: expected {sorted(spec['guide_capabilities'])!r}, "
                f"found {capabilities!r}"
            )

        providers.append(
            {
                **spec,
                "classification": "china_ecosystem",
                "registry_verified": len(verified_tools) == len(spec["tools"]),
                "runtime": "api" if runtimes == {"api"} else "mixed_or_drifted",
                "network_required": network_flags == {True},
                "capabilities": capabilities,
                "install_instructions": sorted(
                    {
                        str(tool.install_instructions).strip()
                        for tool in verified_tools
                        if str(tool.install_instructions).strip()
                    }
                ),
                "configured_status_checked": False,
            }
        )

    return {
        "status": "fail" if errors else "pass",
        "workbuddy_conversation_model": _conversation_model_contract(),
        "production_provider_layer": {
            "managed_by": "golden_key_tool_registry",
            "credentials": "environment_variable_names_only",
            "provider_selection_actor": "workbuddy_agent_with_user_approval",
            "real_provider_authorization_required": True,
        },
        "production_providers": providers,
        "provider_calls_attempted": 0,
        "network_calls_attempted": 0,
        "errors": errors,
    }


def build_provider_setup_guide(repo_root: Path, data_root: Path) -> dict[str, Any]:
    """Report API-key presence for guided setup without returning values or networking."""

    missing_python_dependency: str | None = None
    try:
        report = build_model_provider_report(repo_root)
    except ModuleNotFoundError as exc:
        missing_python_dependency = exc.name or "unknown"
        if missing_python_dependency.split(".", 1)[0] not in GUIDE_FALLBACK_DEPENDENCIES:
            raise
        report = {
            "status": "pass",
            "production_providers": [
                {
                    **spec,
                    "capabilities": list(spec["guide_capabilities"]),
                    "install_instructions": [],
                }
                for spec in CHINA_ECOSYSTEM_PROVIDER_SPECS
            ],
        }
    if report["status"] != "pass":
        raise ModelProviderConfigError("Tool Registry verification failed")

    providers: list[dict[str, Any]] = []
    for provider in report["production_providers"]:
        names = list(provider["credential_env_vars"])
        present = sorted(name for name in names if bool(os.environ.get(name)))
        present_set = set(present)
        groups = [list(group) for group in provider["credential_groups"]]
        complete = any(set(group).issubset(present_set) for group in groups)
        if complete:
            state = "present_unverified"
        elif present:
            state = "partial"
        else:
            state = "not_configured"
        providers.append(
            {
                "provider": provider["provider"],
                "service": provider["service"],
                "access_path": provider["access_path"],
                "capabilities": provider["capabilities"],
                "credential_options": groups,
                "present_env_vars": present,
                "missing_env_vars": sorted(set(names) - present_set),
                "credential_state": state,
                "install_instructions": provider["install_instructions"],
            }
        )

    capabilities: dict[str, dict[str, Any]] = {}
    for provider in providers:
        for capability in provider["capabilities"]:
            bucket = capabilities.setdefault(
                capability,
                {"capability": capability, "configured": 0, "total": 0, "providers": []},
            )
            bucket["total"] += 1
            if provider["credential_state"] == "present_unverified":
                bucket["configured"] += 1
            bucket["providers"].append(provider["provider"])

    return {
        "status": "pass",
        "tool_registry_verification": (
            "verified"
            if missing_python_dependency is None
            else "deferred_missing_python_dependency"
        ),
        "missing_python_dependency": missing_python_dependency,
        "credential_store": {
            "path": str(
                (Path(data_root).resolve() / "Config" / "golden-key-provider-credentials.json")
            ),
            "protection": "windows_dpapi_current_user",
            "values_returned": False,
        },
        "capabilities": sorted(capabilities.values(), key=lambda item: item["capability"]),
        "providers": providers,
        "security_rules": {
            "never_paste_api_keys_in_chat": True,
            "use_local_hidden_input": True,
            "presence_is_not_connectivity": True,
            "configuration_is_not_provider_authorization": True,
        },
        "provider_calls_attempted": 0,
        "network_calls_attempted": 0,
        "warnings": (
            []
            if missing_python_dependency is None
            else [
                "Provider choices are available from the locked consumer index; "
                "prepare Python dependencies before production Tool Registry use."
            ]
        ),
        "errors": [],
    }


def build_safe_provider_template(repo_root: Path) -> dict[str, Any]:
    report = build_model_provider_report(repo_root)
    if report["status"] != "pass":
        raise ModelProviderConfigError("Tool Registry verification failed")
    return {
        "schema_version": "1.0",
        "workbuddy_conversation_model": report["workbuddy_conversation_model"],
        "production_provider_credentials": {
            "storage": "environment",
            "embed_credential_values": False,
            "providers": [
                {
                    key: item[key]
                    for key in (
                        "provider",
                        "service",
                        "classification",
                        "access_path",
                        "credential_env_vars",
                        "configuration_env_vars",
                        "tools",
                        "capabilities",
                    )
                }
                for item in report["production_providers"]
            ],
        },
    }


def write_safe_provider_template(repo_root: Path, data_root: Path) -> dict[str, Any]:
    template = build_safe_provider_template(repo_root)
    target = Path(data_root).resolve() / "Config" / "golden-key-production-providers.json"
    serialized = json.dumps(template, ensure_ascii=False, indent=2) + "\n"
    created = not target.exists()
    if target.exists():
        try:
            existing = target.read_text(encoding="utf-8")
        except OSError as exc:
            raise ModelProviderConfigError(f"cannot read existing template: {exc}") from exc
        if existing != serialized:
            raise ModelProviderConfigError(
                f"refuses to overwrite consumer-owned configuration: {target}"
            )
    else:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(serialized, encoding="utf-8")
    return {
        "status": "pass",
        "path": str(target),
        "created": created,
        "unchanged": not created,
        "provider_calls_attempted": 0,
        "network_calls_attempted": 0,
        "errors": [],
    }
