"""Semantic validation for Director-authored text-layer routing.

The Director decides why visible text exists and which existing OpenMontage
rendering path should realize it. This module checks that the decision is
internally consistent; it intentionally does not impose universal character
counts, line counts, font sizes, or a single Chinese subtitle style.
"""

from __future__ import annotations

from typing import Any


TEXT_LAYER_ROLES = {
    "continuous_caption",
    "expressive_emphasis",
    "title_or_section",
    "cta",
    "annotation",
}

TEXT_LAYER_DELIVERIES = {"subtitles", "overlay"}

TEXT_LAYER_RENDERERS = {
    "subtitle_gen_ffmpeg",
    "subtitle_gen_remotion",
    "remotion_overlay",
    "hyperframes_component",
    "video_compose_overlay",
}

RENDERER_RUNTIME = {
    "subtitle_gen_ffmpeg": "ffmpeg",
    "subtitle_gen_remotion": "remotion",
    "remotion_overlay": "remotion",
    "hyperframes_component": "hyperframes",
}


class TextLayerDirectionValidationError(ValueError):
    """Raised when an approved text-layer plan contradicts its render path."""


def validate_text_layer_direction(
    edit_decisions: dict[str, Any], *, require: bool = False
) -> dict[str, Any]:
    """Validate text roles against subtitles, overlays, and render runtime.

    ``edit_decisions.metadata.text_layer_direction`` uses the existing metadata
    extension point and does not create a parallel canonical artifact.
    """

    issues: list[str] = []
    metadata = edit_decisions.get("metadata") or {}
    direction = metadata.get("text_layer_direction")
    if direction is None:
        if require:
            issues.append("metadata.text_layer_direction is required")
        return {
            "valid": not issues,
            "issues": issues,
            "layer_count": 0,
            "roles": [],
            "deliveries": [],
        }
    if not isinstance(direction, dict):
        issues.append("metadata.text_layer_direction must be an object")
        return {
            "valid": False,
            "issues": issues,
            "layer_count": 0,
            "roles": [],
            "deliveries": [],
        }

    layers = direction.get("layers")
    if not isinstance(layers, list) or not layers:
        issues.append("text_layer_direction.layers must be a non-empty array")
        layers = []

    subtitles = edit_decisions.get("subtitles") or {}
    overlays = edit_decisions.get("overlays") or []
    overlay_ids = {
        item.get("asset_id")
        for item in overlays
        if isinstance(item, dict) and item.get("asset_id")
    }
    runtime = edit_decisions.get("render_runtime")
    roles: list[str] = []
    deliveries: list[str] = []

    for index, layer in enumerate(layers):
        prefix = f"text_layer_direction.layers[{index}]"
        if not isinstance(layer, dict):
            issues.append(f"{prefix} must be an object")
            continue
        for key in ("layer_id", "role", "delivery", "renderer", "reason"):
            if not layer.get(key):
                issues.append(f"{prefix}.{key} is required")

        role = layer.get("role")
        delivery = layer.get("delivery")
        renderer = layer.get("renderer")
        if role:
            roles.append(role)
        if delivery:
            deliveries.append(delivery)

        if role and role not in TEXT_LAYER_ROLES:
            issues.append(f"{prefix}.role is unsupported: {role}")
        if delivery and delivery not in TEXT_LAYER_DELIVERIES:
            issues.append(f"{prefix}.delivery is unsupported: {delivery}")
        if renderer and renderer not in TEXT_LAYER_RENDERERS:
            issues.append(f"{prefix}.renderer is unsupported: {renderer}")

        if role == "continuous_caption" and delivery != "subtitles":
            issues.append(f"{prefix}: continuous_caption must use subtitles delivery")
        if role in TEXT_LAYER_ROLES - {"continuous_caption"} and delivery != "overlay":
            issues.append(f"{prefix}: {role} must use overlay delivery")

        if delivery == "subtitles":
            if not subtitles.get("enabled"):
                issues.append(f"{prefix}: subtitles delivery requires subtitles.enabled=true")
            if not subtitles.get("source"):
                issues.append(f"{prefix}: subtitles delivery requires subtitles.source")
            if renderer not in {"subtitle_gen_ffmpeg", "subtitle_gen_remotion"}:
                issues.append(f"{prefix}: subtitles delivery uses an incompatible renderer")

        if delivery == "overlay":
            asset_ids = layer.get("asset_ids")
            if not isinstance(asset_ids, list) or not asset_ids:
                issues.append(f"{prefix}: overlay delivery requires asset_ids")
            else:
                missing = sorted(set(asset_ids) - overlay_ids)
                if missing:
                    issues.append(
                        f"{prefix}: overlay assets are not present in edit_decisions.overlays: {missing}"
                    )
            if renderer not in {
                "remotion_overlay",
                "hyperframes_component",
                "video_compose_overlay",
            }:
                issues.append(f"{prefix}: overlay delivery uses an incompatible renderer")

        expected_runtime = RENDERER_RUNTIME.get(renderer)
        if expected_runtime and runtime != expected_runtime:
            issues.append(
                f"{prefix}: renderer {renderer} requires render_runtime={expected_runtime}, got {runtime}"
            )

    if "subtitles" in deliveries and "overlay" in deliveries:
        if not direction.get("attention_policy"):
            issues.append(
                "mixed subtitle and overlay text layers require an attention_policy"
            )

    return {
        "valid": not issues,
        "issues": issues,
        "layer_count": len(layers),
        "roles": roles,
        "deliveries": deliveries,
        "render_runtime": runtime,
    }


def assert_text_layer_direction(
    edit_decisions: dict[str, Any], *, require: bool = False
) -> dict[str, Any]:
    """Return the validation report or raise with all semantic conflicts."""

    report = validate_text_layer_direction(edit_decisions, require=require)
    if not report["valid"]:
        raise TextLayerDirectionValidationError("; ".join(report["issues"]))
    return report
