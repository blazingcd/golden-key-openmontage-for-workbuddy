"""Six-condition robustness matrix for each Golden Key custom Pipeline."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests" / "fixtures"
PIPELINES = {
    "golden-key-subject-ip",
    "golden-key-product-marketing",
    "golden-key-brand-company",
    "golden-key-lead-conversion",
}
CONDITIONS = {
    "normal_sufficient",
    "key_information_missing",
    "input_conflict",
    "irrelevant_material",
    "adjacent_pipeline_confusion",
    "same_material_changed_goal",
}


def _load(name: str) -> dict:
    return yaml.safe_load((FIXTURES / name).read_text(encoding="utf-8"))


def test_matrix_is_exactly_four_pipelines_by_six_conditions() -> None:
    fixture = _load("golden_key_four_pipeline_robustness_matrix_cases.yaml")
    cases = fixture["cases"]
    pairs = {(case["pipeline_under_test"], case["condition"]) for case in cases}

    assert fixture["selected_pipeline_policy"] == "null_for_product_routing"
    assert len(cases) == len(pairs) == 24
    assert pairs == {(pipeline, condition) for pipeline in PIPELINES for condition in CONDITIONS}
    assert Counter(case["pipeline_under_test"] for case in cases) == {
        pipeline: 6 for pipeline in PIPELINES
    }


def test_recorded_matrix_matches_expected_routes_questions_and_ignored_material() -> None:
    fixture = _load("golden_key_four_pipeline_robustness_matrix_cases.yaml")
    results = _load("golden_key_four_pipeline_robustness_matrix_results.yaml")
    expected = {case["id"]: case for case in fixture["cases"]}
    actual = {case["id"]: case["actual"] for case in results["cases"]}

    assert expected.keys() == actual.keys()
    assert results["external_llm_called"] is False
    assert results["independence_limit"] == "reviewer_is_not_independent"

    for case_id, case in expected.items():
        target = case["expected"]
        result = actual[case_id]
        assert result["route"] == target["route"]
        assert result["clarification_needed"] == target["clarification_needed"]
        assert result["review_status"] == "pass"
        assert result["rationale"]
        if target["clarification_needed"]:
            assert result["business_question"]
            lowered = result["business_question"].lower()
            assert "pipeline" not in lowered
            assert "golden-key" not in lowered
        if "blocker" in target:
            assert result["blocker"] == target["blocker"]
        if "ignored" in target:
            assert result["ignored"] == target["ignored"]
        if "ignored_as_proof" in target:
            assert result["ignored_as_proof"] == target["ignored_as_proof"]


def test_changed_goal_cases_route_from_goal_not_customer_or_material_identity() -> None:
    fixture = _load("golden_key_four_pipeline_robustness_matrix_cases.yaml")
    results = _load("golden_key_four_pipeline_robustness_matrix_results.yaml")
    by_id = {case["id"]: case["actual"] for case in results["cases"]}
    changed = [case for case in fixture["cases"] if case["condition"] == "same_material_changed_goal"]

    assert len(changed) == 4
    for case in changed:
        actual_route = by_id[case["id"]]["route"]
        assert actual_route != case["pipeline_under_test"] or case["id"] == "product-changed-goal"

    assert by_id["subject-changed-goal"]["route"] == "golden-key-lead-conversion"
    assert by_id["brand-changed-goal"]["route"] == "golden-key-lead-conversion"
    assert by_id["lead-changed-goal"]["route"] == "golden-key-subject-ip"
