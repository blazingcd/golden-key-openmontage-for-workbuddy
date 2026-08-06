from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


EXPECTED_PIPELINES = (
    "golden-key-brand-company",
    "golden-key-lead-conversion",
    "golden-key-product-marketing",
    "golden-key-subject-ip",
)
EXPECTED_CONTRACT_ID = "golden-key-workbuddy-callable-core-v1"
EXPECTED_TAG = "golden-key-v0.3.21"
EXPECTED_SOURCE_COMMIT = "757ea3822e5f2eef7f341389983119021e827c8d"


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
    runtime = {
        "ffmpeg": _command_runtime("ffmpeg"),
        "node": _command_runtime("node"),
        "python": {
            "available": True,
            "executable": sys.executable,
            "minimum": "3.10",
            "supported": python_supported,
            "version": ".".join(str(part) for part in sys.version_info[:3]),
        },
    }

    return {
        "status": "fail" if errors else "pass",
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
            "policy": "prefer_d_drive_on_windows",
            "created": create_dirs and all(path.is_dir() for path in directories.values()),
            "directories": {name: str(path) for name, path in directories.items()},
        },
        "mcp": {
            "status": "decision_pending",
            "role": "optional deterministic local execution adapter",
        },
        "claims": {
            "install_ready": False,
            "offline_adapter_ready": False,
            "real_workbuddy_accepted": False,
        },
        "runtime": runtime,
        "provider_calls_attempted": 0,
        "errors": errors,
    }


def format_doctor_report(report: dict[str, Any]) -> str:
    lines = [
        f"Golden Key WorkBuddy doctor: {report['status'].upper()}",
        f"Core: {report['core']['tag']} / {report['core']['contract_id']}",
        f"Pipelines: {len(report['pipelines']['available'])}/{report['pipelines']['expected_count']}",
        f"Data root: {report['storage']['data_root']}",
        f"Python: {report['runtime']['python']['version']}",
        f"Node: {'available' if report['runtime']['node']['available'] else 'missing'}",
        f"FFmpeg: {'available' if report['runtime']['ffmpeg']['available'] else 'missing'}",
        "MCP: decision pending; WorkBuddy remains the only Agent.",
    ]
    lines.extend(f"ERROR: {message}" for message in report["errors"])
    return "\n".join(lines)
