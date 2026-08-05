# Script Director — Golden Key Subject IP Pipeline

## Purpose

Create the canonical `script` from the approved brief and proposal. The subject—not the
editing technique—must be the irreplaceable narrative center.

Read the selected recipe and `director-decision-policy.md`. Preserve the selected narrative
driver; do not force every subject into one universal story template.
Read `skills/meta/material-retrieval-boundary.md` and the OpenMontage-authored
selected-concept query result. If the script creates a genuinely new evidence need, author a
narrower `shot_candidates` request with a script decision reference; never ask Golden Key to
invent the requirement or treat retrieval rank as a shot decision.

If the approved audio architecture uses generated narration, read
`skills/meta/voice-performance-director.md` and persist the script's top-level
`voice_performance` plus section delivery cues. Do not add narration merely because a TTS
tool exists.

## Grounding Rules

Use `source_media_review`, transcription, and scene evidence before writing claims about the
subject. Separate:

- what is visible or audible,
- what the user has verified,
- what the narrator interprets emotionally,
- what is synthetic or hypothetical.

Anthropomorphic framing can be charming, especially for animals, but phrase it as playful
interpretation rather than factual access to the subject's internal state. Do not fabricate
quotes, motives, history, credentials, or relationships.

Resolve `ProjectContentContext` before writing. Every document-backed fact or quotation and
every image/video-backed observation must cite `context_evidence_id`, `asset_id`, content and
understanding revisions, and the exact page/table/cell/region/temporal anchor in section
metadata. Do not quote or display material lacking public-use permission; it may only constrain
the script when Director-context use is allowed. Do not use expired facts, unresolved
conflicts, prohibited expressions, or assets outside the frozen project selection. If the
approved script needs missing evidence, author the narrow OpenMontage query or surface a gap;
never fill it with a plausible claim.

## Story Architecture Selection

Choose the smallest structure that delivers the selected episode role:

- `contrast`: hook -> first behavior -> counter-behavior -> recognition;
- `ritual_observation`: recognizable ritual -> detail -> emotional meaning -> landing;
- `direct_commentary`: claim/opinion -> example -> implication -> closing thought;
- `authority_proof`: promise -> demonstrated process/evidence -> conclusion;
- `personal_story`: situation -> turning point -> meaning;
- `relationship`: two-sided interaction -> tension/care -> shared payoff;
- `series_episode`: familiar device -> new variation -> continuity tag;
- `character_performance`: action objective -> obstacle -> expressive payoff.

Use only the beats the duration and evidence need. The subject should normally appear or be
named inside the PlatformProfile's opening window, but a justified reveal may delay it when
the profile and approved concept support that choice.

For an approved 8–15 second minimalist micro-short, write 2–4 expressive text beats around
one idea. They are display phrases, not continuous subtitle chunks: their length, line breaks,
and timing follow the visual action and PlatformProfile. Do not add narration merely to make
the artifact look more substantial, and do not turn an unverified motivational phrase into
the subject's quotation, history, profession, or viewpoint.

Avoid a generic sequence of cute, impressive, or atmospheric clips. If another subject could
replace this one without rewriting the script, revise it.

## Audio Script

For every section, specify:

- primary carrier: narration, source speech, or expressive caption;
- exact spoken or on-screen text when applicable;
- BGM function and intensity change;
- natural sound to retain;
- silence or pause only when it serves a named emotional beat.

The audio plan must feel like a final video. Do not default to bare natural sound because no
provider has been selected. Any approved music-free or narration-free choice must remain
visible in the decision log and proposal.

## Platform Application

Read the versioned PlatformProfile reference from the brief/proposal metadata. Apply it to
hook form, emotional intensity, sentence length, caption density, pacing, ending, and review.
For Xiaohongshu, prioritize a specific emotional or relational value over raw incident
coverage; do not copy Douyin pacing rules mechanically.

## Viewer Response Architecture

From the resolved PlatformProfile, select one primary viewer payoff and at most one secondary
payoff: curiosity, resonance, utility, conversation, trust, or offer. State who the opening
addresses and what it promises; use observable subject behavior, verified facts, or clearly
labeled interpretation to deliver that promise; and give every suspense setup a real payoff.
Use controversy only when the subject matter contains an evidence-grounded difference of
viewpoint—never manufacture hostility or identity conflict for comments.

The ending must close the subject beat. It may then offer one natural interaction action, or
it may finish with a memorable image, emotional landing, or complete conclusion when a CTA
would feel forced. Early-retention and average-watch targets are diagnostic hypotheses, not
an official ranking formula and not a reason to distort the subject.

## Source and Support Map

Each script section should identify in metadata:

- `source_refs`,
- `context_evidence_refs` with exact multimodal anchors and permission-sensitive use,
- `subject_function`,
- `evidence_type`,
- `audio_carrier`,
- `emotional_beat`,
- `support_need`,
- `interpretation_label` when relevant.

Unsupported future assets must be marked as capability demands or blockers, not written as
if they already exist.

## Quality Gate

- subject appears immediately and remains central,
- story has the necessary change, proof, observation, or payoff for its selected structure,
- the selected structure fits the episode role and is not mechanically fixed,
- observable evidence supports all factual statements,
- creative interpretation is clearly framed,
- audio carriers and music beats form a finished plan,
- PlatformProfile decisions are visible throughout,
- output validates against `script.schema.json`.

## Gate Reminder

This stage requires internal-operator approval, not another customer questionnaire. Write
`awaiting_human`, present the script and review to the mapped actor, and end the turn before
scene planning. After approval, rewrite it as `completed` with `human_approved=True`.
