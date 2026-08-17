from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from types import MappingProxyType, SimpleNamespace
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


ORIGIN = "https://github.com/calesthio/OpenMontage.git"


def _git(root: Path, *arguments: str) -> bytes:
    completed = subprocess.run(
        ["git", "-C", str(root), *arguments],
        shell=False,
        capture_output=True,
        check=False,
        timeout=10,
    )
    assert completed.returncode == 0, completed.stderr.decode("utf-8", errors="replace")
    return completed.stdout


def _sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _sha256(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())


def _canonical(value: dict[str, Any]) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode(
            "utf-8"
        )
        + b"\n"
    )


@dataclass
class Candidate:
    root: Path
    data_root: Path
    commit: str

    @property
    def guide(self) -> Path:
        return self.root / registration.GUIDE_NAME

    @property
    def managed(self) -> Path:
        return self.root / "src" / "fixture.txt"

    def register(self) -> dict[str, Any]:
        return dict(register_package(self.data_root, self.root, ORIGIN, self.commit))


def _make_candidate(
    base: Path,
    *,
    data_root: Path | None = None,
    with_guide: bool = True,
    empty_guide: bool = False,
    origin: str = ORIGIN,
) -> Candidate:
    root = base / "package"
    root.mkdir(parents=True)
    data = data_root or (base / "data")
    data.mkdir(parents=True, exist_ok=True)
    _git(root, "init", "-q")
    _git(root, "config", "user.email", "fixture@example.invalid")
    _git(root, "config", "user.name", "Fixture")
    _git(root, "config", "core.autocrlf", "false")
    _git(root, "remote", "add", "origin", origin)
    (root / ".gitignore").write_text("ignored.tmp\n", encoding="utf-8")
    managed = root / "src" / "fixture.txt"
    managed.parent.mkdir()
    managed.write_text("fixture\n", encoding="utf-8")
    if with_guide:
        (root / registration.GUIDE_NAME).write_text(
            "" if empty_guide else "# Fixture Guide\n", encoding="utf-8"
        )
    _git(root, "add", "--", ".")
    _git(root, "commit", "-q", "-m", "fixture")
    commit = _git(root, "rev-parse", "HEAD").decode("ascii").strip()
    return Candidate(root=root.resolve(), data_root=data.resolve(), commit=commit)


def _registry(candidate: Candidate) -> Path:
    return candidate.data_root / "State" / "PackageRegistration" / "v2"


def _object(candidate: Candidate, digest: str) -> Path:
    return _registry(candidate) / "objects" / f"{digest}.json"


def _active(candidate: Candidate) -> Path:
    return _registry(candidate) / "active.json"


def _pointer(digest: str) -> bytes:
    return _canonical(
        {
            "schema_version": registration.ACTIVE_POINTER_SCHEMA,
            "owner": registration.REGISTRATION_OWNER,
            "registration_sha256": digest,
        }
    )


def _expect_code(code: str, action: Callable[[], Any]) -> PackageRegistrationError:
    with pytest.raises(PackageRegistrationError) as captured:
        action()
    assert captured.value.code == code
    return captured.value


def _snapshot(*roots: Path) -> tuple[tuple[str, str, int, int, str], ...]:
    rows: list[tuple[str, str, int, int, str]] = []
    for root in roots:
        if not root.exists():
            rows.append((str(root), "missing", 0, 0, ""))
            continue
        for path in [root, *sorted(root.rglob("*"))]:
            identity = path.stat()
            rows.append(
                (
                    str(path),
                    "dir" if path.is_dir() else "file",
                    identity.st_size,
                    identity.st_mtime_ns,
                    _sha256(path) if path.is_file() else "",
                )
            )
    return tuple(rows)


def _install_changed_object(
    candidate: Candidate, original_digest: str, mutate: Callable[[dict[str, Any]], None]
) -> str:
    value = json.loads(_object(candidate, original_digest).read_text(encoding="utf-8"))
    mutate(value)
    raw = _canonical(value)
    digest = _sha256_bytes(raw)
    _object(candidate, digest).write_bytes(raw)
    _active(candidate).write_bytes(_pointer(digest))
    return digest


def _activation_child(
    data_root: Path, expected: str, target: str, *, timeout_seconds: float = 0.15
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
        timeout=15,
    )


def _create_real_directory_reparse(link: Path, target: Path) -> str:
    assert os.name == "nt"
    try:
        os.symlink(target, link, target_is_directory=True)
        return "symlink"
    except OSError as symlink_error:
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


def test_registers_canonical_immutable_v2_git_identity_without_activation(
    tmp_path: Path,
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    before = _snapshot(candidate.root)
    result = candidate.register()
    digest = result["registration_sha256"]
    assert isinstance(register_package(candidate.data_root, candidate.root, ORIGIN, candidate.commit), MappingProxyType)
    assert result["schema_version"] == registration.REGISTRATION_SCHEMA
    assert result["origin_url"] == ORIGIN
    assert result["openmontage_commit"] == candidate.commit
    assert result["inventory"]["file_count"] == 3
    assert result["guide"]["sha256"] == _sha256(candidate.guide)
    assert _sha256(_object(candidate, digest)) == digest
    assert not _active(candidate).exists()
    assert (_registry(candidate) / "active.lock").read_bytes() == registration.LOCK_BYTES
    assert _snapshot(candidate.root) == before


def test_registration_is_deterministic_and_idempotent(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    first = candidate.register()
    before = _snapshot(_registry(candidate))
    second = candidate.register()
    assert second["registration_sha256"] == first["registration_sha256"]
    assert _snapshot(_registry(candidate)) == before


@pytest.mark.parametrize(
    ("expected_origin", "actual_origin"),
    [
        ("https://github.com/other/OpenMontage.git", ORIGIN),
        (ORIGIN, "https://github.com/other/OpenMontage.git"),
    ],
)
def test_origin_mismatch_fails_before_registry_write(
    tmp_path: Path, expected_origin: str, actual_origin: str
) -> None:
    candidate = _make_candidate(tmp_path / "candidate", origin=actual_origin)
    _expect_code(
        "IDENTITY_MISMATCH",
        lambda: register_package(
            candidate.data_root, candidate.root, expected_origin, candidate.commit
        ),
    )
    assert not _registry(candidate).exists()


def test_official_origin_normalization_accepts_optional_dot_git(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    result = register_package(
        candidate.data_root,
        candidate.root,
        "https://github.com/calesthio/OpenMontage",
        candidate.commit,
    )
    assert result["origin_url"] == ORIGIN


def test_head_mismatch_fails_before_registry_write(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    _expect_code(
        "IDENTITY_MISMATCH",
        lambda: register_package(candidate.data_root, candidate.root, ORIGIN, "1" * 40),
    )
    assert not _registry(candidate).exists()


@pytest.mark.parametrize("dirty", ["tracked", "untracked"])
def test_dirty_tracked_and_untracked_are_rejected(tmp_path: Path, dirty: str) -> None:
    candidate = _make_candidate(tmp_path / dirty)
    path = candidate.managed if dirty == "tracked" else candidate.root / "extra.txt"
    path.write_text("dirty\n", encoding="utf-8")
    _expect_code("IDENTITY_MISMATCH", candidate.register)
    assert not _registry(candidate).exists()


def test_ignored_files_are_allowed_and_excluded_from_inventory(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    (candidate.root / "ignored.tmp").write_text("ignored\n", encoding="utf-8")
    registered = candidate.register()
    paths = {entry["path"] for entry in registered["inventory"]["entries"]}
    assert "ignored.tmp" not in paths
    activate_package(candidate.data_root, "MISSING", registered["registration_sha256"])
    assert locate_active_package(candidate.data_root)["inventory"]["file_count"] == 3


def test_assume_unchanged_tracked_file_cannot_be_registered(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    _git(candidate.root, "update-index", "--assume-unchanged", "--", "src/fixture.txt")
    _expect_code("IDENTITY_MISMATCH", candidate.register)
    assert not _registry(candidate).exists()


def test_skip_worktree_tracked_file_cannot_be_registered(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    _git(candidate.root, "update-index", "--skip-worktree", "--", "src/fixture.txt")
    _expect_code("IDENTITY_MISMATCH", candidate.register)
    assert not _registry(candidate).exists()


def test_worktree_file_must_match_head_blob(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    candidate.managed.write_text("not the committed blob\n", encoding="utf-8")
    original = registration._run_git

    def hide_status(root: Path, arguments: list[str], *, label: str) -> bytes:
        if arguments and arguments[0] == "status":
            return b""
        return original(root, arguments, label=label)

    monkeypatch.setattr(registration, "_run_git", hide_status)
    _expect_code("HASH_MISMATCH", candidate.register)


def test_inventory_rejects_file_swap_between_status_and_hash(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    original = registration._stable_tracked_file_identity

    def swap_then_hash(
        root: Path, relative: str, *, expected_blob: str
    ) -> tuple[str, int]:
        if relative == "src/fixture.txt":
            candidate.managed.write_text("swapped after status\n", encoding="utf-8")
        return original(root, relative, expected_blob=expected_blob)

    monkeypatch.setattr(registration, "_stable_tracked_file_identity", swap_then_hash)
    _expect_code("HASH_MISMATCH", candidate.register)


def test_locator_rejects_file_swap_during_revalidation(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    activate_package(candidate.data_root, "MISSING", digest)
    original = registration._stable_tracked_file_identity

    def swap_then_hash(
        root: Path, relative: str, *, expected_blob: str
    ) -> tuple[str, int]:
        if relative == "src/fixture.txt":
            candidate.managed.write_text("locator swap\n", encoding="utf-8")
        return original(root, relative, expected_blob=expected_blob)

    monkeypatch.setattr(registration, "_stable_tracked_file_identity", swap_then_hash)
    _expect_code("HASH_MISMATCH", lambda: locate_active_package(candidate.data_root))


def test_git_environment_cannot_redirect_package_root(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    other = _make_candidate(tmp_path / "other")
    monkeypatch.setenv("GIT_DIR", str(other.root / ".git"))
    monkeypatch.setenv("GIT_WORK_TREE", str(other.root))
    result = candidate.register()
    assert result["package_root"] == str(candidate.root)
    assert result["openmontage_commit"] == candidate.commit


def test_git_config_environment_cannot_spoof_origin(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    candidate = _make_candidate(
        tmp_path / "candidate", origin="https://github.com/other/OpenMontage.git"
    )
    monkeypatch.setenv("GIT_CONFIG_COUNT", "1")
    monkeypatch.setenv("GIT_CONFIG_KEY_0", "remote.origin.url")
    monkeypatch.setenv("GIT_CONFIG_VALUE_0", ORIGIN)
    _expect_code("IDENTITY_MISMATCH", candidate.register)


def test_package_root_requires_its_own_git_metadata(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    source = _make_candidate(tmp_path / "source")
    plain = (tmp_path / "plain").resolve()
    plain.mkdir()
    (plain / registration.GUIDE_NAME).write_bytes(source.guide.read_bytes())
    (plain / ".gitignore").write_bytes((source.root / ".gitignore").read_bytes())
    (plain / "src").mkdir()
    (plain / "src" / "fixture.txt").write_bytes(source.managed.read_bytes())
    data = (tmp_path / "data").resolve()
    data.mkdir()
    original = registration._run_git

    def redirect_reads(root: Path, arguments: list[str], *, label: str) -> bytes:
        if arguments == ["rev-parse", "--show-toplevel"]:
            return str(plain).encode("utf-8") + b"\n"
        return original(source.root, arguments, label=label)

    monkeypatch.setattr(registration, "_run_git", redirect_reads)
    _expect_code(
        "IDENTITY_MISMATCH",
        lambda: register_package(data, plain, ORIGIN, source.commit),
    )


def test_locator_disables_fsmonitor_and_optional_git_writes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    activate_package(candidate.data_root, "MISSING", digest)
    real = registration._run_process
    observed: list[tuple[list[str], dict[str, Any]]] = []

    def capture(argv: list[str], **kwargs: Any) -> Any:
        observed.append((argv, kwargs))
        return real(argv, **kwargs)

    monkeypatch.setattr(registration, "_run_process", capture)
    locate_active_package(candidate.data_root)
    assert observed
    for argv, kwargs in observed:
        assert ["-c", "core.fsmonitor=false"] == argv[1:3]
        assert kwargs["env"]["GIT_OPTIONAL_LOCKS"] == "0"
        assert kwargs["env"]["GIT_CONFIG_NOSYSTEM"] == "1"
        assert kwargs["env"]["GIT_CONFIG_GLOBAL"] == os.devnull


def test_git_environment_is_allowlisted_not_inherited(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    injected = {
        "UNRELATED_SECRET": "secret",
        "GIT_DIR": "redirect",
        "GIT_WORK_TREE": "redirect",
        "GIT_INDEX_FILE": "redirect",
        "GIT_OBJECT_DIRECTORY": "redirect",
        "GIT_ALTERNATE_OBJECT_DIRECTORIES": "redirect",
        "GIT_CONFIG_COUNT": "1",
        "GIT_CONFIG_KEY_0": "remote.origin.url",
        "GIT_CONFIG_VALUE_0": "spoof",
    }
    for key, value in injected.items():
        monkeypatch.setenv(key, value)
    real = registration._run_process
    environments: list[dict[str, str]] = []

    def capture(argv: list[str], **kwargs: Any) -> Any:
        environments.append(kwargs["env"])
        return real(argv, **kwargs)

    monkeypatch.setattr(registration, "_run_process", capture)
    candidate.register()
    controlled = {
        "GIT_CONFIG_GLOBAL",
        "GIT_CONFIG_NOSYSTEM",
        "GIT_OPTIONAL_LOCKS",
        "GIT_TERMINAL_PROMPT",
        "GCM_INTERACTIVE",
    }
    allowed = set(registration._GIT_ENVIRONMENT_ALLOWLIST) | controlled
    assert environments
    assert all(set(environment) <= allowed for environment in environments)
    assert all(not (set(injected) & set(environment)) for environment in environments)


@pytest.mark.parametrize("drift", ["missing", "hash", "size", "extra"])
def test_locator_rejects_tracked_inventory_drift(tmp_path: Path, drift: str) -> None:
    candidate = _make_candidate(tmp_path / drift)
    digest = candidate.register()["registration_sha256"]
    activate_package(candidate.data_root, "MISSING", digest)
    if drift == "missing":
        candidate.managed.unlink()
    elif drift == "hash":
        candidate.managed.write_text("changed\n", encoding="utf-8")
    elif drift == "size":
        candidate.managed.write_text("different-size\n", encoding="utf-8")
    else:
        extra = candidate.root / "extra.txt"
        extra.write_text("tracked extra\n", encoding="utf-8")
        _git(candidate.root, "add", "--", "extra.txt")
    _expect_code("IDENTITY_MISMATCH", lambda: locate_active_package(candidate.data_root))


def test_git_mode_drift_in_registration_is_rejected(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]

    def mutate(value: dict[str, Any]) -> None:
        value["inventory"]["entries"][0]["git_mode"] = "100755"
        value["inventory"]["sha256"] = _sha256_bytes(
            _canonical({"entries": value["inventory"]["entries"]})
        )

    _install_changed_object(candidate, digest, mutate)
    _expect_code("TAMPERED", lambda: locate_active_package(candidate.data_root))


@pytest.mark.parametrize("bad_path", ["../escape", "folder\\file", "C:/file", "a:stream", "NUL.txt", "trailing."])
def test_unsafe_inventory_paths_fail_closed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, bad_path: str
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    original = registration._run_git

    def injected(root: Path, arguments: list[str], *, label: str) -> bytes:
        if arguments[:2] == ["ls-tree", "-rz"]:
            return f"100644 blob {'1' * 40}\t{bad_path}\0".encode("utf-8")
        return original(root, arguments, label=label)

    monkeypatch.setattr(registration, "_run_git", injected)
    _expect_code("PATH_VIOLATION", candidate.register)


def test_duplicate_inventory_alias_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    original = registration._run_git
    source = _git(candidate.root, "ls-tree", "-rz", "--full-tree", "HEAD")
    first = next(record for record in source.split(b"\0") if b"AGENT_GUIDE.md" in record)

    def injected(root: Path, arguments: list[str], *, label: str) -> bytes:
        if arguments[:2] == ["ls-tree", "-rz"]:
            return source + first.replace(b"AGENT_GUIDE.md", b"agent_guide.md") + b"\0"
        return original(root, arguments, label=label)

    monkeypatch.setattr(registration, "_run_git", injected)
    _expect_code("DUPLICATE", candidate.register)


def test_reparse_or_symlink_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    original = registration._is_reparse_or_symlink

    def injected(path: Path) -> bool:
        return path.name == "fixture.txt" or original(path)

    monkeypatch.setattr(registration, "_is_reparse_or_symlink", injected)
    _expect_code("PATH_VIOLATION", candidate.register)


def test_windows_missing_safe_handle_api_fails_closed_without_plain_open(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    assert os.name == "nt"
    candidate = _make_candidate(tmp_path / "candidate")
    plain_open_called = False
    real_open = registration.os.open

    def observe_open(path: Any, flags: int, *args: Any, **kwargs: Any) -> int:
        nonlocal plain_open_called
        if Path(path).is_relative_to(candidate.root):
            plain_open_called = True
        return real_open(path, flags, *args, **kwargs)

    monkeypatch.setattr(registration, "_WINDOWS_HANDLE_API", None)
    monkeypatch.setattr(registration.os, "open", observe_open)
    _expect_code("TAMPERED", candidate.register)
    assert plain_open_called is False
    assert not _registry(candidate).exists()


def test_windows_real_junction_swap_after_precheck_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    assert os.name == "nt"
    candidate = _make_candidate(tmp_path / "candidate")
    outside = tmp_path / "outside"
    outside.mkdir()
    outside_file = outside / "fixture.txt"
    os.link(candidate.managed, outside_file)
    source_parent = candidate.root / "src"
    retained_parent = candidate.root / "src.prechecked"
    swapped = False
    reparse_kind = ""

    def swap_parent(path: Path) -> None:
        nonlocal swapped, reparse_kind
        if path == candidate.managed and not swapped:
            source_parent.rename(retained_parent)
            reparse_kind = _create_real_directory_reparse(source_parent, outside)
            swapped = True

    monkeypatch.setattr(registration, "_tracked_open_race_hook", swap_parent)
    try:
        _expect_code("PATH_VIOLATION", candidate.register)
        assert swapped is True
        assert reparse_kind in {"symlink", "junction"}
        assert os.path.samefile(retained_parent / "fixture.txt", outside_file)
        assert not _registry(candidate).exists()
    finally:
        if source_parent.is_symlink():
            source_parent.unlink()
        elif source_parent.exists():
            source_parent.rmdir()
        if retained_parent.exists():
            retained_parent.rename(source_parent)
    assert source_parent.is_dir()
    assert candidate.managed.read_text(encoding="utf-8") == "fixture\n"


def test_windows_open_handle_final_path_must_match_tracked_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    assert os.name == "nt"
    candidate = _make_candidate(tmp_path / "candidate")
    api = registration._WINDOWS_HANDLE_API
    assert api is not None
    monkeypatch.setattr(api, "final_path", lambda handle: str(tmp_path / "outside.txt"))
    _expect_code("PATH_VIOLATION", candidate.register)


def test_windows_open_handle_final_path_change_during_read_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    assert os.name == "nt"
    candidate = _make_candidate(tmp_path / "candidate")
    api = registration._WINDOWS_HANDLE_API
    assert api is not None
    real_final_path = api.final_path
    calls = 0

    def change_after_open(handle: int) -> str:
        nonlocal calls
        calls += 1
        if calls == 1:
            return real_final_path(handle)
        return str(tmp_path / "changed-after-open.txt")

    monkeypatch.setattr(api, "final_path", change_after_open)
    _expect_code("PATH_VIOLATION", candidate.register)
    assert calls == 2


@pytest.mark.parametrize("guide_case", ["missing", "untracked", "empty"])
def test_guide_must_be_tracked_and_nonempty(tmp_path: Path, guide_case: str) -> None:
    candidate = _make_candidate(
        tmp_path / guide_case,
        with_guide=guide_case != "missing",
        empty_guide=guide_case == "empty",
    )
    if guide_case == "untracked":
        _git(candidate.root, "rm", "--cached", registration.GUIDE_NAME)
    expected = "OBJECT_MISSING" if guide_case in {"missing", "untracked"} else "IDENTITY_MISMATCH"
    if guide_case == "untracked":
        expected = "IDENTITY_MISMATCH"
    _expect_code(expected, candidate.register)


def test_locator_rejects_changed_guide(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    activate_package(candidate.data_root, "MISSING", digest)
    candidate.guide.write_text("changed\n", encoding="utf-8")
    _expect_code("IDENTITY_MISMATCH", lambda: locate_active_package(candidate.data_root))


def test_git_commands_use_argv_shell_false_timeout_and_no_network(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    real = registration._run_process
    calls: list[tuple[list[str], dict[str, Any]]] = []

    def observed(argv: list[str], **kwargs: Any) -> Any:
        calls.append((argv, kwargs))
        return real(argv, **kwargs)

    monkeypatch.setattr(registration, "_run_process", observed)
    digest = candidate.register()["registration_sha256"]
    activate_package(candidate.data_root, "MISSING", digest)
    locate_active_package(candidate.data_root)
    assert calls
    assert all(call[0][0] == "git" for call in calls)
    assert all(call[1]["shell"] is False for call in calls)
    assert all(call[1]["timeout"] == registration._GIT_TIMEOUT_SECONDS for call in calls)
    forbidden = {"fetch", "pull", "push", "clone", "ls-remote"}
    assert not any(forbidden.intersection(argv) for argv, _ in calls)


@pytest.mark.parametrize(
    ("failure", "code"),
    [("exit", "GIT_COMMAND_FAILED"), ("timeout", "GIT_TIMEOUT"), ("non_utf8", "GIT_OUTPUT_INVALID")],
)
def test_git_failure_timeout_and_non_utf8_fail_closed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failure: str,
    code: str,
) -> None:
    candidate = _make_candidate(tmp_path / failure)

    def injected(*args: Any, **kwargs: Any) -> Any:
        if failure == "timeout":
            raise registration._process_timeout(cmd=args[0], timeout=10)
        if failure == "non_utf8":
            return SimpleNamespace(returncode=0, stdout=b"\xff", stderr=b"")
        return SimpleNamespace(returncode=9, stdout=b"", stderr=b"failed")

    monkeypatch.setattr(registration, "_run_process", injected)
    _expect_code(code, candidate.register)
    assert not _registry(candidate).exists()


def test_activate_locate_and_return_only_v2_identity(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    registered = candidate.register()
    digest = registered["registration_sha256"]
    assert activate_package(candidate.data_root, "MISSING", digest) == digest
    located = locate_active_package(candidate.data_root)
    assert isinstance(located, MappingProxyType)
    assert set(located) == {
        "registration_sha256",
        "package_root",
        "guide",
        "origin_url",
        "openmontage_commit",
        "git_tree",
        "inventory",
    }
    assert "entries" not in located["inventory"]
    assert located["guide"]["sha256"] == _sha256(candidate.guide)


def test_active_pointer_tamper_is_rejected(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    activate_package(candidate.data_root, "MISSING", digest)
    _active(candidate).write_bytes(b"tampered")
    _expect_code("TAMPERED", lambda: locate_active_package(candidate.data_root))


def test_activation_cas_race_has_one_winner(tmp_path: Path) -> None:
    data = (tmp_path / "data").resolve()
    data.mkdir()
    first = _make_candidate(tmp_path / "first", data_root=data)
    second = _make_candidate(tmp_path / "second", data_root=data)
    first_sha = first.register()["registration_sha256"]
    second_sha = second.register()["registration_sha256"]
    outcomes: list[str] = []
    barrier = threading.Barrier(2)

    def writer(target: str) -> None:
        barrier.wait()
        try:
            outcomes.append(activate_package(data, "MISSING", target))
        except PackageRegistrationError as exc:
            outcomes.append(exc.code)

    threads = [threading.Thread(target=writer, args=(target,)) for target in (first_sha, second_sha)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join(timeout=10)
    assert sorted(outcomes).count("ACTIVE_CAS_MISMATCH") == 1
    assert locate_active_package(data)["registration_sha256"] in {first_sha, second_sha}


def test_unavailable_kernel_lock_api_fails_closed(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    if os.name == "nt":
        monkeypatch.setattr(registration, "_msvcrt", None)
    else:
        monkeypatch.setattr(registration, "_fcntl", None)
    _expect_code(
        "TAMPERED",
        lambda: activate_package(candidate.data_root, "MISSING", digest),
    )
    assert not _active(candidate).exists()


def test_lock_contention_times_out_without_pointer_write(tmp_path: Path) -> None:
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
        raise BlockingIOError("injected kernel contention")

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
    data = (tmp_path / "data").resolve()
    data.mkdir()
    old = _make_candidate(tmp_path / "old", data_root=data)
    new = _make_candidate(tmp_path / "new", data_root=data)
    old_sha = old.register()["registration_sha256"]
    new_sha = new.register()["registration_sha256"]
    activate_package(data, "MISSING", old_sha)
    before = _active(old).read_bytes()
    real_replace = registration.os.replace

    def fail_replace(source: Any, destination: Any) -> None:
        raise OSError("injected replace failure")

    monkeypatch.setattr(registration.os, "replace", fail_replace)
    _expect_code(
        "ATOMIC_WRITE_FAILED",
        lambda: activate_package(data, _sha256_bytes(before), new_sha),
    )
    assert _active(old).read_bytes() == before
    assert not list(_registry(old).glob(".active.*.tmp"))
    monkeypatch.setattr(registration.os, "replace", real_replace)
    assert activate_package(data, _sha256_bytes(before), new_sha) == new_sha


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


def test_writer_holds_kernel_lock_from_final_compare_through_replace(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    data = (tmp_path / "data").resolve()
    data.mkdir()
    current = _make_candidate(tmp_path / "current", data_root=data)
    next_a = _make_candidate(tmp_path / "next-a", data_root=data)
    next_b = _make_candidate(tmp_path / "next-b", data_root=data)
    current_sha = current.register()["registration_sha256"]
    a_sha = next_a.register()["registration_sha256"]
    b_sha = next_b.register()["registration_sha256"]
    activate_package(data, "MISSING", current_sha)
    expected = _sha256(_active(current))
    entered = threading.Event()
    release = threading.Event()
    original = registration._atomic_replace_active

    def paused_replace(
        path: Path, payload: bytes, expected_current_raw: bytes | None
    ) -> None:
        if threading.current_thread().name == "writer-a":
            entered.set()
            assert release.wait(timeout=5)
        original(path, payload, expected_current_raw)

    monkeypatch.setattr(registration, "_atomic_replace_active", paused_replace)
    monkeypatch.setattr(registration, "_ACTIVE_LOCK_TIMEOUT_SECONDS", 0.15)
    monkeypatch.setattr(registration, "_ACTIVE_LOCK_RETRY_SECONDS", 0.01)
    outcomes: dict[str, str] = {}

    def writer_a() -> None:
        outcomes["a"] = activate_package(data, expected, a_sha)

    first = threading.Thread(target=writer_a, name="writer-a")
    first.start()
    assert entered.wait(timeout=5)
    child = _activation_child(data, expected, b_sha, timeout_seconds=0.15)
    assert child.returncode == 0, child.stderr
    outcomes["b"] = child.stdout.strip()
    assert outcomes["b"] == "ACTIVE_LOCK_BUSY"
    release.set()
    first.join(timeout=5)
    assert not first.is_alive()
    assert outcomes["a"] == a_sha
    _expect_code(
        "ACTIVE_CAS_MISMATCH",
        lambda: activate_package(data, expected, b_sha),
    )
    assert locate_active_package(data)["registration_sha256"] == a_sha


def test_activate_and_recover_are_mutually_exclusive(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    data = (tmp_path / "data").resolve()
    data.mkdir()
    first = _make_candidate(tmp_path / "first", data_root=data)
    second = _make_candidate(tmp_path / "second", data_root=data)
    first_sha = first.register()["registration_sha256"]
    second_sha = second.register()["registration_sha256"]
    broken = b"broken-pointer"
    _active(first).write_bytes(broken)
    entered = threading.Event()
    release = threading.Event()
    original = registration._atomic_replace_active

    def paused_replace(
        path: Path, payload: bytes, expected_current_raw: bytes | None
    ) -> None:
        if threading.current_thread().name == "recover-writer":
            entered.set()
            assert release.wait(timeout=5)
        original(path, payload, expected_current_raw)

    monkeypatch.setattr(registration, "_atomic_replace_active", paused_replace)
    monkeypatch.setattr(registration, "_ACTIVE_LOCK_TIMEOUT_SECONDS", 0.15)
    monkeypatch.setattr(registration, "_ACTIVE_LOCK_RETRY_SECONDS", 0.01)
    result: dict[str, str] = {}

    def recover_writer() -> None:
        result["recover"] = recover_active_package(
            data, _sha256_bytes(broken), first_sha
        )

    thread = threading.Thread(target=recover_writer, name="recover-writer")
    thread.start()
    assert entered.wait(timeout=5)
    child = _activation_child(
        data, _sha256_bytes(broken), second_sha, timeout_seconds=0.15
    )
    assert child.returncode == 0, child.stderr
    result["activate"] = child.stdout.strip()
    release.set()
    thread.join(timeout=5)
    assert not thread.is_alive()
    assert result == {"activate": "ACTIVE_LOCK_BUSY", "recover": first_sha}


def test_explicit_recovery_replaces_only_hash_locked_broken_pointer(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    broken = b'{"broken":true}\n'
    _active(candidate).write_bytes(broken)
    _expect_code(
        "ACTIVE_CAS_MISMATCH",
        lambda: recover_active_package(candidate.data_root, "0" * 64, digest),
    )
    assert recover_active_package(candidate.data_root, _sha256_bytes(broken), digest) == digest
    assert locate_active_package(candidate.data_root)["registration_sha256"] == digest


def test_recovery_rejects_valid_pointer(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    activate_package(candidate.data_root, "MISSING", digest)
    raw = _active(candidate).read_bytes()
    _expect_code(
        "INPUT_INVALID",
        lambda: recover_active_package(candidate.data_root, _sha256_bytes(raw), digest),
    )


def test_locator_is_zero_write_and_offline(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    digest = candidate.register()["registration_sha256"]
    activate_package(candidate.data_root, "MISSING", digest)
    before = _snapshot(candidate.data_root, candidate.root)
    locate_active_package(candidate.data_root)
    assert _snapshot(candidate.data_root, candidate.root) == before


@pytest.mark.parametrize("change", ["unknown", "missing", "duplicate_inventory"])
def test_registration_object_is_closed_and_duplicate_safe(tmp_path: Path, change: str) -> None:
    candidate = _make_candidate(tmp_path / change)
    digest = candidate.register()["registration_sha256"]

    def mutate(value: dict[str, Any]) -> None:
        if change == "unknown":
            value["unknown"] = True
        elif change == "missing":
            value.pop("git_tree")
        else:
            value["inventory"]["entries"].append(dict(value["inventory"]["entries"][0]))
            value["inventory"]["file_count"] += 1
            value["inventory"]["sha256"] = _sha256_bytes(
                _canonical({"entries": value["inventory"]["entries"]})
            )

    _install_changed_object(candidate, digest, mutate)
    expected = "DUPLICATE" if change == "duplicate_inventory" else "INPUT_INVALID"
    _expect_code(expected, lambda: locate_active_package(candidate.data_root))


def test_v1_registry_is_not_read_or_migrated(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    v1 = candidate.data_root / "State" / "PackageRegistration" / "v1"
    v1.mkdir(parents=True)
    (v1 / "active.json").write_bytes(b"legacy")
    digest = candidate.register()["registration_sha256"]
    assert _registry(candidate).is_dir()
    assert (v1 / "active.json").read_bytes() == b"legacy"
    activate_package(candidate.data_root, "MISSING", digest)
    assert locate_active_package(candidate.data_root)["registration_sha256"] == digest


def test_no_legacy_package_artifact_or_runtime_identity_dependency() -> None:
    source = Path(registration.__file__).read_text(encoding="utf-8")
    assert "BUNDLE-MANIFEST.json" not in source
    assert "GOLDEN_KEY_WORKBUDDY_CORE.lock.json" not in source
    assert "bootstrap/python/python.exe" not in source
    assert "package_python" not in source
    assert "release_archive" not in source


def test_data_root_and_package_root_must_be_explicit_absolute_paths(tmp_path: Path) -> None:
    candidate = _make_candidate(tmp_path / "candidate")
    _expect_code(
        "PATH_VIOLATION",
        lambda: register_package("relative-data", candidate.root, ORIGIN, candidate.commit),
    )
    _expect_code(
        "PATH_VIOLATION",
        lambda: register_package(candidate.data_root, "relative-package", ORIGIN, candidate.commit),
    )


def test_module_does_not_import_shell_runtime_or_agent_control_planes() -> None:
    source = Path(registration.__file__).read_text(encoding="utf-8")
    forbidden = (
        "golden_key_openmontage_workbuddy.runtime",
        "golden_key_openmontage_workbuddy.tasks",
        "golden_key_openmontage_workbuddy.mcp_server",
        "lib.checkpoint",
        "lib.pipeline_loader",
        "schemas.artifacts",
        "socket",
    )
    assert not any(token in source for token in forbidden)
