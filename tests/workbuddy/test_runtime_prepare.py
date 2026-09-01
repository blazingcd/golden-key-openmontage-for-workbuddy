from __future__ import annotations

import copy
import errno
import hashlib
import importlib
import json
import os
import shutil
import threading
import time
from pathlib import Path

import pytest

from golden_key_openmontage_workbuddy import prepare_optional_capabilities


runtime_prepare = importlib.import_module("golden_key_openmontage_workbuddy.runtime_prepare")


def _entrypoint_name(capability: str) -> str:
    return f"bin/{capability}.cmd" if os.name == "nt" else f"bin/{capability}"


def _payload(capability: str, version: str) -> bytes:
    if os.name == "nt":
        return f"@echo off\r\necho {capability} {version}\r\n".encode()
    return f"#!/bin/sh\necho {capability} {version}\n".encode()


def _forged_same_size_payload(capability: str, version: str) -> bytes:
    original = _payload(capability, version)
    if os.name == "nt":
        forged = original.replace(b"@echo off", b"@ECHO OFF")
    else:
        forged = original.replace(b"\necho ", b"\n echo ").removesuffix(b"\n")
    assert len(forged) == len(original)
    assert hashlib.sha256(forged).digest() != hashlib.sha256(original).digest()
    return forged


def _seal_definition(definition: dict) -> None:
    sources = sorted(
        (dict(source) for source in definition["approved_mainland_sources"]),
        key=lambda source: source["filename"],
    )
    assets = sorted(
        (dict(asset) for asset in definition["assets"]),
        key=lambda asset: (asset["managed_target"], asset["filename"]),
    )
    body = {
        "capability": definition["capability"],
        "version": definition["version"],
        "verified_entrypoint": definition["verified_entrypoint"],
        "approved_mainland_sources": sources,
        "assets": assets,
        "explicit_registered_or_configured_candidate_paths": sorted(
            definition.get("explicit_registered_or_configured_candidate_paths", [])
        ),
        "normal_command_name": definition.get("normal_command_name"),
    }
    encoded = json.dumps(
        body,
        allow_nan=False,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    definition["definition_sha256"] = hashlib.sha256(encoded).hexdigest()


def _definition(capability: str, version: str) -> tuple[dict, bytes]:
    payload = _payload(capability, version)
    filename = f"{capability}-{version}.bin"
    definition = {
            "capability": capability,
            "definition_sha256": "0" * 64,
            "version": version,
            "verified_entrypoint": _entrypoint_name(capability),
            "approved_mainland_sources": [
                {
                    "filename": filename,
                    "url": f"https://registry.npmmirror.com/{capability}/-/{filename}",
                }
            ],
            "assets": [
                {
                    "filename": filename,
                    "size": len(payload),
                    "sha256": hashlib.sha256(payload).hexdigest(),
                    "license": "MIT",
                    "managed_target": _entrypoint_name(capability),
                }
            ],
        }
    _seal_definition(definition)
    return definition, payload


@pytest.fixture
def definitions() -> tuple[list[dict], dict[str, bytes]]:
    remotion, remotion_payload = _definition("remotion", "4.0.1")
    hyperframes, hyperframes_payload = _definition("hyperframes", "1.3.0")
    payloads = {
        remotion["approved_mainland_sources"][0]["url"]: remotion_payload,
        hyperframes["approved_mainland_sources"][0]["url"]: hyperframes_payload,
    }
    return [remotion, hyperframes], payloads


def _managed_root(data_root: Path, definition: dict) -> Path:
    return (
        data_root
        / "Runtime"
        / "Composition"
        / definition["capability"]
        / definition["definition_sha256"]
    )


def _write_capability(root: Path, definition: dict, payload: bytes) -> Path:
    entrypoint = root / Path(definition["verified_entrypoint"])
    entrypoint.parent.mkdir(parents=True, exist_ok=True)
    entrypoint.write_bytes(payload)
    entrypoint.chmod(entrypoint.stat().st_mode | 0o111)
    return entrypoint


def _plans_by_capability(result: dict) -> dict[str, dict]:
    return {plan["capability"]: plan for plan in result["plans"]}


def _decision(definition: dict, plan: dict, action: str) -> dict:
    return {
        "decision": action,
        "capability": definition["capability"],
        "definition_sha256": definition["definition_sha256"],
        "plan_sha256": plan["plan_sha256"],
    }


def _install_transport(monkeypatch: pytest.MonkeyPatch, payloads: dict[str, bytes], calls: list[str]):
    def transport(url: str, destination: Path, expected_size: int) -> str:
        calls.append(url)
        assert len(payloads[url]) == expected_size
        destination.write_bytes(payloads[url])
        return url

    monkeypatch.setattr(runtime_prepare, "_download_asset", transport)


def test_both_missing_returns_deterministic_zero_write_plans(tmp_path: Path, definitions) -> None:
    catalog, _ = definitions
    data_root = tmp_path / "data"
    first = prepare_optional_capabilities(data_root, catalog)
    second = prepare_optional_capabilities(data_root, catalog)

    assert first == second
    assert first["result"] == "CONSENT_REQUIRED"
    assert [fact["status"] for fact in first["capabilities"]] == ["MISSING", "MISSING"]
    assert {plan["capability"] for plan in first["plans"]} == {"remotion", "hyperframes"}
    assert not data_root.exists()


def test_both_managed_present_are_reported_without_writes(tmp_path: Path, definitions) -> None:
    catalog, payloads = definitions
    data_root = tmp_path / "data"
    for definition in catalog:
        url = definition["approved_mainland_sources"][0]["url"]
        _write_capability(_managed_root(data_root, definition), definition, payloads[url])
    before = {path: path.stat().st_mtime_ns for path in data_root.rglob("*")}

    result = prepare_optional_capabilities(data_root, catalog)

    assert result["result"] == "DETECTION_REPORT"
    assert [fact["status"] for fact in result["capabilities"]] == ["PRESENT", "PRESENT"]
    assert {fact["evidence"]["source"] for fact in result["capabilities"]} == {"managed"}
    assert before == {path: path.stat().st_mtime_ns for path in data_root.rglob("*")}


def test_one_present_one_missing(tmp_path: Path, definitions) -> None:
    catalog, payloads = definitions
    data_root = tmp_path / "data"
    remotion = catalog[0]
    _write_capability(
        _managed_root(data_root, remotion),
        remotion,
        payloads[remotion["approved_mainland_sources"][0]["url"]],
    )
    result = prepare_optional_capabilities(data_root, catalog)
    facts = {fact["capability"]: fact for fact in result["capabilities"]}
    assert result["result"] == "CONSENT_REQUIRED"
    assert facts["remotion"]["status"] == "PRESENT"
    assert facts["hyperframes"]["status"] == "MISSING"


def test_incompatible_version_is_a_plan_not_a_failure(tmp_path: Path, definitions) -> None:
    catalog, _ = definitions
    data_root = tmp_path / "data"
    _write_capability(_managed_root(data_root, catalog[0]), catalog[0], _payload("remotion", "0.0.1"))
    result = prepare_optional_capabilities(data_root, catalog)
    facts = {fact["capability"]: fact for fact in result["capabilities"]}
    assert result["result"] == "CONSENT_REQUIRED"
    assert facts["remotion"]["status"] == "INCOMPATIBLE"


def test_explicit_candidate_is_bounded_and_verified(tmp_path: Path, definitions) -> None:
    catalog, payloads = definitions
    explicit = tmp_path / "registered-remotion"
    _write_capability(
        explicit,
        catalog[0],
        payloads[catalog[0]["approved_mainland_sources"][0]["url"]],
    )
    catalog[0]["explicit_registered_or_configured_candidate_paths"] = [str(explicit)]
    _seal_definition(catalog[0])
    result = prepare_optional_capabilities(tmp_path / "data", catalog)
    remotion = result["capabilities"][0]
    assert remotion["status"] == "PRESENT"
    assert remotion["evidence"]["source"] == "explicit"


def test_explicit_candidate_rejects_a_direct_file_without_executing_it(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, payloads = definitions
    direct_file = _write_capability(
        tmp_path / "registered-remotion",
        catalog[0],
        payloads[catalog[0]["approved_mainland_sources"][0]["url"]],
    )
    catalog[0]["explicit_registered_or_configured_candidate_paths"] = [str(direct_file)]
    _seal_definition(catalog[0])
    monkeypatch.setattr(runtime_prepare, "_probe", lambda *_a: pytest.fail("probe executed"))
    result = prepare_optional_capabilities(tmp_path / "data", catalog)
    remotion = result["capabilities"][0]
    assert remotion["status"] == "INCOMPATIBLE"
    assert remotion["candidates"][0]["identity_reason"] == "EXPLICIT_DIRECTORY_REQUIRED"


def test_explicit_spoofed_version_program_is_rejected_by_hash_before_probe(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, _ = definitions
    explicit = tmp_path / "registered-remotion"
    forged = _forged_same_size_payload("remotion", catalog[0]["version"])
    _write_capability(explicit, catalog[0], forged)
    catalog[0]["explicit_registered_or_configured_candidate_paths"] = [str(explicit)]
    _seal_definition(catalog[0])
    monkeypatch.setattr(runtime_prepare, "_probe", lambda *_a: pytest.fail("probe executed"))
    result = prepare_optional_capabilities(tmp_path / "data", catalog)
    remotion = result["capabilities"][0]
    assert remotion["status"] == "INCOMPATIBLE"
    assert remotion["candidates"][0]["asset_evidence"][0]["reason"] == "HASH_MISMATCH"


def test_path_candidate_uses_only_normal_resolution(tmp_path: Path, definitions, monkeypatch) -> None:
    catalog, payloads = definitions
    command = _write_capability(
        tmp_path / "path-candidate",
        catalog[0],
        payloads[catalog[0]["approved_mainland_sources"][0]["url"]],
    )
    catalog[0]["normal_command_name"] = command.name
    _seal_definition(catalog[0])
    monkeypatch.setattr(runtime_prepare.shutil, "which", lambda name: str(command) if name == command.name else None)
    result = prepare_optional_capabilities(tmp_path / "data", catalog)
    assert result["capabilities"][0]["evidence"]["source"] == "PATH"


def test_path_spoofed_version_program_is_rejected_by_hash_before_probe(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, _ = definitions
    command = _write_capability(
        tmp_path / "path-candidate",
        catalog[0],
        _forged_same_size_payload("remotion", catalog[0]["version"]),
    )
    catalog[0]["normal_command_name"] = command.name
    _seal_definition(catalog[0])
    monkeypatch.setattr(runtime_prepare.shutil, "which", lambda name: str(command))
    monkeypatch.setattr(runtime_prepare, "_probe", lambda *_a: pytest.fail("probe executed"))
    result = prepare_optional_capabilities(tmp_path / "data", catalog)
    remotion = result["capabilities"][0]
    assert remotion["status"] == "INCOMPATIBLE"
    assert remotion["candidates"][0]["identity_reason"] == "PATH_ENTRYPOINT_IDENTITY_MISMATCH"


def test_missing_detection_does_not_probe_or_enumerate(tmp_path: Path, definitions, monkeypatch) -> None:
    catalog, _ = definitions
    catalog[0]["normal_command_name"] = "remotion.cmd" if os.name == "nt" else "remotion"
    _seal_definition(catalog[0])
    monkeypatch.setattr(runtime_prepare.shutil, "which", lambda _name: None)
    monkeypatch.setattr(runtime_prepare.subprocess, "run", lambda *_a, **_k: pytest.fail("probe called"))
    monkeypatch.setattr(runtime_prepare.os, "walk", lambda *_a, **_k: pytest.fail("disk scan called"))
    result = prepare_optional_capabilities(tmp_path / "data", catalog)
    assert result["result"] == "CONSENT_REQUIRED"


@pytest.mark.parametrize("action", ["decline", "defer"])
def test_decline_and_defer_are_skipped_without_download(tmp_path: Path, definitions, action: str, monkeypatch) -> None:
    catalog, _ = definitions
    first = prepare_optional_capabilities(tmp_path / "data", catalog)
    plans = _plans_by_capability(first)
    decisions = [_decision(item, plans[item["capability"]], action) for item in catalog]
    monkeypatch.setattr(runtime_prepare, "_download_asset", lambda *_a: pytest.fail("download called"))
    result = prepare_optional_capabilities(tmp_path / "data", catalog, decisions)
    assert result["result"] == "SKIPPED"
    assert {fact["status"] for fact in result["capabilities"]} == {"NOT_INTEGRATED"}
    assert not (tmp_path / "data").exists()


def test_approve_prepares_only_approved_capability(tmp_path: Path, definitions, monkeypatch) -> None:
    catalog, payloads = definitions
    data_root = tmp_path / "data"
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    decisions = [
        _decision(catalog[0], plans["remotion"], "approve"),
        _decision(catalog[1], plans["hyperframes"], "decline"),
    ]
    calls: list[str] = []
    _install_transport(monkeypatch, payloads, calls)
    result = prepare_optional_capabilities(data_root, catalog, decisions)
    assert result["result"] == "INTEGRATED"
    assert calls == [catalog[0]["approved_mainland_sources"][0]["url"]]
    assert _managed_root(data_root, catalog[0]).is_dir()
    assert not _managed_root(data_root, catalog[1]).exists()
    facts = {fact["capability"]: fact for fact in result["capabilities"]}
    assert facts["hyperframes"]["status"] == "NOT_INTEGRATED"


def test_partial_decisions_keep_unaddressed_capability_at_consent_required(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, payloads = definitions
    data_root = tmp_path / "data"
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    calls: list[str] = []
    _install_transport(monkeypatch, payloads, calls)
    result = prepare_optional_capabilities(
        data_root,
        catalog,
        [_decision(catalog[0], plans["remotion"], "approve")],
    )
    assert result["result"] == "CONSENT_REQUIRED"
    assert [plan["capability"] for plan in result["plans"]] == ["hyperframes"]
    assert result["integrated"][0]["capability"] == "remotion"
    assert calls == [catalog[0]["approved_mainland_sources"][0]["url"]]


def test_approved_integration_is_idempotently_reused(tmp_path: Path, definitions, monkeypatch) -> None:
    catalog, payloads = definitions
    data_root = tmp_path / "data"
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    decisions = [_decision(item, plans[item["capability"]], "approve") for item in catalog]
    calls: list[str] = []
    _install_transport(monkeypatch, payloads, calls)
    integrated = prepare_optional_capabilities(data_root, catalog, decisions)
    assert integrated["result"] == "INTEGRATED", integrated
    mtimes = {path: path.stat().st_mtime_ns for path in data_root.rglob("*")}
    detected = prepare_optional_capabilities(data_root, catalog, decisions)
    assert detected["result"] == "DETECTION_REPORT"
    assert calls == [item["approved_mainland_sources"][0]["url"] for item in catalog]
    assert mtimes == {path: path.stat().st_mtime_ns for path in data_root.rglob("*")}


def test_stale_or_missing_approval_never_downloads(tmp_path: Path, definitions, monkeypatch) -> None:
    catalog, _ = definitions
    first = prepare_optional_capabilities(tmp_path / "data", catalog)
    plans = _plans_by_capability(first)
    stale = _decision(catalog[0], plans["remotion"], "approve")
    stale["plan_sha256"] = "f" * 64
    monkeypatch.setattr(runtime_prepare, "_download_asset", lambda *_a: pytest.fail("download called"))
    result = prepare_optional_capabilities(tmp_path / "data", catalog, [stale])
    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "STALE_DECISION"
    assert not (tmp_path / "data").exists()


def test_definition_digest_must_match_normalized_closed_content(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, _ = definitions
    catalog[0]["definition_sha256"] = "f" * 64
    monkeypatch.setattr(runtime_prepare, "_detect_one", lambda *_a: pytest.fail("detection called"))
    result = prepare_optional_capabilities(tmp_path / "data", catalog)
    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "INVALID_DEFINITION"
    assert "normalized closed definition" in result["message"]


@pytest.mark.parametrize("changed_field", ["version", "url", "asset", "license", "target"])
def test_any_definition_content_change_invalidates_old_approval(
    tmp_path: Path, definitions, monkeypatch, changed_field: str
) -> None:
    catalog, _ = definitions
    data_root = tmp_path / "data"
    first = prepare_optional_capabilities(data_root, catalog)
    old_plan = _plans_by_capability(first)["remotion"]
    old_decision = _decision(catalog[0], old_plan, "approve")
    old_definition_sha = catalog[0]["definition_sha256"]

    if changed_field == "version":
        catalog[0]["version"] = "4.0.2"
    elif changed_field == "url":
        catalog[0]["approved_mainland_sources"][0]["url"] = (
            "https://registry.npmmirror.com/remotion/-/alternate-remotion.bin"
        )
    elif changed_field == "asset":
        catalog[0]["assets"][0]["sha256"] = "c" * 64
    elif changed_field == "license":
        catalog[0]["assets"][0]["license"] = "Apache-2.0"
    else:
        catalog[0]["verified_entrypoint"] = "bin/remotion-alt"
        catalog[0]["assets"][0]["managed_target"] = "bin/remotion-alt"
    _seal_definition(catalog[0])
    assert catalog[0]["definition_sha256"] != old_definition_sha
    monkeypatch.setattr(runtime_prepare, "_download_asset", lambda *_a: pytest.fail("download called"))
    result = prepare_optional_capabilities(data_root, catalog, [old_decision])
    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "STALE_DECISION"
    assert not data_root.exists()


@pytest.mark.parametrize(
    "mutation,reason",
    [
        (lambda catalog: catalog[0].update(extra="x"), "INVALID_DEFINITION"),
        (lambda catalog: catalog[0].update(capability="python"), "INVALID_CAPABILITY"),
        (lambda catalog: catalog[0]["assets"][0].update(managed_target="../escape"), "PATH_VIOLATION"),
        (lambda catalog: catalog[0].update(normal_command_name="npm"), "INVALID_DEFINITION"),
        (
            lambda catalog: catalog[0]["approved_mainland_sources"][0].update(
                url="https://registry.npmjs.org/remotion/file"
            ),
            "UNAPPROVED_SOURCE",
        ),
        (lambda catalog: catalog[0]["assets"][0].pop("license"), "INVALID_DEFINITION"),
        (lambda catalog: catalog[0]["assets"][0].update(license="../unknown"), "INVALID_DEFINITION"),
        (lambda catalog: catalog[0].update(user_message="literal text"), "INVALID_DEFINITION"),
    ],
)
def test_invalid_definitions_fail_closed_without_writes(tmp_path: Path, definitions, mutation, reason) -> None:
    catalog, _ = definitions
    mutation(catalog)
    result = prepare_optional_capabilities(tmp_path / "data", catalog)
    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == reason
    assert not (tmp_path / "data").exists()


def test_unknown_decision_fields_fail_closed(tmp_path: Path, definitions) -> None:
    catalog, _ = definitions
    first = prepare_optional_capabilities(tmp_path / "data", catalog)
    decision = _decision(catalog[0], _plans_by_capability(first)["remotion"], "decline")
    decision["extra"] = "x"
    result = prepare_optional_capabilities(tmp_path / "data", catalog, [decision])
    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "INVALID_DECISION"


@pytest.mark.parametrize("failure", ["download", "size", "hash", "redirect", "probe"])
def test_integration_failures_cleanup_owned_temporary_objects(
    tmp_path: Path, definitions, monkeypatch, failure: str
) -> None:
    catalog, payloads = definitions
    data_root = tmp_path / "data"
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    decision = [_decision(catalog[0], plans["remotion"], "approve")]
    url = catalog[0]["approved_mainland_sources"][0]["url"]

    if failure == "probe":
        probe_payload = _payload("remotion", "0.0.0")
        catalog[0]["assets"][0]["size"] = len(probe_payload)
        catalog[0]["assets"][0]["sha256"] = hashlib.sha256(probe_payload).hexdigest()
        payloads[url] = probe_payload
        _seal_definition(catalog[0])
        first = prepare_optional_capabilities(data_root, catalog)
        plans = _plans_by_capability(first)
        decision = [_decision(catalog[0], plans["remotion"], "approve")]

    def transport(source: str, destination: Path, expected_size: int) -> str:
        if failure == "download":
            raise OSError("offline")
        payload = payloads[source]
        if failure == "size":
            payload += b"x"
        if failure == "hash":
            payload = b"x" * len(payload)
        assert expected_size == catalog[0]["assets"][0]["size"]
        destination.write_bytes(payload)
        return "https://registry.npmmirror.com/redirected/file" if failure == "redirect" else source

    monkeypatch.setattr(runtime_prepare, "_download_asset", transport)
    result = prepare_optional_capabilities(data_root, catalog, decision)
    assert result["result"] == "BLOCKED"
    assert not _managed_root(data_root, catalog[0]).exists()
    cache = data_root / "Caches" / "optional-runtime"
    assert not cache.exists() or list(cache.iterdir()) == []


def test_transport_reads_at_most_expected_size_plus_one(
    tmp_path: Path, monkeypatch
) -> None:
    expected_size = 8

    class EndlessResponse:
        def __init__(self) -> None:
            self.bytes_returned = 0

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def geturl(self) -> str:
            return "https://registry.npmmirror.com/remotion/-/asset.bin"

        def read(self, size: int) -> bytes:
            self.bytes_returned += size
            return b"x" * size

    response = EndlessResponse()

    class FakeOpener:
        def open(self, *_args, **_kwargs):
            return response

    monkeypatch.setattr(runtime_prepare.urllib.request, "build_opener", lambda *_a: FakeOpener())
    destination = tmp_path / "asset.bin"
    with pytest.raises(runtime_prepare._ContractError) as failure:
        runtime_prepare._download_asset(
            "https://registry.npmmirror.com/remotion/-/asset.bin",
            destination,
            expected_size,
        )
    assert failure.value.code == "SIZE_MISMATCH"
    assert response.bytes_returned == expected_size + 1
    assert destination.stat().st_size <= expected_size


def test_foreign_target_is_preserved(tmp_path: Path, definitions, monkeypatch) -> None:
    catalog, _ = definitions
    data_root = tmp_path / "data"
    target = _managed_root(data_root, catalog[0])
    target.mkdir(parents=True)
    foreign = target / "foreign.txt"
    foreign.write_text("keep", encoding="utf-8")
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    decision = [_decision(catalog[0], plans["remotion"], "approve")]
    monkeypatch.setattr(runtime_prepare, "_download_asset", lambda *_a: pytest.fail("download called"))
    result = prepare_optional_capabilities(data_root, catalog, decision)
    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "FOREIGN_TARGET", result
    assert foreign.read_text(encoding="utf-8") == "keep"


def test_extra_file_makes_otherwise_valid_managed_target_foreign(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, payloads = definitions
    data_root = tmp_path / "data"
    target = _managed_root(data_root, catalog[0])
    url = catalog[0]["approved_mainland_sources"][0]["url"]
    _write_capability(target, catalog[0], payloads[url])
    foreign = target / "foreign.txt"
    foreign.write_text("keep", encoding="utf-8")
    monkeypatch.setattr(runtime_prepare, "_probe", lambda *_a: pytest.fail("probe executed"))
    first = prepare_optional_capabilities(data_root, catalog)
    assert first["capabilities"][0]["status"] == "INCOMPATIBLE"
    plans = _plans_by_capability(first)
    decision = [_decision(catalog[0], plans["remotion"], "approve")]
    monkeypatch.setattr(runtime_prepare, "_download_asset", lambda *_a: pytest.fail("download called"))
    result = prepare_optional_capabilities(data_root, catalog, decision)
    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "FOREIGN_TARGET"
    assert foreign.read_text(encoding="utf-8") == "keep"


def test_missing_approved_managed_asset_blocks_probe(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, payloads = definitions
    support = b"approved-support-asset"
    support_filename = "remotion-support.bin"
    support_url = f"https://registry.npmmirror.com/remotion/-/{support_filename}"
    catalog[0]["approved_mainland_sources"].append(
        {"filename": support_filename, "url": support_url}
    )
    catalog[0]["assets"].append(
        {
            "filename": support_filename,
            "size": len(support),
            "sha256": hashlib.sha256(support).hexdigest(),
            "license": "MIT",
            "managed_target": "lib/support.bin",
        }
    )
    _seal_definition(catalog[0])
    target = _managed_root(tmp_path / "data", catalog[0])
    entry_url = catalog[0]["approved_mainland_sources"][0]["url"]
    _write_capability(target, catalog[0], payloads[entry_url])
    monkeypatch.setattr(runtime_prepare, "_probe", lambda *_a: pytest.fail("probe executed"))
    result = prepare_optional_capabilities(tmp_path / "data", catalog)
    remotion = result["capabilities"][0]
    assert remotion["status"] == "INCOMPATIBLE"
    support_evidence = next(
        item for item in remotion["candidates"][0]["asset_evidence"]
        if item["managed_target"] == "lib/support.bin"
    )
    assert support_evidence["reason"] == "MISSING_OR_UNSAFE_FILE"


@pytest.mark.parametrize(
    "staging_mutation",
    ["missing_asset", "extra_file", "extra_directory", "unsafe_directory"],
)
def test_invalid_staging_closure_blocks_before_probe_and_cleans_owned_objects(
    tmp_path: Path, definitions, monkeypatch, staging_mutation: str
) -> None:
    catalog, payloads = definitions
    data_root = tmp_path / "data"
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    decisions = [
        _decision(catalog[0], plans["remotion"], "approve"),
        _decision(catalog[1], plans["hyperframes"], "defer"),
    ]
    original_is_symlink = Path.is_symlink
    probe_calls: list[Path] = []

    def transport(url: str, destination: Path, expected_size: int) -> str:
        assert len(payloads[url]) == expected_size
        staging = destination.parents[1]
        if staging_mutation != "missing_asset":
            destination.write_bytes(payloads[url])
        if staging_mutation == "extra_file":
            (staging / "extra.bin").write_bytes(b"foreign")
        elif staging_mutation == "extra_directory":
            (staging / "extra").mkdir()
        return url

    def is_symlink(path: Path) -> bool:
        if staging_mutation == "unsafe_directory" and path.name == "bin":
            return True
        return original_is_symlink(path)

    def probe(entrypoint: Path, _version: str):
        probe_calls.append(entrypoint)
        return True, {"reason": "unexpected"}

    monkeypatch.setattr(runtime_prepare, "_download_asset", transport)
    monkeypatch.setattr(Path, "is_symlink", is_symlink)
    monkeypatch.setattr(runtime_prepare, "_probe", probe)
    result = prepare_optional_capabilities(data_root, catalog, decisions)

    assert result["result"] == "BLOCKED"
    assert probe_calls == []
    assert not _managed_root(data_root, catalog[0]).exists()
    cache = data_root / "Caches" / "optional-runtime"
    assert not cache.exists() or list(cache.iterdir()) == []


def test_final_probe_failure_withdraws_own_publication_and_allows_retry(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, payloads = definitions
    data_root = tmp_path / "data"
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    decisions = [
        _decision(catalog[0], plans["remotion"], "approve"),
        _decision(catalog[1], plans["hyperframes"], "defer"),
    ]
    calls: list[str] = []
    _install_transport(monkeypatch, payloads, calls)
    original_probe = runtime_prepare._probe
    probe_calls = 0

    def fail_final_probe(entrypoint: Path, version: str):
        nonlocal probe_calls
        probe_calls += 1
        if probe_calls == 2:
            return False, {"reason": "FINAL_PROBE_FAILED"}
        return original_probe(entrypoint, version)

    monkeypatch.setattr(runtime_prepare, "_probe", fail_final_probe)
    result = prepare_optional_capabilities(data_root, catalog, decisions)

    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "PROBE_FAILED"
    assert probe_calls == 2
    assert not _managed_root(data_root, catalog[0]).exists()
    cache = data_root / "Caches" / "optional-runtime"
    assert not cache.exists() or list(cache.iterdir()) == []

    monkeypatch.setattr(runtime_prepare, "_probe", original_probe)
    retry = prepare_optional_capabilities(data_root, catalog, decisions)
    assert retry["result"] == "INTEGRATED"


def test_final_probe_preserves_target_replaced_by_foreign_object(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, payloads = definitions
    data_root = tmp_path / "data"
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    decisions = [
        _decision(catalog[0], plans["remotion"], "approve"),
        _decision(catalog[1], plans["hyperframes"], "defer"),
    ]
    calls: list[str] = []
    _install_transport(monkeypatch, payloads, calls)
    original_probe = runtime_prepare._probe
    probe_calls = 0
    foreign_payload = b"preserve-concurrent-owner"

    def replace_during_final_probe(entrypoint: Path, version: str):
        nonlocal probe_calls
        probe_calls += 1
        if probe_calls == 2:
            target = entrypoint.parents[1]
            shutil.rmtree(target)
            target.mkdir(parents=True)
            (target / "foreign.txt").write_bytes(foreign_payload)
            return False, {"reason": "FINAL_PROBE_FAILED"}
        return original_probe(entrypoint, version)

    monkeypatch.setattr(runtime_prepare, "_probe", replace_during_final_probe)
    result = prepare_optional_capabilities(data_root, catalog, decisions)

    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "FOREIGN_TARGET"
    target = _managed_root(data_root, catalog[0])
    assert (target / "foreign.txt").read_bytes() == foreign_payload
    cache = data_root / "Caches" / "optional-runtime"
    assert not cache.exists() or list(cache.iterdir()) == []


def test_public_transport_overflow_blocks_and_cleans_owned_objects(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, _ = definitions
    data_root = tmp_path / "data"
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    decision = [_decision(catalog[0], plans["remotion"], "approve")]

    def overflow_transport(url: str, destination: Path, expected_size: int) -> str:
        destination.write_bytes(b"x" * (expected_size + 1))
        return url

    monkeypatch.setattr(runtime_prepare, "_download_asset", overflow_transport)
    result = prepare_optional_capabilities(data_root, catalog, decision)

    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "SIZE_MISMATCH"
    assert not _managed_root(data_root, catalog[0]).exists()
    cache = data_root / "Caches" / "optional-runtime"
    assert not cache.exists() or list(cache.iterdir()) == []


def test_enospc_blocks_without_half_product_or_preexisting_directory_loss(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, _ = definitions
    data_root = tmp_path / "data"
    cache = data_root / "Caches" / "optional-runtime"
    cache.mkdir(parents=True)
    foreign = data_root / "foreign.txt"
    foreign.write_text("keep", encoding="utf-8")
    snapshots = {path: (path.stat().st_dev, path.stat().st_ino) for path in (data_root, cache)}
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    decision = [_decision(catalog[0], plans["remotion"], "approve")]

    def no_space(_url: str, destination: Path, _expected_size: int) -> str:
        destination.write_bytes(b"partial")
        raise OSError(errno.ENOSPC, "simulated full volume")

    monkeypatch.setattr(runtime_prepare, "_download_asset", no_space)
    result = prepare_optional_capabilities(data_root, catalog, decision)

    assert result["result"] == "BLOCKED"
    assert not _managed_root(data_root, catalog[0]).exists()
    assert foreign.read_text(encoding="utf-8") == "keep"
    assert {path: (path.stat().st_dev, path.stat().st_ino) for path in (data_root, cache)} == snapshots
    assert list(cache.iterdir()) == []


def test_directory_permission_error_preserves_preexisting_objects(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, _ = definitions
    data_root = tmp_path / "data"
    caches = data_root / "Caches"
    caches.mkdir(parents=True)
    foreign = data_root / "foreign.txt"
    foreign.write_text("keep", encoding="utf-8")
    snapshots = {path: (path.stat().st_dev, path.stat().st_ino) for path in (data_root, caches)}
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    decision = [_decision(catalog[0], plans["remotion"], "approve")]
    original_mkdir = Path.mkdir

    def deny_cache_root(path: Path, *args, **kwargs):
        if path == data_root / "Caches" / "optional-runtime":
            raise PermissionError(errno.EACCES, "simulated permission denial")
        return original_mkdir(path, *args, **kwargs)

    monkeypatch.setattr(Path, "mkdir", deny_cache_root)
    monkeypatch.setattr(
        runtime_prepare,
        "_download_asset",
        lambda *_args: pytest.fail("transport called after mkdir failure"),
    )
    result = prepare_optional_capabilities(data_root, catalog, decision)

    assert result["result"] == "BLOCKED"
    assert foreign.read_text(encoding="utf-8") == "keep"
    assert caches.is_dir()
    assert {path: (path.stat().st_dev, path.stat().st_ino) for path in (data_root, caches)} == snapshots
    assert not (caches / "optional-runtime").exists()
    assert not _managed_root(data_root, catalog[0]).exists()


def test_publish_failure_cleans_staging_and_does_not_publish(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, payloads = definitions
    data_root = tmp_path / "data"
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    decision = [_decision(catalog[0], plans["remotion"], "approve")]
    calls: list[str] = []
    _install_transport(monkeypatch, payloads, calls)
    monkeypatch.setattr(runtime_prepare.os, "replace", lambda *_a: (_ for _ in ()).throw(OSError("denied")))
    result = prepare_optional_capabilities(data_root, catalog, decision)
    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "PUBLISH_FAILED"
    assert not _managed_root(data_root, catalog[0]).exists()
    cache = data_root / "Caches" / "optional-runtime"
    assert not cache.exists() or list(cache.iterdir()) == []


def test_failure_preserves_preexisting_empty_directory_identity_and_mtime(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, payloads = definitions
    data_root = tmp_path / "data"
    preexisting = [
        data_root,
        data_root / "Runtime",
        data_root / "Runtime" / "Composition",
        data_root / "Caches",
        data_root / "Caches" / "optional-runtime",
    ]
    for path in preexisting:
        path.mkdir(exist_ok=True)
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    decision = [_decision(catalog[0], plans["remotion"], "approve")]
    snapshots = {
        path: (path.stat().st_dev, path.stat().st_ino, path.stat().st_mtime_ns)
        for path in preexisting
    }
    calls: list[str] = []
    _install_transport(monkeypatch, payloads, calls)
    monkeypatch.setattr(
        runtime_prepare.os,
        "replace",
        lambda *_a: (_ for _ in ()).throw(OSError("denied")),
    )
    result = prepare_optional_capabilities(data_root, catalog, decision)
    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "PUBLISH_FAILED"
    assert all(path.is_dir() for path in preexisting)
    assert {
        path: (path.stat().st_dev, path.stat().st_ino, path.stat().st_mtime_ns)
        for path in preexisting
    } == snapshots
    assert list((data_root / "Caches" / "optional-runtime").iterdir()) == []


def test_owned_directory_cleanup_does_not_remove_a_replacement(tmp_path: Path) -> None:
    path = tmp_path / "owned-once"
    path.mkdir()
    original = path.stat()
    path.rmdir()
    path.mkdir()
    replacement = path.stat()
    if (replacement.st_dev, replacement.st_ino) == (original.st_dev, original.st_ino):
        pytest.skip("filesystem immediately reused the same directory identity")
    runtime_prepare._cleanup_owned_empty_directories(
        [(path, original.st_dev, original.st_ino)]
    )
    assert path.is_dir()


def test_managed_path_link_escape_is_rejected_without_following_it(
    tmp_path: Path, definitions, monkeypatch
) -> None:
    catalog, _ = definitions
    data_root = tmp_path / "data"
    outside = tmp_path / "outside"
    outside.mkdir()
    original_resolve = Path.resolve

    def adversarial_resolve(path: Path, strict: bool = False) -> Path:
        if "Runtime" in path.parts:
            return outside / "escaped"
        return original_resolve(path, strict=strict)

    monkeypatch.setattr(Path, "resolve", adversarial_resolve)
    result = prepare_optional_capabilities(data_root, catalog)
    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "PATH_VIOLATION"
    assert list(outside.iterdir()) == []


def test_concurrent_approval_publishes_no_half_product(tmp_path: Path, definitions, monkeypatch) -> None:
    catalog, payloads = definitions
    data_root = tmp_path / "data"
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    decisions = [
        _decision(catalog[0], plans["remotion"], "approve"),
        _decision(catalog[1], plans["hyperframes"], "defer"),
    ]
    calls: list[str] = []
    call_lock = threading.Lock()

    def transport(url: str, destination: Path, expected_size: int) -> str:
        with call_lock:
            calls.append(url)
        time.sleep(0.1)
        assert len(payloads[url]) == expected_size
        destination.write_bytes(payloads[url])
        return url

    monkeypatch.setattr(runtime_prepare, "_download_asset", transport)
    results: list[dict] = []
    threads = [
        threading.Thread(
            target=lambda: results.append(prepare_optional_capabilities(data_root, catalog, decisions))
        )
        for _ in range(2)
    ]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=10)
    assert all(not thread.is_alive() for thread in threads)
    assert [result["result"] for result in results] == ["INTEGRATED", "INTEGRATED"], results
    assert calls == [catalog[0]["approved_mainland_sources"][0]["url"]]
    final = prepare_optional_capabilities(data_root, catalog)
    assert final["capabilities"][0]["status"] == "PRESENT"
    cache = data_root / "Caches" / "optional-runtime"
    assert not cache.exists() or list(cache.iterdir()) == []


def test_stage2_sources_and_toolchain_paths_are_untouched(tmp_path: Path, definitions, monkeypatch) -> None:
    catalog, payloads = definitions
    data_root = tmp_path / "data"
    sentinels = {
        data_root / "Runtime" / "Python" / "keep": b"python",
        data_root / "Runtime" / "FFmpeg" / "keep": b"ffmpeg",
        data_root / "Runtime" / "Node" / "keep": b"node",
        data_root / "PackageRoot" / "keep": b"package",
        data_root / "Registrations" / "keep": b"registration",
    }
    for path, payload in sentinels.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
    first = prepare_optional_capabilities(data_root, catalog)
    plans = _plans_by_capability(first)
    decisions = [
        _decision(catalog[0], plans["remotion"], "approve"),
        _decision(catalog[1], plans["hyperframes"], "defer"),
    ]
    calls: list[str] = []
    _install_transport(monkeypatch, payloads, calls)
    result = prepare_optional_capabilities(data_root, catalog, decisions)
    assert result["result"] == "INTEGRATED"
    assert {path: path.read_bytes() for path in sentinels} == sentinels


def _package_definition_fixture(tmp_path: Path) -> tuple[Path, dict]:
    package_root = tmp_path / "PackageRoot"
    project = package_root / "remotion-composer"
    project.mkdir(parents=True)
    manifest = {"name": "openmontage-remotion-composer", "version": "1.0.0", "dependencies": {"remotion": "4.0.484"}}
    lock = {"name": manifest["name"], "version": manifest["version"], "lockfileVersion": 3, "packages": {"": {"dependencies": manifest["dependencies"]}}}
    manifest_path = project / "package.json"
    lock_path = project / "package-lock.json"
    manifest_path.write_text(json.dumps(manifest, separators=(",", ":")), encoding="utf-8")
    lock_path.write_text(json.dumps(lock, separators=(",", ":")), encoding="utf-8")
    (project / "src").mkdir()
    (project / "src" / "index.tsx").write_text("export {}\n", encoding="utf-8")
    definition = {
        "capability": "remotion",
        "version": "4.0.484",
        "license": "AGPL-3.0-only",
        "runtime_license": "SEE LICENSE IN LICENSE.md",
        "source": "https://www.npmjs.com/package/remotion/v/4.0.484",
        "registry": "https://registry.npmmirror.com",
        "install_scope": "system",
        "install_target": "windows_default_for_scope",
        "package": {
            "name": manifest["name"],
            "version": manifest["version"],
            "manifest": "remotion-composer/package.json",
            "manifest_sha256": hashlib.sha256(manifest_path.read_bytes()).hexdigest(),
            "lockfile": "remotion-composer/package-lock.json",
            "lockfile_sha256": hashlib.sha256(lock_path.read_bytes()).hexdigest(),
        },
        "project_root": "remotion-composer",
        "verified_entrypoint": "node_modules/.bin/remotion.cmd",
        "command": ["npx", "remotion", "render"],
        "definition_sha256": "0" * 64,
    }
    body = {key: value for key, value in definition.items() if key != "definition_sha256"}
    definition["definition_sha256"] = hashlib.sha256(json.dumps(body, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()
    return package_root, definition


def test_package_remotion_plan_is_mirror_only_and_does_not_download(tmp_path: Path, monkeypatch) -> None:
    package_root, definition = _package_definition_fixture(tmp_path)
    data_root = tmp_path / "data"
    monkeypatch.setenv("ProgramFiles", str(tmp_path / "Windows" / "Program Files"))
    monkeypatch.setenv("LocalAppData", str(tmp_path / "Windows" / "Users" / "Local"))

    result = prepare_optional_capabilities(data_root, [definition], package_root=package_root)

    assert result["result"] == "CONSENT_REQUIRED"
    assert result["capabilities"] == [
        {"capability": "remotion", "status": "MISSING"},
        {"capability": "hyperframes", "status": "NOT_INTEGRATED", "reason": "UNIMPLEMENTED"},
    ]
    plan = result["plans"][0]
    assert plan["registry"] == "https://registry.npmmirror.com"
    assert plan["download_size_bytes"] is None
    assert plan["download_size"] == "unknown"
    assert plan["install_command"][1:2] == ["ci"]
    assert "--registry=https://registry.npmmirror.com" in plan["install_command"]
    assert {item["install_scope"] for item in plan["install_scopes"]} == {"system", "current-user"}
    assert not data_root.exists()


def test_package_remotion_fake_npm_ci_publishes_and_rediscoveries(tmp_path: Path, monkeypatch) -> None:
    package_root, definition = _package_definition_fixture(tmp_path)
    data_root = tmp_path / "data"
    monkeypatch.setenv("ProgramFiles", str(tmp_path / "Windows" / "Program Files"))
    monkeypatch.setenv("LocalAppData", str(tmp_path / "Windows" / "Users" / "Local"))
    probe_calls: list[Path] = []
    npm_calls: list[tuple[list[str], Path, str]] = []

    def fake_probe(entrypoint: Path, version: str) -> tuple[bool, dict]:
        probe_calls.append(entrypoint)
        return True, {"reason": "COMPATIBLE", "entrypoint": str(entrypoint.resolve()), "exit_code": 0, "version_output": f"remotion {version}"}

    def fake_npm(command, cwd: Path, environment) -> None:
        npm_calls.append((list(command), cwd, environment["NPM_CONFIG_REGISTRY"]))
        assert environment["npm_config_registry"] == "https://registry.npmmirror.com"
        entrypoint = cwd / "node_modules" / ".bin" / "remotion.cmd"
        entrypoint.parent.mkdir(parents=True)
        entrypoint.write_text("@echo off\necho remotion 4.0.484\n", encoding="utf-8")

    monkeypatch.setattr(runtime_prepare, "_probe", fake_probe)
    monkeypatch.setattr(runtime_prepare, "_npm_executor", fake_npm)
    first = prepare_optional_capabilities(data_root, [definition], package_root=package_root)
    plan = first["plans"][0]
    decision = {"decision": "approve", "capability": "remotion", "definition_sha256": definition["definition_sha256"], "plan_sha256": plan["plan_sha256"], "install_scope": "system"}

    result = prepare_optional_capabilities(data_root, [definition], [decision], package_root=package_root)

    assert result["result"] == "INTEGRATED"
    runtime = result["managed_remotion_runtime"]
    assert runtime["status"] == "PRESENT"
    assert runtime["source"] == "managed"
    assert Path(runtime["runtime_root"]).is_absolute()
    assert Path(runtime["verified_entrypoint"]).is_relative_to(Path(runtime["runtime_root"]))
    assert runtime["version"] == "4.0.484"
    assert runtime["install_scope"] == "system"
    assert npm_calls and npm_calls[0][0][1] == "ci"
    assert npm_calls[0][2] == "https://registry.npmmirror.com"
    assert len(probe_calls) >= 2
    record = data_root / "State" / "OptionalRuntime" / f"remotion-{definition['definition_sha256']}.json"
    assert record.is_file()
    rediscovered = prepare_optional_capabilities(data_root, [definition], package_root=package_root)
    assert rediscovered["result"] == "DETECTION_REPORT"
    assert rediscovered["managed_remotion_runtime"]["runtime_root"] == runtime["runtime_root"]
    assert rediscovered["capabilities"][1]["status"] == "NOT_INTEGRATED"


def test_package_remotion_invalid_decision_does_not_call_npm_or_create_target(
    tmp_path: Path, monkeypatch
) -> None:
    package_root, definition = _package_definition_fixture(tmp_path)
    data_root = tmp_path / "data"
    monkeypatch.setenv("ProgramFiles", str(tmp_path / "Windows" / "Program Files"))
    monkeypatch.setenv("LocalAppData", str(tmp_path / "Windows" / "Users" / "Local"))
    npm_calls: list[tuple[list[str], Path]] = []

    def fake_npm(command, cwd: Path, environment) -> None:
        npm_calls.append((list(command), cwd))

    monkeypatch.setattr(runtime_prepare, "_npm_executor", fake_npm)
    first = prepare_optional_capabilities(data_root, [definition], package_root=package_root)
    plan = first["plans"][0]
    decision = {
        "decision": "approve-without-consent",
        "capability": "remotion",
        "definition_sha256": definition["definition_sha256"],
        "plan_sha256": plan["plan_sha256"],
        "install_scope": "system",
    }

    result = prepare_optional_capabilities(
        data_root, [definition], [decision], package_root=package_root
    )

    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "INVALID_DECISION"
    assert npm_calls == []
    target = Path(plan["install_scopes"][0]["runtime_root"])
    assert not target.exists()


def test_package_remotion_record_write_failure_withdraws_target_and_is_retryable(
    tmp_path: Path, monkeypatch
) -> None:
    package_root, definition = _package_definition_fixture(tmp_path)
    data_root = tmp_path / "data"
    monkeypatch.setenv("ProgramFiles", str(tmp_path / "Windows" / "Program Files"))
    monkeypatch.setenv("LocalAppData", str(tmp_path / "Windows" / "Users" / "Local"))

    def fake_probe(entrypoint: Path, version: str) -> tuple[bool, dict]:
        return True, {
            "reason": "COMPATIBLE",
            "entrypoint": str(entrypoint.resolve()),
            "exit_code": 0,
            "version_output": f"remotion {version}",
        }

    def fake_npm(command, cwd: Path, environment) -> None:
        entrypoint = cwd / "node_modules" / ".bin" / "remotion.cmd"
        entrypoint.parent.mkdir(parents=True)
        entrypoint.write_text("@echo off\necho remotion 4.0.484\n", encoding="utf-8")

    def fail_record(data_root_arg, definition_arg, evidence_arg) -> None:
        raise runtime_prepare._ContractError("INSTALL_FAILED", "forced record failure")

    monkeypatch.setattr(runtime_prepare, "_probe", fake_probe)
    monkeypatch.setattr(runtime_prepare, "_npm_executor", fake_npm)
    monkeypatch.setattr(runtime_prepare, "_write_runtime_record", fail_record)
    first = prepare_optional_capabilities(data_root, [definition], package_root=package_root)
    plan = first["plans"][0]
    decision = {
        "decision": "approve",
        "capability": "remotion",
        "definition_sha256": definition["definition_sha256"],
        "plan_sha256": plan["plan_sha256"],
        "install_scope": "system",
    }

    result = prepare_optional_capabilities(
        data_root, [definition], [decision], package_root=package_root
    )

    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "INSTALL_FAILED"
    target = Path(plan["install_scopes"][0]["runtime_root"])
    assert not target.exists()
    record = data_root / "State" / "OptionalRuntime" / f"remotion-{definition['definition_sha256']}.json"
    assert not record.exists()
    retry = prepare_optional_capabilities(data_root, [definition], package_root=package_root)
    assert retry["result"] == "CONSENT_REQUIRED"
    assert retry["plans"][0]["plan_sha256"] == plan["plan_sha256"]
