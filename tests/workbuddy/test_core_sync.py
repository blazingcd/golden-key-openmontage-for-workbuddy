from __future__ import annotations

import hashlib
import json
import zipfile
from pathlib import Path

import pytest

from scripts.core_sync import sync_workbuddy_core


CONSUMER_REMOVE_PATHS = [
    "lib/agent_host_authority.py",
    "lib/model_driven_agent_host.py",
    "lib/openai_compatible_transport.py",
    "tests/contracts/test_agent_host_authority.py",
    "tests/contracts/test_model_driven_agent_host.py",
    "tests/contracts/test_openai_compatible_transport.py",
]


def _sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _write_bundle(
    root: Path,
    files: dict[str, bytes],
    *,
    extra_members: dict[str, bytes] | None = None,
    lock_updates: dict | None = None,
    scope_updates: dict | None = None,
    declared_hash_overrides: dict[str, str] | None = None,
    declared_mode_overrides: dict[str, str] | None = None,
    omitted_members: set[str] | None = None,
) -> tuple[Path, Path, str]:
    entries = []
    for source_path, data in sorted(files.items()):
        entries.append(
            {
                "apply_mode": "replace",
                "classification": "workbuddy_callable",
                "path": f"workbuddy-core/{source_path}",
                "sha256": (declared_hash_overrides or {}).get(source_path, _sha256(data)),
                "size": len(data),
                "source_mode": (declared_mode_overrides or {}).get(source_path, "100644"),
                "source_path": source_path,
            }
        )
    canonical = json.dumps(
        entries, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    lock = {
        "schema_version": 2,
        "contract_id": "golden-key-workbuddy-callable-core-v1",
        "source_ref": "golden-key-v0.3.21",
        "source_commit": "757ea3822e5f2eef7f341389983119021e827c8d",
        "upstream_base": "4eab34c5cfcccaa4f1970554928feccce73ee930",
        "authority": {
            "consumer": "workbuddy",
            "consumer_direct_official_sync_allowed": False,
            "invocation_model": "direct_agent",
            "nested_agent_host_allowed": False,
            "official_openmontage_role": "reviewed_upstream_baseline_only",
            "source": "golden-key-core",
        },
        "managed_scope": {
            "destination_root": "workbuddy-core",
            "managed_paths": ["AGENT_GUIDE.md"],
            "managed_prefixes": ["lib/", "tests/contracts/"],
            "required_paths": ["AGENT_GUIDE.md", "lib/checkpoint.py"],
            "forbidden_paths": [*CONSUMER_REMOVE_PATHS, "requirements.txt", "setup.py"],
            "consumer_remove_paths": CONSUMER_REMOVE_PATHS,
        },
        "files": entries,
        "bundle_sha256": _sha256(canonical),
    }
    if lock_updates:
        lock.update(lock_updates)
    if scope_updates:
        lock["managed_scope"].update(scope_updates)
    lock_bytes = (json.dumps(lock, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    lock_path = root / "GOLDEN_KEY_WORKBUDDY_CORE.lock.json"
    lock_path.write_bytes(lock_bytes)
    zip_path = root / "golden-key-v0.3.21-workbuddy-core.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for source_path, data in sorted(files.items()):
            if source_path in (omitted_members or set()):
                continue
            info = zipfile.ZipInfo(f"workbuddy-core/{source_path}")
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
        for member, data in sorted((extra_members or {}).items()):
            info = zipfile.ZipInfo(member)
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
        archive.writestr("GOLDEN_KEY_WORKBUDDY_CORE.lock.json", lock_bytes)
    return zip_path, lock_path, _sha256(zip_path.read_bytes())


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_sync_mirrors_managed_scope_and_preserves_consumer_files(tmp_path: Path):
    bundle_root = tmp_path / "bundle"
    bundle_root.mkdir()
    zip_path, lock_path, zip_sha256 = _write_bundle(
        bundle_root,
        {
            "AGENT_GUIDE.md": b"new guide\n",
            "lib/checkpoint.py": b"new checkpoint\n",
            "tests/contracts/test_public_contract.py": b"def test_public(): pass\n",
        },
    )
    destination = tmp_path / "consumer"
    _write(destination / "AGENT_GUIDE.md", "old guide\n")
    _write(destination / "lib/checkpoint.py", "old checkpoint\n")
    _write(destination / "lib/stale_managed.py", "stale\n")
    for relative in CONSUMER_REMOVE_PATHS:
        _write(destination / relative, "must be removed\n")
    _write(destination / "requirements.txt", "consumer requirements\n")
    _write(destination / "setup.py", "consumer setup\n")
    _write(destination / "README.md", "consumer readme\n")
    _write(destination / "docs/workbuddy/OWNED.md", "consumer docs\n")

    report = sync_workbuddy_core.synchronize(
        zip_path=zip_path,
        lock_path=lock_path,
        destination_root=destination,
        expected_zip_sha256=zip_sha256,
        expected_contract_id="golden-key-workbuddy-callable-core-v1",
        expected_source_ref="golden-key-v0.3.21",
        expected_source_commit="757ea3822e5f2eef7f341389983119021e827c8d",
    )

    assert (destination / "AGENT_GUIDE.md").read_text(encoding="utf-8") == "new guide\n"
    assert (destination / "lib/checkpoint.py").read_text(encoding="utf-8") == "new checkpoint\n"
    assert not (destination / "lib/stale_managed.py").exists()
    assert all(not (destination / relative).exists() for relative in CONSUMER_REMOVE_PATHS)
    assert (destination / "requirements.txt").read_text(encoding="utf-8") == "consumer requirements\n"
    assert (destination / "setup.py").read_text(encoding="utf-8") == "consumer setup\n"
    assert (destination / "README.md").read_text(encoding="utf-8") == "consumer readme\n"
    assert (destination / "docs/workbuddy/OWNED.md").read_text(encoding="utf-8") == "consumer docs\n"
    assert report["verified_file_count"] == 3
    assert report["consumer_remove_paths"] == CONSUMER_REMOVE_PATHS
    assert report["removed_existing_paths"] == CONSUMER_REMOVE_PATHS


def test_sync_rejects_any_change_to_the_six_consumer_remove_paths(tmp_path: Path):
    zip_path, lock_path, zip_sha256 = _write_bundle(
        tmp_path,
        {
            "AGENT_GUIDE.md": b"guide\n",
            "lib/checkpoint.py": b"checkpoint\n",
        },
        scope_updates={"consumer_remove_paths": CONSUMER_REMOVE_PATHS[:-1]},
    )

    with pytest.raises(sync_workbuddy_core.SyncContractError, match="consumer_remove_paths"):
        sync_workbuddy_core.verify_bundle(
            zip_path=zip_path,
            lock_path=lock_path,
            expected_zip_sha256=zip_sha256,
            expected_contract_id="golden-key-workbuddy-callable-core-v1",
            expected_source_ref="golden-key-v0.3.21",
            expected_source_commit="757ea3822e5f2eef7f341389983119021e827c8d",
        )


@pytest.mark.parametrize(
    ("case", "bundle_options", "message"),
    [
        (
            "forbidden",
            {"files": {"requirements.txt": b"must stay consumer-owned\n"}},
            "forbidden path",
        ),
        (
            "hash",
            {"declared_hash_overrides": {"lib/checkpoint.py": "0" * 64}},
            "file hash mismatch",
        ),
        (
            "missing",
            {"omitted_members": {"lib/checkpoint.py"}},
            "bundle inventory mismatch",
        ),
        (
            "extra",
            {"extra_members": {"workbuddy-core/lib/extra.py": b"extra\n"}},
            "bundle inventory mismatch",
        ),
        (
            "mode",
            {"declared_mode_overrides": {"lib/checkpoint.py": "100755"}},
            "file mode mismatch",
        ),
        (
            "digest",
            {"lock_updates": {"bundle_sha256": "0" * 64}},
            "bundle inventory digest mismatch",
        ),
    ],
)
def test_sync_rejects_tampered_or_invalid_bundle(
    tmp_path: Path, case: str, bundle_options: dict, message: str
):
    del case
    files = {
        "AGENT_GUIDE.md": b"guide\n",
        "lib/checkpoint.py": b"checkpoint\n",
    }
    files.update(bundle_options.pop("files", {}))
    zip_path, lock_path, zip_sha256 = _write_bundle(
        tmp_path, files, **bundle_options
    )

    with pytest.raises(sync_workbuddy_core.SyncContractError, match=message):
        sync_workbuddy_core.verify_bundle(
            zip_path=zip_path,
            lock_path=lock_path,
            expected_zip_sha256=zip_sha256,
            expected_contract_id="golden-key-workbuddy-callable-core-v1",
            expected_source_ref="golden-key-v0.3.21",
            expected_source_commit="757ea3822e5f2eef7f341389983119021e827c8d",
        )


def test_sync_rejects_external_zip_sha_mismatch(tmp_path: Path):
    zip_path, lock_path, _ = _write_bundle(
        tmp_path,
        {
            "AGENT_GUIDE.md": b"guide\n",
            "lib/checkpoint.py": b"checkpoint\n",
        },
    )

    with pytest.raises(sync_workbuddy_core.SyncContractError, match="ZIP SHA-256 mismatch"):
        sync_workbuddy_core.verify_bundle(
            zip_path=zip_path,
            lock_path=lock_path,
            expected_zip_sha256="0" * 64,
            expected_contract_id="golden-key-workbuddy-callable-core-v1",
            expected_source_ref="golden-key-v0.3.21",
            expected_source_commit="757ea3822e5f2eef7f341389983119021e827c8d",
        )


def test_repeated_sync_is_idempotent(tmp_path: Path):
    zip_path, lock_path, zip_sha256 = _write_bundle(
        tmp_path,
        {
            "AGENT_GUIDE.md": b"guide\n",
            "lib/checkpoint.py": b"checkpoint\n",
        },
    )
    destination = tmp_path / "consumer"
    _write(destination / "requirements.txt", "consumer requirements\n")
    _write(destination / "setup.py", "consumer setup\n")
    arguments = {
        "zip_path": zip_path,
        "lock_path": lock_path,
        "destination_root": destination,
        "expected_zip_sha256": zip_sha256,
        "expected_contract_id": "golden-key-workbuddy-callable-core-v1",
        "expected_source_ref": "golden-key-v0.3.21",
        "expected_source_commit": "757ea3822e5f2eef7f341389983119021e827c8d",
    }

    first = sync_workbuddy_core.synchronize(**arguments)
    second = sync_workbuddy_core.synchronize(**arguments)

    assert first["changed_file_count"] == 2
    assert second["changed_file_count"] == 0
    assert second["deleted_file_count"] == 0
    assert second["preserved_consumer_paths"] == ["requirements.txt", "setup.py"]


def test_read_only_destination_verification_rejects_drift_without_mutating(tmp_path: Path):
    zip_path, lock_path, zip_sha256 = _write_bundle(
        tmp_path,
        {
            "AGENT_GUIDE.md": b"guide\n",
            "lib/checkpoint.py": b"checkpoint\n",
        },
    )
    bundle = sync_workbuddy_core.verify_bundle(
        zip_path=zip_path,
        lock_path=lock_path,
        expected_zip_sha256=zip_sha256,
        expected_contract_id="golden-key-workbuddy-callable-core-v1",
        expected_source_ref="golden-key-v0.3.21",
        expected_source_commit="757ea3822e5f2eef7f341389983119021e827c8d",
    )
    destination = tmp_path / "consumer"
    sync_workbuddy_core.apply_verified_bundle(bundle, destination)
    _write(destination / "lib/unexpected.py", "drift\n")

    with pytest.raises(sync_workbuddy_core.SyncContractError, match="inventory mismatch"):
        sync_workbuddy_core.verify_destination(bundle, destination)

    assert (destination / "lib/unexpected.py").read_text(encoding="utf-8") == "drift\n"


def test_config_pins_external_lock_bundle_and_upstream_identity(tmp_path: Path):
    zip_path, lock_path, zip_sha256 = _write_bundle(
        tmp_path,
        {
            "AGENT_GUIDE.md": b"guide\n",
            "lib/checkpoint.py": b"checkpoint\n",
        },
    )
    bundle = sync_workbuddy_core.verify_bundle(
        zip_path=zip_path,
        lock_path=lock_path,
        expected_zip_sha256=zip_sha256,
        expected_contract_id="golden-key-workbuddy-callable-core-v1",
        expected_source_ref="golden-key-v0.3.21",
        expected_source_commit="757ea3822e5f2eef7f341389983119021e827c8d",
    )
    config = {
        "golden_key_core_lock_sha256": _sha256(lock_path.read_bytes()),
        "golden_key_core_bundle_sha256": bundle.lock["bundle_sha256"],
        "upstream_base_commit": bundle.lock["upstream_base"],
        "authority": {
            "invocation_model": "direct_agent",
            "nested_agent_host_allowed": False,
            "consumer_direct_official_sync_allowed": False,
            "official_openmontage_role": "reviewed_upstream_baseline_only",
        },
    }

    result = sync_workbuddy_core.validate_configured_bundle(
        bundle=bundle, lock_path=lock_path, config=config
    )
    assert result["configured_identity_match"] is True

    config["golden_key_core_lock_sha256"] = "0" * 64
    with pytest.raises(sync_workbuddy_core.SyncContractError, match="lock SHA-256"):
        sync_workbuddy_core.validate_configured_bundle(
            bundle=bundle, lock_path=lock_path, config=config
        )
