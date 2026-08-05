# Reviewer Rubric — Golden Key Subject IP Pipeline

Use this rubric together with `skills/meta/reviewer.md`. It adds subject-IP semantic review;
it does not replace the OpenMontage reviewer or create a second review artifact.

Treat the resolved PlatformProfile as one of the native review layers described by
`skills/meta/reviewer.md`. Review the decisions that are actually relevant to the current
stage and cite concrete artifact fields, source ranges, or timecodes. Do not require a
second Golden Key review artifact or a mechanical echo of every platform rule ID.

## Critical Findings

Any critical finding must be fixed and re-reviewed:

1. **Wrong route:** primary goal is actually product sales, company proof, or lead conversion
   but the run remains in the subject-IP Pipeline.
2. **Unresolved context:** `subject_facts_profile_ref` or `platform_profile_ref` lacks
   ID/version/hash, cannot be
   resolved, or has no applied rules.
3. Unverified facts, motives, credentials, relationships, animal emotions, or generated
   behavior are presented as real evidence.
4. Likeness, voice, character, music, or source-media rights are missing.
5. **Identity drift:** subject identity anchors drift or a generated asset is presented as
   documentary footage.
6. The proposal lacks options considered/rejected reasons, required recipe fields, capability
   demands, or an explicit fallback/blocker.
7. **Silent substitution:** runtime, provider, voice, music, motion treatment, or composition
   mode changed silently.
8. A reference-driven production skips the approved 10–15 second sample checkpoint.
9. **Audio plan disappearance:** an approved narration/music requirement disappears because a
   provider is unavailable.
10. **Text-role collapse:** ordinary captions, expressive emphasis, titles, annotations, or
    CTA are treated as one universal subtitle layout, or the selected role contradicts its
    subtitle/overlay renderer path.
11. **Accidental ending:** the final subject beat, caption/CTA, BGM, or natural sound reaches the
    export boundary without an intentional landing treatment and dedicated last-second review.
12. **Capability-driven creative collapse:** the artifact removes or avoids narration, music,
    presenter, I2V, enhancement, or another editorially warranted layer because a provider or
    local executor is unavailable, instead of preserving the chosen direction and declaring
    explicit execution requirements plus an execution blocker. Merely documenting
    capability status at proposal is not a collapse when an independent creative, truth,
    rights, identity, or customer-governance reason already rejects that option and the
    unavailable capability did not change the selected direction.
13. **Unjustified duration:** the customer did not specify duration and no
    `duration_selection` entry compares at least two plausible bands using story, evidence,
    platform, audio, readability, and ending needs; or the selected duration is justified only
    by local execution convenience.
14. **Unrecorded pre-authorization:** a human-default planning checkpoint is auto-advanced
    without an `approval_policy` decision that matches the supplied actor, scope, reference,
    constraints, and excluded actions, or the matching entry does not set
    `user_approved: true`.
15. **Unreviewed or contaminated source audio:** at scene, asset, or edit stage, natural sound is retained without exact
    source ranges and persisted audio-analysis evidence, or a retained range overlaps crew
    direction, counting, prompting, or unrelated speech. Muting everything by default also
    fails: the artifact must contain an evidence-based Director decision for the selected
    ranges.
16. **Behavior-to-credential overclaim:** walking, arriving, sitting, looking focused, or
    another observable action is presented as proof of punctuality, honesty, project results,
    commercial competence, "never talks empty words," or a similar unverified trait.
17. **Invalid proposal handoff:** production-plan tools are not exposed by the active
    OpenMontage manifest/registry, the final compose tool contradicts the locked runtime, an
    unused optional field is null, CTA exists while its text role is false, or the ending is
    conditional on footage that has not been retrieved.
18. **Unverified arrival narrative:** observable movement is rewritten as an appointment,
    punctuality, repeated attendance, honesty, reliability, or project competence without a
    cited fact. Proposed fixes such as `按约出现` are equally invalid when the footage proves
    only arrival or walking.
19. **Invented or incomplete execution path:** a stage names tools not exposed by its
    OpenMontage manifest/registry, treats the reasoning Agent as an executable tool, or
    hand-waves unavailable narration, source-audio, generation, or composition as "manual
    FFmpeg" without an actual supported path.
20. **Availability-driven voice substitution:** an identity/tone-selected human or cloned
    voice is replaced by preset TTS because the former is unavailable, rather than preserving
    the ideal demand and blocker or recording an independent creative reason.
21. **Non-executable shot ledger:** `scene_plan.metadata.shot_plan` is missing a scene, hides
    lineage only in prose, lacks the applicable exact temporal range/speed or still/document
    anchor/display duration, disagrees with scene boundaries, leaves an unintended main-
    timeline gap/overlap, or violates the applicable timeline arithmetic.
22. **Unresolved ProjectContentContext:** the context ID/version/hash/project scope or frozen
    source revisions cannot be resolved, an empty selection triggers library retrieval, or an
    artifact uses an asset outside the selected/resolved snapshot.
23. **Invalid multimodal evidence use:** a fact, quotation, visible text, identity statement,
    or visual obligation lacks its context evidence ID and exact asset/revision/page/table/
    region/time anchor; or expired, conflicted, prohibited, non-referenceable, or
    permission-ineligible material is used.
24. **False temporal lineage:** a still image or document is given invented source in/out
    times, or a document/page/table/region shot lacks public-use permission, redaction,
    legibility, and display-duration checks.

A ready Golden Key `MaterialIndexSnapshot` plus its complete-ingest receipt and task-level
`material_query_result` satisfies Source Understanding Review. Do not require a duplicate
`source_media_review` or reopening every source file. At proposal, review the natural-sound
role and evidence source; exact retained ranges are intentionally deferred until shots exist.

When the canonical artifact schema uses only broad platform enums, do not require an
out-of-schema value such as `wechat_channels`, `xiaohongshu`, `douyin`, or `kuaishou` in
`target_platform`. Accept `target_platform: generic` only when
`metadata.actual_target_platform` and the resolved PlatformProfile reference establish the
real platform consistently and the artifact visibly applies its relevant constraints.

## Stage Review

### Idea

- eligibility and route-out are correct;
- the fact-only SubjectFactsProfile and resolved PlatformProfile actually affect the brief,
  while creative subject positioning is derived inside the OpenMontage brief;
- episode role, truth boundaries, source reality, and audio intent are explicit.
- duration is an editorial decision rather than a template or executor default;
- creative requirements precede capability feasibility, and any missing capability remains
  visible as an execution boundary.
- eligible ProjectContentContext documents, images, temporal observations, permissions,
  conflicts, expiry, prohibitions, and gaps visibly constrain the brief without pre-authoring it.

### Proposal

- concepts differ in narrative driver, media role, audio, and ending;
- vetoes are applied before scoring;
- the recommendation explains why alternatives were rejected;
- renderer family, runtime, composition mode, presenter, layout, I2V, audio, cost, and
  fallbacks are locked by the correct approval actors.
- text roles are chosen for content purpose before typography, and no universal character
  count replaces the task-specific decision.

### Script

- structure was selected for this subject rather than copied from a universal template;
- the subject remains irreplaceable;
- speech, behavior, and interpretation are grounded and correctly labeled.
- every context-backed line has exact multimodal evidence lineage and a permitted public use.

### Scene Plan and Assets

- every scene/asset has lineage or a synthetic designation;
- the chosen visual backbone may be real footage or approved character assets according to
  the decision policy;
- support solves a named gap and identity-sensitive generation has an approved sample.
- temporal assets have exact ranges; images and documents have exact anchors, display
  duration, permission, and legibility/redaction treatment.

### Edit and Compose

- the approved narrative driver and episode role remain visible;
- overlays and audio support rather than flatten the subject;
- continuous captions remain readable; expressive text follows its approved hierarchy; when
  both coexist, the attention policy prevents duplication and visual competition;
- runtime, identity, platform, disclosure, and technical QA pass.
- the final second was reviewed as a time sequence and the subject story lands cleanly.

### Publish

- packaging reinforces the subject and series continuity;
- CTA does not silently turn the episode into another business Pipeline;
- rights and disclosure records are complete.

## Content Performance Review

- the opening identifies a target viewer and one concrete promise, and the middle visibly
  starts paying it off rather than only delaying the answer;
- the script has one primary viewer payoff and at most one secondary payoff;
- every suspense setup resolves, viewpoint tension is evidence-grounded, and no conflict is
  manufactured for comments;
- the ending closes the episode before offering at most one natural interaction action;
- title, one-focus cover, evidence-bounded copy, and relevant tags match the actual video;
- early retention, average watch, completion, and interaction remain diagnostic hypotheses,
  not an official ranking formula, semantic pass condition, or release gate.

## Cross-Artifact Consistency

Compare `brief -> proposal_packet -> script -> scene_plan -> asset_manifest ->
edit_decisions -> render_report/final_review -> publish_log` for:

- identical subject/profile references and versions,
- stable episode role and primary goal,
- justified changes recorded in the append-only decision log,
- recipe projection fields carried forward,
- stable PlatformProfile reference and visible platform-fit decisions,
- source lineage, rights, identity anchors, audio decisions, capability state, and fallback.
- stable ProjectContentContext reference, frozen source revisions, exact evidence anchors,
  permissions, validity, conflicts, prohibitions, and source-scope discipline.

If the artifacts are schema-valid but could describe any other subject with only a name swap,
the semantic review fails.
