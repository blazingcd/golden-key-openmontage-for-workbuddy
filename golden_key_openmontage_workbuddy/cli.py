from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .doctor import build_doctor_report, format_doctor_report
from .gate import build_gate_report, format_gate_report


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="golden-key-workbuddy")
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor = subparsers.add_parser(
        "doctor", help="Check the local WorkBuddy callable-core environment."
    )
    doctor.add_argument("--repo-root", type=Path, default=Path.cwd())
    doctor.add_argument("--data-root", type=Path, default=Path("D:/WorkBuddyData"))
    doctor.add_argument(
        "--create-dirs",
        action="store_true",
        help="Create the declared WorkBuddy data directories under --data-root.",
    )
    doctor.add_argument("--json", action="store_true", dest="as_json")

    gate = subparsers.add_parser(
        "gate", help="Run the fail-closed W1 callable-core and adapter boundary Gate."
    )
    gate.add_argument("--repo-root", type=Path, default=Path.cwd())
    gate.add_argument("--data-root", type=Path, default=Path("D:/WorkBuddyData"))
    gate.add_argument("--json", action="store_true", dest="as_json")

    context = subparsers.add_parser(
        "context", help="Read the authoritative direct-agent WorkBuddy context."
    )
    context.add_argument("--repo-root", type=Path, default=Path.cwd())
    context.add_argument("--json", action="store_true", dest="as_json")

    pipelines = subparsers.add_parser(
        "pipelines", help="List callable Pipeline contracts without selecting one."
    )
    pipelines.add_argument("--repo-root", type=Path, default=Path.cwd())
    pipelines.add_argument("--json", action="store_true", dest="as_json")

    project = subparsers.add_parser(
        "project", help="Create or inspect a D-drive WorkBuddy project."
    )
    project_commands = project.add_subparsers(dest="project_command", required=True)
    project_create = project_commands.add_parser("create")
    project_create.add_argument("--repo-root", type=Path, default=Path.cwd())
    project_create.add_argument(
        "--data-root", type=Path, default=Path("D:/WorkBuddyData")
    )
    project_create.add_argument("--project-id", required=True)
    project_create.add_argument("--title", required=True)
    project_create.add_argument("--pipeline", required=True)
    project_create.add_argument("--json", action="store_true", dest="as_json")
    project_status = project_commands.add_parser("status")
    project_status.add_argument(
        "--data-root", type=Path, default=Path("D:/WorkBuddyData")
    )
    project_status.add_argument("--project-id", required=True)
    project_status.add_argument("--json", action="store_true", dest="as_json")

    artifact = subparsers.add_parser(
        "artifact", help="Validate a canonical Artifact inside a WorkBuddy project."
    )
    artifact_commands = artifact.add_subparsers(dest="artifact_command", required=True)
    artifact_validate = artifact_commands.add_parser("validate")
    artifact_validate.add_argument(
        "--data-root", type=Path, default=Path("D:/WorkBuddyData")
    )
    artifact_validate.add_argument("--project-id", required=True)
    artifact_validate.add_argument("--name", required=True)
    artifact_validate.add_argument("--input", type=Path, required=True)
    artifact_validate.add_argument("--json", action="store_true", dest="as_json")

    checkpoint = subparsers.add_parser(
        "checkpoint", help="Submit a native, schema-validated project Checkpoint."
    )
    checkpoint_commands = checkpoint.add_subparsers(
        dest="checkpoint_command", required=True
    )
    checkpoint_submit = checkpoint_commands.add_parser("submit")
    checkpoint_submit.add_argument(
        "--data-root", type=Path, default=Path("D:/WorkBuddyData")
    )
    checkpoint_submit.add_argument("--project-id", required=True)
    checkpoint_submit.add_argument("--stage", required=True)
    checkpoint_submit.add_argument(
        "--status",
        required=True,
        choices=("in_progress", "awaiting_human", "completed", "failed"),
    )
    checkpoint_submit.add_argument("--artifacts-file", type=Path, required=True)
    checkpoint_submit.add_argument("--human-approved", action="store_true")
    checkpoint_submit.add_argument("--json", action="store_true", dest="as_json")

    stage = subparsers.add_parser(
        "stage", help="Inspect the next native Stage contract for a project."
    )
    stage_commands = stage.add_subparsers(dest="stage_command", required=True)
    stage_inspect = stage_commands.add_parser("inspect")
    stage_inspect.add_argument("--repo-root", type=Path, default=Path.cwd())
    stage_inspect.add_argument(
        "--data-root", type=Path, default=Path("D:/WorkBuddyData")
    )
    stage_inspect.add_argument("--project-id", required=True)
    stage_inspect.add_argument("--json", action="store_true", dest="as_json")

    tool = subparsers.add_parser(
        "tool", help="Discover or execute tools allowed by the current Stage."
    )
    tool_commands = tool.add_subparsers(dest="tool_command", required=True)
    tool_list = tool_commands.add_parser("list")
    tool_list.add_argument("--repo-root", type=Path, default=Path.cwd())
    tool_list.add_argument(
        "--data-root", type=Path, default=Path("D:/WorkBuddyData")
    )
    tool_list.add_argument("--project-id", required=True)
    tool_list.add_argument("--json", action="store_true", dest="as_json")
    tool_execute = tool_commands.add_parser("execute")
    tool_execute.add_argument("--repo-root", type=Path, default=Path.cwd())
    tool_execute.add_argument(
        "--data-root", type=Path, default=Path("D:/WorkBuddyData")
    )
    tool_execute.add_argument("--project-id", required=True)
    tool_execute.add_argument("--name", required=True)
    tool_execute.add_argument("--inputs-file", type=Path, required=True)
    tool_execute.add_argument(
        "--ack-agent-skill",
        action="append",
        default=[],
        help="A Layer 3 Skill WorkBuddy read before invoking the tool (repeatable).",
    )
    tool_execute.add_argument("--json", action="store_true", dest="as_json")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "doctor":
        report = build_doctor_report(
            args.repo_root, args.data_root, create_dirs=args.create_dirs
        )
        if args.as_json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print(format_doctor_report(report))
        return 0 if report["status"] == "pass" else 1
    if args.command == "gate":
        report = build_gate_report(args.repo_root, args.data_root)
        if args.as_json:
            print(json.dumps(report, ensure_ascii=False, indent=2))
        else:
            print(format_gate_report(report))
        return 0 if report["status"] == "pass" else 1
    if args.command == "context":
        from .runtime import build_context_report

        report = build_context_report(args.repo_root)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["status"] == "pass" else 1
    if args.command == "pipelines":
        from .runtime import build_pipeline_catalog

        report = build_pipeline_catalog(args.repo_root)
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["status"] == "pass" else 1
    if args.command == "project":
        from .runtime import RuntimeContractError, build_project_status, create_project

        try:
            if args.project_command == "create":
                report = create_project(
                    args.repo_root,
                    args.data_root,
                    project_id=args.project_id,
                    title=args.title,
                    pipeline=args.pipeline,
                )
            else:
                report = build_project_status(
                    args.data_root, project_id=args.project_id
                )
        except RuntimeContractError as exc:
            report = {
                "status": "fail",
                "provider_calls_attempted": 0,
                "errors": [str(exc)],
            }
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["status"] == "pass" else 1
    if args.command == "artifact":
        from .runtime import RuntimeContractError, validate_project_artifact

        try:
            report = validate_project_artifact(
                args.data_root,
                project_id=args.project_id,
                artifact_name=args.name,
                input_path=args.input,
            )
        except RuntimeContractError as exc:
            report = {
                "status": "fail",
                "provider_calls_attempted": 0,
                "errors": [str(exc)],
            }
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["status"] == "pass" else 1
    if args.command == "checkpoint":
        from .runtime import RuntimeContractError, submit_checkpoint

        try:
            report = submit_checkpoint(
                args.data_root,
                project_id=args.project_id,
                stage=args.stage,
                checkpoint_status=args.status,
                artifacts_file=args.artifacts_file,
                human_approved=args.human_approved,
            )
        except RuntimeContractError as exc:
            report = {
                "status": "fail",
                "provider_calls_attempted": 0,
                "errors": [str(exc)],
            }
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["status"] == "pass" else 1
    if args.command == "stage":
        from .runtime import RuntimeContractError, inspect_current_stage

        try:
            report = inspect_current_stage(
                args.repo_root, args.data_root, project_id=args.project_id
            )
        except RuntimeContractError as exc:
            report = {
                "status": "fail",
                "provider_calls_attempted": 0,
                "errors": [str(exc)],
            }
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["status"] == "pass" else 1
    if args.command == "tool":
        from .runtime import (
            RuntimeContractError,
            build_stage_tool_catalog,
            execute_stage_tool,
        )

        try:
            if args.tool_command == "list":
                report = build_stage_tool_catalog(
                    args.repo_root, args.data_root, project_id=args.project_id
                )
            else:
                report = execute_stage_tool(
                    args.repo_root,
                    args.data_root,
                    project_id=args.project_id,
                    tool_name=args.name,
                    inputs_file=args.inputs_file,
                    acknowledged_agent_skills=args.ack_agent_skill,
                )
        except RuntimeContractError as exc:
            report = {
                "status": "fail",
                "tool_calls_attempted": 0,
                "provider_calls_attempted": 0,
                "errors": [str(exc)],
            }
        print(json.dumps(report, ensure_ascii=False, indent=2))
        return 0 if report["status"] == "pass" else 1
    return 2
