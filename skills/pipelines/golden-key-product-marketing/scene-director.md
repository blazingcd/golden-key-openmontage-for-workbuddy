# Scene Director — Golden Key Product Marketing

Translate the selected script into a schema-valid `scene_plan`. Put the detailed shot plan in
`scene_plan.metadata.shot_plan` so it remains part of the canonical scene artifact.
Read `meta/material-retrieval-boundary`. For provisional source requirements, author
`exact_range_review` with a scene-plan decision reference or use the Manifest's native
inspection tools. Reinspect candidates marked `exact_review_required`; this `scene_plan`, not
the query result, owns final source path, range, speed, order, audio, fallback, and generation.
Resolve `ProjectContentContext` and keep every provided source inside its frozen project
scope with exact evidence lineage and applicable permission.

Every source shot must state its `source_kind`, `context_evidence_id`, asset/content/
understanding revisions, and exact cited anchor. Temporal video/audio uses source ranges;
still images use exact region/whole-asset anchors; documents use exact page/table/cell/region
anchors and public-use permission. Every source shot must also state:

- timeline in/out and intended duration;
- exact `source_path`, source hash/reference, and selection confidence; temporal assets also
  require `source_in` and `source_out`, while still/document assets require display duration,
  crop/render treatment, and no invented source time;
- visual content, framing/crop/safe-zone intent, narrative/information role;
- narration, subtitle, emphasis, BGM/natural-sound relationship;
- transform or enhancement need and fallback;
- acceptance checks.

Use one executor-facing `scene_plan.metadata.shot_plan` row per scene. For temporal source, place
`scene_id`, `timeline_in`, `timeline_out`, `asset_id`, exact `source_path`, `source_in`,
`source_out`, `execution.module`, `execution.speed`, and
`execution.generated_asset_required: false` in structured fields, not only in prose. For a
still image, replace temporal fields with region anchor, crop/fit, display duration, motion
treatment, and fallback. For a document, use page/table/cell/region anchor, render/crop,
redaction/legibility checks, display duration, public-use permission, and fallback. For a
generated row set `generated_asset_required: true` and include `generation_prompt` and
`negative_prompt` in addition to the generation requirements below.

Before returning, calculate each temporal-source row with
`timeline_out - timeline_in == (source_out - source_in) / execution.speed`, verify its matching
scene uses the same boundaries, verify each still/document timeline span equals its declared
display duration, verify rows cover the main timeline without unintended gaps or
overlaps, and verify the last row ends at the approved total duration. Repair any mismatch
before submitting the artifact to Reviewer.

Do not copy ranges from a rough probe unless provenance proves them. Inspect or re-derive the
source boundaries. Make the service/product and evidence visible near relevant copy.

For generated/I2V shots, state the named gap, input reference/keyframe, prompt, negative
prompt, protected elements, disclosure, duration, motion purpose, provider-neutral demand,
sample gate, fallback, and acceptance. Reject generation when real source already solves the
shot. Plan vertical framing and text safe zones from applied PlatformProfile rules.

Natural sound is not automatically useful. Read each selected asset's persisted
`source_audio_analysis` before retaining it, cite that evidence, and name exact source-time
ranges. Never retain a range overlapping crew direction, counting, prompting, unrelated
conversation, or another rejected label. Mute, replace, retain, or duck remains a Director
decision for the evidence and concept; there is no product-wide default.
