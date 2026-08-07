from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Any


MANAGED_RUNTIME_SCHEMA = "golden-key-workbuddy-managed-python-v1"


def _requirements_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _relative_interpreter() -> Path:
    if os.name == "nt":
        return Path("Scripts") / "python.exe"
    return Path("bin") / "python"


def _locations(repo_root: Path, data_root: Path) -> tuple[Path, Path, Path, Path]:
    repo_root = Path(repo_root).resolve()
    data_root = Path(data_root).resolve()
    requirements = repo_root / "requirements.txt"
    target = data_root / "Runtime" / "Python"
    record = target / "WORKBUDDY-MANAGED-PYTHON.json"
    return requirements, target, record, target / _relative_interpreter()


def build_runtime_plan(repo_root: Path, data_root: Path) -> dict[str, Any]:
    requirements, target, record_path, interpreter = _locations(
        repo_root, data_root
    )
    errors: list[str] = []
    if not requirements.is_file():
        errors.append(f"requirements file is missing: {requirements}")
    python_supported = sys.version_info >= (3, 10)
    if not python_supported:
        errors.append("Python 3.10 or newer is required to prepare the runtime")

    reusable = False
    if record_path.is_file() and interpreter.is_file() and requirements.is_file():
        try:
            record = json.loads(record_path.read_text(encoding="utf-8"))
            reusable = (
                record.get("schema_version") == MANAGED_RUNTIME_SCHEMA
                and record.get("requirements_sha256")
                == _requirements_sha256(requirements)
                and record.get("interpreter_relative")
                == _relative_interpreter().as_posix()
            )
        except (OSError, json.JSONDecodeError):
            reusable = False

    status = "fail" if errors else ("ready" if reusable else "needs_confirmation")
    return {
        "status": status,
        "target": str(target),
        "interpreter": str(interpreter),
        "requirements_file": str(requirements),
        "downloads_required": not reusable,
        "confirmation_flag": "--confirm-download",
        "system_python_modified": False,
        "storage_policy": "managed_under_selected_data_root",
        "provider_calls_attempted": 0,
        "network_calls_attempted": 0,
        "errors": errors,
    }


def prepare_managed_runtime(
    repo_root: Path, data_root: Path, *, confirm_download: bool
) -> dict[str, Any]:
    plan = build_runtime_plan(repo_root, data_root)
    if plan["status"] == "fail":
        return plan
    if plan["status"] == "ready":
        return {
            **plan,
            "status": "pass",
            "created": False,
            "reused": True,
        }
    if not confirm_download:
        return {
            **plan,
            "status": "fail",
            "downloads_required": True,
            "errors": [
                "runtime preparation can download Python packages; rerun with "
                "--confirm-download only after the user explicitly agrees"
            ],
        }

    requirements, target, _, _ = _locations(repo_root, data_root)
    runtime_root = target.parent
    if target.exists():
        return {
            **plan,
            "status": "fail",
            "network_calls_attempted": 0,
            "errors": [
                f"managed runtime target already exists and was not overwritten: {target}"
            ],
        }

    runtime_root.mkdir(parents=True, exist_ok=True)
    staging = runtime_root / f".python-staging-{uuid.uuid4().hex}"
    cache_root = Path(data_root).resolve() / "Caches" / "pip"
    cache_root.mkdir(parents=True, exist_ok=True)
    environment = os.environ.copy()
    environment["PIP_CACHE_DIR"] = str(cache_root)
    try:
        create = subprocess.run(
            [sys.executable, "-m", "venv", str(staging)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        if create.returncode != 0:
            raise RuntimeError(
                "cannot create the managed Python environment: "
                + (create.stderr or create.stdout).strip()
            )
        staging_interpreter = staging / _relative_interpreter()
        install = subprocess.run(
            [
                str(staging_interpreter),
                "-m",
                "pip",
                "install",
                "--disable-pip-version-check",
                "--no-input",
                "-r",
                str(requirements),
            ],
            env=environment,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        if install.returncode != 0:
            raise RuntimeError(
                "cannot install the managed Python dependencies: "
                + (install.stderr or install.stdout).strip()
            )
        record = {
            "schema_version": MANAGED_RUNTIME_SCHEMA,
            "requirements_sha256": _requirements_sha256(requirements),
            "interpreter_relative": _relative_interpreter().as_posix(),
            "source_python": sys.executable,
            "system_python_modified": False,
        }
        (staging / "WORKBUDDY-MANAGED-PYTHON.json").write_text(
            json.dumps(record, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        os.replace(staging, target)
    except (OSError, RuntimeError, subprocess.SubprocessError) as exc:
        if staging.exists() and staging.parent == runtime_root:
            shutil.rmtree(staging, ignore_errors=True)
        return {
            **plan,
            "status": "fail",
            "network_calls_attempted": 1,
            "errors": [str(exc)],
        }

    return {
        **plan,
        "status": "pass",
        "interpreter": str(target / _relative_interpreter()),
        "downloads_required": False,
        "created": True,
        "reused": False,
        "network_calls_attempted": 1,
        "errors": [],
    }
