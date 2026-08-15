from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import threading
import time
import unicodedata
import zipfile
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType
from typing import Any, Callable

import pytest

from golden_key_openmontage_workbuddy import package_registration as registration
from golden_key_openmontage_workbuddy.package_registration import (
    PackageRegistrationError,
    activate_package,
    locate_active_package,
    recover_active_package,
    register_package,
)


CONTRACT_ID = "golden-key-workbuddy-callable-core-v1"
RELEASE = "golden-key-v-test"
COMMIT = "1" * 40
MANIFEST_AUTHORITY = {
    "invocation_model": "direct_agent",
    "nested_agent_host_allowed": False,
}
LOCK_AUTHORITY = {
    "consumer": "workbuddy",
    "consumer_direct_official_sync_allowed": False,
    "invocation_model": "direct_agent",
    "nested_agent_host_allowed": False,
    "official_openmontage_role": "reviewed_upstream_baseline_only",
    "source": "golden-key-core",
}


def _sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _sha256(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _canonical(value: dict[str, Any]) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
        + b"\n"
    )


def _write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _json_fixture_bytes(value: dict[str, Any]) -> bytes:
    """Encode deliberately invalid JSON-domain values without encoding surrogates."""

    return (
        json.dumps(
            value,
            ensure_ascii=True,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("ascii")
        + b"\n"
    )


def _inventory_entry(path: Path, relative: str, owner: str) -> dict[str, Any]:
    return {
        "path": relative,
        "owner": owner,
        "sha256": _sha256(path),
        "size": path.stat().st_size,
    }


@dataclass
class Candidate:
    base: Path
    data_root: Path
    package_root: Path
    package_python: Path
    manifest_path: Path
    lock_path: Path
    guide_path: Path
    managed_path: Path
    archive: Path
    sidecar: Path

    def manifest(self) -> dict[str, Any]:
        return json.loads(self.manifest_path.read_text(encoding="utf-8"))

    def lock(self) -> dict[str, Any]:
        return json.loads(self.lock_path.read_text(encoding="utf-8"))

    def write_manifest(self, value: dict[str, Any]) -> None:
        _write_json(self.manifest_path, value)

    def write_lock(self, value: dict[str, Any], *, sync_manifest: bool = True) -> None:
        _write_json(self.lock_path, value)
        if sync_manifest:
            manifest = self.manifest()
            entry = next(item for item in manifest["files"] if item["path"] == registration.LOCK_NAME)
            entry["sha256"] = _sha256(self.lock_path)
            entry["size"] = self.lock_path.stat().st_size
            self.write_manifest(manifest)

    def rebuild_archive(self, *, extra: list[tuple[str, bytes]] | None = None) -> None:
        if self.archive.exists():
            self.archive.unlink()
        with zipfile.ZipFile(self.archive, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
            prefix = "GoldenKeyOpenMontageForWorkBuddy"
            bundle.writestr(f"{prefix}/{registration.MANIFEST_NAME}", self.manifest_path.read_bytes())
            bundle.writestr(f"{prefix}/{registration.LOCK_NAME}", self.lock_path.read_bytes())
            bundle.writestr(f"{prefix}/{registration.GUIDE_NAME}", self.guide_path.read_bytes())
            for name, raw in extra or []:
                bundle.writestr(name, raw)
        self.sidecar.write_text(f"{_sha256(self.archive)} *{self.archive.name}\n", encoding="utf-8")

    def register(self) -> dict[str, Any]:
        return dict(
            register_package(
                self.data_root,
                self.archive,
                self.sidecar,
                self.package_root,
                self.package_python,
            )
        )


def _make_candidate(
    base: Path,
    *,
    data_root: Path | None = None,
    python_payload: bytes = b"private-python",
) -> Candidate:
    base.mkdir(parents=True, exist_ok=True)
    data = data_root or (base / "data")
    data.mkdir(parents=True, exist_ok=True)
    root = base / "package"
    root.mkdir()
    guide = root / registration.GUIDE_NAME
    guide.write_text("# Fixture Guide\n", encoding="utf-8")
    managed = root / "pipeline_defs" / "fixture.yaml"
    managed.parent.mkdir(parents=True)
    managed.write_text("name: fixture\n", encoding="utf-8")
    package_python = root / "bootstrap" / "python" / "python.exe"
    package_python.parent.mkdir(parents=True)
    package_python.write_bytes(python_payload)

    lock_files = []
    for relative, path in (
        (registration.GUIDE_NAME, guide),
        ("pipeline_defs/fixture.yaml", managed),
    ):
        lock_files.append(
            {
                "path": f"workbuddy-core/{relative}",
                "source_path": relative,
                "sha256": _sha256(path),
                "size": path.stat().st_size,
                "source_mode": "100644",
                "apply_mode": "replace",
                "classification": "workbuddy_callable",
            }
        )
    lock = {
        "schema_version": 2,
        "contract_id": CONTRACT_ID,
        "source_ref": RELEASE,
        "source_commit": COMMIT,
        "authority": dict(LOCK_AUTHORITY),
        "files": lock_files,
    }
    lock["bundle_sha256"] = _sha256_bytes(
        json.dumps(
            lock_files,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    )
    lock_path = root / registration.LOCK_NAME
    _write_json(lock_path, lock)

    manifest_files = [
        _inventory_entry(guide, registration.GUIDE_NAME, "managed_core"),
        _inventory_entry(managed, "pipeline_defs/fixture.yaml", "managed_core"),
        _inventory_entry(lock_path, registration.LOCK_NAME, "core_contract"),
        _inventory_entry(
            package_python,
            registration.PYTHON_RELATIVE_PATH,
            "workbuddy_bootstrap_runtime",
        ),
    ]
    manifest = {
        "schema_version": registration.MANIFEST_SCHEMA,
        "distribution": {"channel": "fixture", "format": "portable_zip"},
        "core": {
            "contract_id": CONTRACT_ID,
            "tag": RELEASE,
            "source_commit": COMMIT,
            "file_count": len(lock_files),
            "usage": "fixture",
        },
        "authority": dict(MANIFEST_AUTHORITY),
        "installation": {
            "runtime_roles": {"python": "bundled_private_interpreter"}
        },
        "bootstrap_runtime": {
            "python": {
                "version": "3.13.15",
                "source": "python.org_windows_embeddable_x64",
                "archive_sha256": "2" * 64,
                "system_python_required": False,
            }
        },
        "files": manifest_files,
    }
    manifest_path = root / registration.MANIFEST_NAME
    _write_json(manifest_path, manifest)
    archive = base / "golden-key-fixture.zip"
    sidecar = base / "golden-key-fixture.zip.sha256"
    candidate = Candidate(
        base=base,
        data_root=data,
        package_root=root,
        package_python=package_python,
        manifest_path=manifest_path,
        lock_path=lock_path,
        guide_path=guide,
        managed_path=managed,
        archive=archive,
        sidecar=sidecar,
    )
    candidate.rebuild_archive()
    return candidate


def _registry(candidate: Candidate) -> Path:
    return candidate.data_root / "State" / "PackageRegistration" / "v1"


def _active(candidate: Candidate) -> Path:
    return _registry(candidate) / "active.json"


def _object(candidate: Candidate, digest: str) -> Path:
    return _registry(candidate) / "objects" / f"{digest}.json"


def _pointer(digest: str) -> bytes:
    return _canonical(
        {
            "schema_version": registration.ACTIVE_POINTER_SCHEMA,
            "owner": registration.REGISTRATION_OWNER,
            "registration_sha256": digest,
        }
    )


def _activate_missing(candidate: Candidate, digest: str) -> None:
    assert activate_package(candidate.data_root, "MISSING", digest) == digest


def _snapshot(*roots: Path) -> tuple[tuple[str, str, int, int, str], ...]:
    rows: list[tuple[str, str, int, int, str]] = []
    for root in roots:
        if not root.exists():
            rows.append((str(root), "missing", 0, 0, ""))
            continue
        for path in [root, *sorted(root.rglob("*"))]:
            stat_result = path.stat()
            kind = "dir" if path.is_dir() else "file"
            digest = _sha256(path) if path.is_file() else ""
            rows.append(
                (
                    str(path),
                    kind,
                    stat_result.st_size,
                    stat_result.st_mtime_ns,
                    digest,
                )
            )
    return tuple(rows)


def _expect_code(code: str, action: Callable[[], Any]) -> PackageRegistrationError:
    with pytest.raises(PackageRegistrationError) as captured:
        action()
    assert captured.value.code == code
    return captured.value


def _activation_child(
    data_root: Path, expected: str, target: str, *, timeout_seconds: float = 0.12
) -> subprocess.CompletedProcess[str]:
    child_code = r"""
import sys
from golden_key_openmontage_workbuddy import package_registration as module

module._ACTIVE_LOCK_TIMEOUT_SECONDS = float(sys.argv[4])
module._ACTIVE_LOCK_RETRY_SECONDS = 0.01
try:
    module.activate_package(sys.argv[1], sys.argv[2], sys.argv[3])
except module.PackageRegistrationError as exc:
    print(exc.code)
else:
    print("SUCCESS")
"""
    return subprocess.run(
        [
            sys.executable,
            "-c",
            child_code,
            str(data_root),
            expected,
            target,
            str(timeout_seconds),
        ],
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
    )


def _install_special_json_boundary(
    candidate: Candidate, document: str, special: Any
) -> tuple[Callable[[], Any], str]:
    if document == "manifest":
        manifest = candidate.manifest()
        manifest["distribution"]["strict_json_probe"] = special
        candidate.manifest_path.write_bytes(_json_fixture_bytes(manifest))
        candidate.rebuild_archive()
        return candidate.register, "INPUT_INVALID"

    if document == "lock":
        lock = candidate.lock()
        lock["files"][0]["strict_json_probe"] = special
        if not isinstance(special, str):
            lock["bundle_sha256"] = _sha256_bytes(
                json.dumps(
                    lock["files"],
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode("utf-8")
            )
        candidate.lock_path.write_bytes(_json_fixture_bytes(lock))
        manifest = candidate.manifest()
        lock_entry = next(
            item for item in manifest["files"] if item["path"] == registration.LOCK_NAME
        )
        lock_entry["sha256"] = _sha256(candidate.lock_path)
        lock_entry["size"] = candidate.lock_path.stat().st_size
        candidate.write_manifest(manifest)
        candidate.rebuild_archive()
        return candidate.register, "INPUT_INVALID"

    registered = candidate.register()
    digest = registered["registration_sha256"]
    if document == "registration":
        value = json.loads(_object(candidate, digest).read_text(encoding="utf-8"))
        value["contract_id"] = special
        raw = _json_fixture_bytes(value)
        changed_digest = _sha256_bytes(raw)
        _object(candidate, changed_digest).write_bytes(raw)
        _active(candidate).write_bytes(_pointer(changed_digest))
        return lambda: locate_active_package(candidate.data_root), "INPUT_INVALID"

    assert document == "active"
    raw = _json_fixture_bytes(
        {
            "schema_version": registration.ACTIVE_POINTER_SCHEMA,
            "owner": registration.REGISTRATION_OWNER,
            "registration_sha256": special,
        }
    )
    _active(candidate).write_bytes(raw)
    return (
        lambda: activate_package(candidate.data_root, _sha256_bytes(raw), digest),
        "TAMPERED",
    )


def _create_real_directory_reparse(link: Path, target: Path) -> str:
    try:
        os.symlink(target, link, target_is_directory=True)
        return "symlink"
    except OSError as symlink_error:
        if os.name != "nt":
            raise AssertionError(f"could not create required real symlink: {symlink_error}")
        created = subprocess.run(
            ["cmd.exe", "/d", "/c", "mklink", "/J", str(link), str(target)],
            capture_output=True,
            text=True,
            check=False,
            timeout=10,
        )
        assert created.returncode == 0, (
            f"symlink failed: {symlink_error}; junction failed: "
            f"stdout={created.stdout!r}, stderr={created.stderr!r}"
        )
        return "junction"


def test_register_package_builds_canonical_immutable_v1_object_without_activation(
    tmp_path: Path,
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    result = register_package(
        candidate.data_root,
        candidate.archive,
        candidate.sidecar,
        candidate.package_root,
        candidate.package_python,
    )
    digest = result["registration_sha256"]
    object_path = _object(candidate, digest)
    assert isinstance(result, MappingProxyType)
    with pytest.raises(TypeError):
        result["package_root"] = "changed"  # type: ignore[index]
    assert result["schema_version"] == registration.REGISTRATION_SCHEMA
    assert result["owner"] == registration.REGISTRATION_OWNER
    assert result["authority"]["manifest"] == MANIFEST_AUTHORITY
    assert result["authority"]["lock"] == LOCK_AUTHORITY
    assert result["package_python"]["path"] == str(candidate.package_python.resolve())
    assert _sha256(object_path) == digest
    assert object_path.read_bytes().endswith(b"\n")
    assert json.loads(object_path.read_text(encoding="utf-8"))["package_root"] == str(
        candidate.package_root.resolve()
    )
    assert not _active(candidate).exists()
    assert (_registry(candidate) / "active.lock").read_bytes() == registration.LOCK_BYTES


def test_registration_is_deterministic_and_same_object_is_idempotent(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    first = candidate.register()
    before = _snapshot(_registry(candidate))
    second = candidate.register()
    assert second["registration_sha256"] == first["registration_sha256"]
    assert _snapshot(_registry(candidate)) == before


@pytest.mark.parametrize(
    ("mutate", "expected"),
    [
        (lambda c: c.sidecar.write_text("0" * 64 + "\n", encoding="utf-8"), "HASH_MISMATCH"),
        (
            lambda c: c.sidecar.write_text(f"{_sha256(c.archive)} other.zip\n", encoding="utf-8"),
            "IDENTITY_MISMATCH",
        ),
        (lambda c: c.sidecar.write_text("bad\n", encoding="utf-8"), "INPUT_INVALID"),
    ],
)
def test_invalid_sidecar_is_rejected_before_any_registry_write(
    tmp_path: Path, mutate: Callable[[Candidate], None], expected: str
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    before = _snapshot(candidate.data_root, candidate.package_root, candidate.archive, candidate.sidecar)
    mutate(candidate)
    expected_snapshot = _snapshot(
        candidate.data_root, candidate.package_root, candidate.archive, candidate.sidecar
    )
    _expect_code(expected, candidate.register)
    assert _snapshot(
        candidate.data_root, candidate.package_root, candidate.archive, candidate.sidecar
    ) == expected_snapshot
    assert before != expected_snapshot
    assert not _registry(candidate).exists()


@pytest.mark.parametrize("authority_target", ["manifest", "lock"])
@pytest.mark.parametrize("change", ["missing", "unknown"])
def test_authority_objects_require_their_exact_independent_shapes(
    tmp_path: Path, authority_target: str, change: str
) -> None:
    candidate = _make_candidate(tmp_path / f"{authority_target}-{change}")
    value = candidate.manifest() if authority_target == "manifest" else candidate.lock()
    authority = value["authority"]
    if change == "missing":
        authority.pop(next(iter(authority)))
    else:
        authority["unexpected"] = True
    if authority_target == "manifest":
        candidate.write_manifest(value)
    else:
        candidate.write_lock(value)
    candidate.rebuild_archive()
    _expect_code("INPUT_INVALID", candidate.register)
    assert not _registry(candidate).exists()


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("source_commit", "A" * 40),
        ("file_count", True),
    ],
)
def test_manifest_commit_and_integer_types_are_strict(
    tmp_path: Path, field: str, value: Any
) -> None:
    candidate = _make_candidate(tmp_path / field)
    manifest = candidate.manifest()
    manifest["core"][field] = value
    candidate.write_manifest(manifest)
    candidate.rebuild_archive()
    _expect_code("INPUT_INVALID", candidate.register)


def test_manifest_and_lock_identity_mismatch_is_rejected(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    lock = candidate.lock()
    lock["source_ref"] = "different-release"
    candidate.write_lock(lock)
    candidate.rebuild_archive()
    _expect_code("IDENTITY_MISMATCH", candidate.register)


@pytest.mark.parametrize(
    ("mutation", "code"),
    [
        ("python_owner", "IDENTITY_MISMATCH"),
        ("python_hash", "HASH_MISMATCH"),
        ("python_size", "HASH_MISMATCH"),
        ("python_metadata_unknown", "INPUT_INVALID"),
        ("python_runtime_role", "IDENTITY_MISMATCH"),
    ],
)
def test_bundled_python_contract_is_fail_closed(
    tmp_path: Path, mutation: str, code: str
) -> None:
    candidate = _make_candidate(tmp_path / mutation)
    manifest = candidate.manifest()
    entry = next(
        item for item in manifest["files"] if item["path"] == registration.PYTHON_RELATIVE_PATH
    )
    if mutation == "python_owner":
        entry["owner"] = "workbuddy_consumer"
    elif mutation == "python_hash":
        entry["sha256"] = "0" * 64
    elif mutation == "python_size":
        entry["size"] += 1
    elif mutation == "python_metadata_unknown":
        manifest["bootstrap_runtime"]["python"]["unexpected"] = True
    else:
        manifest["installation"]["runtime_roles"]["python"] = "required"
    candidate.write_manifest(manifest)
    candidate.rebuild_archive()
    _expect_code(code, candidate.register)


def test_external_python_is_rejected(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    external = tmp_path / "external-python.exe"
    external.write_bytes(candidate.package_python.read_bytes())
    _expect_code(
        "IDENTITY_MISMATCH",
        lambda: register_package(
            candidate.data_root,
            candidate.archive,
            candidate.sidecar,
            candidate.package_root,
            external,
        ),
    )


@pytest.mark.parametrize("bad_path", ["../escape.txt", "folder\\escape.txt", "C:/escape.txt"])
def test_manifest_paths_cannot_escape_or_use_noncanonical_separators(
    tmp_path: Path, bad_path: str
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    manifest = candidate.manifest()
    manifest["files"][0]["path"] = bad_path
    candidate.write_manifest(manifest)
    candidate.rebuild_archive()
    _expect_code("PATH_VIOLATION", candidate.register)


def test_non_nfc_json_string_is_rejected(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    manifest = candidate.manifest()
    manifest["distribution"]["label"] = unicodedata.normalize("NFD", "café")
    candidate.write_manifest(manifest)
    candidate.rebuild_archive()
    _expect_code("INPUT_INVALID", candidate.register)


@pytest.mark.parametrize("document", ["manifest", "lock", "registration", "active"])
@pytest.mark.parametrize(
    ("token", "special"),
    [
        ("NaN", float("nan")),
        ("Infinity", float("inf")),
        ("-Infinity", float("-inf")),
    ],
)
def test_nonfinite_json_is_rejected_at_every_load_boundary_without_state_advance(
    tmp_path: Path, document: str, token: str, special: float
) -> None:
    candidate = _make_candidate(tmp_path / f"{document}-{token}")
    action, expected_code = _install_special_json_boundary(candidate, document, special)
    before = _snapshot(candidate.data_root, candidate.package_root, candidate.archive, candidate.sidecar)
    error = _expect_code(expected_code, action)
    assert "non-finite JSON constant" in error.message
    assert _snapshot(
        candidate.data_root, candidate.package_root, candidate.archive, candidate.sidecar
    ) == before


@pytest.mark.parametrize("document", ["manifest", "lock", "registration", "active"])
def test_lone_surrogate_is_rejected_at_every_load_boundary_without_native_exception(
    tmp_path: Path, document: str
) -> None:
    candidate = _make_candidate(tmp_path / document)
    action, expected_code = _install_special_json_boundary(candidate, document, "\ud800")
    before = _snapshot(candidate.data_root, candidate.package_root, candidate.archive, candidate.sidecar)
    error = _expect_code(expected_code, action)
    assert "surrogate" in error.message
    assert _snapshot(
        candidate.data_root, candidate.package_root, candidate.archive, candidate.sidecar
    ) == before


@pytest.mark.parametrize("document", ["manifest", "lock"])
@pytest.mark.parametrize(
    "bad_path",
    [
        "nested/file.txt:stream",
        "nested/CON.txt",
        "nested/aUx.json",
        "nested/COM1.cfg",
        "nested/trailing.",
        "nested/trailing ",
    ],
)
def test_windows_unsafe_components_are_rejected_in_manifest_and_lock_paths(
    tmp_path: Path, document: str, bad_path: str
) -> None:
    candidate = _make_candidate(tmp_path / document)
    if document == "manifest":
        manifest = candidate.manifest()
        manifest["files"][0]["path"] = bad_path
        candidate.write_manifest(manifest)
    else:
        lock = candidate.lock()
        lock["files"][0]["source_path"] = bad_path
        lock["bundle_sha256"] = _sha256_bytes(
            json.dumps(
                lock["files"], ensure_ascii=False, sort_keys=True, separators=(",", ":")
            ).encode("utf-8")
        )
        candidate.write_lock(lock)
    candidate.rebuild_archive()
    before = _snapshot(candidate.data_root, candidate.package_root, candidate.archive, candidate.sidecar)
    _expect_code("PATH_VIOLATION", candidate.register)
    assert _snapshot(
        candidate.data_root, candidate.package_root, candidate.archive, candidate.sidecar
    ) == before
    assert not _registry(candidate).exists()


@pytest.mark.parametrize("document", ["manifest", "lock"])
def test_windows_case_alias_collisions_are_rejected_in_both_inventories(
    tmp_path: Path, document: str
) -> None:
    candidate = _make_candidate(tmp_path / document)
    if document == "manifest":
        manifest = candidate.manifest()
        alias = dict(manifest["files"][0])
        alias["path"] = manifest["files"][0]["path"].swapcase()
        manifest["files"].append(alias)
        candidate.write_manifest(manifest)
    else:
        lock = candidate.lock()
        alias = dict(lock["files"][0])
        alias["source_path"] = lock["files"][0]["source_path"].swapcase()
        lock["files"].append(alias)
        lock["bundle_sha256"] = _sha256_bytes(
            json.dumps(
                lock["files"], ensure_ascii=False, sort_keys=True, separators=(",", ":")
            ).encode("utf-8")
        )
        candidate.write_lock(lock)
    candidate.rebuild_archive()
    _expect_code("DUPLICATE", candidate.register)
    assert not _registry(candidate).exists()


@pytest.mark.parametrize(
    "member",
    [
        "root/nested/file.txt:stream",
        "root/nested/NUL.txt",
        "root/nested/trailing.",
        "root/nested/trailing ",
    ],
)
def test_zip_members_reject_windows_unsafe_components(tmp_path: Path, member: str) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    candidate.rebuild_archive(extra=[(member, b"unsafe")])
    _expect_code("PATH_VIOLATION", candidate.register)
    assert not _registry(candidate).exists()


def test_zip_members_reject_windows_case_alias_collisions(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    alias = f"goldenkeyopenmontageforworkbuddy/{registration.MANIFEST_NAME.swapcase()}"
    candidate.rebuild_archive(extra=[(alias, candidate.manifest_path.read_bytes())])
    _expect_code("DUPLICATE", candidate.register)
    assert not _registry(candidate).exists()


def test_real_symlink_or_junction_managed_path_escape_is_rejected_without_skip(
    tmp_path: Path,
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    outside = tmp_path / "outside"
    outside.mkdir()
    payload = outside / "payload.txt"
    payload.write_text("outside\n", encoding="utf-8")
    link = candidate.package_root / "escaped"
    reparse_kind = _create_real_directory_reparse(link, outside)
    assert reparse_kind in {"symlink", "junction"}

    relative = "escaped/payload.txt"
    lock = candidate.lock()
    lock["files"].append(
        {
            "path": f"workbuddy-core/{relative}",
            "source_path": relative,
            "sha256": _sha256(payload),
            "size": payload.stat().st_size,
            "source_mode": "100644",
            "apply_mode": "replace",
            "classification": "workbuddy_callable",
        }
    )
    lock["bundle_sha256"] = _sha256_bytes(
        json.dumps(
            lock["files"], ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
    )
    candidate.write_lock(lock, sync_manifest=False)
    manifest = candidate.manifest()
    manifest["core"]["file_count"] = len(lock["files"])
    manifest["files"].append(_inventory_entry(payload, relative, "managed_core"))
    lock_entry = next(
        item for item in manifest["files"] if item["path"] == registration.LOCK_NAME
    )
    lock_entry["sha256"] = _sha256(candidate.lock_path)
    lock_entry["size"] = candidate.lock_path.stat().st_size
    candidate.write_manifest(manifest)
    candidate.rebuild_archive()
    before_data = _snapshot(candidate.data_root)
    before_outside = _snapshot(outside)
    try:
        _expect_code("PATH_VIOLATION", candidate.register)
        assert _snapshot(candidate.data_root) == before_data
        assert _snapshot(outside) == before_outside
        assert not _registry(candidate).exists()
    finally:
        if link.is_symlink():
            link.unlink()
        elif link.exists():
            link.rmdir()


def test_archive_requires_unique_safe_manifest_and_lock(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    with pytest.warns(UserWarning):
        candidate.rebuild_archive(
            extra=[
                (
                    f"GoldenKeyOpenMontageForWorkBuddy/{registration.MANIFEST_NAME}",
                    candidate.manifest_path.read_bytes(),
                )
            ]
        )
    _expect_code("DUPLICATE", candidate.register)


def test_archive_and_installed_manifest_must_be_byte_identical(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    installed = candidate.manifest_path.read_bytes()
    with zipfile.ZipFile(candidate.archive, "w") as bundle:
        bundle.writestr(f"root/{registration.MANIFEST_NAME}", installed + b" ")
        bundle.writestr(f"root/{registration.LOCK_NAME}", candidate.lock_path.read_bytes())
    candidate.sidecar.write_text(f"{_sha256(candidate.archive)}\n", encoding="utf-8")
    _expect_code("HASH_MISMATCH", candidate.register)


def test_lock_bundle_digest_and_duplicate_source_paths_are_rejected(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    lock = candidate.lock()
    lock["files"].append(dict(lock["files"][0]))
    lock["bundle_sha256"] = _sha256_bytes(
        json.dumps(
            lock["files"], ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
    )
    candidate.write_lock(lock)
    candidate.rebuild_archive()
    _expect_code("DUPLICATE", candidate.register)


def test_managed_file_tampering_is_rejected_before_registry_write(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    candidate.managed_path.write_text("tampered\n", encoding="utf-8")
    before = _snapshot(candidate.data_root, candidate.package_root)
    _expect_code("HASH_MISMATCH", candidate.register)
    assert _snapshot(candidate.data_root, candidate.package_root) == before
    assert not _registry(candidate).exists()


def test_activate_and_locate_exact_registered_package(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    registered = candidate.register()
    digest = registered["registration_sha256"]
    _activate_missing(candidate, digest)
    located = locate_active_package(candidate.data_root)
    assert isinstance(located, MappingProxyType)
    assert located["registration_sha256"] == digest
    assert located["contract_id"] == CONTRACT_ID
    assert located["package_root"] == str(candidate.package_root.resolve())
    assert located["package_python"]["relative_path"] == registration.PYTHON_RELATIVE_PATH
    assert set(located) == {
        "registration_sha256",
        "contract_id",
        "openmontage_release",
        "openmontage_commit",
        "authority",
        "release",
        "package_root",
        "package_python",
        "manifest",
        "lock",
        "guide",
    }


def test_activation_requires_exact_raw_pointer_cas(tmp_path: Path) -> None:
    data_root = tmp_path / "data"
    first = _make_candidate(tmp_path / "first", data_root=data_root)
    second = _make_candidate(tmp_path / "second", data_root=data_root, python_payload=b"python-two")
    first_sha = first.register()["registration_sha256"]
    second_sha = second.register()["registration_sha256"]
    _activate_missing(first, first_sha)
    old_raw = _active(first).read_bytes()
    old_hash = _sha256_bytes(old_raw)
    assert activate_package(data_root, old_hash, second_sha) == second_sha
    _expect_code(
        "ACTIVE_CAS_MISMATCH",
        lambda: activate_package(data_root, old_hash, first_sha),
    )
    assert locate_active_package(data_root)["registration_sha256"] == second_sha


def test_explicit_old_registration_reactivation_is_the_only_rollback(tmp_path: Path) -> None:
    data_root = tmp_path / "data"
    old = _make_candidate(tmp_path / "old", data_root=data_root)
    new = _make_candidate(tmp_path / "new", data_root=data_root, python_payload=b"new-python")
    old_sha = old.register()["registration_sha256"]
    new_sha = new.register()["registration_sha256"]
    _activate_missing(old, old_sha)
    pointer_hash = _sha256(_active(old))
    activate_package(data_root, pointer_hash, new_sha)
    pointer_hash = _sha256(_active(old))
    assert activate_package(data_root, pointer_hash, old_sha) == old_sha
    assert locate_active_package(data_root)["registration_sha256"] == old_sha


def test_foreign_bytes_at_content_address_are_never_overwritten(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    path = _object(candidate, digest)
    path.write_bytes(b"foreign")
    _expect_code("DUPLICATE", candidate.register)
    assert path.read_bytes() == b"foreign"


@pytest.mark.parametrize("state", ["missing", "tampered"])
def test_existing_registry_never_recreates_missing_or_tampered_lock(
    tmp_path: Path, state: str
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    lock = _registry(candidate) / "active.lock"
    if state == "missing":
        lock.unlink()
    else:
        lock.write_bytes(b"tampered")
    _expect_code("TAMPERED", lambda: activate_package(candidate.data_root, "MISSING", digest))
    if state == "missing":
        assert not lock.exists()
    else:
        assert lock.read_bytes() == b"tampered"


def test_unavailable_kernel_lock_api_fails_closed(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    if os.name == "nt":
        monkeypatch.setattr(registration, "_msvcrt", None)
    else:
        monkeypatch.setattr(registration, "_fcntl", None)
    _expect_code("TAMPERED", lambda: activate_package(candidate.data_root, "MISSING", digest))
    assert not _active(candidate).exists()


def test_lock_contention_times_out_without_pointer_write(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    paths = registration._registry_paths(candidate.data_root)
    with registration._active_lock(paths):
        child = _activation_child(candidate.data_root, "MISSING", digest)
    assert child.returncode == 0, child.stderr
    assert child.stdout.strip() == "ACTIVE_LOCK_BUSY"
    assert not _active(candidate).exists()


def test_process_and_kernel_lock_contention_share_one_total_deadline(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    clock = [0.0]

    class ScriptedProcessLock:
        def __init__(self) -> None:
            self.attempts = 0
            self.released = False

        def acquire(self, *, blocking: bool) -> bool:
            assert blocking is False
            self.attempts += 1
            return self.attempts >= 4

        def release(self) -> None:
            self.released = True

    process_lock = ScriptedProcessLock()

    def monotonic() -> float:
        return clock[0]

    def advance(seconds: float) -> None:
        clock[0] += seconds

    def kernel_busy(handle: Any) -> None:
        raise BlockingIOError("injected external kernel-lock contention")

    monkeypatch.setattr(registration, "_PROCESS_ACTIVE_LOCK", process_lock)
    monkeypatch.setattr(registration, "_ACTIVE_LOCK_TIMEOUT_SECONDS", 5.0)
    monkeypatch.setattr(registration, "_ACTIVE_LOCK_RETRY_SECONDS", 1.0)
    monkeypatch.setattr(registration.time, "monotonic", monotonic)
    monkeypatch.setattr(registration.time, "sleep", advance)
    monkeypatch.setattr(registration, "_lock_byte", kernel_busy)

    _expect_code(
        "ACTIVE_LOCK_BUSY",
        lambda: activate_package(candidate.data_root, "MISSING", digest),
    )
    assert process_lock.attempts == 4
    assert process_lock.released is True
    assert clock[0] == pytest.approx(5.0)
    assert not _active(candidate).exists()


def test_process_crash_releases_kernel_lock_without_deleting_identity_file(
    tmp_path: Path,
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    lock_path = _registry(candidate) / "active.lock"
    child_code = r"""
import os
import sys

handle = open(sys.argv[1], "r+b", buffering=0)
handle.seek(0)
if os.name == "nt":
    import msvcrt
    msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
else:
    import fcntl
    fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
os._exit(23)
"""
    crashed = subprocess.run(
        [sys.executable, "-c", child_code, str(lock_path)],
        capture_output=True,
        text=True,
        check=False,
        timeout=10,
    )
    assert crashed.returncode == 23, crashed.stderr
    assert lock_path.read_bytes() == registration.LOCK_BYTES
    assert activate_package(candidate.data_root, "MISSING", digest) == digest


def test_replace_failure_preserves_old_pointer_and_hides_temp(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    data_root = tmp_path / "data"
    old = _make_candidate(tmp_path / "old", data_root=data_root)
    new = _make_candidate(tmp_path / "new", data_root=data_root, python_payload=b"new")
    old_sha = old.register()["registration_sha256"]
    new_sha = new.register()["registration_sha256"]
    _activate_missing(old, old_sha)
    before = _active(old).read_bytes()
    real_replace = registration.os.replace

    def fail_replace(source: Any, destination: Any) -> None:
        raise OSError("injected replace failure")

    monkeypatch.setattr(registration.os, "replace", fail_replace)
    _expect_code(
        "ATOMIC_WRITE_FAILED",
        lambda: activate_package(data_root, _sha256_bytes(before), new_sha),
    )
    assert _active(old).read_bytes() == before
    assert not list(_registry(old).glob(".active.*.tmp"))
    monkeypatch.setattr(registration.os, "replace", real_replace)
    assert activate_package(data_root, _sha256_bytes(before), new_sha) == new_sha


def test_lock_critical_section_observed_pointer_tampering_fails_cas(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    original = registration._atomic_replace_active
    intruder = b"out-of-band-change"

    def change_then_replace(
        path: Path, payload: bytes, expected_current_raw: bytes | None
    ) -> None:
        path.write_bytes(intruder)
        original(path, payload, expected_current_raw)

    monkeypatch.setattr(registration, "_atomic_replace_active", change_then_replace)
    _expect_code(
        "ACTIVE_CAS_MISMATCH",
        lambda: activate_package(candidate.data_root, "MISSING", digest),
    )
    assert _active(candidate).read_bytes() == intruder
    assert not list(_registry(candidate).glob(".active.*.tmp"))


def test_stale_temp_is_ignored_by_locator(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    _activate_missing(candidate, digest)
    stale = _registry(candidate) / ".active.stale.tmp"
    stale.write_bytes(b"not a pointer")
    assert locate_active_package(candidate.data_root)["registration_sha256"] == digest


def test_writer_holds_kernel_lock_from_final_compare_through_replace(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    data_root = tmp_path / "data"
    current = _make_candidate(tmp_path / "current", data_root=data_root)
    next_a = _make_candidate(tmp_path / "next-a", data_root=data_root, python_payload=b"a")
    next_b = _make_candidate(tmp_path / "next-b", data_root=data_root, python_payload=b"b")
    current_sha = current.register()["registration_sha256"]
    a_sha = next_a.register()["registration_sha256"]
    b_sha = next_b.register()["registration_sha256"]
    _activate_missing(current, current_sha)
    expected = _sha256(_active(current))
    entered = threading.Event()
    release = threading.Event()
    original = registration._atomic_replace_active

    def paused_replace(path: Path, payload: bytes, expected_current_raw: bytes | None) -> None:
        if threading.current_thread().name == "writer-a":
            entered.set()
            assert release.wait(timeout=5)
        original(path, payload, expected_current_raw)

    monkeypatch.setattr(registration, "_atomic_replace_active", paused_replace)
    monkeypatch.setattr(registration, "_ACTIVE_LOCK_TIMEOUT_SECONDS", 0.15)
    monkeypatch.setattr(registration, "_ACTIVE_LOCK_RETRY_SECONDS", 0.01)
    outcomes: dict[str, str] = {}

    def writer_a() -> None:
        outcomes["a"] = activate_package(data_root, expected, a_sha)

    first = threading.Thread(target=writer_a, name="writer-a")
    first.start()
    assert entered.wait(timeout=5)
    child = _activation_child(data_root, expected, b_sha, timeout_seconds=0.15)
    assert child.returncode == 0, child.stderr
    outcomes["b"] = child.stdout.strip()
    assert outcomes["b"] == "ACTIVE_LOCK_BUSY"
    release.set()
    first.join(timeout=3)
    assert outcomes["a"] == a_sha
    _expect_code(
        "ACTIVE_CAS_MISMATCH",
        lambda: activate_package(data_root, expected, b_sha),
    )
    assert locate_active_package(data_root)["registration_sha256"] == a_sha


def test_recover_requires_exact_broken_pointer_hash_and_valid_explicit_target(
    tmp_path: Path,
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    broken = b'{"broken":true}\n'
    _active(candidate).write_bytes(broken)
    _expect_code(
        "ACTIVE_CAS_MISMATCH",
        lambda: recover_active_package(candidate.data_root, "0" * 64, digest),
    )
    _expect_code(
        "OBJECT_MISSING",
        lambda: recover_active_package(candidate.data_root, _sha256_bytes(broken), "f" * 64),
    )
    assert recover_active_package(candidate.data_root, _sha256_bytes(broken), digest) == digest
    assert locate_active_package(candidate.data_root)["registration_sha256"] == digest


def test_recover_rejects_valid_pointer(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    _activate_missing(candidate, digest)
    raw = _active(candidate).read_bytes()
    _expect_code(
        "INPUT_INVALID",
        lambda: recover_active_package(candidate.data_root, _sha256_bytes(raw), digest),
    )
    assert _active(candidate).read_bytes() == raw


def test_activate_and_recover_are_mutually_exclusive(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    data_root = tmp_path / "data"
    first = _make_candidate(tmp_path / "first", data_root=data_root)
    second = _make_candidate(tmp_path / "second", data_root=data_root, python_payload=b"second")
    first_sha = first.register()["registration_sha256"]
    second_sha = second.register()["registration_sha256"]
    broken = b"broken-pointer"
    _active(first).write_bytes(broken)
    entered = threading.Event()
    release = threading.Event()
    original = registration._atomic_replace_active

    def paused_replace(path: Path, payload: bytes, expected_current_raw: bytes | None) -> None:
        if threading.current_thread().name == "recover-writer":
            entered.set()
            assert release.wait(timeout=5)
        original(path, payload, expected_current_raw)

    monkeypatch.setattr(registration, "_atomic_replace_active", paused_replace)
    monkeypatch.setattr(registration, "_ACTIVE_LOCK_TIMEOUT_SECONDS", 0.12)
    monkeypatch.setattr(registration, "_ACTIVE_LOCK_RETRY_SECONDS", 0.01)
    result: dict[str, str] = {}

    def recover_writer() -> None:
        result["recover"] = recover_active_package(
            data_root, _sha256_bytes(broken), first_sha
        )

    thread = threading.Thread(target=recover_writer, name="recover-writer")
    thread.start()
    assert entered.wait(timeout=5)
    child = _activation_child(
        data_root, _sha256_bytes(broken), second_sha, timeout_seconds=0.12
    )
    assert child.returncode == 0, child.stderr
    result["activate"] = child.stdout.strip()
    release.set()
    thread.join(timeout=3)
    assert result == {"activate": "ACTIVE_LOCK_BUSY", "recover": first_sha}


@pytest.mark.parametrize(
    "target",
    ["manifest", "lock", "guide", "python", "managed"],
)
def test_locator_revalidates_every_local_identity(tmp_path: Path, target: str) -> None:
    candidate = _make_candidate(tmp_path / target)
    digest = candidate.register()["registration_sha256"]
    _activate_missing(candidate, digest)
    paths = {
        "manifest": candidate.manifest_path,
        "lock": candidate.lock_path,
        "guide": candidate.guide_path,
        "python": candidate.package_python,
        "managed": candidate.managed_path,
    }
    paths[target].write_bytes(paths[target].read_bytes() + b"tampered")
    before = _snapshot(candidate.data_root, candidate.package_root)
    error = _expect_code(
        "HASH_MISMATCH",
        lambda: locate_active_package(candidate.data_root),
    )
    assert "mismatch" in error.message
    assert _snapshot(candidate.data_root, candidate.package_root) == before


@pytest.mark.parametrize("case", ["missing_pointer", "bad_pointer", "missing_object", "changed_object"])
def test_locator_fails_closed_for_pointer_and_object_damage(tmp_path: Path, case: str) -> None:
    candidate = _make_candidate(tmp_path / case)
    digest = candidate.register()["registration_sha256"]
    if case != "missing_pointer":
        _activate_missing(candidate, digest)
    if case == "bad_pointer":
        _active(candidate).write_bytes(b"bad")
    elif case == "missing_object":
        _object(candidate, digest).unlink()
    elif case == "changed_object":
        _object(candidate, digest).write_bytes(b"changed")
    expected = "OBJECT_MISSING" if case in {"missing_pointer", "missing_object"} else "TAMPERED"
    before = _snapshot(candidate.data_root, candidate.package_root)
    _expect_code(expected, lambda: locate_active_package(candidate.data_root))
    assert _snapshot(candidate.data_root, candidate.package_root) == before


def test_one_or_multiple_objects_never_substitute_for_missing_pointer(tmp_path: Path) -> None:
    data_root = tmp_path / "data"
    first = _make_candidate(tmp_path / "first", data_root=data_root)
    second = _make_candidate(tmp_path / "second", data_root=data_root, python_payload=b"second")
    first.register()
    _expect_code("OBJECT_MISSING", lambda: locate_active_package(data_root))
    second.register()
    _expect_code("OBJECT_MISSING", lambda: locate_active_package(data_root))
    assert not _active(first).exists()


def test_moved_package_root_is_not_guessed_or_scanned(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    _activate_missing(candidate, digest)
    moved = candidate.package_root.with_name("moved-package")
    candidate.package_root.rename(moved)
    _expect_code("OBJECT_MISSING", lambda: locate_active_package(candidate.data_root))
    assert moved.is_dir()


def test_locator_success_is_byte_and_mtime_read_only(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    _activate_missing(candidate, digest)
    before = _snapshot(candidate.data_root, candidate.package_root)
    assert locate_active_package(candidate.data_root)["registration_sha256"] == digest
    assert _snapshot(candidate.data_root, candidate.package_root) == before


@pytest.mark.parametrize(
    ("where", "change"),
    [
        ("root", "unknown"),
        ("root", "missing"),
        ("authority", "unknown"),
        ("authority", "missing"),
        ("release", "unknown"),
        ("package_python", "missing"),
        ("manifest", "unknown"),
        ("lock", "unknown"),
        ("guide", "unknown"),
    ],
)
def test_registration_object_rejects_unknown_and_missing_fields_at_every_level(
    tmp_path: Path, where: str, change: str
) -> None:
    candidate = _make_candidate(tmp_path / f"{where}-{change}")
    registered = candidate.register()
    digest = registered["registration_sha256"]
    value = json.loads(_object(candidate, digest).read_text(encoding="utf-8"))
    target = value if where == "root" else value[where]
    if change == "unknown":
        target["unexpected"] = True
    else:
        target.pop(next(iter(target)))
    raw = _canonical(value)
    changed_digest = _sha256_bytes(raw)
    _object(candidate, changed_digest).write_bytes(raw)
    _active(candidate).write_bytes(_pointer(changed_digest))
    _expect_code("INPUT_INVALID", lambda: locate_active_package(candidate.data_root))


def test_registration_object_duplicate_json_key_is_rejected(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    candidate.register()
    raw = (
        b'{"owner":"golden-key-workbuddy-shell-v2",'
        b'"owner":"golden-key-workbuddy-shell-v2",'
        b'"schema_version":"golden-key-workbuddy-openmontage-package-registration-v1"}\n'
    )
    digest = _sha256_bytes(raw)
    _object(candidate, digest).write_bytes(raw)
    _active(candidate).write_bytes(_pointer(digest))
    _expect_code("DUPLICATE", lambda: locate_active_package(candidate.data_root))


def test_registration_object_path_alias_is_rejected(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    registered = candidate.register()
    digest = registered["registration_sha256"]
    value = json.loads(_object(candidate, digest).read_text(encoding="utf-8"))
    value["package_root"] = str(candidate.package_root / ".") + os.sep
    raw = _canonical(value)
    changed_digest = _sha256_bytes(raw)
    _object(candidate, changed_digest).write_bytes(raw)
    _active(candidate).write_bytes(_pointer(changed_digest))
    _expect_code("TAMPERED", lambda: locate_active_package(candidate.data_root))


def test_invalid_old_registration_cannot_be_reactivated(tmp_path: Path) -> None:
    data_root = tmp_path / "data"
    old = _make_candidate(tmp_path / "old", data_root=data_root)
    new = _make_candidate(tmp_path / "new", data_root=data_root, python_payload=b"new")
    old_sha = old.register()["registration_sha256"]
    new_sha = new.register()["registration_sha256"]
    _activate_missing(old, new_sha)
    old.guide_path.write_text("tampered", encoding="utf-8")
    raw = _active(old).read_bytes()
    _expect_code(
        "HASH_MISMATCH",
        lambda: activate_package(data_root, _sha256_bytes(raw), old_sha),
    )
    assert locate_active_package(data_root)["registration_sha256"] == new_sha


def test_data_root_and_all_candidate_paths_must_be_explicit_absolute_paths(
    tmp_path: Path,
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    _expect_code(
        "PATH_VIOLATION",
        lambda: register_package(
            "relative-data",
            candidate.archive,
            candidate.sidecar,
            candidate.package_root,
            candidate.package_python,
        ),
    )
    _expect_code(
        "PATH_VIOLATION",
        lambda: register_package(
            candidate.data_root,
            "relative.zip",
            candidate.sidecar,
            candidate.package_root,
            candidate.package_python,
        ),
    )


def test_package_registration_imports_no_forbidden_shell_or_agent_control_modules() -> None:
    source = Path(registration.__file__).read_text(encoding="utf-8")
    forbidden = (
        "golden_key_openmontage_workbuddy.runtime",
        "golden_key_openmontage_workbuddy.tasks",
        "golden_key_openmontage_workbuddy.mcp_server",
        "lib.checkpoint",
        "lib.pipeline_loader",
        "schemas.artifacts",
        "subprocess",
        "socket",
    )
    assert not any(token in source for token in forbidden)
