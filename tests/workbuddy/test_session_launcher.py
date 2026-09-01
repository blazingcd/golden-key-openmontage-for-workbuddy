from __future__ import annotations

import hashlib
import io
import json
import os
import shutil
import stat
import subprocess
import sys
import threading
import time
from collections.abc import Mapping
from pathlib import Path
from types import MappingProxyType
from typing import Any

import pytest

from golden_key_openmontage_workbuddy import launch_session_tool
from golden_key_openmontage_workbuddy import fixed_child
from golden_key_openmontage_workbuddy import package_registration as registration
from golden_key_openmontage_workbuddy import session_launcher as launcher_module
from tests.workbuddy.test_package_registration import (
    COMMIT,
    RELEASE,
    _activate_missing,
    _inventory_entry,
    _make_candidate,
    _sha256,
    _sha256_bytes,
)


REQUEST_HASH = "c5b196bfe69c6a6db7073fb7fa7503a58837907e939fceeb5436fa7d19f80ce1"
RESULT_HASH = "8a96aceb463da2ea39549de44b06a765a3ac859260001ae277b99dbf2a8ca1b3"
SUCCESS_CODE = r'''import hashlib,json,pathlib,sys
r=json.load(sys.stdin)
p=pathlib.Path(r["executor_controls"]["result_root"])/"result.bin"
p.write_bytes(b"fixture-result")
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"SUCCEEDED","result_pointer":{"relative_path":"result.bin","sha256":hashlib.sha256(b"fixture-result").hexdigest(),"size":14},"error":None}
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode())'''
FAILED_CODE = r'''import json,sys
r=json.load(sys.stdin)
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"FAILED","result_pointer":None,"error":{"code":"FIXTURE","origin":"FIXTURE","message":"fixture failure"}}
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode())'''


def _canonical(value: dict[str, Any], *, newline: bool = True) -> bytes:
    raw = json.dumps(value, allow_nan=False, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return raw + (b"\n" if newline else b"")


def _lock_entry(path: Path, relative: str) -> dict[str, Any]:
    return {
        "path": f"workbuddy-core/{relative}", "source_path": relative,
        "sha256": _sha256(path), "size": path.stat().st_size,
        "source_mode": "100644", "apply_mode": "replace", "classification": "workbuddy_callable",
    }


def _seal_definition(definition: dict[str, Any]) -> None:
    body = dict(definition)
    body.pop("definition_sha256", None)
    definition["definition_sha256"] = hashlib.sha256(_canonical(body)).hexdigest()


def _add_package_file(candidate: Any, path: Path, relative: str, owner: str, *, locked: bool) -> None:
    manifest = candidate.manifest()
    manifest["files"].append(_inventory_entry(path, relative, owner))
    if owner == registration.REQUIRED_TOOLCHAIN_OWNER:
        manifest["required_toolchain"]["managed_files"].append(relative)
        manifest["required_toolchain"]["managed_files"].sort()
    candidate.write_manifest(manifest)
    if locked:
        lock = candidate.lock()
        lock["files"].append(_lock_entry(path, relative))
        lock["bundle_sha256"] = _sha256_bytes(_canonical(lock["files"], newline=False))
        manifest = candidate.manifest()
        manifest["core"]["file_count"] = len(lock["files"])
        candidate.write_manifest(manifest)
        candidate.write_lock(lock)


def _materialize_fixture_pyvenv_cfg(
    destination: Path,
    *,
    source: Path | None = None,
    base_executable: Path | None = None,
    version: tuple[int, int, int] | None = None,
) -> None:
    source = source if source is not None else Path(sys.prefix) / "pyvenv.cfg"
    if source.is_file():
        shutil.copy2(source, destination)
        return

    if base_executable is None:
        base_executable = Path(getattr(sys, "_base_executable", None) or sys.executable)
        if not base_executable.is_file():
            base_executable = Path(sys.executable)
    base_executable = base_executable.resolve(strict=True)
    if not base_executable.is_file():
        raise FileNotFoundError(base_executable)
    base_home = base_executable.parent
    if not base_home.is_dir():
        raise FileNotFoundError(base_home)
    if version is None:
        version = (sys.version_info.major, sys.version_info.minor, sys.version_info.micro)
    contents = (
        f"home = {base_home}\n"
        "include-system-site-packages = false\n"
        f"version = {'.'.join(str(part) for part in version)}\n"
        f"executable = {base_executable}\n"
    )
    destination.write_text(contents, encoding="utf-8", newline="\n")


def _fixture(
    tmp_path: Path,
    *,
    execution_kind: str = "DIRECT_EXECUTABLE",
    code: str = SUCCESS_CODE,
    allowed: tuple[str, ...] = (),
    secrets: tuple[str, ...] = (),
    requirements: tuple[dict[str, Any], ...] = (),
    declared_tool_sha256: str | None = None,
    declared_tool_size: int | None = None,
    tool_locked: bool = True,
    definition_owner: str = "managed_core",
    pyvenv_source: Path | None = None,
) -> dict[str, Any]:
    candidate = _make_candidate(tmp_path / "candidate", python_payload=Path(sys.executable).read_bytes())
    if os.name != "nt":
        candidate.package_python.chmod(
            candidate.package_python.stat().st_mode
            | stat.S_IXUSR
            | stat.S_IXGRP
            | stat.S_IXOTH
        )
    pyvenv = candidate.package_python.parent.parent / "pyvenv.cfg"
    _materialize_fixture_pyvenv_cfg(pyvenv, source=pyvenv_source)
    _add_package_file(
        candidate, pyvenv, pyvenv.relative_to(candidate.package_root).as_posix(),
        "managed_core", locked=True,
    )
    if execution_kind == "PACKAGE_PYTHON_SCRIPT":
        tool = candidate.package_root / "tools" / "session_tool.py"
        tool.parent.mkdir(parents=True)
        tool.write_text(code, encoding="utf-8")
        template = ["{verified_tool_path}"]
        placeholders = ["{verified_tool_path}"]
        binding = "LOCATOR_PACKAGE_PYTHON"
    else:
        tool = candidate.package_root / "tools" / "direct" / "python.exe"
        tool.parent.mkdir(parents=True)
        shutil.copy2(sys.executable, tool)
        tool_config = tool.parent.parent / "pyvenv.cfg"
        _materialize_fixture_pyvenv_cfg(tool_config, source=pyvenv_source)
        _add_package_file(candidate, tool_config, tool_config.relative_to(candidate.package_root).as_posix(), "managed_core", locked=True)
        template = ["-c", code]
        placeholders = []
        binding = "SELF"
    relative_tool = tool.relative_to(candidate.package_root).as_posix()
    _add_package_file(candidate, tool, relative_tool, "managed_core", locked=tool_locked)
    definition_path = candidate.package_root / "definitions" / "session-tool.json"
    definition_path.parent.mkdir(parents=True)
    definition = {
        "schema_version": "golden-key-workbuddy-package-tool-definition-v1",
        "definition_id": "fixture-session-tool", "definition_sha256": "0" * 64,
        "definition_relative_path": definition_path.relative_to(candidate.package_root).as_posix(),
        "authority_owner": "managed_core", "package_release": RELEASE, "package_commit": COMMIT,
        "tool_id": "fixture-tool", "relative_path": relative_tool, "sha256": declared_tool_sha256 or _sha256(tool),
        "size": declared_tool_size if declared_tool_size is not None else tool.stat().st_size,
        "owner": definition_owner, "execution_kind": execution_kind,
        "interpreter_binding": binding, "fixed_argv_template": template,
        "fixed_argv_placeholders": placeholders, "request_schema_sha256": REQUEST_HASH,
        "result_schema_sha256": RESULT_HASH, "allowed_environment_names": list(allowed),
        "secret_environment_names": list(secrets), "required_local_capabilities": list(requirements),
    }
    _seal_definition(definition)
    definition_path.write_bytes(_canonical(definition))
    _add_package_file(candidate, definition_path, definition["definition_relative_path"], "managed_core", locked=True)
    candidate.rebuild_archive()
    registered = candidate.register()
    _activate_missing(candidate, registered["registration_sha256"])
    result_root = candidate.data_root / "Results"
    result_root.mkdir()
    controls = {
        "schema_version": "golden-key-workbuddy-launcher-executor-controls-v1",
        "session_id": "session-1", "request_id": "request-1", "timeout_seconds": 10,
        "termination_grace_seconds": 1, "result_root": str(result_root), "provider_environment": {},
    }
    return {"candidate": candidate, "definition": definition, "controls": controls, "result_root": result_root}


def _launch(
    fixture: dict[str, Any],
    *,
    message: str = "原样业务请求",
    evidence: Any = (),
    event: threading.Event | None = None,
    managed_runtime: Mapping[str, Any] | None = None,
):
    return launch_session_tool(
        fixture["candidate"].data_root,
        message,
        fixture["controls"],
        fixture["definition"],
        evidence,
        event,
        managed_remotion_runtime=managed_runtime,
    )


def _assert(receipt: Any, outcome: str, reason: str, spawn: int, residual: bool = False) -> None:
    assert receipt["outcome"] == outcome, dict(receipt)
    assert receipt["reason_code"] == reason, dict(receipt)
    assert receipt["spawn_count"] == spawn
    assert receipt["residual_process"]["detected"] is residual
    assert receipt["retry_count"] == 0


def _assert_secret_safe_receipt_types(receipt: Any, canary: str) -> None:
    assert isinstance(receipt["schema_version"], str)
    assert isinstance(receipt["outcome"], str)
    assert isinstance(receipt["reason_code"], str)
    assert isinstance(receipt["provider_environment_names"], tuple)
    assert all(isinstance(name, str) for name in receipt["provider_environment_names"])
    assert isinstance(receipt["local_capability_evidence_identities"], tuple)
    assert isinstance(receipt["result_pointer"]["valid"], bool)
    assert receipt["result_pointer"]["path"] is None or isinstance(
        receipt["result_pointer"]["path"], str
    )
    assert receipt["result_pointer"]["sha256"] is None or isinstance(
        receipt["result_pointer"]["sha256"], str
    )
    assert receipt["result_pointer"]["size"] is None or isinstance(
        receipt["result_pointer"]["size"], int
    )
    assert receipt["error"] is not None
    assert all(
        isinstance(receipt["error"][field], str)
        for field in ("code", "origin", "sanitized_message")
    )
    dynamic_domains = {
        "session": receipt["session"],
        "request": receipt["request"],
        "user_message": receipt["user_message"],
        "local_capability_evidence_identities": receipt[
            "local_capability_evidence_identities"
        ],
        "stdout": receipt["stdout"],
        "stderr": receipt["stderr"],
        "result_pointer": receipt["result_pointer"],
    }
    assert not launcher_module._dynamic_value_contains_secret(dynamic_domains, (canary,))
    assert canary not in repr(receipt)


def _managed_runtime(tmp_path: Path) -> dict[str, str]:
    root = tmp_path / "managed-remotion-runtime"
    entrypoint = root / "node_modules" / ".bin" / "remotion.cmd"
    entrypoint.parent.mkdir(parents=True)
    entrypoint.write_text("managed remotion", encoding="utf-8")
    return {
        "status": "PRESENT",
        "source": "managed",
        "runtime_root": str(root.resolve()),
        "verified_entrypoint": str(entrypoint.resolve()),
        "version": "4.0.0",
        "install_scope": "system",
        "definition_sha256": "a" * 64,
        "manifest_sha256": "b" * 64,
        "lockfile_sha256": "c" * 64,
    }


def _rehash_stage3_evidence(evidence: dict[str, Any]) -> dict[str, Any]:
    definition = evidence["approved_capability_definition"]
    body = {key: value for key, value in definition.items() if key != "definition_sha256"}
    digest = hashlib.sha256(_canonical(body, newline=False)).hexdigest()
    definition["definition_sha256"] = digest
    evidence["approved_capability_definition_sha256"] = digest
    fact = evidence["original_stage3_fact"]
    if fact["status"] == "PRESENT":
        fact["evidence"]["definition_sha256"] = digest
    else:
        fact["definition_sha256"] = digest
    evidence["original_stage3_fact_sha256"] = hashlib.sha256(
        _canonical(fact, newline=False)
    ).hexdigest()
    return {
        "evidence_schema_version": "golden-key-workbuddy-local-capability-evidence-v1",
        "capability_id": definition["capability"],
        "definition_sha256": digest,
        "compatibility_basis": "EXACT_ASSET_IDENTITY",
    }


def _make_directory_reparse(link: Path, target: Path) -> None:
    if os.name == "nt":
        completed = subprocess.run(
            [
                os.environ.get("COMSPEC", "cmd.exe"),
                "/d", "/c", "mklink", "/J", str(link), str(target),
            ],
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        assert completed.returncode == 0, (completed.stdout, completed.stderr)
    else:
        link.symlink_to(target, target_is_directory=True)


def _remove_directory_reparse(link: Path) -> None:
    if os.name == "nt":
        os.rmdir(link)
    else:
        link.unlink()


def _install_simulated_windows_lifecycle(
    monkeypatch: pytest.MonkeyPatch,
    fixture: dict[str, Any],
    *,
    fail_at: str | None,
) -> tuple[list[str], list[dict[str, Any]]]:
    events: list[str] = []
    popen_kwargs: list[dict[str, Any]] = []
    result = {
        "schema_version": "golden-key-workbuddy-package-tool-result-v1",
        "session_id": fixture["controls"]["session_id"],
        "request_id": fixture["controls"]["request_id"],
        "outcome": "SUCCEEDED",
        "result_pointer": {
            "relative_path": "result.bin",
            "sha256": hashlib.sha256(b"fixture-result").hexdigest(),
            "size": 14,
        },
        "error": None,
    }

    class SimulatedProcess:
        def __init__(self) -> None:
            self.pid = 4242
            self._handle = 4242
            self.stdin = io.BytesIO()
            self.stdout = io.BytesIO(_canonical(result))
            self.stderr = io.BytesIO()
            self.returncode: int | None = None

        def poll(self) -> int | None:
            return self.returncode

        def kill(self) -> None:
            events.append("kill")
            self.returncode = 1

        def wait(self, timeout: int | None = None) -> int:
            events.append("wait")
            if self.returncode is None:
                raise subprocess.TimeoutExpired("simulated", timeout)
            return self.returncode

    process = SimulatedProcess()

    class SimulatedJob:
        def __init__(self) -> None:
            self.handle = 1
            self.assigned = False

        def assign(self, child: Any) -> None:
            assert child is process
            events.append("assign")
            if fail_at == "assign":
                raise OSError("simulated assign failure")
            self.assigned = True

        def resume(self, child: Any) -> None:
            assert child is process and self.assigned
            events.append("resume")
            if fail_at == "resume":
                raise OSError("simulated resume failure")
            (fixture["result_root"] / "result.bin").write_bytes(b"fixture-result")
            process.returncode = 0

        def active_count(self) -> int:
            return int(self.assigned and process.returncode is None)

        def terminate(self) -> None:
            events.append("terminate")
            # Model TerminateJobObject as an asynchronous kill request.  The
            # launcher must still kill/wait the concrete Popen object and
            # prove that no process remains before returning its receipt.

        def close(self) -> None:
            events.append("close")

    def fake_popen(*_args: Any, **kwargs: Any) -> SimulatedProcess:
        events.append("popen")
        popen_kwargs.append(kwargs)
        return process

    monkeypatch.setattr(launcher_module, "_WINDOWS_PROCESS_PLATFORM", True)
    monkeypatch.setattr(launcher_module, "_WindowsJob", SimulatedJob)
    monkeypatch.setattr(launcher_module.subprocess, "Popen", fake_popen)
    return events, popen_kwargs


def _capability_definition(capability: str, asset_root: Path, source: str) -> tuple[dict[str, Any], bytes]:
    payload = f"{capability}-asset".encode()
    explicit = [str(asset_root)] if source == "explicit" else []
    command = capability if source == "PATH" else None
    definition: dict[str, Any] = {
        "capability": capability,
        "definition_sha256": "0" * 64,
        "version": "1.2.3",
        "verified_entrypoint": "tool.exe",
        "approved_mainland_sources": [
            {"filename": "tool.bin", "url": f"https://registry.npmmirror.com/{capability}/-/tool.bin"}
        ],
        "assets": [
            {
                "filename": "tool.bin", "size": len(payload),
                "sha256": hashlib.sha256(payload).hexdigest(), "license": "MIT",
                "managed_target": "tool.exe",
            }
        ],
        "explicit_registered_or_configured_candidate_paths": explicit,
        "normal_command_name": command,
    }
    body = {key: value for key, value in definition.items() if key != "definition_sha256"}
    definition["definition_sha256"] = hashlib.sha256(_canonical(body, newline=False)).hexdigest()
    return definition, payload


def _local_evidence(
    fixture: dict[str, Any],
    *,
    source: str,
    status: str = "PRESENT",
    add_extra: bool = False,
    capability: str = "opaque-capability",
) -> tuple[dict[str, Any], dict[str, Any], Path]:
    provisional_root = fixture["candidate"].data_root / "external"
    definition, payload = _capability_definition(capability, provisional_root, source)
    if source == "managed":
        root = fixture["candidate"].data_root / "Runtime" / "Composition" / capability / definition["definition_sha256"]
    elif source == "explicit":
        root = provisional_root
    else:
        root = fixture["candidate"].data_root / "path-command.exe"
    if source == "PATH":
        root.write_bytes(payload)
        entrypoint = root
        runtime_root = root
    else:
        root.mkdir(parents=True)
        entrypoint = root / "tool.exe"
        entrypoint.write_bytes(payload)
        runtime_root = root
        if add_extra:
            (root / "foreign.txt").write_text("preserve", encoding="utf-8")
            (root / "foreign-directory").mkdir()
            (root / "foreign-directory" / "keep.txt").write_text("keep", encoding="utf-8")
    evidence_fields = {
        "status": "PRESENT" if status == "PRESENT" else "INTEGRATED",
        "capability": capability,
        "definition_sha256": definition["definition_sha256"],
        "runtime_root": str(runtime_root.resolve()),
        "verified_entrypoint": str(entrypoint.resolve()),
        "version_evidence": {
            "reason": "COMPATIBLE", "entrypoint": str(entrypoint.resolve()),
            "exit_code": 0, "version_output": "untrusted caller text 1.2.3",
        },
        "asset_evidence": [
            {
                "managed_target": "tool.exe", "expected_size": len(payload),
                "expected_sha256": hashlib.sha256(payload).hexdigest(), "license": "MIT",
                "exists": True, "size": len(payload), "sha256": hashlib.sha256(payload).hexdigest(),
                "reason": "IDENTITY_MATCH",
            }
        ],
        "source": source,
    }
    if status == "PRESENT":
        fact: dict[str, Any] = {"capability": capability, "status": "PRESENT", "evidence": evidence_fields}
    else:
        fact = {**evidence_fields, "plan_sha256": "a" * 64, "reused": False}
    evidence = {
        "schema_version": "golden-key-workbuddy-local-capability-evidence-v1",
        "approved_capability_definition": definition,
        "approved_capability_definition_sha256": definition["definition_sha256"],
        "original_stage3_fact": fact,
        "original_stage3_fact_sha256": hashlib.sha256(_canonical(fact, newline=False)).hexdigest(),
    }
    requirement = {
        "evidence_schema_version": "golden-key-workbuddy-local-capability-evidence-v1",
        "capability_id": capability,
        "definition_sha256": definition["definition_sha256"],
        "compatibility_basis": "EXACT_ASSET_IDENTITY",
    }
    return requirement, evidence, root


def test_fixture_pyvenv_cfg_is_generated_when_source_is_missing(tmp_path: Path) -> None:
    base_home = tmp_path / "standalone-python" / "bin"
    base_home.mkdir(parents=True)
    base_executable = base_home / "python"
    base_executable.write_bytes(b"fixture executable identity")
    destination = tmp_path / "generated" / "pyvenv.cfg"
    destination.parent.mkdir()

    _materialize_fixture_pyvenv_cfg(
        destination,
        source=tmp_path / "standalone-python" / "missing-pyvenv.cfg",
        base_executable=base_executable,
        version=(3, 11, 16),
    )

    assert destination.read_bytes() == (
        f"home = {base_home.resolve()}\n"
        "include-system-site-packages = false\n"
        "version = 3.11.16\n"
        f"executable = {base_executable.resolve()}\n"
    ).encode("utf-8")
    assert base_home.is_dir()
    assert base_executable.is_file()


@pytest.mark.parametrize("execution_kind", ["DIRECT_EXECUTABLE", "PACKAGE_PYTHON_SCRIPT"])
def test_fixture_launches_when_setup_python_has_no_pyvenv_cfg(
    tmp_path: Path,
    execution_kind: str,
) -> None:
    fixture = _fixture(
        tmp_path,
        execution_kind=execution_kind,
        pyvenv_source=tmp_path / "standalone-python" / "missing-pyvenv.cfg",
    )

    package_python = fixture["candidate"].package_python
    package_config = package_python.parent.parent / "pyvenv.cfg"
    config_text = package_config.read_text(encoding="utf-8")
    assert "include-system-site-packages = false\n" in config_text
    assert f"version = {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}\n" in config_text
    assert not (package_python.parent / "pyvenv.cfg").exists()
    if execution_kind == "DIRECT_EXECUTABLE":
        direct_root = fixture["candidate"].package_root / "tools"
        direct_config = direct_root / "pyvenv.cfg"
        assert direct_config.read_bytes() == package_config.read_bytes()
        assert not (direct_root / "direct" / "pyvenv.cfg").exists()

    receipt = _launch(fixture)
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    # Python 3.14 validates venv prefix layout during startup.  A zero-byte
    # child stderr proves both real execution kinds start without that warning.
    assert receipt["stderr"]["size"] == 0
    assert receipt["stderr"]["sha256"] == hashlib.sha256(b"").hexdigest()
    assert receipt["stderr"]["truncated"] is False


def test_37_real_stage2_roundtrip_and_priority_level_11_success(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path)
    receipt = _launch(fixture)
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    assert receipt["result_pointer"]["valid"] is True
    assert receipt["user_message"]["sha256"] == hashlib.sha256("原样业务请求".encode()).hexdigest()
    assert receipt["provider_environment_names"] == ()


def test_managed_remotion_runtime_reaches_child_stdin_and_receipt(tmp_path: Path) -> None:
    runtime = _managed_runtime(tmp_path)
    expected = repr(runtime)
    code = f'''import hashlib,json,pathlib,sys
r=json.load(sys.stdin)
assert r["managed_remotion_runtime"] == {expected}
p=pathlib.Path(r["executor_controls"]["result_root"])/"result.bin"; p.write_bytes(b"ok")
o={{"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"SUCCEEDED","result_pointer":{{"relative_path":"result.bin","sha256":hashlib.sha256(b"ok").hexdigest(),"size":2}},"error":None}}
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\\n").encode())'''
    receipt = _launch(_fixture(tmp_path, code=code), managed_runtime=runtime)
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    assert receipt["managed_remotion_runtime"] == runtime


def test_invalid_managed_remotion_runtime_blocks_before_spawn(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path)
    invalid = dict(_managed_runtime(tmp_path))
    invalid["runtime_root"] = "relative-runtime-root"
    receipt = _launch(fixture, managed_runtime=invalid)
    _assert(receipt, "PRELAUNCH_BLOCKED", "MANAGED_REMOTION_RUNTIME_INVALID", 0)


def test_fixed_child_handoff_preserves_managed_remotion_runtime_fact(tmp_path: Path) -> None:
    runtime = _managed_runtime(tmp_path)
    result_root = tmp_path / "handoff-results"
    result_root.mkdir()
    request = {
        "session_id": "session-1",
        "request_id": "request-1",
        "message": "ordinary request",
        "timeout_seconds": 10,
        "provider_environment_names": [],
        "registration_sha256": "d" * 64,
        "openmontage_release": "release-1",
        "openmontage_commit": "0" * 40,
        "tool_definition_sha256": "e" * 64,
        "local_capability_evidence_identities": [],
        "managed_remotion_runtime": runtime,
        "result_root": result_root,
    }
    relative, _digest, _size = fixed_child._write_handoff(request)
    handoff = result_root / Path(relative)
    payload = json.loads(handoff.read_text(encoding="utf-8"))
    assert payload["managed_remotion_runtime"] == runtime
    assert payload["renderer_selected"] is False
    assert payload["media_executed"] is False


def test_10_literal_user_message_bytes_reach_child_unchanged(tmp_path: Path) -> None:
    message = "  原样\r\n业务请求：A/B + ①  "
    expected = message.encode("utf-8")
    code = f'''import hashlib,json,pathlib,sys
r=json.load(sys.stdin)
assert r["user_message"].encode("utf-8") == {expected!r}
p=pathlib.Path(r["executor_controls"]["result_root"])/"result.bin"; p.write_bytes(b"ok")
o={{"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"SUCCEEDED","result_pointer":{{"relative_path":"result.bin","sha256":hashlib.sha256(b"ok").hexdigest(),"size":2}},"error":None}}
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\\n").encode())'''
    receipt = _launch(_fixture(tmp_path, code=code), message=message)
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    assert receipt["user_message"]["sha256"] == hashlib.sha256(expected).hexdigest()


def test_11_executor_controls_remain_separate_from_literal_message(tmp_path: Path) -> None:
    message = "只处理这条业务原话"
    code = r'''import hashlib,json,pathlib,sys
r=json.load(sys.stdin)
assert r["user_message"] == "只处理这条业务原话"
assert "timeout_seconds" not in r["user_message"] and r["executor_controls"]["timeout_seconds"] == 10
p=pathlib.Path(r["executor_controls"]["result_root"])/"result.bin"; p.write_bytes(b"ok")
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"SUCCEEDED","result_pointer":{"relative_path":"result.bin","sha256":hashlib.sha256(b"ok").hexdigest(),"size":2},"error":None}
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode())'''
    receipt = _launch(_fixture(tmp_path, code=code), message=message)
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)


def test_14_base_tool_requires_no_named_optional_capability(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path, requirements=())
    assert fixture["definition"]["required_local_capabilities"] == []
    receipt = _launch(fixture)
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    assert receipt["local_capability_evidence_identities"] == ()


def test_20_real_popen_occurs_exactly_once_and_retry_is_zero(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fixture = _fixture(tmp_path)
    real_popen = launcher_module.subprocess.Popen
    calls = 0

    def counted_popen(*args: Any, **kwargs: Any):
        nonlocal calls
        calls += 1
        return real_popen(*args, **kwargs)

    monkeypatch.setattr(launcher_module.subprocess, "Popen", counted_popen)
    receipt = _launch(fixture)
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    assert calls == 1


def test_21_launcher_exposes_no_second_agent_or_control_plane(tmp_path: Path) -> None:
    receipt = _launch(_fixture(tmp_path))
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    assert launcher_module.__all__ == ["launch_session_tool"]
    assert not any(
        hasattr(launcher_module, name)
        for name in ("Agent", "Director", "Scheduler", "Pipeline", "Checkpoint", "ArtifactStore")
    )


def test_25_absent_provider_is_not_local_capability_failure(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path, allowed=("FUTURE_PROVIDER_KEY",), requirements=())
    receipt = _launch(fixture)
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    assert receipt["provider_environment_names"] == ()


def test_26_undeclared_local_evidence_is_rejected_without_spawn(tmp_path: Path) -> None:
    seed = _fixture(tmp_path / "seed")
    _requirement, evidence, _root = _local_evidence(seed, source="explicit")
    receipt = _launch(_fixture(tmp_path / "actual", requirements=()), evidence=(evidence,))
    _assert(receipt, "PRELAUNCH_BLOCKED", "INVALID_INPUT", 0)


def test_36_definition_has_no_registration_manifest_or_lock_hash_cycle(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path)
    forbidden = {
        "registration_sha256", "manifest_sha256", "manifest_size",
        "lock_sha256", "lock_size", "bundle_sha256",
    }
    assert not (forbidden & set(fixture["definition"]))
    receipt = _launch(fixture)
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)


def test_09_python_script_execution_kind_succeeds_without_caller_argv(tmp_path: Path) -> None:
    receipt = _launch(_fixture(tmp_path, execution_kind="PACKAGE_PYTHON_SCRIPT"))
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)


def test_1_no_active_registration_returns_full_receipt(tmp_path: Path) -> None:
    data = tmp_path / "data"
    data.mkdir()
    receipt = launch_session_tool(data, "x", {}, {})
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCATOR_FAILED", 0)
    assert len(receipt) == 31


def test_32_entry_cancel_precedes_locator_and_priority_level_02(tmp_path: Path) -> None:
    event = threading.Event()
    event.set()
    receipt = launch_session_tool(tmp_path / "missing", "x", {"session_id": "s", "request_id": "r"}, {}, cancel_event=event)
    _assert(receipt, "CANCELLED", "CANCELLED_BEFORE_SPAWN", 0)
    assert receipt["cancelled"] is True


@pytest.mark.parametrize("hint_field", ["session_id", "request_id"])
def test_49_pre_cancel_extracts_raw_provider_secret_before_hints_or_locator(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, hint_field: str
) -> None:
    canary = "cancel-secret-value"
    controls: dict[str, Any] = {
        "session_id": "safe-session",
        "request_id": "safe-request",
        "provider_environment": {"UNVERIFIED_PROVIDER_NAME": canary},
        "otherwise_invalid": object(),
    }
    controls[hint_field] = canary
    event = threading.Event()
    event.set()
    locator_calls = 0
    popen_calls = 0

    def forbidden_locator(_data_root: Any) -> Any:
        nonlocal locator_calls
        locator_calls += 1
        raise AssertionError("pre-cancel must not access Locator")

    def forbidden_popen(*_args: Any, **_kwargs: Any) -> Any:
        nonlocal popen_calls
        popen_calls += 1
        raise AssertionError("pre-cancel must not spawn")

    monkeypatch.setattr(launcher_module, "locate_active_package", forbidden_locator)
    monkeypatch.setattr(launcher_module.subprocess, "Popen", forbidden_popen)
    receipt = launch_session_tool(
        tmp_path / "missing",
        "ordinary-message",
        controls,
        {},
        cancel_event=event,
    )
    _assert(receipt, "CANCELLED", "CANCELLED_BEFORE_SPAWN", 0)
    assert locator_calls == 0 and popen_calls == 0
    assert receipt["cancelled"] is True
    assert receipt["session" if hint_field == "session_id" else "request"][hint_field] is None
    assert receipt["provider_environment_names"] == ()
    _assert_secret_safe_receipt_types(receipt, canary)


def test_48_hyphen_secret_can_collide_with_fixed_schema_on_pre_cancel(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    event = threading.Event()
    event.set()
    monkeypatch.setattr(
        launcher_module,
        "locate_active_package",
        lambda _root: (_ for _ in ()).throw(AssertionError("Locator must stay at zero")),
    )
    receipt = launch_session_tool(
        tmp_path / "missing",
        "ordinarymessage",
        {
            "session_id": "safesession",
            "request_id": "saferequest",
            "provider_environment": {"OPAQUE": "-"},
        },
        {},
        cancel_event=event,
    )
    _assert(receipt, "CANCELLED", "CANCELLED_BEFORE_SPAWN", 0)
    assert receipt["schema_version"] == "golden-key-workbuddy-launcher-receipt-v1"
    assert receipt["session"]["session_id"] == "safesession"
    assert receipt["request"]["request_id"] == "saferequest"


def test_49_unreadable_raw_controls_suppress_all_unconfirmed_cancel_hints(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    canary = "unreadable-provider-value"

    class UnreadableControls(dict[str, Any]):
        def get(self, _key: str, _default: Any = None) -> Any:
            raise RuntimeError("untrusted controls read failure")

    event = threading.Event()
    event.set()
    locator_calls = 0

    def forbidden_locator(_root: Any) -> Any:
        nonlocal locator_calls
        locator_calls += 1
        raise AssertionError("Locator must stay at zero")

    monkeypatch.setattr(launcher_module, "locate_active_package", forbidden_locator)
    receipt = launch_session_tool(
        tmp_path / "missing",
        canary,
        UnreadableControls(
            session_id=canary,
            request_id=canary,
            provider_environment={"OPAQUE": canary},
        ),
        {},
        cancel_event=event,
    )
    _assert(receipt, "CANCELLED", "CANCELLED_BEFORE_SPAWN", 0)
    assert locator_calls == 0
    assert receipt["session"]["session_id"] is None
    assert receipt["request"]["request_id"] is None
    assert receipt["user_message"] == {"sha256": None, "byte_length": None}
    assert canary not in repr(receipt)


@pytest.mark.parametrize(
    ("mutation", "reason"),
    [
        pytest.param(lambda d: d.pop("tool_id"), "TOOL_DEFINITION_INVALID", id="missing-field"),
        pytest.param(lambda d: d.__setitem__("unknown", True), "TOOL_DEFINITION_INVALID", id="unknown-field"),
        pytest.param(lambda d: d.__setitem__("definition_sha256", "f" * 64), "TOOL_DEFINITION_INVALID", id="self-hash"),
    ],
)
def test_04_definition_closed_shape_and_self_hash_fail_closed(tmp_path: Path, mutation, reason: str) -> None:
    fixture = _fixture(tmp_path)
    mutation(fixture["definition"])
    receipt = _launch(fixture)
    _assert(receipt, "PRELAUNCH_BLOCKED", reason, 0)


@pytest.mark.parametrize(
    "mutation",
    [
        pytest.param(lambda d: d.__setitem__("fixed_argv_placeholders", []), id="drop-python-placeholder"),
        pytest.param(lambda d: d.__setitem__("fixed_argv_template", ["{verified_tool_path}", "--extra"]), id="extra-fixed-argv"),
        pytest.param(lambda d: d.__setitem__("interpreter_binding", "SELF"), id="wrong-binding"),
    ],
)
def test_09_placeholder_binding_or_argv_injection_is_rejected(tmp_path: Path, mutation) -> None:
    fixture = _fixture(tmp_path, execution_kind="PACKAGE_PYTHON_SCRIPT")
    mutation(fixture["definition"])
    receipt = _launch(fixture)
    _assert(receipt, "PRELAUNCH_BLOCKED", "TOOL_DEFINITION_INVALID", 0)


def test_15_nonzero_exit_is_preserved_at_priority_level_08(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path, code="import sys; sys.stdin.buffer.read(); sys.exit(7)")
    receipt = _launch(fixture)
    _assert(receipt, "EXITED_NONZERO", "EXITED_NONZERO", 1)
    assert receipt["exit_code"] == 7


def test_16_timeout_terminates_owned_tree_at_priority_level_07(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path, code="import sys,time; sys.stdin.buffer.read(); time.sleep(30)")
    fixture["controls"]["timeout_seconds"] = 1
    receipt = _launch(fixture)
    _assert(receipt, "TIMED_OUT", "TIMEOUT", 1)
    assert receipt["timed_out"] is True
    assert receipt["residual_process"]["termination_attempted"] is True


def test_35_child_reported_failure_is_priority_level_10(tmp_path: Path) -> None:
    receipt = _launch(_fixture(tmp_path, code=FAILED_CODE))
    _assert(receipt, "CHILD_REPORTED_FAILURE", "CHILD_REPORTED_FAILURE", 1)


def test_17_invalid_output_is_priority_level_09(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path, code="import sys; sys.stdin.buffer.read(); print('not-json')")
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "OUTPUT_INVALID", 1)


def test_18_secret_disclosure_is_priority_level_06_and_wins_over_nonzero(tmp_path: Path) -> None:
    code = "import os,sys; sys.stdin.buffer.read(); print(os.environ['DYNAMIC_TOKEN']); sys.exit(9)"
    fixture = _fixture(tmp_path, code=code, allowed=("DYNAMIC_TOKEN",), secrets=("DYNAMIC_TOKEN",))
    fixture["controls"]["provider_environment"] = {"DYNAMIC_TOKEN": "split-canary-secret"}
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    assert "split-canary-secret" not in repr(receipt)


@pytest.mark.parametrize("stream", ["stdout", "stderr"])
def test_18_secret_is_detected_across_real_pipe_chunks(tmp_path: Path, stream: str) -> None:
    code = f'''import os,sys,time
sys.stdin.buffer.read()
s=os.environ["DYNAMIC_TOKEN"].encode(); target=sys.{stream}.buffer
target.write(s[:11]); target.flush(); time.sleep(0.1); target.write(s[11:]); target.flush(); sys.exit(9)'''
    fixture = _fixture(
        tmp_path, code=code, allowed=("DYNAMIC_TOKEN",), secrets=("DYNAMIC_TOKEN",)
    )
    secret = "cross-chunk-canary-value"
    fixture["controls"]["provider_environment"] = {"DYNAMIC_TOKEN": secret}
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    assert secret not in repr(receipt)


@pytest.mark.parametrize("stream", ["stdout", "stderr"])
def test_18_every_allowlisted_provider_value_is_a_secret_canary_even_when_unmarked(
    tmp_path: Path, stream: str
) -> None:
    code = f'''import os,sys
sys.stdin.buffer.read(); sys.{stream}.write(os.environ["OPAQUE_PROVIDER_VALUE"]); sys.{stream}.flush(); sys.exit(9)'''
    fixture = _fixture(
        tmp_path,
        code=code,
        allowed=("OPAQUE_PROVIDER_VALUE",),
        secrets=(),
    )
    canary = "unmarked-provider-canary-value"
    fixture["controls"]["provider_environment"] = {"OPAQUE_PROVIDER_VALUE": canary}
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    _assert_secret_safe_receipt_types(receipt, canary)
    assert receipt[stream] == {
        "size": 0,
        "sha256": hashlib.sha256(b"").hexdigest(),
        "truncated": True,
    }


@pytest.mark.parametrize("dynamic_kind", ["result_pointer", "error"])
def test_52_json_escape_cannot_hide_secret_reconstructed_in_child_dynamic_fields(
    tmp_path: Path, dynamic_kind: str
) -> None:
    if dynamic_kind == "result_pointer":
        code = r'''import hashlib,json,os,pathlib,sys
r=json.load(sys.stdin); s=os.environ["OPAQUE_PROVIDER_VALUE"]; p=pathlib.Path(r["executor_controls"]["result_root"])/(s+".bin"); p.write_bytes(b"ok")
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"SUCCEEDED","result_pointer":{"relative_path":s+".bin","sha256":hashlib.sha256(b"ok").hexdigest(),"size":2},"error":None}
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=True,sort_keys=True,separators=(",",":"))+"\n").encode())'''
    else:
        code = r'''import json,os,sys
r=json.load(sys.stdin); s=os.environ["OPAQUE_PROVIDER_VALUE"]
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"FAILED","result_pointer":None,"error":{"code":"FIXTURE","origin":"FIXTURE","message":s}}
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=True,sort_keys=True,separators=(",",":"))+"\n").encode())'''
    fixture = _fixture(
        tmp_path,
        code=code,
        allowed=("OPAQUE_PROVIDER_VALUE",),
        secrets=(),
    )
    canary = "秘密动态值"
    fixture["controls"]["provider_environment"] = {"OPAQUE_PROVIDER_VALUE": canary}
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    _assert_secret_safe_receipt_types(receipt, canary)
    assert receipt["stdout"] == {
        "size": 0,
        "sha256": hashlib.sha256(b"").hexdigest(),
        "truncated": True,
    }


@pytest.mark.parametrize(
    "dynamic_location",
    ["unknown_value", "nested_array", "invalid_schema", "invalid_outcome", "dynamic_key"],
)
def test_52_complete_decoded_child_object_is_scanned_before_schema_rejection(
    tmp_path: Path, dynamic_location: str
) -> None:
    code = f'''import json,os,sys
r=json.load(sys.stdin); s=os.environ["OPAQUE_PROVIDER_VALUE"]
o={{"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"FAILED","result_pointer":None,"error":{{"code":"FIXTURE","origin":"FIXTURE","message":"ordinary"}}}}
location={dynamic_location!r}
if location=="unknown_value": o["unknown_dynamic_field"]=s
elif location=="nested_array": o["unknown_dynamic_field"]=["ordinary",{{"deep":[s]}}]
elif location=="invalid_schema": o["schema_version"]=s
elif location=="invalid_outcome": o["outcome"]=s
else: o[s]="ordinary"
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=True,sort_keys=True,separators=(",",":"))+"\\n").encode())'''
    fixture = _fixture(
        tmp_path,
        code=code,
        allowed=("OPAQUE_PROVIDER_VALUE",),
        secrets=(),
    )
    canary = "秘密子对象值"
    fixture["controls"]["provider_environment"] = {
        "OPAQUE_PROVIDER_VALUE": canary
    }
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    _assert_secret_safe_receipt_types(receipt, canary)
    assert receipt["stdout"] == {
        "size": 0,
        "sha256": hashlib.sha256(b"").hexdigest(),
        "truncated": True,
    }


@pytest.mark.parametrize("dynamic_location", ["unknown_value", "invalid_outcome"])
def test_52_child_float_uses_canonical_json_spelling_before_schema_rejection(
    tmp_path: Path, dynamic_location: str
) -> None:
    code = f'''import json,sys
r=json.load(sys.stdin)
o={{"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"FAILED","result_pointer":None,"error":{{"code":"FIXTURE","origin":"FIXTURE","message":"ordinary"}}}}
if {dynamic_location!r}=="unknown_value": o["unknown_dynamic_field"]=1.0
else: o["outcome"]=1.0
raw=json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))
sys.stdout.write(raw.replace("1.0","1e0",1)+"\\n")'''
    fixture = _fixture(
        tmp_path,
        code=code,
        allowed=("OPAQUE_PROVIDER_VALUE",),
        secrets=(),
    )
    canary = "1.0"
    fixture["controls"]["provider_environment"] = {
        "OPAQUE_PROVIDER_VALUE": canary
    }
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    _assert_secret_safe_receipt_types(receipt, canary)
    assert receipt["stdout"] == {
        "size": 0,
        "sha256": hashlib.sha256(b"").hexdigest(),
        "truncated": True,
    }


@pytest.mark.parametrize(
    ("value", "canary"),
    [(1.0, "1.0"), (-0.0, "-0.0"), (1e20, "1e+20")],
)
def test_55_finite_float_scanner_matches_project_canonical_json_spelling(
    value: float, canary: str
) -> None:
    assert launcher_module._dynamic_value_contains_secret(
        {"nested": [value]}, (canary,)
    )


@pytest.mark.parametrize("duplicate_location", ["root", "nested"])
def test_52_duplicate_first_value_is_scanned_before_overwrite(
    tmp_path: Path, duplicate_location: str
) -> None:
    code = f'''import json,os,sys
r=json.load(sys.stdin); s=os.environ["OPAQUE_PROVIDER_VALUE"]
o={{"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"FAILED","result_pointer":None,"error":{{"code":"SAFE","origin":"SAFE","message":"ordinary"}}}}
raw=json.dumps(o,ensure_ascii=True,sort_keys=True,separators=(",",":")); escaped=json.dumps(s,ensure_ascii=True,separators=(",",":"))
if {duplicate_location!r}=="root": raw=raw.replace('"outcome":"FAILED"','"outcome":'+escaped+',"outcome":"FAILED"',1)
else: raw=raw.replace('"code":"SAFE"','"code":'+escaped+',"code":"SAFE"',1)
sys.stdout.write(raw+"\\n")'''
    fixture = _fixture(
        tmp_path,
        code=code,
        allowed=("OPAQUE_PROVIDER_VALUE",),
        secrets=(),
    )
    canary = "重复首值秘密"
    fixture["controls"]["provider_environment"] = {
        "OPAQUE_PROVIDER_VALUE": canary
    }
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    _assert_secret_safe_receipt_types(receipt, canary)
    assert receipt["stdout"] == {
        "size": 0,
        "sha256": hashlib.sha256(b"").hexdigest(),
        "truncated": True,
    }


def test_17_safe_duplicate_remains_output_invalid(tmp_path: Path) -> None:
    code = r'''import json,sys
r=json.load(sys.stdin)
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"FAILED","result_pointer":None,"error":{"code":"SAFE","origin":"SAFE","message":"ordinary"}}
raw=json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":")); raw=raw.replace('"outcome":"FAILED"','"outcome":"SAFE_FIRST","outcome":"FAILED"',1)
sys.stdout.write(raw+"\n")'''
    receipt = _launch(_fixture(tmp_path, code=code))
    _assert(receipt, "INCOMPLETE", "OUTPUT_INVALID", 1)
    assert receipt["stdout"]["size"] > 0
    assert receipt["stdout"]["truncated"] is False


def test_52_complete_secret_object_beats_trailing_data(
    tmp_path: Path,
) -> None:
    code = r'''import json,os,sys
r=json.load(sys.stdin); s=os.environ["OPAQUE_PROVIDER_VALUE"]
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"FAILED","result_pointer":None,"error":{"code":"SAFE","origin":"SAFE","message":"ordinary"},"unknown":s}
sys.stdout.write(json.dumps(o,ensure_ascii=True,sort_keys=True,separators=(",",":"))+" trailing\n")'''
    fixture = _fixture(
        tmp_path,
        code=code,
        allowed=("OPAQUE_PROVIDER_VALUE",),
        secrets=(),
    )
    canary = "尾随前秘密"
    fixture["controls"]["provider_environment"] = {
        "OPAQUE_PROVIDER_VALUE": canary
    }
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    _assert_secret_safe_receipt_types(receipt, canary)
    assert receipt["stdout"] == {
        "size": 0,
        "sha256": hashlib.sha256(b"").hexdigest(),
        "truncated": True,
    }


@pytest.mark.parametrize("leading", [" ", "\t", "\r", "\n"])
def test_52_escaped_secret_after_json_leading_whitespace_is_detected(
    tmp_path: Path, leading: str
) -> None:
    code = f'''import json,os,sys
r=json.load(sys.stdin); s=os.environ["OPAQUE_PROVIDER_VALUE"]
o={{"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"FAILED","result_pointer":None,"error":{{"code":"SAFE","origin":"SAFE","message":"ordinary"}},"unknown":s}}
sys.stdout.write({leading!r}+json.dumps(o,ensure_ascii=True,sort_keys=True,separators=(",",":"))+"\\n")'''
    fixture = _fixture(
        tmp_path,
        code=code,
        allowed=("OPAQUE_PROVIDER_VALUE",),
        secrets=(),
    )
    canary = "前导空白后秘密"
    fixture["controls"]["provider_environment"] = {
        "OPAQUE_PROVIDER_VALUE": canary
    }
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    _assert_secret_safe_receipt_types(receipt, canary)
    assert receipt["stdout"] == {
        "size": 0,
        "sha256": hashlib.sha256(b"").hexdigest(),
        "truncated": True,
    }


@pytest.mark.parametrize("prefix", [" ", "\ufeff"])
def test_17_safe_leading_space_or_bom_is_output_invalid(
    tmp_path: Path, prefix: str
) -> None:
    code = f'''import json,sys
r=json.load(sys.stdin)
o={{"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"FAILED","result_pointer":None,"error":{{"code":"SAFE","origin":"SAFE","message":"ordinary"}}}}
sys.stdout.write({prefix!r}+json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\\n")'''
    receipt = _launch(_fixture(tmp_path, code=code))
    _assert(receipt, "INCOMPLETE", "OUTPUT_INVALID", 1)
    assert receipt["error"]["origin"] == "OUTPUT"


def test_52_completed_secret_pair_beats_later_decoder_recursion_error(
    tmp_path: Path,
) -> None:
    code = r'''import json,os,sys
sys.stdin.buffer.read(); s=os.environ["OPAQUE_PROVIDER_VALUE"]; escaped=json.dumps(s,ensure_ascii=True,separators=(",",":"))
deep="["*3000+"0"+"]"*3000
sys.stdout.write('{"captured":{"value":'+escaped+'},"later":'+deep+'}\n')'''
    fixture = _fixture(
        tmp_path,
        code=code,
        allowed=("OPAQUE_PROVIDER_VALUE",),
        secrets=(),
    )
    canary = "递归错误前秘密"
    fixture["controls"]["provider_environment"] = {
        "OPAQUE_PROVIDER_VALUE": canary
    }
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    _assert_secret_safe_receipt_types(receipt, canary)
    assert receipt["stdout"] == {
        "size": 0,
        "sha256": hashlib.sha256(b"").hexdigest(),
        "truncated": True,
    }


def test_52_deep_decodable_secret_is_found_without_recursive_scan(
    tmp_path: Path,
) -> None:
    code = r'''import json,os,sys
sys.stdin.buffer.read(); s=os.environ["OPAQUE_PROVIDER_VALUE"]; escaped=json.dumps(s,ensure_ascii=True,separators=(",",":"))
deep="["*700+escaped+"]"*700
sys.stdout.write('{"deep":'+deep+'}\n')'''
    fixture = _fixture(
        tmp_path,
        code=code,
        allowed=("OPAQUE_PROVIDER_VALUE",),
        secrets=(),
    )
    canary = "深层秘密"
    fixture["controls"]["provider_environment"] = {
        "OPAQUE_PROVIDER_VALUE": canary
    }
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    _assert_secret_safe_receipt_types(receipt, canary)


def test_17_secret_free_decoder_recursion_is_output_invalid_not_a_crash(
    tmp_path: Path,
) -> None:
    code = r'''import sys
sys.stdin.buffer.read(); sys.stdout.write("["*3000+"0"+"]"*3000+"\n")'''
    receipt = _launch(_fixture(tmp_path, code=code))
    _assert(receipt, "INCOMPLETE", "OUTPUT_INVALID", 1)
    assert receipt["error"]["origin"] == "OUTPUT"


def test_55_bounded_dynamic_scan_handles_cycles_and_fails_closed_on_depth() -> None:
    cyclic: list[Any] = []
    cyclic.append(cyclic)
    assert not launcher_module._dynamic_value_contains_secret(cyclic, ("absent",))
    deep: Any = "ordinary"
    for _ in range(launcher_module._MAX_DYNAMIC_SCAN_DEPTH + 1):
        deep = [deep]
    with pytest.raises(launcher_module._DynamicScanIncomplete):
        launcher_module._dynamic_value_contains_secret(deep, ("absent",))


@pytest.mark.parametrize("later_token", ["NaN}", "]}", "1e999}"])
def test_52_nested_secret_pair_beats_later_parse_failure(
    tmp_path: Path, later_token: str
) -> None:
    code = f'''import json,os,sys
sys.stdin.buffer.read(); s=os.environ["OPAQUE_PROVIDER_VALUE"]; escaped=json.dumps(s,ensure_ascii=True,separators=(",",":"))
sys.stdout.write('{{"captured":{{"value":'+escaped+'}},"later":{later_token}\\n')'''
    fixture = _fixture(
        tmp_path,
        code=code,
        allowed=("OPAQUE_PROVIDER_VALUE",),
        secrets=(),
    )
    canary = "解析失败前秘密"
    fixture["controls"]["provider_environment"] = {
        "OPAQUE_PROVIDER_VALUE": canary
    }
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    _assert_secret_safe_receipt_types(receipt, canary)
    assert receipt["stdout"] == {
        "size": 0,
        "sha256": hashlib.sha256(b"").hexdigest(),
        "truncated": True,
    }


def test_17_safe_complete_object_with_trailing_data_remains_output_invalid(
    tmp_path: Path,
) -> None:
    code = r'''import json,sys
r=json.load(sys.stdin)
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"FAILED","result_pointer":None,"error":{"code":"SAFE","origin":"SAFE","message":"ordinary"}}
sys.stdout.write(json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))+" trailing\n")'''
    receipt = _launch(_fixture(tmp_path, code=code))
    _assert(receipt, "INCOMPLETE", "OUTPUT_INVALID", 1)
    assert receipt["stdout"]["size"] > 0
    assert receipt["stdout"]["truncated"] is False


def test_17_escaped_lone_surrogate_is_output_invalid_with_output_origin(
    tmp_path: Path,
) -> None:
    code = r'''import json,sys
r=json.load(sys.stdin)
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"FAILED","result_pointer":None,"error":{"code":"SAFE","origin":"SAFE","message":"\ud800"}}
sys.stdout.write(json.dumps(o,ensure_ascii=True,sort_keys=True,separators=(",",":"))+"\n")'''
    receipt = _launch(_fixture(tmp_path, code=code))
    _assert(receipt, "INCOMPLETE", "OUTPUT_INVALID", 1)
    assert receipt["error"]["origin"] == "OUTPUT"


def test_52_secret_flag_beats_lone_surrogate_serialization_failure(
    tmp_path: Path,
) -> None:
    code = r'''import json,os,sys
r=json.load(sys.stdin); s=os.environ["OPAQUE_PROVIDER_VALUE"]
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"FAILED","result_pointer":None,"error":{"code":"SAFE","origin":"SAFE","message":"\ud800"},"unknown":s}
sys.stdout.write(json.dumps(o,ensure_ascii=True,sort_keys=True,separators=(",",":"))+"\n")'''
    fixture = _fixture(
        tmp_path,
        code=code,
        allowed=("OPAQUE_PROVIDER_VALUE",),
        secrets=(),
    )
    canary = "代理项前秘密"
    fixture["controls"]["provider_environment"] = {
        "OPAQUE_PROVIDER_VALUE": canary
    }
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    _assert_secret_safe_receipt_types(receipt, canary)
    assert receipt["stdout"] == {
        "size": 0,
        "sha256": hashlib.sha256(b"").hexdigest(),
        "truncated": True,
    }


@pytest.mark.parametrize("numeric_token", ["NaN", "Infinity", "-Infinity", "1e999"])
def test_17_nonfinite_child_number_remains_output_invalid(
    tmp_path: Path, numeric_token: str
) -> None:
    code = f'''import json,sys
r=json.load(sys.stdin)
raw='{{"error":null,"outcome":"FAILED","request_id":'+json.dumps(r["request_id"])+',"result_pointer":null,"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":'+json.dumps(r["session_id"])+',"unknown":{numeric_token}}}'
sys.stdout.write(raw+"\\n")'''
    receipt = _launch(_fixture(tmp_path, code=code))
    _assert(receipt, "INCOMPLETE", "OUTPUT_INVALID", 1)


@pytest.mark.parametrize(
    "collision",
    ["user_message", "session_id", "request_id", "result_root"],
)
def test_24_secret_input_collisions_fail_closed_before_spawn(
    tmp_path: Path, collision: str
) -> None:
    fixture = _fixture(
        tmp_path, allowed=("DYNAMIC_TOKEN",), secrets=("DYNAMIC_TOKEN",)
    )
    message = "ordinary-message"
    if collision == "user_message":
        secret = "user-message-secret-canary"
        message = secret
    elif collision == "session_id":
        secret = fixture["controls"]["session_id"]
    elif collision == "request_id":
        secret = fixture["controls"]["request_id"]
    elif collision == "result_root":
        secret = fixture["controls"]["result_root"]
    fixture["controls"]["provider_environment"] = {"DYNAMIC_TOKEN": secret}
    receipt = _launch(fixture, message=message)
    _assert(receipt, "PRELAUNCH_BLOCKED", "INVALID_INPUT", 0)
    _assert_secret_safe_receipt_types(receipt, secret)


@pytest.mark.parametrize(
    "collision", ["package_release", "registration", "tool_path", "argv"]
)
def test_53_independent_package_authority_collision_is_not_secret_propagation(
    tmp_path: Path, collision: str
) -> None:
    fixture = _fixture(tmp_path, allowed=("DYNAMIC_TOKEN",), secrets=())
    if collision == "package_release":
        secret = RELEASE
    elif collision == "registration":
        located = registration.locate_active_package(fixture["candidate"].data_root)
        secret = located["registration_sha256"]
    elif collision == "tool_path":
        secret = str(
            fixture["candidate"].package_root.joinpath(
                *Path(fixture["definition"]["relative_path"]).parts
            ).resolve()
        )
    else:
        secret = "-c"
    fixture["controls"]["provider_environment"] = {"DYNAMIC_TOKEN": secret}
    receipt = _launch(fixture, message="ordinary-message")
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)


@pytest.mark.parametrize("canary", ["NONE", "EXITED_SUCCESS", "I"])
def test_48_fixed_protocol_token_collision_does_not_rewrite_closed_schema(
    tmp_path: Path, canary: str
) -> None:
    fixture = _fixture(tmp_path, allowed=("OPAQUE_PROVIDER_VALUE",), secrets=())
    fixture["controls"]["provider_environment"] = {"OPAQUE_PROVIDER_VALUE": canary}
    receipt = _launch(fixture)
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    assert receipt["schema_version"] == "golden-key-workbuddy-launcher-receipt-v1"
    assert receipt["error"] is None


def test_52_dynamic_result_path_collision_is_suppressed_after_success_parse(
    tmp_path: Path,
) -> None:
    fixture = _fixture(tmp_path, allowed=("OPAQUE_PROVIDER_VALUE",), secrets=())
    canary = str((fixture["result_root"] / "result.bin").resolve())
    fixture["controls"]["provider_environment"] = {"OPAQUE_PROVIDER_VALUE": canary}
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    _assert_secret_safe_receipt_types(receipt, canary)
    assert receipt["result_pointer"] == {
        "path": None, "sha256": None, "size": None, "valid": False,
    }


def test_53_allowlisted_provider_name_collision_is_not_value_propagation(
    tmp_path: Path,
) -> None:
    fixture = _fixture(
        tmp_path, allowed=("DYNAMIC_TOKEN_SLOT",), secrets=()
    )
    canary = "TOKEN"
    fixture["controls"]["provider_environment"] = {"DYNAMIC_TOKEN_SLOT": canary}
    receipt = _launch(fixture)
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    assert receipt["provider_environment_names"] == ("DYNAMIC_TOKEN_SLOT",)


def test_23_environment_allowlist_rejects_before_spawn(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path)
    fixture["controls"]["provider_environment"] = {"UNLISTED_PROVIDER": "x"}
    receipt = _launch(fixture)
    _assert(receipt, "PRELAUNCH_BLOCKED", "ENVIRONMENT_NOT_ALLOWED", 0)


def test_34_priority_level_03_preflight_failure_beats_spawn_failure(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fixture = _fixture(tmp_path)
    fixture["controls"]["provider_environment"] = {"UNLISTED_PROVIDER": "x"}
    calls = 0

    def should_not_spawn(*_args: Any, **_kwargs: Any):
        nonlocal calls
        calls += 1
        raise OSError("lower-priority spawn failure")

    monkeypatch.setattr(launcher_module.subprocess, "Popen", should_not_spawn)
    receipt = _launch(fixture)
    _assert(receipt, "PRELAUNCH_BLOCKED", "ENVIRONMENT_NOT_ALLOWED", 0)
    assert calls == 0


def test_22_dynamic_allowlisted_provider_is_opaque_and_passed_only_in_environment(tmp_path: Path) -> None:
    code = r'''import hashlib,json,os,pathlib,sys
r=json.load(sys.stdin); assert os.environ["FUTURE_IMAGE_PROVIDER_KEY"] not in json.dumps(r)
p=pathlib.Path(r["executor_controls"]["result_root"])/"result.bin"; p.write_bytes(b"ok")
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"SUCCEEDED","result_pointer":{"relative_path":"result.bin","sha256":hashlib.sha256(b"ok").hexdigest(),"size":2},"error":None}
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode())'''
    fixture = _fixture(tmp_path, code=code, allowed=("FUTURE_IMAGE_PROVIDER_KEY",), secrets=())
    fixture["controls"]["provider_environment"] = {"FUTURE_IMAGE_PROVIDER_KEY": "dynamic-secret"}
    receipt = _launch(fixture)
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    assert receipt["provider_environment_names"] == ("FUTURE_IMAGE_PROVIDER_KEY",)
    assert "dynamic-secret" not in repr(receipt)


def test_30_receipt_is_recursively_frozen_and_stage6_can_consume_shape(tmp_path: Path) -> None:
    receipt = _launch(_fixture(tmp_path))
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    assert isinstance(receipt, MappingProxyType)
    assert isinstance(receipt["package"], MappingProxyType)
    with pytest.raises(TypeError):
        receipt["outcome"] = "FAILED"
    stage6_view = (receipt["schema_version"], receipt["outcome"], receipt["result_pointer"]["valid"])
    assert stage6_view == ("golden-key-workbuddy-launcher-receipt-v1", "EXITED_SUCCESS", True)


@pytest.mark.parametrize("source", ["managed", "explicit", "PATH"])
def test_41_three_original_present_source_profiles_succeed(tmp_path: Path, source: str) -> None:
    seed = _fixture(tmp_path / "seed")
    requirement, evidence, _root = _local_evidence(seed, source=source)
    fixture = _fixture(tmp_path / "actual", requirements=(requirement,))
    # Recreate the source under the actual fixture DataRoot while preserving the approved definition.
    definition = evidence["approved_capability_definition"]
    payload = f"{definition['capability']}-asset".encode()
    if source == "managed":
        root = fixture["candidate"].data_root / "Runtime" / "Composition" / definition["capability"] / definition["definition_sha256"]
        root.mkdir(parents=True)
        entrypoint = root / "tool.exe"
    elif source == "explicit":
        root = Path(definition["explicit_registered_or_configured_candidate_paths"][0])
        entrypoint = root / "tool.exe"
    else:
        root = fixture["candidate"].data_root / "path-command.exe"
        entrypoint = root
        evidence["original_stage3_fact"]["evidence"]["runtime_root"] = str(root.resolve())
        evidence["original_stage3_fact"]["evidence"]["verified_entrypoint"] = str(root.resolve())
        evidence["original_stage3_fact"]["evidence"]["version_evidence"]["entrypoint"] = str(root.resolve())
    entrypoint.parent.mkdir(parents=True, exist_ok=True)
    entrypoint.write_bytes(payload)
    if source == "managed":
        evidence["original_stage3_fact"]["evidence"]["runtime_root"] = str(root.resolve())
        evidence["original_stage3_fact"]["evidence"]["verified_entrypoint"] = str(entrypoint.resolve())
        evidence["original_stage3_fact"]["evidence"]["version_evidence"]["entrypoint"] = str(entrypoint.resolve())
    evidence["original_stage3_fact_sha256"] = hashlib.sha256(_canonical(evidence["original_stage3_fact"], newline=False)).hexdigest()
    receipt = _launch(fixture, evidence=(evidence,))
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    assert receipt["local_capability_evidence_identities"][0]["source"] == source


def test_12_required_local_evidence_missing(tmp_path: Path) -> None:
    seed = _fixture(tmp_path / "seed")
    requirement, _evidence, _root = _local_evidence(seed, source="managed")
    receipt = _launch(_fixture(tmp_path / "actual", requirements=(requirement,)))
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_REQUIRED", 0)


def test_38_summary_only_or_mismatched_evidence_is_rejected(tmp_path: Path) -> None:
    seed = _fixture(tmp_path / "seed")
    requirement, _evidence, _root = _local_evidence(seed, source="managed")
    fixture = _fixture(tmp_path / "actual", requirements=(requirement,))
    receipt = _launch(fixture, evidence=({"schema_version": "golden-key-workbuddy-local-capability-evidence-v1"},))
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


def test_13_capability_entrypoint_identity_mismatch_is_rejected(tmp_path: Path) -> None:
    seed = _fixture(tmp_path / "seed")
    requirement, evidence, _root = _local_evidence(seed, source="explicit")
    wrong = tmp_path / "wrong-tool.exe"
    wrong.write_bytes(b"opaque-capability-asset")
    fact = evidence["original_stage3_fact"]["evidence"]
    fact["verified_entrypoint"] = str(wrong.resolve())
    fact["version_evidence"]["entrypoint"] = str(wrong.resolve())
    evidence["original_stage3_fact_sha256"] = hashlib.sha256(
        _canonical(evidence["original_stage3_fact"], newline=False)
    ).hexdigest()
    receipt = _launch(
        _fixture(tmp_path / "actual", requirements=(requirement,)), evidence=(evidence,)
    )
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("reason", "CALLER_ASSERTED_ONLY"),
        ("exit_code", 1),
        ("entrypoint", "relative-tool.exe"),
    ],
)
def test_40_untrusted_version_evidence_cannot_override_identity_rules(
    tmp_path: Path, field: str, value: Any
) -> None:
    seed = _fixture(tmp_path / "seed")
    requirement, evidence, _root = _local_evidence(seed, source="explicit")
    evidence["original_stage3_fact"]["evidence"]["version_evidence"][field] = value
    evidence["original_stage3_fact_sha256"] = hashlib.sha256(
        _canonical(evidence["original_stage3_fact"], newline=False)
    ).hexdigest()
    receipt = _launch(
        _fixture(tmp_path / "actual", requirements=(requirement,)), evidence=(evidence,)
    )
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


@pytest.mark.parametrize(
    "url",
    [
        "http://registry.npmmirror.com/pkg/-/tool.bin",
        "https://registry.npmmirror.com.evil.example/pkg/-/tool.bin",
        "https://registry.npmmirror.com:444/pkg/-/tool.bin",
        "https://user:password@registry.npmmirror.com/pkg/-/tool.bin",
        "https://registry.npmmirror.com/pkg/-/tool.bin?query=1",
        "https://registry.npmmirror.com/pkg/-/tool.bin#fragment",
        "https://registry.npmmirror.com:invalid/pkg/-/tool.bin",
        "https://registry.npmmirror.com",
    ],
)
def test_39_unapproved_mainland_source_url_variants_are_rejected(
    tmp_path: Path, url: str
) -> None:
    seed = _fixture(tmp_path / "seed")
    _old_requirement, evidence, _root = _local_evidence(seed, source="explicit")
    evidence["approved_capability_definition"]["approved_mainland_sources"][0]["url"] = url
    requirement = _rehash_stage3_evidence(evidence)
    receipt = _launch(
        _fixture(tmp_path / "actual", requirements=(requirement,)), evidence=(evidence,)
    )
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


def test_39_exact_npmmirror_https_port_443_source_remains_approved(tmp_path: Path) -> None:
    seed = _fixture(tmp_path / "seed")
    _old_requirement, evidence, _root = _local_evidence(seed, source="explicit")
    evidence["approved_capability_definition"]["approved_mainland_sources"][0]["url"] = (
        "https://registry.npmmirror.com:443/opaque-capability/-/tool.bin"
    )
    requirement = _rehash_stage3_evidence(evidence)
    receipt = _launch(
        _fixture(tmp_path / "actual", requirements=(requirement,)), evidence=(evidence,)
    )
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)


def test_42_managed_extra_file_breaks_closed_tree(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path / "actual")
    requirement, evidence, _root = _local_evidence(fixture, source="managed", add_extra=True)
    fixture = _fixture(tmp_path / "bound", requirements=(requirement,))
    definition = evidence["approved_capability_definition"]
    root = fixture["candidate"].data_root / "Runtime" / "Composition" / definition["capability"] / definition["definition_sha256"]
    root.mkdir(parents=True)
    (root / "tool.exe").write_bytes(f"{definition['capability']}-asset".encode())
    (root / "extra").mkdir()
    evidence["original_stage3_fact"]["evidence"]["runtime_root"] = str(root.resolve())
    evidence["original_stage3_fact"]["evidence"]["verified_entrypoint"] = str((root / "tool.exe").resolve())
    evidence["original_stage3_fact"]["evidence"]["version_evidence"]["entrypoint"] = str((root / "tool.exe").resolve())
    evidence["original_stage3_fact_sha256"] = hashlib.sha256(_canonical(evidence["original_stage3_fact"], newline=False)).hexdigest()
    receipt = _launch(fixture, evidence=(evidence,))
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


def test_43_explicit_drift_rejected_and_foreign_file_preserved(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path / "actual")
    requirement, evidence, root = _local_evidence(fixture, source="explicit", add_extra=True)
    fixture = _fixture(tmp_path / "bound", requirements=(requirement,))
    (root / "tool.exe").write_bytes(b"drifted-but-same-path")
    receipt = _launch(fixture, evidence=(evidence,))
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)
    assert (root / "foreign.txt").read_text(encoding="utf-8") == "preserve"
    assert (root / "foreign-directory" / "keep.txt").read_text(encoding="utf-8") == "keep"


def test_44_path_identity_drift_is_rejected(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path / "actual")
    requirement, evidence, root = _local_evidence(fixture, source="PATH")
    fixture = _fixture(tmp_path / "bound", requirements=(requirement,))
    root.write_bytes(b"replacement")
    receipt = _launch(fixture, evidence=(evidence,))
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


def test_44_path_command_nonabsolute_is_rejected(tmp_path: Path) -> None:
    seed = _fixture(tmp_path / "seed")
    requirement, evidence, _root = _local_evidence(seed, source="PATH")
    fact = evidence["original_stage3_fact"]["evidence"]
    fact["runtime_root"] = "relative-command.exe"
    fact["verified_entrypoint"] = "relative-command.exe"
    fact["version_evidence"]["entrypoint"] = "relative-command.exe"
    evidence["original_stage3_fact_sha256"] = hashlib.sha256(
        _canonical(evidence["original_stage3_fact"], newline=False)
    ).hexdigest()
    receipt = _launch(
        _fixture(tmp_path / "actual", requirements=(requirement,)), evidence=(evidence,)
    )
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


def test_44_path_command_nonregular_is_rejected(tmp_path: Path) -> None:
    seed = _fixture(tmp_path / "seed")
    requirement, evidence, root = _local_evidence(seed, source="PATH")
    root.unlink()
    root.mkdir()
    receipt = _launch(
        _fixture(tmp_path / "actual", requirements=(requirement,)), evidence=(evidence,)
    )
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


def test_44_path_command_reparse_component_is_rejected(tmp_path: Path) -> None:
    seed = _fixture(tmp_path / "seed")
    requirement, evidence, _root = _local_evidence(seed, source="PATH")
    real_dir = tmp_path / "path-real"
    real_dir.mkdir()
    command = real_dir / "opaque-capability.exe"
    command.write_bytes(b"opaque-capability-asset")
    alias_dir = tmp_path / "path-alias"
    _make_directory_reparse(alias_dir, real_dir)
    alias_command = alias_dir / command.name
    fact = evidence["original_stage3_fact"]["evidence"]
    fact["runtime_root"] = str(alias_command)
    fact["verified_entrypoint"] = str(alias_command)
    fact["version_evidence"]["entrypoint"] = str(alias_command)
    evidence["original_stage3_fact_sha256"] = hashlib.sha256(
        _canonical(evidence["original_stage3_fact"], newline=False)
    ).hexdigest()
    try:
        receipt = _launch(
            _fixture(tmp_path / "actual", requirements=(requirement,)), evidence=(evidence,)
        )
    finally:
        _remove_directory_reparse(alias_dir)
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


def test_45_integrated_nonmanaged_rejected(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path / "actual")
    requirement, evidence, _root = _local_evidence(fixture, source="explicit", status="INTEGRATED")
    fixture = _fixture(tmp_path / "bound", requirements=(requirement,))
    receipt = _launch(fixture, evidence=(evidence,))
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


def test_45_integrated_missing_plan_identity_is_rejected(tmp_path: Path) -> None:
    seed = _fixture(tmp_path / "seed")
    requirement, evidence, _root = _local_evidence(seed, source="managed", status="INTEGRATED")
    evidence["original_stage3_fact"].pop("plan_sha256")
    evidence["original_stage3_fact_sha256"] = hashlib.sha256(
        _canonical(evidence["original_stage3_fact"], newline=False)
    ).hexdigest()
    receipt = _launch(
        _fixture(tmp_path / "actual", requirements=(requirement,)), evidence=(evidence,)
    )
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


def test_46_managed_integrated_preserves_plan_and_reused_binding(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path / "actual")
    requirement, evidence, _root = _local_evidence(fixture, source="managed", status="INTEGRATED")
    fixture = _fixture(tmp_path / "bound", requirements=(requirement,))
    definition = evidence["approved_capability_definition"]
    root = fixture["candidate"].data_root / "Runtime" / "Composition" / definition["capability"] / definition["definition_sha256"]
    root.mkdir(parents=True)
    entrypoint = root / "tool.exe"
    entrypoint.write_bytes(f"{definition['capability']}-asset".encode())
    evidence["original_stage3_fact"]["runtime_root"] = str(root.resolve())
    evidence["original_stage3_fact"]["verified_entrypoint"] = str(entrypoint.resolve())
    evidence["original_stage3_fact"]["version_evidence"]["entrypoint"] = str(entrypoint.resolve())
    evidence["original_stage3_fact_sha256"] = hashlib.sha256(_canonical(evidence["original_stage3_fact"], newline=False)).hexdigest()
    receipt = _launch(fixture, evidence=(evidence,))
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    assert receipt["local_capability_evidence_identities"][0]["plan_sha256"] == "a" * 64


@pytest.mark.parametrize("status", ["PRESENT", "INTEGRATED"])
def test_55_managed_fact_identity_is_wholly_dynamic_for_secret_propagation(
    tmp_path: Path, status: str
) -> None:
    seed = _fixture(tmp_path / "seed")
    requirement, evidence, _root = _local_evidence(
        seed, source="managed", status=status
    )
    fixture = _fixture(
        tmp_path / "bound",
        allowed=("OPAQUE_PROVIDER_VALUE",),
        secrets=(),
        requirements=(requirement,),
    )
    definition = evidence["approved_capability_definition"]
    root = (
        fixture["candidate"].data_root
        / "Runtime"
        / "Composition"
        / definition["capability"]
        / definition["definition_sha256"]
    )
    root.mkdir(parents=True)
    entrypoint = root / "tool.exe"
    entrypoint.write_bytes(f"{definition['capability']}-asset".encode())
    fact = evidence["original_stage3_fact"]
    fact_fields = fact["evidence"] if status == "PRESENT" else fact
    fact_fields["runtime_root"] = str(root.resolve())
    fact_fields["verified_entrypoint"] = str(entrypoint.resolve())
    fact_fields["version_evidence"]["entrypoint"] = str(entrypoint.resolve())
    evidence["original_stage3_fact_sha256"] = hashlib.sha256(
        _canonical(fact, newline=False)
    ).hexdigest()
    canary = (
        evidence["original_stage3_fact_sha256"]
        if status == "PRESENT"
        else fact["plan_sha256"]
    )
    fixture["controls"]["provider_environment"] = {
        "OPAQUE_PROVIDER_VALUE": canary
    }
    receipt = _launch(fixture, evidence=(evidence,))
    _assert(receipt, "PRELAUNCH_BLOCKED", "INVALID_INPUT", 0)
    assert receipt["local_capability_evidence_identities"] == ()
    _assert_secret_safe_receipt_types(receipt, canary)


@pytest.mark.parametrize(
    ("status", "canary", "capability", "reused", "scalar_kind"),
    [
        pytest.param("PRESENT", "14", "capabxyz", None, "size", id="integer-14"),
        pytest.param("PRESENT", "15", "capabxyzz", None, "size", id="integer-15"),
        pytest.param("PRESENT", "null", "opaque-capability", None, "plan", id="null-plan"),
        pytest.param("INTEGRATED", "true", "opaque-capability", True, "reused", id="boolean-true"),
        pytest.param("INTEGRATED", "false", "opaque-capability", False, "reused", id="boolean-false"),
    ],
)
def test_55_canonical_json_scalars_in_local_fact_are_dynamic_secret_propagation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    status: str,
    canary: str,
    capability: str,
    reused: bool | None,
    scalar_kind: str,
) -> None:
    seed = _fixture(tmp_path / "seed")
    requirement, evidence, _root = _local_evidence(
        seed,
        source="managed",
        status=status,
        capability=capability,
    )
    fixture = _fixture(
        tmp_path / "bound",
        allowed=("OPAQUE_PROVIDER_VALUE",),
        secrets=(),
        requirements=(requirement,),
    )
    definition = evidence["approved_capability_definition"]
    root = (
        fixture["candidate"].data_root
        / "Runtime"
        / "Composition"
        / definition["capability"]
        / definition["definition_sha256"]
    )
    root.mkdir(parents=True)
    entrypoint = root / "tool.exe"
    payload = f"{definition['capability']}-asset".encode()
    entrypoint.write_bytes(payload)
    fact = evidence["original_stage3_fact"]
    fact_fields = fact["evidence"] if status == "PRESENT" else fact
    fact_fields["runtime_root"] = str(root.resolve())
    fact_fields["verified_entrypoint"] = str(entrypoint.resolve())
    fact_fields["version_evidence"]["entrypoint"] = str(entrypoint.resolve())
    if scalar_kind == "reused":
        fact["reused"] = reused
        scalar: Any = reused
    elif scalar_kind == "size":
        assert len(payload) == int(canary)
        assert fact_fields["asset_evidence"][0]["size"] == int(canary)
        scalar = fact_fields["asset_evidence"][0]["size"]
    else:
        assert status == "PRESENT"
        scalar = None
    evidence["original_stage3_fact_sha256"] = hashlib.sha256(
        _canonical(fact, newline=False)
    ).hexdigest()
    if scalar_kind == "plan":
        control = _launch(fixture, evidence=(evidence,))
        _assert(control, "EXITED_SUCCESS", "NONE", 1)
        assert control["local_capability_evidence_identities"][0][
            "plan_sha256"
        ] is None
    fixture["controls"]["provider_environment"] = {
        "OPAQUE_PROVIDER_VALUE": canary
    }
    assert launcher_module._dynamic_value_contains_secret(
        {"canonical_scalar": scalar}, (canary,)
    )
    monkeypatch.setattr(
        launcher_module,
        "_request_payload",
        lambda _first: pytest.fail("canonical stdin must not be constructed"),
    )
    receipt = _launch(fixture, evidence=(evidence,))
    _assert(receipt, "PRELAUNCH_BLOCKED", "INVALID_INPUT", 0)
    assert receipt["local_capability_evidence_identities"] == ()
    assert receipt["provider_environment_names"] == ("OPAQUE_PROVIDER_VALUE",)


def test_47_unknown_source_is_rejected(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path / "actual")
    requirement, evidence, _root = _local_evidence(fixture, source="managed")
    fixture = _fixture(tmp_path / "bound", requirements=(requirement,))
    evidence["original_stage3_fact"]["evidence"]["source"] = "unknown"
    evidence["original_stage3_fact_sha256"] = hashlib.sha256(_canonical(evidence["original_stage3_fact"], newline=False)).hexdigest()
    receipt = _launch(fixture, evidence=(evidence,))
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


def test_2_damaged_active_registration_fails_locator(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path)
    active = fixture["candidate"].data_root / "State" / "PackageRegistration" / "v1" / "active.json"
    active.write_bytes(b"damaged")
    receipt = _launch(fixture)
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCATOR_FAILED", 0)


def test_3_required_toolchain_drift_fails_locator(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path)
    fixture["candidate"].ffmpeg_path.write_bytes(b"drift")
    receipt = _launch(fixture)
    _assert(receipt, "PRELAUNCH_BLOCKED", "LOCATOR_FAILED", 0)


def test_08_real_tool_directory_junction_or_symlink_is_rejected_before_spawn(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fixture = _fixture(tmp_path)
    real_locator = launcher_module.locate_active_package
    tool_parent = fixture["candidate"].package_root / Path(fixture["definition"]["relative_path"]).parent
    real_parent = tool_parent.with_name(tool_parent.name + "-real")
    changed = False

    def link_after_real_locator(data_root: Any):
        nonlocal changed
        value = real_locator(data_root)
        if not changed:
            tool_parent.rename(real_parent)
            _make_directory_reparse(tool_parent, real_parent)
            changed = True
        return value

    monkeypatch.setattr(launcher_module, "locate_active_package", link_after_real_locator)
    try:
        receipt = _launch(fixture)
    finally:
        if tool_parent.exists() or tool_parent.is_symlink():
            _remove_directory_reparse(tool_parent)
        if real_parent.exists():
            real_parent.rename(tool_parent)
    _assert(receipt, "PRELAUNCH_BLOCKED", "TOOL_PATH_VIOLATION", 0)


def test_08_real_data_root_junction_or_symlink_alias_is_invalid_input(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path / "real")
    alias = tmp_path / "data-alias"
    _make_directory_reparse(alias, fixture["candidate"].data_root)
    try:
        receipt = launch_session_tool(
            alias, "x", fixture["controls"], fixture["definition"]
        )
    finally:
        _remove_directory_reparse(alias)
    _assert(receipt, "PRELAUNCH_BLOCKED", "INVALID_INPUT", 0)


def test_07_real_hardlink_alias_for_tool_is_rejected(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path)
    tool = fixture["candidate"].package_root.joinpath(
        *Path(fixture["definition"]["relative_path"]).parts
    )
    alias = tool.with_name("tool-hardlink-alias.exe")
    os.link(tool, alias)
    receipt = _launch(fixture)
    _assert(receipt, "PRELAUNCH_BLOCKED", "TOOL_PATH_VIOLATION", 0)


def test_19_residual_is_priority_level_05_and_wins_over_secret_and_nonzero(tmp_path: Path) -> None:
    code = r'''import hashlib,json,os,pathlib,subprocess,sys
r=json.load(sys.stdin)
subprocess.Popen([sys.executable,"-c","import time; time.sleep(30)"])
p=pathlib.Path(r["executor_controls"]["result_root"])/"result.bin"; p.write_bytes(b"ok")
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"SUCCEEDED","result_pointer":{"relative_path":"result.bin","sha256":hashlib.sha256(b"ok").hexdigest(),"size":2},"error":None}
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode()); sys.stdout.flush()
sys.stderr.write(os.environ["DYNAMIC_TOKEN"]); sys.stderr.flush(); sys.exit(9)'''
    fixture = _fixture(
        tmp_path, code=code, allowed=("DYNAMIC_TOKEN",), secrets=("DYNAMIC_TOKEN",)
    )
    fixture["controls"]["provider_environment"] = {"DYNAMIC_TOKEN": "residual-secret-canary"}
    receipt = _launch(fixture)
    _assert(receipt, "RESIDUAL_PROCESS", "RESIDUAL_PROCESS_DETECTED", 1, residual=True)
    assert receipt["residual_process"]["termination_attempted"] is True


def test_27_second_locator_identity_drift_blocks_spawn(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fixture = _fixture(tmp_path)
    real = launcher_module.locate_active_package
    calls = 0

    def drifting(data_root: Any):
        nonlocal calls
        calls += 1
        value = real(data_root)
        if calls == 2:
            return {**dict(value), "registration_sha256": "f" * 64}
        return value

    monkeypatch.setattr(launcher_module, "locate_active_package", drifting)
    receipt = _launch(fixture)
    _assert(receipt, "PRELAUNCH_BLOCKED", "REGISTRATION_DRIFT", 0)
    assert calls == 2


@pytest.mark.parametrize("execution_kind", ["DIRECT_EXECUTABLE", "PACKAGE_PYTHON_SCRIPT"])
def test_27_actual_tool_or_interpreter_replacement_after_second_locator_blocks_spawn(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, execution_kind: str
) -> None:
    fixture = _fixture(tmp_path, execution_kind=execution_kind)
    real_locator = launcher_module.locate_active_package
    calls = 0

    def replace_after_second_locator(data_root: Any):
        nonlocal calls
        calls += 1
        located = real_locator(data_root)
        if calls == 2:
            if execution_kind == "DIRECT_EXECUTABLE":
                target = fixture["candidate"].package_root.joinpath(
                    *Path(fixture["definition"]["relative_path"]).parts
                )
            else:
                target = Path(located["package_python"]["path"])
            target.write_bytes(b"X" * target.stat().st_size)
        return located

    monkeypatch.setattr(launcher_module, "locate_active_package", replace_after_second_locator)
    receipt = _launch(fixture)
    _assert(receipt, "PRELAUNCH_BLOCKED", "REGISTRATION_DRIFT", 0)
    assert calls == 2


def test_27_actual_result_root_reparse_after_second_locator_blocks_spawn(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fixture = _fixture(tmp_path)
    real_locator = launcher_module.locate_active_package
    result_root = fixture["result_root"]
    real_root = result_root.with_name("Results-real")
    calls = 0

    def replace_result_root_after_second_locator(data_root: Any):
        nonlocal calls
        calls += 1
        located = real_locator(data_root)
        if calls == 2:
            result_root.rename(real_root)
            _make_directory_reparse(result_root, real_root)
        return located

    monkeypatch.setattr(
        launcher_module, "locate_active_package", replace_result_root_after_second_locator
    )
    try:
        receipt = _launch(fixture)
    finally:
        if result_root.exists() or result_root.is_symlink():
            _remove_directory_reparse(result_root)
        if real_root.exists():
            real_root.rename(result_root)
    _assert(receipt, "PRELAUNCH_BLOCKED", "REGISTRATION_DRIFT", 0)
    assert calls == 2


def test_29_large_stream_is_fully_hashed_and_truncated_without_success(tmp_path: Path) -> None:
    size = 1024 * 1024 + 17
    code = f"import sys; sys.stdin.buffer.read(); sys.stderr.buffer.write(b'x'*{size}); sys.exit(4)"
    receipt = _launch(_fixture(tmp_path, code=code))
    _assert(receipt, "EXITED_NONZERO", "EXITED_NONZERO", 1)
    assert receipt["stderr"]["size"] == size
    assert receipt["stderr"]["sha256"] == hashlib.sha256(b"x" * size).hexdigest()
    assert receipt["stderr"]["truncated"] is True


def test_33_os_spawn_failure_is_priority_level_04_and_reports_zero_spawn(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fixture = _fixture(tmp_path)

    def denied(**_kwargs: Any):
        raise OSError("fixture denial")

    monkeypatch.setattr(launcher_module.subprocess, "Popen", denied)
    receipt = _launch(fixture)
    _assert(receipt, "SPAWN_FAILED", "SPAWN_OS_ERROR", 0)


def test_m13_ark_secret_canary_is_never_returned_by_fixed_child_boundary(tmp_path: Path) -> None:
    code = r'''import json,os,sys
r=json.load(sys.stdin); s=os.environ["ARK_API_KEY"]
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"FAILED","result_pointer":None,"error":{"code":"SAFE","origin":"SAFE","message":s}}
sys.stdout.write(json.dumps(o,sort_keys=True,separators=(",",":"))+"\n")'''
    fixture = _fixture(
        tmp_path,
        code=code,
        allowed=("ARK_API_KEY",),
        secrets=("ARK_API_KEY",),
    )
    fixture["controls"]["provider_environment"] = {"ARK_API_KEY": "m13-secret-canary"}

    receipt = _launch(fixture)

    _assert(receipt, "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    assert "m13-secret-canary" not in repr(receipt)


def test_28_cancel_after_spawn_terminates_without_retry_at_priority_level_07(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path, code="import sys,time; sys.stdin.buffer.read(); time.sleep(30)")
    event = threading.Event()
    timer = threading.Timer(0.2, event.set)
    timer.start()
    try:
        receipt = _launch(fixture, event=event)
    finally:
        timer.cancel()
    _assert(receipt, "CANCELLED", "CANCELLED", 1)
    assert receipt["cancelled"] is True


def test_28_windows_job_assign_failure_terminates_the_real_suspended_process(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fixture = _fixture(tmp_path, code="import sys,time; sys.stdin.buffer.read(); time.sleep(30)")
    if os.name == "nt":
        real_popen = launcher_module.subprocess.Popen
        popen_calls = 0

        def counted_popen(*args: Any, **kwargs: Any):
            nonlocal popen_calls
            popen_calls += 1
            assert kwargs["creationflags"] & getattr(
                subprocess, "CREATE_SUSPENDED", 0x00000004
            )
            return real_popen(*args, **kwargs)

        def assign_failure(self: Any, process: Any) -> None:
            assert process.poll() is None
            raise OSError("injected AssignProcessToJobObject failure")

        monkeypatch.setattr(launcher_module.subprocess, "Popen", counted_popen)
        monkeypatch.setattr(launcher_module._WindowsJob, "assign", assign_failure)
        events: list[str] | None = None
    else:
        events, popen_kwargs = _install_simulated_windows_lifecycle(
            monkeypatch, fixture, fail_at="assign"
        )
        popen_calls = len(popen_kwargs)
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "EVIDENCE_INCOMPLETE", 1)
    if events is not None:
        assert events[:2] == ["popen", "assign"]
        assert "resume" not in events
        assert "kill" in events and "wait" in events
        popen_calls = 1
    assert popen_calls == 1
    assert receipt["residual_process"]["termination_attempted"] is True
    assert receipt["residual_process"]["termination_succeeded"] is True
    assert receipt["exit_code"] is not None


def test_28_windows_resume_failure_terminates_the_bound_suspended_process(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fixture = _fixture(tmp_path, code="import sys,time; sys.stdin.buffer.read(); time.sleep(30)")
    if os.name == "nt":
        def resume_failure(self: Any, process: Any) -> None:
            assert process.poll() is None
            raise OSError("injected NtResumeProcess failure")

        monkeypatch.setattr(launcher_module._WindowsJob, "resume", resume_failure)
        events: list[str] | None = None
    else:
        events, _ = _install_simulated_windows_lifecycle(
            monkeypatch, fixture, fail_at="resume"
        )
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "EVIDENCE_INCOMPLETE", 1)
    if events is not None:
        assert events[:3] == ["popen", "assign", "resume"]
        assert "terminate" in events and "kill" in events and "wait" in events
    assert receipt["residual_process"]["termination_succeeded"] is True
    assert receipt["exit_code"] is not None


def test_28_windows_real_suspended_assign_resume_order_succeeds(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fixture = _fixture(tmp_path)
    if os.name == "nt":
        events: list[str] = []
        popen_kwargs: list[dict[str, Any]] = []
        real_popen = launcher_module.subprocess.Popen
        real_assign = launcher_module._WindowsJob.assign
        real_resume = launcher_module._WindowsJob.resume

        def ordered_popen(*args: Any, **kwargs: Any):
            events.append("popen")
            popen_kwargs.append(kwargs)
            return real_popen(*args, **kwargs)

        def ordered_assign(self: Any, process: Any) -> None:
            events.append("assign")
            real_assign(self, process)

        def ordered_resume(self: Any, process: Any) -> None:
            events.append("resume")
            real_resume(self, process)

        monkeypatch.setattr(launcher_module.subprocess, "Popen", ordered_popen)
        monkeypatch.setattr(launcher_module._WindowsJob, "assign", ordered_assign)
        monkeypatch.setattr(launcher_module._WindowsJob, "resume", ordered_resume)
    else:
        events, popen_kwargs = _install_simulated_windows_lifecycle(
            monkeypatch, fixture, fail_at=None
        )
    receipt = _launch(fixture)
    _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
    assert events[:3] == ["popen", "assign", "resume"]
    assert len(popen_kwargs) == 1
    assert popen_kwargs[0]["creationflags"] & getattr(
        subprocess, "CREATE_SUSPENDED", 0x00000004
    )


@pytest.mark.parametrize("fail_at", [None, "assign", "resume"])
def test_28_portable_windows_lifecycle_abstraction_has_no_skip(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, fail_at: str | None
) -> None:
    fixture = _fixture(tmp_path)
    events, popen_kwargs = _install_simulated_windows_lifecycle(
        monkeypatch, fixture, fail_at=fail_at
    )
    receipt = _launch(fixture)
    assert len(popen_kwargs) == 1
    assert popen_kwargs[0]["creationflags"] & getattr(
        subprocess, "CREATE_SUSPENDED", 0x00000004
    )
    if fail_at is None:
        _assert(receipt, "EXITED_SUCCESS", "NONE", 1)
        assert events[:3] == ["popen", "assign", "resume"]
    else:
        _assert(receipt, "INCOMPLETE", "EVIDENCE_INCOMPLETE", 1)
        assert events[:2] == ["popen", "assign"]
        assert "kill" in events and "wait" in events
        assert receipt["residual_process"]["termination_succeeded"] is True


def test_34_nine_outcomes_and_twenty_four_reasons_are_closed() -> None:
    assert launcher_module._OUTCOMES == {
        "PRELAUNCH_BLOCKED", "SPAWN_FAILED", "EXITED_SUCCESS", "EXITED_NONZERO",
        "CHILD_REPORTED_FAILURE", "TIMED_OUT", "CANCELLED", "INCOMPLETE", "RESIDUAL_PROCESS",
    }
    assert launcher_module._REASON_CODES == {
        "NONE", "INVALID_INPUT", "CANCELLED_BEFORE_SPAWN", "LOCATOR_FAILED", "REGISTRATION_DRIFT",
        "TOOL_DEFINITION_INVALID", "TOOL_DEFINITION_UNBOUND", "TOOL_PATH_VIOLATION",
        "TOOL_IDENTITY_MISMATCH", "INTERPRETER_IDENTITY_MISMATCH",
        "LOCAL_CAPABILITY_EVIDENCE_REQUIRED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH",
        "MANAGED_REMOTION_RUNTIME_INVALID",
        "ENVIRONMENT_NOT_ALLOWED", "SPAWN_OS_ERROR", "EXITED_NONZERO", "TIMEOUT", "CANCELLED",
        "CHILD_REPORTED_FAILURE", "OUTPUT_INVALID", "RESULT_POINTER_INVALID",
        "SECRET_DISCLOSURE_DETECTED", "EVIDENCE_INCOMPLETE", "RESIDUAL_PROCESS_DETECTED",
    }


def test_05_tool_requires_unique_manifest_and_lock_coverage(tmp_path: Path) -> None:
    receipt = _launch(_fixture(tmp_path, tool_locked=False))
    _assert(receipt, "PRELAUNCH_BLOCKED", "TOOL_IDENTITY_MISMATCH", 0)


@pytest.mark.parametrize(
    "fixture_kwargs",
    [
        pytest.param({"declared_tool_sha256": "f" * 64}, id="hash"),
        pytest.param({"declared_tool_size": 1}, id="size"),
        pytest.param({"definition_owner": "foreign_owner"}, id="owner"),
    ],
)
def test_06_tool_hash_size_or_owner_mismatch_is_distinct(
    tmp_path: Path, fixture_kwargs: dict[str, Any]
) -> None:
    receipt = _launch(_fixture(tmp_path, **fixture_kwargs))
    _assert(receipt, "PRELAUNCH_BLOCKED", "TOOL_IDENTITY_MISMATCH", 0)


def test_04_release_unbound_definition_has_distinct_reason(tmp_path: Path) -> None:
    unbound = _fixture(tmp_path / "unbound")
    unbound["definition"]["package_release"] = "different-release"
    _seal_definition(unbound["definition"])
    receipt = _launch(unbound)
    _assert(receipt, "PRELAUNCH_BLOCKED", "TOOL_DEFINITION_UNBOUND", 0)


def test_03_interpreter_identity_mismatch_is_distinct(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fixture = _fixture(tmp_path, execution_kind="PACKAGE_PYTHON_SCRIPT")
    real = launcher_module.locate_active_package

    def wrong_interpreter(data_root: Any):
        value = real(data_root)
        package_python = {**dict(value["package_python"]), "sha256": "f" * 64}
        return {**dict(value), "package_python": package_python}

    monkeypatch.setattr(launcher_module, "locate_active_package", wrong_interpreter)
    receipt = _launch(fixture)
    _assert(receipt, "PRELAUNCH_BLOCKED", "INTERPRETER_IDENTITY_MISMATCH", 0)


def test_17_result_pointer_hash_mismatch_is_incomplete(tmp_path: Path) -> None:
    code = r'''import json,pathlib,sys
r=json.load(sys.stdin); p=pathlib.Path(r["executor_controls"]["result_root"])/"result.bin"; p.write_bytes(b"ok")
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"SUCCEEDED","result_pointer":{"relative_path":"result.bin","sha256":"ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff","size":2},"error":None}
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode())'''
    receipt = _launch(_fixture(tmp_path, code=code))
    _assert(receipt, "INCOMPLETE", "RESULT_POINTER_INVALID", 1)


def test_17_result_pointer_replacement_between_lstat_and_open_is_detected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    fixture = _fixture(tmp_path)
    pointer = fixture["result_root"] / "result.bin"
    replacement = fixture["result_root"] / "replacement.bin"
    real_open = launcher_module.os.open
    replaced = False
    opened: list[str] = []

    def replace_before_real_open(path: Any, *args: Any, **kwargs: Any):
        nonlocal replaced
        opened.append(str(path))
        try:
            same_path = os.path.normcase(os.path.abspath(os.fspath(path))) == os.path.normcase(
                os.path.abspath(os.fspath(pointer))
            )
        except (OSError, RuntimeError, ValueError):
            same_path = False
        if same_path and pointer.exists() and not replaced:
            replacement.write_bytes(b"fixture-result")
            os.replace(replacement, pointer)
            replaced = True
        return real_open(path, *args, **kwargs)

    monkeypatch.setattr(launcher_module.os, "open", replace_before_real_open)
    receipt = _launch(fixture)
    _assert(receipt, "INCOMPLETE", "RESULT_POINTER_INVALID", 1)
    assert replaced is True, (opened, pointer, dict(receipt))


def test_17_result_pointer_reparse_parent_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    code = r'''import hashlib,json,pathlib,sys
r=json.load(sys.stdin); root=pathlib.Path(r["executor_controls"]["result_root"])
p=root/"real"/"result.bin"; p.parent.mkdir(); p.write_bytes(b"ok")
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"SUCCEEDED","result_pointer":{"relative_path":"alias/result.bin","sha256":hashlib.sha256(b"ok").hexdigest(),"size":2},"error":None}
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode())'''
    fixture = _fixture(tmp_path, code=code)
    alias = fixture["result_root"] / "alias"
    real = fixture["result_root"] / "real"
    original_parse = launcher_module._parse_result

    def add_actual_reparse(raw: bytes, first: Any):
        result = original_parse(raw, first)
        _make_directory_reparse(alias, real)
        return result

    monkeypatch.setattr(launcher_module, "_parse_result", add_actual_reparse)
    try:
        receipt = _launch(fixture)
    finally:
        if alias.exists() or alias.is_symlink():
            _remove_directory_reparse(alias)
    _assert(receipt, "INCOMPLETE", "RESULT_POINTER_INVALID", 1)


def test_31_unclassified_preflight_error_is_evidence_incomplete(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fixture = _fixture(tmp_path)

    def broken_inventory(*_args: Any, **_kwargs: Any):
        raise RuntimeError("fixture internal failure")

    monkeypatch.setattr(launcher_module, "_inventory", broken_inventory)
    receipt = _launch(fixture)
    _assert(receipt, "PRELAUNCH_BLOCKED", "EVIDENCE_INCOMPLETE", 0)


def test_31_unreadable_input_still_returns_full_receipt_with_none_hints(tmp_path: Path) -> None:
    receipt = launch_session_tool(
        tmp_path / "missing",
        "\ud800",
        {"session_id": object(), "request_id": object()},
        {},
    )
    _assert(receipt, "PRELAUNCH_BLOCKED", "INVALID_INPUT", 0)
    assert len(receipt) == 31
    assert receipt["session"]["session_id"] is None
    assert receipt["request"]["request_id"] is None
    assert receipt["user_message"]["sha256"] is None
    assert receipt["user_message"]["byte_length"] is None


def test_34_priority_level_01_invalid_cancel_event_has_highest_precedence(tmp_path: Path) -> None:
    receipt = launch_session_tool(tmp_path / "missing", "x", {}, {}, cancel_event=object())  # type: ignore[arg-type]
    _assert(receipt, "PRELAUNCH_BLOCKED", "INVALID_INPUT", 0)


@pytest.mark.parametrize(
    "relative_path",
    ["../escape", "tools/file:stream", "tools/CON.txt", "tools/trailing."],
)
def test_07_escape_ads_or_windows_alias_is_a_path_violation(
    tmp_path: Path, relative_path: str
) -> None:
    fixture = _fixture(tmp_path)
    fixture["definition"]["relative_path"] = relative_path
    receipt = _launch(fixture)
    _assert(receipt, "PRELAUNCH_BLOCKED", "TOOL_PATH_VIOLATION", 0)
