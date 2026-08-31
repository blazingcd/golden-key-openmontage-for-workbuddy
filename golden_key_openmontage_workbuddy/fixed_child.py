"""Bounded mechanical child used by the final Shell package binding.

The child records only transport facts and a handoff receipt.  It does not
interpret the user's request, choose a provider or renderer, or run a
production pipeline; those decisions remain with WorkBuddy/OpenMontage.
"""

from __future__ import annotations

import hashlib
import importlib
import json
import os
import re
import stat
import sys
import unicodedata
from pathlib import Path, PurePosixPath
from typing import Any


sys.dont_write_bytecode = True

REQUEST_SCHEMA = "golden-key-workbuddy-package-tool-request-v1"
RESULT_SCHEMA = "golden-key-workbuddy-package-tool-result-v1"
HANDOFF_SCHEMA = "golden-key-workbuddy-fixed-child-handoff-v2"
CONFIGURATION_DISPATCH_SCHEMA = "golden-key-workbuddy-configuration-dispatch-v1"
CONFIGURATION_ACTION_SCHEMA = "golden-key-workbuddy-configuration-action-v1"
MAX_INPUT_BYTES = 4 * 1024 * 1024
MAX_OUTPUT_BYTES = 1024 * 1024
MAX_PACKAGE_SUMMARY_BYTES = 512 * 1024
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
IDENTIFIER_RE = re.compile(r"^[A-Za-z0-9._-]{1,128}$")
ENV_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
SECRET_NAME_RE = re.compile(r"(?:KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL)", re.IGNORECASE)
REPARSE_ATTRIBUTE = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)


class _InputError(ValueError):
    pass


def _canonical(value: Any, *, newline: bool = True) -> bytes:
    try:
        text = json.dumps(
            value,
            allow_nan=False,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        return text.encode("utf-8") + (b"\n" if newline else b"")
    except (TypeError, ValueError, UnicodeEncodeError, RecursionError) as exc:
        raise _InputError("non-canonical-value") from exc


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _InputError("duplicate-key")
        result[key] = value
    return result


def _text(value: Any, *, empty: bool = False) -> str:
    if not isinstance(value, str) or (not empty and not value):
        raise _InputError("text")
    if any(0xD800 <= ord(char) <= 0xDFFF for char in value):
        raise _InputError("surrogate")
    if unicodedata.normalize("NFC", value) != value:
        raise _InputError("non-nfc")
    return value


def _mapping(value: Any, fields: set[str]) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != fields:
        raise _InputError("closed-mapping")
    return value


def _sha(value: Any) -> str:
    value = _text(value)
    if SHA256_RE.fullmatch(value) is None:
        raise _InputError("sha256")
    return value


def _safe_result_root(value: Any) -> Path:
    path = Path(_text(value))
    if not path.is_absolute() or "~" in path.parts or not path.is_dir():
        raise _InputError("result-root")
    try:
        status = path.lstat()
        if path.is_symlink() or bool(getattr(status, "st_file_attributes", 0) & REPARSE_ATTRIBUTE):
            raise _InputError("result-root-reparse")
        resolved = path.resolve(strict=True)
    except (OSError, RuntimeError) as exc:
        raise _InputError("result-root") from exc
    if not resolved.is_dir():
        raise _InputError("result-root")
    _assert_no_reparse_chain(resolved)
    return resolved


def _assert_no_reparse_chain(path: Path, *, boundary: Path | None = None) -> None:
    """Check each existing parent with lstat before handoff I/O."""

    path = Path(path)
    if boundary is not None:
        boundary = Path(boundary)
        try:
            path.relative_to(boundary)
        except ValueError as exc:
            raise _InputError("handoff-path") from exc
    current = path
    while True:
        try:
            status = current.lstat()
        except FileNotFoundError:
            status = None
        except OSError as exc:
            raise _InputError("handoff-parent") from exc
        if status is not None and (
            stat.S_ISLNK(status.st_mode)
            or bool(getattr(status, "st_file_attributes", 0) & REPARSE_ATTRIBUTE)
        ):
            raise _InputError("handoff-parent-reparse")
        if boundary is not None and current == boundary:
            break
        parent = current.parent
        if parent == current:
            break
        current = parent


def _handoff_directory(root: Path) -> Path:
    directory = root / "fixed-child-handoff"
    _assert_no_reparse_chain(directory, boundary=root)
    try:
        directory.mkdir(exist_ok=True)
    except OSError as exc:
        raise _InputError("handoff-parent") from exc
    _assert_no_reparse_chain(directory, boundary=root)
    try:
        if not directory.is_dir():
            raise _InputError("handoff-parent")
    except OSError as exc:
        raise _InputError("handoff-parent") from exc
    return directory


def _restore_environment(before: dict[str, str]) -> None:
    for name in tuple(os.environ):
        if name not in before:
            os.environ.pop(name, None)
    os.environ.update(before)


def _secret_values(
    provider_environment_names: list[str],
    before: dict[str, str],
    after: dict[str, str],
) -> set[str]:
    explicit = set(provider_environment_names)
    values: set[str] = set()
    for environment in (before, after):
        for name, value in environment.items():
            if not value or (name not in explicit and (len(value) < 8 or SECRET_NAME_RE.search(name) is None)):
                continue
            values.add(value)
    return values


def _contains_secret(value: Any, secrets: set[str]) -> bool:
    if isinstance(value, str):
        return any(secret in value for secret in secrets)
    if isinstance(value, dict):
        return any(
            _contains_secret(key, secrets) or _contains_secret(item, secrets)
            for key, item in value.items()
        )
    if isinstance(value, (list, tuple)):
        return any(_contains_secret(item, secrets) for item in value)
    return False


def _unverified_package_summary(source: str, error_code: str = "UNAVAILABLE") -> dict[str, Any]:
    return {"source": source, "status": "NOT_VERIFIED", "facts": None, "error_code": error_code}


def _package_capability_summary(provider_environment_names: list[str]) -> dict[str, Any]:
    source = "registry.provider_menu_summary"
    before_environment = dict(os.environ)
    before_modules = set(sys.modules)
    package_root = Path.cwd().resolve(strict=True)
    module_path = package_root / "tools" / "tool_registry.py"
    if not module_path.is_file():
        return _unverified_package_summary(source)
    _assert_no_reparse_chain(module_path, boundary=package_root)
    sys.path.insert(0, str(package_root))
    try:
        try:
            module = importlib.import_module("tools.tool_registry")
            loaded_path = Path(module.__file__).resolve(strict=True)
            if loaded_path != module_path.resolve(strict=True):
                raise _InputError("package-summary-source")
            summary = module.registry.provider_menu_summary()
        except _InputError:
            raise
        except Exception:
            return _unverified_package_summary(source)
        after_environment = dict(os.environ)
        try:
            encoded = _canonical(summary, newline=False)
            unsafe = not isinstance(summary, dict) or len(encoded) > MAX_PACKAGE_SUMMARY_BYTES
            unsafe = unsafe or _contains_secret(
                summary,
                _secret_values(provider_environment_names, before_environment, after_environment),
            )
        except _InputError:
            unsafe = True
        if unsafe:
            return _unverified_package_summary(source, "REJECTED")
        return {"source": source, "status": "REPORTED", "facts": summary, "error_code": None}
    finally:
        _restore_environment(before_environment)
        if sys.path and sys.path[0] == str(package_root):
            sys.path.pop(0)
        for name in tuple(sys.modules):
            if name not in before_modules and (name == "tools" or name.startswith("tools.")):
                sys.modules.pop(name, None)


def _configuration_action(request: dict[str, Any]) -> tuple[dict[str, Any], dict[str, Any] | None] | None:
    try:
        value = json.loads(request["message"], object_pairs_hook=_pairs)
    except (json.JSONDecodeError, _InputError):
        return None
    if not isinstance(value, dict) or value.get("schema_version") != CONFIGURATION_DISPATCH_SCHEMA:
        return None
    envelope = _mapping(value, {"schema_version", "request_id", "action", "configuration_result"})
    if envelope["request_id"] != request["request_id"]:
        raise _InputError("configuration-request")
    action = _mapping(
        envelope["action"],
        {
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
        },
    )
    if (
        action["schema_version"] != CONFIGURATION_ACTION_SCHEMA
        or action["package_release"] != request["openmontage_release"]
        or action["package_commit"] != request["openmontage_commit"]
        or action["package_definition_sha256"] != request["tool_definition_sha256"]
    ):
        raise _InputError("configuration-binding")
    result = envelope["configuration_result"]
    if result is not None and not isinstance(result, dict):
        raise _InputError("configuration-result")
    return dict(action), result


def _package_connection_test(request: dict[str, Any], action: dict[str, Any]) -> dict[str, Any]:
    if (
        action["action"] not in {"configure_provider", "retest_provider"}
        or action["capability"] != "video_generation"
        or action["provider"] != "seedance_ark"
        or action["consent"] != "confirmed"
        or action["capability_definitions"] is not None
        or action["user_decisions"] is not None
        or request["provider_environment_names"] != ["ARK_API_KEY"]
    ):
        raise _InputError("configuration-provider")
    package_root = Path.cwd().resolve(strict=True)
    release_path = package_root / "GOLDEN_KEY_OPENMONTAGE_RELEASE.json"
    module_path = package_root / "tools" / "video" / "seedance_ark.py"
    for path in (release_path, module_path):
        if not path.is_file():
            raise _InputError("configuration-package")
        _assert_no_reparse_chain(path, boundary=package_root)
    try:
        release = json.loads(release_path.read_text(encoding="utf-8"), object_pairs_hook=_pairs)
        declarations = release["workbuddy_configuration_actions"]
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, _InputError) as exc:
        raise _InputError("configuration-declaration") from exc
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
    if declarations != [expected]:
        raise _InputError("configuration-declaration")
    before_modules = set(sys.modules)
    sys.path.insert(0, str(package_root))
    try:
        module = importlib.import_module("tools.video.seedance_ark")
        if Path(module.__file__).resolve(strict=True) != module_path.resolve(strict=True):
            raise _InputError("configuration-package")
        result = module.SeedanceArkVideo().connection_test()
    except _InputError:
        raise
    except Exception as exc:
        raise _InputError("configuration-execution") from exc
    finally:
        if sys.path and sys.path[0] == str(package_root):
            sys.path.pop(0)
        for name in tuple(sys.modules):
            if name not in before_modules and (name == "tools" or name.startswith("tools.")):
                sys.modules.pop(name, None)
    fields = {
        "status",
        "error_code",
        "check",
        "request_kind",
        "media_executed",
        "paid_task_created",
        "proves",
        "does_not_prove",
    }
    result = _mapping(result, fields)
    if (
        result["status"] not in {"CHECK_SUCCEEDED", "NOT_CONNECTED"}
        or result["check"] != "ARK_DOCUMENTED_PING"
        or result["request_kind"] != "READ_ONLY_NON_MEDIA"
        or result["media_executed"] is not False
        or result["paid_task_created"] is not False
        or not isinstance(result["proves"], list)
        or not isinstance(result["does_not_prove"], list)
    ):
        raise _InputError("configuration-result")
    return dict(result)


def _configuration_result(request: dict[str, Any]) -> dict[str, Any] | None:
    parsed = _configuration_action(request)
    if parsed is None:
        return None
    action, result = parsed
    if result is None:
        result = _package_connection_test(request, action)
    elif request["provider_environment_names"]:
        raise _InputError("configuration-provider")
    secrets = _secret_values(request["provider_environment_names"], dict(os.environ), dict(os.environ))
    if _contains_secret(result, secrets) or len(_canonical(result, newline=False)) > MAX_PACKAGE_SUMMARY_BYTES:
        raise _InputError("configuration-result")
    return {
        "action": action["action"],
        "capability": action["capability"],
        "provider": action["provider"],
        "consent": action["consent"],
        "package_release": action["package_release"],
        "package_commit": action["package_commit"],
        "package_definition_sha256": action["package_definition_sha256"],
        "outcome": result,
    }


def _validate(raw: bytes) -> dict[str, Any]:
    if len(raw) > MAX_INPUT_BYTES or not raw.endswith(b"\n"):
        raise _InputError("wire")
    try:
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=_pairs)
    except (UnicodeDecodeError, json.JSONDecodeError, _InputError) as exc:
        raise _InputError("json") from exc
    if _canonical(value) != raw:
        raise _InputError("wire")
    request = _mapping(
        value,
        {
            "schema_version",
            "session_id",
            "request_id",
            "user_message",
            "executor_controls",
            "package",
            "tool_definition_sha256",
            "local_capability_evidence_identities",
        },
    )
    if request["schema_version"] != REQUEST_SCHEMA:
        raise _InputError("schema")
    for field in ("session_id", "request_id"):
        identifier = _text(request[field])
        if IDENTIFIER_RE.fullmatch(identifier) is None:
            raise _InputError("identifier")
    message = _text(request["user_message"], empty=True)
    controls = _mapping(request["executor_controls"], {"timeout_seconds", "result_root", "provider_environment_names"})
    if type(controls["timeout_seconds"]) is not int or not 1 <= controls["timeout_seconds"] <= 3600:
        raise _InputError("timeout")
    result_root = _safe_result_root(controls["result_root"])
    names = controls["provider_environment_names"]
    if not isinstance(names, list) or any(not isinstance(name, str) or ENV_NAME_RE.fullmatch(name) is None for name in names):
        raise _InputError("environment-names")
    if names != sorted(set(names)):
        raise _InputError("environment-names")
    package = _mapping(request["package"], {"registration_sha256", "openmontage_release", "openmontage_commit"})
    registration = _sha(package["registration_sha256"])
    release = _text(package["openmontage_release"])
    commit = _text(package["openmontage_commit"])
    if COMMIT_RE.fullmatch(commit) is None:
        raise _InputError("commit")
    definition = _sha(request["tool_definition_sha256"])
    identities = request["local_capability_evidence_identities"]
    if not isinstance(identities, list):
        raise _InputError("local-identities")
    identity_fields = {
        "capability_id",
        "definition_sha256",
        "approved_capability_definition_sha256",
        "original_stage3_fact_sha256",
        "status",
        "source",
        "plan_sha256",
        "entrypoint_sha256",
        "entrypoint_size",
    }
    normalized: list[dict[str, Any]] = []
    for item in identities:
        identity = _mapping(item, identity_fields)
        for field in (
            "definition_sha256",
            "approved_capability_definition_sha256",
            "original_stage3_fact_sha256",
            "plan_sha256",
            "entrypoint_sha256",
        ):
            _sha(identity[field])
        _text(identity["capability_id"])
        _text(identity["status"])
        _text(identity["source"])
        if type(identity["entrypoint_size"]) is not int or identity["entrypoint_size"] < 0:
            raise _InputError("entrypoint-size")
        normalized.append(dict(identity))
    if normalized != sorted(normalized, key=lambda item: (item["capability_id"], item["definition_sha256"])):
        raise _InputError("local-identities")
    return {
        "session_id": request["session_id"],
        "request_id": request["request_id"],
        "message": message,
        "timeout_seconds": controls["timeout_seconds"],
        "result_root": result_root,
        "provider_environment_names": list(names),
        "registration_sha256": registration,
        "openmontage_release": release,
        "openmontage_commit": commit,
        "tool_definition_sha256": definition,
        "local_capability_evidence_identities": normalized,
    }


def _write_handoff(request: dict[str, Any]) -> tuple[str, str, int]:
    relative = PurePosixPath("fixed-child-handoff") / f"{request['session_id']}--{request['request_id']}.json"
    root = request["result_root"]
    directory = _handoff_directory(root)
    package_capability_summary = _package_capability_summary(request["provider_environment_names"])
    configuration_result = _configuration_result(request)
    payload = _canonical(
        {
            "schema_version": HANDOFF_SCHEMA,
            "session_id": request["session_id"],
            "request_id": request["request_id"],
            "user_message_sha256": hashlib.sha256(request["message"].encode("utf-8")).hexdigest(),
            "user_message_byte_length": len(request["message"].encode("utf-8")),
            "executor_timeout_seconds": request["timeout_seconds"],
            "provider_environment_names": request["provider_environment_names"],
            "package": {
                "registration_sha256": request["registration_sha256"],
                "openmontage_release": request["openmontage_release"],
                "openmontage_commit": request["openmontage_commit"],
            },
            "tool_definition_sha256": request["tool_definition_sha256"],
            "local_capability_evidence_identities": request["local_capability_evidence_identities"],
            "package_capability_summary": package_capability_summary,
            "configuration_result": configuration_result,
            "decision_owner": "WorkBuddy",
            "production_decision_made": False,
            "provider_selected": False,
            "renderer_selected": False,
            "media_executed": False,
        }
    )
    if len(payload) > MAX_OUTPUT_BYTES:
        raise _InputError("handoff-size")
    path = directory / relative.name
    _assert_no_reparse_chain(path, boundary=root)
    created = False
    complete = False
    try:
        # WorkBuddy may retain deleted temporaries in the recycle bin, so a
        # hard-link publish can leave the result aliased and fail validation.
        with path.open("xb") as stream:
            created = True
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        _assert_no_reparse_chain(path, boundary=root)
        if path.read_bytes() != payload:
            raise _InputError("handoff-readback")
        complete = True
    except FileExistsError:
        _assert_no_reparse_chain(path, boundary=root)
        try:
            if path.read_bytes() != payload:
                raise _InputError("handoff-collision")
        except OSError as exc:
            raise _InputError("handoff-collision") from exc
        complete = True
    except OSError as exc:
        raise _InputError("handoff-write") from exc
    finally:
        if created and not complete:
            try:
                path.unlink(missing_ok=True)
            except OSError:
                pass
    return relative.as_posix(), hashlib.sha256(payload).hexdigest(), len(payload)


def main() -> int:
    try:
        raw = sys.stdin.buffer.read(MAX_INPUT_BYTES + 1)
        request = _validate(raw)
        relative, digest, size = _write_handoff(request)
        sys.stdout.buffer.write(
            _canonical(
                {
                    "schema_version": RESULT_SCHEMA,
                    "session_id": request["session_id"],
                    "request_id": request["request_id"],
                    "outcome": "SUCCEEDED",
                    "result_pointer": {"relative_path": relative, "sha256": digest, "size": size},
                    "error": None,
                }
            )
        )
        sys.stdout.buffer.flush()
        return 0
    except (_InputError, OSError, ValueError):
        return 64


if __name__ == "__main__":
    raise SystemExit(main())
