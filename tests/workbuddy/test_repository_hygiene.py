from __future__ import annotations

import hashlib
import re
import tomllib
from pathlib import Path

import golden_key_openmontage_workbuddy as package_api
from golden_key_openmontage_workbuddy import package_registration


REPO_ROOT = Path(__file__).resolve().parents[2]

REMOVED_LEGACY_PATHS = (
    ".env.example",
    ".workbuddy/README.md",
    "config/openmontage.sync.json",
    "golden_key_openmontage_workbuddy/__main__.py",
    "golden_key_openmontage_workbuddy/cli.py",
    "golden_key_openmontage_workbuddy/doctor.py",
    "golden_key_openmontage_workbuddy/gate.py",
    "golden_key_openmontage_workbuddy/mcp_server.py",
    "golden_key_openmontage_workbuddy/model_config.py",
    "golden_key_openmontage_workbuddy/paths.py",
    "golden_key_openmontage_workbuddy/runtime.py",
    "golden_key_openmontage_workbuddy/runtime_prepare.py",
    "golden_key_openmontage_workbuddy/security.py",
    "golden_key_openmontage_workbuddy/subprocess_guard/__init__.py",
    "golden_key_openmontage_workbuddy/subprocess_guard/offline_guard.cjs",
    "golden_key_openmontage_workbuddy/subprocess_guard/sitecustomize.py",
    "golden_key_openmontage_workbuddy/tasks.py",
    "packaging/workbuddy/bootstrap/install-to-workbuddy.cmd",
    "packaging/workbuddy/bootstrap/sitecustomize.py",
    "packaging/workbuddy/configure-provider-keys.ps1",
    "packaging/workbuddy/golden-key-workbuddy.ps1",
    "packaging/workbuddy/install-to-workbuddy.ps1",
    "packaging/workbuddy/install-workbuddy.ps1",
    "packaging/workbuddy/uninstall-workbuddy.ps1",
    "packaging/workbuddy/安装到WorkBuddy.cmd",
    "packaging/workbuddy/从WorkBuddy卸载.cmd",
    "packaging/workbuddy/配置API密钥.cmd",
    "scripts/core_sync/sync_workbuddy_core.py",
    "scripts/workbuddy/build_portable_bundle.py",
    "scripts/workbuddy/sanitize_historical_w0.py",
    "scripts/workbuddy/w0_audit.py",
    "WORKBUDDY-BOOTSTRAP-RUNTIME.lock.json",
    "WORKBUDDY-PRODUCTION-RUNTIME.lock.json",
    "workbuddy-runtime/hyperframes/package-lock.json",
    "workbuddy-runtime/hyperframes/package.json",
    "workbuddy-skill/golden-key-openmontage-onboarding/SKILL.md",
    "workbuddy-skill/golden-key-openmontage/SKILL.md",
    "Makefile",
    "requirements-dev.txt",
    "requirements-gpu.txt",
    "requirements.txt",
    "setup.py",
)

REMOVED_LEGACY_TESTS = (
    "test_ci_contract.py",
    "test_core_sync.py",
    "test_doctor.py",
    "test_mcp_server.py",
    "test_model_provider_config.py",
    "test_portable_bundle.py",
    "test_runtime_prepare.py",
    "test_skill_package.py",
    "test_task_runtime.py",
    "test_w0_audit.py",
    "test_w2_runtime.py",
    "test_w3_offline_isolation.py",
)

FROZEN_BLOBS = {
    "golden_key_openmontage_workbuddy/package_registration.py": (
        "d0676fb6a0ec22135ade8bc1462337ced05beec0"
    ),
    "tests/workbuddy/test_package_registration.py": (
        "7f3f0e7cf1a16fbe63ee0bb8669797bc88c78ec6"
    ),
}

ACTIVE_SHELL_FILES = (
    "golden_key_openmontage_workbuddy/__init__.py",
    "golden_key_openmontage_workbuddy/package_registration.py",
    ".github/workflows/ci.yml",
)

FORBIDDEN_COPY_PATTERNS = (
    r"repo_root.{0,160}managed_core",
    r"managed_core.{0,160}(?:copytree|copy2|shutil\.copy|copyfile)",
    r"(?:copytree|copy2|shutil\.copy|copyfile).{0,160}managed_core",
)

STAGE3_IMPLEMENTATION_PATHS = (
    "golden_key_openmontage_workbuddy/launcher.py",
    "golden_key_openmontage_workbuddy/entry.py",
    "golden_key_openmontage_workbuddy/workbuddy.py",
    "golden_key_openmontage_workbuddy/workbuddy_entry.py",
    "golden_key_openmontage_workbuddy/relay.py",
    "golden_key_openmontage_workbuddy/status_result_relay.py",
    "golden_key_openmontage_workbuddy/runtime_prepare.py",
    "golden_key_openmontage_workbuddy/cli.py",
    "golden_key_openmontage_workbuddy/mcp_server.py",
)

# These reviewed prefixes remain intentionally present until Wave C. Transition
# checks are deliberately limited to fixed Shell files and never scan them.
WAVE_C_PENDING_PREFIXES = (
    ".agents",
    ".claude",
    "assets",
    "backlot",
    "ink-theater",
    "lib",
    "pipeline_defs",
    "remotion-composer",
    "schemas",
    "skills",
    "styles",
    "tools",
)


def _git_blob_id(path: Path) -> str:
    payload = path.read_bytes()
    header = f"blob {len(payload)}\0".encode()
    return hashlib.sha1(header + payload).hexdigest()


def test_legacy_package_control_plane_and_build_files_are_absent() -> None:
    assert all(not (REPO_ROOT / relative).exists() for relative in REMOVED_LEGACY_PATHS)
    workbuddy_tests = REPO_ROOT / "tests" / "workbuddy"
    assert all(not (workbuddy_tests / name).exists() for name in REMOVED_LEGACY_TESTS)


def test_pyproject_is_registration_only() -> None:
    pyproject_path = REPO_ROOT / "pyproject.toml"
    assert pyproject_path.is_file()
    project = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))

    assert project["build-system"]["build-backend"] == "setuptools.build_meta"
    assert project["project"] == {
        "name": "golden-key-openmontage-workbuddy",
        "version": "0.1.0a0",
        "description": "WorkBuddy Shell V2 Package Registration",
        "requires-python": ">=3.10",
        "dependencies": [],
        "optional-dependencies": {"test": ["pytest>=8.0"]},
    }
    assert project["tool"]["setuptools"]["packages"] == [
        "golden_key_openmontage_workbuddy"
    ]
    assert "scripts" not in project["project"]
    assert "entry-points" not in project["project"]
    assert "console_scripts" not in pyproject_path.read_text(encoding="utf-8")


def test_registration_implementation_and_evidence_are_frozen() -> None:
    for relative, expected_blob in FROZEN_BLOBS.items():
        path = REPO_ROOT / relative
        assert path.is_file()
        assert _git_blob_id(path) == expected_blob


def test_package_root_exports_only_the_registration_api() -> None:
    expected = [
        "PackageRegistrationError",
        "register_package",
        "activate_package",
        "recover_active_package",
        "locate_active_package",
        "__version__",
    ]
    assert package_api.__version__ == "0.1.0a0"
    assert package_api.__all__ == expected
    for name in expected[:-1]:
        assert getattr(package_api, name) is getattr(package_registration, name)


def test_no_active_tree_managed_core_copy_consumer_remains() -> None:
    consumer_paths = (
        "scripts/core_sync/sync_workbuddy_core.py",
        "scripts/workbuddy/build_portable_bundle.py",
        "scripts/workbuddy/sanitize_historical_w0.py",
        "scripts/workbuddy/w0_audit.py",
    )
    assert all(not (REPO_ROOT / relative).exists() for relative in consumer_paths)
    for relative in ACTIVE_SHELL_FILES:
        source = (REPO_ROOT / relative).read_text(encoding="utf-8")
        assert not any(
            re.search(pattern, source, flags=re.IGNORECASE | re.DOTALL)
            for pattern in FORBIDDEN_COPY_PATTERNS
        )


def test_stage3_and_replacement_control_planes_are_not_implemented() -> None:
    assert all(not (REPO_ROOT / relative).exists() for relative in STAGE3_IMPLEMENTATION_PATHS)
    init_source = (
        REPO_ROOT / "golden_key_openmontage_workbuddy" / "__init__.py"
    ).read_text(encoding="utf-8")
    assert "launcher" not in init_source.lower()
    assert "runtime" not in init_source.lower()
    assert "mcp" not in init_source.lower()
    assert "task" not in init_source.lower()


def test_wave_c_content_is_outside_transition_scan() -> None:
    assert WAVE_C_PENDING_PREFIXES == (
        ".agents",
        ".claude",
        "assets",
        "backlot",
        "ink-theater",
        "lib",
        "pipeline_defs",
        "remotion-composer",
        "schemas",
        "skills",
        "styles",
        "tools",
    )


def test_ci_runs_only_the_two_transition_test_files() -> None:
    ci = (REPO_ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    expected_trigger_block = (
        "pull_request:\n"
        "  branches:\n"
        "    - codex/workbuddy-shell-v2\n"
        "push:\n"
        "  branches:\n"
        "    - codex/workbuddy-shell-v2\n"
    )
    command = (
        "python -m pytest -p no:cacheprovider "
        "tests/workbuddy/test_package_registration.py "
        "tests/workbuddy/test_repository_hygiene.py -q"
    )
    def extract_top_level_on(source: str) -> str:
        assert source.count("\non:\n") == 1
        after_on = source.split("\non:\n", maxsplit=1)[1]
        next_top_level_key = re.search(r"(?m)^(?=\S)", after_on)
        assert next_top_level_key is not None
        indented_body = after_on[: next_top_level_key.start()]
        assert indented_body.endswith("\n\n")
        indented_body = indented_body.removesuffix("\n")
        assert all(
            line.startswith("  ")
            for line in indented_body.splitlines(keepends=True)
        )
        return "".join(
            line[2:] for line in indented_body.splitlines(keepends=True)
        )

    trigger_block = extract_top_level_on(ci)
    assert trigger_block == expected_trigger_block

    rejected_mutations = (
        ci.replace(
            "  push:\n"
            "    branches:\n"
            "      - codex/workbuddy-shell-v2\n",
            "  push:\n"
            "    branches:\n"
            "      - codex/workbuddy-shell-v2\n"
            "      - main\n",
            1,
        ),
        ci.replace(
            "  push:\n"
            "    branches:\n"
            "      - codex/workbuddy-shell-v2\n",
            "  push:\n"
            "    branches:\n"
            "      - codex/workbuddy-shell-v2\n"
            "    tags:\n"
            "      - v*\n",
            1,
        ),
        ci.replace(
            "  push:\n"
            "    branches:\n"
            "      - codex/workbuddy-shell-v2\n",
            "  push:\n"
            "    branches:\n"
            "      - codex/workbuddy-shell-v2\n"
            "  workflow_dispatch:\n",
            1,
        ),
    )
    assert all(
        extract_top_level_on(mutated_ci) != expected_trigger_block
        for mutated_ci in rejected_mutations
    )
    assert ci.count("python -m pytest") == 1
    assert ci.count(command) == 1
    assert "python-version: \"3.11\"" in ci
    assert "cache-dependency-path: pyproject.toml" in ci
    assert "ffmpeg" not in ci.lower()
    assert "make " not in ci.lower()
    assert " setup.py" not in ci.lower()
    assert " golden_key_openmontage_workbuddy gate" not in ci
    assert " mcp" not in ci.lower()
