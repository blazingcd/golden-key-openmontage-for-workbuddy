from __future__ import annotations

import json
import socket
import subprocess
import sys
from pathlib import Path

from golden_key_openmontage_workbuddy.cli import main


ROOT = Path(__file__).resolve().parents[2]


def test_w1_gate_stays_lightweight_when_w2_runtime_dependencies_are_unavailable(
    tmp_path: Path,
) -> None:
    completed = subprocess.run(
        [
            sys.executable,
            "-S",
            "-m",
            "golden_key_openmontage_workbuddy",
            "gate",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(tmp_path / "WorkBuddyData"),
            "--json",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )

    assert completed.returncode == 0, completed.stderr
    assert json.loads(completed.stdout)["status"] == "pass"


def test_context_exposes_direct_agent_authority_without_selecting_a_pipeline(
    capsys,
) -> None:
    result = main(["context", "--repo-root", str(ROOT), "--json"])

    assert result == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["status"] == "pass"
    assert payload["authority"] == {
        "invocation_model": "direct_agent",
        "nested_agent_host_allowed": False,
        "pipeline_selection_actor": "workbuddy_agent",
    }
    assert payload["selected_pipeline"] is None
    assert payload["pipelines"] == [
        "golden-key-brand-company",
        "golden-key-lead-conversion",
        "golden-key-product-marketing",
        "golden-key-subject-ip",
    ]
    assert payload["provider_calls_attempted"] == 0


def test_pipelines_lists_manifest_contracts_without_ranking_or_selection(capsys) -> None:
    result = main(["pipelines", "--repo-root", str(ROOT), "--json"])

    assert result == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["status"] == "pass"
    assert payload["selection_performed"] is False
    assert [item["name"] for item in payload["pipelines"]] == [
        "golden-key-brand-company",
        "golden-key-lead-conversion",
        "golden-key-product-marketing",
        "golden-key-subject-ip",
    ]
    for pipeline in payload["pipelines"]:
        assert pipeline["stages"][0]["name"] == "idea"
        assert pipeline["stages"][0]["skill"].startswith("pipelines/golden-key-")
        assert isinstance(pipeline["stages"][0]["human_approval_default"], bool)
        assert pipeline["stages"][0]["produces"]
    assert payload["provider_calls_attempted"] == 0


def test_project_create_and_status_use_the_agent_selected_pipeline(
    tmp_path: Path, capsys
) -> None:
    data_root = tmp_path / "WorkBuddyData"
    create_result = main(
        [
            "project",
            "create",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "launch-film",
            "--title",
            "Launch Film",
            "--pipeline",
            "golden-key-product-marketing",
            "--json",
        ]
    )

    assert create_result == 0
    created = json.loads(capsys.readouterr().out)
    assert created["status"] == "pass"
    assert created["pipeline"] == "golden-key-product-marketing"
    assert created["pipeline_selected_by"] == "workbuddy_agent"
    assert created["created"] is True
    project_dir = data_root / "Projects" / "launch-film"
    marker = json.loads((project_dir / "project.json").read_text(encoding="utf-8"))
    assert marker["pipeline_type"] == "golden-key-product-marketing"

    status_result = main(
        [
            "project",
            "status",
            "--data-root",
            str(data_root),
            "--project-id",
            "launch-film",
            "--json",
        ]
    )

    assert status_result == 0
    status = json.loads(capsys.readouterr().out)
    assert status["status"] == "pass"
    assert status["pipeline"] == "golden-key-product-marketing"
    assert status["next_stage"] == "idea"
    assert status["latest_checkpoint"] is None
    assert status["provider_calls_attempted"] == 0


def test_artifact_validate_reads_only_from_the_project_artifact_directory(
    tmp_path: Path, capsys
) -> None:
    data_root = tmp_path / "WorkBuddyData"
    main(
        [
            "project",
            "create",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "brand-film",
            "--title",
            "Brand Film",
            "--pipeline",
            "golden-key-brand-company",
            "--json",
        ]
    )
    capsys.readouterr()
    artifact_path = data_root / "Projects" / "brand-film" / "artifacts" / "brief.json"
    artifact_path.write_text(
        json.dumps(
            {
                "version": "1.0",
                "title": "Brand Film",
                "hook": "A clear opening",
                "key_points": ["One verified point"],
                "tone": "clear",
                "style": "clean-professional",
                "target_platform": "generic",
                "target_duration_seconds": 30,
            }
        ),
        encoding="utf-8",
    )

    result = main(
        [
            "artifact",
            "validate",
            "--data-root",
            str(data_root),
            "--project-id",
            "brand-film",
            "--name",
            "brief",
            "--input",
            str(artifact_path),
            "--json",
        ]
    )

    assert result == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["status"] == "pass"
    assert payload["artifact_name"] == "brief"
    assert payload["schema_valid"] is True
    assert payload["provider_calls_attempted"] == 0


def test_checkpoint_submit_uses_native_schema_and_human_gate(
    tmp_path: Path, capsys
) -> None:
    data_root = tmp_path / "WorkBuddyData"
    main(
        [
            "project",
            "create",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "subject-film",
            "--title",
            "Subject Film",
            "--pipeline",
            "golden-key-subject-ip",
            "--json",
        ]
    )
    capsys.readouterr()
    project_dir = data_root / "Projects" / "subject-film"
    artifacts_path = project_dir / "artifacts" / "idea-checkpoint.json"
    artifacts_path.write_text(
        json.dumps(
                {
                    "brief": {
                    "version": "1.0",
                    "title": "Subject Film",
                    "hook": "A grounded opening",
                    "key_points": ["One verified insight"],
                    "tone": "clear",
                    "style": "clean-professional",
                    "target_platform": "generic",
                    "target_duration_seconds": 30,
                },
                "decision_log": {
                    "version": "1.0",
                    "project_id": "subject-film",
                    "decisions": [],
                },
            }
        ),
        encoding="utf-8",
    )

    result = main(
        [
            "checkpoint",
            "submit",
            "--data-root",
            str(data_root),
            "--project-id",
            "subject-film",
            "--stage",
            "idea",
            "--status",
            "awaiting_human",
            "--artifacts-file",
            str(artifacts_path),
            "--json",
        ]
    )

    assert result == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["status"] == "pass"
    assert payload["stage"] == "idea"
    assert payload["checkpoint_status"] == "awaiting_human"
    assert payload["human_approval_required"] is True
    checkpoint = json.loads(
        (project_dir / "checkpoint_idea.json").read_text(encoding="utf-8")
    )
    assert checkpoint["pipeline_type"] == "golden-key-subject-ip"
    assert checkpoint["artifacts"]["brief"]["title"] == "Subject Film"
    assert payload["provider_calls_attempted"] == 0


def test_project_id_path_traversal_is_rejected_before_writing(
    tmp_path: Path, capsys
) -> None:
    data_root = tmp_path / "WorkBuddyData"

    result = main(
        [
            "project",
            "create",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "../escape",
            "--title",
            "Escape",
            "--pipeline",
            "golden-key-brand-company",
            "--json",
        ]
    )

    assert result == 1
    payload = json.loads(capsys.readouterr().out)
    assert payload["status"] == "fail"
    assert "project_id" in payload["errors"][0]
    assert not (data_root / "escape").exists()
    assert payload["provider_calls_attempted"] == 0


def test_project_create_cannot_rebind_an_existing_project_pipeline(
    tmp_path: Path, capsys
) -> None:
    data_root = tmp_path / "WorkBuddyData"
    base_args = [
        "project",
        "create",
        "--repo-root",
        str(ROOT),
        "--data-root",
        str(data_root),
        "--project-id",
        "fixed-project",
        "--title",
        "Fixed Project",
    ]
    assert (
        main(base_args + ["--pipeline", "golden-key-brand-company", "--json"])
        == 0
    )
    capsys.readouterr()

    result = main(
        base_args + ["--pipeline", "golden-key-product-marketing", "--json"]
    )

    assert result == 1
    payload = json.loads(capsys.readouterr().out)
    assert "already bound" in payload["errors"][0]
    marker = json.loads(
        (
            data_root / "Projects" / "fixed-project" / "project.json"
        ).read_text(encoding="utf-8")
    )
    assert marker["pipeline_type"] == "golden-key-brand-company"


def test_checkpoint_completed_without_human_approval_is_rejected(
    tmp_path: Path, capsys
) -> None:
    data_root = tmp_path / "WorkBuddyData"
    main(
        [
            "project",
            "create",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "gated-project",
            "--title",
            "Gated Project",
            "--pipeline",
            "golden-key-lead-conversion",
            "--json",
        ]
    )
    capsys.readouterr()
    artifacts_file = (
        data_root
        / "Projects"
        / "gated-project"
        / "artifacts"
        / "idea-checkpoint.json"
    )
    artifacts_file.write_text(
        json.dumps(
            {
                "brief": {
                    "version": "1.0",
                    "title": "Gated Project",
                    "hook": "A grounded opening",
                    "key_points": ["One verified point"],
                    "tone": "clear",
                    "style": "clean-professional",
                    "target_platform": "generic",
                        "target_duration_seconds": 30,
                    },
                    "decision_log": {
                        "version": "1.0",
                        "project_id": "gated-project",
                        "decisions": [],
                    },
                }
        ),
        encoding="utf-8",
    )

    result = main(
        [
            "checkpoint",
            "submit",
            "--data-root",
            str(data_root),
            "--project-id",
            "gated-project",
            "--stage",
            "idea",
            "--status",
            "completed",
            "--artifacts-file",
            str(artifacts_file),
            "--json",
        ]
    )

    assert result == 1
    payload = json.loads(capsys.readouterr().out)
    assert "GATE VIOLATION" in payload["errors"][0]
    assert not (
        data_root / "Projects" / "gated-project" / "checkpoint_idea.json"
    ).exists()
    assert payload["provider_calls_attempted"] == 0


def test_artifact_file_outside_project_is_rejected(tmp_path: Path, capsys) -> None:
    data_root = tmp_path / "WorkBuddyData"
    main(
        [
            "project",
            "create",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "closed-project",
            "--title",
            "Closed Project",
            "--pipeline",
            "golden-key-brand-company",
            "--json",
        ]
    )
    capsys.readouterr()
    outside = tmp_path / "outside-brief.json"
    outside.write_text("{}", encoding="utf-8")

    result = main(
        [
            "artifact",
            "validate",
            "--data-root",
            str(data_root),
            "--project-id",
            "closed-project",
            "--name",
            "brief",
            "--input",
            str(outside),
            "--json",
        ]
    )

    assert result == 1
    payload = json.loads(capsys.readouterr().out)
    assert "outside the allowed project root" in payload["errors"][0]
    assert payload["provider_calls_attempted"] == 0


def test_w2_lifecycle_stays_offline_and_does_not_start_a_second_agent(
    tmp_path: Path, capsys, monkeypatch
) -> None:
    network_attempts: list[str] = []

    def reject_network(*args, **kwargs):
        network_attempts.append(repr(args))
        raise AssertionError("external network access is forbidden")

    monkeypatch.setattr(socket, "create_connection", reject_network)
    monkeypatch.setattr(socket.socket, "connect", reject_network)
    data_root = tmp_path / "WorkBuddyData"

    commands = [
        ["context", "--repo-root", str(ROOT), "--json"],
        ["pipelines", "--repo-root", str(ROOT), "--json"],
        [
            "project",
            "create",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "offline-project",
            "--title",
            "Offline Project",
            "--pipeline",
            "golden-key-product-marketing",
            "--json",
        ],
        [
            "project",
            "status",
            "--data-root",
            str(data_root),
            "--project-id",
            "offline-project",
            "--json",
        ],
    ]
    for command in commands:
        assert main(command) == 0
        payload = json.loads(capsys.readouterr().out)
        assert payload["provider_calls_attempted"] == 0

    assert network_attempts == []


def test_stage_inspect_returns_the_native_next_stage_contract(
    tmp_path: Path, capsys
) -> None:
    data_root = tmp_path / "WorkBuddyData"
    main(
        [
            "project",
            "create",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "stage-project",
            "--title",
            "Stage Project",
            "--pipeline",
            "golden-key-product-marketing",
            "--json",
        ]
    )
    capsys.readouterr()

    result = main(
        [
            "stage",
            "inspect",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "stage-project",
            "--json",
        ]
    )

    assert result == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["status"] == "pass"
    assert payload["stage"] == "idea"
    assert payload["pipeline"] == "golden-key-product-marketing"
    assert payload["skill"].endswith(
        "skills/pipelines/golden-key-product-marketing/idea-director.md"
    )
    assert Path(payload["skill"]).is_file()
    assert payload["produces"] == ["brief", "decision_log"]
    assert payload["tools_available"] == []
    assert payload["human_approval_default"] is True
    assert payload["selection_performed"] is False


def test_checkpoint_submit_requires_every_manifest_produced_artifact(
    tmp_path: Path, capsys
) -> None:
    data_root = tmp_path / "WorkBuddyData"
    main(
        [
            "project",
            "create",
            "--repo-root",
            str(ROOT),
            "--data-root",
            str(data_root),
            "--project-id",
            "complete-contract",
            "--title",
            "Complete Contract",
            "--pipeline",
            "golden-key-product-marketing",
            "--json",
        ]
    )
    capsys.readouterr()
    artifact_file = (
        data_root
        / "Projects"
        / "complete-contract"
        / "artifacts"
        / "idea-checkpoint.json"
    )
    artifact_file.write_text(
        json.dumps(
            {
                "brief": {
                    "version": "1.0",
                    "title": "Complete Contract",
                    "hook": "A grounded opening",
                    "key_points": ["One verified point"],
                    "tone": "clear",
                    "style": "clean-professional",
                    "target_platform": "generic",
                    "target_duration_seconds": 30,
                }
            }
        ),
        encoding="utf-8",
    )

    result = main(
        [
            "checkpoint",
            "submit",
            "--data-root",
            str(data_root),
            "--project-id",
            "complete-contract",
            "--stage",
            "idea",
            "--status",
            "awaiting_human",
            "--artifacts-file",
            str(artifact_file),
            "--json",
        ]
    )

    assert result == 1
    payload = json.loads(capsys.readouterr().out)
    assert "missing manifest-produced artifacts: decision_log" in payload["errors"][0]
    assert not (
        data_root / "Projects" / "complete-contract" / "checkpoint_idea.json"
    ).exists()
