from __future__ import annotations

import hashlib
import json
import math
import os
import re
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from .runtime import (
    LOCAL_TOOL_RUNTIMES,
    RuntimeContractError,
    _contained_path,
    _contained_tool_inputs,
    _projects_root,
    _validated_project_id,
    inspect_current_stage,
    execute_stage_tool,
)
from .security import redact_payload, redact_text


TASK_ID_PATTERN = re.compile(r"^[0-9a-f]{32}$")
TERMINAL_TASK_STATES = {"succeeded", "failed", "cancelled"}
EXECUTION_SLOT_FILE = ".execution.lock"
DEFAULT_TASK_TIMEOUT_SECONDS = 3600.0
MAX_TASK_TIMEOUT_SECONDS = 86400.0
TIMEOUT_ENFORCEMENT = "observe_only_no_forced_termination"


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _validated_timeout_seconds(value: Any) -> float:
    try:
        timeout_seconds = float(value)
    except (TypeError, ValueError) as exc:
        raise RuntimeContractError("timeout_seconds must be a number") from exc
    if not math.isfinite(timeout_seconds) or not (
        0 < timeout_seconds <= MAX_TASK_TIMEOUT_SECONDS
    ):
        raise RuntimeContractError(
            f"timeout_seconds must be greater than 0 and at most {MAX_TASK_TIMEOUT_SECONDS:g}"
        )
    return timeout_seconds


def _task_timeout_exceeded(task: dict[str, Any]) -> bool:
    deadline = task.get("deadline_at")
    if deadline is None:
        return False
    if not isinstance(deadline, str):
        raise RuntimeContractError("persisted task deadline_at must be an ISO timestamp")
    try:
        deadline_at = datetime.fromisoformat(deadline)
    except ValueError as exc:
        raise RuntimeContractError(
            "persisted task deadline_at must be an ISO timestamp"
        ) from exc
    if deadline_at.tzinfo is None:
        raise RuntimeContractError("persisted task deadline_at must include a timezone")
    completed_at = task.get("completed_at")
    observed_at = datetime.now(timezone.utc)
    if isinstance(completed_at, str):
        try:
            observed_at = datetime.fromisoformat(completed_at)
        except ValueError as exc:
            raise RuntimeContractError(
                "persisted task completed_at must be an ISO timestamp"
            ) from exc
    return observed_at > deadline_at


def _write_new_json(path: Path, payload: dict[str, Any]) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = redact_payload(payload)
    try:
        with path.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
    except FileExistsError:
        return False
    return True


def _write_json_atomic(path: Path, payload: dict[str, Any]) -> None:
    payload = redact_payload(payload)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        temporary.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


@contextmanager
def _exclusive_task_operation(task_path: Path):
    lock_path = task_path.with_suffix(".lock")
    try:
        with lock_path.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump({"pid": os.getpid(), "created_at": _utc_now()}, handle)
            handle.write("\n")
    except FileExistsError as exc:
        raise RuntimeContractError(
            "another operation already owns this task; retry status later"
        ) from exc
    try:
        yield
    finally:
        lock_path.unlink(missing_ok=True)


@contextmanager
def _exclusive_execution_slot(data_root: Path, task: dict[str, Any]):
    """Allow at most one local Tool execution for a WorkBuddy data root."""

    lock_path = Path(data_root).resolve() / "Jobs" / EXECUTION_SLOT_FILE
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    owner = {
        "pid": os.getpid(),
        "project_id": task["project_id"],
        "task_id": task["task_id"],
        "created_at": _utc_now(),
    }
    try:
        with lock_path.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(owner, handle, ensure_ascii=False)
            handle.write("\n")
    except FileExistsError as exc:
        try:
            active_owner = json.loads(lock_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            active_owner = {}
        owner_task = active_owner.get("task_id") or "unknown"
        owner_project = active_owner.get("project_id") or "unknown"
        raise RuntimeContractError(
            "cross-task concurrency limit of 1 reached; "
            f"task {owner_task} in project {owner_project} owns the execution slot"
        ) from exc
    try:
        yield
    finally:
        try:
            persisted_owner = json.loads(lock_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            persisted_owner = None
        if persisted_owner == owner:
            lock_path.unlink(missing_ok=True)


def _read_task(path: Path) -> dict[str, Any]:
    try:
        task = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeContractError(f"invalid persisted task: {exc}") from exc
    if not isinstance(task, dict):
        raise RuntimeContractError("persisted task must be a JSON object")
    if task.get("schema_version") != "1.0":
        raise RuntimeContractError("persisted task schema_version must be '1.0'")
    task_id = task.get("task_id")
    if not isinstance(task_id, str) or not TASK_ID_PATTERN.fullmatch(task_id):
        raise RuntimeContractError("persisted task has an invalid task_id")
    if _computed_task_id(task) != task_id:
        raise RuntimeContractError("task identity digest does not match persisted fields")
    return task


def _computed_task_id(task: dict[str, Any]) -> str:
    acknowledged = task.get("acknowledged_agent_skills")
    if not isinstance(acknowledged, list) or not all(
        isinstance(item, str) for item in acknowledged
    ):
        raise RuntimeContractError(
            "persisted task acknowledged_agent_skills must be a string list"
        )
    identity_fields = ("project_id", "pipeline", "stage", "tool", "inputs_sha256")
    if not all(isinstance(task.get(key), str) and task[key] for key in identity_fields):
        raise RuntimeContractError("persisted task identity fields are incomplete")
    identity = json.dumps(
        {
            "project_id": task["project_id"],
            "pipeline": task["pipeline"],
            "stage": task["stage"],
            "tool": task["tool"],
            "inputs_sha256": task["inputs_sha256"],
            "acknowledged_agent_skills": sorted(set(acknowledged)),
        },
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(identity).hexdigest()[:32]


def _task_path(data_root: Path, project_id: str, task_id: str) -> Path:
    project_id = _validated_project_id(project_id)
    if not TASK_ID_PATTERN.fullmatch(task_id):
        raise RuntimeContractError("task_id must be exactly 32 lowercase hex characters")
    return Path(data_root).resolve() / "Jobs" / project_id / f"{task_id}.json"


def _process_is_alive(pid: Any) -> bool:
    if not isinstance(pid, int) or pid <= 0:
        return False
    if pid == os.getpid():
        return True
    if os.name == "nt":
        import ctypes

        process = ctypes.windll.kernel32.OpenProcess(0x1000, False, pid)
        if not process:
            return False
        ctypes.windll.kernel32.CloseHandle(process)
        return True
    try:
        os.kill(pid, 0)
    except PermissionError:
        return True
    except OSError:
        return False
    return True


def _task_activity(task_path: Path, task: dict[str, Any]) -> tuple[bool, bool]:
    if task.get("state") != "running":
        return False, False
    lock_path = task_path.with_suffix(".lock")
    if not lock_path.is_file():
        return False, True
    try:
        lock = json.loads(lock_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return False, True
    active = _process_is_alive(lock.get("pid"))
    return active, not active


def _release_interrupted_execution_slot(
    data_root: Path, task: dict[str, Any]
) -> bool:
    lock_path = Path(data_root).resolve() / "Jobs" / EXECUTION_SLOT_FILE
    if not lock_path.is_file():
        return False
    try:
        owner = json.loads(lock_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeContractError(
            "persisted execution slot is invalid; refusing automatic deletion"
        ) from exc
    if not isinstance(owner, dict):
        raise RuntimeContractError(
            "persisted execution slot is invalid; refusing automatic deletion"
        )
    if owner.get("project_id") != task.get("project_id") or owner.get(
        "task_id"
    ) != task.get("task_id"):
        return False
    if _process_is_alive(owner.get("pid")):
        raise RuntimeContractError(
            "execution slot owner is still active; recovery is not allowed"
        )
    lock_path.unlink()
    return True


def get_tool_task_status(
    data_root: Path, *, project_id: str, task_id: str
) -> dict[str, Any]:
    task_path = _task_path(data_root, project_id, task_id)
    if not task_path.is_file():
        raise RuntimeContractError(f"task not found: {task_id}")
    task = _read_task(task_path)
    if task.get("task_id") != task_id or task.get("project_id") != project_id:
        raise RuntimeContractError("persisted task identity does not match its path")
    execution_active, recovery_required = _task_activity(task_path, task)
    state = task.get("state")
    timeout_exceeded = _task_timeout_exceeded(task)
    if recovery_required:
        recommended_action = "recover_interrupted_task"
    elif execution_active and timeout_exceeded:
        recommended_action = "wait_for_non_cancelable_execution"
    elif execution_active:
        recommended_action = "wait_or_query_status"
    elif state == "queued":
        recommended_action = "run_or_cancel"
    else:
        recommended_action = None
    return {
        "status": "pass",
        "task": task,
        "task_path": str(task_path),
        "terminal": state in TERMINAL_TASK_STATES,
        "execution_active": execution_active,
        "recovery_required": recovery_required,
        "cancel_available": state == "queued",
        "timeout_exceeded": timeout_exceeded,
        "timeout_enforcement": task.get("timeout_enforcement"),
        "recommended_action": recommended_action,
        "tool_calls_attempted": 0,
        "provider_calls_attempted": 0,
        "network_calls_attempted": 0,
        "errors": [],
    }


def cancel_tool_task(
    data_root: Path, *, project_id: str, task_id: str
) -> dict[str, Any]:
    task_path = _task_path(data_root, project_id, task_id)
    if not task_path.is_file():
        raise RuntimeContractError(f"task not found: {task_id}")
    running_error = (
        "task is already running and this Tool contract is not safely "
        "cancelable after execution starts"
    )
    if _read_task(task_path).get("state") == "running":
        raise RuntimeContractError(running_error)
    try:
        with _exclusive_task_operation(task_path):
            task = _read_task(task_path)
            state = task.get("state")
            replay = state == "cancelled"
            if state == "queued":
                task["state"] = "cancelled"
                task["updated_at"] = _utc_now()
                _write_json_atomic(task_path, task)
            elif not replay:
                if state == "running":
                    raise RuntimeContractError(running_error)
                raise RuntimeContractError(
                    f"task in state {state!r} cannot be cancelled"
                )
    except RuntimeContractError as exc:
        if _read_task(task_path).get("state") == "running":
            raise RuntimeContractError(running_error) from exc
        raise
    return {
        "status": "pass",
        "cancelled": True,
        "idempotent_replay": replay,
        "task": task,
        "task_path": str(task_path),
        "tool_calls_attempted": 0,
        "provider_calls_attempted": 0,
        "network_calls_attempted": 0,
        "errors": [],
    }


def run_tool_task(
    repo_root: Path,
    data_root: Path,
    *,
    project_id: str,
    task_id: str,
    timeout_seconds: float = DEFAULT_TASK_TIMEOUT_SECONDS,
) -> dict[str, Any]:
    timeout_seconds = _validated_timeout_seconds(timeout_seconds)
    task_path = _task_path(data_root, project_id, task_id)
    if not task_path.is_file():
        raise RuntimeContractError(f"task not found: {task_id}")

    with _exclusive_task_operation(task_path):
        task = _read_task(task_path)
        state = task.get("state")
        if state == "succeeded":
            return {
                "status": "pass",
                "idempotent_replay": True,
                "task": task,
                "task_path": str(task_path),
                "tool_calls_attempted": 0,
                "provider_calls_attempted": 0,
                "network_calls_attempted": 0,
                "errors": [],
            }
        if state in {"failed", "cancelled"}:
            return {
                "status": "fail",
                "idempotent_replay": True,
                "task": task,
                "task_path": str(task_path),
                "tool_calls_attempted": 0,
                "provider_calls_attempted": 0,
                "network_calls_attempted": 0,
                "errors": list(task.get("errors") or [f"task is {state}"]),
            }
        if state != "queued":
            raise RuntimeContractError(
                f"task in state {state!r} cannot start another execution"
            )

        project_dir = _projects_root(data_root) / _validated_project_id(project_id)
        request_path = _contained_path(
            Path(str(task.get("inputs_file", ""))), project_dir / "artifacts"
        )
        if not request_path.is_file():
            raise RuntimeContractError(f"tool inputs file not found: {request_path}")
        current_sha256 = hashlib.sha256(request_path.read_bytes()).hexdigest()
        if current_sha256 != task.get("inputs_sha256"):
            raise RuntimeContractError(
                "tool inputs changed after task submission; submit a new task"
            )

        with _exclusive_execution_slot(data_root, task):
            started_at = datetime.now(timezone.utc)
            deadline_at = started_at + timedelta(seconds=timeout_seconds)
            now = started_at.isoformat()
            task["state"] = "running"
            task["attempt_count"] = int(task.get("attempt_count", 0)) + 1
            task["started_at"] = now
            task["updated_at"] = now
            task["runner_pid"] = os.getpid()
            task["timeout_seconds"] = timeout_seconds
            task["deadline_at"] = deadline_at.isoformat()
            task["timeout_enforcement"] = TIMEOUT_ENFORCEMENT
            task["timeout_exceeded"] = False
            _write_json_atomic(task_path, task)

            try:
                execution = execute_stage_tool(
                    repo_root,
                    data_root,
                    project_id=project_id,
                    tool_name=str(task["tool"]),
                    inputs_file=request_path,
                    acknowledged_agent_skills=list(
                        task.get("acknowledged_agent_skills") or []
                    ),
                )
            except Exception as exc:
                execution = {
                    "status": "fail",
                    "tool_calls_attempted": 0,
                    "provider_calls_attempted": 0,
                    "cost_usd": 0,
                    "errors": [
                        redact_text(f"task execution contract failed: {exc}")
                    ],
                }

            execution = redact_payload(execution)

            finished_at = datetime.now(timezone.utc)
            finished = finished_at.isoformat()
            task["state"] = (
                "succeeded" if execution["status"] == "pass" else "failed"
            )
            task["updated_at"] = finished
            task["completed_at"] = finished
            task["timeout_exceeded"] = finished_at > deadline_at
            task["result"] = execution
            task["errors"] = list(execution.get("errors") or [])
            _write_json_atomic(task_path, task)

    return {
        "status": execution["status"],
        "idempotent_replay": False,
        "task": task,
        "task_path": str(task_path),
        "tool_calls_attempted": int(execution.get("tool_calls_attempted", 0)),
        "provider_calls_attempted": int(
            execution.get("provider_calls_attempted", 0)
        ),
        "network_calls_attempted": 0,
        "errors": list(execution.get("errors") or []),
    }


def recover_interrupted_tool_task(
    data_root: Path, *, project_id: str, task_id: str
) -> dict[str, Any]:
    task_path = _task_path(data_root, project_id, task_id)
    if not task_path.is_file():
        raise RuntimeContractError(f"task not found: {task_id}")
    task = _read_task(task_path)
    if task.get("state") == "failed" and task.get("recovered_from_interruption"):
        replay = True
    else:
        replay = False
        active, recovery_required = _task_activity(task_path, task)
        if active:
            raise RuntimeContractError(
                "task execution is still active; recovery is not allowed"
            )
        if not recovery_required:
            raise RuntimeContractError(
                f"task in state {task.get('state')!r} does not require recovery"
            )
        task_path.with_suffix(".lock").unlink(missing_ok=True)
        with _exclusive_task_operation(task_path):
            task = _read_task(task_path)
            if task.get("state") != "running":
                raise RuntimeContractError(
                    "task state changed before recovery; query status again"
                )
            now = _utc_now()
            task["state"] = "failed"
            task["updated_at"] = now
            task["completed_at"] = now
            task["recovered_from_interruption"] = True
            task["interrupted_runner_pid"] = task.pop("runner_pid", None)
            task["errors"] = [
                "task execution was interrupted; automatic retry is forbidden "
                "because local Tool side effects may be partial"
            ]
            _write_json_atomic(task_path, task)
    execution_slot_released = _release_interrupted_execution_slot(data_root, task)
    return {
        "status": "pass",
        "recovered": True,
        "idempotent_replay": replay,
        "execution_slot_released": execution_slot_released,
        "task": task,
        "task_path": str(task_path),
        "tool_calls_attempted": 0,
        "provider_calls_attempted": 0,
        "network_calls_attempted": 0,
        "errors": [],
    }


def submit_tool_task(
    repo_root: Path,
    data_root: Path,
    *,
    project_id: str,
    tool_name: str,
    inputs_file: Path,
    acknowledged_agent_skills: list[str] | None = None,
) -> dict[str, Any]:
    """Persist one validated local Tool request without executing it."""

    project_id = _validated_project_id(project_id)
    stage = inspect_current_stage(repo_root, data_root, project_id=project_id)
    if stage.get("pipeline_complete"):
        raise RuntimeContractError("pipeline is complete; no Tool task can be submitted")
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
            "authorization; this offline task entry refuses it before submission"
        )
    if tool.get_status().value != "available":
        raise RuntimeContractError(
            f"tool {tool_name!r} is unavailable: {tool.install_instructions}"
        )
    acknowledged = sorted(set(acknowledged_agent_skills or []))
    missing_skills = sorted(set(tool.agent_skills or []) - set(acknowledged))
    if missing_skills:
        raise RuntimeContractError(
            "required Layer 3 Skills were not acknowledged: "
            + ", ".join(missing_skills)
        )

    project_dir = _projects_root(data_root) / project_id
    request_path = _contained_path(inputs_file, project_dir / "artifacts")
    if not request_path.is_file():
        raise RuntimeContractError(f"tool inputs file not found: {request_path}")
    request_bytes = request_path.read_bytes()
    try:
        inputs = json.loads(request_bytes.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
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
            "authorization is required before task submission"
        )

    inputs_sha256 = hashlib.sha256(request_bytes).hexdigest()
    identity_fields = {
        "project_id": project_id,
        "pipeline": stage["pipeline"],
        "stage": stage["stage"],
        "tool": tool_name,
        "inputs_sha256": inputs_sha256,
        "acknowledged_agent_skills": acknowledged,
    }
    task_id = _computed_task_id(identity_fields)
    now = _utc_now()
    task = {
        "schema_version": "1.0",
        "task_id": task_id,
        "project_id": project_id,
        "pipeline": stage["pipeline"],
        "stage": stage["stage"],
        "tool": tool_name,
        "inputs_file": str(request_path),
        "inputs_sha256": inputs_sha256,
        "acknowledged_agent_skills": acknowledged,
        "state": "queued",
        "cancel_mode": "before_execution_only",
        "concurrency_limit": 1,
        "default_timeout_seconds": DEFAULT_TASK_TIMEOUT_SECONDS,
        "timeout_enforcement": TIMEOUT_ENFORCEMENT,
        "timeout_exceeded": False,
        "attempt_count": 0,
        "created_at": now,
        "updated_at": now,
        "result": None,
        "errors": [],
    }
    task_path = _task_path(data_root, project_id, task_id)
    created = _write_new_json(task_path, task)
    if not created:
        task = _read_task(task_path)
    return {
        "status": "pass",
        "created": created,
        "idempotent_replay": not created,
        "task": task,
        "task_path": str(task_path),
        "tool_calls_attempted": 0,
        "provider_calls_attempted": 0,
        "network_calls_attempted": 0,
        "errors": [],
    }
