# Edit Director — Golden Key Subject IP Pipeline

## Purpose

Create canonical `edit_decisions` for a finished subject-led short. Lock the subject story
first, then add support and polish.

Read `director-decision-policy.md`, `skills/meta/text-layer-direction.md`, and the approved recipe. “Anchor cut” means the chosen
primary narrative driver works before optional decoration; it does not mean every subject
must use real-footage montage.

## Anchor Cut First

Build an anchor cut from the selected real-source, presenter, narration, or character-
performance backbone before optional graphics, generated inserts, or decorative transitions.
It must communicate:

- who the subject is,
- the recognizable pattern or promise,
- the contrast/turn,
- the recognition/payoff,
- the landing emotion.

If the cut could feature any person, animal, character, or mascot, return to script or scene
plan. Support layers cannot repair a generic subject story.

## Pacing

Use the PlatformProfile for the opening window, shot duration, information density, emotional
breathing room, and ending. Protect authentic performance: a strong look, movement, reaction,
pause, or environmental sound may deserve a longer hold than a generic “fast-cut” rule.

For approved source-derived slow motion, set the canonical cut `speed` explicitly and verify
`timeline_duration = (source_out - source_in) / speed`. Prefer a verified 50/60 fps source for
0.5x delivery at 25/30 fps. Do not request optical flow or generated intermediate frames
unless the approved concept names that synthetic treatment, provider, cost, disclosure, and
fallback. Retiming must emphasize a readable subject action, not disguise weak footage.

## Audio Edit (Finished-Video Requirement)

Lay out the mix as one system:

1. primary meaning carrier: narration or source speech, with expressive captions as approved;
2. BGM emotional curve, entry/exit, transitions, and ducking;
3. natural sound retained at identity-rich or emotionally credible moments;
4. effects used sparingly for emphasis, not to manufacture emotion;
5. intentional silence only where it produces a named result.

Record the final evidence-based decision in
`edit_decisions.metadata.source_audio_policy`: `mode` (`mute`, `replace`,
`retain_selected`, or `duck_selected`), `reviewed: true`, reason, volume, exact retained
source ranges with `source_asset_ref`, and the material audio-analysis evidence references.
Retained ranges must not overlap persisted crew direction, counting, prompting, or unrelated
speech. This is a Director decision per selected range, not a default-mute or default-retain
product rule.

Do not mark narration or BGM as “optional.” Follow the approved proposal. If an approved
element is missing, create a blocker instead of delivering a bare rough cut as a final plan.

## Support Layers

Add in priority order: captions, identity/context labels, necessary reframing, graphics,
generated inserts, and series/ending devices. Limit concurrent layers so the subject remains
readable. Never cover face, distinctive markings, hands/paws, or the defining action with a
caption or CTA.

## Text Layer Direction

Carry the proposal's text roles into `edit_decisions.metadata.text_layer_direction`.
Continuous speech/narration belongs in `edit_decisions.subtitles`; expressive emphasis,
titles, CTA, and annotations belong in `edit_decisions.overlays` with their approved asset
IDs and renderer. If both deliveries are present, write an `attention_policy` that limits
simultaneous competition and protects the subject/evidence.

Do not apply ordinary-caption character recommendations to expressive display text. Do not
render a large emphasis treatment as continuous subtitles merely because the words have
timestamps. Before checkpoint, run
`lib.text_layer_direction.assert_text_layer_direction(edit_decisions, require=True)` and
fix every semantic conflict.

## Truth and Identity Review

- source moments retain exact lineage,
- generated moments remain disclosed,
- creative interpretations are not edited as factual proof,
- identity anchors remain consistent across cuts and generated assets,
- no reaction is created by misleading temporal juxtaposition.

## Runtime Lock

Carry `proposal_packet.production_plan.render_runtime` and composition mode unchanged into
`edit_decisions`. Do not silently substitute Remotion, HyperFrames, FFmpeg, a provider, or a
still-led treatment.

## Ending Closure

Treat the ending as the subject story's final beat, not as the point where the last source range
runs out. Record `metadata.ending_treatment`: landing frame/action, last readable text time,
visual release, audio tail, and the intended viewer feeling. A hard cut is allowed only as an
explicitly justified punctuation. Otherwise reserve a short natural resolve, hold, dissolve, or
fade so the recognition/payoff is felt before export ends. Captions and music must not terminate
at the same frame as the file.

## Quality Gate

- anchor cut works without support,
- subject remains irreplaceable and emotionally legible,
- platform pacing is deliberate rather than mechanical,
- audio plan is complete and mixable,
- overlay density protects performance,
- runtime and mode match approvals,
- text roles, delivery paths, renderer/runtime, and overlay asset references validate,
- the final beat has explicit picture, text, and audio closure,
- output validates against `edit_decisions.schema.json`.
