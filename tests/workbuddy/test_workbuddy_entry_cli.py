from __future__ import annotations

import hashlib
import io
import json
import os
import sys
from pathlib import Path
from types import MappingProxyType
from typing import Any

import pytest

from golden_key_openmontage_workbuddy import workbuddy_entry_cli as cli


class _BinaryStream:
    def __init__(self, payload: bytes = b"") -> None:
        self.buffer = io.BytesIO(payload)


def _definition(*, allowed: list[str] | None = None) -> dict[str, Any]:
    allowed = [] if allowed is None else allowed
    return {
        "schema_version": "golden-key-workbuddy-package-tool-definition-v1",
        "definition_id": "definition-1",
        "definition_sha256": "a" * 64,
        "definition_relative_path": "definitions/tool.json",
        "authority_owner": "golden-key",
        "package_release": "release-1",
        "package_commit": "0" * 40,
        "tool_id": "tool-1",
        "relative_path": "tools/tool.exe",
        "sha256": "b" * 64,
        "size": 1,
        "owner": "golden-key",
        "execution_kind": "DIRECT_EXECUTABLE",
        "interpreter_binding": "SELF",
        "fixed_argv_template": [],
        "fixed_argv_placeholders": [],
        "request_schema_sha256": "c" * 64,
        "result_schema_sha256": "d" * 64,
        "allowed_environment_names": allowed,
        "secret_environment_names": allowed,
        "required_local_capabilities": [],
    }


def _request(
    *,
    message: str = "literal user message",
    provider_names: list[str] | None = None,
    allowed: list[str] | None = None,
    cancel: bool = False,
    continuation: dict[str, Any] | None = None,
    managed_remotion_runtime: dict[str, Any] | None = None,
) -> dict[str, Any]:
    provider_names = [] if provider_names is None else provider_names
    allowed = provider_names if allowed is None else allowed
    return {
        "schema_version": cli._REQUEST_SCHEMA,
        "bridge_contract_id": cli._BRIDGE_CONTRACT_ID,
        "data_root": "D:/fixtures/data",
        "user_message": message,
        "executor_controls": {
            "schema_version": cli._CONTROLS_SCHEMA,
            "session_id": "session-1",
            "request_id": "request-1",
            "timeout_seconds": 30,
            "termination_grace_seconds": 2,
            "result_root": "D:/fixtures/data/results",
            "provider_environment_source": "FIXED_CLI_PROCESS_ENV",
            "provider_environment_names": provider_names,
        },
        "package_tool_definition": _definition(allowed=allowed),
        "local_capability_evidence": [],
        "managed_remotion_runtime": managed_remotion_runtime,
        "cancel_requested": cancel,
        "continuation": continuation or {"mode": "NONE", "prior_request_id": None},
    }


def _receipt(
    *,
    outcome: str = "EXITED_SUCCESS",
    reason: str = "NONE",
    provider_names: tuple[str, ...] = (),
    secret: str | None = None,
    partial_identity: bool = False,
    managed_remotion_runtime: dict[str, Any] | None = None,
) -> MappingProxyType:
    definition = _definition()
    partial_prelaunch = outcome == "PRELAUNCH_BLOCKED" or (
        outcome == "CANCELLED" and reason == "CANCELLED_BEFORE_SPAWN"
    )
    spawn_failed = outcome == "SPAWN_FAILED"
    package = {
        "openmontage_release": definition["package_release"],
        "openmontage_commit": definition["package_commit"],
        "package_root": "D:/fixtures/package",
    }
    tool_definition = {
        "definition_id": definition["definition_id"],
        "definition_sha256": definition["definition_sha256"],
        "authority_owner": definition["authority_owner"],
    }
    if outcome == "CANCELLED" and reason == "CANCELLED_BEFORE_SPAWN":
        package = {"openmontage_release": None, "openmontage_commit": None, "package_root": None}
    if partial_prelaunch:
        tool_definition = {"definition_id": None, "definition_sha256": None, "authority_owner": None}
    if partial_identity:
        package = {"openmontage_release": None, "openmontage_commit": None, "package_root": None}
        tool_definition = {"definition_id": None, "definition_sha256": None, "authority_owner": None}
    error: Any = None
    if outcome != "EXITED_SUCCESS":
        error = {"code": reason, "origin": "CHILD", "sanitized_message": reason}
    if secret is not None:
        error = {"code": reason, "origin": "CHILD", "sanitized_message": secret}
    return MappingProxyType(
        {
            "schema_version": cli._RESULT_SCHEMA,
            "outcome": outcome,
            "reason_code": reason,
            "session": MappingProxyType({"session_id": None if partial_identity else "session-1"}),
            "request": MappingProxyType({"request_id": None if partial_identity else "request-1"}),
            "registration": MappingProxyType({"registration_sha256": None}),
            "package": MappingProxyType(package),
            "manifest": MappingProxyType({"sha256": None, "size": None}),
            "lock": MappingProxyType({"sha256": None, "size": None, "bundle_sha256": None}),
            "tool_definition": MappingProxyType(tool_definition),
            "tool_file": MappingProxyType(
                {"tool_id": None, "relative_path": None, "path": None, "sha256": None, "size": None, "owner": None}
            ),
            "interpreter": MappingProxyType({"binding": None, "path": None, "sha256": None, "size": None}),
            "user_message": MappingProxyType(
                {
                    "sha256": None
                    if partial_identity
                    else hashlib.sha256("literal user message".encode()).hexdigest(),
                    "byte_length": None if partial_identity else len("literal user message".encode()),
                }
            ),
            "provider_environment_names": provider_names,
            "local_capability_evidence_identities": (),
            "managed_remotion_runtime": managed_remotion_runtime,
            "launched": False if partial_prelaunch or spawn_failed else True,
            "spawn_count": 0 if partial_prelaunch or spawn_failed else 1,
            "pid": None if partial_prelaunch or spawn_failed else 1234,
            "started_at_utc": None
            if partial_prelaunch or spawn_failed
            else "2026-08-23T00:00:00.000Z",
            "ended_at_utc": None,
            "duration_ms": 0,
            "exit_code": None,
            "timed_out": False,
            "cancelled": outcome == "CANCELLED",
            "retry_count": 0,
            "stdout": MappingProxyType({"size": 0, "sha256": hashlib.sha256(b"").hexdigest(), "truncated": False}),
            "stderr": MappingProxyType({"size": 0, "sha256": hashlib.sha256(b"").hexdigest(), "truncated": False}),
            "result_pointer": MappingProxyType({"path": None, "sha256": None, "size": None, "valid": False}),
            "error": error,
            "residual_process": MappingProxyType(
                {
                    "detected": False,
                    "termination_attempted": False,
                    "termination_succeeded": None,
                    "observed_pids": (),
                }
            ),
        }
    )


def _environment(provider: Mapping[str, str] | None = None) -> dict[str, str]:
    provider = {} if provider is None else dict(provider)
    interpreter = Path(sys.executable).resolve()
    module_hash = hashlib.sha256(Path(cli.__file__).read_bytes()).hexdigest()
    interpreter_hash = hashlib.sha256(interpreter.read_bytes()).hexdigest()
    environment = {
        cli._ENV_SKILL_IDENTITY: "golden-key-openmontage",
        cli._ENV_RELEASE_IDENTITY: "release-1",
        cli._ENV_AUTHORITY_OWNER: "golden-key",
        cli._ENV_PACKAGE_TOOL_DEFINITION_ID: "definition-1",
        cli._ENV_PACKAGE_TOOL_DEFINITION_SHA256: "a" * 64,
        cli._ENV_PACKAGE_TOOL_DEFINITION_RELATIVE_PATH: "definitions/tool.json",
        cli._ENV_BRIDGE_CONTRACT_ID: cli._BRIDGE_CONTRACT_ID,
        cli._ENV_REQUEST_SCHEMA_ID: cli._REQUEST_SCHEMA,
        cli._ENV_REQUEST_SCHEMA_SHA256: cli._REQUEST_SCHEMA_SHA256,
        cli._ENV_RESULT_SCHEMA_ID: cli._RESULT_SCHEMA,
        cli._ENV_RESULT_SCHEMA_SHA256: cli._RESULT_SCHEMA_SHA256,
        cli._ENV_MODULE_NAME: cli._MODULE_NAME,
        cli._ENV_MODULE_SHA256: module_hash,
        cli._ENV_FIXED_ARGV: cli._FIXED_ARGV_TEXT,
        cli._ENV_FIXED_ARGV_SHA256: hashlib.sha256(cli._FIXED_ARGV_TEXT.encode()).hexdigest(),
        cli._ENV_INTERPRETER_SHA256: interpreter_hash,
    }
    for name in cli._runtime_environment_names():
        environment[name] = os.environ.get(name, "")
    environment.update(provider)
    return environment


def _run(
    monkeypatch: pytest.MonkeyPatch,
    request: dict[str, Any],
    *,
    provider: Mapping[str, str] | None = None,
    environment: Mapping[str, str] | None = None,
    result: Any = None,
    raw: bytes | None = None,
) -> tuple[int, bytes, bytes, list[tuple[Any, ...]]]:
    calls: list[tuple[Any, ...]] = []
    if result is None:
        result = _receipt(
            provider_names=tuple(request["executor_controls"]["provider_environment_names"]),
            managed_remotion_runtime=request["managed_remotion_runtime"],
        )

    def fake_launch(*args: Any, **kwargs: Any) -> Any:
        calls.append((*args, kwargs))
        return result

    monkeypatch.setattr(cli, "_launch_session_tool", fake_launch)
    monkeypatch.setattr(cli.os, "environ", _environment(provider) if environment is None else environment)
    stdin = _BinaryStream(cli._canonical_json(request) if raw is None else raw)
    stdout = _BinaryStream()
    stderr = _BinaryStream()
    monkeypatch.setattr(cli.sys, "stdin", stdin)
    monkeypatch.setattr(cli.sys, "stdout", stdout)
    monkeypatch.setattr(cli.sys, "stderr", stderr)
    code = cli.main()
    return code, stdout.buffer.getvalue(), stderr.buffer.getvalue(), calls


def test_success_receipt_is_canonical_and_calls_stage4_once(monkeypatch: pytest.MonkeyPatch) -> None:
    request = _request()
    code, stdout, stderr, calls = _run(monkeypatch, request)
    assert code == 0
    assert stderr == b""
    assert json.loads(stdout) == cli._wire_value(_receipt())
    assert len(calls) == 1
    assert calls[0][0] == request["data_root"]
    assert calls[0][1] == request["user_message"]
    assert calls[0][2]["provider_environment"] == {}
    assert isinstance(calls[0][5]["cancel_event"], type(__import__("threading").Event()))
    assert not calls[0][5]["cancel_event"].is_set()
    assert calls[0][5]["managed_remotion_runtime"] is None


def test_managed_remotion_runtime_is_transported_as_one_fact(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    runtime = {
        "status": "PRESENT",
        "source": "managed",
        "runtime_root": str(tmp_path),
        "verified_entrypoint": str(tmp_path / "remotion.cmd"),
        "version": "4.0.0",
        "install_scope": "system",
        "definition_sha256": "a" * 64,
        "manifest_sha256": "b" * 64,
        "lockfile_sha256": "c" * 64,
    }
    request = _request(managed_remotion_runtime=runtime)
    code, stdout, stderr, calls = _run(monkeypatch, request)
    assert code == 0
    assert stderr == b""
    assert json.loads(stdout)["managed_remotion_runtime"] == runtime
    assert calls[0][5]["managed_remotion_runtime"] == runtime


def test_invalid_managed_remotion_runtime_is_rejected_at_bridge_boundary(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    request = _request(
        managed_remotion_runtime={
            "status": "PRESENT",
            "source": "managed",
            "runtime_root": "C:/runtime",
            "verified_entrypoint": "C:/runtime/remotion.cmd",
            "version": "4.0.0",
            "install_scope": "system",
            "definition_sha256": "a" * 64,
            "manifest_sha256": "b" * 64,
        }
    )
    code, stdout, stderr, calls = _run(monkeypatch, request)
    assert (code, stdout, stderr, calls) == (
        64,
        b"",
        b"BRIDGE_INPUT_INVALID\n",
        [],
    )


def test_failure_receipt_is_transport_success_without_rewrite(monkeypatch: pytest.MonkeyPatch) -> None:
    request = _request()
    receipt = _receipt(outcome="CHILD_REPORTED_FAILURE", reason="CHILD_REPORTED_FAILURE")
    code, stdout, stderr, calls = _run(monkeypatch, request, result=receipt)
    assert code == 0
    assert stderr == b""
    assert json.loads(stdout)["outcome"] == "CHILD_REPORTED_FAILURE"
    assert len(calls) == 1


def test_spawn_failed_receipt_keeps_full_identity_and_zero_spawn(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    request = _request()
    receipt = _receipt(outcome="SPAWN_FAILED", reason="SPAWN_OS_ERROR")
    code, stdout, stderr, calls = _run(monkeypatch, request, result=receipt)
    wire = json.loads(stdout)
    assert code == 0
    assert stderr == b""
    assert wire["outcome"] == "SPAWN_FAILED"
    assert wire["launched"] is False
    assert wire["spawn_count"] == 0
    assert wire["pid"] is None
    assert wire["started_at_utc"] is None
    assert wire["session"]["session_id"] == "session-1"
    assert wire["request"]["request_id"] == "request-1"
    assert wire["package"]["openmontage_release"] == "release-1"
    assert wire["package"]["openmontage_commit"] == "0" * 40
    assert wire["tool_definition"]["authority_owner"] == "golden-key"
    assert wire["tool_definition"]["definition_id"] == "definition-1"
    assert wire["tool_definition"]["definition_sha256"] == "a" * 64
    assert len(calls) == 1


@pytest.mark.parametrize(("field", "value"), [("launched", True), ("spawn_count", 1)])
def test_spawn_failed_receipt_rejects_inconsistent_spawn_facts(
    monkeypatch: pytest.MonkeyPatch, field: str, value: Any
) -> None:
    request = _request()
    receipt = dict(_receipt(outcome="SPAWN_FAILED", reason="SPAWN_OS_ERROR"))
    receipt[field] = value
    code, stdout, stderr, calls = _run(monkeypatch, request, result=receipt)
    assert (code, stdout, stderr) == (70, b"", b"BRIDGE_OUTPUT_INVALID\n")
    assert len(calls) == 1


@pytest.mark.parametrize(
    "raw",
    [
        b'{"schema_version":"x","schema_version":"y"}\n',
        lambda request: cli._canonical_json(request).rstrip(b"\n") + b" \n",
    ],
)
def test_duplicate_or_trailing_input_is_fail_closed_without_stage4(
    monkeypatch: pytest.MonkeyPatch, raw: Any
) -> None:
    request = _request()
    payload = raw(request) if callable(raw) else raw
    code, stdout, stderr, calls = _run(monkeypatch, request, raw=payload)
    assert code == 64
    assert stdout == b""
    assert stderr == b"BRIDGE_INPUT_INVALID\n"
    assert calls == []


def test_non_nfc_literal_message_is_rejected_without_normalization(monkeypatch: pytest.MonkeyPatch) -> None:
    request = _request(message="e\u0301")
    code, stdout, stderr, calls = _run(monkeypatch, request)
    assert code == 64
    assert stdout == b""
    assert stderr == b"BRIDGE_INPUT_INVALID\n"
    assert calls == []


def test_unknown_root_field_is_input_error(monkeypatch: pytest.MonkeyPatch) -> None:
    request = _request()
    request["unknown"] = True
    code, stdout, stderr, calls = _run(monkeypatch, request)
    assert code == 64
    assert stdout == b""
    assert calls == []


def test_definition_and_evidence_semantics_are_deferred_to_stage4(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    request = _request()
    request["package_tool_definition"]["relative_path"] = 17
    request["local_capability_evidence"] = [{"schema_version": "stage4-owns-this-wire"}]
    receipt = _receipt(outcome="PRELAUNCH_BLOCKED", reason="TOOL_DEFINITION_INVALID")
    code, stdout, stderr, calls = _run(monkeypatch, request, result=receipt)
    assert code == 0
    assert stderr == b""
    assert json.loads(stdout)["reason_code"] == "TOOL_DEFINITION_INVALID"
    assert len(calls) == 1
    assert calls[0][3] == request["package_tool_definition"]
    assert calls[0][4] == request["local_capability_evidence"]


@pytest.mark.parametrize(
    "field,value",
    [
        ("package_release", "other-release"),
        ("authority_owner", "other-owner"),
        ("definition_id", "other-definition"),
        ("definition_sha256", "f" * 64),
        ("definition_relative_path", "definitions/other.json"),
    ],
)
def test_installer_stamped_definition_identity_is_required_before_stage4(
    monkeypatch: pytest.MonkeyPatch, field: str, value: Any
) -> None:
    request = _request()
    request["package_tool_definition"][field] = value
    code, stdout, stderr, calls = _run(monkeypatch, request)
    assert (code, stdout, stderr, calls) == (78, b"", b"BRIDGE_ASSET_INVALID\n", [])


def test_missing_and_disallowed_environment_names_are_78(monkeypatch: pytest.MonkeyPatch) -> None:
    request = _request(provider_names=["PROVIDER_SECRET"], allowed=["PROVIDER_SECRET"])
    code, stdout, stderr, calls = _run(monkeypatch, request, provider={})
    assert (code, stdout, stderr, calls) == (78, b"", b"BRIDGE_ENVIRONMENT_INVALID\n", [])

    disallowed = _request(provider_names=["NOT_ALLOWED"], allowed=[])
    code, stdout, stderr, calls = _run(monkeypatch, disallowed, provider={"NOT_ALLOWED": "x"})
    assert (code, stdout, stderr, calls) == (78, b"", b"BRIDGE_ENVIRONMENT_INVALID\n", [])


def test_unrelated_environment_values_are_not_read_or_forwarded(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    request = _request()
    receipt = _receipt(provider_names=())

    class _NoExtraRead(dict[str, str]):
        def __getitem__(self, key: str) -> str:
            if key.casefold() == "workbuddy_sandbox":
                raise AssertionError("sandbox value was read")
            return super().__getitem__(key)

    environment = _NoExtraRead(_environment())
    environment["WORKBUDDY_SANDBOX"] = "opaque"
    code, stdout, stderr, calls = _run(
        monkeypatch, request, environment=environment, result=receipt
    )
    assert code == 0
    assert stderr == b""
    assert json.loads(stdout)["provider_environment_names"] == []
    assert len(calls) == 1
    assert calls[0][2]["provider_environment"] == {}


def test_secret_never_reaches_stdout_or_stderr(monkeypatch: pytest.MonkeyPatch) -> None:
    secret = "provider-secret-canary"
    request = _request(provider_names=["PROVIDER_SECRET"], allowed=["PROVIDER_SECRET"])
    receipt = _receipt(provider_names=("PROVIDER_SECRET",), secret=secret)
    code, stdout, stderr, calls = _run(
        monkeypatch, request, provider={"PROVIDER_SECRET": secret}, result=receipt
    )
    assert code == 70
    assert stdout == b""
    assert secret.encode() not in stderr
    assert stderr == b"BRIDGE_OUTPUT_INVALID\n"
    assert len(calls) == 1


def test_cancel_entry_fact_sets_local_event_and_does_not_replay(monkeypatch: pytest.MonkeyPatch) -> None:
    request = _request(cancel=True)
    receipt = _receipt(outcome="CANCELLED", reason="CANCELLED_BEFORE_SPAWN")
    code, stdout, stderr, calls = _run(monkeypatch, request, result=receipt)
    assert code == 0
    assert stderr == b""
    assert len(calls) == 1
    assert calls[0][5]["cancel_event"].is_set()


def test_confirmed_continuation_is_a_new_single_call(monkeypatch: pytest.MonkeyPatch) -> None:
    request = _request(
        continuation={"mode": "USER_CONFIRMED_NEW_REQUEST", "prior_request_id": "request-old"}
    )
    code, stdout, stderr, calls = _run(monkeypatch, request)
    assert code == 0
    assert stdout
    assert stderr == b""
    assert len(calls) == 1
    assert calls[0][3] == request["package_tool_definition"]


def test_invalid_receipt_is_70_with_no_partial_stdout(monkeypatch: pytest.MonkeyPatch) -> None:
    request = _request()
    invalid = dict(_receipt())
    invalid.pop("error")
    code, stdout, stderr, calls = _run(monkeypatch, request, result=invalid)
    assert code == 70
    assert stdout == b""
    assert stderr == b"BRIDGE_OUTPUT_INVALID\n"
    assert len(calls) == 1


@pytest.mark.parametrize(
    "path,value",
    [
        (("session", "session_id"), "other-session"),
        (("request", "request_id"), "other-request"),
        (("user_message", "sha256"), "f" * 64),
        (("user_message", "byte_length"), 999),
        (("package", "openmontage_release"), "other-release"),
        (("package", "openmontage_commit"), "f" * 40),
        (("tool_definition", "authority_owner"), "other-owner"),
        (("tool_definition", "definition_id"), "other-definition"),
        (("tool_definition", "definition_sha256"), "f" * 64),
    ],
)
def test_receipt_identity_mismatch_is_output_error(
    monkeypatch: pytest.MonkeyPatch, path: tuple[str, str], value: Any
) -> None:
    request = _request()
    receipt = dict(_receipt())
    nested = dict(receipt[path[0]])
    nested[path[1]] = value
    receipt[path[0]] = MappingProxyType(nested)
    code, stdout, stderr, calls = _run(monkeypatch, request, result=receipt)
    assert (code, stdout, stderr) == (70, b"", b"BRIDGE_OUTPUT_INVALID\n")
    assert len(calls) == 1


def test_partial_prelaunch_receipt_is_forwarded_without_fabricating_identity(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    request = _request()
    receipt = _receipt(
        outcome="PRELAUNCH_BLOCKED",
        reason="LOCATOR_FAILED",
        partial_identity=True,
    )
    code, stdout, stderr, calls = _run(monkeypatch, request, result=receipt)
    assert code == 0
    assert stderr == b""
    assert json.loads(stdout)["outcome"] == "PRELAUNCH_BLOCKED"
    assert json.loads(stdout)["package"]["openmontage_release"] is None
    assert len(calls) == 1


def test_non_prelaunch_receipt_must_be_fully_correlated(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    request = _request()
    receipt = _receipt(partial_identity=True)
    code, stdout, stderr, calls = _run(monkeypatch, request, result=receipt)
    assert (code, stdout, stderr) == (70, b"", b"BRIDGE_OUTPUT_INVALID\n")
    assert len(calls) == 1


def test_provider_values_are_reconstructed_only_for_stage4(monkeypatch: pytest.MonkeyPatch) -> None:
    secret = "secret-value"
    request = _request(provider_names=["PROVIDER_SECRET"], allowed=["PROVIDER_SECRET"])
    receipt = _receipt(provider_names=("PROVIDER_SECRET",))
    code, stdout, stderr, calls = _run(
        monkeypatch, request, provider={"PROVIDER_SECRET": secret}, result=receipt
    )
    assert code == 0
    assert stdout
    assert stderr == b""
    assert len(calls) == 1
    assert calls[0][2]["provider_environment"] == {"PROVIDER_SECRET": secret}
    assert secret.encode() not in stdout
    assert secret.encode() not in stderr


def test_provider_names_casefold_to_definition_spelling(monkeypatch: pytest.MonkeyPatch) -> None:
    secret = "casefold-secret"
    request = _request(provider_names=["API_KEY"], allowed=["Api_Key"])
    receipt = _receipt(provider_names=("Api_Key",))
    code, stdout, stderr, calls = _run(
        monkeypatch, request, provider={"api_key": secret}, result=receipt
    )
    assert code == 0
    assert stderr == b""
    assert json.loads(stdout)["provider_environment_names"] == ["Api_Key"]
    assert len(calls) == 1
    assert calls[0][2]["provider_environment"] == {"Api_Key": secret}
    assert secret.encode() not in stdout
    assert secret.encode() not in stderr


def test_opaque_allowlist_does_not_read_provider_value(monkeypatch: pytest.MonkeyPatch) -> None:
    secret = "opaque-allowlist-secret"
    request = _request(provider_names=["PROVIDER_SECRET"], allowed=["PROVIDER_SECRET", 7])
    receipt = _receipt(provider_names=())

    class _NoProviderRead(dict[str, str]):
        def __getitem__(self, key: str) -> str:
            if key.casefold() == "provider_secret":
                raise AssertionError("opaque provider value was read")
            return super().__getitem__(key)

    environment = _NoProviderRead(_environment({"PROVIDER_SECRET": secret}))
    code, stdout, stderr, calls = _run(
        monkeypatch, request, environment=environment, result=receipt
    )
    assert code == 0
    assert stderr == b""
    assert json.loads(stdout)["provider_environment_names"] == []
    assert len(calls) == 1
    assert calls[0][2]["provider_environment"] == {}
    assert secret.encode() not in stdout
    assert secret.encode() not in stderr


def test_opaque_allowlist_requires_all_runtime_names(monkeypatch: pytest.MonkeyPatch) -> None:
    runtime_names = ("RUNTIME_A", "RUNTIME_B")
    monkeypatch.setattr(cli, "_runtime_environment_names", lambda: runtime_names)
    request = _request(provider_names=["PROVIDER_SECRET"], allowed=["PROVIDER_SECRET", 7])
    receipt = _receipt(provider_names=())
    environment = _environment({"PROVIDER_SECRET": "opaque-runtime-secret"})
    environment.pop("RUNTIME_B")
    code, stdout, stderr, calls = _run(
        monkeypatch, request, environment=environment, result=receipt
    )
    assert code == 78
    assert stdout == b""
    assert stderr == b"BRIDGE_ENVIRONMENT_INVALID\n"
    assert calls == []


def test_stdin_read_is_bounded_before_parsing() -> None:
    class _BoundedReader:
        def __init__(self) -> None:
            self.requested: int | None = None

        def read(self, size: int = -1) -> bytes:
            self.requested = size
            return b"{}"

    reader = _BoundedReader()
    original = cli.sys.stdin
    cli.sys.stdin = reader  # type: ignore[assignment]
    try:
        assert cli._read_stdin() == b"{}"
    finally:
        cli.sys.stdin = original
    assert reader.requested == cli._MAX_INPUT_BYTES + 1


def test_skill_keeps_optional_setup_guidance_only() -> None:
    skill = Path(__file__).resolve().parents[2] / "workbuddy-skill/golden-key-openmontage/SKILL.md"
    source = skill.read_text(encoding="utf-8")
    normalized = " ".join(source.split())
    assert "WorkBuddy remains the sole Agent and the sole user conversation entry" in normalized
    assert "Keep the complete original message and business goal" in normalized
    assert "the Package Guide is the production-semantic authority" in normalized
    assert "Present the actual business result naturally" in normalized
    assert "do not claim that an Artifact, video, file" in normalized
    assert "Do not delay delivery to create workspace memory, another Skill" in normalized
    assert "registry.npmmirror.com" in normalized
    assert "Never assume a drive letter" in normalized
    assert "Remotion invocation" in normalized
    assert "version print alone is not final proof" in normalized.casefold()
    assert "locate and verify the current OpenMontage Package root and Package Guide" in normalized
    assert "On the first relevant use after Package verification" in normalized
    assert "external AI image/video generation" in normalized
    assert "ask for more detail" in normalized
    assert "two or three image/video choices or one or two TTS choices" in normalized
    assert "verify that the current OpenMontage Package recognizes it" in normalized
    for technical in (
        "<installer:",
        "LauncherReceipt",
        "golden-key-workbuddy-configuration-action-v1",
        "scripts/run.ps1",
        "latest-launcher-receipt.json",
    ):
        assert technical.casefold() not in source.casefold()


def test_schema_hashes_bind_canonical_closed_descriptors_not_schema_ids() -> None:
    assert cli._REQUEST_SCHEMA_SHA256 == cli._schema_digest(cli._REQUEST_SCHEMA_DESCRIPTOR)
    assert cli._RESULT_SCHEMA_SHA256 == cli._schema_digest(cli._RESULT_SCHEMA_DESCRIPTOR)
    assert cli._REQUEST_SCHEMA_SHA256 != hashlib.sha256(cli._REQUEST_SCHEMA.encode()).hexdigest()
    assert cli._RESULT_SCHEMA_SHA256 != hashlib.sha256(cli._RESULT_SCHEMA.encode()).hexdigest()
    package_constraints = cli._REQUEST_SCHEMA_DESCRIPTOR["constraints"]["package_tool_definition"]
    assert package_constraints["semantic_owner"] == "Stage4"
    assert package_constraints["bridge_validation"] == (
        "Installer-stamped exact release/authority/definition-id/hash/relative-path identity binding"
    )

    assert cli._REQUEST_SCHEMA_DESCRIPTOR["root_fields"] == [
        "bridge_contract_id",
        "cancel_requested",
        "continuation",
        "data_root",
        "executor_controls",
        "local_capability_evidence",
        "managed_remotion_runtime",
        "package_tool_definition",
        "schema_version",
        "user_message",
    ]
    assert cli._REQUEST_SCHEMA_DESCRIPTOR["control_fields"] == [
        "provider_environment_names",
        "provider_environment_source",
        "request_id",
        "result_root",
        "schema_version",
        "session_id",
        "termination_grace_seconds",
        "timeout_seconds",
    ]
    assert cli._REQUEST_SCHEMA_DESCRIPTOR["continuation_fields"] == ["mode", "prior_request_id"]
    assert set(cli._REQUEST_SCHEMA_DESCRIPTOR["package_tool_definition_fields"]) == {
        "allowed_environment_names",
        "authority_owner",
        "definition_id",
        "definition_relative_path",
        "definition_sha256",
        "execution_kind",
        "fixed_argv_placeholders",
        "fixed_argv_template",
        "interpreter_binding",
        "owner",
        "package_commit",
        "package_release",
        "relative_path",
        "required_local_capabilities",
        "request_schema_sha256",
        "result_schema_sha256",
        "schema_version",
        "secret_environment_names",
        "sha256",
        "size",
        "tool_id",
    }
    assert cli._REQUEST_SCHEMA_DESCRIPTOR["local_capability_evidence_fields"] == [
        "approved_capability_definition",
        "approved_capability_definition_sha256",
        "original_stage3_fact",
        "original_stage3_fact_sha256",
        "schema_version",
    ]
    nested = cli._RESULT_SCHEMA_DESCRIPTOR["nested_fields"]
    assert set(nested) == {
        "error",
        "interpreter",
        "local_capability_evidence_identity",
        "managed_remotion_runtime",
        "lock",
        "manifest",
        "package",
        "registration",
        "request",
        "residual_process",
        "result_pointer",
        "session",
        "stream",
        "tool_definition",
        "tool_file",
        "user_message",
    }
    assert nested["session"] == ["session_id"]
    assert nested["request"] == ["request_id"]
    assert nested["registration"] == ["registration_sha256"]
    assert nested["package"] == ["openmontage_commit", "openmontage_release", "package_root"]
    assert nested["manifest"] == ["sha256", "size"]
    assert nested["lock"] == ["bundle_sha256", "sha256", "size"]
    assert nested["tool_definition"] == ["authority_owner", "definition_id", "definition_sha256"]
    assert nested["tool_file"] == ["owner", "path", "relative_path", "sha256", "size", "tool_id"]
    assert nested["interpreter"] == ["binding", "path", "sha256", "size"]
    assert nested["user_message"] == ["byte_length", "sha256"]
    assert nested["managed_remotion_runtime"] == [
        "definition_sha256",
        "install_scope",
        "lockfile_sha256",
        "manifest_sha256",
        "runtime_root",
        "source",
        "status",
        "verified_entrypoint",
        "version",
    ]
    assert nested["stream"] == ["sha256", "size", "truncated"]
    assert nested["result_pointer"] == ["path", "sha256", "size", "valid"]
    assert nested["error"] == ["code", "origin", "sanitized_message"]
    assert nested["residual_process"] == [
        "detected",
        "observed_pids",
        "termination_attempted",
        "termination_succeeded",
    ]
