from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import threading
from pathlib import Path
from types import MappingProxyType
from typing import Any

import pytest

from golden_key_openmontage_workbuddy import launch_session_tool
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


MATRIX = {
    1: "no active registration", 2: "registration damage or drift", 3: "required toolchain drift",
    4: "definition closed shape and self hash", 5: "manifest and lock coverage", 6: "tool identity",
    7: "unsafe relative path", 8: "reparse component", 9: "argv injection", 10: "literal message bytes",
    11: "controls separate from message", 12: "required local evidence", 13: "local identity mismatch",
    14: "base path has no named runtime requirement", 15: "nonzero exit", 16: "timeout",
    17: "result envelope and pointer", 18: "secret disclosure", 19: "residual process",
    20: "single spawn no retry", 21: "no control plane", 22: "opaque provider and capability",
    23: "environment allowlist", 24: "secret absent from request and receipt", 25: "provider absence is not local evidence",
    26: "only declared local requirements", 27: "second preflight drift", 28: "cancel lifecycle",
    29: "stream size hash truncation", 30: "recursive freeze", 31: "invalid input full receipt",
    32: "entry cancel before locator", 33: "OS spawn failure", 34: "outcome priority",
    35: "child reported failure", 36: "definition excludes registration hashes", 37: "real Stage2 roundtrip",
    38: "reject summary-only evidence", 39: "source asset revalidation", 40: "version evidence not trusted",
    41: "managed explicit PATH success", 42: "managed closed tree", 43: "explicit foreign files retained",
    44: "PATH command identity", 45: "integrated is managed only", 46: "integrated plan identity",
    47: "unknown source",
}


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


def _fixture(
    tmp_path: Path,
    *,
    execution_kind: str = "DIRECT_EXECUTABLE",
    code: str = SUCCESS_CODE,
    allowed: tuple[str, ...] = (),
    secrets: tuple[str, ...] = (),
    requirements: tuple[dict[str, Any], ...] = (),
    declared_tool_sha256: str | None = None,
) -> dict[str, Any]:
    candidate = _make_candidate(tmp_path / "candidate", python_payload=Path(sys.executable).read_bytes())
    pyvenv = candidate.package_python.parent / "pyvenv.cfg"
    shutil.copy2(Path(sys.prefix) / "pyvenv.cfg", pyvenv)
    _add_package_file(
        candidate, pyvenv, pyvenv.relative_to(candidate.package_root).as_posix(),
        registration.REQUIRED_TOOLCHAIN_OWNER, locked=False,
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
        tool_config = tool.parent / "pyvenv.cfg"
        shutil.copy2(Path(sys.prefix) / "pyvenv.cfg", tool_config)
        _add_package_file(candidate, tool_config, tool_config.relative_to(candidate.package_root).as_posix(), "managed_core", locked=True)
        template = ["-c", code]
        placeholders = []
        binding = "SELF"
    relative_tool = tool.relative_to(candidate.package_root).as_posix()
    _add_package_file(candidate, tool, relative_tool, "managed_core", locked=True)
    definition_path = candidate.package_root / "definitions" / "session-tool.json"
    definition_path.parent.mkdir(parents=True)
    definition = {
        "schema_version": "golden-key-workbuddy-package-tool-definition-v1",
        "definition_id": "fixture-session-tool", "definition_sha256": "0" * 64,
        "definition_relative_path": definition_path.relative_to(candidate.package_root).as_posix(),
        "authority_owner": "managed_core", "package_release": RELEASE, "package_commit": COMMIT,
        "tool_id": "fixture-tool", "relative_path": relative_tool, "sha256": declared_tool_sha256 or _sha256(tool),
        "size": tool.stat().st_size, "owner": "managed_core", "execution_kind": execution_kind,
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


def _launch(fixture: dict[str, Any], *, message: str = "原样业务请求", evidence: Any = (), event: threading.Event | None = None):
    return launch_session_tool(
        fixture["candidate"].data_root, message, fixture["controls"], fixture["definition"], evidence, event
    )


def _assert(receipt: Any, case_ids: tuple[int, ...], outcome: str, reason: str, spawn: int, residual: bool = False) -> None:
    assert set(case_ids) <= set(MATRIX)
    assert receipt["outcome"] == outcome, dict(receipt)
    assert receipt["reason_code"] == reason, dict(receipt)
    assert receipt["spawn_count"] == spawn
    assert receipt["residual_process"]["detected"] is residual
    assert receipt["retry_count"] == 0


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
) -> tuple[dict[str, Any], dict[str, Any], Path]:
    capability = "opaque-capability"
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


def test_37_real_stage2_roundtrip_and_direct_success_covers_base_boundaries(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path)
    receipt = _launch(fixture)
    _assert(receipt, (10, 11, 14, 20, 21, 22, 25, 26, 36, 37), "EXITED_SUCCESS", "NONE", 1)
    assert receipt["result_pointer"]["valid"] is True
    assert receipt["user_message"]["sha256"] == hashlib.sha256("原样业务请求".encode()).hexdigest()
    assert receipt["provider_environment_names"] == ()


def test_python_script_execution_kind_succeeds(tmp_path: Path) -> None:
    receipt = _launch(_fixture(tmp_path, execution_kind="PACKAGE_PYTHON_SCRIPT"))
    _assert(receipt, (9,), "EXITED_SUCCESS", "NONE", 1)


def test_1_no_active_registration_returns_full_receipt(tmp_path: Path) -> None:
    data = tmp_path / "data"
    data.mkdir()
    receipt = launch_session_tool(data, "x", {}, {})
    _assert(receipt, (1, 31), "PRELAUNCH_BLOCKED", "LOCATOR_FAILED", 0)
    assert len(receipt) == 30


def test_32_entry_cancel_precedes_locator(tmp_path: Path) -> None:
    event = threading.Event()
    event.set()
    receipt = launch_session_tool(tmp_path / "missing", "x", {"session_id": "s", "request_id": "r"}, {}, cancel_event=event)
    _assert(receipt, (28, 32), "CANCELLED", "CANCELLED_BEFORE_SPAWN", 0)
    assert receipt["cancelled"] is True


@pytest.mark.parametrize(
    ("mutation", "reason", "case_ids"),
    [
        (lambda d: d.pop("tool_id"), "TOOL_DEFINITION_INVALID", (4,)),
        (lambda d: d.__setitem__("definition_sha256", "f" * 64), "TOOL_DEFINITION_INVALID", (4,)),
        (lambda d: d.__setitem__("fixed_argv_template", ["--bad"]), "TOOL_DEFINITION_INVALID", (9,)),
        (lambda d: d.__setitem__("relative_path", "../bad"), "TOOL_PATH_VIOLATION", (7,)),
        (lambda d: d.__setitem__("sha256", "f" * 64), "TOOL_DEFINITION_INVALID", (5, 6)),
    ],
)
def test_definition_and_tool_fail_closed(tmp_path: Path, mutation, reason: str, case_ids: tuple[int, ...]) -> None:
    fixture = _fixture(tmp_path)
    mutation(fixture["definition"])
    receipt = _launch(fixture)
    _assert(receipt, case_ids, "PRELAUNCH_BLOCKED", reason, 0)


def test_15_nonzero_exit_is_preserved(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path, code="import sys; sys.stdin.buffer.read(); sys.exit(7)")
    receipt = _launch(fixture)
    _assert(receipt, (15, 34), "EXITED_NONZERO", "EXITED_NONZERO", 1)
    assert receipt["exit_code"] == 7


def test_16_timeout_terminates_owned_tree(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path, code="import sys,time; sys.stdin.buffer.read(); time.sleep(30)")
    fixture["controls"]["timeout_seconds"] = 1
    receipt = _launch(fixture)
    _assert(receipt, (16,), "TIMED_OUT", "TIMEOUT", 1)
    assert receipt["timed_out"] is True
    assert receipt["residual_process"]["termination_attempted"] is True


def test_35_child_reported_failure(tmp_path: Path) -> None:
    receipt = _launch(_fixture(tmp_path, code=FAILED_CODE))
    _assert(receipt, (35,), "CHILD_REPORTED_FAILURE", "CHILD_REPORTED_FAILURE", 1)


def test_17_invalid_output_and_pointer_are_incomplete(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path, code="import sys; sys.stdin.buffer.read(); print('not-json')")
    receipt = _launch(fixture)
    _assert(receipt, (17, 34), "INCOMPLETE", "OUTPUT_INVALID", 1)


def test_18_secret_disclosure_wins_over_nonzero(tmp_path: Path) -> None:
    code = "import os,sys; sys.stdin.buffer.read(); print(os.environ['DYNAMIC_TOKEN']); sys.exit(9)"
    fixture = _fixture(tmp_path, code=code, allowed=("DYNAMIC_TOKEN",), secrets=("DYNAMIC_TOKEN",))
    fixture["controls"]["provider_environment"] = {"DYNAMIC_TOKEN": "split-canary-secret"}
    receipt = _launch(fixture)
    _assert(receipt, (18, 24, 34), "INCOMPLETE", "SECRET_DISCLOSURE_DETECTED", 1)
    assert "split-canary-secret" not in repr(receipt)


def test_23_environment_allowlist_rejects_before_spawn(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path)
    fixture["controls"]["provider_environment"] = {"UNLISTED_PROVIDER": "x"}
    receipt = _launch(fixture)
    _assert(receipt, (23,), "PRELAUNCH_BLOCKED", "ENVIRONMENT_NOT_ALLOWED", 0)


def test_dynamic_allowlisted_provider_is_passed_without_entering_request(tmp_path: Path) -> None:
    code = r'''import hashlib,json,os,pathlib,sys
r=json.load(sys.stdin); assert os.environ["FUTURE_IMAGE_PROVIDER_KEY"] not in json.dumps(r)
p=pathlib.Path(r["executor_controls"]["result_root"])/"result.bin"; p.write_bytes(b"ok")
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"SUCCEEDED","result_pointer":{"relative_path":"result.bin","sha256":hashlib.sha256(b"ok").hexdigest(),"size":2},"error":None}
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode())'''
    fixture = _fixture(tmp_path, code=code, allowed=("FUTURE_IMAGE_PROVIDER_KEY",), secrets=())
    fixture["controls"]["provider_environment"] = {"FUTURE_IMAGE_PROVIDER_KEY": "dynamic-secret"}
    receipt = _launch(fixture)
    _assert(receipt, (22, 24, 25), "EXITED_SUCCESS", "NONE", 1)
    assert receipt["provider_environment_names"] == ("FUTURE_IMAGE_PROVIDER_KEY",)
    assert "dynamic-secret" not in repr(receipt)


def test_30_receipt_is_recursively_frozen_and_stage6_can_consume_shape(tmp_path: Path) -> None:
    receipt = _launch(_fixture(tmp_path))
    _assert(receipt, (30,), "EXITED_SUCCESS", "NONE", 1)
    assert isinstance(receipt, MappingProxyType)
    assert isinstance(receipt["package"], MappingProxyType)
    with pytest.raises(TypeError):
        receipt["outcome"] = "FAILED"
    stage6_view = (receipt["schema_version"], receipt["outcome"], receipt["result_pointer"]["valid"])
    assert stage6_view == ("golden-key-workbuddy-launcher-receipt-v1", "EXITED_SUCCESS", True)


def test_matrix_has_exactly_47_traceable_categories() -> None:
    assert set(MATRIX) == set(range(1, 48))


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
    _assert(receipt, (39, 40, 41), "EXITED_SUCCESS", "NONE", 1)
    assert receipt["local_capability_evidence_identities"][0]["source"] == source


def test_12_required_local_evidence_missing(tmp_path: Path) -> None:
    seed = _fixture(tmp_path / "seed")
    requirement, _evidence, _root = _local_evidence(seed, source="managed")
    receipt = _launch(_fixture(tmp_path / "actual", requirements=(requirement,)))
    _assert(receipt, (12,), "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_REQUIRED", 0)


def test_38_summary_only_or_mismatched_evidence_is_rejected(tmp_path: Path) -> None:
    seed = _fixture(tmp_path / "seed")
    requirement, _evidence, _root = _local_evidence(seed, source="managed")
    fixture = _fixture(tmp_path / "actual", requirements=(requirement,))
    receipt = _launch(fixture, evidence=({"schema_version": "golden-key-workbuddy-local-capability-evidence-v1"},))
    _assert(receipt, (13, 38), "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


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
    _assert(receipt, (42,), "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


def test_43_explicit_drift_rejected_and_foreign_file_preserved(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path / "actual")
    requirement, evidence, root = _local_evidence(fixture, source="explicit", add_extra=True)
    fixture = _fixture(tmp_path / "bound", requirements=(requirement,))
    (root / "tool.exe").write_bytes(b"drifted-but-same-path")
    receipt = _launch(fixture, evidence=(evidence,))
    _assert(receipt, (43,), "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)
    assert (root / "foreign.txt").read_text(encoding="utf-8") == "preserve"


def test_44_path_identity_drift_is_rejected(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path / "actual")
    requirement, evidence, root = _local_evidence(fixture, source="PATH")
    fixture = _fixture(tmp_path / "bound", requirements=(requirement,))
    root.write_bytes(b"replacement")
    receipt = _launch(fixture, evidence=(evidence,))
    _assert(receipt, (44,), "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


def test_45_integrated_nonmanaged_rejected(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path / "actual")
    requirement, evidence, _root = _local_evidence(fixture, source="explicit", status="INTEGRATED")
    fixture = _fixture(tmp_path / "bound", requirements=(requirement,))
    receipt = _launch(fixture, evidence=(evidence,))
    _assert(receipt, (45,), "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


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
    _assert(receipt, (46,), "EXITED_SUCCESS", "NONE", 1)
    assert receipt["local_capability_evidence_identities"][0]["plan_sha256"] == "a" * 64


def test_47_unknown_source_is_rejected(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path / "actual")
    requirement, evidence, _root = _local_evidence(fixture, source="managed")
    fixture = _fixture(tmp_path / "bound", requirements=(requirement,))
    evidence["original_stage3_fact"]["evidence"]["source"] = "unknown"
    evidence["original_stage3_fact_sha256"] = hashlib.sha256(_canonical(evidence["original_stage3_fact"], newline=False)).hexdigest()
    receipt = _launch(fixture, evidence=(evidence,))
    _assert(receipt, (47,), "PRELAUNCH_BLOCKED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH", 0)


def test_2_damaged_active_registration_fails_locator(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path)
    active = fixture["candidate"].data_root / "State" / "PackageRegistration" / "v1" / "active.json"
    active.write_bytes(b"damaged")
    receipt = _launch(fixture)
    _assert(receipt, (2,), "PRELAUNCH_BLOCKED", "LOCATOR_FAILED", 0)


def test_3_required_toolchain_drift_fails_locator(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path)
    fixture["candidate"].ffmpeg_path.write_bytes(b"drift")
    receipt = _launch(fixture)
    _assert(receipt, (3,), "PRELAUNCH_BLOCKED", "LOCATOR_FAILED", 0)


def test_8_reparse_component_is_rejected_before_spawn(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fixture = _fixture(tmp_path)
    real = launcher_module._is_reparse
    tool_parent = Path(fixture["definition"]["relative_path"]).parent.as_posix()

    def selected(path: Path) -> bool:
        if path.as_posix().endswith(tool_parent):
            return True
        return real(path)

    monkeypatch.setattr(launcher_module, "_is_reparse", selected)
    receipt = _launch(fixture)
    _assert(receipt, (8,), "PRELAUNCH_BLOCKED", "TOOL_PATH_VIOLATION", 0)


def test_19_background_descendant_is_residual_and_is_terminated(tmp_path: Path) -> None:
    code = r'''import hashlib,json,pathlib,subprocess,sys
r=json.load(sys.stdin)
subprocess.Popen([sys.executable,"-c","import time; time.sleep(30)"])
p=pathlib.Path(r["executor_controls"]["result_root"])/"result.bin"; p.write_bytes(b"ok")
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"SUCCEEDED","result_pointer":{"relative_path":"result.bin","sha256":hashlib.sha256(b"ok").hexdigest(),"size":2},"error":None}
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode())'''
    receipt = _launch(_fixture(tmp_path, code=code))
    _assert(receipt, (19,), "RESIDUAL_PROCESS", "RESIDUAL_PROCESS_DETECTED", 1, residual=True)
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
    _assert(receipt, (27,), "PRELAUNCH_BLOCKED", "REGISTRATION_DRIFT", 0)
    assert calls == 2


def test_29_large_stream_is_fully_hashed_and_truncated_without_success(tmp_path: Path) -> None:
    size = 1024 * 1024 + 17
    code = f"import sys; sys.stdin.buffer.read(); sys.stderr.buffer.write(b'x'*{size}); sys.exit(4)"
    receipt = _launch(_fixture(tmp_path, code=code))
    _assert(receipt, (29,), "EXITED_NONZERO", "EXITED_NONZERO", 1)
    assert receipt["stderr"]["size"] == size
    assert receipt["stderr"]["sha256"] == hashlib.sha256(b"x" * size).hexdigest()
    assert receipt["stderr"]["truncated"] is True


def test_33_os_spawn_failure_reports_zero_spawn(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fixture = _fixture(tmp_path)

    def denied(**_kwargs: Any):
        raise OSError("fixture denial")

    monkeypatch.setattr(launcher_module.subprocess, "Popen", denied)
    receipt = _launch(fixture)
    _assert(receipt, (33,), "SPAWN_FAILED", "SPAWN_OS_ERROR", 0)


def test_cancel_after_spawn_terminates_without_retry(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path, code="import sys,time; sys.stdin.buffer.read(); time.sleep(30)")
    event = threading.Event()
    timer = threading.Timer(0.2, event.set)
    timer.start()
    try:
        receipt = _launch(fixture, event=event)
    finally:
        timer.cancel()
    _assert(receipt, (28, 34), "CANCELLED", "CANCELLED", 1)
    assert receipt["cancelled"] is True


def test_nine_outcomes_and_twenty_three_reasons_are_closed() -> None:
    assert launcher_module._OUTCOMES == {
        "PRELAUNCH_BLOCKED", "SPAWN_FAILED", "EXITED_SUCCESS", "EXITED_NONZERO",
        "CHILD_REPORTED_FAILURE", "TIMED_OUT", "CANCELLED", "INCOMPLETE", "RESIDUAL_PROCESS",
    }
    assert launcher_module._REASON_CODES == {
        "NONE", "INVALID_INPUT", "CANCELLED_BEFORE_SPAWN", "LOCATOR_FAILED", "REGISTRATION_DRIFT",
        "TOOL_DEFINITION_INVALID", "TOOL_DEFINITION_UNBOUND", "TOOL_PATH_VIOLATION",
        "TOOL_IDENTITY_MISMATCH", "INTERPRETER_IDENTITY_MISMATCH",
        "LOCAL_CAPABILITY_EVIDENCE_REQUIRED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH",
        "ENVIRONMENT_NOT_ALLOWED", "SPAWN_OS_ERROR", "EXITED_NONZERO", "TIMEOUT", "CANCELLED",
        "CHILD_REPORTED_FAILURE", "OUTPUT_INVALID", "RESULT_POINTER_INVALID",
        "SECRET_DISCLOSURE_DETECTED", "EVIDENCE_INCOMPLETE", "RESIDUAL_PROCESS_DETECTED",
    }


def test_unbound_definition_and_declared_tool_mismatch_have_distinct_reasons(tmp_path: Path) -> None:
    mismatch = _fixture(tmp_path / "mismatch", declared_tool_sha256="f" * 64)
    receipt = _launch(mismatch)
    _assert(receipt, (5, 6), "PRELAUNCH_BLOCKED", "TOOL_IDENTITY_MISMATCH", 0)

    unbound = _fixture(tmp_path / "unbound")
    unbound["definition"]["package_release"] = "different-release"
    _seal_definition(unbound["definition"])
    receipt = _launch(unbound)
    _assert(receipt, (4,), "PRELAUNCH_BLOCKED", "TOOL_DEFINITION_UNBOUND", 0)


def test_interpreter_identity_mismatch_is_distinct(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fixture = _fixture(tmp_path, execution_kind="PACKAGE_PYTHON_SCRIPT")
    real = launcher_module.locate_active_package

    def wrong_interpreter(data_root: Any):
        value = real(data_root)
        package_python = {**dict(value["package_python"]), "sha256": "f" * 64}
        return {**dict(value), "package_python": package_python}

    monkeypatch.setattr(launcher_module, "locate_active_package", wrong_interpreter)
    receipt = _launch(fixture)
    _assert(receipt, (3,), "PRELAUNCH_BLOCKED", "INTERPRETER_IDENTITY_MISMATCH", 0)


def test_result_pointer_hash_mismatch_is_incomplete(tmp_path: Path) -> None:
    code = r'''import json,pathlib,sys
r=json.load(sys.stdin); p=pathlib.Path(r["executor_controls"]["result_root"])/"result.bin"; p.write_bytes(b"ok")
o={"schema_version":"golden-key-workbuddy-package-tool-result-v1","session_id":r["session_id"],"request_id":r["request_id"],"outcome":"SUCCEEDED","result_pointer":{"relative_path":"result.bin","sha256":"ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff","size":2},"error":None}
sys.stdout.buffer.write((json.dumps(o,ensure_ascii=False,sort_keys=True,separators=(",",":"))+"\n").encode())'''
    receipt = _launch(_fixture(tmp_path, code=code))
    _assert(receipt, (17,), "INCOMPLETE", "RESULT_POINTER_INVALID", 1)


def test_unclassified_preflight_error_is_evidence_incomplete(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    fixture = _fixture(tmp_path)

    def broken_inventory(*_args: Any, **_kwargs: Any):
        raise RuntimeError("fixture internal failure")

    monkeypatch.setattr(launcher_module, "_inventory", broken_inventory)
    receipt = _launch(fixture)
    _assert(receipt, (31,), "PRELAUNCH_BLOCKED", "EVIDENCE_INCOMPLETE", 0)


def test_invalid_cancel_event_has_highest_precedence(tmp_path: Path) -> None:
    receipt = launch_session_tool(tmp_path / "missing", "x", {}, {}, cancel_event=object())  # type: ignore[arg-type]
    _assert(receipt, (31, 34), "PRELAUNCH_BLOCKED", "INVALID_INPUT", 0)


def test_7_unsafe_tool_relative_path_is_a_path_violation(tmp_path: Path) -> None:
    fixture = _fixture(tmp_path)
    fixture["definition"]["relative_path"] = "../escape"
    receipt = _launch(fixture)
    _assert(receipt, (7,), "PRELAUNCH_BLOCKED", "TOOL_PATH_VIOLATION", 0)
