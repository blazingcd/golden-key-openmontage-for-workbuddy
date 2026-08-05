"""W0 audit for a v0.3.21 WorkBuddy callable-core publication candidate.

The publication candidate is the verified Release ZIP managed scope plus
WorkBuddy-owned files on top of public ``origin/main``.  Golden Key private Git
history is deliberately outside this audit and must not be merged into the
candidate.
"""

from __future__ import annotations

import argparse
import ast
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.core_sync import sync_workbuddy_core


PUBLIC_BASE = "origin/main"
PIPELINES = (
    "golden-key-brand-company",
    "golden-key-lead-conversion",
    "golden-key-product-marketing",
    "golden-key-subject-ip",
)
FORBIDDEN_CORE_PATHS = sync_workbuddy_core.REQUIRED_CONSUMER_REMOVE_PATHS
ADAPTER_RUNTIME_ROOTS = (
    "golden_key_openmontage_workbuddy",
    "workbuddy-skill",
    "scripts/core_sync",
    "scripts/workbuddy",
    ".workbuddy",
)
ADAPTER_ENTRYPOINT_ROOTS = (
    "golden_key_openmontage_workbuddy",
    "workbuddy-skill",
    ".workbuddy",
)
RUNTIME_SUFFIXES = {".py", ".js", ".cjs", ".mjs", ".ts", ".tsx", ".json"}


def git(*args: str, check: bool = True) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if check and completed.returncode:
        raise RuntimeError(
            f"git {' '.join(args)} failed ({completed.returncode}): "
            f"{completed.stderr.strip()}"
        )
    return completed.stdout.rstrip("\n")


def git_ok(*args: str) -> bool:
    return subprocess.run(
        ["git", *args], cwd=ROOT, capture_output=True, check=False
    ).returncode == 0


def lines(value: str) -> list[str]:
    return [] if not value else value.splitlines()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def write_tsv(path: Path, rows: Iterable[Iterable[str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        csv.writer(handle, delimiter="\t", lineterminator="\n").writerows(rows)


def ref_path_exists(ref: str, path: str) -> bool:
    return git_ok("cat-file", "-e", f"{ref}:{path}")


def manifest_tool_names(manifest: dict[str, Any]) -> set[str]:
    names: set[str] = set()
    for stage in manifest.get("stages", []):
        for field in ("required_tools", "optional_tools", "tools_available"):
            names.update(stage.get(field, []) or [])
        for sub_stage in stage.get("sub_stages", []) or []:
            names.update(sub_stage.get("tools_available", []) or [])
    return names


def discover_tools() -> set[str]:
    from tools.tool_registry import registry

    registry.discover()
    return set(registry._tools)


def _candidate_status_rows(base: str = PUBLIC_BASE) -> list[list[str]]:
    rows: dict[str, list[str]] = {}
    for row in lines(git("diff", "--name-status", "-M", base)):
        fields = row.split("\t")
        if fields[0].startswith(("R", "C")):
            rows[fields[2]] = [fields[0], fields[2], fields[1]]
        else:
            rows[fields[1]] = [fields[0], fields[1], "-"]
    for path in lines(git("ls-files", "--others", "--exclude-standard")):
        rows[path] = ["A", path, "-"]
    return [rows[path] for path in sorted(rows)]


def audit_lineage() -> dict[str, Any]:
    config = json.loads(
        (ROOT / "config/openmontage.sync.json").read_text(encoding="utf-8")
    )
    source_commit = config["golden_key_core_source_commit"]
    return {
        "public_base": PUBLIC_BASE,
        "public_base_commit": git("rev-parse", PUBLIC_BASE),
        "head_commit": git("rev-parse", "HEAD"),
        "public_base_is_head_ancestor": git_ok(
            "merge-base", "--is-ancestor", PUBLIC_BASE, "HEAD"
        ),
        "private_core_source_commit": source_commit,
        "private_core_source_is_head_ancestor": git_ok(
            "merge-base", "--is-ancestor", source_commit, "HEAD"
        ),
        "official_direct_sync_allowed": config["official_direct_sync_allowed"],
        "private_git_ancestry_merge_allowed": config[
            "private_git_ancestry_merge_allowed"
        ],
        "golden_key_core_main_merge_allowed": config[
            "golden_key_core_main_merge_allowed"
        ],
    }


def audit_pipelines() -> dict[str, Any]:
    config = json.loads(
        (ROOT / "config/openmontage.sync.json").read_text(encoding="utf-8")
    )
    comparison_base = config["upstream_base_commit"]
    schema = json.loads(
        (ROOT / "schemas/pipelines/pipeline_manifest.schema.json").read_text(
            encoding="utf-8"
        )
    )
    registered_tools = discover_tools()
    results: dict[str, Any] = {}
    all_pipeline_skills: set[str] = set()
    all_tool_refs: set[str] = set()

    for pipeline in PIPELINES:
        manifest_path = f"pipeline_defs/{pipeline}.yaml"
        manifest = yaml.safe_load((ROOT / manifest_path).read_text(encoding="utf-8"))
        schema_errors = sorted(
            jsonschema.Draft202012Validator(schema).iter_errors(manifest),
            key=lambda error: list(error.absolute_path),
        )
        pipeline_skills = [
            skill
            for skill in manifest.get("required_skills", [])
            if skill.startswith(f"pipelines/{pipeline}/")
        ]
        all_pipeline_skills.update(pipeline_skills)
        stage_checks = []
        produced_artifacts: set[str] = set()
        for stage in manifest.get("stages", []):
            produced_artifacts.update(stage.get("produces", []) or [])
            skill_path = ROOT / f"skills/{stage['skill']}.md"
            stage_checks.append(
                {
                    "stage": stage["name"],
                    "skill": stage["skill"],
                    "skill_exists": skill_path.is_file(),
                    "checkpoint_required": stage.get("checkpoint_required") is True,
                    "human_approval_default": stage.get("human_approval_default"),
                    "review_focus_present": bool(stage.get("review_focus")),
                    "success_criteria_present": bool(stage.get("success_criteria")),
                }
            )
        artifact_schema_checks = {
            artifact: (ROOT / f"schemas/artifacts/{artifact}.schema.json").is_file()
            for artifact in sorted(produced_artifacts)
        }
        tool_refs = manifest_tool_names(manifest)
        all_tool_refs.update(tool_refs)
        results[pipeline] = {
            "manifest_path": manifest_path,
            "manifest_version": manifest.get("version"),
            "manifest_absent_from_locked_upstream": not ref_path_exists(
                comparison_base, manifest_path
            ),
            "schema_valid": not schema_errors,
            "schema_errors": [error.message for error in schema_errors],
            "default_checkpoint_policy": manifest.get("default_checkpoint_policy"),
            "reviewer_skill_declared": "meta/reviewer"
            in manifest.get("required_skills", []),
            "checkpoint_skill_declared": "meta/checkpoint-protocol"
            in manifest.get("required_skills", []),
            "pipeline_skill_count": len(pipeline_skills),
            "pipeline_skills": sorted(pipeline_skills),
            "stage_checks": stage_checks,
            "artifact_schema_checks": artifact_schema_checks,
            "tool_refs": sorted(tool_refs),
            "missing_tool_registry_refs": sorted(tool_refs - registered_tools),
        }

    contract_rows = []
    for row in lines(
        git("diff", "--name-status", comparison_base, "--", "tests/contracts")
    ):
        status, path = row.split("\t", 1)
        contract_rows.append({"status": status, "path": path})
    for path in lines(
        git("ls-files", "--others", "--exclude-standard", "tests/contracts")
    ):
        contract_rows.append({"status": "A", "path": path})

    return {
        "comparison_base_commit": comparison_base,
        "pipeline_count": len(results),
        "pipeline_skill_count": len(all_pipeline_skills),
        "registered_tool_count": len(registered_tools),
        "referenced_tool_count": len(all_tool_refs),
        "reviewer_skill_present": (ROOT / "skills/meta/reviewer.md").is_file(),
        "checkpoint_skill_present": (
            ROOT / "skills/meta/checkpoint-protocol.md"
        ).is_file(),
        "pipelines": results,
        "changed_contract_test_count": len(contract_rows),
        "added_contract_test_count": sum(
            row["status"] == "A" for row in contract_rows
        ),
        "changed_contract_tests": contract_rows,
    }


def runtime_isolation_scan() -> dict[str, Any]:
    config = json.loads(
        (ROOT / "config/openmontage.sync.json").read_text(encoding="utf-8")
    )
    runtime_files: list[Path] = []
    for root_name in ADAPTER_RUNTIME_ROOTS:
        root = ROOT / root_name
        if root.is_file() and root.suffix.lower() in RUNTIME_SUFFIXES:
            runtime_files.append(root)
        elif root.is_dir():
            runtime_files.extend(
                path
                for path in root.rglob("*")
                if path.is_file()
                and path.suffix.lower() in RUNTIME_SUFFIXES
                and "__pycache__" not in path.parts
            )

    hits: list[dict[str, Any]] = []
    forbidden_modules = (
        "model_driven_agent_host",
        "openai_compatible_transport",
        "agent_host_authority",
        "golden_key_short_video_agent",
        "saas_worker",
    )
    for path in runtime_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        relative = path.relative_to(ROOT).as_posix()
        if path.suffix.lower() == ".py":
            try:
                tree = ast.parse(text, filename=relative)
            except SyntaxError:
                hits.append(
                    {"category": "unparseable_python", "path": relative, "line": 1}
                )
                continue
            imported: list[tuple[str, int]] = []
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    imported.extend((alias.name, node.lineno) for alias in node.names)
                elif isinstance(node, ast.ImportFrom):
                    module = node.module or ""
                    imported.extend(
                        (f"{module}.{alias.name}".strip("."), node.lineno)
                        for alias in node.names
                    )
            for module, line_number in imported:
                if any(name in module.lower() for name in forbidden_modules):
                    hits.append(
                        {
                            "category": "forbidden_runtime_import",
                            "path": relative,
                            "line": line_number,
                        }
                    )

    entrypoint_files = [
        path
        for path in runtime_files
        if path.relative_to(ROOT).parts[0] in ADAPTER_ENTRYPOINT_ROOTS
    ]
    forbidden_absent = {
        path: not (ROOT / path).exists() for path in FORBIDDEN_CORE_PATHS
    }
    authority = {
        "invocation_model": config["authority"]["invocation_model"],
        "nested_agent_host_allowed": config["authority"][
            "nested_agent_host_allowed"
        ],
    }
    return {
        "authority": authority,
        "adapter_runtime_roots": list(ADAPTER_RUNTIME_ROOTS),
        "runtime_file_count": len(runtime_files),
        "adapter_entrypoint_file_count": len(entrypoint_files),
        "forbidden_reference_hits": hits,
        "forbidden_core_paths_absent": forbidden_absent,
        "static_result": (
            "fail"
            if hits or not all(forbidden_absent.values())
            else ("pass" if entrypoint_files else "not_yet_applicable")
        ),
        "dynamic_network_block_test": (
            "planned_not_executable_until_adapter_entrypoint_exists"
            if not entrypoint_files
            else "required_in_w3"
        ),
    }


def audit_release_bundle(zip_path: Path, lock_path: Path) -> dict[str, Any]:
    config = json.loads(
        (ROOT / "config/openmontage.sync.json").read_text(encoding="utf-8")
    )
    bundle = sync_workbuddy_core.verify_bundle(
        zip_path=zip_path,
        lock_path=lock_path,
        expected_zip_sha256=config["golden_key_core_zip_sha256"],
        expected_contract_id=config["golden_key_core_contract_id"],
        expected_source_ref=config["golden_key_core_tag"],
        expected_source_commit=config["golden_key_core_source_commit"],
    )
    configured = sync_workbuddy_core.validate_configured_bundle(
        bundle=bundle, lock_path=lock_path, config=config
    )
    destination = sync_workbuddy_core.verify_destination(bundle, ROOT)
    return {
        "release_url": config["golden_key_core_release_url"],
        "zip_asset": config["golden_key_core_zip_asset"],
        "zip_sha256": config["golden_key_core_zip_sha256"],
        "lock_asset": config["golden_key_core_lock_asset"],
        "lock_sha256": configured["lock_sha256"],
        "contract_id": bundle.lock["contract_id"],
        "source_ref": bundle.lock["source_ref"],
        "source_commit": bundle.lock["source_commit"],
        "bundle_sha256": bundle.lock["bundle_sha256"],
        "authority": bundle.lock["authority"],
        "destination": destination,
        "consumer_remove_paths": bundle.lock["managed_scope"][
            "consumer_remove_paths"
        ],
        "forbidden_paths": bundle.lock["managed_scope"]["forbidden_paths"],
        "verified": True,
    }


PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("private_key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("openai_style_key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("github_token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b")),
    ("github_pat", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b")),
    ("aws_access_key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("slack_token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")),
    (
        "credential_assignment",
        re.compile(
            r"(?i)\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|"
            r"password|secret)\b\s*[:=]\s*[\"'][^\"'\r\n]{8,}[\"']"
        ),
    ),
    ("windows_user_path", re.compile(r"(?i)\bC:\\Users\\[^\\\s]+")),
    ("workspace_private_path", re.compile(r"(?i)\bD:\\BlazingCD\\[^\s\"']+")),
    ("named_case_a", re.compile(r"(?i)\b" + "hai" + "tao\b|海" + "涛")),
    ("named_case_b", re.compile(r"(?i)\bhead[- ]spa\b|头" + "疗")),
    ("named_case_c", re.compile(r"(?i)\bga" + "ga\b")),
    (
        "customer_signal",
        re.compile(r"(?i)" + "com" + r"ment(?:-| )666|评论.{0,8}" + "666"),
    ),
)


def publication_risk_scan() -> dict[str, Any]:
    rows = _candidate_status_rows()
    paths = [row[1] for row in rows if not row[0].startswith("D")]
    hits: list[dict[str, Any]] = []
    binary_or_non_utf8: list[str] = []
    for relative in paths:
        path = ROOT / relative
        if not path.is_file():
            continue
        data = path.read_bytes()
        if b"\x00" in data:
            binary_or_non_utf8.append(relative)
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            binary_or_non_utf8.append(relative)
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            for category, pattern in PATTERNS:
                for match in pattern.finditer(line):
                    value = match.group(0)
                    hits.append(
                        {
                            "category": category,
                            "path": relative,
                            "line": line_number,
                            "fingerprint": hashlib.sha256(
                                value.encode("utf-8")
                            ).hexdigest()[:16],
                        }
                    )
    asset_extensions = {
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".svg",
        ".webp",
        ".mp3",
        ".wav",
        ".mp4",
        ".mov",
        ".ttf",
        ".otf",
        ".woff",
        ".woff2",
    }
    return {
        "scope": "public origin/main to current WorkBuddy candidate tree only",
        "private_core_history_scanned": False,
        "candidate_file_count": len(rows),
        "status_counts": dict(Counter(row[0] for row in rows)),
        "pattern_hit_counts": dict(Counter(hit["category"] for hit in hits)),
        "pattern_hits_redacted": hits,
        "binary_or_non_utf8_paths": binary_or_non_utf8,
        "asset_or_font_paths": [
            path for path in paths if Path(path).suffix.lower() in asset_extensions
        ],
        "dependency_manifest_paths": [
            path
            for path in paths
            if Path(path).name
            in {
                "requirements.txt",
                "setup.py",
                "pyproject.toml",
                "package.json",
                "package-lock.json",
                "pnpm-lock.yaml",
                "yarn.lock",
            }
        ],
    }


def candidate_inventory() -> dict[str, Any]:
    rows = _candidate_status_rows()
    digest = hashlib.sha256()
    for status, path, old_path in rows:
        digest.update(f"{status}\0{path}\0{old_path}\0".encode("utf-8"))
        candidate = ROOT / path
        if candidate.is_file():
            digest.update(hashlib.sha256(candidate.read_bytes()).digest())
    return {
        "base": PUBLIC_BASE,
        "base_commit": git("rev-parse", PUBLIC_BASE),
        "head_commit_before_candidate_commit": git("rev-parse", "HEAD"),
        "candidate_file_count": len(rows),
        "status_counts": dict(Counter(row[0] for row in rows)),
        "candidate_snapshot_sha256": digest.hexdigest(),
        "rows": rows,
    }


def run_regressions(output_root: Path) -> dict[str, Any]:
    del output_root
    python = Path(sys.executable)
    suites = (
        ("contracts", "tests/contracts"),
        ("tools", "tests/tools"),
        ("workbuddy", "tests/workbuddy"),
    )
    results = []
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    d_temp = Path(os.environ.get("WORKBUDDY_AUDIT_TEMP_ROOT", "D:/WorkBuddyData/Temp"))
    d_temp.mkdir(parents=True, exist_ok=True)
    runtime_root = Path(
        tempfile.mkdtemp(prefix="workbuddy-w0-v0321-regression-", dir=d_temp)
    )
    try:
        pycache = runtime_root / "pycache"
        pycache.mkdir(parents=True, exist_ok=True)
        env["PYTHONPYCACHEPREFIX"] = str(pycache)
        for name, test_path in suites:
            base_temp = runtime_root / f"pytest-{name}"
            command = [
                str(python),
                "-m",
                "pytest",
                test_path,
                "-q",
                "--disable-warnings",
                "--maxfail=1",
                "-p",
                "no:cacheprovider",
                "--basetemp",
                str(base_temp),
            ]
            started = time.monotonic()
            completed = subprocess.run(
                command,
                cwd=ROOT,
                env=env,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                check=False,
            )
            output = "\n".join(
                part.strip()
                for part in (completed.stdout, completed.stderr)
                if part.strip()
            )
            results.append(
                {
                    "name": name,
                    "test_path": test_path,
                    "returncode": completed.returncode,
                    "duration_seconds": round(time.monotonic() - started, 3),
                    "output_tail": output.splitlines()[-20:],
                }
            )
            if completed.returncode:
                break
    finally:
        shutil.rmtree(runtime_root)
    return {
        "provider_calls_allowed": False,
        "temporary_runtime_on_d_drive": True,
        "temporary_runtime_removed": not runtime_root.exists(),
        "suites": results,
        "overall_pass": len(results) == len(suites)
        and all(result["returncode"] == 0 for result in results),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip", required=True, type=Path)
    parser.add_argument("--lock", required=True, type=Path)
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("docs/workbuddy/audits/evidence-v0.3.21-2026-08-05"),
    )
    parser.add_argument("--run-tests", action="store_true")
    args = parser.parse_args()
    output_dir = args.output_dir
    if not output_dir.is_absolute():
        output_dir = ROOT / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        release = audit_release_bundle(args.zip, args.lock)
        pipeline = audit_pipelines()
        runtime = runtime_isolation_scan()
        lineage = audit_lineage()
        regressions = (
            run_regressions(output_dir)
            if args.run_tests
            else {"overall_pass": False, "not_run": True, "suites": []}
        )
        risk = publication_risk_scan()
        inventory = candidate_inventory()
    except (RuntimeError, OSError, sync_workbuddy_core.SyncContractError) as exc:
        print(json.dumps({"gate": "FAIL", "error": str(exc)}, ensure_ascii=False))
        return 2

    pipeline_pass = (
        pipeline["pipeline_count"] == 4
        and pipeline["pipeline_skill_count"] == 44
        and pipeline["changed_contract_test_count"] == 10
        and pipeline["added_contract_test_count"] == 8
        and pipeline["reviewer_skill_present"]
        and pipeline["checkpoint_skill_present"]
        and all(
            item["schema_valid"]
            and item["pipeline_skill_count"] == 11
            and item["reviewer_skill_declared"]
            and item["checkpoint_skill_declared"]
            and not item["missing_tool_registry_refs"]
            and all(item["artifact_schema_checks"].values())
            and all(stage["skill_exists"] for stage in item["stage_checks"])
            for item in pipeline["pipelines"].values()
        )
    )
    runtime_pass = (
        runtime["authority"]
        == {"invocation_model": "direct_agent", "nested_agent_host_allowed": False}
        and not runtime["forbidden_reference_hits"]
        and all(runtime["forbidden_core_paths_absent"].values())
    )
    lineage_pass = (
        lineage["public_base_is_head_ancestor"]
        and not lineage["private_core_source_is_head_ancestor"]
        and not lineage["official_direct_sync_allowed"]
        and not lineage["private_git_ancestry_merge_allowed"]
        and not lineage["golden_key_core_main_merge_allowed"]
    )
    risk_pass = not risk["pattern_hits_redacted"]
    gate = (
        "PASS"
        if release["verified"]
        and pipeline_pass
        and runtime_pass
        and lineage_pass
        and risk_pass
        and regressions["overall_pass"]
        else "FAIL"
    )
    summary = {
        "gate": gate,
        "release_contract_pass": release["verified"],
        "pipeline_contract_pass": pipeline_pass,
        "runtime_boundary_pass": runtime_pass,
        "public_lineage_pass": lineage_pass,
        "publication_risk_scan_pass": risk_pass,
        "regression_pass": regressions["overall_pass"],
        "verified_core_file_count": release["destination"]["verified_file_count"],
        "candidate_file_count": inventory["candidate_file_count"],
        "candidate_snapshot_sha256": inventory["candidate_snapshot_sha256"],
        "private_core_history_scanned": False,
        "private_core_history_in_candidate": False,
    }

    write_json(output_dir / "release-contract.json", release)
    write_json(output_dir / "pipeline-integrity.json", pipeline)
    write_json(output_dir / "runtime-isolation.json", runtime)
    write_json(output_dir / "lineage.json", lineage)
    write_json(output_dir / "publication-risk-scan.json", risk)
    write_json(output_dir / "regression-results.json", regressions)
    write_tsv(
        output_dir / "publication-candidate-files.tsv",
        [["status", "path", "old_path"], *inventory["rows"]],
    )
    write_json(output_dir / "candidate-inventory.json", inventory)
    write_json(output_dir / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if gate == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
