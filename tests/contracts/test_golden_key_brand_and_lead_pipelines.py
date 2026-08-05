"""Contracts for the Golden Key brand/company and lead-conversion pipelines."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from lib.pipeline_loader import get_stage_order, list_selectable_pipelines, load_pipeline


ROOT = Path(__file__).resolve().parent.parent.parent
PIPELINES = ("golden-key-brand-company", "golden-key-lead-conversion")
ALL_GOLDEN_KEY_PIPELINES = (
    "golden-key-subject-ip",
    "golden-key-product-marketing",
    "golden-key-brand-company",
    "golden-key-lead-conversion",
)
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


def _combined_skills(pipeline: str) -> str:
    skill_dir = ROOT / "skills" / "pipelines" / pipeline
    return "\n".join(
        path.read_text(encoding="utf-8") for path in sorted(skill_dir.glob("*.md"))
    )


@pytest.mark.parametrize("pipeline", ALL_GOLDEN_KEY_PIPELINES)
def test_pipeline_reuses_current_openmontage_direction_meta_skills(pipeline: str) -> None:
    manifest = load_pipeline(pipeline)
    required = set(manifest["required_skills"])
    assert {
        "meta/taste-direction",
        "meta/voice-performance-director",
        "meta/animation-runtime-selector",
        "meta/bespoke-composition",
        "meta/material-retrieval-boundary",
    } <= required

    combined = _combined_skills(pipeline)
    assert "taste_profile" in combined
    assert "voice_performance" in combined


@pytest.mark.parametrize("pipeline", ALL_GOLDEN_KEY_PIPELINES)
def test_content_performance_kernel_reaches_script_publish_and_reviewer(pipeline: str) -> None:
    skill_dir = ROOT / "skills" / "pipelines" / pipeline
    script = (skill_dir / "script-director.md").read_text(encoding="utf-8").lower()
    publish = (skill_dir / "publish-director.md").read_text(encoding="utf-8").lower()
    reviewer = (skill_dir / "reviewer-rubric.md").read_text(encoding="utf-8").lower()

    assert "viewer response architecture" in script
    assert "one primary viewer payoff" in script
    assert "every suspense" in script
    assert all(token in script for token in ("official", "ranking", "formula"))
    assert "one" in publish and "focus" in publish and "tags" in publish
    assert "at most one" in publish or "exactly one" in publish
    assert "content performance review" in reviewer
    assert all(token in reviewer for token in ("not", "official", "ranking", "formula"))
    assert "release gate" in reviewer


def test_agent_guide_applies_resolved_platform_profile_to_every_pipeline() -> None:
    guide = (ROOT / "AGENT_GUIDE.md").read_text(encoding="utf-8")

    assert "Resolved PlatformProfile contract" in guide
    assert "every selectable pipeline" in guide
    assert "Do not create a parallel" in guide
    assert "diagnostic proxies" in guide


def test_agent_guide_treats_external_handoff_as_fact_evidence_not_director() -> None:
    guide = (ROOT / "AGENT_GUIDE.md").read_text(encoding="utf-8")

    assert "External fact-only handoff" in guide
    assert "CustomerFactSet" in guide
    assert "SubjectFactsProfile" in guide
    assert "unranked full ready-library coverage" in guide
    assert "retrieval candidate, never a final select" in guide
    assert "do not adopt it as" in guide


@pytest.mark.parametrize("pipeline", PIPELINES)
def test_manifest_loads_as_complete_native_beta_pipeline(pipeline: str) -> None:
    manifest = load_pipeline(pipeline)
    schema = json.loads(
        (ROOT / "schemas" / "pipelines" / "pipeline_manifest.schema.json").read_text(
            encoding="utf-8"
        )
    )

    assert manifest["name"] == pipeline
    assert manifest["category"] == "custom"
    assert manifest["stability"] == "beta"
    assert get_stage_order(manifest) == EXPECTED_STAGES
    assert set(manifest) <= set(schema["properties"])
    assert manifest["metadata"]["canonical_artifact_policy"] == "openmontage_only"
    assert manifest["metadata"]["platform_profile_transport"] == "agent_input_reference"
    assert "production_modes" not in manifest


@pytest.mark.parametrize("pipeline", PIPELINES)
def test_manifest_closes_skills_artifacts_tools_and_gates(pipeline: str) -> None:
    manifest = load_pipeline(pipeline)
    produced: set[str] = set()

    assert len(manifest["required_skills"]) == 20
    for skill_ref in manifest["required_skills"]:
        assert (ROOT / "skills" / f"{skill_ref}.md").is_file(), skill_ref

    for stage in manifest["stages"]:
        assert not set(stage.get("required_artifacts_in", [])) - produced
        assert set(stage.get("required_tools", [])) <= set(stage["tools_available"])
        assert stage["review_focus"]
        assert stage["success_criteria"]
        produced.update(stage["produces"])

    assert produced == {
        "brief",
        "decision_log",
        "proposal_packet",
        "script",
        "scene_plan",
        "asset_manifest",
        "edit_decisions",
        "render_report",
        "final_review",
        "publish_log",
    }
    assert [s["human_approval_default"] for s in manifest["stages"]] == [
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        True,
    ]


@pytest.mark.parametrize("pipeline", ALL_GOLDEN_KEY_PIPELINES)
def test_material_selection_stays_with_openmontage_after_concept_selection(
    pipeline: str,
) -> None:
    manifest = load_pipeline(pipeline)
    skill_dir = ROOT / "skills" / "pipelines" / pipeline
    proposal = (skill_dir / "proposal-director.md").read_text(encoding="utf-8")
    scene = (skill_dir / "scene-director.md").read_text(encoding="utf-8")

    assert "meta/material-retrieval-boundary" in manifest["required_skills"]
    assert "Only after" in proposal or "After that winner" in proposal
    assert "OpenMontage Agent" in proposal and "shot_candidates" in proposal
    assert "exact_range_review" in scene
    assert "scene_plan" in scene


def test_all_four_custom_pipelines_are_selectable_and_file_complete() -> None:
    selectable = set(list_selectable_pipelines())
    custom = {
        "golden-key-subject-ip",
        "golden-key-product-marketing",
        "golden-key-brand-company",
        "golden-key-lead-conversion",
    }
    assert custom <= selectable
    assert len(selectable) == 16


@pytest.mark.parametrize("pipeline", PIPELINES)
def test_shared_governance_and_executable_timeline_contract(pipeline: str) -> None:
    combined = _combined_skills(pipeline).lower()
    for phrase in (
        "at least three",
        "separate openmontage project",
        "source_path",
        "source_in",
        "source_out",
        "negative prompt",
        "text_layer_direction",
        "duration_selection",
        "may be rejected",
        "duration-0.1s",
        "ending_closure",
    ):
        assert phrase in combined, (pipeline, phrase)

    for retired_contract in (
        "PlatformDirectorContext",
        "DirectorStageRequest",
        "DirectorStageResult",
        "openmontage-director",
    ):
        assert retired_contract not in _combined_skills(pipeline)


def test_brand_pipeline_has_distinct_brand_truth_and_memory_obligations() -> None:
    manifest = load_pipeline("golden-key-brand-company")
    combined = _combined_skills("golden-key-brand-company").lower()

    assert manifest["metadata"]["primary_goal"] == "brand_company_recognition_and_trust"
    for field in ("brand_thesis", "desired_association", "brand_evidence_map", "identity_system"):
        assert field in manifest["metadata"]["required_decision_fields"]
    for phrase in ("company proof", "brand music motif", "memory device", "generated premises"):
        assert phrase in combined


def test_lead_pipeline_has_distinct_offer_qualification_and_single_cta_obligations() -> None:
    manifest = load_pipeline("golden-key-lead-conversion")
    combined = _combined_skills("golden-key-lead-conversion").lower()

    assert manifest["metadata"]["primary_goal"] == "qualified_lead_action"
    for field in ("target_lead", "verified_offer", "qualification_conditions", "primary_cta"):
        assert field in manifest["metadata"]["required_decision_fields"]
    for phrase in ("one primary cta", "qualification", "offer mechanism", "fake urgency"):
        assert phrase in combined


def test_route_boundary_fixtures_cover_both_new_pipelines() -> None:
    brand_cases = yaml.safe_load(
        (ROOT / "tests" / "fixtures" / "golden_key_brand_company_cases.yaml").read_text(
            encoding="utf-8"
        )
    )["cases"]
    lead_cases = yaml.safe_load(
        (ROOT / "tests" / "fixtures" / "golden_key_lead_conversion_cases.yaml").read_text(
            encoding="utf-8"
        )
    )["cases"]

    assert {case["expected"]["route"] for case in brand_cases} == {
        "golden-key-brand-company",
        "golden-key-product-marketing",
        "golden-key-lead-conversion",
    }
    assert {case["expected"]["route"] for case in lead_cases} == {
        "golden-key-lead-conversion",
        "golden-key-product-marketing",
        "golden-key-subject-ip",
    }
