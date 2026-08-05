from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests" / "fixtures"
KNOWN_ROUTES = {
    "golden-key-subject-ip",
    "golden-key-product-marketing",
    "golden-key-brand-company",
    "golden-key-lead-conversion",
    "pending",
}


def _load(name: str) -> dict:
    return yaml.safe_load((FIXTURES / name).read_text(encoding="utf-8"))


def test_recorded_route_robustness_run_matches_expected_decisions() -> None:
    cases = _load("golden_key_four_pipeline_route_robustness_cases.yaml")
    results = _load("golden_key_four_pipeline_route_robustness_results.yaml")
    expected_by_id = {case["id"]: case["expected"] for case in cases["cases"]}
    actual_by_id = {case["id"]: case["actual"] for case in results["cases"]}

    assert expected_by_id.keys() == actual_by_id.keys()
    assert len(expected_by_id) == 11
    assert results["external_llm_called"] is False
    assert results["independence_limit"] == "reviewer_is_not_independent"

    for case_id, expected in expected_by_id.items():
        actual = actual_by_id[case_id]
        assert actual["route"] == expected["route"]
        assert actual["route"] in KNOWN_ROUTES
        assert actual["clarification_needed"] == expected["clarification_needed"]
        assert actual["review_status"] == "pass"
        assert actual["rationale"]
        if expected["clarification_needed"]:
            assert actual["business_question"] == expected["business_question"]
            lowered = actual["business_question"].lower()
            assert "pipeline" not in lowered
            assert "golden-key" not in lowered
        if "blocker_until_answered" in expected:
            assert actual["blocker_until_answered"] == expected["blocker_until_answered"]
        if "real_customer_acceptance_claimed" in expected:
            assert actual["real_customer_acceptance_claimed"] is False
            assert actual["publish_allowed"] is False


def test_route_robustness_covers_each_custom_pipeline_and_pending_questions() -> None:
    results = _load("golden_key_four_pipeline_route_robustness_results.yaml")
    routes = {case["actual"]["route"] for case in results["cases"]}
    assert KNOWN_ROUTES == routes
    clarification_cases = [
        case for case in results["cases"] if case["actual"]["clarification_needed"]
    ]
    assert {case["id"] for case in clarification_cases} == {
        "ambiguous-brand-growth-command",
        "lead-route-missing-qualification",
        "person-versus-product-conflict",
    }
