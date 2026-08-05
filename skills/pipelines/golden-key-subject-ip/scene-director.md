# Scene Director — Golden Key Subject IP Pipeline

## Purpose

Translate the approved script into a canonical `scene_plan` that protects subject identity,
the selected truth source, emotional rhythm, and platform readability. Read
`director-decision-policy.md` and preserve the selected visual backbone and layout strategy.
Read `skills/meta/material-retrieval-boundary.md`. For provisional source requirements,
author `exact_range_review` with a scene-plan decision reference or use the Manifest's native
inspection tools. Reinspect every candidate marked `exact_review_required`; the result stays
evidence and this canonical `scene_plan` alone owns the final path, range, speed, order, audio,
fallback, and generation decision.
Resolve `ProjectContentContext` and keep every provided source inside its frozen project
scope with exact evidence lineage and applicable permission.

## Subject Continuity

Before planning scenes, load the subject identity anchors from canonical artifact metadata.
For every scene verify the relevant anchors:

- person: face, voice, body, name, role, and consent boundaries;
- animal: markings, proportions, gait, species claims, and welfare;
- virtual character: silhouette, palette, design sheet, lore, and voice;
- mascot: approved design, brand usage, role, and claim boundaries.

Cropping, enhancement, I2V, transitions, and overlays must not make the subject look like a
different individual or hide the identifying behavior that carries the scene.

## Visual Arc

Plan identifiable functions rather than a list of clips:

- hook frame in the first three seconds,
- setup/ritual,
- contrast or emotional turn,
- recognition or payoff,
- landing frame and series memory device.

For each scene record source lineage or declare it `provided`, `source_derived`, `generated`,
or `graphic_support`. Generated scenes may illustrate an idea but may not impersonate a real
recorded event.

When deliberate source-derived slow motion is approved, record the verified source frame
rate, delivery frame rate, `speed` value, source in/out, calculated timeline duration, and
fallback at normal speed. A 60 fps source conformed at `speed: 0.5` for a 30 fps delivery is
source-derived treatment; it does not require I2V or frame interpolation. The timing math and
the selected action window must remain consistent with `edit_decisions`.

Put an executor-facing row for every scene in `scene_plan.metadata.shot_plan`. Every provided
source row must contain `scene_id`, `timeline_in`, `timeline_out`, `asset_id`, content and
understanding revisions, `context_evidence_id`, exact `source_path`, `source_kind`, cited
anchor, `execution.module`, `execution.generated_asset_required: false`, selection reason,
fallback, and acceptance checks. A temporal source also requires exact `source_in`,
`source_out`, and `execution.speed`. A still image requires its image-region/whole-asset
anchor, crop/fit, display duration, and motion treatment without invented source time. A
document requires page/table/cell/region anchor, render/crop, public-use permission,
redaction/legibility checks, display duration, and fallback. A document fact used only by
narration remains a script citation and need not be shown as a document shot.
Every generated row must instead set `generated_asset_required: true` and include the named gap,
generation prompt, negative prompt, protected elements, provider-neutral capability demand,
fallback, and acceptance checks. Do not hide executable ranges only in prose inside
`required_assets.description`.

Before returning the artifact, calculate every temporal-source row with
`timeline_out - timeline_in == (source_out - source_in) / execution.speed`, verify the matching
scene has the same timeline boundaries, and verify every still/document row's timeline span
equals its declared display duration. Verify consecutive rows have no unintended gap or
overlap and the final row ends at the approved total duration. A transition may overlap
visually inside the composition, but it must not make the main shot ledger's arithmetic
ambiguous. If the numbers do not balance, revise the range, speed, or scene duration before
submitting it for review.

## Support-Layer Discipline

For real people and animals, real footage is normally the evidence. For an approved virtual
character or mascot, the design/rig/lore package is the identity truth and animation may be
primary. Add captions, graphics, reframing, still-to-video, or generated inserts only to
solve a named problem. Do not cover strong authentic or character-defining performance with
constant overlays.

If I2V is proposed, define:

- the source still and identity role map,
- what motion may be invented,
- what must not change or transfer,
- first/last frame requirements,
- disclosure and fallback behavior.

## Platform and Layout

Apply PlatformProfile rules to shot duration, first frame, caption safe zones, overlay
density, subject scale, cover potential, and ending. For vertical output, protect the
subject from UI zones and keep captions from covering face, markings, paws/hands, or the
behavioral action that defines the beat.

## Audio-by-Scene Map

Each scene must state:

- narration/source speech/caption carrier,
- music cue or transition,
- natural sound retained,
- ducking or silence instruction,
- intended emotional effect.

Natural sound is an evidence decision, not a default texture. Before retaining any source
audio, read the selected asset's persisted `source_audio_analysis`, cite its evidence, and
name exact source-time ranges. A range that overlaps crew direction, counting, prompting,
unrelated conversation, or another rejected label must not be retained. Do not call source
audio "ambient" merely because it is quiet in the picture. If the analysis supports mute or
replacement, record that Director choice explicitly; never apply a product-wide default.

## Quality Gate

- every scene advances the subject-led arc,
- identity anchors remain protected,
- first-three-second hook and landing frame are deliberate,
- every asset has lineage or a synthetic designation,
- `metadata.shot_plan` gives exact temporal ranges or still/document anchors and passes the
  applicable range/speed or display-duration timeline arithmetic,
- support solves named gaps,
- platform safe zones and audio beats are explicit,
- output validates against `scene_plan.schema.json`.

## Gate Reminder

This stage requires internal-operator approval. Write `awaiting_human`, present the scene
plan to the mapped actor, and end the turn. After approval, rewrite it as `completed` with
`human_approved=True` before asset production.
