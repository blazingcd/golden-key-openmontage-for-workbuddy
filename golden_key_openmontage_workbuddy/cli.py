from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .doctor import build_doctor_report, format_doctor_report
from .gate import build_gate_report, format_gate_report
from .paths import default_data_root, default_repo_root
from .security import redact_payload, redact_text


def _print_json_report(report: dict) -> None:
    print(json.dumps(redact_payload(report), ensure_ascii=False, indent=2))


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="golden-key-workbuddy")
    subparsers = parser.add_subparsers(dest="command", required=True)

    doctor = subparsers.add_parser(
        "doctor", help="Check the local WorkBuddy callable-core environment."
    )
    doctor.add_argument("--repo-root", type=Path, default=default_repo_root())
    doctor.add_argument("--data-root", type=Path, default=default_data_root())
    doctor.add_argument(
        "--create-dirs",
        action="store_true",
        help="Create the declared WorkBuddy data directories under --data-root.",
    )
    doctor.add_argument("--json", action="store_true", dest="as_json")

    gate = subparsers.add_parser(
        "gate", help="Run the fail-closed W1 callable-core and adapter boundary Gate."
    )
    gate.add_argument("--repo-root", type=Path, default=default_repo_root())
    gate.add_argument("--data-root", type=Path, default=default_data_root())
    gate.add_argument("--json", action="store_true", dest="as_json")

    context = subparsers.add_parser(
        "context", help="Read the authoritative direct-agent WorkBuddy context."
    )
    context.add_argument("--repo-root", type=Path, default=default_repo_root())
    context.add_argument("--json", action="store_true", dest="as_json")

    pipelines = subparsers.add_parser(
        "pipelines", help="List callable Pipeline contracts without selecting one."
    )
    pipelines.add_argument("--repo-root", type=Path, default=default_repo_root())
    pipelines.add_argument("--json", action="store_true", dest="as_json")

    project = subparsers.add_parser(
        "project", help="Create or inspect a D-drive WorkBuddy project."
    )
    project_commands = project.add_subparsers(dest="project_command", required=True)
    project_create = project_commands.add_parser("create")
    project_create.add_argument("--repo-root", type=Path, default=default_repo_root())
    project_create.add_argument(
        "--data-root", type=Path, default=default_data_root()
    )
    project_create.add_argument("--project-id", required=True)
    project_create.add_argument("--title", required=True)
    project_create.add_argument("--pipeline", required=True)
    project_create.add_argument("--json", action="store_true", dest="as_json")
    project_status = project_commands.add_parser("status")
    project_status.add_argument(
        "--data-root", type=Path, default=default_data_root()
    )
    project_status.add_argument("--project-id", required=True)
    project_status.add_argument("--json", action="store_true", dest="as_json")

    artifact = subparsers.add_parser(
        "artifact", help="Validate a canonical Artifact inside a WorkBuddy project."
    )
    artifact_commands = artifact.add_subparsers(dest="artifact_command", required=True)
    artifact_validate = artifact_commands.add_parser("validate")
    artifact_validate.add_argument(
        "--data-root", type=Path, default=default_data_root()
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
        "--data-root", type=Path, default=default_data_root()
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
    stage_inspect.add_argument("--repo-root", type=Path, default=default_repo_root())
    stage_inspect.add_argument(
        "--data-root", type=Path, default=default_data_root()
    )
    stage_inspect.add_argument("--project-id", required=True)
    stage_inspect.add_argument("--json", action="store_true", dest="as_json")

    tool = subparsers.add_parser(
        "tool", help="Discover or execute tools allowed by the current Stage."
    )
    tool_commands = tool.add_subparsers(dest="tool_command", required=True)
    tool_list = tool_commands.add_parser("list")
    tool_list.add_argument("--repo-root", type=Path, default=default_repo_root())
    tool_list.add_argument(
        "--data-root", type=Path, default=default_data_root()
    )
    tool_list.add_argument("--project-id", required=True)
    tool_list.add_argument("--json", action="store_true", dest="as_json")
    tool_execute = tool_commands.add_parser("execute")
    tool_execute.add_argument("--repo-root", type=Path, default=default_repo_root())
    tool_execute.add_argument(
        "--data-root", type=Path, default=default_data_root()
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

    config = subparsers.add_parser(
        "config", help="Inspect the model boundary or create a safe Provider template."
    )
    config_commands = config.add_subparsers(dest="config_command", required=True)
    config_inspect = config_commands.add_parser("inspect")
    config_inspect.add_argument("--repo-root", type=Path, default=default_repo_root())
    config_inspect.add_argument("--json", action="store_true", dest="as_json")
    config_template = config_commands.add_parser("template")
    config_template.add_argument("--repo-root", type=Path, default=default_repo_root())
    config_template.add_argument(
        "--data-root", type=Path, default=default_data_root()
    )
    config_template.add_argument("--json", action="store_true", dest="as_json")
    config_guide = config_commands.add_parser(
        "guide", help="Report API-key setup options and presence without returning values."
    )
    config_guide.add_argument("--repo-root", type=Path, default=default_repo_root())
    config_guide.add_argument("--data-root", type=Path, default=default_data_root())
    config_guide.add_argument("--json", action="store_true", dest="as_json")

    runtime = subparsers.add_parser(
        "runtime",
        help="Plan or prepare the data-scoped Python dependencies after consent.",
    )
    runtime_commands = runtime.add_subparsers(
        dest="runtime_command", required=True
    )
    runtime_plan = runtime_commands.add_parser("plan")
    runtime_plan.add_argument("--repo-root", type=Path, default=default_repo_root())
    runtime_plan.add_argument("--data-root", type=Path, default=default_data_root())
    runtime_plan.add_argument("--json", action="store_true", dest="as_json")
    runtime_prepare = runtime_commands.add_parser("prepare")
    runtime_prepare.add_argument(
        "--repo-root", type=Path, default=default_repo_root()
    )
    runtime_prepare.add_argument(
        "--data-root", type=Path, default=default_data_root()
    )
    runtime_prepare.add_argument(
        "--confirm-download",
        action="store_true",
        help="Confirm that Python packages may be downloaded into the data root.",
    )
    runtime_prepare.add_argument("--json", action="store_true", dest="as_json")

    task = subparsers.add_parser(
        "task", help="Persist and operate bounded local Tool tasks."
    )
    task_commands = task.add_subparsers(dest="task_command", required=True)
    task_submit = task_commands.add_parser("submit")
    task_submit.add_argument("--repo-root", type=Path, default=default_repo_root())
    task_submit.add_argument(
        "--data-root", type=Path, default=default_data_root()
    )
    task_submit.add_argument("--project-id", required=True)
    task_submit.add_argument("--name", required=True)
    task_submit.add_argument("--inputs-file", type=Path, required=True)
    task_submit.add_argument(
        "--ack-agent-skill", action="append", default=[]
    )
    task_submit.add_argument("--json", action="store_true", dest="as_json")
    task_status = task_commands.add_parser("status")
    task_status.add_argument(
        "--data-root", type=Path, default=default_data_root()
    )
    task_status.add_argument("--project-id", required=True)
    task_status.add_argument("--task-id", required=True)
    task_status.add_argument("--json", action="store_true", dest="as_json")
    task_cancel = task_commands.add_parser("cancel")
    task_cancel.add_argument(
        "--data-root", type=Path, default=default_data_root()
    )
    task_cancel.add_argument("--project-id", required=True)
    task_cancel.add_argument("--task-id", required=True)
    task_cancel.add_argument("--json", action="store_true", dest="as_json")
    task_run = task_commands.add_parser("run")
    task_run.add_argument("--repo-root", type=Path, default=default_repo_root())
    task_run.add_argument(
        "--data-root", type=Path, default=default_data_root()
    )
    task_run.add_argument("--project-id", required=True)
    task_run.add_argument("--task-id", required=True)
    task_run.add_argument("--timeout-seconds", type=float, default=3600.0)
    task_run.add_argument("--json", action="store_true", dest="as_json")
    task_recover = task_commands.add_parser("recover")
    task_recover.add_argument(
        "--data-root", type=Path, default=default_data_root()
    )
    task_recover.add_argument("--project-id", required=True)
    task_recover.add_argument("--task-id", required=True)
    task_recover.add_argument("--json", action="store_true", dest="as_json")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "doctor":
        report = build_doctor_report(
            args.repo_root, args.data_root, create_dirs=args.create_dirs
        )
        if args.as_json:
            _print_json_report(report)
        else:
            print(redact_text(format_doctor_report(report)))
        return 0 if report["status"] == "pass" else 1
    if args.command == "gate":
        report = build_gate_report(args.repo_root, args.data_root)
        if args.as_json:
            _print_json_report(report)
        else:
            print(redact_text(format_gate_report(report)))
        return 0 if report["status"] == "pass" else 1
    if args.command == "context":
        from .runtime import build_context_report

        report = build_context_report(args.repo_root)
        _print_json_report(report)
        return 0 if report["status"] == "pass" else 1
    if args.command == "pipelines":
        from .runtime import build_pipeline_catalog

        report = build_pipeline_catalog(args.repo_root)
        _print_json_report(report)
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
        _print_json_report(report)
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
        _print_json_report(report)
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
        _print_json_report(report)
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
        _print_json_report(report)
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
        _print_json_report(report)
        return 0 if report["status"] == "pass" else 1
    if args.command == "config":
        from .model_config import (
            ModelProviderConfigError,
            build_model_provider_report,
            build_provider_setup_guide,
            write_safe_provider_template,
        )

        try:
            if args.config_command == "inspect":
                report = build_model_provider_report(args.repo_root)
            elif args.config_command == "guide":
                report = build_provider_setup_guide(args.repo_root, args.data_root)
            else:
                report = write_safe_provider_template(args.repo_root, args.data_root)
        except ModelProviderConfigError as exc:
            report = {
                "status": "fail",
                "provider_calls_attempted": 0,
                "network_calls_attempted": 0,
                "errors": [str(exc)],
            }
        _print_json_report(report)
        return 0 if report["status"] == "pass" else 1
    if args.command == "runtime":
        from .runtime_prepare import build_runtime_plan, prepare_managed_runtime

        if args.runtime_command == "plan":
            report = build_runtime_plan(args.repo_root, args.data_root)
            success = report["status"] in {"ready", "needs_confirmation"}
        else:
            report = prepare_managed_runtime(
                args.repo_root,
                args.data_root,
                confirm_download=args.confirm_download,
            )
            success = report["status"] == "pass"
        _print_json_report(report)
        return 0 if success else 1
    if args.command == "task":
        from .runtime import RuntimeContractError
        from .tasks import (
            cancel_tool_task,
            get_tool_task_status,
            recover_interrupted_tool_task,
            run_tool_task,
            submit_tool_task,
        )

        try:
            if args.task_command == "submit":
                report = submit_tool_task(
                    args.repo_root,
                    args.data_root,
                    project_id=args.project_id,
                    tool_name=args.name,
                    inputs_file=args.inputs_file,
                    acknowledged_agent_skills=args.ack_agent_skill,
                )
            elif args.task_command == "status":
                report = get_tool_task_status(
                    args.data_root,
                    project_id=args.project_id,
                    task_id=args.task_id,
                )
            elif args.task_command == "cancel":
                report = cancel_tool_task(
                    args.data_root,
                    project_id=args.project_id,
                    task_id=args.task_id,
                )
            elif args.task_command == "run":
                report = run_tool_task(
                    args.repo_root,
                    args.data_root,
                    project_id=args.project_id,
                    task_id=args.task_id,
                    timeout_seconds=args.timeout_seconds,
                )
            else:
                report = recover_interrupted_tool_task(
                    args.data_root,
                    project_id=args.project_id,
                    task_id=args.task_id,
                )
        except RuntimeContractError as exc:
            report = {
                "status": "fail",
                "tool_calls_attempted": 0,
                "provider_calls_attempted": 0,
                "network_calls_attempted": 0,
                "errors": [str(exc)],
            }
        _print_json_report(report)
        return 0 if report["status"] == "pass" else 1
    return 2
