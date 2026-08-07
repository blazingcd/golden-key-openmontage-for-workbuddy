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

CAPABILITY_GUIDANCE: tuple[dict[str, Any], ...] = (
    {
        "capability": "image_generation",
        "label_zh": "生成图片",
        "description_zh": "生成封面、商品图、场景图或视频所需的静态画面",
        "recommended_providers": ["dashscope", "kling_official"],
    },
    {
        "capability": "video_generation",
        "label_zh": "生成视频",
        "description_zh": "文生视频、图生视频或补充动态镜头",
        "recommended_providers": ["volcengine", "kling_official"],
    },
    {
        "capability": "tts",
        "label_zh": "中文配音",
        "description_zh": "把脚本合成为中文或多语言旁白",
        "recommended_providers": ["doubao", "dashscope"],
    },
    {
        "capability": "avatar",
        "label_zh": "数字人或口型驱动",
        "description_zh": "生成数字人讲解、口型同步或头像驱动视频",
        "recommended_providers": ["kling_official"],
    },
    {
        "capability": "analysis",
        "label_zh": "语音识别与内容分析",
        "description_zh": "识别已有音视频语音或辅助理解素材内容",
        "recommended_providers": ["dashscope"],
    },
)

CAPABILITY_LABELS_ZH = {
    item["capability"]: item["label_zh"] for item in CAPABILITY_GUIDANCE
}

PROVIDER_GUIDANCE: dict[str, dict[str, str]] = {
    "dashscope": {
        "display_name_zh": "阿里云百炼（DashScope）",
        "summary_zh": "适合中文语音识别、图片生成和中文配音的厂商直连接入。",
        "availability_notice_zh": "需要阿里云百炼账号、已开通相应模型，并选择与Key一致的地域。",
    },
    "doubao": {
        "display_name_zh": "火山引擎豆包语音",
        "summary_zh": "面向中文旁白和语音合成的厂商直连接入。",
        "availability_notice_zh": "需要在豆包语音新版控制台开通相应语音服务；旧版App ID/Access Token不能冒充新版API Key。",
    },
    "volcengine": {
        "display_name_zh": "火山引擎即梦",
        "summary_zh": "使用火山引擎IAM的AK/SK调用即梦视频生成。",
        "availability_notice_zh": "需要同时具备Access Key ID和Secret Access Key，并为IAM身份开通即梦相关权限。",
    },
    "kling_official": {
        "display_name_zh": "可灵官方API",
        "summary_zh": "覆盖图片、视频、配音和数字人能力的可灵官方直连接入。",
        "availability_notice_zh": "开发者账户必须实际拥有API入口和相应产品权限；部分账户或地区可能暂未开放。",
    },
    "seedance": {
        "display_name_zh": "Seedance（第三方网关）",
        "summary_zh": "通过fal.ai或Replicate等当前已实现网关调用Seedance视频能力。",
        "availability_notice_zh": "这是第三方网关接入，不是字节跳动或火山引擎官方直连。",
    },
    "minimax": {
        "display_name_zh": "MiniMax / Hailuo（fal.ai网关）",
        "summary_zh": "通过fal.ai网关调用MiniMax/Hailuo视频能力。",
        "availability_notice_zh": "这是第三方网关接入，不是MiniMax官方直连。",
    },
}

CREDENTIAL_GUIDANCE: dict[str, dict[str, str]] = {
    "DASHSCOPE_API_KEY": {
        "label_zh": "百炼API Key",
        "access_name_zh": "阿里云百炼官方",
        "obtain_url": "https://bailian.console.aliyun.com/?apiKey=1#/api-key",
        "documentation_url": "https://help.aliyun.com/zh/model-studio/get-api-key",
        "billing_notice_zh": "模型调用可能按量计费；地域、模型权限和余额以百炼控制台为准。",
    },
    "DOUBAO_SPEECH_API_KEY": {
        "label_zh": "豆包语音新版API Key",
        "access_name_zh": "火山引擎豆包语音官方",
        "obtain_url": "https://www.volcengine.com/docs/6561/1167802",
        "documentation_url": "https://www.volcengine.com/docs/6561/1167802",
        "billing_notice_zh": "需要先开通所选语音服务；赠送额度和实际收费以控制台当前规则为准。",
    },
    "VOLC_ACCESSKEY": {
        "label_zh": "Access Key ID",
        "access_name_zh": "火山引擎IAM官方",
        "obtain_url": "https://console.volcengine.com/iam/keymanage/",
        "documentation_url": "https://www.volcengine.com/docs/6257/64959",
        "billing_notice_zh": "创建AK/SK本身不代表即梦服务免费；生成费用和权限以火山引擎控制台为准。",
    },
    "VOLC_SECRETKEY": {
        "label_zh": "Secret Access Key",
        "access_name_zh": "火山引擎IAM官方",
        "obtain_url": "https://console.volcengine.com/iam/keymanage/",
        "documentation_url": "https://www.volcengine.com/docs/6257/64959",
        "billing_notice_zh": "创建AK/SK本身不代表即梦服务免费；生成费用和权限以火山引擎控制台为准。",
    },
    "KLING_API_KEY": {
        "label_zh": "可灵官方API Key",
        "access_name_zh": "可灵官方开发者平台",
        "obtain_url": "https://app.klingai.com/global/dev",
        "documentation_url": "https://app.klingai.com/global/dev/document-api/quickStart/productIntroduction/overview",
        "billing_notice_zh": "API权限、套餐、余额和各模型价格以可灵开发者账户当前页面为准。",
    },
    "FAL_KEY": {
        "label_zh": "fal.ai API Key",
        "access_name_zh": "fal.ai网关",
        "obtain_url": "https://fal.ai/dashboard/keys",
        "documentation_url": "https://fal.ai/docs/documentation/setting-up/authentication",
        "billing_notice_zh": "fal.ai是第三方计费网关；建议只创建API权限Key，模型调用可能产生费用。",
    },
    "FAL_AI_API_KEY": {
        "label_zh": "fal.ai API Key（兼容变量）",
        "access_name_zh": "fal.ai网关",
        "obtain_url": "https://fal.ai/dashboard/keys",
        "documentation_url": "https://fal.ai/docs/documentation/setting-up/authentication",
        "billing_notice_zh": "fal.ai是第三方计费网关；建议只创建API权限Key，模型调用可能产生费用。",
    },
    "REPLICATE_API_TOKEN": {
        "label_zh": "Replicate API Token",
        "access_name_zh": "Replicate网关",
        "obtain_url": "https://replicate.com/account/api-tokens",
        "documentation_url": "https://replicate.com/docs/topics/security/api-tokens/",
        "billing_notice_zh": "Replicate是第三方计费网关；Token需要像密码一样保管，模型调用可能产生费用。",
    },
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


def _credential_option_guidance(group: list[str]) -> dict[str, Any]:
    primary = CREDENTIAL_GUIDANCE[group[0]]
    return {
        "env_vars": list(group),
        "access_name_zh": primary["access_name_zh"],
        "fields": [
            {
                "env_var": name,
                "label_zh": CREDENTIAL_GUIDANCE[name]["label_zh"],
            }
            for name in group
        ],
        "obtain_url": primary["obtain_url"],
        "documentation_url": primary["documentation_url"],
        "billing_notice_zh": primary["billing_notice_zh"],
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
                **PROVIDER_GUIDANCE[provider["provider"]],
                "access_path": provider["access_path"],
                "capabilities": provider["capabilities"],
                "capability_labels_zh": [
                    CAPABILITY_LABELS_ZH[capability]
                    for capability in provider["capabilities"]
                ],
                "credential_options": groups,
                "credential_option_guidance": [
                    _credential_option_guidance(group) for group in groups
                ],
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
        "capability_choices": [dict(item) for item in CAPABILITY_GUIDANCE],
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
