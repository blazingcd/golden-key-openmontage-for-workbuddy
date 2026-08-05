"""Recorded Director decisions for multimodal ProjectContentContext edge cases."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests" / "fixtures"
EXPECTED_CASE_IDS = {
    "sufficient-product-document",
    "image-only-no-video",
    "unresolved-old-new-price-conflict",
    "expired-offer-document",
    "confidential-brand-document",
    "prohibited-expression",
    "similar-product-document-interference",
    "no-selected-material",
    "project-a-context-given-to-project-b",
    "same-command-with-company-document",
    "same-command-without-company-document",
}


def _load(name: str) -> dict:
    return yaml.safe_load((FIXTURES / name).read_text(encoding="utf-8"))


def test_multimodal_recorded_results_match_predeclared_expectations() -> None:
    cases = _load("golden_key_multimodal_project_context_cases.yaml")
    results = _load("golden_key_multimodal_project_context_results.yaml")
    expected = {case["id"]: case for case in cases["cases"]}
    actual = {case["id"]: case["actual"] for case in results["cases"]}

    assert expected.keys() == actual.keys() == EXPECTED_CASE_IDS
    assert results["external_llm_called"] is False
    assert results["execution_provider_called"] is False
    assert results["independence_limit"] == "reviewer_is_not_independent"

    for case_id, case in expected.items():
        result = actual[case_id]
        target = case["expected"]
        assert result["route"] == target["route"]
        assert result["disposition"] == target["disposition"]
        assert result["review_status"] == "pass"
        assert result["rationale"]
        assert set(target.get("required_effects", [])) <= set(result.get("effects", []))
        if "business_question" in target:
            assert result["business_question"] == target["business_question"]
            assert "pipeline" not in result["business_question"].lower()
        if "real_customer_acceptance_claimed" in target:
            assert result["real_customer_acceptance_claimed"] is False


def test_product_routing_keeps_null_selection_except_specialized_benchmark() -> None:
    cases = _load("golden_key_multimodal_project_context_cases.yaml")["cases"]

    for case in cases:
        if case.get("benchmark_only") and case["id"] == "confidential-brand-document":
            assert case["selected_pipeline"] == "golden-key-brand-company"
        else:
            assert case["selected_pipeline"] is None


def test_empty_context_and_project_isolation_fail_closed() -> None:
    results = _load("golden_key_multimodal_project_context_results.yaml")["cases"]
    actual = {case["id"]: case["actual"] for case in results}

    assert "no_library_retrieval" in actual["no-selected-material"]["effects"]
    assert actual["project-a-context-given-to-project-b"]["route"] == "pending"
    assert "no_project_a_evidence" in actual["project-a-context-given-to-project-b"]["effects"]


def test_same_command_changes_evidence_readiness_not_route() -> None:
    cases = _load("golden_key_multimodal_project_context_cases.yaml")["cases"]
    paired = [case for case in cases if case.get("pair_id") == "company-context-difference"]
    assert len(paired) == 2
    assert len({case["request"] for case in paired}) == 1

    results = _load("golden_key_multimodal_project_context_results.yaml")["cases"]
    actual = {case["id"]: case["actual"] for case in results}
    with_docs = actual["same-command-with-company-document"]
    without_docs = actual["same-command-without-company-document"]
    assert with_docs["route"] == without_docs["route"] == "golden-key-brand-company"
    assert with_docs["disposition"] == "proceed_private_benchmark"
    assert without_docs["disposition"] == "block_for_company_evidence"
    assert set(with_docs["effects"]) != set(without_docs["effects"])
