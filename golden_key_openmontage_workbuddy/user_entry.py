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
import re
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Any, Mapping

from . import package_registration
from . import runtime_prepare
from . import workbuddy_entry_cli as bridge


sys.dont_write_bytecode = True

_BINDING_SCHEMA = "golden-key-workbuddy-user-entry-binding-v1"
_BINDING_RELATIVE_PATH = "shell-adapter/package-runtime-binding.json"
_DATA_ROOT_RELATIVE = "../../data/production"
_RESULT_ROOT_RELATIVE = ("Results", "golden-key-openmontage")
_MAX_MESSAGE_BYTES = 8 * 1024 * 1024
_PACKAGE_RELEASE_FILE = "GOLDEN_KEY_OPENMONTAGE_RELEASE.json"
_ACTION_SCHEMA = "golden-key-workbuddy-configuration-action-v1"
_INTERNAL_ACTION_SCHEMA = "golden-key-workbuddy-configuration-dispatch-v1"
_CREDENTIAL_TARGET = "GoldenKeyOpenMontage/0.3.25/seedance-ark"
_ACTION_FIELDS = {
    "schema_version",
    "action",
    "capability",
    "provider",
    "package_release",
    "package_commit",
    "package_definition_sha256",
    "consent",
    "capability_definitions",
    "user_decisions",
}
_MANAGED_RUNTIME_FIELDS = frozenset(
    {
        "status",
        "source",
        "runtime_root",
        "verified_entrypoint",
        "version",
        "install_scope",
        "definition_sha256",
        "manifest_sha256",
        "lockfile_sha256",
    }
)
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


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


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise ValueError("duplicate-key")
        value[key] = item
    return value


def _configuration_action(message: str, definition: dict[str, Any]) -> dict[str, Any] | None:
    try:
        preview = json.loads(message)
    except json.JSONDecodeError:
        return None
    if not isinstance(preview, dict) or preview.get("schema_version") != _ACTION_SCHEMA:
        return None
    value = json.loads(message, object_pairs_hook=_pairs)
    if message.endswith("\r\n"):
        wire = message[:-2]
    elif message.endswith("\n"):
        wire = message[:-1]
    else:
        wire = message
    canonical = _canonical(value).decode("utf-8").removesuffix("\n")
    if set(value) != _ACTION_FIELDS or canonical != wire:
        raise ValueError("configuration-action")
    if (
        value["package_release"] != definition["package_release"]
        or value["package_commit"] != definition["package_commit"]
        or value["package_definition_sha256"] != definition["definition_sha256"]
    ):
        raise ValueError("configuration-action-binding")
    if value["action"] == "prepare_optional_capabilities":
        if (
            value["capability"] != "composition_runtime"
            or value["provider"] is not None
            or value["consent"] not in {"inspect", "confirmed"}
            or not isinstance(value["capability_definitions"], list)
            or (value["user_decisions"] is not None and not isinstance(value["user_decisions"], list))
            or (value["consent"] == "inspect") != (value["user_decisions"] is None)
        ):
            raise ValueError("configuration-action-local")
    elif value["action"] in {"configure_provider", "retest_provider"}:
        if (
            value["capability"] != "video_generation"
            or value["provider"] != "seedance_ark"
            or value["consent"] != "confirmed"
            or value["capability_definitions"] is not None
            or value["user_decisions"] is not None
        ):
            raise ValueError("configuration-action-provider")
    else:
        raise ValueError("configuration-action-kind")
    return value


def _validate_package_action(
    package_root: Path, definition: dict[str, Any], action: dict[str, Any]
) -> None:
    try:
        release = json.loads(
            (package_root / _PACKAGE_RELEASE_FILE).read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError("configuration-package-declaration") from exc
    if release.get("release_version") != definition["package_release"]:
        raise ValueError("configuration-package-declaration")
    if action["action"] == "prepare_optional_capabilities":
        declared = release.get("workbuddy_optional_capability_definitions")
        if not isinstance(declared, list) or action["capability_definitions"] != declared:
            raise ValueError("configuration-package-definition")
        return
    expected = {
        "action": "provider_connection_test",
        "capability": "video_generation",
        "provider": "seedance_ark",
        "credential_environment_name": "ARK_API_KEY",
        "implementation": "tools.video.seedance_ark:SeedanceArkVideo.connection_test",
        "request_kind": "READ_ONLY_NON_MEDIA",
        "endpoint_contract": "GET https://ark.cn-beijing.volces.com/ping",
        "official_documentation": "https://www.volcengine.com/docs/82379/1339360?lang=zh",
        "success_proves": "ark_documented_ping_succeeded",
        "retry": "forbidden",
    }
    if (
        release.get("workbuddy_configuration_actions") != [expected]
        or definition.get("allowed_environment_names") != ["ARK_API_KEY"]
        or definition.get("secret_environment_names") != ["ARK_API_KEY"]
    ):
        raise ValueError("configuration-package-declaration")


def _prompt_api_key() -> str | None:
    if os.name != "nt":
        raise OSError("credential-ui-unavailable")
    import ctypes
    from ctypes import wintypes

    class _CredUiInfo(ctypes.Structure):
        _fields_ = [
            ("cbSize", wintypes.DWORD),
            ("hwndParent", wintypes.HWND),
            ("pszMessageText", wintypes.LPCWSTR),
            ("pszCaptionText", wintypes.LPCWSTR),
            ("hbmBanner", wintypes.HANDLE),
        ]

    info = _CredUiInfo(
        ctypes.sizeof(_CredUiInfo),
        None,
        "请输入火山方舟 API Key。密钥只保存在当前 Windows 用户的凭据管理器中。",
        "金钥匙智能体",
        None,
    )
    user = ctypes.create_unicode_buffer("Golden Key OpenMontage", 100)
    password = ctypes.create_unicode_buffer(513)
    save = wintypes.BOOL(False)
    prompt = ctypes.windll.credui.CredUIPromptForCredentialsW
    prompt.argtypes = [
        ctypes.POINTER(_CredUiInfo),
        wintypes.LPCWSTR,
        ctypes.c_void_p,
        wintypes.DWORD,
        wintypes.LPWSTR,
        wintypes.DWORD,
        wintypes.LPWSTR,
        wintypes.DWORD,
        ctypes.POINTER(wintypes.BOOL),
        wintypes.DWORD,
    ]
    prompt.restype = wintypes.DWORD
    result = prompt(
        ctypes.byref(info),
        _CREDENTIAL_TARGET,
        None,
        0,
        user,
        len(user),
        password,
        len(password),
        ctypes.byref(save),
        0x00040000 | 0x00000080 | 0x00000002,
    )
    try:
        if result == 1223:
            return None
        if result != 0 or not password.value:
            raise OSError("credential-ui-failed")
        return password.value
    finally:
        ctypes.memset(ctypes.addressof(password), 0, ctypes.sizeof(password))


def _credential_api():
    if os.name != "nt":
        raise OSError("credential-store-unavailable")
    import ctypes
    from ctypes import wintypes

    class _Credential(ctypes.Structure):
        _fields_ = [
            ("Flags", wintypes.DWORD),
            ("Type", wintypes.DWORD),
            ("TargetName", wintypes.LPWSTR),
            ("Comment", wintypes.LPWSTR),
            ("LastWritten", wintypes.FILETIME),
            ("CredentialBlobSize", wintypes.DWORD),
            ("CredentialBlob", ctypes.POINTER(ctypes.c_ubyte)),
            ("Persist", wintypes.DWORD),
            ("AttributeCount", wintypes.DWORD),
            ("Attributes", ctypes.c_void_p),
            ("TargetAlias", wintypes.LPWSTR),
            ("UserName", wintypes.LPWSTR),
        ]

    library = ctypes.windll.advapi32
    library.CredWriteW.argtypes = [ctypes.POINTER(_Credential), wintypes.DWORD]
    library.CredWriteW.restype = wintypes.BOOL
    library.CredReadW.argtypes = [
        wintypes.LPCWSTR,
        wintypes.DWORD,
        wintypes.DWORD,
        ctypes.POINTER(ctypes.POINTER(_Credential)),
    ]
    library.CredReadW.restype = wintypes.BOOL
    library.CredFree.argtypes = [ctypes.c_void_p]
    return ctypes, library, _Credential


def _write_credential(secret: str) -> None:
    ctypes, library, credential_type = _credential_api()
    raw = secret.encode("utf-16-le")
    if not raw or len(raw) > 512:
        raise OSError("credential-size")
    blob = (ctypes.c_ubyte * len(raw)).from_buffer_copy(raw)
    credential = credential_type()
    credential.Type = 1
    credential.TargetName = _CREDENTIAL_TARGET
    credential.CredentialBlobSize = len(raw)
    credential.CredentialBlob = ctypes.cast(blob, ctypes.POINTER(ctypes.c_ubyte))
    credential.Persist = 2
    credential.UserName = "Golden Key OpenMontage"
    try:
        if not library.CredWriteW(ctypes.byref(credential), 0):
            raise OSError("credential-write")
    finally:
        ctypes.memset(ctypes.addressof(blob), 0, ctypes.sizeof(blob))


def _read_credential() -> str | None:
    ctypes, library, credential_type = _credential_api()
    pointer = ctypes.POINTER(credential_type)()
    if not library.CredReadW(_CREDENTIAL_TARGET, 1, 0, ctypes.byref(pointer)):
        if ctypes.windll.kernel32.GetLastError() == 1168:
            return None
        raise OSError("credential-read")
    try:
        raw = ctypes.string_at(pointer.contents.CredentialBlob, pointer.contents.CredentialBlobSize)
        return raw.decode("utf-16-le") if raw else None
    finally:
        library.CredFree(pointer)


def _prepare_action(
    action: dict[str, Any], data_root: Path, package_root: Path | None = None
) -> tuple[str | None, dict[str, Any] | None, list[dict[str, Any]]]:
    if action["action"] == "prepare_optional_capabilities":
        if package_root is None:
            result = runtime_prepare.prepare_optional_capabilities(
                data_root,
                action["capability_definitions"],
                action["user_decisions"],
            )
        else:
            result = runtime_prepare.prepare_optional_capabilities(
                data_root,
                action["capability_definitions"],
                action["user_decisions"],
                package_root=package_root,
            )
        return None, result, []
    try:
        if action["action"] == "configure_provider":
            secret = _prompt_api_key()
            if secret is None:
                return None, {"status": "CANCELLED", "error_code": None}, []
            _write_credential(secret)
        else:
            secret = _read_credential()
        if not secret:
            return None, {"status": "NOT_CONNECTED", "error_code": "CREDENTIAL_UNAVAILABLE"}, []
        return secret, None, []
    except OSError:
        return None, {"status": "NOT_CONNECTED", "error_code": "CREDENTIAL_STORE_UNAVAILABLE"}, []


def _managed_remotion_runtime(result: Mapping[str, Any] | None) -> dict[str, str] | None:
    if not isinstance(result, Mapping):
        return None
    if result.get("result") not in {"DETECTION_REPORT", "INTEGRATED"}:
        return None
    value = result.get("managed_remotion_runtime")
    if value is None:
        return None
    if not isinstance(value, Mapping) or not _MANAGED_RUNTIME_FIELDS.issubset(value):
        raise ValueError("managed-remotion-runtime")
    if set(value) - _MANAGED_RUNTIME_FIELDS:
        # Integration adds plan/reuse bookkeeping; Package receives only the
        # stable runtime identity it consumes.
        value = {key: value[key] for key in _MANAGED_RUNTIME_FIELDS}
    else:
        value = dict(value)
    if value["status"] != "PRESENT" or value["source"] != "managed":
        raise ValueError("managed-remotion-runtime")
    if value["install_scope"] not in {"system", "current-user"}:
        raise ValueError("managed-remotion-runtime")
    if not isinstance(value["version"], str) or not value["version"]:
        raise ValueError("managed-remotion-runtime")
    for field in ("definition_sha256", "manifest_sha256", "lockfile_sha256"):
        if not isinstance(value[field], str) or _SHA256_RE.fullmatch(value[field]) is None:
            raise ValueError("managed-remotion-runtime")
    try:
        root = Path(value["runtime_root"])
        entrypoint = Path(value["verified_entrypoint"])
        if (
            not root.is_absolute()
            or not entrypoint.is_absolute()
            or not root.is_dir()
            or not entrypoint.is_file()
            or entrypoint.resolve(strict=True).relative_to(root.resolve(strict=True)) is None
        ):
            raise ValueError("managed-remotion-runtime")
    except (OSError, RuntimeError, ValueError, TypeError):
        raise ValueError("managed-remotion-runtime") from None
    return value


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


def _request(
    package_root: Path,
    data_root: Path,
    definition: dict[str, Any],
    message: str,
    *,
    action: dict[str, Any] | None = None,
    configuration_result: dict[str, Any] | None = None,
    provider_secret: str | None = None,
    local_evidence: list[dict[str, Any]] | None = None,
    managed_remotion_runtime: dict[str, str] | None = None,
) -> tuple[dict[str, str], bytes]:
    session_id = f"workbuddy-{uuid.uuid4().hex}"
    request_id = f"request-{uuid.uuid4().hex}"
    if action is not None:
        message = _canonical(
            {
                "schema_version": _INTERNAL_ACTION_SCHEMA,
                "request_id": request_id,
                "action": action,
                "configuration_result": configuration_result,
            }
        ).decode("utf-8").removesuffix("\n")
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
    provider_names: list[str] = []
    if provider_secret is not None:
        environment["ARK_API_KEY"] = provider_secret
        provider_names = ["ARK_API_KEY"]
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
            "provider_environment_names": provider_names,
        },
        "package_tool_definition": definition,
        "local_capability_evidence": local_evidence or [],
        "managed_remotion_runtime": managed_remotion_runtime,
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
        action = _configuration_action(message, definition)
        provider_secret = None
        configuration_result = None
        local_evidence: list[dict[str, Any]] = []
        managed_remotion_runtime = None
        if action is not None:
            _validate_package_action(package_root, definition, action)
            provider_secret, configuration_result, local_evidence = _prepare_action(
                action, data_root, package_root
            )
            managed_remotion_runtime = _managed_remotion_runtime(configuration_result)
        environment, payload = _request(
            package_root,
            data_root,
            definition,
            message,
            action=action,
            configuration_result=configuration_result,
            provider_secret=provider_secret,
            local_evidence=local_evidence,
            managed_remotion_runtime=managed_remotion_runtime,
        )
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
