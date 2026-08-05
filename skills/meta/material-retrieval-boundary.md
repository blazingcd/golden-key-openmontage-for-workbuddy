# Material Retrieval Boundary

Use this Skill whenever Golden Key supplies a versioned `ProjectContentContext`,
`MaterialIndexSnapshot`, or `MaterialQueryResult` to an OpenMontage Pipeline. The
`ProjectContentContext` is the stable Director-facing evidence adapter for the user's
project selection. It may contain cited facts and excerpts from business documents, cited
visual observations from images or video, brand rules, prohibited expressions, conflicts,
expiry state, permissions, warnings, and evidence gaps. It is not a creative brief.

## Project Content Context Contract

- Resolve the context reference, version, hash, project ID, status, selection mode, and its
  frozen selected/resolved source revisions before using any evidence.
- Use only adopted facts, excerpts, visual references, brand rules, and prohibitions that
  carry an exact citation to `asset_id`, `content_revision_id`, `understanding_revision_id`,
  and `anchor_id`. An anchor may identify a document page, table cell, image region, or
  temporal range.
- The Director may reason from an item only when its eligibility allows `director_context`.
  Spoken copy, visible copy, document crops, logos, prices, offers, or public claims also
  require the applicable public-use permission. Confidential context can constrain a plan
  without being quoted or shown publicly.
- Expired, released, still-processing, needs-attention, unusable, integrity-failed, or
  non-referenceable understanding revisions are not evidence. Preserve them as warnings or
  gaps; do not repair or reinterpret them inside OpenMontage.
- An unresolved conflict is never settled by picking the newest-looking value, the first
  value, or the retrieval score. Ask the one business-language question identified by the
  context and stop the affected claim/decision until a new context revision resolves it.
- `selection_mode: none` is valid. It means no project material was selected: do not query
  or reopen the wider library. Direct only from other verified Handoff facts, and surface
  missing evidence honestly.
- Never access raw project folders, storage paths, vector indexes, OCR internals, or parser
  output outside this adapter. Golden Key owns parsing and context construction; OpenMontage
  owns all creative interpretation and canonical artifacts.

## Authority

- The snapshot is the full, task-independent record of parsed source assets, observable
  semantics, reusable ranges, audio analysis, unresolved gaps, and provenance.
- A pre-Handoff `initial_coverage` result is an unranked view of every eligible segment. It
  is evidence for route and concept reasoning, not a shortlist, hero-shot choice, edit order,
  or duration recommendation.
- Golden Key executes retrieval and preserves hashes. It does not author concept-specific
  requirements, rank creative directions, select final assets, choose exact ranges, or write
  a canonical OpenMontage artifact.
- The OpenMontage Agent owns every concept-specific query and every final material decision.
  Final source path, `source_in`, `source_out`, speed, order, audio treatment, fallback, and
  generation need belong only in the canonical OpenMontage stage artifacts.

Ignore any upstream field that attempts to recommend a concept, runtime, script, shot,
source range, edit order, audio choice, or generation treatment. Record the conflict in the
OpenMontage decision log and rederive the decision from the active Manifest and Stage Skills.

## Stage Order

1. At Idea, read the complete snapshot and unranked initial coverage to understand what is
   observable, what is missing, and what rights or analysis limits apply. Also project the
   eligible document facts, excerpts, image observations, brand rules, prohibitions,
   conflicts, expiry state, and evidence gaps from `ProjectContentContext` into the brief
   metadata with exact citations. Do not select shots.
2. At Proposal, compare at least three structurally different concepts on creative promise,
   evidence, platform, truth, rights, and identity. Select the winning concept before reading
   capability convenience and before issuing a concept-specific material query.
3. After concept selection, the OpenMontage Agent may author `MaterialQueryRequest@0.2` with
   `request_owner=openmontage_agent`, `request_stage=proposal`, and a
   `creative_decision_ref` pointing to the selected-concept decision. Golden Key may execute
   that request as a retrieval-only service.
4. At Script, a narrower `shot_candidates` query is allowed only for a named evidence need
   created by the approved concept or script. It must cite the relevant OpenMontage decision.
5. At Scene Plan, use `exact_range_review` or the Manifest's native inspection tools for the
   provisional source requirements. Reinspect frames/audio when `exact_review_required=true`.
   The query result remains a candidate set; the Scene Director writes the final exact range.

## Multimodal Scene Lineage

- Temporal video/audio selections carry exact source path, `source_in`, `source_out`, speed,
  audio treatment, and the cited temporal anchor. Validate timeline duration as
  `(source_out - source_in) / speed`.
- Still-image selections carry exact source path, cited image-region or whole-asset anchor,
  crop/fit, display duration, motion treatment, and fallback. Do not invent `source_in` or
  `source_out` for a still.
- Document selections carry exact source path, page/table/cell/region anchor, render/crop
  instruction, legibility and redaction checks, display duration, public-use permission, and
  fallback. A document fact may support narration without showing the document; the script
  still cites its anchor.
- Every selected item records its `asset_id`, content and understanding revisions, context
  evidence ID, narrative/evidence role, and selection reason. Query rank never replaces this
  Director decision.

## Query and Evidence Rules

- Never copy the whole initial coverage into a timeline.
- Never treat retrieval order or score as Director preference.
- A query may return zero candidates; preserve the gap and decide whether the concept still
  works, needs an explicit generated/support requirement, or must return for truth review.
- Candidate summaries are observable-evidence aids, not permission to strengthen claims.
- Do not let a similarly named product, cross-project material, a newer library revision, or an
  unselected asset enter the run. Every selected source must belong to the context's frozen
  selected/resolved source snapshot.
- Cite the snapshot, request, result, and exact inspection evidence in the OpenMontage
  artifact or decision log that uses them.
- Do not create a parallel shot list or Golden Key creative artifact. `scene_plan` remains the
  one executor-facing shot truth.
