"""Private fixed transport adapter for the single WorkBuddy Skill entry.

This module deliberately has no console-script contract, subcommands, router,
retry policy, or second control plane.  WorkBuddy supplies one canonical JSON
request; the adapter validates the release-bound bridge and calls the accepted
Stage 4 launcher exactly once.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import sys
import threading
import unicodedata
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from .session_launcher import launch_session_tool as _launch_session_tool


_BRIDGE_CONTRACT_ID = "golden-key-workbuddy-skill-cli-bridge-v1"
_REQUEST_SCHEMA = "golden-key-workbuddy-skill-cli-request-v1"
_RESULT_SCHEMA = "golden-key-workbuddy-launcher-receipt-v1"
_CONTROLS_SCHEMA = "golden-key-workbuddy-launcher-executor-controls-v1"
_MODULE_NAME = "golden_key_openmontage_workbuddy.workbuddy_entry_cli"
_FIXED_ARGV = ("-I", "-m", _MODULE_NAME)
_FIXED_ARGV_TEXT = json.dumps(list(_FIXED_ARGV), ensure_ascii=False, separators=(",", ":"))

# Release-bound wire descriptors identify the bridge envelope.  They are not
# copies of Stage 4 semantic validators: Stage 4 remains authoritative for
# definition, capability, binding, path, and hash semantics.
_REQUEST_ROOT_FIELDS = [
    "bridge_contract_id",
    "cancel_requested",
    "continuation",
    "data_root",
    "executor_controls",
    "local_capability_evidence",
    "package_tool_definition",
    "schema_version",
    "user_message",
]
_REQUEST_CONTROL_FIELDS = [
    "provider_environment_names",
    "provider_environment_source",
    "request_id",
    "result_root",
    "schema_version",
    "session_id",
    "termination_grace_seconds",
    "timeout_seconds",
]
_REQUEST_CONTINUATION_FIELDS = ["mode", "prior_request_id"]
_REQUEST_PACKAGE_DEFINITION_FIELDS = [
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
]
_REQUEST_LOCAL_EVIDENCE_FIELDS = [
    "approved_capability_definition",
    "approved_capability_definition_sha256",
    "original_stage3_fact",
    "original_stage3_fact_sha256",
    "schema_version",
]
_RESULT_ROOT_FIELDS = [
    "cancelled",
    "duration_ms",
    "ended_at_utc",
    "error",
    "exit_code",
    "interpreter",
    "launched",
    "local_capability_evidence_identities",
    "lock",
    "manifest",
    "outcome",
    "package",
    "pid",
    "provider_environment_names",
    "reason_code",
    "registration",
    "request",
    "residual_process",
    "result_pointer",
    "retry_count",
    "schema_version",
    "session",
    "spawn_count",
    "started_at_utc",
    "stderr",
    "stdout",
    "timed_out",
    "tool_definition",
    "tool_file",
    "user_message",
]
_RESULT_NESTED_FIELDS = {
    "session": ["session_id"],
    "request": ["request_id"],
    "registration": ["registration_sha256"],
    "package": ["openmontage_commit", "openmontage_release", "package_root"],
    "manifest": ["sha256", "size"],
    "lock": ["bundle_sha256", "sha256", "size"],
    "tool_definition": ["authority_owner", "definition_id", "definition_sha256"],
    "tool_file": ["owner", "path", "relative_path", "sha256", "size", "tool_id"],
    "interpreter": ["binding", "path", "sha256", "size"],
    "user_message": ["byte_length", "sha256"],
    "stream": ["sha256", "size", "truncated"],
    "result_pointer": ["path", "sha256", "size", "valid"],
    "error": ["code", "origin", "sanitized_message"],
    "residual_process": [
        "detected",
        "observed_pids",
        "termination_attempted",
        "termination_succeeded",
    ],
    "local_capability_evidence_identity": [
        "approved_capability_definition_sha256",
        "capability_id",
        "definition_sha256",
        "entrypoint_sha256",
        "entrypoint_size",
        "original_stage3_fact_sha256",
        "plan_sha256",
        "source",
        "status",
    ],
}


def _schema_digest(descriptor: Mapping[str, Any]) -> str:
    encoded = json.dumps(
        descriptor, allow_nan=False, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


_REQUEST_SCHEMA_DESCRIPTOR = {
    "schema_version": _REQUEST_SCHEMA,
    "root_fields": _REQUEST_ROOT_FIELDS,
    "control_fields": _REQUEST_CONTROL_FIELDS,
    "continuation_fields": _REQUEST_CONTINUATION_FIELDS,
    "package_tool_definition_fields": _REQUEST_PACKAGE_DEFINITION_FIELDS,
    "local_capability_evidence_fields": _REQUEST_LOCAL_EVIDENCE_FIELDS,
    "constraints": {
        "root": {
            "closed": True,
            "encoding": "UTF-8",
            "canonical": "sort_keys=true;ensure_ascii=false;allow_nan=false;one-trailing-LF",
            "duplicate_keys": "reject",
            "unknown_fields": "reject",
        },
        "executor_controls": {
            "closed": True,
            "provider_environment_names": "ASCII;casefold-unique;request-order-lexically-sorted",
            "timeout_seconds": "integer:1..3600",
            "termination_grace_seconds": "integer:1..30",
        },
        "continuation": {"closed": True, "mode": "NONE|USER_CONFIRMED_NEW_REQUEST"},
        "package_tool_definition": {
            "wire_type": "JSON mapping",
            "semantic_owner": "Stage4",
            "bridge_validation": "mapping-only;no-definition-hash-binding-path-validation",
        },
        "local_capability_evidence": {
            "wire_type": "JSON list of mapping wires",
            "semantic_owner": "Stage4",
            "bridge_validation": "list-and-mapping-item-shape-only",
        },
        "user_message": "literal;NFC-required;no-normalization",
    },
}
_RESULT_SCHEMA_DESCRIPTOR = {
    "schema_version": _RESULT_SCHEMA,
    "root_fields": _RESULT_ROOT_FIELDS,
    "nested_fields": _RESULT_NESTED_FIELDS,
    "constraints": {
        "encoding": "UTF-8",
        "canonical": "sort_keys=true;ensure_ascii=false;allow_nan=false;one-trailing-LF",
        "outcome": "Stage4-nine-value-closed-set",
        "root": "exact-fields;immutable-wire-mapping",
        "nested": "exact-field-sets;stdout-and-stderr-use-stream-fields;error-nullable",
        "provider_environment_names": "canonical-definition-spelling;casefold-request-match;sorted",
        "retry_count": "exactly-zero",
    },
}
_REQUEST_SCHEMA_SHA256 = _schema_digest(_REQUEST_SCHEMA_DESCRIPTOR)
_RESULT_SCHEMA_SHA256 = _schema_digest(_RESULT_SCHEMA_DESCRIPTOR)
_IDENTIFIER_RE = re.compile(r"^[A-Za-z0-9._-]{1,128}$")
_ENV_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_PLACEHOLDER_MARKERS = ("${", "<installer", "placeholder", "unresolved", "todo")
_MAX_INPUT_BYTES = 8 * 1024 * 1024
_MAX_OUTPUT_BYTES = 4 * 1024 * 1024

_ENV_SKILL_IDENTITY = "GOLDEN_KEY_WORKBUDDY_SKILL_IDENTITY"
_ENV_RELEASE_IDENTITY = "GOLDEN_KEY_WORKBUDDY_RELEASE_IDENTITY"
_ENV_AUTHORITY_OWNER = "GOLDEN_KEY_WORKBUDDY_AUTHORITY_OWNER"
_ENV_PACKAGE_TOOL_DEFINITION_ID = "GOLDEN_KEY_WORKBUDDY_PACKAGE_TOOL_DEFINITION_ID"
_ENV_PACKAGE_TOOL_DEFINITION_SHA256 = "GOLDEN_KEY_WORKBUDDY_PACKAGE_TOOL_DEFINITION_SHA256"
_ENV_PACKAGE_TOOL_DEFINITION_RELATIVE_PATH = "GOLDEN_KEY_WORKBUDDY_PACKAGE_TOOL_DEFINITION_RELATIVE_PATH"
_ENV_BRIDGE_CONTRACT_ID = "GOLDEN_KEY_WORKBUDDY_BRIDGE_CONTRACT_ID"
_ENV_REQUEST_SCHEMA_ID = "GOLDEN_KEY_WORKBUDDY_REQUEST_SCHEMA_ID"
_ENV_REQUEST_SCHEMA_SHA256 = "GOLDEN_KEY_WORKBUDDY_REQUEST_SCHEMA_SHA256"
_ENV_RESULT_SCHEMA_ID = "GOLDEN_KEY_WORKBUDDY_RESULT_SCHEMA_ID"
_ENV_RESULT_SCHEMA_SHA256 = "GOLDEN_KEY_WORKBUDDY_RESULT_SCHEMA_SHA256"
_ENV_MODULE_NAME = "GOLDEN_KEY_WORKBUDDY_MODULE_NAME"
_ENV_MODULE_SHA256 = "GOLDEN_KEY_WORKBUDDY_MODULE_SHA256"
_ENV_FIXED_ARGV = "GOLDEN_KEY_WORKBUDDY_FIXED_ARGV"
_ENV_FIXED_ARGV_SHA256 = "GOLDEN_KEY_WORKBUDDY_FIXED_ARGV_SHA256"
_ENV_INTERPRETER_PATH = "GOLDEN_KEY_WORKBUDDY_INTERPRETER_PATH"
_ENV_INTERPRETER_SHA256 = "GOLDEN_KEY_WORKBUDDY_INTERPRETER_SHA256"
_WINDOWS_RUNTIME_ENV_NAMES = ("COMSPEC", "PATHEXT", "SystemRoot", "TEMP", "TMP", "WINDIR")
_FIXED_ENVIRONMENT_NAMES = (
    _ENV_AUTHORITY_OWNER,
    _ENV_BRIDGE_CONTRACT_ID,
    _ENV_FIXED_ARGV,
    _ENV_FIXED_ARGV_SHA256,
    _ENV_INTERPRETER_PATH,
    _ENV_INTERPRETER_SHA256,
    _ENV_MODULE_NAME,
    _ENV_MODULE_SHA256,
    _ENV_PACKAGE_TOOL_DEFINITION_ID,
    _ENV_PACKAGE_TOOL_DEFINITION_RELATIVE_PATH,
    _ENV_PACKAGE_TOOL_DEFINITION_SHA256,
    _ENV_RELEASE_IDENTITY,
    _ENV_REQUEST_SCHEMA_ID,
    _ENV_REQUEST_SCHEMA_SHA256,
    _ENV_RESULT_SCHEMA_ID,
    _ENV_RESULT_SCHEMA_SHA256,
    _ENV_SKILL_IDENTITY,
)


def _runtime_environment_names() -> tuple[str, ...]:
    return _WINDOWS_RUNTIME_ENV_NAMES if os.name == "nt" else ()

_REQUEST_FIELDS = frozenset(
    {
        "schema_version",
        "bridge_contract_id",
        "data_root",
        "user_message",
        "executor_controls",
        "package_tool_definition",
        "local_capability_evidence",
        "cancel_requested",
        "continuation",
    }
)
_CONTROL_FIELDS = frozenset(
    {
        "schema_version",
        "session_id",
        "request_id",
        "timeout_seconds",
        "termination_grace_seconds",
        "result_root",
        "provider_environment_source",
        "provider_environment_names",
    }
)
_CONTINUATION_FIELDS = frozenset({"mode", "prior_request_id"})
_RECEIPT_FIELDS = frozenset(
    {
        "schema_version",
        "outcome",
        "reason_code",
        "session",
        "request",
        "registration",
        "package",
        "manifest",
        "lock",
        "tool_definition",
        "tool_file",
        "interpreter",
        "user_message",
        "provider_environment_names",
        "local_capability_evidence_identities",
        "launched",
        "spawn_count",
        "pid",
        "started_at_utc",
        "ended_at_utc",
        "duration_ms",
        "exit_code",
        "timed_out",
        "cancelled",
        "retry_count",
        "stdout",
        "stderr",
        "result_pointer",
        "error",
        "residual_process",
    }
)
_OUTCOMES = frozenset(
    {
        "PRELAUNCH_BLOCKED",
        "SPAWN_FAILED",
        "EXITED_SUCCESS",
        "EXITED_NONZERO",
        "CHILD_REPORTED_FAILURE",
        "TIMED_OUT",
        "CANCELLED",
        "INCOMPLETE",
        "RESIDUAL_PROCESS",
    }
)
_REASONS = frozenset(
    {
        "NONE",
        "INVALID_INPUT",
        "CANCELLED_BEFORE_SPAWN",
        "LOCATOR_FAILED",
        "REGISTRATION_DRIFT",
        "TOOL_DEFINITION_INVALID",
        "TOOL_DEFINITION_UNBOUND",
        "TOOL_PATH_VIOLATION",
        "TOOL_IDENTITY_MISMATCH",
        "INTERPRETER_IDENTITY_MISMATCH",
        "LOCAL_CAPABILITY_EVIDENCE_REQUIRED",
        "LOCAL_CAPABILITY_EVIDENCE_MISMATCH",
        "ENVIRONMENT_NOT_ALLOWED",
        "SPAWN_OS_ERROR",
        "EXITED_NONZERO",
        "TIMEOUT",
        "CANCELLED",
        "CHILD_REPORTED_FAILURE",
        "OUTPUT_INVALID",
        "RESULT_POINTER_INVALID",
        "SECRET_DISCLOSURE_DETECTED",
        "EVIDENCE_INCOMPLETE",
        "RESIDUAL_PROCESS_DETECTED",
    }
)


class _BridgeError(Exception):
    def __init__(self, exit_code: int, token: str) -> None:
        self.exit_code = exit_code
        self.token = token
        super().__init__(token)


def _input_error() -> None:
    raise _BridgeError(64, "BRIDGE_INPUT_INVALID")


def _environment_error() -> None:
    raise _BridgeError(78, "BRIDGE_ENVIRONMENT_INVALID")


def _asset_error() -> None:
    raise _BridgeError(78, "BRIDGE_ASSET_INVALID")


def _output_error() -> None:
    raise _BridgeError(70, "BRIDGE_OUTPUT_INVALID")


def _internal_error() -> None:
    raise _BridgeError(70, "BRIDGE_INTERNAL_ERROR")


def _text(value: Any, *, allow_empty: bool = False) -> str:
    if not isinstance(value, str) or (not allow_empty and not value):
        _input_error()
    if any(0xD800 <= ord(char) <= 0xDFFF for char in value):
        _input_error()
    if unicodedata.normalize("NFC", value) != value:
        _input_error()
    try:
        value.encode("utf-8")
    except UnicodeEncodeError:
        _input_error()
    return value


def _validate_json_tree(value: Any) -> None:
    if isinstance(value, str):
        _text(value, allow_empty=True)
        return
    if value is None or isinstance(value, bool) or type(value) is int:
        return
    if type(value) is float:
        if not math.isfinite(value):
            _input_error()
        return
    if isinstance(value, Mapping):
        for key, item in value.items():
            _text(key, allow_empty=True)
            _validate_json_tree(item)
        return
    if isinstance(value, list):
        for item in value:
            _validate_json_tree(item)
        return
    _input_error()


def _canonical_json(value: Any) -> bytes:
    try:
        return (
            json.dumps(
                value,
                allow_nan=False,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
            + b"\n"
        )
    except (TypeError, ValueError, UnicodeEncodeError, RecursionError, MemoryError):
        _input_error()


def _parse_request(raw: bytes) -> dict[str, Any]:
    if len(raw) > _MAX_INPUT_BYTES:
        _input_error()
    try:
        text = raw.decode("utf-8")
        duplicate = False

        def object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
            nonlocal duplicate
            result: dict[str, Any] = {}
            for key, item in pairs:
                if key in result:
                    duplicate = True
                result[key] = item
            return result

        def reject_constant(_value: str) -> None:
            raise ValueError("constant")

        decoder = json.JSONDecoder(object_pairs_hook=object_pairs, parse_constant=reject_constant)
        value, end = decoder.raw_decode(text)
    except (UnicodeError, ValueError, TypeError, json.JSONDecodeError, RecursionError, MemoryError):
        _input_error()
    if duplicate or end != len(text) - 1 or text[-1:] != "\n":
        _input_error()
    if not isinstance(value, dict):
        _input_error()
    _validate_json_tree(value)
    if raw != _canonical_json(value):
        _input_error()
    return value


def _mapping(value: Any, fields: frozenset[str]) -> dict[str, Any]:
    if not isinstance(value, Mapping) or set(value) != fields:
        _input_error()
    return dict(value)


def _env_names(value: Any) -> tuple[str, ...]:
    if not isinstance(value, list):
        _input_error()
    names: list[str] = []
    folded: set[str] = set()
    for item in value:
        name = _text(item)
        if _ENV_NAME_RE.fullmatch(name) is None or not name.isascii():
            _input_error()
        if name.casefold() in folded:
            _input_error()
        folded.add(name.casefold())
        names.append(name)
    if names != sorted(names):
        _input_error()
    return tuple(names)


def _validate_request(value: dict[str, Any]) -> dict[str, Any]:
    request = _mapping(value, _REQUEST_FIELDS)
    if request["schema_version"] != _REQUEST_SCHEMA or request["bridge_contract_id"] != _BRIDGE_CONTRACT_ID:
        _input_error()
    request["data_root"] = _text(request["data_root"])
    request["user_message"] = _text(request["user_message"], allow_empty=True)
    controls = _mapping(request["executor_controls"], _CONTROL_FIELDS)
    if controls["schema_version"] != _CONTROLS_SCHEMA:
        _input_error()
    for field in ("session_id", "request_id"):
        identifier = _text(controls[field])
        if _IDENTIFIER_RE.fullmatch(identifier) is None:
            _input_error()
    if type(controls["timeout_seconds"]) is not int or not 1 <= controls["timeout_seconds"] <= 3600:
        _input_error()
    if type(controls["termination_grace_seconds"]) is not int or not 1 <= controls["termination_grace_seconds"] <= 30:
        _input_error()
    controls["result_root"] = _text(controls["result_root"])
    if controls["provider_environment_source"] != "FIXED_CLI_PROCESS_ENV":
        _input_error()
    provider_names = _env_names(controls["provider_environment_names"])
    controls["provider_environment_names"] = list(provider_names)
    # These two values are opaque Stage 4 wires.  The bridge checks only the
    # envelope shape needed to transport them; Stage 4 owns every semantic,
    # definition-binding, path, hash, and capability decision.
    if not isinstance(request["package_tool_definition"], Mapping):
        _input_error()
    if not isinstance(request["local_capability_evidence"], list):
        _input_error()
    if not all(isinstance(item, Mapping) for item in request["local_capability_evidence"]):
        _input_error()
    if type(request["cancel_requested"]) is not bool:
        _input_error()
    continuation = _mapping(request["continuation"], _CONTINUATION_FIELDS)
    mode = _text(continuation["mode"])
    prior = continuation["prior_request_id"]
    if mode == "NONE":
        if prior is not None:
            _input_error()
    elif mode == "USER_CONFIRMED_NEW_REQUEST":
        prior = _text(prior)
        if _IDENTIFIER_RE.fullmatch(prior) is None or prior == controls["request_id"]:
            _input_error()
    else:
        _input_error()
    return request


def _file_sha256(path: Path) -> str:
    try:
        digest = hashlib.sha256()
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()
    except (OSError, ValueError):
        _asset_error()


def _asset_text(value: str) -> str:
    if not value or any(marker in value.casefold() for marker in _PLACEHOLDER_MARKERS):
        _asset_error()
    if any(ord(char) < 32 or 0xD800 <= ord(char) <= 0xDFFF for char in value):
        _asset_error()
    return value


def _safe_allowed_environment_map(value: Any) -> dict[str, str] | None:
    """Return canonical provider names only when the allowlist is safely closed.

    This deliberately does not validate the PackageToolDefinition.  It is the
    narrow security exception needed to decide whether a provider value may be
    read at all; every other definition decision belongs to Stage 4.
    """

    if not isinstance(value, list):
        return None
    canonical: dict[str, str] = {}
    for item in value:
        if not isinstance(item, str) or _ENV_NAME_RE.fullmatch(item) is None or not item.isascii():
            return None
        folded = item.casefold()
        if folded in canonical:
            return None
        canonical[folded] = item
    return canonical


def _load_environment(
    request: Mapping[str, Any], raw: bytes
) -> tuple[dict[str, str], tuple[str, ...], tuple[str, ...], dict[str, str]]:
    controls = request["executor_controls"]
    definition = request["package_tool_definition"]
    provider_names = tuple(controls["provider_environment_names"])
    allowed_by_fold = _safe_allowed_environment_map(definition.get("allowed_environment_names"))
    fixed_runtime_folds = {
        name.casefold() for name in (*_FIXED_ENVIRONMENT_NAMES, *_runtime_environment_names())
    }
    provider_folds = {name.casefold() for name in provider_names}
    if provider_folds & fixed_runtime_folds:
        _environment_error()
    try:
        # Enumerate names first.  No unallowlisted provider value is fetched.
        environment = os.environ
        environment_names = list(environment.keys())
    except Exception:
        _environment_error()
    by_fold: dict[str, str] = {}
    for name in environment_names:
        if not isinstance(name, str) or name.casefold() in by_fold:
            _environment_error()
        by_fold[name.casefold()] = name

    if allowed_by_fold is None:
        # A malformed/opaque allowlist is Stage 4's definition concern.  Do
        # not read provider values; require the scrubbed process environment to
        # contain exactly the fixed/runtime names plus the requested provider
        # names, including required runtime names.
        if set(by_fold) != fixed_runtime_folds | provider_folds:
            _environment_error()
        canonical_names: tuple[str, ...] = ()
        provider_names_to_read: tuple[tuple[str, str], ...] = ()
    else:
        if not provider_folds.issubset(allowed_by_fold):
            _environment_error()
        expected = fixed_runtime_folds | provider_folds
        if set(by_fold) != expected:
            _environment_error()
        canonical_names = tuple(sorted(allowed_by_fold[folded] for folded in provider_folds))
        provider_names_to_read = tuple(
            (allowed_by_fold[name.casefold()], name) for name in provider_names
        )

    def value(name: str) -> str:
        actual = by_fold.get(name.casefold())
        if actual is None:
            _environment_error()
        result = environment[actual]
        if not isinstance(result, str):
            _environment_error()
        return result

    expected_values = {
        _ENV_SKILL_IDENTITY: "golden-key-openmontage",
        _ENV_BRIDGE_CONTRACT_ID: _BRIDGE_CONTRACT_ID,
        _ENV_REQUEST_SCHEMA_ID: _REQUEST_SCHEMA,
        _ENV_RESULT_SCHEMA_ID: _RESULT_SCHEMA,
        _ENV_MODULE_NAME: _MODULE_NAME,
        _ENV_FIXED_ARGV: _FIXED_ARGV_TEXT,
    }
    for name, expected_value in expected_values.items():
        if value(name) != expected_value:
            _asset_error()
    release_identity = _asset_text(value(_ENV_RELEASE_IDENTITY))
    authority_owner = _asset_text(value(_ENV_AUTHORITY_OWNER))
    definition_id = _asset_text(value(_ENV_PACKAGE_TOOL_DEFINITION_ID))
    definition_sha256 = value(_ENV_PACKAGE_TOOL_DEFINITION_SHA256)
    if not re.fullmatch(r"[0-9a-f]{64}", definition_sha256):
        _asset_error()
    definition_relative_path = _asset_text(value(_ENV_PACKAGE_TOOL_DEFINITION_RELATIVE_PATH))
    if value(_ENV_REQUEST_SCHEMA_SHA256) != _REQUEST_SCHEMA_SHA256:
        _asset_error()
    if value(_ENV_RESULT_SCHEMA_SHA256) != _RESULT_SCHEMA_SHA256:
        _asset_error()
    if value(_ENV_FIXED_ARGV_SHA256) != hashlib.sha256(_FIXED_ARGV_TEXT.encode("utf-8")).hexdigest():
        _asset_error()
    if value(_ENV_MODULE_SHA256) != _file_sha256(Path(__file__)):
        _asset_error()
    interpreter_path = Path(value(_ENV_INTERPRETER_PATH))
    try:
        if not interpreter_path.is_absolute() or interpreter_path.resolve() != Path(sys.executable).resolve():
            _asset_error()
    except (OSError, RuntimeError, ValueError):
        _asset_error()
    if value(_ENV_INTERPRETER_SHA256) != _file_sha256(interpreter_path):
        _asset_error()

    provider: dict[str, str] = {}
    secrets: list[str] = []
    for canonical_name, requested_name in provider_names_to_read:
        provider[canonical_name] = value(requested_name)
        if "\x00" in provider[canonical_name] or any(
            0xD800 <= ord(char) <= 0xDFFF for char in provider[canonical_name]
        ):
            _environment_error()
        try:
            encoded = provider[canonical_name].encode("utf-8")
        except UnicodeEncodeError:
            _environment_error()
        if encoded:
            secrets.append(provider[canonical_name])
            if encoded in raw:
                _environment_error()
    return provider, tuple(secrets), canonical_names, {
        "release_identity": release_identity,
        "authority_owner": authority_owner,
        "definition_id": definition_id,
        "definition_sha256": definition_sha256,
        "definition_relative_path": definition_relative_path,
    }


def _bind_installer_definition(
    request: dict[str, Any], installer_identity: Mapping[str, str]
) -> None:
    """Require the complete request definition to match the stamped release asset."""

    definition = request["package_tool_definition"]
    if not isinstance(definition, Mapping):
        _asset_error()
    expected = {
        "package_release": installer_identity["release_identity"],
        "authority_owner": installer_identity["authority_owner"],
        "definition_id": installer_identity["definition_id"],
        "definition_sha256": installer_identity["definition_sha256"],
        "definition_relative_path": installer_identity["definition_relative_path"],
    }
    if any(definition.get(field) != value for field, value in expected.items()):
        _asset_error()
    # Keep the full caller envelope while making the release binding explicit.
    request["package_tool_definition"] = dict(definition)


def _secret_occurs(value: Any, secrets: tuple[str, ...]) -> bool:
    if isinstance(value, str):
        return any(secret and secret in value for secret in secrets)
    if value is True:
        scalar = "true"
    elif value is False:
        scalar = "false"
    elif value is None:
        scalar = "null"
    elif type(value) in (int, float):
        scalar = str(value)
    else:
        scalar = None
    if scalar is not None and any(secret and secret in scalar for secret in secrets):
        return True
    if isinstance(value, Mapping):
        return any(_secret_occurs(key, secrets) or _secret_occurs(item, secrets) for key, item in value.items())
    if isinstance(value, (list, tuple)):
        return any(_secret_occurs(item, secrets) for item in value)
    return False


def _reconstructed_controls(request: Mapping[str, Any], provider: Mapping[str, str]) -> dict[str, Any]:
    controls = request["executor_controls"]
    return {
        "schema_version": controls["schema_version"],
        "session_id": controls["session_id"],
        "request_id": controls["request_id"],
        "timeout_seconds": controls["timeout_seconds"],
        "termination_grace_seconds": controls["termination_grace_seconds"],
        "result_root": controls["result_root"],
        "provider_environment": dict(provider),
    }


def _wire_value(value: Any) -> Any:
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, item in value.items():
            if not isinstance(key, str) or key in result:
                _output_error()
            result[key] = _wire_value(item)
        return result
    if isinstance(value, (list, tuple)):
        return [_wire_value(item) for item in value]
    if isinstance(value, str):
        if any(0xD800 <= ord(char) <= 0xDFFF for char in value) or unicodedata.normalize("NFC", value) != value:
            _output_error()
        try:
            value.encode("utf-8")
        except UnicodeEncodeError:
            _output_error()
        return value
    if value is None or isinstance(value, bool) or type(value) is int:
        return value
    if type(value) is float and math.isfinite(value):
        return value
    _output_error()


def _receipt_identity_matches(
    wire: Mapping[str, Any], request: Mapping[str, Any]
) -> None:
    controls = request["executor_controls"]
    definition = request["package_tool_definition"]
    if not isinstance(controls, Mapping) or not isinstance(definition, Mapping):
        _output_error()
    message_bytes = request["user_message"].encode("utf-8")
    expected = {
        "session_id": controls["session_id"],
        "request_id": controls["request_id"],
        "message_sha256": hashlib.sha256(message_bytes).hexdigest(),
        "message_byte_length": len(message_bytes),
        "package_release": definition["package_release"],
        "package_commit": definition["package_commit"],
        "definition_id": definition["definition_id"],
        "definition_sha256": definition["definition_sha256"],
        "authority_owner": definition["authority_owner"],
    }
    partial_prelaunch = wire["outcome"] == "PRELAUNCH_BLOCKED" or (
        wire["outcome"] == "CANCELLED" and wire["reason_code"] == "CANCELLED_BEFORE_SPAWN"
    )

    def match_scalar(container: Any, field: str, expected_value: Any) -> bool:
        if not isinstance(container, Mapping) or field not in container:
            _output_error()
        actual = container[field]
        if actual is None:
            return partial_prelaunch
        if actual != expected_value:
            _output_error()
        return True

    match_scalar(wire["session"], "session_id", expected["session_id"])
    match_scalar(wire["request"], "request_id", expected["request_id"])
    message = wire["user_message"]
    if not isinstance(message, Mapping) or "sha256" not in message or "byte_length" not in message:
        _output_error()
    message_sha = message["sha256"]
    message_length = message["byte_length"]
    if (message_sha is None) != (message_length is None):
        _output_error()
    message_present = message_sha is not None
    if message_present and (
        message_sha != expected["message_sha256"] or message_length != expected["message_byte_length"]
    ):
        _output_error()
    if not partial_prelaunch and not message_present:
        _output_error()

    package = wire["package"]
    if not isinstance(package, Mapping):
        _output_error()
    package_release = package.get("openmontage_release")
    package_commit = package.get("openmontage_commit")
    if (package_release is None) != (package_commit is None):
        _output_error()
    package_present = package_release is not None
    if package_present and (
        package_release != expected["package_release"] or package_commit != expected["package_commit"]
    ):
        _output_error()
    if not partial_prelaunch and not package_present:
        _output_error()

    tool_definition = wire["tool_definition"]
    if not isinstance(tool_definition, Mapping):
        _output_error()
    definition_fields = (
        ("authority_owner", expected["authority_owner"]),
        ("definition_id", expected["definition_id"]),
        ("definition_sha256", expected["definition_sha256"]),
    )
    definition_values = [tool_definition.get(field) for field, _ in definition_fields]
    if any(value is None for value in definition_values) and any(value is not None for value in definition_values):
        _output_error()
    definition_present = all(value is not None for value in definition_values)
    if definition_present:
        for (field, expected_value), actual in zip(definition_fields, definition_values):
            if actual != expected_value:
                _output_error()
    if not partial_prelaunch and not definition_present:
        _output_error()

    if partial_prelaunch:
        if wire["spawn_count"] != 0 or wire["launched"] is not False:
            _output_error()
    elif wire["outcome"] == "SPAWN_FAILED":
        if wire["spawn_count"] != 0 or wire["launched"] is not False:
            _output_error()
    elif wire["spawn_count"] != 1 or wire["launched"] is not True:
        _output_error()
def _validate_receipt(
    value: Any,
    provider_names: tuple[str, ...],
    secrets: tuple[str, ...],
    request: Mapping[str, Any] | None = None,
) -> bytes:
    wire = _wire_value(value)
    if not isinstance(wire, dict) or set(wire) != _RECEIPT_FIELDS:
        _output_error()
    if wire["schema_version"] != _RESULT_SCHEMA or wire["outcome"] not in _OUTCOMES or wire["reason_code"] not in _REASONS:
        _output_error()
    if wire["retry_count"] != 0 or type(wire["spawn_count"]) is not int or wire["spawn_count"] not in (0, 1):
        _output_error()
    if wire["provider_environment_names"] != list(provider_names):
        _output_error()
    if request is not None:
        _receipt_identity_matches(wire, request)
    if _secret_occurs(wire, secrets):
        _output_error()
    try:
        payload = _canonical_json(wire)
    except _BridgeError:
        _output_error()
    if len(payload) > _MAX_OUTPUT_BYTES:
        _output_error()
    return payload


def _read_stdin() -> bytes:
    try:
        stream = getattr(sys.stdin, "buffer", sys.stdin)
        raw = stream.read(_MAX_INPUT_BYTES + 1)
        if isinstance(raw, str):
            raw = raw.encode("utf-8")
        if not isinstance(raw, bytes):
            _input_error()
        if len(raw) > _MAX_INPUT_BYTES:
            _input_error()
        return raw
    except _BridgeError:
        raise
    except Exception:
        _input_error()


def _write_fixed(stream: Any, token: str) -> None:
    target = getattr(stream, "buffer", stream)
    payload = (token + "\n").encode("ascii")
    try:
        target.write(payload)
        target.flush()
    except Exception:
        return


def _write_stdout(payload: bytes) -> None:
    target = getattr(sys.stdout, "buffer", sys.stdout)
    try:
        target.write(payload)
        target.flush()
    except Exception:
        _internal_error()


def main() -> int:
    try:
        raw = _read_stdin()
        request = _validate_request(_parse_request(raw))
        provider, secrets, canonical_provider_names, installer_identity = _load_environment(request, raw)
        _bind_installer_definition(request, installer_identity)
        if _secret_occurs(request, secrets):
            _environment_error()
        cancel_event = threading.Event()
        if request["cancel_requested"]:
            cancel_event.set()
        try:
            receipt = _launch_session_tool(
                request["data_root"],
                request["user_message"],
                _reconstructed_controls(request, provider),
                request["package_tool_definition"],
                request["local_capability_evidence"],
                cancel_event=cancel_event,
            )
        except Exception:
            _internal_error()
        payload = _validate_receipt(receipt, canonical_provider_names, secrets, request)
        _write_stdout(payload)
        return 0
    except _BridgeError as error:
        _write_fixed(sys.stderr, error.token)
        return error.exit_code
    except Exception:
        _write_fixed(sys.stderr, "BRIDGE_INTERNAL_ERROR")
        return 70


__all__: tuple[str, ...] = ()


if __name__ == "__main__":
    raise SystemExit(main())
