# Proposal Director — Golden Key Subject IP Pipeline

## Purpose

Turn the approved brief into a schema-valid `proposal_packet` and append-only
`decision_log`. This stage resolves the actual production path before money is spent or
assets are generated.

Read `director-decision-policy.md`, `skills/meta/text-layer-direction.md`,
`skills/meta/taste-direction.md`, and `skills/meta/animation-runtime-selector.md` first. The
proposal is a conditional recommendation, not a menu of every capability and not a fixed
recipe. Persist a task-specific `taste_profile`; when atelier is a real candidate, also read
`skills/meta/bespoke-composition.md` before recommending composition mode.
Read `skills/meta/material-retrieval-boundary.md` before using any snapshot or query result.

## Persisted Source Understanding

When Golden Key supplies a ready `MaterialIndexSnapshot`, its complete-ingest receipt, and
task-level `material_query_result`, treat that bound set as this product's implementation of
OpenMontage Source Understanding Review. It already contains technical probes, reusable
source ranges, visual semantics, timestamped speech, audio labels, and provenance gathered at
upload time. The Handoff query is unranked initial coverage, not a creative shortlist. Do not
request a second `source_media_review` or reopen all source files during a task.

Resolve the frozen `ProjectContentContext` and its permissions/conflicts before comparing
concepts. For every concept, identify which cited facts, excerpts, image regions, document
pages/tables, or temporal observations carry its promise and which are merely inspiration or
interpretation. Reject any use of expired, unresolved-conflict, prohibited, non-referenceable,
cross-project, or permission-ineligible evidence. Private material may constrain the
direction but may not be quoted or shown publicly without public-use permission. A context
with `selection_mode: none` is a legitimate no-material case, not permission to search the
library.

## Concept Requirement

Generate at least three genuinely different subject-led concepts. They must differ in story
mechanism, emotional arc, use of source moments, audio carrier, and ending—not just title or
music mood. Useful structures include contrast, ritual, discovery, relationship, growth,
point-of-view, or a recurring episode device.

Apply rights/truth/identity/capability/goal vetoes first. Score surviving concepts using the
decision policy, record the full comparison internally, and recommend the highest-fit one.
Golden Key customers receive one recommended natural-language direction; rejected concepts
and technical comparisons remain available to the designated OpenMontage approval actor.

Only after the creative winner is recorded may the OpenMontage Agent author a
`shot_candidates` request tied to that selected-concept decision. Golden Key may execute it,
but its result remains retrieval evidence; source and exact-range selection remain here and in
the later canonical stages.

If the decision policy's minimalist micro-short suitability check passes, include one
8–15 second action-led concept in the internal three-concept comparison. It must compete on
the same evidence, platform, identity, and feasibility scores; it is not an automatic winner
or a fallback of last resort. Explain whether it builds recognition/affinity only or whether
verified speech/profile facts support a stronger IP promise.

For each concept explain:

- what the viewer should feel and remember about the subject,
- the first-three-second hook,
- which verified source moments carry the claim,
- narration/source speech/caption treatment,
- BGM and natural-sound behavior,
- what support or generated assets solve,
- identity, rights, and interpretation risks,
- why it fits the selected PlatformProfile.

Record exact ProjectContentContext evidence IDs and anchors for each material-backed claim or
visual obligation. After creative selection, any `shot_candidates` request is restricted to
the context's frozen selected/resolved assets; a similarly named or newly uploaded asset is
out of scope.

Visible behavior may establish mood, presence, style, or an observable action; it does not by
itself prove punctuality, honesty, project performance, commercial success, reliability, or
that the person "never talks empty words." Keep copy at the level supported by the footage and
approved subject profile. A concept that lacks rights for its planned source speech, voice, or
identity use is vetoed before scoring, not retained as an attractive option.

Every concept must name a definite ending available from evidence or a provider-neutral
capability demand. Do not write "if there is a smiling shot" or another conditional ending.

## Capability and Cost Preflight

Use the registry `provider_menu_summary()` before recommending tools. Report the real
configured capability ratios, setup offers, and runtime warnings. Separate:

- available now,
- available with a small configuration step,
- unavailable or blocked,
- optional premium paths.

Name the exact tool/provider/model before any consequential generation. Do not invent a
provider or assume a capability from documentation alone.

Carry `platform_profile_ref`, its version/hash, and `actual_target_platform` into
`proposal_packet.metadata`. Apply capability availability
only after ranking concepts on creative, evidence, platform, truth, rights, and identity.
Availability decides execution readiness and explicit blockers; it may not change the winner.
Do not praise the selected concept for avoiding an unavailable provider, lowering execution
risk, being local, or costing less. Put feasibility and cost in the capability audit after the
creative rationale. Any such factor in `selected_concept.rationale` is evidence that the
ordering was violated.

Populate `production_plan.stages[].tools` only with tools exposed by the active OpenMontage
manifest or tool registry. Planning stages may have an empty tool list; the OpenMontage
Agent itself is not an executable tool and must not be represented as a production-plan
tool or another invented capability. Record unavailable execution needs in
`proposal_packet.metadata.execution_requirements`, with their purpose, affected stage,
availability, fallback, and blocker status. The Pipeline selects the production path; the
Golden Key control plane supplies capability facts but does not prescribe stage tools.

If a selected narration, voice-clone, source-audio, I2V, or compose treatment cannot be
executed by the tools exposed to the relevant stage, keep the creative decision and stop at
the execution boundary unless an approved fallback preserves the same promise. If no voice
is selected, omit `production_plan.voice_selection` rather than writing null.

## Render Runtime Selection (MANDATORY — Present Both)

Query `video_compose.get_info()["render_engines"]`.

- **Remotion** is usually stronger when real subject footage remains primary and React
  overlays, captions, callouts, or source-video composition are needed.
- **HyperFrames** (`render_runtime="hyperframes"`) is stronger when the approved treatment is HTML/CSS/GSAP-native kinetic
  typography or a bespoke web-motion layer around the footage.
- **FFmpeg** is acceptable only for a deliberately simple footage-led cut whose approved
  character does not depend on a richer composition runtime.

When both Remotion and HyperFrames are available, present both with brief-specific benefits
and tradeoffs, recommend one, and wait for explicit approval. Log `render_runtime_selection`
with all available options in `options_considered`. A single-option log when both were
available is a critical defect. Never silently choose a default.

## Composition Mode

Present `templated` and `atelier` separately from runtime. Recommend atelier only when the
piece needs a one-off visual language and the extra authoring cost is justified. Log the
choice under `composition_mode`. If atelier is chosen, record a specific art direction and
taste profile before authoring scenes.

## Production Recipe Selection

Lock all decision dimensions required by the manifest:

- episode role and narrative driver;
- presenter mode and visual source/backbone;
- layout strategy and source/support policy;
- audio treatment;
- text-layer direction: each planned layer's content role, delivery, renderer family, and
  reason; ordinary captions and expressive text must remain distinct;
- I2V/generated-support decision and fallback;
- applied PlatformProfile rules;
- capability demands and review obligations.

If the selected concept has a CTA, classify it as a CTA text role. Do not mark
`text_layer_direction.cta` false while the concept contains CTA copy.

Also select `renderer_family` from the schema-valid options. For example, presenter-led work
can use `presenter`, real observational stories can use `documentary-montage`, a mood-led
piece can use `cinematic-trailer`, and an approved virtual-character performance can use
`animation-first`. This is a recommendation based on the chosen recipe, not an auto-default.

## Audio Decision (Mandatory)

Resolve all of these now:

- primary meaning carrier: narration, source speech, expressive captions, or a deliberately
  approved alternative;
- voice provider/voice identity/delivery style when narration is used;
- music source: user library, available provider, bring-your-own, or explicitly approved none;
- BGM emotional curve and ducking relationship to speech;
- natural-sound moments to preserve;
- caption role and density.

At proposal, identify the intended natural-sound role and cite the persisted audio analysis;
exact retained source ranges are locked at scene/edit after the actual shots are selected.
Do not demand or invent exact audio ranges before shot selection.

For an approved minimalist micro-short, BGM is normally the emotional carrier and
`expressive_captions` the meaning carrier. State the music curve, text beats, natural-sound
accent, and why narration/source speech is intentionally absent. This is a finished audio
design, not permission to omit missing elements silently.

Choose the ideal voice on identity, tone, consent, and creative fit before reading
availability. Do not replace an ideal authorized clone or human voice with a preset voice
because execution is easier. A genuinely creative preset-voice choice must have a rationale
that stands without availability. Otherwise keep the ideal voice and declare its capability
and disclosure blockers.

For visible text, decide the content role before appearance. A continuous narration caption,
large emphasis phrase, title, annotation, and CTA are different production decisions even
when the customer calls all of them “subtitles.” Character capacity is task-specific; do not
use a universal Chinese line length as a substitute for Director judgment.

Do not write “BGM optional.” If no music source is currently available, state the blocker or
bring-your-own path before asset work. A no-narration and no-music result requires an
intentional, approved creative rationale—not a silent fallback.

## Identity and Synthetic Media Plan

Record the subject identity anchors and forbidden transfers for any generation or I2V work.
Generated footage must be disclosed and cannot be presented as documentary proof of a real
behavior. For people, require likeness/voice authorization; for animals, protect markings,
proportions, and welfare; for virtual characters and mascots, protect the approved design
system and lore.

## Production Plan

Populate the existing `proposal_packet.production_plan` with:

- pipeline name `golden-key-subject-ip`,
- stage-by-stage tool path and fallbacks,
- selected playbook,
- renderer family, render runtime, and composition mode,
- delivery promise (`source_led` or `hybrid` as appropriate),
- voice selection and music source,
- exact quality/cost tradeoffs,
- decision log reference,
- metadata references to the subject dossier, PlatformProfile, and source review.

Use `proposal_packet.metadata` for subject-specific planning details; do not create a parallel
production recipe artifact.

## Approval Actors and Gate Sequence

The customer confirms one natural-language direction; the internal operator reviews the full
runtime/provider/composition comparison required by OpenMontage. Do not ask the customer to
choose raw engine names.

First write the proposal checkpoint as `awaiting_human`, present the appropriate view to each
required actor, and end the turn. After the recorded approvals arrive, rewrite the checkpoint
as `completed` with `human_approved=True`. For reference-driven work, run and approve the
manifest's 10–15 second `sample` sub-checkpoint before full production.
