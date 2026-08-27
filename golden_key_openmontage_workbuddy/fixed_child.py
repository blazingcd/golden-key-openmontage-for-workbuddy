"""Bounded mechanical child used by the final Shell package binding.

The child records only transport facts and a handoff receipt.  It does not
interpret the user's request, choose a provider or renderer, or run a
production pipeline; those decisions remain with WorkBuddy/OpenMontage.
"""

from __future__ import annotations

import hashlib
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
HANDOFF_SCHEMA = "golden-key-workbuddy-fixed-child-handoff-v1"
MAX_INPUT_BYTES = 4 * 1024 * 1024
MAX_OUTPUT_BYTES = 1024 * 1024
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
IDENTIFIER_RE = re.compile(r"^[A-Za-z0-9._-]{1,128}$")
ENV_NAME_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
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
