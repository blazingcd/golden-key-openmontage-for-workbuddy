from __future__ import annotations

import json
import socket
import subprocess
import threading
from pathlib import Path

from golden_key_openmontage_workbuddy.cli import main
from tests.workbuddy.test_w2_runtime import (
    _advance_project_to_assets,
    _advance_project_to_script,
)


ROOT = Path(__file__).resolve().parents[2]


def test_task_submit_persists_one_idempotent_queued_local_tool_task(
    tmp_path: Path, capsys
) -> None:
    data_root, artifacts_dir = _advance_project_to_script(tmp_path, capsys)
    inputs_file = artifacts_dir / "scene-detect-task-inputs.json"
    inputs_file.write_text(
        json.dumps(
            {
                "input_path": str(artifacts_dir / "source.mp4"),
                "output_path": str(artifacts_dir / "source-scenes.json"),
            }
        ),
        encoding="utf-8",
    )
    argv = [
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
        "--ack-agent-skill",
        "ffmpeg",
        "--json",
    ]

    assert main(argv) == 0
    submitted = json.loads(capsys.readouterr().out)
    assert submitted["status"] == "pass"
    assert submitted["created"] is True
    assert submitted["task"]["state"] == "queued"
    assert submitted["task"]["cancel_mode"] == "before_execution_only"
    assert submitted["task"]["tool"] == "scene_detect"
    assert submitted["task"]["attempt_count"] == 0
    assert submitted["tool_calls_attempted"] == 0
    assert submitted["provider_calls_attempted"] == 0
    task_id = submitted["task"]["task_id"]
    task_path = data_root / "Jobs" / "tool-project" / f"{task_id}.json"
    assert task_path.is_file()
    assert json.loads(task_path.read_text(encoding="utf-8")) == submitted["task"]

    assert main(argv) == 0
    repeated = json.loads(capsys.readouterr().out)
    assert repeated["created"] is False
    assert repeated["idempotent_replay"] is True
    assert repeated["task"]["task_id"] == task_id
    assert repeated["task"]["state"] == "queued"
    assert repeated["tool_calls_attempted"] == 0


def test_task_status_reads_the_persisted_task_without_reexecuting(
    tmp_path: Path, capsys
) -> None:
    data_root, artifacts_dir = _advance_project_to_script(tmp_path, capsys)
    inputs_file = artifacts_dir / "status-inputs.json"
    inputs_file.write_text(
        json.dumps(
            {
                "input_path": str(artifacts_dir / "source.mp4"),
                "output_path": str(artifacts_dir / "source-scenes.json"),
            }
        ),
        encoding="utf-8",
    )
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
            "--ack-agent-skill",
            "ffmpeg",
            "--json",
        ]
    ) == 0
    task_id = json.loads(capsys.readouterr().out)["task"]["task_id"]

    assert main(
        [
            "task",
            "status",
            "--data-root",
            str(data_root),
            "--project-id",
            "tool-project",
            "--task-id",
            task_id,
            "--json",
        ]
    ) == 0
    status = json.loads(capsys.readouterr().out)
    assert status["status"] == "pass"
    assert status["task"]["task_id"] == task_id
    assert status["task"]["state"] == "queued"
    assert status["task"]["attempt_count"] == 0
    assert status["terminal"] is False
    assert status["tool_calls_attempted"] == 0
    assert status["provider_calls_attempted"] == 0


def test_task_cancel_changes_only_a_queued_task_and_is_idempotent(
    tmp_path: Path, capsys
) -> None:
    data_root, artifacts_dir = _advance_project_to_script(tmp_path, capsys)
    inputs_file = artifacts_dir / "cancel-inputs.json"
    inputs_file.write_text(
        json.dumps(
            {
                "input_path": str(artifacts_dir / "source.mp4"),
                "output_path": str(artifacts_dir / "must-not-exist.json"),
            }
        ),
        encoding="utf-8",
    )
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
            "--ack-agent-skill",
            "ffmpeg",
            "--json",
        ]
    ) == 0
    task_id = json.loads(capsys.readouterr().out)["task"]["task_id"]
    argv = [
        "task",
        "cancel",
        "--data-root",
        str(data_root),
        "--project-id",
        "tool-project",
        "--task-id",
        task_id,
        "--json",
    ]

    assert main(argv) == 0
    cancelled = json.loads(capsys.readouterr().out)
    assert cancelled["status"] == "pass"
    assert cancelled["cancelled"] is True
    assert cancelled["idempotent_replay"] is False
    assert cancelled["task"]["state"] == "cancelled"
    assert cancelled["task"]["attempt_count"] == 0
    assert cancelled["tool_calls_attempted"] == 0
    assert not (artifacts_dir / "must-not-exist.json").exists()

    assert main(argv) == 0
    repeated = json.loads(capsys.readouterr().out)
    assert repeated["cancelled"] is True
    assert repeated["idempotent_replay"] is True
    assert repeated["task"]["state"] == "cancelled"


def test_task_run_executes_once_and_persists_a_terminal_result(
    tmp_path: Path, capsys
) -> None:
    data_root, artifacts_dir = _advance_project_to_script(tmp_path, capsys)
    source = artifacts_dir.parent / "assets" / "video" / "source.mp4"
    source.parent.mkdir(parents=True, exist_ok=True)
    completed = subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-f",
            "lavfi",
            "-i",
            "color=c=black:s=64x64:r=10:d=1",
            "-c:v",
            "mpeg4",
            "-y",
            str(source),
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    output = artifacts_dir / "task-scenes.json"
    inputs_file = artifacts_dir / "run-inputs.json"
    inputs_file.write_text(
        json.dumps(
            {
                "input_path": str(source),
                "method": "content",
                "min_scene_length_seconds": 0.1,
                "output_path": str(output),
            }
        ),
        encoding="utf-8",
    )
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
            "--ack-agent-skill",
            "ffmpeg",
            "--json",
        ]
    ) == 0
    task_id = json.loads(capsys.readouterr().out)["task"]["task_id"]
    argv = [
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

    assert main(argv) == 0
    executed = json.loads(capsys.readouterr().out)
    assert executed["status"] == "pass"
    assert executed["idempotent_replay"] is False
    assert executed["task"]["state"] == "succeeded"
    assert executed["task"]["attempt_count"] == 1
    assert executed["task"]["result"]["tool"] == "scene_detect"
    assert executed["tool_calls_attempted"] == 1
    assert executed["provider_calls_attempted"] == 0
    assert output.is_file()
    output_bytes = output.read_bytes()

    assert main(argv) == 0
    repeated = json.loads(capsys.readouterr().out)
    assert repeated["status"] == "pass"
    assert repeated["idempotent_replay"] is True
    assert repeated["task"]["state"] == "succeeded"
    assert repeated["task"]["attempt_count"] == 1
    assert repeated["tool_calls_attempted"] == 0
    assert output.read_bytes() == output_bytes

    assert main(
        [
            "task",
            "status",
            "--data-root",
            str(data_root),
            "--project-id",
            "tool-project",
            "--task-id",
            task_id,
            "--json",
        ]
    ) == 0
    status = json.loads(capsys.readouterr().out)
    assert status["terminal"] is True
    assert status["task"]["state"] == "succeeded"


def test_task_run_blocks_a_misdeclared_local_tool_network_attempt(
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

    class MisdeclaredLocalTool(BaseTool):
        name = "scene_detect"
        capability = "analysis"
        provider = "test-misdeclared"
        runtime = ToolRuntime.LOCAL
        input_schema = {"type": "object"}
        resource_profile = ResourceProfile(network_required=False)

        def get_status(self):
            return ToolStatus.AVAILABLE

        def execute(self, inputs):
            socket.create_connection(("example.invalid", 443), timeout=0.01)
            return ToolResult(success=True)

    fake_tool = MisdeclaredLocalTool()
    original_get = registry.get
    monkeypatch.setattr(
        registry,
        "get",
        lambda name: fake_tool if name == "scene_detect" else original_get(name),
    )
    network_attempts: list[tuple] = []

    def record_network(*args, **kwargs):
        network_attempts.append(args)
        return object()

    monkeypatch.setattr(socket, "create_connection", record_network)
    data_root, artifacts_dir = _advance_project_to_script(tmp_path, capsys)
    inputs_file = artifacts_dir / "blocked-network-inputs.json"
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

    assert main(
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
    ) == 1
    blocked = json.loads(capsys.readouterr().out)
    assert blocked["task"]["state"] == "failed"
    assert blocked["tool_calls_attempted"] == 1
    assert blocked["provider_calls_attempted"] == 0
    assert "network access is blocked" in blocked["errors"][0]
    assert network_attempts == []


def test_task_cancel_reports_running_local_tool_as_not_safely_cancelable(
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

    started = threading.Event()
    release = threading.Event()

    class BlockingLocalTool(BaseTool):
        name = "scene_detect"
        capability = "analysis"
        provider = "test-blocking"
        runtime = ToolRuntime.LOCAL
        input_schema = {"type": "object"}
        resource_profile = ResourceProfile(network_required=False)

        def get_status(self):
            return ToolStatus.AVAILABLE

        def execute(self, inputs):
            started.set()
            assert release.wait(timeout=5)
            return ToolResult(success=True)

    fake_tool = BlockingLocalTool()
    original_get = registry.get
    monkeypatch.setattr(
        registry,
        "get",
        lambda name: fake_tool if name == "scene_detect" else original_get(name),
    )
    data_root, artifacts_dir = _advance_project_to_script(tmp_path, capsys)
    inputs_file = artifacts_dir / "blocking-inputs.json"
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
    run_argv = [
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
    worker = threading.Thread(target=lambda: main(run_argv), daemon=True)
    worker.start()
    assert started.wait(timeout=5)

    assert main(
        [
            "task",
            "status",
            "--data-root",
            str(data_root),
            "--project-id",
            "tool-project",
            "--task-id",
            task_id,
            "--json",
        ]
    ) == 0
    active = json.loads(capsys.readouterr().out)
    assert active["task"]["state"] == "running"
    assert active["execution_active"] is True
    assert active["recovery_required"] is False
    assert active["cancel_available"] is False

    assert main(
        [
            "task",
            "cancel",
            "--data-root",
            str(data_root),
            "--project-id",
            "tool-project",
            "--task-id",
            task_id,
            "--json",
        ]
    ) == 1
    refusal = json.loads(capsys.readouterr().out)
    assert "not safely cancelable after execution starts" in refusal["errors"][0]
    persisted = json.loads(
        (data_root / "Jobs" / "tool-project" / f"{task_id}.json").read_text(
            encoding="utf-8"
        )
    )
    assert persisted["state"] == "running"

    release.set()
    worker.join(timeout=5)
    assert not worker.is_alive()
    capsys.readouterr()


def test_task_submit_blocks_hybrid_provider_path_before_status_or_network(
    tmp_path: Path, capsys, monkeypatch
) -> None:
    data_root, artifacts_dir = _advance_project_to_assets(tmp_path, capsys)
    inputs_file = artifacts_dir / "blocked-provider-task.json"
    inputs_file.write_text('{"prompt": "must not run"}\n', encoding="utf-8")
    network_attempts: list[tuple] = []

    def reject_network(*args, **kwargs):
        network_attempts.append(args)
        raise AssertionError("network must not be reached")

    monkeypatch.setattr(socket, "create_connection", reject_network)
    monkeypatch.setattr(socket.socket, "connect", reject_network)

    assert main(
        [
            "task",
            "submit",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "provider-project",
            "--name",
            "video_selector",
            "--inputs-file",
            str(inputs_file),
            "--json",
        ]
    ) == 1
    blocked = json.loads(capsys.readouterr().out)
    assert "runtime 'hybrid' requires explicit Provider authorization" in blocked[
        "errors"
    ][0]
    assert blocked["tool_calls_attempted"] == 0
    assert blocked["provider_calls_attempted"] == 0
    assert blocked["network_calls_attempted"] == 0
    assert network_attempts == []
    jobs_dir = data_root / "Jobs" / "provider-project"
    assert not jobs_dir.exists()


def test_task_run_rejects_inputs_changed_after_submission(
    tmp_path: Path, capsys
) -> None:
    data_root, artifacts_dir = _advance_project_to_script(tmp_path, capsys)
    inputs_file = artifacts_dir / "immutable-inputs.json"
    inputs_file.write_text(
        json.dumps(
            {
                "input_path": str(artifacts_dir / "source.mp4"),
                "output_path": str(artifacts_dir / "must-not-exist.json"),
            }
        ),
        encoding="utf-8",
    )
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
            "--ack-agent-skill",
            "ffmpeg",
            "--json",
        ]
    ) == 0
    task_id = json.loads(capsys.readouterr().out)["task"]["task_id"]
    inputs_file.write_text('{"tampered": true}\n', encoding="utf-8")

    assert main(
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
    ) == 1
    refused = json.loads(capsys.readouterr().out)
    assert "inputs changed after task submission" in refused["errors"][0]
    assert refused["tool_calls_attempted"] == 0
    persisted = json.loads(
        (data_root / "Jobs" / "tool-project" / f"{task_id}.json").read_text(
            encoding="utf-8"
        )
    )
    assert persisted["state"] == "queued"
    assert persisted["attempt_count"] == 0
    assert not (artifacts_dir / "must-not-exist.json").exists()


def test_task_recover_marks_an_interrupted_execution_failed_without_retrying(
    tmp_path: Path, capsys
) -> None:
    data_root, artifacts_dir = _advance_project_to_script(tmp_path, capsys)
    inputs_file = artifacts_dir / "interrupted-inputs.json"
    inputs_file.write_text(
        json.dumps(
            {
                "input_path": str(artifacts_dir / "source.mp4"),
                "output_path": str(artifacts_dir / "must-not-exist.json"),
            }
        ),
        encoding="utf-8",
    )
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
            "--ack-agent-skill",
            "ffmpeg",
            "--json",
        ]
    ) == 0
    task_id = json.loads(capsys.readouterr().out)["task"]["task_id"]
    task_path = data_root / "Jobs" / "tool-project" / f"{task_id}.json"
    lock_path = task_path.with_suffix(".lock")
    task = json.loads(task_path.read_text(encoding="utf-8"))
    task["state"] = "running"
    task["attempt_count"] = 1
    task["runner_pid"] = 2_000_000_000
    task_path.write_text(json.dumps(task), encoding="utf-8")
    lock_path.write_text('{"pid": 2000000000}\n', encoding="utf-8")

    assert main(
        [
            "task",
            "status",
            "--data-root",
            str(data_root),
            "--project-id",
            "tool-project",
            "--task-id",
            task_id,
            "--json",
        ]
    ) == 0
    interrupted = json.loads(capsys.readouterr().out)
    assert interrupted["execution_active"] is False
    assert interrupted["recovery_required"] is True
    assert interrupted["recommended_action"] == "recover_interrupted_task"

    recover_argv = [
        "task",
        "recover",
        "--data-root",
        str(data_root),
        "--project-id",
        "tool-project",
        "--task-id",
        task_id,
        "--json",
    ]
    assert main(recover_argv) == 0
    recovered = json.loads(capsys.readouterr().out)
    assert recovered["recovered"] is True
    assert recovered["idempotent_replay"] is False
    assert recovered["task"]["state"] == "failed"
    assert "interrupted" in recovered["task"]["errors"][0]
    assert recovered["tool_calls_attempted"] == 0
    assert recovered["provider_calls_attempted"] == 0
    assert not lock_path.exists()
    assert not (artifacts_dir / "must-not-exist.json").exists()

    assert main(recover_argv) == 0
    replay = json.loads(capsys.readouterr().out)
    assert replay["idempotent_replay"] is True
    assert replay["task"]["state"] == "failed"


def test_task_status_rejects_a_tampered_persisted_task_identity(
    tmp_path: Path, capsys
) -> None:
    data_root, artifacts_dir = _advance_project_to_script(tmp_path, capsys)
    inputs_file = artifacts_dir / "identity-inputs.json"
    inputs_file.write_text(
        json.dumps(
            {
                "input_path": str(artifacts_dir / "source.mp4"),
                "output_path": str(artifacts_dir / "source-scenes.json"),
            }
        ),
        encoding="utf-8",
    )
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
            "--ack-agent-skill",
            "ffmpeg",
            "--json",
        ]
    ) == 0
    task_id = json.loads(capsys.readouterr().out)["task"]["task_id"]
    task_path = data_root / "Jobs" / "tool-project" / f"{task_id}.json"
    task = json.loads(task_path.read_text(encoding="utf-8"))
    task["tool"] = "frame_sampler"
    task_path.write_text(json.dumps(task), encoding="utf-8")

    assert main(
        [
            "task",
            "status",
            "--data-root",
            str(data_root),
            "--project-id",
            "tool-project",
            "--task-id",
            task_id,
            "--json",
        ]
    ) == 1
    refused = json.loads(capsys.readouterr().out)
    assert "task identity digest does not match" in refused["errors"][0]
    assert refused["tool_calls_attempted"] == 0
