from __future__ import annotations

import json
import os
import shutil
import socket
import subprocess
import sys
import threading
from pathlib import Path

from golden_key_openmontage_workbuddy.cli import main
from tests.workbuddy.test_w2_runtime import _advance_project_to_script


ROOT = Path(__file__).resolve().parents[2]


def _run_workbuddy_cli(
    python: str, args: list[str], *, cwd: Path, environment: dict[str, str]
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [python, "-m", "golden_key_openmontage_workbuddy", *args],
        cwd=cwd,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )


def test_local_tool_python_subprocess_inherits_the_offline_network_guard(
    tmp_path: Path, capsys, monkeypatch
) -> None:
    from tools.base_tool import (
        BaseTool,
        ResourceProfile,
        ToolResult,
        ToolRuntime,
        ToolStatus,
    )
    from tools.tool_registry import registry

    accepted = threading.Event()
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    listener.settimeout(1)
    port = listener.getsockname()[1]

    def accept_probe() -> None:
        try:
            connection, _ = listener.accept()
        except OSError:
            return
        accepted.set()
        connection.close()

    probe = threading.Thread(target=accept_probe, daemon=True)
    probe.start()

    class PythonSubprocessProbeTool(BaseTool):
        name = "scene_detect"
        capability = "analysis"
        provider = "test-python-subprocess"
        runtime = ToolRuntime.LOCAL
        input_schema = {"type": "object"}
        resource_profile = ResourceProfile(network_required=False)

        def get_status(self):
            return ToolStatus.AVAILABLE

        def execute(self, inputs):
            completed = subprocess.run(
                [
                    sys.executable,
                    "-c",
                    (
                        "import socket; "
                        f"socket.create_connection(('127.0.0.1', {port}), timeout=1).close()"
                    ),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            return ToolResult(
                success=completed.returncode == 0,
                error=(completed.stderr or completed.stdout).strip() or None,
            )

    fake_tool = PythonSubprocessProbeTool()
    original_get = registry.get
    monkeypatch.setattr(
        registry,
        "get",
        lambda name: fake_tool if name == "scene_detect" else original_get(name),
    )
    data_root, artifacts_dir = _advance_project_to_script(tmp_path, capsys)
    inputs_file = artifacts_dir / "python-subprocess-network-probe.json"
    inputs_file.write_text("{}\n", encoding="utf-8")

    try:
        exit_code = main(
            [
                "tool",
                "execute",
                "--repo-root",
                str(ROOT),
                "--data-root",
                str(data_root),
                "--project-id",
                "tool-project",
                "--name",
                "scene_detect",
                "--inputs-file",
                str(inputs_file),
                "--json",
            ]
        )
        payload = json.loads(capsys.readouterr().out)
    finally:
        listener.close()
        probe.join(timeout=2)

    assert exit_code == 1
    assert payload["status"] == "fail"
    assert "subprocess network access is blocked" in payload["errors"][0]
    assert accepted.is_set() is False
    assert payload["provider_calls_attempted"] == 0


def test_local_tool_node_subprocess_inherits_the_offline_network_guard(
    tmp_path: Path, capsys, monkeypatch
) -> None:
    from tools.base_tool import (
        BaseTool,
        ResourceProfile,
        ToolResult,
        ToolRuntime,
        ToolStatus,
    )
    from tools.tool_registry import registry

    node = shutil.which("node")
    assert node is not None, "W3 requires the Node runtime checked by doctor"
    accepted = threading.Event()
    listener = socket.socket()
    listener.bind(("127.0.0.1", 0))
    listener.listen(1)
    listener.settimeout(1)
    port = listener.getsockname()[1]

    def accept_probe() -> None:
        try:
            connection, _ = listener.accept()
        except OSError:
            return
        accepted.set()
        connection.close()

    probe = threading.Thread(target=accept_probe, daemon=True)
    probe.start()

    class NodeSubprocessProbeTool(BaseTool):
        name = "scene_detect"
        capability = "analysis"
        provider = "test-node-subprocess"
        runtime = ToolRuntime.LOCAL
        input_schema = {"type": "object"}
        resource_profile = ResourceProfile(network_required=False)

        def get_status(self):
            return ToolStatus.AVAILABLE

        def execute(self, inputs):
            completed = subprocess.run(
                [
                    node,
                    "-e",
                    (
                        "const net=require('node:net');"
                        f"const s=net.createConnection({{host:'127.0.0.1',port:{port}}},()=>{{s.end();process.exit(0)}});"
                        "s.on('error',e=>{console.error(e.message);process.exit(1)});"
                    ),
                ],
                capture_output=True,
                text=True,
                check=False,
            )
            return ToolResult(
                success=completed.returncode == 0,
                error=(completed.stderr or completed.stdout).strip() or None,
            )

    fake_tool = NodeSubprocessProbeTool()
    original_get = registry.get
    monkeypatch.setattr(
        registry,
        "get",
        lambda name: fake_tool if name == "scene_detect" else original_get(name),
    )
    data_root, artifacts_dir = _advance_project_to_script(tmp_path, capsys)
    inputs_file = artifacts_dir / "node-subprocess-network-probe.json"
    inputs_file.write_text("{}\n", encoding="utf-8")

    try:
        exit_code = main(
            [
                "tool",
                "execute",
                "--repo-root",
                str(ROOT),
                "--data-root",
                str(data_root),
                "--project-id",
                "tool-project",
                "--name",
                "scene_detect",
                "--inputs-file",
                str(inputs_file),
                "--json",
            ]
        )
        payload = json.loads(capsys.readouterr().out)
    finally:
        listener.close()
        probe.join(timeout=2)

    assert exit_code == 1
    assert payload["status"] == "fail"
    assert "subprocess network access is blocked" in payload["errors"][0]
    assert accepted.is_set() is False
    assert payload["provider_calls_attempted"] == 0


def test_local_tool_exception_redacts_environment_secrets_from_output_and_task(
    tmp_path: Path, capsys, monkeypatch
) -> None:
    from tools.base_tool import BaseTool, ResourceProfile, ToolRuntime, ToolStatus
    from tools.tool_registry import registry

    canary = "w3-secret-must-never-escape"
    monkeypatch.setenv("DASHSCOPE_API_KEY", canary)

    class SecretLeakingProbeTool(BaseTool):
        name = "scene_detect"
        capability = "analysis"
        provider = "test-secret-redaction"
        runtime = ToolRuntime.LOCAL
        input_schema = {"type": "object"}
        resource_profile = ResourceProfile(network_required=False)

        def get_status(self):
            return ToolStatus.AVAILABLE

        def execute(self, inputs):
            raise RuntimeError(f"provider rejected credential {canary}")

    fake_tool = SecretLeakingProbeTool()
    original_get = registry.get
    monkeypatch.setattr(
        registry,
        "get",
        lambda name: fake_tool if name == "scene_detect" else original_get(name),
    )
    data_root, artifacts_dir = _advance_project_to_script(tmp_path, capsys)
    inputs_file = artifacts_dir / "secret-redaction-probe.json"
    inputs_file.write_text("{}\n", encoding="utf-8")
    assert main(
        [
            "task",
            "submit",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "tool-project",
            "--name",
            "scene_detect",
            "--inputs-file",
            str(inputs_file),
            "--json",
        ]
    ) == 0
    task_id = json.loads(capsys.readouterr().out)["task"]["task_id"]

    exit_code = main(
        [
            "task",
            "run",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "tool-project",
            "--task-id",
            task_id,
            "--json",
        ]
    )
    output = capsys.readouterr().out
    task_text = (
        data_root / "Jobs" / "tool-project" / f"{task_id}.json"
    ).read_text(encoding="utf-8")

    assert exit_code == 1
    assert canary not in output
    assert canary not in task_text
    assert "[REDACTED]" in output
    assert "[REDACTED]" in task_text
    payload = json.loads(output)
    assert payload["provider_calls_attempted"] == 0


def test_cli_schema_error_redacts_secret_before_output(
    tmp_path: Path, capsys, monkeypatch
) -> None:
    from tools.base_tool import BaseTool, ResourceProfile, ToolRuntime, ToolStatus
    from tools.tool_registry import registry

    canary = "w3-schema-secret-must-never-escape"
    monkeypatch.setenv("VOLCENGINE_API_KEY", canary)

    class SchemaProbeTool(BaseTool):
        name = "scene_detect"
        capability = "analysis"
        provider = "test-schema-redaction"
        runtime = ToolRuntime.LOCAL
        input_schema = {
            "type": "object",
            "properties": {"credential": {"type": "integer"}},
            "required": ["credential"],
        }
        resource_profile = ResourceProfile(network_required=False)

        def get_status(self):
            return ToolStatus.AVAILABLE

        def execute(self, inputs):
            raise AssertionError("schema-invalid input must not execute")

    fake_tool = SchemaProbeTool()
    original_get = registry.get
    monkeypatch.setattr(
        registry,
        "get",
        lambda name: fake_tool if name == "scene_detect" else original_get(name),
    )
    data_root, artifacts_dir = _advance_project_to_script(tmp_path, capsys)
    inputs_file = artifacts_dir / "schema-secret-probe.json"
    inputs_file.write_text(
        json.dumps({"credential": canary}), encoding="utf-8"
    )

    exit_code = main(
        [
            "tool",
            "execute",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "tool-project",
            "--name",
            "scene_detect",
            "--inputs-file",
            str(inputs_file),
            "--json",
        ]
    )
    output = capsys.readouterr().out

    assert exit_code == 1
    assert canary not in output
    assert "[REDACTED]" in output
    assert json.loads(output)["provider_calls_attempted"] == 0


def test_mcp_tool_result_redacts_nested_secret(tmp_path: Path, capsys, monkeypatch) -> None:
    from golden_key_openmontage_workbuddy.mcp_server import WorkBuddyMcpServer
    from tools.base_tool import (
        BaseTool,
        ResourceProfile,
        ToolResult,
        ToolRuntime,
        ToolStatus,
    )
    from tools.tool_registry import registry

    canary = "opaque-mcp-value-must-never-escape"

    class McpResultProbeTool(BaseTool):
        name = "scene_detect"
        capability = "analysis"
        provider = "test-mcp-redaction"
        runtime = ToolRuntime.LOCAL
        input_schema = {"type": "object"}
        resource_profile = ResourceProfile(network_required=False)

        def get_status(self):
            return ToolStatus.AVAILABLE

        def execute(self, inputs):
            return ToolResult(
                success=False,
                data={"nested": {"credential": canary}},
                error=f"Bearer {canary}",
            )

    fake_tool = McpResultProbeTool()
    original_get = registry.get
    monkeypatch.setattr(
        registry,
        "get",
        lambda name: fake_tool if name == "scene_detect" else original_get(name),
    )
    data_root, artifacts_dir = _advance_project_to_script(tmp_path, capsys)
    inputs_file = artifacts_dir / "mcp-secret-probe.json"
    inputs_file.write_text("{}\n", encoding="utf-8")

    result = WorkBuddyMcpServer(ROOT, data_root).call_tool(
        "golden_key_tool_execute",
        {
            "project_id": "tool-project",
            "name": "scene_detect",
            "inputs_file": str(inputs_file),
            "ack_agent_skills": [],
        },
    )
    serialized = json.dumps(result, ensure_ascii=False)

    assert result["isError"] is True
    assert canary not in serialized
    assert "[REDACTED]" in serialized
    assert result["structuredContent"]["provider_calls_attempted"] == 0


def test_offline_adapter_operates_when_golden_key_saas_repo_is_unavailable(
    tmp_path: Path,
) -> None:
    missing_saas_root = tmp_path / "golden-key-saas-must-not-exist"
    data_root = tmp_path / "data"
    outside_repo = tmp_path / "outside-repo"
    outside_repo.mkdir()
    environment = os.environ.copy()
    environment["GOLDEN_KEY_SAAS_REPO_ROOT"] = str(missing_saas_root)
    environment["GOLDEN_KEY_PRIVATE_CORE_ROOT"] = str(missing_saas_root)
    environment["PYTHONPATH"] = str(ROOT)
    environment["PYTHONDONTWRITEBYTECODE"] = "1"

    context = _run_workbuddy_cli(
        sys.executable,
        ["context", "--repo-root", str(ROOT), "--json"],
        cwd=outside_repo,
        environment=environment,
    )
    created = _run_workbuddy_cli(
        sys.executable,
        [
            "project",
            "create",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "saas-absent",
            "--title",
            "SaaS absent isolation probe",
            "--pipeline",
            "golden-key-product-marketing",
            "--json",
        ],
        cwd=outside_repo,
        environment=environment,
    )

    assert missing_saas_root.exists() is False
    assert context.returncode == 0, context.stderr
    context_payload = json.loads(context.stdout)
    assert context_payload["authority"]["invocation_model"] == "direct_agent"
    assert context_payload["authority"]["nested_agent_host_allowed"] is False
    assert context_payload["provider_calls_attempted"] == 0
    assert created.returncode == 0, created.stderr
    created_payload = json.loads(created.stdout)
    assert created_payload["status"] == "pass"
    assert created_payload["pipeline_selected_by"] == "workbuddy_agent"
    assert created_payload["provider_calls_attempted"] == 0
