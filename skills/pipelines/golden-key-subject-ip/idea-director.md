# Idea Director — Golden Key Subject IP Pipeline

## Purpose

Qualify the request and create the canonical `brief`. The defining question is not “what
format is this?” but “should the viewer remember, like, trust, or identify with this
recurring subject after watching?”

Read `director-decision-policy.md` first. Use its eligibility, route-out, episode-role,
truth-source, and blocker rules rather than treating this Pipeline as a universal format.

## Inputs

- user intent and verified facts,
- versioned fact-only `subject_facts_profile_ref` with ID, version, hash, subject identity,
  verified facts, identity anchors, prohibitions, and rights,
- `source_media_review` when footage or stills are supplied,
- `video_analysis_brief` when a reference video is supplied,
- versioned PlatformProfile reference,
- versioned `ProjectContentContext` reference with frozen selected/resolved source revisions,
  eligible facts/excerpts/visuals, exact anchors, permissions, validity, conflicts,
  prohibitions, warnings, and gaps,
- product capability policy boundary. Live executor availability is intentionally deferred
  to proposal, after the ideal creative direction is established.

When Golden Key supplies a ready `MaterialIndexSnapshot`, complete-ingest receipt, and
task-level `material_query_result`, that bound set is the product's Source Understanding
Review. Read `skills/meta/material-retrieval-boundary.md`: the Handoff result is unranked
initial coverage, not a shortlist or shot choice. Do not request another whole-library
`source_media_review` or reopen source files.

Read `skills/meta/material-retrieval-boundary.md` for the full multimodal contract. Treat
`ProjectContentContext` as evidence, never as an episode idea. Resolve its ID/version/hash and
project scope; cite every adopted fact or observation by context evidence ID plus asset,
content revision, understanding revision, and page/table/region/time anchor. Honor expiry,
permissions, prohibited expressions, and unresolved conflicts. If `selection_mode: none`, do
not query the wider library. Put the context reference, applied evidence IDs, conflicts,
warnings, and gaps in `brief.metadata.context_evidence_map` without selecting shots.

For a reference video, apply `skills/meta/video-reference-analyst.md`: extract structure,
pacing, scene logic, and style, then create differentiated concepts rather than copying.

## Qualification

Apply the route-out table in `director-decision-policy.md`. Accept only when subject affinity,
authority, trust, recognition, personal story, or series continuity is primary. A product can
feature the subject, but that does not make the job a subject-IP job. A request to create a
new reusable rig belongs in `character-animation` before subject-IP episode production.

Resolve and record `subject_facts_profile_ref`, then record `subject_type` as `person`, `animal`,
`virtual_character`, or `mascot`. Record:

- verified facts,
- observable behaviors with source references,
- identity anchors,
- rights/consent status,
- interpretations that must not be presented as facts,
- any recurring trait or series continuity that is explicitly verified by the user or source.

The input profile is not a creative dossier. Derive the episode role, recurring trait,
content pillar, tone, expression strategy, duration, and story structure here under this
Skill, then store that Director-owned projection in the canonical `brief`. Do not treat a
Golden Key profile, query label, or prior benchmark wording as creative authority.

An observed walk, arrival, seated pose, look, or work-like setting can establish only the
visible action, mood, presence, and first impression. It cannot prove punctuality, an
appointment, honesty, reliability, project competence, commercial results, "not talking
empty words," or what happens "every time." Do not use `赴约`, `按约`, `准时`, `每次到场`,
`说到做到`, or equivalent claims unless a cited profile fact or source statement proves it.
With limited evidence, build trust honestly through restrained first-impression framing,
an explicit value statement that is not disguised as biography, and an invitation to verify
through real conversation. Reviewer fixes must obey the same boundary.

## Clarification Contract

Ask only what changes the route or prevents a safe brief. Ask one customer-facing question
at a time, normally zero to three in total. Never present a questionnaire wall. After each
answer, update the known facts and decide whether another question is still necessary.

## PlatformProfile Contract

The canonical schemas use broad platform enums. For Xiaohongshu, Douyin, Kuaishou, or
WeChat Channels, use `target_platform: generic` when needed and store the actual platform,
resolved `platform_profile_ref`, profile version, and hash in `brief.metadata`.

Read the resolved PlatformProfile supplied through the OpenMontage Agent input. Apply the
rules that matter to the current decision; do not echo every rule ID into every artifact as
proof of compliance. The artifact and native review must instead show the concrete effect of
the profile on:

- hook and first-frame promise,
- emotional value and pacing,
- caption density and visual safe zones,
- narration/source-speech/BGM/natural-sound balance,
- ending and CTA behavior,
- review criteria.

Do not reduce platform behavior to aspect ratio or export settings.

For a share/trust routing rule, put the analytical `share_reason` and
`credibility_carrier` in brief metadata. Do not force that analysis into the hook as a claim
about the subject, and do not require the hook to say "值得转发".

## Audio Architecture (Mandatory)

Define a finished-video audio strategy at idea time:

1. Choose the primary meaning carrier: narration, source speech, or intentionally expressive
   captions. Natural ambience alone is normally insufficient for a finished subject story.
2. State the BGM role and desired emotional progression. “Optional” is not a decision.
3. Reserve purposeful natural-sound moments that preserve authenticity.
4. A music-free plan requires a specific creative reason and explicit user approval later.

For emotion-led platforms such as Xiaohongshu, strengthen personality and emotional value
through voice, captions, music, and natural sound rather than relying on bare montage.

## Duration and Capability Ordering (Mandatory)

When the customer has not specified a duration, do not inherit a template length or choose
the shortest locally executable cut. Compare at least two plausible duration bands against
the episode promise, available evidence, platform pacing, meaning carrier, and required
ending clearance. Record a `duration_selection` entry in the append-only `decision_log`
with the options considered, selected range, rejected reasons, and evidence references. The
idea-stage duration may be a planning range; proposal must lock the exact target runtime.

Choose the strongest honest creative and audio treatment without reading live executor
availability. Live availability is deliberately introduced at proposal, where it answers
whether the approved direction can execute now, not what the Director was allowed to
imagine. At idea, record required creative functions in plain terms and mark capability
feasibility as `pending_proposal_audit`; do not predict unavailable providers. Proposal then
preserves the direction, records explicit missing execution requirements and blockers, and
stops before execution or uses only a creatively valid approved fallback.

Do not name a provider, voice ID, fallback voice, model, or current availability at idea.
State only the ideal meaning carrier and desired human/synthetic voice qualities. Exact
voice/provider/capability binding belongs to proposal after the creative direction is fixed.

## Approval Policy Record

If the customer has explicitly pre-authorized a bounded multi-stage Director run, preserve
the supplied approval-policy reference. When the product control plane has already recorded
the matching `approval_policy` entry in an input decision log, copy that entry byte-for-byte
into the cumulative output and append only new Director decisions; never replace, renumber,
summarize, or duplicate it. Otherwise append an `approval_policy` decision-log entry
stating scope, actor, constraints, and excluded actions. Set `user_approved: true` because
the entry records an approval the customer has already granted; `false` contradicts the
input and must block every human-default gate. Include the exact `approval_ref` in the entry.
This may advance only the named
non-paid planning gates. It never authorizes paid generation, identity-sensitive sampling,
provider changes, publishing, or execution beyond the stated boundary.

## Runtime Selection (Planning Input)

Do not lock a runtime yet, but inspect the available render engines and note whether both
Remotion and HyperFrames are viable. Final `render_runtime_selection` occurs in proposal.

## Brief Metadata

Use the existing `brief.metadata` field for:

- `primary_goal: subject_affinity`,
- `subject_facts_profile_ref` and the OpenMontage-derived `subject_dossier_projection`,
- `platform_profile_id`, `platform_profile_ref`, `actual_target_platform`, and
  profile version and hash,
- `source_inventory` and lineage references,
- `project_content_context_ref` and `context_evidence_map`, including applied document/image/
  temporal anchors and unused or blocked evidence reasons,
- `episode_promise`,
- `audio_architecture`,
- `identity_protection`,
- creative capability needs and `capability_feasibility: pending_proposal_audit`,
- `reference_analysis_ref` when applicable.

Do not create a new canonical subject-dossier artifact.

## Quality Gate

- the job truly qualifies as subject IP,
- both profile references resolve and their hashes match,
- the subject is irreplaceable to the concept,
- facts, observations, interpretations, and generated fiction are separated,
- the platform affects the full direction,
- the audio architecture is explicit,
- duration has a logged editorial basis when the customer did not set it,
- creative requirements were selected before execution feasibility and missing capabilities
  remain visible rather than silently simplifying the concept,
- the brief validates against `brief.schema.json`.

## Gate Reminder

This stage requires human approval. After review, write `awaiting_human`, present the brief,
and end the turn. Do not advance to proposal until approval is recorded.
