"""Director contracts for project-scoped multimodal evidence."""

from __future__ import annotations

from pathlib import Path

import pytest

from lib.pipeline_loader import load_pipeline


ROOT = Path(__file__).resolve().parent.parent.parent
PIPELINE_VERSIONS = {
    "golden-key-subject-ip": "0.6.4",
    "golden-key-product-marketing": "0.4.4",
    "golden-key-brand-company": "0.2.4",
    "golden-key-lead-conversion": "0.2.4",
}
DIRECTOR_STAGE_FILES = (
    "idea-director.md",
    "proposal-director.md",
    "script-director.md",
    "scene-director.md",
)


@pytest.mark.parametrize("pipeline,version", PIPELINE_VERSIONS.items())
def test_manifest_declares_project_content_context_contract(
    pipeline: str, version: str
) -> None:
    manifest = load_pipeline(pipeline)
    metadata = manifest["metadata"]

    assert manifest["version"] == version
    assert metadata["project_content_context_transport"] == "agent_input_reference"
    assert metadata["project_content_context_policy"] == "frozen_selected_sources_only"
    assert {"project_content_context_ref", "context_evidence_map"} <= set(
        metadata["required_decision_fields"]
    )

    relevant = {
        stage["name"]: " ".join(stage["review_focus"]).lower()
        for stage in manifest["stages"]
        if stage["name"] in {"idea", "proposal", "script", "scene_plan"}
    }
    assert "projectcontentcontext" in relevant["idea"]
    assert "projectcontentcontext" in relevant["proposal"]
    assert "projectcontentcontext" in relevant["script"]
    assert all(token in relevant["scene_plan"] for token in ("temporal", "images", "documents"))


@pytest.mark.parametrize("pipeline", PIPELINE_VERSIONS)
def test_each_director_stage_reads_and_applies_multimodal_context(pipeline: str) -> None:
    skill_dir = ROOT / "skills" / "pipelines" / pipeline
    for name in DIRECTOR_STAGE_FILES:
        text = (skill_dir / name).read_text(encoding="utf-8").lower()
        assert "projectcontentcontext" in text, (pipeline, name)

    idea = (skill_dir / "idea-director.md").read_text(encoding="utf-8").lower()
    proposal = (skill_dir / "proposal-director.md").read_text(encoding="utf-8").lower()
    script = (skill_dir / "script-director.md").read_text(encoding="utf-8").lower()
    scene = (skill_dir / "scene-director.md").read_text(encoding="utf-8").lower()

    assert all(token in idea for token in ("selection_mode", "context_evidence_map", "conflict"))
    assert all(token in proposal for token in ("frozen", "public-use", "cross-project"))
    assert all(token in script for token in ("context_evidence", "permission", "anchor"))
    assert all(
        token in scene
        for token in (
            "context_evidence_id",
            "temporal",
            "still",
            "document",
            "display duration",
            "public-use permission",
        )
    )


@pytest.mark.parametrize("pipeline", PIPELINE_VERSIONS)
def test_reviewer_rejects_invalid_context_and_false_temporal_lineage(pipeline: str) -> None:
    reviewer = (
        ROOT / "skills" / "pipelines" / pipeline / "reviewer-rubric.md"
    ).read_text(encoding="utf-8").lower()

    for token in (
        "projectcontentcontext",
        "frozen source revisions",
        "empty selection",
        "expired",
        "conflict",
        "prohibited",
        "permission",
        "still",
        "document",
        "display duration",
    ):
        assert token in reviewer, (pipeline, token)


def test_shared_boundary_blocks_raw_access_and_cross_project_leakage() -> None:
    boundary = (ROOT / "skills" / "meta" / "material-retrieval-boundary.md").read_text(
        encoding="utf-8"
    ).lower()
    guide = (ROOT / "AGENT_GUIDE.md").read_text(encoding="utf-8").lower()

    for token in (
        "projectcontentcontext",
        "selection_mode: none",
        "raw project folders",
        "unresolved conflict",
        "document page",
        "image-region",
        "cross-project",
    ):
        assert token in boundary

    assert "projectcontentcontext" in guide
    assert "selection_mode: none" in guide
    assert "vector indexes" in guide
