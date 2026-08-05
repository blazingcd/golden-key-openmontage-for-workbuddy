# Scene Director — Golden Key Brand / Company

Translate the selected script into schema-valid `scene_plan`. Put one executor-facing row per
scene in `scene_plan.metadata.shot_plan`; it is part of the canonical artifact, not a separate
shot truth.
Read `meta/material-retrieval-boundary`. For provisional source requirements, author
`exact_range_review` with a scene-plan decision reference or use the Manifest's native
inspection tools. Reinspect candidates marked `exact_review_required`; this `scene_plan`, not
the query result, owns final source path, range, speed, order, audio, fallback, and generation.
Resolve `ProjectContentContext` and keep every provided source inside its frozen project
scope with exact evidence lineage and applicable permission.

Every provided source row states `scene_id`, timeline in/out, asset ID, content/understanding
revisions, `context_evidence_id`, `source_kind`, exact `source_path`, source hash/reference,
exact cited anchor, selection confidence, narrative/evidence role, identity treatment,
framing/safe zone, audio relation, transform, acceptance, fallback, `execution.module`, and
`generated_asset_required: false`. Temporal source additionally requires `source_in`,
`source_out`, and `execution.speed`. Still images use region/whole-asset anchor, crop/fit,
display duration, and motion treatment without invented source time. Documents use exact
page/table/cell/region anchor, render/crop, public-use permission, redaction/legibility checks,
display duration, and fallback.

For temporal rows verify `timeline_out - timeline_in == (source_out - source_in) /
execution.speed`. For still/document rows verify timeline span equals declared display
duration. Verify matching scene boundaries, full main-timeline coverage without unintended
gaps/overlaps, and the final row ending at approved duration. Rough probe ranges are not final
evidence.

Place real company proof near the claim it supports. A mascot, atmosphere, symbol, generated
shot, or graphic may carry emotion or explanation but cannot prove history, people, premises,
operations, customers, scale, or results.

For generated/I2V rows set `generated_asset_required: true` and include the named gap, input
reference/keyframe, generation prompt, negative prompt, protected logo/text/color/person/
product elements, duration, motion purpose, truth label, sample gate, acceptance, disclosure,
and fallback. Reject generation when real source already solves the shot.

Read persisted source-audio analysis before selecting exact natural-sound ranges. Exclude crew
direction, counting, prompting, unrelated speech, and unauthorized statements. Retain, duck,
replace, or mute per scene evidence and concept; never use a blanket default.
