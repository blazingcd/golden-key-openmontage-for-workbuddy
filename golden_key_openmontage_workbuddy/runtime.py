from __future__ import annotations

import json
import re
import socket
from contextlib import contextmanager
from pathlib import Path
from typing import Any

from lib.checkpoint import (
    get_latest_checkpoint,
    get_next_stage,
    init_project,
    write_checkpoint,
)
from lib.pipeline_loader import load_pipeline
from schemas.artifacts import ARTIFACT_NAMES, validate_artifact

from .doctor import EXPECTED_PIPELINES


PROJECT_ID_PATTERN = re.compile(r"^[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?$")


class RuntimeContractError(ValueError):
    """The WorkBuddy request violates the deterministic adapter contract."""


LOCAL_TOOL_RUNTIMES = {"local", "local_gpu"}


@contextmanager
def _deny_local_tool_network():
    """Fail closed if a declared local Tool attempts socket access."""

    def blocked(*args, **kwargs):
        raise RuntimeContractError(
            "local-only Tool network access is blocked by the WorkBuddy runtime"
        )

    originals = {
        "create_connection": socket.create_connection,
        "getaddrinfo": socket.getaddrinfo,
        "connect": socket.socket.connect,
        "connect_ex": socket.socket.connect_ex,
        "sendto": socket.socket.sendto,
    }
    socket.create_connection = blocked
    socket.getaddrinfo = blocked
    socket.socket.connect = blocked
    socket.socket.connect_ex = blocked
    socket.socket.sendto = blocked
    try:
        yield
    finally:
        socket.create_connection = originals["create_connection"]
        socket.getaddrinfo = originals["getaddrinfo"]
        socket.socket.connect = originals["connect"]
        socket.socket.connect_ex = originals["connect_ex"]
        socket.socket.sendto = originals["sendto"]


def _validated_project_id(project_id: str) -> str:
    if not PROJECT_ID_PATTERN.fullmatch(project_id):
        raise RuntimeContractError(
            "project_id must be 1-64 lowercase letters, digits, or hyphens"
        )
    return project_id


def _projects_root(data_root: Path) -> Path:
    return Path(data_root).resolve() / "Projects"


def _contained_path(path: Path, root: Path) -> Path:
    resolved = Path(path).resolve()
    try:
        resolved.relative_to(Path(root).resolve())
    except ValueError as exc:
        raise RuntimeContractError(f"path is outside the allowed project root: {path}") from exc
    return resolved


def _is_path_parameter(name: str) -> bool:
    return name in {"path", "paths", "output"} or name.endswith(
        ("_path", "_paths", "_dir")
    )


def _contained_tool_inputs(
    inputs: dict[str, Any], *, project_dir: Path, input_schema: dict[str, Any]
) -> dict[str, Any]:
    """Resolve schema-declared path parameters inside the project workspace."""

    normalized = dict(inputs)
    properties = input_schema.get("properties") or {}
    for name in properties:
        if name not in normalized or not _is_path_parameter(name):
            continue
        raw_value = normalized[name]
        values = raw_value if isinstance(raw_value, list) else [raw_value]
        if not all(isinstance(value, str) for value in values):
            raise RuntimeContractError(f"tool path parameter {name!r} must be text")
        resolved_values: list[str] = []
        for value in values:
            candidate = Path(value)
            if not candidate.is_absolute():
                candidate = project_dir / candidate
            resolved_values.append(str(_contained_path(candidate, project_dir)))
        normalized[name] = (
            resolved_values if isinstance(raw_value, list) else resolved_values[0]
        )
    return normalized


def build_context_report(repo_root: Path) -> dict[str, Any]:
    """Expose the frozen direct-agent context without making Agent decisions."""

    repo_root = Path(repo_root).resolve()
    guide_path = repo_root / "AGENT_GUIDE.md"
    pipelines = [
        name
        for name in EXPECTED_PIPELINES
        if (repo_root / "pipeline_defs" / f"{name}.yaml").is_file()
    ]
    errors: list[str] = []
    if not guide_path.is_file():
        errors.append("AGENT_GUIDE.md is missing")
    missing = sorted(set(EXPECTED_PIPELINES) - set(pipelines))
    if missing:
        errors.append(f"missing Golden Key pipelines: {', '.join(missing)}")

    return {
        "status": "fail" if errors else "pass",
        "repo_root": str(repo_root),
        "agent_guide": str(guide_path),
        "authority": {
            "invocation_model": "direct_agent",
            "nested_agent_host_allowed": False,
            "pipeline_selection_actor": "workbuddy_agent",
        },
        "selected_pipeline": None,
        "pipelines": pipelines,
        "provider_calls_attempted": 0,
        "errors": errors,
    }


def build_pipeline_catalog(repo_root: Path) -> dict[str, Any]:
    """Return declarative contracts for the four pipelines without selecting one."""

    repo_root = Path(repo_root).resolve()
    definitions = repo_root / "pipeline_defs"
    pipelines: list[dict[str, Any]] = []
    errors: list[str] = []
    for name in EXPECTED_PIPELINES:
        try:
            manifest = load_pipeline(name, definitions)
        except Exception as exc:
            errors.append(f"cannot load pipeline {name}: {exc}")
            continue
        pipelines.append(
            {
                "name": name,
                "description": manifest.get("description", "").strip(),
                "stability": manifest.get("stability"),
                "stages": [
                    {
                        "name": stage["name"],
                        "skill": stage.get("skill"),
                        "produces": list(stage.get("produces", [])),
                        "human_approval_default": bool(
                            stage.get("human_approval_default", False)
                        ),
                    }
                    for stage in manifest["stages"]
                ],
            }
        )
    return {
        "status": "fail" if errors else "pass",
        "selection_performed": False,
        "selection_actor": "workbuddy_agent",
        "pipelines": pipelines,
        "provider_calls_attempted": 0,
        "errors": errors,
    }


def create_project(
    repo_root: Path,
    data_root: Path,
    *,
    project_id: str,
    title: str,
    pipeline: str,
) -> dict[str, Any]:
    """Create a project only after WorkBuddy supplies its selected Pipeline."""

    project_id = _validated_project_id(project_id)
    if pipeline not in EXPECTED_PIPELINES:
        raise RuntimeContractError(
            "pipeline must be one of the four Golden Key WorkBuddy pipelines"
        )
    load_pipeline(pipeline, Path(repo_root).resolve() / "pipeline_defs")
    projects_root = _projects_root(data_root)
    marker_path = projects_root / project_id / "project.json"
    existed = marker_path.exists()
    if existed:
        try:
            marker = json.loads(marker_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise RuntimeContractError(f"invalid existing project marker: {exc}") from exc
        if marker.get("pipeline_type") != pipeline:
            raise RuntimeContractError(
                f"project {project_id} is already bound to "
                f"{marker.get('pipeline_type')!r}"
            )
        project_dir = marker_path.parent
    else:
        project_dir = init_project(
            project_id,
            title=title,
            pipeline_type=pipeline,
            pipeline_dir=projects_root,
        )
    return {
        "status": "pass",
        "created": not existed,
        "project_id": project_id,
        "project_dir": str(project_dir.resolve()),
        "pipeline": pipeline,
        "pipeline_selected_by": "workbuddy_agent",
        "provider_calls_attempted": 0,
        "errors": [],
    }


def build_project_status(data_root: Path, *, project_id: str) -> dict[str, Any]:
    project_id = _validated_project_id(project_id)
    projects_root = _projects_root(data_root)
    project_dir = projects_root / project_id
    marker_path = project_dir / "project.json"
    if not marker_path.is_file():
        raise RuntimeContractError(f"project not found: {project_id}")
    try:
        marker = json.loads(marker_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeContractError(f"invalid project marker: {exc}") from exc
    pipeline = marker.get("pipeline_type")
    if pipeline not in EXPECTED_PIPELINES:
        raise RuntimeContractError("project is not bound to a Golden Key Pipeline")
    latest = get_latest_checkpoint(projects_root, project_id)
    return {
        "status": "pass",
        "project_id": project_id,
        "project_dir": str(project_dir.resolve()),
        "title": marker.get("title"),
        "pipeline": pipeline,
        "next_stage": get_next_stage(projects_root, project_id, pipeline),
        "latest_checkpoint": latest,
        "provider_calls_attempted": 0,
        "errors": [],
    }


def validate_project_artifact(
    data_root: Path,
    *,
    project_id: str,
    artifact_name: str,
    input_path: Path,
) -> dict[str, Any]:
    project_id = _validated_project_id(project_id)
    if artifact_name not in ARTIFACT_NAMES:
        raise RuntimeContractError(f"unknown artifact schema: {artifact_name}")
    project_dir = _projects_root(data_root) / project_id
    if not (project_dir / "project.json").is_file():
        raise RuntimeContractError(f"project not found: {project_id}")
    artifact_dir = project_dir / "artifacts"
    path = _contained_path(input_path, artifact_dir)
    if not path.is_file():
        raise RuntimeContractError(f"artifact file not found: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeContractError(f"invalid artifact JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise RuntimeContractError("artifact JSON must be an object")
    try:
        validate_artifact(artifact_name, data)
    except Exception as exc:
        raise RuntimeContractError(
            f"artifact {artifact_name} failed schema validation: {exc}"
        ) from exc
    return {
        "status": "pass",
        "project_id": project_id,
        "artifact_name": artifact_name,
        "artifact_path": str(path),
        "schema_valid": True,
        "provider_calls_attempted": 0,
        "errors": [],
    }


def submit_checkpoint(
    data_root: Path,
    *,
    project_id: str,
    stage: str,
    checkpoint_status: str,
    artifacts_file: Path,
    human_approved: bool = False,
) -> dict[str, Any]:
    """Submit a native Core checkpoint after bounded project-local validation."""

    project_id = _validated_project_id(project_id)
    projects_root = _projects_root(data_root)
    project_dir = projects_root / project_id
    marker_path = project_dir / "project.json"
    if not marker_path.is_file():
        raise RuntimeContractError(f"project not found: {project_id}")
    try:
        marker = json.loads(marker_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeContractError(f"invalid project marker: {exc}") from exc
    pipeline = marker.get("pipeline_type")
    if pipeline not in EXPECTED_PIPELINES:
        raise RuntimeContractError("project is not bound to a Golden Key Pipeline")

    artifacts_path = _contained_path(artifacts_file, project_dir / "artifacts")
    if not artifacts_path.is_file():
        raise RuntimeContractError(f"artifacts file not found: {artifacts_path}")
    try:
        artifacts = json.loads(artifacts_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeContractError(f"invalid artifacts JSON: {exc}") from exc
    if not isinstance(artifacts, dict):
        raise RuntimeContractError("artifacts file must contain a JSON object")

    if checkpoint_status in {"awaiting_human", "completed"}:
        manifest = load_pipeline(pipeline)
        stage_contract = next(
            (item for item in manifest["stages"] if item["name"] == stage), None
        )
        if stage_contract is None:
            raise RuntimeContractError(
                f"stage {stage!r} is not declared by Pipeline {pipeline!r}"
            )
        missing_artifacts = sorted(
            set(stage_contract.get("produces", [])) - set(artifacts)
        )
        if missing_artifacts:
            raise RuntimeContractError(
                "missing manifest-produced artifacts: "
                + ", ".join(missing_artifacts)
            )

    try:
        checkpoint_path = write_checkpoint(
            projects_root,
            project_id,
            stage,
            checkpoint_status,
            artifacts,
            pipeline_type=pipeline,
            human_approved=human_approved,
        )
    except Exception as exc:
        raise RuntimeContractError(f"checkpoint rejected: {exc}") from exc
    checkpoint = json.loads(checkpoint_path.read_text(encoding="utf-8"))
    return {
        "status": "pass",
        "project_id": project_id,
        "pipeline": pipeline,
        "stage": stage,
        "checkpoint_status": checkpoint_status,
        "checkpoint_path": str(checkpoint_path.resolve()),
        "human_approval_required": checkpoint["human_approval_required"],
        "human_approved": checkpoint["human_approved"],
        "provider_calls_attempted": 0,
        "errors": [],
    }


def inspect_current_stage(
    repo_root: Path, data_root: Path, *, project_id: str
) -> dict[str, Any]:
    """Resolve the next native Stage contract; never rank or select a Pipeline."""

    status = build_project_status(data_root, project_id=project_id)
    stage_name = status["next_stage"]
    if stage_name is None:
        return {
            "status": "pass",
            "project_id": project_id,
            "pipeline": status["pipeline"],
            "stage": None,
            "pipeline_complete": True,
            "selection_performed": False,
            "provider_calls_attempted": 0,
            "errors": [],
        }
    repo_root = Path(repo_root).resolve()
    manifest = load_pipeline(status["pipeline"], repo_root / "pipeline_defs")
    stage = next(
        (item for item in manifest["stages"] if item["name"] == stage_name), None
    )
    if stage is None:
        raise RuntimeContractError(
            f"stage {stage_name!r} is missing from Pipeline {status['pipeline']!r}"
        )
    skill_ref = stage.get("skill")
    if not skill_ref:
        raise RuntimeContractError(f"stage {stage_name!r} has no director Skill")
    skill_path = _contained_path(
        repo_root / "skills" / f"{skill_ref}.md", repo_root / "skills"
    )
    if not skill_path.is_file():
        raise RuntimeContractError(f"stage Skill not found: {skill_path}")
    return {
        "status": "pass",
        "project_id": project_id,
        "pipeline": status["pipeline"],
        "stage": stage_name,
        "pipeline_complete": False,
        "skill": skill_path.as_posix(),
        "produces": list(stage.get("produces", [])),
        "tools_available": list(stage.get("tools_available", [])),
        "human_approval_default": bool(
            stage.get("human_approval_default", False)
        ),
        "review_focus": list(stage.get("review_focus", [])),
        "success_criteria": list(stage.get("success_criteria", [])),
        "selection_performed": False,
        "provider_calls_attempted": 0,
        "errors": [],
    }


def build_stage_tool_catalog(
    repo_root: Path, data_root: Path, *, project_id: str
) -> dict[str, Any]:
    """Discover only tools allowed by the project's current native Stage."""

    stage = inspect_current_stage(repo_root, data_root, project_id=project_id)
    if stage.get("pipeline_complete"):
        return {
            **stage,
            "tools": [],
        }

    from tools.tool_registry import registry

    registry.ensure_discovered()
    tools: list[dict[str, Any]] = []
    missing: list[str] = []
    for name in stage["tools_available"]:
        tool = registry.get(name)
        if tool is None:
            missing.append(name)
            continue
        runtime_value = getattr(tool.runtime, "value", tool.runtime)
        runtime = str(runtime_value)
        network_required = bool(tool.resource_profile.network_required)
        if runtime not in LOCAL_TOOL_RUNTIMES or network_required:
            status = "authorization_required"
            execution_policy = "blocked_provider_authorization"
        else:
            status = tool.get_status().value
        if status not in {"available", "authorization_required"}:
            execution_policy = "blocked_unavailable"
        elif status == "available":
            execution_policy = "allowed_local"
        tools.append(
            {
                "name": name,
                "status": status,
                "capability": tool.capability,
                "provider": tool.provider,
                "runtime": runtime,
                "network_required": network_required,
                "execution_policy": execution_policy,
                "input_schema": tool.input_schema or {},
                "side_effects": list(tool.side_effects or []),
                "agent_skills": list(tool.agent_skills or []),
                "install_instructions": tool.install_instructions or "",
            }
        )
    if missing:
        raise RuntimeContractError(
            "manifest tools are missing from the Tool Registry: "
            + ", ".join(missing)
        )
    return {
        "status": "pass",
        "project_id": project_id,
        "pipeline": stage["pipeline"],
        "stage": stage["stage"],
        "pipeline_complete": False,
        "tools": tools,
        "selection_performed": False,
        "provider_calls_attempted": 0,
        "errors": [],
    }


def execute_stage_tool(
    repo_root: Path,
    data_root: Path,
    *,
    project_id: str,
    tool_name: str,
    inputs_file: Path,
    acknowledged_agent_skills: list[str] | None = None,
) -> dict[str, Any]:
    """Execute a deterministic tool only inside its native Stage allowance."""

    stage = inspect_current_stage(repo_root, data_root, project_id=project_id)
    if stage.get("pipeline_complete"):
        raise RuntimeContractError("pipeline is complete; no Stage tool can run")
    if tool_name not in stage["tools_available"]:
        raise RuntimeContractError(
            f"tool {tool_name!r} is not allowed by current Stage {stage['stage']}"
        )
    from tools.tool_registry import registry

    registry.ensure_discovered()
    tool = registry.get(tool_name)
    if tool is None:
        raise RuntimeContractError(
            f"manifest tool {tool_name!r} is missing from the Tool Registry"
        )
    runtime_value = getattr(tool.runtime, "value", tool.runtime)
    runtime = str(runtime_value)
    network_required = bool(tool.resource_profile.network_required)
    if runtime not in LOCAL_TOOL_RUNTIMES or network_required:
        raise RuntimeContractError(
            f"tool {tool_name!r} runtime {runtime!r} requires explicit Provider "
            "authorization; this offline entry refuses it before execution"
        )
    if tool.get_status().value != "available":
        raise RuntimeContractError(
            f"tool {tool_name!r} is unavailable: {tool.install_instructions}"
        )
    missing_skills = sorted(
        set(tool.agent_skills or []) - set(acknowledged_agent_skills or [])
    )
    if missing_skills:
        raise RuntimeContractError(
            "required Layer 3 Skills were not acknowledged: "
            + ", ".join(missing_skills)
        )

    project_dir = _projects_root(data_root) / _validated_project_id(project_id)
    request_path = _contained_path(inputs_file, project_dir / "artifacts")
    if not request_path.is_file():
        raise RuntimeContractError(f"tool inputs file not found: {request_path}")
    try:
        inputs = json.loads(request_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeContractError(f"invalid tool inputs JSON: {exc}") from exc
    if not isinstance(inputs, dict):
        raise RuntimeContractError("tool inputs file must contain a JSON object")

    try:
        import jsonschema

        jsonschema.validate(inputs, tool.input_schema or {"type": "object"})
    except Exception as exc:
        raise RuntimeContractError(
            f"tool {tool_name!r} inputs failed schema validation: {exc}"
        ) from exc
    normalized_inputs = _contained_tool_inputs(
        inputs, project_dir=project_dir, input_schema=tool.input_schema or {}
    )
    estimated_cost = float(tool.estimate_cost(normalized_inputs) or 0.0)
    if estimated_cost > 0:
        raise RuntimeContractError(
            f"tool {tool_name!r} estimates ${estimated_cost:.6f}; explicit Provider "
            "authorization is required before execution"
        )

    try:
        with _deny_local_tool_network():
            result = tool.execute(normalized_inputs)
    except Exception as exc:
        return {
            "status": "fail",
            "project_id": project_id,
            "pipeline": stage["pipeline"],
            "stage": stage["stage"],
            "tool": tool_name,
            "tool_calls_attempted": 1,
            "provider_calls_attempted": 0,
            "cost_usd": 0,
            "errors": [f"local tool execution failed: {exc}"],
        }

    artifact_paths: list[str] = []
    output_errors: list[str] = []
    for path in result.artifacts:
        candidate = Path(path)
        if not candidate.is_absolute():
            candidate = project_dir / candidate
        try:
            artifact_paths.append(str(_contained_path(candidate, project_dir)))
        except RuntimeContractError as exc:
            output_errors.append(f"tool returned an unsafe artifact path: {exc}")
    actual_cost = float(result.cost_usd or 0.0)
    result_payload = {
        "success": bool(result.success),
        "data": result.data,
        "artifacts": artifact_paths,
        "error": result.error,
        "duration_seconds": result.duration_seconds,
        "seed": result.seed,
        "model": result.model,
    }
    errors: list[str] = list(output_errors)
    if actual_cost > 0:
        errors.append(
            f"local-only contract violation: tool reported ${actual_cost:.6f} cost"
        )
    if not result.success:
        errors.append(result.error or "tool returned an unsuccessful result")
    return {
        "status": "fail" if errors else "pass",
        "project_id": project_id,
        "pipeline": stage["pipeline"],
        "stage": stage["stage"],
        "tool": tool_name,
        "tool_calls_attempted": 1,
        "provider_calls_attempted": 0,
        "cost_usd": actual_cost,
        "result": result_payload,
        "errors": errors,
    }
