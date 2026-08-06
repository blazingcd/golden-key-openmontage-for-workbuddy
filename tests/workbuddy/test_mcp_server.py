from __future__ import annotations

import io
import json
from pathlib import Path

from golden_key_openmontage_workbuddy.mcp_server import (
    TOOLS,
    WorkBuddyMcpServer,
    serve_stdio,
)


ROOT = Path(__file__).resolve().parents[2]


def test_mcp_tools_are_deterministic_wrappers_with_structured_schemas() -> None:
    names = [tool["name"] for tool in TOOLS]

    assert len(names) == len(set(names)) == 17
    assert names[:4] == [
        "golden_key_doctor",
        "golden_key_context",
        "golden_key_pipelines",
        "golden_key_config_inspect",
    ]
    assert "golden_key_task_submit" in names
    assert "golden_key_tool_execute" in names
    assert "golden_key_task_status" in names
    assert "golden_key_task_run" in names
    assert "golden_key_task_cancel" in names
    assert "golden_key_task_recover" in names
    task_run = next(tool for tool in TOOLS if tool["name"] == "golden_key_task_run")
    timeout_schema = task_run["inputSchema"]["properties"]["timeout_seconds"]
    assert timeout_schema == {
        "type": "number",
        "exclusiveMinimum": 0,
        "maximum": 86400,
    }
    assert "timeout_seconds" not in task_run["inputSchema"]["required"]
    for tool in TOOLS:
        assert tool["inputSchema"]["type"] == "object"
        assert tool["inputSchema"]["additionalProperties"] is False
        assert tool["annotations"]["openWorldHint"] is False


def test_mcp_context_preserves_direct_agent_authority_without_provider_calls(
    tmp_path: Path,
) -> None:
    server = WorkBuddyMcpServer(ROOT, tmp_path)

    result = server.call_tool("golden_key_context", {})

    assert result["isError"] is False
    report = result["structuredContent"]
    assert report["status"] == "pass"
    assert report["authority"]["invocation_model"] == "direct_agent"
    assert report["authority"]["nested_agent_host_allowed"] is False
    assert report["authority"]["pipeline_selection_actor"] == "workbuddy_agent"
    assert report["selected_pipeline"] is None
    assert report["provider_calls_attempted"] == 0


def test_mcp_stdio_handshake_lists_tools_and_returns_structured_context(
    tmp_path: Path,
) -> None:
    requests = [
        {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "initialize",
            "params": {
                "protocolVersion": "2025-06-18",
                "capabilities": {},
                "clientInfo": {"name": "test", "version": "1"},
            },
        },
        {"jsonrpc": "2.0", "method": "notifications/initialized"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}},
        {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {"name": "golden_key_context", "arguments": {}},
        },
    ]
    source = io.StringIO("".join(json.dumps(item) + "\n" for item in requests))
    sink = io.StringIO()

    assert (
        serve_stdio(
            WorkBuddyMcpServer(ROOT, tmp_path),
            input_stream=source,
            output_stream=sink,
        )
        == 0
    )

    responses = [json.loads(line) for line in sink.getvalue().splitlines()]
    assert [response["id"] for response in responses] == [1, 2, 3]
    assert responses[0]["result"]["protocolVersion"] == "2025-06-18"
    assert responses[0]["result"]["capabilities"] == {
        "tools": {"listChanged": False}
    }
    assert len(responses[1]["result"]["tools"]) == 17
    assert (
        responses[2]["result"]["structuredContent"]["authority"][
            "nested_agent_host_allowed"
        ]
        is False
    )


def test_mcp_rejects_unknown_or_incomplete_tool_arguments(tmp_path: Path) -> None:
    server = WorkBuddyMcpServer(ROOT, tmp_path)

    output = io.StringIO()
    requests = io.StringIO(
        json.dumps(
            {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "tools/call",
                "params": {
                    "name": "golden_key_task_status",
                    "arguments": {"project_id": "demo", "unexpected": True},
                },
            }
        )
        + "\n"
    )

    serve_stdio(server, input_stream=requests, output_stream=output)

    response = json.loads(output.getvalue())
    assert response["error"]["code"] == -32602
    assert "Unknown tool arguments" in response["error"]["message"]


def test_mcp_task_status_failure_is_structured_and_does_not_retry(
    tmp_path: Path,
) -> None:
    server = WorkBuddyMcpServer(ROOT, tmp_path)

    result = server.call_tool(
        "golden_key_task_status",
        {"project_id": "missing", "task_id": "missing"},
    )

    assert result["isError"] is True
    report = result["structuredContent"]
    assert report["status"] == "fail"
    assert report["tool_calls_attempted"] == 0
    assert report["provider_calls_attempted"] == 0
    assert report["network_calls_attempted"] == 0
