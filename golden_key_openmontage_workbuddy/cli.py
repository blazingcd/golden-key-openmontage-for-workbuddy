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
    return 2
