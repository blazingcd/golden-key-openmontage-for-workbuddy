from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, TextIO

from .security import redact_payload, redact_text


SERVER_NAME = "golden-key-openmontage-workbuddy"
SERVER_VERSION = "0.1.0a0"
DEFAULT_PROTOCOL_VERSION = "2024-11-05"
SUPPORTED_PROTOCOL_VERSIONS = {
    "2024-11-05",
    "2025-03-26",
    "2025-06-18",
}


class McpRequestError(ValueError):
    def __init__(self, code: int, message: str) -> None:
        super().__init__(message)
        self.code = code


def _object_schema(
    properties: dict[str, Any] | None = None,
    *,
    required: tuple[str, ...] = (),
) -> dict[str, Any]:
    schema: dict[str, Any] = {
        "type": "object",
        "properties": properties or {},
        "additionalProperties": False,
    }
    if required:
        schema["required"] = list(required)
    return schema


STRING = {"type": "string", "minLength": 1}
BOOLEAN = {"type": "boolean"}
TIMEOUT_SECONDS = {"type": "number", "exclusiveMinimum": 0, "maximum": 86400}


def _tool(
    name: str,
    description: str,
    input_schema: dict[str, Any],
    *,
    read_only: bool,
    idempotent: bool,
) -> dict[str, Any]:
    return {
        "name": name,
        "description": description,
        "inputSchema": input_schema,
        "annotations": {
            "readOnlyHint": read_only,
            "destructiveHint": False,
            "idempotentHint": idempotent,
            "openWorldHint": False,
        },
    }


TOOLS = [
    _tool(
        "golden_key_doctor",
        "Check the locked callable Core, direct-agent authority, four Pipelines, local runtimes, and D-drive data layout without calling a Provider.",
        _object_schema({"create_dirs": BOOLEAN}),
        read_only=False,
        idempotent=True,
    ),
    _tool(
        "golden_key_context",
        "Read the authoritative direct-agent context. This never selects a Pipeline.",
        _object_schema(),
        read_only=True,
        idempotent=True,
    ),
    _tool(
        "golden_key_pipelines",
        "List the four callable Pipeline contracts without ranking or selecting one.",
        _object_schema(),
        read_only=True,
        idempotent=True,
    ),
    _tool(
        "golden_key_config_inspect",
        "Inspect the WorkBuddy conversation-model and Golden Key production-Provider boundary without reading credentials or contacting a Provider.",
        _object_schema(),
        read_only=True,
        idempotent=True,
    ),
    _tool(
        "golden_key_config_template",
        "Create the consumer-owned production Provider reference template under the configured D-drive data root. It stores environment-variable names only.",
        _object_schema(),
        read_only=False,
        idempotent=True,
    ),
    _tool(
        "golden_key_project_create",
        "Create a D-drive project bound to a Pipeline already selected by the WorkBuddy Agent.",
        _object_schema(
            {"project_id": STRING, "title": STRING, "pipeline": STRING},
            required=("project_id", "title", "pipeline"),
        ),
        read_only=False,
        idempotent=True,
    ),
    _tool(
        "golden_key_project_status",
        "Read a persisted WorkBuddy project without executing a Tool or Provider.",
        _object_schema({"project_id": STRING}, required=("project_id",)),
        read_only=True,
        idempotent=True,
    ),
    _tool(
        "golden_key_stage_inspect",
        "Read the next native Stage, Stage Skill, Artifact, Tool allowlist, and Human Gate for a project.",
        _object_schema({"project_id": STRING}, required=("project_id",)),
        read_only=True,
        idempotent=True,
    ),
    _tool(
        "golden_key_tool_list",
        "List only the current Stage's Tool Registry allowlist, input Schemas, and required Layer 3 Skills.",
        _object_schema({"project_id": STRING}, required=("project_id",)),
        read_only=True,
        idempotent=True,
    ),
    _tool(
        "golden_key_tool_execute",
        "Execute one current-Stage local, zero-network, zero-cost Tool after WorkBuddy has read every required Layer 3 Skill. Prefer the durable task tools for long-running work.",
        _object_schema(
            {
                "project_id": STRING,
                "name": STRING,
                "inputs_file": STRING,
                "ack_agent_skills": {"type": "array", "items": STRING, "uniqueItems": True},
            },
            required=("project_id", "name", "inputs_file", "ack_agent_skills"),
        ),
        read_only=False,
        idempotent=False,
    ),
    _tool(
        "golden_key_artifact_validate",
        "Validate a canonical Artifact JSON already stored inside the project artifacts directory.",
        _object_schema(
            {"project_id": STRING, "name": STRING, "input_file": STRING},
            required=("project_id", "name", "input_file"),
        ),
        read_only=True,
        idempotent=True,
    ),
    _tool(
        "golden_key_checkpoint_submit",
        "Submit a native Checkpoint after Artifact validation. Human-gated completion requires explicit prior approval.",
        _object_schema(
            {
                "project_id": STRING,
                "stage": STRING,
                "status": {
                    "type": "string",
                    "enum": ["in_progress", "awaiting_human", "completed", "failed"],
                },
                "artifacts_file": STRING,
                "human_approved": BOOLEAN,
            },
            required=("project_id", "stage", "status", "artifacts_file"),
        ),
        read_only=False,
        idempotent=True,
    ),
    _tool(
        "golden_key_task_submit",
        "Validate and queue an immutable local Tool request. This does not execute the Tool.",
        _object_schema(
            {
                "project_id": STRING,
                "name": STRING,
                "inputs_file": STRING,
                "ack_agent_skills": {"type": "array", "items": STRING, "uniqueItems": True},
            },
            required=("project_id", "name", "inputs_file", "ack_agent_skills"),
        ),
        read_only=False,
        idempotent=True,
    ),
    _tool(
        "golden_key_task_status",
        "Read a durable local Tool task without executing or retrying it.",
        _object_schema(
            {"project_id": STRING, "task_id": STRING},
            required=("project_id", "task_id"),
        ),
        read_only=True,
        idempotent=True,
    ),
    _tool(
        "golden_key_task_run",
        "Run one queued local, zero-network, zero-cost Tool task in the foreground. Only one task runs per data root. The timeout is observable and never claims forced termination of a blocking Core Tool.",
        _object_schema(
            {
                "project_id": STRING,
                "task_id": STRING,
                "timeout_seconds": TIMEOUT_SECONDS,
            },
            required=("project_id", "task_id"),
        ),
        read_only=False,
        idempotent=True,
    ),
    _tool(
        "golden_key_task_cancel",
        "Cancel a queued task only. A running blocking Tool is explicitly not claimed safely cancelable.",
        _object_schema(
            {"project_id": STRING, "task_id": STRING},
            required=("project_id", "task_id"),
        ),
        read_only=False,
        idempotent=True,
    ),
    _tool(
        "golden_key_task_recover",
        "Mark an interrupted Tool task failed without re-executing it or retrying unknown partial side effects.",
        _object_schema(
            {"project_id": STRING, "task_id": STRING},
            required=("project_id", "task_id"),
        ),
        read_only=False,
        idempotent=True,
    ),
]

TOOL_BY_NAME = {tool["name"]: tool for tool in TOOLS}


def _validate_arguments(tool_name: str, arguments: Any) -> dict[str, Any]:
    if not isinstance(arguments, dict):
        raise McpRequestError(-32602, "Tool arguments must be a JSON object.")
    schema = TOOL_BY_NAME[tool_name]["inputSchema"]
    properties = schema["properties"]
    unknown = sorted(set(arguments) - set(properties))
    if unknown:
        raise McpRequestError(-32602, f"Unknown tool arguments: {', '.join(unknown)}")
    missing = [name for name in schema.get("required", []) if name not in arguments]
    if missing:
        raise McpRequestError(-32602, f"Missing required tool arguments: {', '.join(missing)}")
    for name, value in arguments.items():
        expected = properties[name].get("type")
        if expected == "string" and (not isinstance(value, str) or not value):
            raise McpRequestError(-32602, f"Tool argument {name!r} must be a non-empty string.")
        if expected == "boolean" and not isinstance(value, bool):
            raise McpRequestError(-32602, f"Tool argument {name!r} must be a boolean.")
        if expected == "array":
            if not isinstance(value, list) or not all(isinstance(item, str) and item for item in value):
                raise McpRequestError(-32602, f"Tool argument {name!r} must be an array of non-empty strings.")
    return arguments


@dataclass(frozen=True)
class WorkBuddyMcpServer:
    repo_root: Path
    data_root: Path

    @classmethod
    def from_environment(cls) -> "WorkBuddyMcpServer":
        repo_root = Path(os.environ.get("GOLDEN_KEY_REPO_ROOT", Path.cwd()))
        data_root = Path(os.environ.get("GOLDEN_KEY_DATA_ROOT", "D:/WorkBuddyData"))
        return cls(repo_root=repo_root.resolve(), data_root=data_root.resolve())

    def initialize(self, params: dict[str, Any]) -> dict[str, Any]:
        requested = params.get("protocolVersion")
        protocol_version = (
            requested if requested in SUPPORTED_PROTOCOL_VERSIONS else DEFAULT_PROTOCOL_VERSION
        )
        return {
            "protocolVersion": protocol_version,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
            "instructions": (
                "WorkBuddy is the only Agent. Use Golden Key tools only after reading the "
                "golden-key-openmontage Skill and AGENT_GUIDE.md. The server never selects a "
                "Pipeline and never starts a nested Agent Host."
            ),
        }

    def call_tool(self, name: str, arguments: Any) -> dict[str, Any]:
        if name not in TOOL_BY_NAME:
            raise McpRequestError(-32602, f"Unknown Golden Key tool: {name}")
        args = _validate_arguments(name, arguments)
        report = redact_payload(self._dispatch(name, args))
        is_error = report.get("status") != "pass"
        return {
            "content": [
                {
                    "type": "text",
                    "text": json.dumps(report, ensure_ascii=False, indent=2),
                }
            ],
            "structuredContent": report,
            "isError": is_error,
        }

    def _dispatch(self, name: str, args: dict[str, Any]) -> dict[str, Any]:
        try:
            if name == "golden_key_doctor":
                from .doctor import build_doctor_report

                return build_doctor_report(
                    self.repo_root,
                    self.data_root,
                    create_dirs=args.get("create_dirs", False),
                )
            if name == "golden_key_context":
                from .runtime import build_context_report

                return build_context_report(self.repo_root)
            if name == "golden_key_pipelines":
                from .runtime import build_pipeline_catalog

                return build_pipeline_catalog(self.repo_root)
            if name == "golden_key_config_inspect":
                from .model_config import build_model_provider_report

                return build_model_provider_report(self.repo_root)
            if name == "golden_key_config_template":
                from .model_config import write_safe_provider_template

                return write_safe_provider_template(self.repo_root, self.data_root)
            if name == "golden_key_project_create":
                from .runtime import create_project

                return create_project(
                    self.repo_root,
                    self.data_root,
                    project_id=args["project_id"],
                    title=args["title"],
                    pipeline=args["pipeline"],
                )
            if name == "golden_key_project_status":
                from .runtime import build_project_status

                return build_project_status(self.data_root, project_id=args["project_id"])
            if name == "golden_key_stage_inspect":
                from .runtime import inspect_current_stage

                return inspect_current_stage(
                    self.repo_root, self.data_root, project_id=args["project_id"]
                )
            if name == "golden_key_tool_list":
                from .runtime import build_stage_tool_catalog

                return build_stage_tool_catalog(
                    self.repo_root, self.data_root, project_id=args["project_id"]
                )
            if name == "golden_key_tool_execute":
                from .runtime import execute_stage_tool

                return execute_stage_tool(
                    self.repo_root,
                    self.data_root,
                    project_id=args["project_id"],
                    tool_name=args["name"],
                    inputs_file=Path(args["inputs_file"]),
                    acknowledged_agent_skills=args["ack_agent_skills"],
                )
            if name == "golden_key_artifact_validate":
                from .runtime import validate_project_artifact

                return validate_project_artifact(
                    self.data_root,
                    project_id=args["project_id"],
                    artifact_name=args["name"],
                    input_path=Path(args["input_file"]),
                )
            if name == "golden_key_checkpoint_submit":
                from .runtime import submit_checkpoint

                return submit_checkpoint(
                    self.data_root,
                    project_id=args["project_id"],
                    stage=args["stage"],
                    checkpoint_status=args["status"],
                    artifacts_file=Path(args["artifacts_file"]),
                    human_approved=args.get("human_approved", False),
                )
            if name == "golden_key_task_submit":
                from .tasks import submit_tool_task

                return submit_tool_task(
                    self.repo_root,
                    self.data_root,
                    project_id=args["project_id"],
                    tool_name=args["name"],
                    inputs_file=Path(args["inputs_file"]),
                    acknowledged_agent_skills=args["ack_agent_skills"],
                )
            if name == "golden_key_task_status":
                from .tasks import get_tool_task_status

                return get_tool_task_status(
                    self.data_root,
                    project_id=args["project_id"],
                    task_id=args["task_id"],
                )
            if name == "golden_key_task_run":
                from .tasks import run_tool_task

                return run_tool_task(
                    self.repo_root,
                    self.data_root,
                    project_id=args["project_id"],
                    task_id=args["task_id"],
                    timeout_seconds=args.get("timeout_seconds", 3600.0),
                )
            if name == "golden_key_task_cancel":
                from .tasks import cancel_tool_task

                return cancel_tool_task(
                    self.data_root,
                    project_id=args["project_id"],
                    task_id=args["task_id"],
                )
            if name == "golden_key_task_recover":
                from .tasks import recover_interrupted_tool_task

                return recover_interrupted_tool_task(
                    self.data_root,
                    project_id=args["project_id"],
                    task_id=args["task_id"],
                )
            raise McpRequestError(-32602, f"Unknown Golden Key tool: {name}")
        except McpRequestError:
            raise
        except Exception as exc:
            return {
                "status": "fail",
                "tool_calls_attempted": 0,
                "provider_calls_attempted": 0,
                "network_calls_attempted": 0,
                "errors": [str(exc)],
            }

    def handle(self, request: Any) -> dict[str, Any] | None:
        if not isinstance(request, dict) or request.get("jsonrpc") != "2.0":
            raise McpRequestError(-32600, "Invalid JSON-RPC request.")
        method = request.get("method")
        if not isinstance(method, str):
            raise McpRequestError(-32600, "JSON-RPC method is required.")
        if "id" not in request:
            return None
        params = request.get("params", {})
        if not isinstance(params, dict):
            raise McpRequestError(-32602, "JSON-RPC params must be an object.")
        if method == "initialize":
            return self.initialize(params)
        if method == "ping":
            return {}
        if method == "tools/list":
            return {"tools": TOOLS}
        if method == "tools/call":
            name = params.get("name")
            if not isinstance(name, str):
                raise McpRequestError(-32602, "tools/call requires a tool name.")
            return self.call_tool(name, params.get("arguments", {}))
        if method == "resources/list":
            return {"resources": []}
        if method == "prompts/list":
            return {"prompts": []}
        if method == "logging/setLevel":
            return {}
        raise McpRequestError(-32601, f"Method not found: {method}")


def _response(request_id: Any, result: dict[str, Any]) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": request_id, "result": result}


def _error_response(request_id: Any, error: Exception) -> dict[str, Any]:
    code = error.code if isinstance(error, McpRequestError) else -32603
    return {
        "jsonrpc": "2.0",
        "id": request_id,
        "error": {"code": code, "message": redact_text(str(error))},
    }


def serve_stdio(
    server: WorkBuddyMcpServer | None = None,
    *,
    input_stream: TextIO = sys.stdin,
    output_stream: TextIO = sys.stdout,
) -> int:
    active_server = server or WorkBuddyMcpServer.from_environment()
    for line in input_stream:
        if not line.strip():
            continue
        request_id: Any = None
        try:
            request = json.loads(line)
            if isinstance(request, dict):
                request_id = request.get("id")
            result = active_server.handle(request)
            if result is None:
                continue
            payload = _response(request_id, result)
        except Exception as exc:
            payload = _error_response(request_id, exc)
        output_stream.write(
            json.dumps(
                redact_payload(payload),
                ensure_ascii=False,
                separators=(",", ":"),
            )
        )
        output_stream.write("\n")
        output_stream.flush()
    return 0


def main() -> int:
    return serve_stdio()


if __name__ == "__main__":
    raise SystemExit(main())
