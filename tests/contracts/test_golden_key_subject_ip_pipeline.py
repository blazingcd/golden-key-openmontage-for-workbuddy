"""Contracts for the Golden Key subject-IP OpenMontage pipeline."""

from __future__ import annotations

import json
from pathlib import Path

import yaml

from lib.checkpoint import get_next_stage, init_project, read_checkpoint, write_checkpoint
from lib.pipeline_loader import (
    get_stage_order,
    get_stage_sub_stages,
    load_pipeline,
    pipeline_supports_reference_input,
)


ROOT = Path(__file__).resolve().parent.parent.parent
PIPELINE_NAME = "golden-key-subject-ip"
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
DOCUMENTED_PIPELINES = [
    "animated-explainer",
    "talking-head",
    "screen-demo",
    "clip-factory",
    "podcast-repurpose",
    "cinematic",
    "animation",
    "character-animation",
    "hybrid",
    "avatar-spokesperson",
    "localization-dub",
    "framework-smoke",
]


def _stages_by_name(manifest: dict) -> dict[str, dict]:
    return {stage["name"]: stage for stage in manifest["stages"]}


def _minimal_subject_brief() -> dict:
    return {
        "version": "1.0",
        "title": "示例宠物回家",
        "hook": "同一个呼唤，两次完全不同的回家反应。",
        "key_points": [
            "The sample pet is the recurring subject.",
            "Contrasting returns reveal a recognizable personality pattern.",
        ],
        "core_message": "Familiar rituals make a subject memorable.",
        "cta": "Follow the sample pet's next homecoming.",
        "tone": "warm, playful, emotionally observant",
        "style": "flat-motion-graphics",
        "target_audience": "Xiaohongshu users who enjoy real pet stories",
        "target_platform": "generic",
        "target_duration_seconds": 30,
        "reference_material": ["fixtures/sample-pet"],
        "metadata": {
            "primary_goal": "subject_affinity",
            "distribution_platform": "xiaohongshu",
            "platform_profile_ref": "xiaohongshu@2026.07.1",
            "subject_facts_profile_ref": "sample-pet@2026.07.2#sha256:test",
            "subject_dossier_projection": {
                "subject_type": "animal",
                "verified_facts": ["The sample pet is a cat"],
                "identity_anchors": ["source-footage appearance and movement"],
            },
            "audio_architecture": {
                "meaning_carrier": "narration_and_expressive_captions",
                "bgm_role": "shape the playful-to-warm emotional arc",
                "natural_sound_role": "retain recognizable homecoming ambience",
            },
        },
    }


def test_manifest_loads_with_native_stage_order():
    manifest = load_pipeline(PIPELINE_NAME)

    assert manifest["name"] == PIPELINE_NAME
    assert manifest["category"] == "custom"
    assert manifest["stability"] == "beta"
    assert get_stage_order(manifest) == EXPECTED_STAGES
    assert manifest["metadata"]["canonical_artifact_policy"] == "openmontage_only"


def test_manifest_matches_the_documented_pipeline_format_without_copying_upstream_exceptions():
    """Compare against all 12 documented manifests, then enforce the native schema."""
    defs_dir = ROOT / "pipeline_defs"
    schema = json.loads(
        (ROOT / "schemas" / "pipelines" / "pipeline_manifest.schema.json").read_text(
            encoding="utf-8"
        )
    )
    common_production_keys = {
        "name",
        "version",
        "description",
        "category",
        "stability",
        "default_checkpoint_policy",
        "stages",
    }

    for pipeline_name in DOCUMENTED_PIPELINES:
        path = defs_dir / f"{pipeline_name}.yaml"
        assert path.is_file(), f"Missing documented pipeline: {pipeline_name}"
        baseline = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert common_production_keys <= baseline.keys()
        assert isinstance(baseline["stages"], list) and baseline["stages"]

    manifest = load_pipeline(PIPELINE_NAME)
    assert common_production_keys <= manifest.keys()
    assert set(manifest) <= set(schema["properties"])
    assert "production_modes" not in manifest

    for stage in manifest["stages"]:
        assert {
            "name",
            "skill",
            "produces",
            "tools_available",
            "checkpoint_required",
            "human_approval_default",
            "review_focus",
            "success_criteria",
        } <= stage.keys()
        assert stage["review_focus"] and stage["success_criteria"]
        assert set(stage.get("required_tools", [])) <= set(stage["tools_available"])
        assert not (
            set(stage.get("required_artifacts_in", []))
            & set(stage.get("optional_artifacts_in", []))
        )


def test_artifact_dependencies_and_orchestration_references_are_closed():
    manifest = load_pipeline(PIPELINE_NAME)
    produced: set[str] = set()

    assert manifest["orchestration"]["skill"] in manifest["required_skills"]
    for stage in manifest["stages"]:
        missing = set(stage.get("required_artifacts_in", [])) - produced
        assert not missing, f"{stage['name']} requires artifacts not produced earlier: {missing}"
        produced.update(stage.get("produces", []))


def test_reference_input_activates_the_native_sample_substage():
    manifest = load_pipeline(PIPELINE_NAME)

    assert pipeline_supports_reference_input(manifest) is True
    assert "proposal.sample" in get_stage_order(manifest, include_sub_stages=True)
    active = get_stage_sub_stages(
        manifest,
        "proposal",
        context={"video_analysis_brief_exists": True},
        include_inactive=False,
    )
    assert [substage["name"] for substage in active] == ["sample"]


def test_manifest_preserves_canonical_artifact_chain_and_gates():
    manifest = load_pipeline(PIPELINE_NAME)
    stages = _stages_by_name(manifest)

    assert stages["idea"]["produces"] == ["brief", "decision_log"]
    assert stages["proposal"]["required_artifacts_in"] == ["brief"]
    assert stages["proposal"]["produces"] == ["proposal_packet", "decision_log"]
    assert stages["script"]["required_artifacts_in"] == ["brief", "proposal_packet"]
    assert stages["scene_plan"]["produces"] == ["scene_plan"]
    assert stages["assets"]["produces"] == ["asset_manifest"]
    assert stages["edit"]["produces"] == ["edit_decisions"]
    assert stages["compose"]["produces"] == ["render_report", "final_review"]
    assert stages["publish"]["produces"] == ["publish_log"]

    gated = {"idea", "proposal", "script", "scene_plan", "assets", "publish"}
    for name, stage in stages.items():
        assert stage["human_approval_default"] is (name in gated)


def test_all_declared_skills_exist_and_carry_subject_contracts():
    manifest = load_pipeline(PIPELINE_NAME)
    declared = set(manifest["required_skills"])

    for skill_ref in declared:
        skill_path = ROOT / "skills" / f"{skill_ref}.md"
        assert skill_path.is_file(), f"Missing skill: {skill_ref}"

    pipeline_skill_dir = ROOT / "skills" / "pipelines" / PIPELINE_NAME
    combined = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted(pipeline_skill_dir.glob("*.md"))
    )
    for required_phrase in (
        "subject_affinity",
        "platform_profile_ref",
        "audio architecture",
        "identity anchors",
        "generated",
        "source lineage",
    ):
        assert required_phrase.lower() in combined.lower()

    assert "meta/text-layer-direction" in declared


def test_pipeline_keeps_native_agent_and_reviewer_authority():
    """Reject the retired Golden Key stage-RPC and rule-echo contracts."""
    manifest = load_pipeline(PIPELINE_NAME)
    skill_dir = ROOT / "skills" / "pipelines" / PIPELINE_NAME
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


def test_director_policy_makes_conditional_use_and_rejection_decisions():
    manifest = load_pipeline(PIPELINE_NAME)
    skill_dir = ROOT / "skills" / "pipelines" / PIPELINE_NAME
    policy = (skill_dir / "director-decision-policy.md").read_text(encoding="utf-8")
    reviewer = (skill_dir / "reviewer-rubric.md").read_text(encoding="utf-8")

    for decision_field in manifest["metadata"]["required_decision_fields"]:
        assert decision_field in policy
    for policy_phrase in (
        "Route Out",
        "Use when",
        "Do not use when",
        "veto",
        "scor",
        "PlatformProfile",
    ):
        assert policy_phrase.lower() in policy.lower()
    for critical_check in (
        "wrong route",
        "unresolved",
        "identity drift",
        "silent",
        "audio",
    ):
        assert critical_check in reviewer.lower()


def test_duration_capability_order_and_full_run_approval_are_governed():
    skill_dir = ROOT / "skills" / "pipelines" / PIPELINE_NAME
    idea = (skill_dir / "idea-director.md").read_text(encoding="utf-8")
    policy = (skill_dir / "director-decision-policy.md").read_text(encoding="utf-8")
    reviewer = (skill_dir / "reviewer-rubric.md").read_text(encoding="utf-8")

    assert "duration_selection" in idea and "at least two" in idea
    assert "goal and evidence -> platform and audience" in policy
    assert "does not veto the creative concept" in policy
    assert "Capability-driven creative collapse" in reviewer
    assert "Unrecorded pre-authorization" in reviewer
    assert "Multi-Output Batch Ownership" in policy
    assert "may not choose the differences" in policy


def test_decision_log_schema_supports_required_duration_and_approval_records():
    schema = json.loads(
        (ROOT / "schemas" / "artifacts" / "decision_log.schema.json").read_text(
            encoding="utf-8"
        )
    )
    categories = schema["properties"]["decisions"]["items"]["properties"]["category"]["enum"]

    assert "duration_selection" in categories
    assert "approval_policy" in categories


def test_semantic_decision_fixture_covers_positive_boundary_and_negative_routes():
    fixture = yaml.safe_load(
        (ROOT / "tests" / "fixtures" / "golden_key_subject_ip_decision_cases.yaml")
        .read_text(encoding="utf-8")
    )
    cases = fixture["cases"]

    assert len(cases) >= 7
    for case in cases:
        assert {"id", "input", "expected"} <= case.keys()
        assert {
            "route",
            "episode_role",
            "narrative_driver",
            "presenter_mode",
            "visual_backbone",
            "use",
            "do_not_use",
            "blocker_if_missing",
        } <= case["expected"].keys()
        assert case["expected"]["use"]
        assert case["expected"]["do_not_use"]
        assert case["expected"]["blocker_if_missing"]

    expected = [case["expected"] for case in cases]
    assert {
        "golden-key-subject-ip",
        "golden-key-product-marketing",
        "character-animation",
    } <= {item["route"] for item in expected}
    assert {"observed_action", "original_voice", "narration", "character_performance"} <= {
        item["narrative_driver"] for item in expected
    }


def test_recorded_semantic_run_matches_expected_routes_and_rejections():
    fixture_dir = ROOT / "tests" / "fixtures"
    expected_fixture = yaml.safe_load(
        (fixture_dir / "golden_key_subject_ip_decision_cases.yaml").read_text(
            encoding="utf-8"
        )
    )
    result_fixture = yaml.safe_load(
        (fixture_dir / "golden_key_subject_ip_decision_results.yaml").read_text(
            encoding="utf-8"
        )
    )
    expected_by_id = {case["id"]: case["expected"] for case in expected_fixture["cases"]}
    actual_by_id = {case["id"]: case["actual"] for case in result_fixture["cases"]}

    assert result_fixture["independence_limit"] == "reviewer_is_not_independent"
    assert set(actual_by_id) == set(expected_by_id)
    for case_id, expected in expected_by_id.items():
        actual = actual_by_id[case_id]
        for field in (
            "route",
            "episode_role",
            "narrative_driver",
            "presenter_mode",
            "visual_backbone",
        ):
            assert actual[field] == expected[field], f"{case_id}: {field}"
        assert set(actual["selected_use"]) == set(expected["use"])
        assert set(actual["rejected"]) == set(expected["do_not_use"])
        assert set(actual["blockers"]) == set(expected["blocker_if_missing"])
        assert actual["review_status"] == "pass"
        assert actual["rationale"]


def test_runtime_and_finished_audio_governance_are_explicit():
    skill_dir = ROOT / "skills" / "pipelines" / PIPELINE_NAME
    proposal = (skill_dir / "proposal-director.md").read_text(encoding="utf-8")
    compose = (skill_dir / "compose-director.md").read_text(encoding="utf-8")

    assert "render_runtime_selection" in proposal
    assert "Remotion" in proposal and "HyperFrames" in proposal
    assert "BGM optional" in proposal and "Do not write" in proposal
    assert "render_runtime" in compose
    assert "HyperFrames" in compose
    assert "silent" in compose.lower() and "substitution" in compose.lower()


def test_minimalist_high_frame_rate_micro_short_is_a_governed_option():
    skill_dir = ROOT / "skills" / "pipelines" / PIPELINE_NAME
    policy = (skill_dir / "director-decision-policy.md").read_text(encoding="utf-8")
    proposal = (skill_dir / "proposal-director.md").read_text(encoding="utf-8")
    script = (skill_dir / "script-director.md").read_text(encoding="utf-8")
    scene = (skill_dir / "scene-director.md").read_text(encoding="utf-8")
    edit = (skill_dir / "edit-director.md").read_text(encoding="utf-8")

    assert "Minimalist micro-short suitability check" in policy
    assert "8–15 second" in proposal
    assert "2–4 expressive text beats" in script
    assert "verified source frame rate" in " ".join(scene.split())
    assert "speed: 0.5" in scene
    assert "timeline_duration = (source_out - source_in) / speed" in edit
    assert "optical flow" in edit


def test_text_layer_direction_is_required_before_caption_or_overlay_routing():
    manifest = load_pipeline(PIPELINE_NAME)
    stages = _stages_by_name(manifest)
    skill_dir = ROOT / "skills" / "pipelines" / PIPELINE_NAME
    proposal = (skill_dir / "proposal-director.md").read_text(encoding="utf-8")
    edit = (skill_dir / "edit-director.md").read_text(encoding="utf-8")
    reviewer = (skill_dir / "reviewer-rubric.md").read_text(encoding="utf-8")

    assert "text_layer_direction" in manifest["metadata"]["required_decision_fields"]
    assert "text-layer-direction" in proposal
    assert "assert_text_layer_direction" in edit
    assert "Text-role collapse" in reviewer
    assert any(
        "text-layer" in focus.lower() for focus in stages["edit"]["review_focus"]
    )


def test_ending_closure_is_directed_and_temporally_reviewed():
    manifest = load_pipeline(PIPELINE_NAME)
    stages = _stages_by_name(manifest)
    skill_dir = ROOT / "skills" / "pipelines" / PIPELINE_NAME
    edit = (skill_dir / "edit-director.md").read_text(encoding="utf-8")
    compose = (skill_dir / "compose-director.md").read_text(encoding="utf-8")
    reviewer = (skill_dir / "reviewer-rubric.md").read_text(encoding="utf-8")

    assert "metadata.ending_treatment" in edit
    assert "duration-0.1s" in compose
    assert "ending_closure" in compose
    assert "Accidental ending" in reviewer
    assert any("final subject beat" in item.lower() for item in stages["edit"]["review_focus"])
    assert any("last-second" in item.lower() for item in stages["compose"]["review_focus"])


def test_native_checkpoint_resume_uses_custom_manifest_order(tmp_path):
    project_id = "sample-pet-subject-ip-smoke"
    init_project(
        project_id,
        title="Sample Pet Subject IP Smoke",
        pipeline_type=PIPELINE_NAME,
        pipeline_dir=tmp_path,
    )

    assert get_next_stage(tmp_path, project_id, PIPELINE_NAME) == "idea"

    checkpoint_path = write_checkpoint(
        tmp_path,
        project_id,
        "idea",
        "completed",
        {"brief": _minimal_subject_brief()},
        pipeline_type=PIPELINE_NAME,
        human_approved=True,
    )

    assert checkpoint_path.is_file()
    checkpoint = read_checkpoint(tmp_path, project_id, "idea")
    assert checkpoint is not None
    assert checkpoint["pipeline_type"] == PIPELINE_NAME
    assert checkpoint["human_approved"] is True
    assert checkpoint["artifacts"]["brief"]["title"] == "示例宠物回家"
    assert checkpoint["artifacts"]["brief"]["hook"] == "同一个呼唤，两次完全不同的回家反应。"
    assert get_next_stage(tmp_path, project_id, PIPELINE_NAME) == "proposal"
