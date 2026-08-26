"""Opaque fixed entry for ordinary WorkBuddy user messages.

The entry accepts only the literal UTF-8 message on stdin.  It resolves the
installed package and its private binding locally, then invokes the existing
closed bridge once; it never interprets the message or makes production
decisions.
"""

from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Any

from . import package_registration
from . import workbuddy_entry_cli as bridge


sys.dont_write_bytecode = True

_BINDING_SCHEMA = "golden-key-workbuddy-user-entry-binding-v1"
_BINDING_RELATIVE_PATH = "shell-adapter/package-runtime-binding.json"
_DATA_ROOT_RELATIVE = "../../data/production"
_RESULT_ROOT_RELATIVE = ("Results", "golden-key-openmontage")
_MAX_MESSAGE_BYTES = 8 * 1024 * 1024


def _canonical(value: Any) -> bytes:
    return (
        json.dumps(value, allow_nan=False, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        .encode("utf-8")
        + b"\n"
    )


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _package_root() -> Path:
    package_root = Path(__file__).resolve().parents[2]
    if not package_root.is_dir():
        raise ValueError("package-root")
    return package_root


def _binding(package_root: Path) -> tuple[dict[str, Any], Path]:
    path = package_root / _BINDING_RELATIVE_PATH
    raw = path.read_bytes()
    value = json.loads(raw.decode("utf-8"))
    if _canonical(value) != raw or set(value) != {
        "schema_version",
        "data_root_relative",
        "entry_module",
        "entry_argv",
        "entry_module_sha256",
        "bridge_module",
        "bridge_module_sha256",
        "fixed_argv_sha256",
        "request_schema_sha256",
        "result_schema_sha256",
        "definition_relative_path",
        "definition_sha256",
    }:
        raise ValueError("binding")
    if value["schema_version"] != _BINDING_SCHEMA or value["data_root_relative"] != _DATA_ROOT_RELATIVE:
        raise ValueError("binding")
    if value["entry_module"] != "golden_key_openmontage_workbuddy.user_entry":
        raise ValueError("binding")
    if value["entry_argv"] != ["-I", "-m", bridge._MODULE_NAME]:
        raise ValueError("binding")
    if value["entry_module_sha256"] != _sha256(Path(__file__)):
        raise ValueError("binding")
    bridge_path = Path(bridge.__file__).resolve()
    if value["bridge_module"] != bridge._MODULE_NAME or value["bridge_module_sha256"] != _sha256(bridge_path):
        raise ValueError("binding")
    fixed_argv_text = bridge._FIXED_ARGV_TEXT
    if value["fixed_argv_sha256"] != hashlib.sha256(fixed_argv_text.encode("utf-8")).hexdigest():
        raise ValueError("binding")
    if value["request_schema_sha256"] != bridge._REQUEST_SCHEMA_SHA256 or value["result_schema_sha256"] != bridge._RESULT_SCHEMA_SHA256:
        raise ValueError("binding")
    definition_path = package_root / Path(*value["definition_relative_path"].split("/"))
    if value["definition_relative_path"] != "shell-adapter/package-tool-definition.json":
        raise ValueError("binding")
    definition_raw = definition_path.read_bytes()
    definition = json.loads(definition_raw.decode("utf-8"))
    if not isinstance(definition, dict) or _canonical(definition) != definition_raw or definition.get("definition_sha256") != value["definition_sha256"]:
        raise ValueError("binding")
    return value, definition_path


def _data_root(package_root: Path, binding: dict[str, Any]) -> Path:
    relative = Path(*binding["data_root_relative"].split("/"))
    data_root = (package_root / relative).resolve(strict=True)
    if not data_root.is_dir():
        raise ValueError("data-root")
    return data_root


def _request(package_root: Path, data_root: Path, definition: dict[str, Any], message: str) -> tuple[dict[str, str], bytes]:
    session_id = f"workbuddy-{uuid.uuid4().hex}"
    request_id = f"request-{uuid.uuid4().hex}"
    result_root = data_root.joinpath(*_RESULT_ROOT_RELATIVE)
    result_root.mkdir(parents=True, exist_ok=True)
    fixed_argv_text = bridge._FIXED_ARGV_TEXT
    module_path = Path(bridge.__file__).resolve()
    interpreter_path = Path(sys.executable).resolve()
    environment = {
        bridge._ENV_SKILL_IDENTITY: "golden-key-openmontage",
        bridge._ENV_RELEASE_IDENTITY: f"golden-key-openmontage-{definition['package_release']}",
        bridge._ENV_AUTHORITY_OWNER: definition["authority_owner"],
        bridge._ENV_PACKAGE_TOOL_DEFINITION_ID: definition["definition_id"],
        bridge._ENV_PACKAGE_TOOL_DEFINITION_SHA256: definition["definition_sha256"],
        bridge._ENV_PACKAGE_TOOL_DEFINITION_RELATIVE_PATH: definition["definition_relative_path"],
        bridge._ENV_BRIDGE_CONTRACT_ID: bridge._BRIDGE_CONTRACT_ID,
        bridge._ENV_REQUEST_SCHEMA_ID: bridge._REQUEST_SCHEMA,
        bridge._ENV_REQUEST_SCHEMA_SHA256: bridge._REQUEST_SCHEMA_SHA256,
        bridge._ENV_RESULT_SCHEMA_ID: bridge._RESULT_SCHEMA,
        bridge._ENV_RESULT_SCHEMA_SHA256: bridge._RESULT_SCHEMA_SHA256,
        bridge._ENV_MODULE_NAME: bridge._MODULE_NAME,
        bridge._ENV_MODULE_SHA256: _sha256(module_path),
        bridge._ENV_FIXED_ARGV: fixed_argv_text,
        bridge._ENV_FIXED_ARGV_SHA256: hashlib.sha256(fixed_argv_text.encode("utf-8")).hexdigest(),
        bridge._ENV_INTERPRETER_SHA256: _sha256(interpreter_path),
    }
    for name in bridge._runtime_environment_names():
        value = os.environ.get(name)
        if value is None:
            raise ValueError("runtime-environment")
        environment[name] = value
    request = {
        "schema_version": bridge._REQUEST_SCHEMA,
        "bridge_contract_id": bridge._BRIDGE_CONTRACT_ID,
        "data_root": str(data_root),
        "user_message": message,
        "executor_controls": {
            "schema_version": bridge._CONTROLS_SCHEMA,
            "session_id": session_id,
            "request_id": request_id,
            "timeout_seconds": 3600,
            "termination_grace_seconds": 30,
            "result_root": str(result_root),
            "provider_environment_source": "FIXED_CLI_PROCESS_ENV",
            "provider_environment_names": [],
        },
        "package_tool_definition": definition,
        "local_capability_evidence": [],
        "cancel_requested": False,
        "continuation": {"mode": "NONE", "prior_request_id": None},
    }
    return environment, _canonical(request)


def main() -> int:
    try:
        raw = sys.stdin.buffer.read(_MAX_MESSAGE_BYTES + 1)
        if len(raw) > _MAX_MESSAGE_BYTES:
            raise ValueError("message-size")
        message = raw.decode("utf-8")
        package_root = _package_root()
        binding, definition_path = _binding(package_root)
        data_root = _data_root(package_root, binding)
        definition = json.loads(definition_path.read_bytes().decode("utf-8"))
        environment, payload = _request(package_root, data_root, definition, message)
        command = [str(Path(sys.executable).resolve()), *binding["entry_argv"]]
        completed = subprocess.run(
            command,
            cwd=str(package_root),
            env=environment,
            input=payload,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        sys.stdout.buffer.write(completed.stdout)
        sys.stdout.buffer.flush()
        sys.stderr.buffer.write(completed.stderr)
        sys.stderr.buffer.flush()
        return completed.returncode
    except (OSError, UnicodeError, ValueError, TypeError, RecursionError, json.JSONDecodeError, package_registration.PackageRegistrationError):
        sys.stderr.buffer.write(b"WORKBUDDY_ENTRY_INVALID\n")
        sys.stderr.buffer.flush()
        return 64


__all__: tuple[str, ...] = ()


if __name__ == "__main__":
    raise SystemExit(main())
