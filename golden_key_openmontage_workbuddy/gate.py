from __future__ import annotations

import ast
from pathlib import Path
from typing import Any

from .doctor import build_doctor_report


FORBIDDEN_PATHS = (
    "lib/agent_host_authority.py",
    "lib/model_driven_agent_host.py",
    "lib/openai_compatible_transport.py",
    "tests/contracts/test_agent_host_authority.py",
    "tests/contracts/test_model_driven_agent_host.py",
    "tests/contracts/test_openai_compatible_transport.py",
)
FORBIDDEN_MODULE_TOKENS = (
    "agent_host_authority",
    "golden_key_short_video_agent",
    "model_driven_agent_host",
    "openai_compatible_transport",
    "saas_worker",
)


def _static_isolation_violations(repo_root: Path) -> list[dict[str, Any]]:
    runtime_root = repo_root / "golden_key_openmontage_workbuddy"
    if not runtime_root.is_dir():
        return []
    violations: list[dict[str, Any]] = []
    for path in sorted(runtime_root.rglob("*.py")):
        relative = path.relative_to(repo_root).as_posix()
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"), filename=relative)
        except (OSError, SyntaxError):
            violations.append({"line": 1, "module": "<unparseable>", "path": relative})
            continue
        imported: list[tuple[str, int]] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported.extend((alias.name, node.lineno) for alias in node.names)
            elif isinstance(node, ast.ImportFrom):
                base = node.module or ""
                imported.extend(
                    (f"{base}.{alias.name}".strip("."), node.lineno)
                    for alias in node.names
                )
        for module, line in imported:
            if any(token in module.lower() for token in FORBIDDEN_MODULE_TOKENS):
                violations.append(
                    {"line": line, "module": module, "path": relative}
                )
    return violations


def build_gate_report(repo_root: Path, data_root: Path) -> dict[str, Any]:
    repo_root = Path(repo_root).resolve()
    doctor = build_doctor_report(repo_root, data_root)
    present_forbidden = [
        relative for relative in FORBIDDEN_PATHS if (repo_root / relative).exists()
    ]
    skill_path = (
        repo_root / "workbuddy-skill" / "golden-key-openmontage" / "SKILL.md"
    )
    active_mcp_path = repo_root / ".workbuddy" / "mcp.json"
    isolation_violations = _static_isolation_violations(repo_root)
    errors = list(doctor["errors"])
    if present_forbidden:
        errors.append("forbidden Agent Host or transport paths are present")
    if not skill_path.is_file():
        errors.append("WorkBuddy Skill package is missing")
    if active_mcp_path.exists():
        errors.append("active MCP configuration is forbidden before the W2 decision Gate")
    if isolation_violations:
        errors.append("WorkBuddy runtime violates the direct-agent isolation boundary")

    return {
        "status": "fail" if errors else "pass",
        "doctor_status": doctor["status"],
        "skill": {
            "path": str(skill_path),
            "status": "present" if skill_path.is_file() else "missing",
        },
        "forbidden_paths": {
            "expected_absent": list(FORBIDDEN_PATHS),
            "present": present_forbidden,
        },
        "mcp": {
            "active_config_present": active_mcp_path.exists(),
            "decision_status": "pending",
        },
        "static_isolation": {"violations": isolation_violations},
        "provider_calls_attempted": 0,
        "errors": errors,
    }


def format_gate_report(report: dict[str, Any]) -> str:
    lines = [
        f"Golden Key WorkBuddy W1 Gate: {report['status'].upper()}",
        f"Doctor: {report['doctor_status']}",
        f"Skill: {report['skill']['status']}",
        f"Forbidden paths present: {len(report['forbidden_paths']['present'])}",
        "MCP: decision pending; no active configuration.",
    ]
    lines.extend(f"ERROR: {message}" for message in report["errors"])
    return "\n".join(lines)
