"""Semantic contracts for Director-authored text-layer routing."""

from __future__ import annotations

from pathlib import Path

import yaml

from lib.text_layer_direction import (
    TextLayerDirectionValidationError,
    assert_text_layer_direction,
    validate_text_layer_direction,
)


ROOT = Path(__file__).resolve().parent.parent.parent


def _cases() -> list[dict]:
    fixture = yaml.safe_load(
        (ROOT / "tests" / "fixtures" / "text_layer_direction_cases.yaml").read_text(
            encoding="utf-8"
        )
    )
    return fixture["cases"]


def test_fixture_covers_ordinary_emphasis_mixed_and_invalid_routes():
    cases = _cases()

    assert len(cases) >= 7
    assert {case["id"] for case in cases} >= {
        "ordinary-narration-active-word",
        "four-character-large-emphasis",
        "mixed-caption-and-emphasis",
        "invalid-large-text-forced-into-subtitles",
        "invalid-remotion-caption-on-ffmpeg-runtime",
        "invalid-mixed-without-attention-policy",
        "invalid-unbound-overlay-asset",
    }


def test_semantic_cases_match_expected_validity_and_reasons():
    for case in _cases():
        report = validate_text_layer_direction(case["edit_decisions"], require=True)
        assert report["valid"] is case["expected_valid"], case["id"]
        if not case["expected_valid"]:
            assert case["expected_issue"] in " | ".join(report["issues"]), case["id"]


def test_assertion_api_returns_report_or_raises_all_conflicts():
    valid_case = next(case for case in _cases() if case["expected_valid"])
    invalid_case = next(case for case in _cases() if not case["expected_valid"])

    assert assert_text_layer_direction(
        valid_case["edit_decisions"], require=True
    )["valid"] is True

    try:
        assert_text_layer_direction(invalid_case["edit_decisions"], require=True)
    except TextLayerDirectionValidationError as exc:
        assert invalid_case["expected_issue"] in str(exc)
    else:
        raise AssertionError("invalid text-layer direction did not raise")


def test_validator_does_not_impose_character_or_line_count_rules():
    case = next(
        case for case in _cases() if case["id"] == "ordinary-narration-active-word"
    )
    changed = case["edit_decisions"] | {
        "subtitles": case["edit_decisions"]["subtitles"]
        | {"max_chars_per_line": 37, "max_lines_per_page": 4}
    }

    report = validate_text_layer_direction(changed, require=True)

    assert report["valid"] is True
