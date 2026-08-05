# Scene Director — Golden Key Lead Conversion

Translate the approved script into schema-valid `scene_plan`. Put one executor-facing row per
scene in `scene_plan.metadata.shot_plan`; do not create a parallel shot artifact.
Read `meta/material-retrieval-boundary`. For provisional source requirements, author
`exact_range_review` with a scene-plan decision reference or use the Manifest's native
inspection tools. Reinspect candidates marked `exact_review_required`; this `scene_plan`, not
the query result, owns final source path, range, speed, order, audio, fallback, and generation.
Resolve `ProjectContentContext` and keep every provided source inside its frozen project
scope with exact evidence lineage and applicable permission.

Every provided source row states `scene_id`, timeline in/out, asset ID, content/understanding
revisions, `context_evidence_id`, `source_kind`, exact `source_path`, source hash/reference,
exact cited anchor, confidence, conversion/evidence role, framing/safe zone, audio relation,
transform, acceptance, fallback, `execution.module`, and `generated_asset_required: false`.
Temporal source additionally requires `source_in`, `source_out`, and `execution.speed`. Still
images use region/whole-asset anchor, crop/fit, display duration, and motion treatment without
invented source time. Documents use page/table/cell/region anchor, render/crop,
public-use permission, redaction/legibility checks, display duration, and fallback.

For temporal rows verify `timeline_out - timeline_in == (source_out - source_in) /
execution.speed`. For still/document rows verify timeline span equals declared display
duration. Verify matching scene boundaries, full timeline coverage without unintended gaps/
overlaps, and final row at approved duration. Rough probe ranges are not final selections.

Give relevance, offer mechanism, proof, qualification, and CTA their own visible support.
Attention footage, atmosphere, mascot/person behavior, stock, or graphics may attract or
explain; they cannot prove a customer result, earnings, demand, offer quality, or eligibility.

For generated/I2V rows set `generated_asset_required: true` and include named gap, reference/
keyframe, generation prompt, negative prompt, protected people/logo/text/product/offer terms,
duration, motion purpose, truth label, sample gate, acceptance, disclosure, and fallback.
Never generate a fake testimonial, customer, result, certificate, contact, or demand signal.

Read persisted source-audio analysis before retaining exact ranges. Exclude crew direction,
counting, prompting, unrelated speech, and unapproved offer/customer statements. Retain,
duck, replace, or mute per evidence and concept; no blanket default applies.
