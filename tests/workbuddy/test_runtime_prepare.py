from __future__ import annotations

import copy
import hashlib
import importlib
import os
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


def _definition(capability: str, marker: str, version: str) -> tuple[dict, bytes]:
    payload = _payload(capability, version)
    filename = f"{capability}-{version}.bin"
    return (
        {
            "capability": capability,
            "definition_sha256": marker * 64,
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
        },
        payload,
    )


@pytest.fixture
def definitions() -> tuple[list[dict], dict[str, bytes]]:
    remotion, remotion_payload = _definition("remotion", "a", "4.0.1")
    hyperframes, hyperframes_payload = _definition("hyperframes", "b", "1.3.0")
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
    def transport(url: str, destination: Path) -> str:
        calls.append(url)
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
    result = prepare_optional_capabilities(tmp_path / "data", catalog)
    remotion = result["capabilities"][0]
    assert remotion["status"] == "PRESENT"
    assert remotion["evidence"]["source"] == "explicit"


def test_path_candidate_uses_only_normal_resolution(tmp_path: Path, definitions, monkeypatch) -> None:
    catalog, payloads = definitions
    command = _write_capability(
        tmp_path / "path-candidate",
        catalog[0],
        payloads[catalog[0]["approved_mainland_sources"][0]["url"]],
    )
    catalog[0]["normal_command_name"] = command.name
    monkeypatch.setattr(runtime_prepare.shutil, "which", lambda name: str(command) if name == command.name else None)
    result = prepare_optional_capabilities(tmp_path / "data", catalog)
    assert result["capabilities"][0]["evidence"]["source"] == "PATH"


def test_missing_detection_does_not_probe_or_enumerate(tmp_path: Path, definitions, monkeypatch) -> None:
    catalog, _ = definitions
    catalog[0]["normal_command_name"] = "remotion.cmd" if os.name == "nt" else "remotion"
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
    assert integrated["result"] == "INTEGRATED"
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
        first = prepare_optional_capabilities(data_root, catalog)
        plans = _plans_by_capability(first)
        decision = [_decision(catalog[0], plans["remotion"], "approve")]

    def transport(source: str, destination: Path) -> str:
        if failure == "download":
            raise OSError("offline")
        payload = payloads[source]
        if failure == "size":
            payload += b"x"
        if failure == "hash":
            payload = b"x" * len(payload)
        destination.write_bytes(payload)
        return "https://registry.npmmirror.com/redirected/file" if failure == "redirect" else source

    monkeypatch.setattr(runtime_prepare, "_download_asset", transport)
    result = prepare_optional_capabilities(data_root, catalog, decision)
    assert result["result"] == "BLOCKED"
    assert not _managed_root(data_root, catalog[0]).exists()
    cache = data_root / "Caches" / "optional-runtime"
    assert not cache.exists() or list(cache.iterdir()) == []


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
    assert result["reason_code"] == "FOREIGN_TARGET"
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
    first = prepare_optional_capabilities(data_root, catalog)
    assert first["capabilities"][0]["status"] == "INCOMPATIBLE"
    plans = _plans_by_capability(first)
    decision = [_decision(catalog[0], plans["remotion"], "approve")]
    monkeypatch.setattr(runtime_prepare, "_download_asset", lambda *_a: pytest.fail("download called"))
    result = prepare_optional_capabilities(data_root, catalog, decision)
    assert result["result"] == "BLOCKED"
    assert result["reason_code"] == "FOREIGN_TARGET"
    assert foreign.read_text(encoding="utf-8") == "keep"


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

    def transport(url: str, destination: Path) -> str:
        with call_lock:
            calls.append(url)
        time.sleep(0.1)
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
