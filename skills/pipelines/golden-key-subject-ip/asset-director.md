# Asset Director — Golden Key Subject IP Pipeline

## Purpose

Build the canonical `asset_manifest` for a subject-led piece. The approved truth source may
be real subject media or approved virtual-character/mascot design assets. Support completes
the selected story and audio architecture without changing what counts as truth.

Read `director-decision-policy.md` and follow the selected presenter mode, visual backbone,
source/support policy, audio treatment, and I2V decision.

## Preflight and Layer 3 Skills

Read the live tool registry before selecting providers. Before calling any generation tool,
read every Layer 3 skill named in that tool's `agent_skills` field. Announce the exact tool,
provider, model/variant, purpose, and whether the call is a sample or batch.

No paid, identity-sensitive, or consequential generation may begin until the proposal and
scene plan gates are approved.

## Asset Priority

Acquire and prepare assets in this order:

1. verified real-source selects or approved character/design assets with exact lineage,
2. source-derived crops/trims/enhancement or approved rig/animation assets,
3. captions and approved narration/source-speech treatment,
4. approved BGM and sound design,
5. graphics that solve named comprehension or platform problems,
6. generated stills/video only for approved gaps.

Do not generate an insert merely because the provider is available.

## Sample Before Batch

Create one representative sample for paid, identity-sensitive, or high-risk classes:

- one narration passage before full TTS,
- one I2V/generated shot before all generated scenes,
- one identity-sensitive enhancement before batch processing,

Routine captions and low-risk graphics do not require a separate human sample unless they
materially change identity, meaning, cost, or the approved visual direction.

Show the sample and wait for approval. Retry a rejected sample at most three times. Do not
change provider, model family, or creative treatment silently.

## Identity-Preserving Generation

For any I2V or generated subject asset, carry forward:

- source reference and subject role map,
- identity anchors,
- `must_preserve`,
- `must_not_transfer`,
- allowed motion and camera behavior,
- forbidden fabricated behavior or claim,
- provider/model/prompt/seed when available,
- disclosure status.

Prompt only what the reference image cannot already establish. Use Hold/React behavior,
first/last frames, accepted-output continuity, and one-variable retakes when supported by the
selected provider skill. If identity drifts, re-anchor from an approved frame rather than
stacking more uncontrolled changes.

## Audio Completion

The manifest must account for:

- narration or source-speech assets when approved,
- captions/subtitles,
- BGM source and license/provenance,
- natural-sound extracts,
- sound effects only when they serve the story,
- mix notes for the edit stage.

If an approved music or voice source is unavailable, stop and surface a blocker. Do not
silently fall back to natural ambience or remove an approved audio element.

## Manifest Metadata

Record provenance, source lineage, subject identity checks, provider/model metadata,
generation parameters, rights/license status, scene linkage, platform variants, sample
approval, and any downgrade/blocker. Use the existing asset manifest schema and metadata;
do not create a parallel asset truth.

For every selected source asset, resolve `source_asset_ref` through the supplied material
query result or material snapshot and record the exact existing `source_path`, source hash,
selected source range, and persisted audio-analysis evidence. An asset ID alone is not an
executable source reference. If the query result lacks that mapping, request it once through
the material-query contract; do not guess a path.

## Quality Gate

- all paths exist,
- source and generated assets are unmistakably separated,
- subject identity anchors pass review,
- paid/identity-sensitive samples were approved,
- audio architecture is complete,
- all assets map to planned scenes,
- output validates against `asset_manifest.schema.json`.

## Gate Reminder

This stage requires internal-operator approval. Write `awaiting_human`, present the
scene-by-scene asset review to the mapped actor, and end the turn. After approval, rewrite it
as `completed` with `human_approved=True` before edit.
