"""Contracts for the Golden Key product/service marketing pipeline."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from lib.checkpoint import (
    CheckpointValidationError,
    get_next_stage,
    init_project,
    write_checkpoint,
)
from lib.pipeline_loader import get_stage_order, load_pipeline
from schemas.artifacts import validate_artifact


ROOT = Path(__file__).resolve().parent.parent.parent
PIPELINE = "golden-key-product-marketing"
EXPECTED_STAGES = [
    "idea",
    "proposal",
    "script",
    "scene_plan",
    "assets",
    "edit",
    "compose",
    "publish",
]


def _stages(manifest: dict) -> dict[str, dict]:
    return {stage["name"]: stage for stage in manifest["stages"]}


def _brief() -> dict:
    return {
        "version": "1.0",
        "title": "下班以后，把时间慢下来",
        "hook": "下班以后，给自己留一点安静时间。",
        "key_points": [
            "Real store and service-process footage anchors the experience.",
            "The video invites consideration without unsupported effect claims.",
        ],
        "core_message": "A calm local wellness-studio experience can enter the weekend list.",
        "cta": "Save for a later weekend.",
        "tone": "warm, sensory, restrained",
        "style": "premium-minimalist",
        "target_audience": "Xiaohongshu users considering a local relaxation experience",
        "target_platform": "generic",
        "target_duration_seconds": 25,
        "reference_material": ["fixtures/wellness-studio"],
        "metadata": {
            "primary_goal": "product_or_service_interest",
            "marketed_object": {"type": "service", "name": "示例门店舒缓体验"},
            "marketing_fact_set_ref": "wellness-studio-facts@1#sha256:test",
            "platform_profile_ref": "xiaohongshu@2026.07.1#sha256:test",
            "material_intake_ref": "wellness-studio-intake@0.2#sha256:test",
            "material_query_ref": "wellness-studio-query@1#sha256:test",
            "audio_architecture": {
                "meaning_carrier": "narration",
                "bgm_role": "shape the busy-to-calm arc",
                "natural_sound_role": "retain selected service texture",
            },
        },
    }


def _valid_text_layer_edit() -> dict:
    return {
        "version": "1.0",
        "cuts": [],
        "render_runtime": "remotion",
        "subtitles": {
            "enabled": True,
            "source": "asset-caption-words",
            "style": "word-by-word",
        },
        "metadata": {
            "text_layer_direction": {
                "attention_policy": "continuous captions remain primary; no competing overlays",
                "layers": [
                    {
                        "layer_id": "captions",
                        "role": "continuous_caption",
                        "delivery": "subtitles",
                        "renderer": "subtitle_gen_remotion",
                        "reason": "Narration requires readable continuous captions.",
                    }
                ],
            }
        },
    }


def test_manifest_loads_and_matches_native_schema() -> None:
    manifest = load_pipeline(PIPELINE)
    schema = json.loads(
        (ROOT / "schemas" / "pipelines" / "pipeline_manifest.schema.json").read_text(
            encoding="utf-8"
        )
    )

    assert manifest["name"] == PIPELINE
    assert manifest["category"] == "custom"
    assert manifest["stability"] == "beta"
    assert get_stage_order(manifest) == EXPECTED_STAGES
    assert set(manifest) <= set(schema["properties"])
    assert "production_modes" not in manifest
    assert manifest["metadata"]["canonical_artifact_policy"] == "openmontage_only"


def test_manifest_closes_artifacts_skills_and_tools() -> None:
    manifest = load_pipeline(PIPELINE)
    produced: set[str] = set()

    for skill_ref in manifest["required_skills"]:
        assert (ROOT / "skills" / f"{skill_ref}.md").is_file(), skill_ref

    for stage in manifest["stages"]:
        assert not set(stage.get("required_artifacts_in", [])) - produced
        assert set(stage.get("required_tools", [])) <= set(stage["tools_available"])
        assert stage["review_focus"]
        assert stage["success_criteria"]
        produced.update(stage["produces"])

    stages = _stages(manifest)
    assert stages["proposal"]["produces"] == ["proposal_packet", "decision_log"]
    assert stages["scene_plan"]["produces"] == ["scene_plan"]
    assert stages["edit"]["produces"] == ["edit_decisions"]
    assert stages["compose"]["produces"] == ["render_report", "final_review"]


def test_pipeline_keeps_native_agent_and_reviewer_authority() -> None:
    manifest = load_pipeline(PIPELINE)
    skill_dir = ROOT / "skills" / "pipelines" / PIPELINE
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted(skill_dir.glob("*.md"))
    )

    for retired_contract in (
        "PlatformDirectorContext",
        "applied_platform_rule_ids",
        "openmontage-director",
        "DirectorStageRequest",
        "DirectorStageResult",
    ):
        assert retired_contract not in combined

    assert "meta/reviewer" in manifest["required_skills"]
    assert manifest["metadata"]["platform_profile_transport"] == "agent_input_reference"
    assert "execution_requirements" in manifest["metadata"]["required_decision_fields"]


def test_policy_requires_real_concept_diversity_and_conditional_i2v() -> None:
    skill_dir = ROOT / "skills" / "pipelines" / PIPELINE
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted(skill_dir.glob("*.md"))
    ).lower()

    for phrase in (
        "at least three",
        "fact",
        "benefit",
        "evidence",
        "source_in",
        "source_out",
        "negative prompt",
        "benchmark",
        "may be rejected",
        "separate openmontage project",
        "text_layer_direction",
    ):
        assert phrase in combined

    reviewer = (skill_dir / "reviewer-rubric.md").read_text(encoding="utf-8").lower()
    for critical in (
        "wrong route",
        "unsupported",
        "cosmetic variants",
        "exact `source_path`",
        "silent",
        "text-role collapse",
        "ending",
    ):
        assert critical in reviewer

    edit = (skill_dir / "edit-director.md").read_text(encoding="utf-8").lower()
    compose = (skill_dir / "compose-director.md").read_text(encoding="utf-8").lower()
    assert "metadata.ending_treatment" in edit
    assert "duration-0.1s" in compose
    assert "ending_closure" in compose


def test_duration_capability_order_and_full_run_approval_are_governed() -> None:
    skill_dir = ROOT / "skills" / "pipelines" / PIPELINE
    idea = (skill_dir / "idea-director.md").read_text(encoding="utf-8")
    policy = (skill_dir / "director-decision-policy.md").read_text(encoding="utf-8")
    reviewer = (skill_dir / "reviewer-rubric.md").read_text(encoding="utf-8")

    assert "duration_selection" in idea and "at least two" in idea
    assert "Decision Order (Binding)" in policy
    assert "vetoes immediate execution, not Director" in policy
    assert "Capability-driven creative collapse" in reviewer
    assert "approval_policy" in reviewer
    assert "OpenMontage Agent plans the differentiated portfolio" in policy
    assert "may not" in policy and "concept matrix" in policy

    stages = _stages(load_pipeline(PIPELINE))
    assert any("ending" in item.lower() for item in stages["edit"]["review_focus"])
    assert any("last-second" in item.lower() for item in stages["compose"]["review_focus"])


def test_pipeline_checkpoint_order_and_text_layer_fail_closed(tmp_path: Path) -> None:
    project_id = "product-marketing-smoke"
    init_project(
        project_id,
        title="Product Marketing Smoke",
        pipeline_type=PIPELINE,
        pipeline_dir=tmp_path,
    )
    assert get_next_stage(tmp_path, project_id, PIPELINE) == "idea"

    write_checkpoint(
        tmp_path,
        project_id,
        "idea",
        "completed",
        {"brief": _brief()},
        pipeline_type=PIPELINE,
        human_approved=True,
    )
    assert get_next_stage(tmp_path, project_id, PIPELINE) == "proposal"

    edit_decisions = _valid_text_layer_edit()
    validate_artifact("edit_decisions", edit_decisions)
    with pytest.raises(CheckpointValidationError, match="PREREQUISITE VIOLATION"):
        write_checkpoint(
            tmp_path,
            project_id,
            "edit",
            "completed",
            {"edit_decisions": edit_decisions},
            pipeline_type=PIPELINE,
        )
    assert get_next_stage(tmp_path, project_id, PIPELINE) == "proposal"


def test_wellness_studio_route_fixture_is_product_marketing_not_lead_conversion() -> None:
    fixture = yaml.safe_load(
        (ROOT / "tests" / "fixtures" / "golden_key_product_marketing_cases.yaml")
        .read_text(encoding="utf-8")
    )
    cases = {case["id"]: case for case in fixture["cases"]}

    wellness_studio = cases["wellness-studio-soft-seeding"]
    assert wellness_studio["expected"]["route"] == PIPELINE
    assert wellness_studio["expected"]["image_to_video"] == "director_decides"
    assert wellness_studio["expected"]["concept_count_min"] == 3
    assert "medical_effect_claim" in wellness_studio["expected"]["reject"]

    direct_booking = cases["wellness-studio-direct-booking-offer"]
    assert direct_booking["expected"]["route"] == "golden-key-lead-conversion"


def test_proposal_stage_review_is_schema_valid() -> None:
    from schemas.artifacts import validate_artifact

    validate_artifact(
        "review",
        {
            "version": "1.0",
            "stage": "proposal",
            "round": 1,
            "findings": [],
            "metadata": {"status": "pass"},
        },
    )


def test_final_review_schema_accepts_dedicated_ending_closure_evidence() -> None:
    from schemas.artifacts import validate_artifact

    validate_artifact(
        "final_review",
        {
            "version": "1.0",
            "output_path": "D:/renders/final.mp4",
            "status": "pass",
            "checks": {
                "technical_probe": {},
                "visual_spotcheck": {"frames_sampled": 4},
                "audio_spotcheck": {},
                "promise_preservation": {},
                "subtitle_check": {},
                "ending_closure": {
                    "status": "pass",
                    "strategy": "fade_to_black",
                    "last_text_clearance_passed": True,
                    "visual_release_passed": True,
                    "audio_release_passed": True,
                    "tail_evidence": ["tail-1000.jpg", "tail-500.jpg", "tail-100.jpg"],
                    "review_note": "The last second lands cleanly.",
                },
            },
            "issues_found": [],
            "recommended_action": "present_to_user",
        },
    )
