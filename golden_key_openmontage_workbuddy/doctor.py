from __future__ import annotations

import json
import importlib.util
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

from .runtime_prepare import build_runtime_plan


EXPECTED_PIPELINES = (
    "golden-key-brand-company",
    "golden-key-lead-conversion",
    "golden-key-product-marketing",
    "golden-key-subject-ip",
)
EXPECTED_CONTRACT_ID = "golden-key-workbuddy-callable-core-v1"
EXPECTED_TAG = "golden-key-v0.3.21"
EXPECTED_SOURCE_COMMIT = "757ea3822e5f2eef7f341389983119021e827c8d"
REQUIRED_PYTHON_PACKAGES = (
    "dotenv",
    "google.genai",
    "httpx",
    "jsonschema",
    "openai",
    "PIL",
    "pydantic",
    "requests",
    "yaml",
)


def _missing_python_packages() -> list[str]:
    missing: list[str] = []
    for module in REQUIRED_PYTHON_PACKAGES:
        try:
            available = importlib.util.find_spec(module) is not None
        except (ImportError, ModuleNotFoundError, ValueError):
            available = False
        if not available:
            missing.append(module)
    return missing


def _command_runtime(command: str) -> dict[str, Any]:
    executable = shutil.which(command)
    if executable is None:
        return {"available": False, "executable": None, "version": None}
    try:
        result = subprocess.run(
            [executable, "--version"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=5,
            check=False,
        )
        version = (result.stdout or result.stderr).splitlines()[0].strip()
    except (OSError, subprocess.SubprocessError) as exc:
        return {
            "available": False,
            "executable": executable,
            "version": None,
            "error": str(exc),
        }
    return {"available": True, "executable": executable, "version": version}


def _local_cli_runtime(
    path: Path, *, inspection: str, runtime_name: str
) -> dict[str, Any]:
    if not path.is_file():
        return {
            "available": False,
            "executable": str(path),
            "version": None,
            "inspection": inspection,
        }
    root = path.parents[2]
    node = shutil.which("node")
    if runtime_name == "remotion":
        script = root / "node_modules" / "@remotion" / "cli" / "remotion-cli.js"
        command = [node or "node", str(script), "versions"]
    elif runtime_name == "hyperframes":
        script = root / "node_modules" / "hyperframes" / "bin" / "hyperframes.mjs"
        command = [node or "node", str(script), "--version"]
    else:
        script = path
        command = [str(path), "--version"]
    if node is None or not script.is_file():
        return {
            "available": False,
            "executable": str(path),
            "version": None,
            "inspection": inspection,
            "error": "managed Node or runtime entrypoint is missing",
        }
    try:
        result = subprocess.run(
            command,
            cwd=root,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=20,
            check=False,
        )
        output = result.stdout or result.stderr
        if runtime_name == "remotion":
            match = re.search(r"^On version:\s*(\S+)", output, re.MULTILINE)
            version = match.group(1) if match else None
        else:
            version = output.splitlines()[0].strip() if output.splitlines() else None
        available = result.returncode == 0
    except (OSError, subprocess.SubprocessError) as exc:
        return {
            "available": False,
            "executable": str(path),
            "version": None,
            "inspection": inspection,
            "error": str(exc),
        }
    return {
        "available": available,
        "executable": str(path),
        "version": version or None,
        "inspection": inspection,
    }


def build_doctor_report(
    repo_root: Path, data_root: Path, *, create_dirs: bool = False
) -> dict[str, Any]:
    repo_root = Path(repo_root).resolve()
    data_root = Path(data_root).resolve()
    errors: list[str] = []

    config_path = repo_root / "config" / "openmontage.sync.json"
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        config = {}
        errors.append(f"cannot read sync config: {exc}")

    core = {
        "contract_id": config.get("golden_key_core_contract_id"),
        "source_commit": config.get("golden_key_core_source_commit"),
        "tag": config.get("golden_key_core_tag"),
    }
    expected_core = {
        "contract_id": EXPECTED_CONTRACT_ID,
        "source_commit": EXPECTED_SOURCE_COMMIT,
        "tag": EXPECTED_TAG,
    }
    if core != expected_core:
        errors.append("callable-core identity does not match the locked v0.3.21 contract")

    authority_config = config.get("authority") or {}
    authority = {
        "invocation_model": authority_config.get("invocation_model"),
        "nested_agent_host_allowed": authority_config.get(
            "nested_agent_host_allowed"
        ),
    }
    if authority != {
        "invocation_model": "direct_agent",
        "nested_agent_host_allowed": False,
    }:
        errors.append("authority must remain direct_agent with no nested Agent Host")

    available = sorted(
        pipeline
        for pipeline in EXPECTED_PIPELINES
        if (repo_root / "pipeline_defs" / f"{pipeline}.yaml").is_file()
    )
    missing = sorted(set(EXPECTED_PIPELINES) - set(available))
    if missing:
        errors.append(f"missing Golden Key pipelines: {', '.join(missing)}")

    directories = {
        "caches": data_root / "Caches",
        "jobs": data_root / "Jobs",
        "logs": data_root / "Logs",
        "models": data_root / "Models",
        "projects": data_root / "Projects",
        "temp": data_root / "Temp",
    }
    if create_dirs:
        try:
            for path in directories.values():
                path.mkdir(parents=True, exist_ok=True)
        except OSError as exc:
            errors.append(f"cannot create data directories: {exc}")

    python_supported = sys.version_info >= (3, 10)
    if not python_supported:
        errors.append("Python 3.10 or newer is required")
    missing_python_packages = _missing_python_packages()
    production_plan = build_runtime_plan(repo_root, data_root)
    production_components = {
        name: bool(component["ready"])
        for name, component in production_plan["components"].items()
    }
    targets = production_plan["targets"]
    command_suffix = ".cmd" if sys.platform == "win32" else ""
    remotion_cli = (
        Path(targets["remotion"])
        / "node_modules"
        / ".bin"
        / f"remotion{command_suffix}"
    )
    hyperframes_cli = (
        Path(targets["hyperframes"])
        / "node_modules"
        / ".bin"
        / f"hyperframes{command_suffix}"
    )
    remotion_runtime = _local_cli_runtime(
        remotion_cli,
        inspection="local_cli_only",
        runtime_name="remotion",
    )
    hyperframes_runtime = _local_cli_runtime(
        hyperframes_cli,
        inspection="local_cli_and_managed_browser_only",
        runtime_name="hyperframes",
    )
    hyperframes_runtime["managed_browser_ready"] = production_components[
        "hyperframes"
    ]
    ffmpeg_runtime = _command_runtime("ffmpeg")
    node_runtime = _command_runtime("node")
    complete_environment_ready = (
        production_plan["status"] == "ready"
        and not missing_python_packages
        and ffmpeg_runtime["available"]
        and node_runtime["available"]
        and remotion_runtime["available"]
        and hyperframes_runtime["available"]
    )
    runtime = {
        "capability_requirements": {
            "python": {
                "requirement": "required",
                "preparation": "managed_complete_environment_after_user_confirmation",
            },
            "ffmpeg": {
                "requirement": "required_for_complete_environment",
                "preparation": "managed_complete_environment_after_user_confirmation",
            },
            "node": {
                "requirement": "required_for_complete_environment",
                "unlocks": ["remotion", "hyperframes"],
                "preparation": "managed_complete_environment_after_user_confirmation",
            },
            "remotion": {
                "requirement": "required_for_complete_environment",
                "selection": "agent_selected_after_capability_discovery",
            },
            "hyperframes": {
                "requirement": "required_for_complete_environment",
                "selection": "agent_selected_after_capability_discovery",
            },
        },
        "complete_production_environment": {
            "profile_id": production_plan["profile"]["id"],
            "display_name_zh": production_plan["profile"]["display_name_zh"],
            "status": "ready" if complete_environment_ready else "not_ready",
            "components": production_components,
            "single_user_confirmation": True,
            "repair_command": "golden-key-workbuddy runtime prepare --confirm-download --json",
            "errors": production_plan["errors"],
        },
        "ffmpeg": ffmpeg_runtime,
        "hyperframes": hyperframes_runtime,
        "node": node_runtime,
        "python": {
            "available": True,
            "executable": sys.executable,
            "minimum": "3.10",
            "supported": python_supported,
            "version": ".".join(str(part) for part in sys.version_info[:3]),
        },
        "python_packages": {
            "ready": not missing_python_packages,
            "required": list(REQUIRED_PYTHON_PACKAGES),
            "missing": missing_python_packages,
            "inspection": "local_module_discovery_only",
        },
        "remotion": remotion_runtime,
    }

    warnings = []
    if missing_python_packages:
        warnings.append(
            "Python runtime packages are incomplete: "
            + ", ".join(missing_python_packages)
        )
    if not runtime["ffmpeg"]["available"]:
        warnings.append(
            "FFmpeg is required for compose and local media tools but is not available"
        )
    if production_plan["status"] != "ready":
        missing_components = [
            name for name, ready in production_components.items() if not ready
        ]
        warnings.append(
            "Complete video production environment is not ready: "
            + ", ".join(missing_components)
        )
    elif not complete_environment_ready:
        failed_probes = [
            name
            for name, report in (
                ("ffmpeg", ffmpeg_runtime),
                ("node", node_runtime),
                ("remotion", remotion_runtime),
                ("hyperframes", hyperframes_runtime),
            )
            if not report["available"]
        ]
        warnings.append(
            "Complete video production environment failed executable probes: "
            + ", ".join(failed_probes)
        )

    return {
        "status": "fail" if errors else ("degraded" if warnings else "pass"),
        "repo_root": str(repo_root),
        "core": core,
        "authority": authority,
        "pipelines": {
            "available": available,
            "missing": missing,
            "expected_count": len(EXPECTED_PIPELINES),
        },
        "storage": {
            "data_root": str(data_root),
            "policy": "standard_user_location_with_override",
            "created": create_dirs and all(path.is_dir() for path in directories.values()),
            "directories": {name: str(path) for name, path in directories.items()},
        },
        "mcp": {
            "status": "optional",
            "role": "optional deterministic local stdio execution adapter",
            "canonical_fallback": "golden-key-workbuddy CLI",
            "real_workbuddy_comparison": "pass",
        },
        "claims": {
            "install_ready": False,
            "offline_adapter_ready": False,
            "real_workbuddy_accepted": False,
        },
        "runtime": runtime,
        "network_calls_attempted": 0,
        "provider_calls_attempted": 0,
        "warnings": warnings,
        "errors": errors,
    }


def format_doctor_report(report: dict[str, Any]) -> str:
    lines = [
        f"Golden Key WorkBuddy doctor: {report['status'].upper()}",
        f"Core: {report['core']['tag']} / {report['core']['contract_id']}",
        f"Pipelines: {len(report['pipelines']['available'])}/{report['pipelines']['expected_count']}",
        f"Data root: {report['storage']['data_root']}",
        f"Python: {report['runtime']['python']['version']}",
        (
            "Python packages: ready"
            if report["runtime"]["python_packages"]["ready"]
            else "Python packages missing: "
            + ", ".join(report["runtime"]["python_packages"]["missing"])
        ),
        f"Node: {'available' if report['runtime']['node']['available'] else 'missing'}",
        f"FFmpeg: {'available' if report['runtime']['ffmpeg']['available'] else 'missing'}",
        "Complete production environment: "
        + report["runtime"]["complete_production_environment"]["status"],
        "Runtime roles: Python, FFmpeg, Node, Remotion, and HyperFrames are prepared "
        "together after one user confirmation; the Agent selects the composition engine.",
        "MCP: optional local stdio adapter; CLI remains the canonical fallback.",
    ]
    lines.extend(f"WARNING: {message}" for message in report.get("warnings", []))
    lines.extend(f"ERROR: {message}" for message in report["errors"])
    return "\n".join(lines)
