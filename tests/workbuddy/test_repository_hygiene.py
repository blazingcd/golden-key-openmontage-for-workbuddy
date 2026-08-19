from __future__ import annotations

import os
import re
import subprocess
import tomllib
from pathlib import Path

import golden_key_openmontage_workbuddy as package_api
from golden_key_openmontage_workbuddy import package_registration
from golden_key_openmontage_workbuddy import runtime_prepare


REPO_ROOT = Path(__file__).resolve().parents[2]

EXPECTED_TRACKED_FILES = frozenset(
    {
        ".gitattributes",
        ".github/CODEOWNERS",
        ".github/PULL_REQUEST_TEMPLATE.md",
        ".github/copilot-instructions.md",
        ".github/workflows/ci.yml",
        ".gitignore",
        ".python-version",
        ".windsurfrules",
        "AGENTS.md",
        "AGENT_GUIDE.md",
        "CLAUDE.md",
        "CODEX.md",
        "CONTRIBUTING.md",
        "COPILOT.md",
        "CURSOR.md",
        "LICENSE",
        "PROJECT-STATE.md",
        "PROJECT_CONTEXT.md",
        "README.md",
        "README_zh-CN.md",
        "WORK-LOG.md",
        "docs/workbuddy/v2/ACCEPTANCE-MATRIX.md",
        "docs/workbuddy/v2/DRIFT-GUARD.md",
        "docs/workbuddy/v2/MODULE-DISPOSITION.md",
        "docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md",
        "docs/workbuddy/v2/PROJECT-CHARTER.md",
        "docs/workbuddy/v2/README.md",
        "docs/workbuddy/v2/TASK-REGISTER.md",
        "golden_key_openmontage_workbuddy/__init__.py",
        "golden_key_openmontage_workbuddy/package_registration.py",
        "golden_key_openmontage_workbuddy/runtime_prepare.py",
        "pyproject.toml",
        "tests/workbuddy/test_package_registration.py",
        "tests/workbuddy/test_repository_hygiene.py",
        "tests/workbuddy/test_runtime_prepare.py",
    }
)

EXPECTED_SOURCE_DIRECTORIES = frozenset(
    {
        ".github",
        ".github/workflows",
        "docs",
        "docs/workbuddy",
        "docs/workbuddy/v2",
        "golden_key_openmontage_workbuddy",
        "tests",
        "tests/workbuddy",
    }
)

GENERATED_DIRECTORY_NAMES = frozenset({".pytest_cache", "__pycache__"})

REMOVED_TOP_LEVEL_DIRECTORIES = (
    ".agents",
    ".claude",
    ".codex",
    ".cursor",
    ".workbuddy",
    "assets",
    "backlot",
    "config",
    "ink-theater",
    "lib",
    "packaging",
    "pipeline_defs",
    "remotion-composer",
    "schemas",
    "scripts",
    "skills",
    "styles",
    "tools",
    "workbuddy-runtime",
    "workbuddy-skill",
)

REMOVED_SHELL_CONTROL_PLANE_PATHS = (
    ".env.example",
    "golden_key_openmontage_workbuddy/__main__.py",
    "golden_key_openmontage_workbuddy/cli.py",
    "golden_key_openmontage_workbuddy/doctor.py",
    "golden_key_openmontage_workbuddy/gate.py",
    "golden_key_openmontage_workbuddy/mcp_server.py",
    "golden_key_openmontage_workbuddy/model_config.py",
    "golden_key_openmontage_workbuddy/paths.py",
    "golden_key_openmontage_workbuddy/runtime.py",
    "golden_key_openmontage_workbuddy/security.py",
    "golden_key_openmontage_workbuddy/subprocess_guard",
    "golden_key_openmontage_workbuddy/tasks.py",
    "Makefile",
    "requirements-dev.txt",
    "requirements-gpu.txt",
    "requirements.txt",
    "setup.py",
    "WORKBUDDY-BOOTSTRAP-RUNTIME.lock.json",
    "WORKBUDDY-PRODUCTION-RUNTIME.lock.json",
)

REMOVED_LEGACY_TESTS = (
    "test_ci_contract.py",
    "test_core_sync.py",
    "test_doctor.py",
    "test_mcp_server.py",
    "test_model_provider_config.py",
    "test_portable_bundle.py",
    "test_skill_package.py",
    "test_task_runtime.py",
    "test_w0_audit.py",
    "test_w2_runtime.py",
    "test_w3_offline_isolation.py",
)

REPLACEMENT_CONTROL_PLANE_PATHS = (
    "golden_key_openmontage_workbuddy/entry.py",
    "golden_key_openmontage_workbuddy/launcher.py",
    "golden_key_openmontage_workbuddy/relay.py",
    "golden_key_openmontage_workbuddy/status_result_relay.py",
    "golden_key_openmontage_workbuddy/workbuddy.py",
    "golden_key_openmontage_workbuddy/workbuddy_entry.py",
)

FORBIDDEN_COPY_DIRECTORY_NAMES = frozenset(
    {
        "archive",
        "archives",
        "backup",
        "backups",
        "legacy",
        "quarantine",
        "quarantined",
        "repo-copy",
        "repository-copy",
    }
)


def _git_index_files() -> frozenset[str]:
    result = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "ls-files", "-z"],
        check=True,
        capture_output=True,
    )
    return frozenset(
        path.decode("utf-8") for path in result.stdout.split(b"\0") if path
    )


def _is_generated_directory(name: str) -> bool:
    return name in GENERATED_DIRECTORY_NAMES or name.endswith(".egg-info")


def _source_inventory() -> tuple[frozenset[str], frozenset[str]]:
    files: set[str] = set()
    directories: set[str] = set()
    for current_root, child_directories, child_files in os.walk(
        REPO_ROOT, topdown=True, followlinks=False
    ):
        current = Path(current_root)
        relative_current = current.relative_to(REPO_ROOT)
        if relative_current == Path("."):
            child_directories[:] = [
                name for name in child_directories if name != ".git"
            ]

        retained_children: list[str] = []
        for name in child_directories:
            if _is_generated_directory(name):
                continue
            relative = (relative_current / name).as_posix()
            directories.add(relative)
            retained_children.append(name)
        child_directories[:] = retained_children

        for name in child_files:
            relative = (relative_current / name).as_posix()
            if relative == ".git":
                continue
            files.add(relative)
    return frozenset(files), frozenset(directories)


def test_final_git_index_is_the_fixed_35_file_contract() -> None:
    actual = _git_index_files()
    assert len(EXPECTED_TRACKED_FILES) == 35
    assert len(actual) == 35
    assert actual == EXPECTED_TRACKED_FILES


def test_final_worktree_has_no_unregistered_source_or_vendor_content() -> None:
    files, directories = _source_inventory()
    assert files == EXPECTED_TRACKED_FILES
    assert directories == EXPECTED_SOURCE_DIRECTORIES
    assert all(not (REPO_ROOT / name).exists() for name in REMOVED_TOP_LEVEL_DIRECTORIES)


def test_old_shell_control_planes_build_files_and_tests_are_absent() -> None:
    assert all(
        not (REPO_ROOT / relative).exists()
        for relative in REMOVED_SHELL_CONTROL_PLANE_PATHS
    )
    workbuddy_tests = REPO_ROOT / "tests" / "workbuddy"
    assert all(not (workbuddy_tests / name).exists() for name in REMOVED_LEGACY_TESTS)


def test_no_archive_legacy_quarantine_or_repository_copy_exists() -> None:
    _, directories = _source_inventory()
    assert all(
        component.casefold() not in FORBIDDEN_COPY_DIRECTORY_NAMES
        for relative in directories
        for component in Path(relative).parts
    )
    assert all(
        relative == ".git"
        for relative in (
            path.relative_to(REPO_ROOT).as_posix()
            for path in REPO_ROOT.rglob(".git")
        )
    )


def test_pyproject_keeps_one_dependency_free_shell_package() -> None:
    pyproject_path = REPO_ROOT / "pyproject.toml"
    source = pyproject_path.read_text(encoding="utf-8")
    project = tomllib.loads(source)

    assert project["build-system"] == {
        "requires": ["setuptools>=69"],
        "build-backend": "setuptools.build_meta",
    }
    assert project["project"] == {
        "name": "golden-key-openmontage-workbuddy",
        "version": "0.1.0a0",
        "description": "WorkBuddy Shell V2 Package Registration",
        "requires-python": ">=3.10",
        "dependencies": [],
        "optional-dependencies": {"test": ["pytest>=8.0"]},
    }
    assert project["tool"]["setuptools"] == {
        "packages": ["golden_key_openmontage_workbuddy"]
    }
    assert "scripts" not in project["project"]
    assert "entry-points" not in project["project"]
    assert "console_scripts" not in source


def test_stage2_registration_and_stage3_runtime_prepare_are_the_only_apis() -> None:
    registration_path = (
        REPO_ROOT / "golden_key_openmontage_workbuddy" / "package_registration.py"
    )
    evidence_path = REPO_ROOT / "tests" / "workbuddy" / "test_package_registration.py"
    assert registration_path.is_file()
    assert evidence_path.is_file()

    expected_exports = [
        "PackageRegistrationError",
        "register_package",
        "activate_package",
        "recover_active_package",
        "locate_active_package",
        "prepare_optional_capabilities",
        "__version__",
    ]
    assert package_api.__version__ == "0.1.0a0"
    assert package_api.__all__ == expected_exports
    for name in expected_exports[:5]:
        assert getattr(package_api, name) is getattr(package_registration, name)
    assert package_api.prepare_optional_capabilities is runtime_prepare.prepare_optional_capabilities

    package_sources = {
        path.name
        for path in (REPO_ROOT / "golden_key_openmontage_workbuddy").glob("*.py")
    }
    assert package_sources == {"__init__.py", "package_registration.py", "runtime_prepare.py"}


def test_stage3_is_bounded_and_replacement_control_planes_are_not_implemented() -> None:
    assert (REPO_ROOT / "golden_key_openmontage_workbuddy/runtime_prepare.py").is_file()
    assert all(
        not (REPO_ROOT / relative).exists()
        for relative in REPLACEMENT_CONTROL_PLANE_PATHS
    )
    task_register = (
        REPO_ROOT / "docs" / "workbuddy" / "v2" / "TASK-REGISTER.md"
    ).read_text(encoding="utf-8")
    assert "stage3_implementation: PASS_ACCEPTED" in task_register
    assert "stage_3_implementation_authorization: CONSUMED_COMPLETE" in task_register

    init_source = (
        REPO_ROOT / "golden_key_openmontage_workbuddy" / "__init__.py"
    ).read_text(encoding="utf-8")
    assert not any(
        forbidden in init_source.casefold()
        for forbidden in ("launcher", "mcp", "relay", "task", "workbuddy_entry")
    )


def test_agent_guide_preserves_the_shell_and_verified_package_boundaries() -> None:
    guide = (REPO_ROOT / "AGENT_GUIDE.md").read_text(encoding="utf-8")
    assert guide.startswith("# WorkBuddy Shell V2 Agent Guide\n")
    assert "This repository owns only the Shell V2 six-module boundary" in guide
    assert "only after Package Registration identity validation has succeeded" in guide
    assert "Never scan disks, guess a Package, or read an unverified Guide as authority." in guide
    assert (
        "Repository agents must not run a video Pipeline, Provider, media generation, "
        "or OpenMontage production work from this tree."
    ) in guide


def test_ci_targets_only_the_formal_branch_and_the_three_final_tests() -> None:
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
        "tests/workbuddy/test_runtime_prepare.py "
        "tests/workbuddy/test_repository_hygiene.py -q"
    )

    def extract_top_level_on(source: str) -> str:
        assert source.count("\non:\n") == 1
        after_on = source.split("\non:\n", maxsplit=1)[1]
        next_top_level_key = re.search(r"(?m)^(?=\S)", after_on)
        assert next_top_level_key is not None
        body = after_on[: next_top_level_key.start()]
        assert body.endswith("\n\n")
        body = body.removesuffix("\n")
        assert all(line.startswith("  ") for line in body.splitlines(keepends=True))
        return "".join(line[2:] for line in body.splitlines(keepends=True))

    assert extract_top_level_on(ci) == expected_trigger_block
    assert ci.count("python -m pytest") == 1
    assert ci.count(command) == 1
    assert "python-version: \"3.11\"" in ci
    assert "cache-dependency-path: pyproject.toml" in ci
    assert "workflow_dispatch" not in ci
    assert not any(
        forbidden in ci.casefold()
        for forbidden in (" ffmpeg", " make ", " setup.py", " gate", " mcp")
    )


def test_historical_prompts_task_packets_and_old_docs_are_absent() -> None:
    assert not any("prompt" in relative.casefold() for relative in EXPECTED_TRACKED_FILES)
    historical_prompt = re.compile(r"next[-_ ]conversation[-_ ]prompt", re.IGNORECASE)
    for relative in EXPECTED_TRACKED_FILES:
        path = REPO_ROOT / relative
        if path.suffix.casefold() in {".md", ".py", ".toml", ".yml", ".rules"}:
            assert historical_prompt.search(path.read_text(encoding="utf-8")) is None
