# Director Decision Policy — Golden Key Subject IP Pipeline

## Purpose

This policy is the selection intelligence shared by every stage. It does not prescribe one
fixed format. It tells the Director how to choose, reject, degrade, or block a production
approach from the goal, subject, evidence, platform, rights, and live capabilities.

The Executive Producer and every stage director must read this policy. Decisions are written
into existing canonical artifact metadata and the append-only `decision_log`; this file does
not create a new canonical artifact or a Python orchestrator.

## Resolved Context Contract

Do not plan until the Golden Key control plane supplies these validated inputs or explicit
unknowns:

- `subject_facts_profile_ref`: ID, version, hash, owner, and a fact-only projection containing
  subject type, identity statement, verified facts, identity anchors, rights, and
  prohibitions. Content pillars, established creative traits, episode role, series direction,
  expression rules, duration, and story treatment are OpenMontage decisions and must not be
  supplied as Golden Key authority;
- `platform_profile_ref`: ID, version, hash, and the actual resolved rules relevant to this
  task—not only a filename;
- `project_content_context_ref`: ID, version, hash, project scope, frozen selected/resolved
  source revisions, exact multimodal anchors, permissions, validity, conflicts, prohibitions,
  warnings, and gaps. It is evidence only and supplies no episode role or treatment;
- source inventory and `source_media_review` when user media exists;
- task goal, audience, duration, and reference analysis; live capability snapshot is supplied
  at proposal only, after idea has established the ideal creative treatment;
- rights/consent state for likeness, voice, character, source media, and generated treatment.

An unresolved reference is not usable context. Ask one question at a time for customer facts;
use an internal blocker for technical or rights gaps.
`selection_mode: none` forbids project-library retrieval. Every material-backed decision must
cite an eligible asset/revision/anchor inside the frozen project scope; conflicts, expiry,
prohibitions, and public-use permissions are binding.
Carry these uses and blocked reasons forward as `context_evidence_map` in canonical artifact
metadata; it is a lineage projection, not a new artifact or an upstream creative answer.

### Decision order is binding

Apply this order for every concept: `goal and evidence -> platform and audience -> ideal
creative/audio treatment -> duration -> capability feasibility -> execute, fallback, or
block`. Runtime availability may classify a selected direction as executable or blocked; it
must not reach backward and erase narration, music, presenter, generation, or enhancement
that the Director selected for an editorial reason. A fallback is valid only when it still
delivers the same approved promise and is chosen on creative grounds, not merely because it
is cheap or locally available.

## 1. Eligibility and Route-Out

Use this Pipeline only when the primary outcome is subject recognition, affection, trust,
authority, identification, or series continuity.

Route out before the `idea` checkpoint when another obligation dominates:

| Dominant obligation | Route |
| --- | --- |
| prove a product benefit and drive purchase/trial | `golden-key-product-marketing` |
| prove company/brand capability or history | `golden-key-brand-company` |
| qualify leads and drive one conversion action | `golden-key-lead-conversion` |
| extract many clips from one long source | `clip-factory` |
| only translate/dub an existing finished video | `localization-dub` |
| create a new reusable rig, pose library, or character acting system | `character-animation` prerequisite or separate production |

Block rather than route when likeness/voice/character rights are missing, identity cannot be
protected, or the requested factual claim has no evidence.

## 2. Select the Episode Role

Choose one primary `episode_role`; secondary roles may support it but may not rewrite it:

- `recognition`: establish who the subject is and one memorable trait;
- `affinity`: create warmth, delight, empathy, or emotional closeness;
- `authority`: demonstrate expertise through verified speech or action;
- `trust`: show consistent values, process, honesty, or relationship evidence;
- `personal_story`: reveal an experience or change that explains the subject;
- `series_continuity`: deepen an already established character or recurring device.

If the proposed role is mainly direct conversion, reroute or make conversion explicitly
subordinate. Do not disguise a sales video as “IP content.”

## 3. Choose the Narrative Driver

Evaluate candidates, then select one primary `narrative_driver`:

| Candidate | Use when | Do not use when |
| --- | --- | --- |
| `observed_action` | real behavior/action itself carries personality or relationship | footage is ambiguous or requires invented motive |
| `original_voice` | a person's existing speech is strong, authentic, and authorized | audio is unusable or the words do not support the episode promise |
| `direct_address` | the subject can credibly explain, comment, teach, or invite | an animal cannot speak; an avatar would damage authenticity |
| `narration` | context, contrast, inner framing, or emotional meaning is otherwise missing | it merely describes what viewers already see or overpowers a strong original voice |
| `expressive_captions` | short, visually clear behavior needs a light meaning layer | the story requires nuance that captions cannot carry legibly |
| `character_performance` | an approved virtual character/mascot design and motion system are the truth source | a reusable rig/design must first be created or rights are unclear |
| `hybrid` | two drivers are genuinely co-primary and each solves a distinct need | “hybrid” is only a label for using every available capability |

### Minimalist micro-short suitability check

Do not treat the absence of speech, many locations, or a long story as a material failure.
Evaluate an 8–15 second minimalist micro-short as a real concept candidate when verified
source evidence contains one visually legible subject action (for example walking, arriving,
working, looking, or a recognizable gesture) and one emotional or identity promise can land
through `expressive_captions` plus intentional BGM. This route is strongest for `recognition`
or `affinity`; it cannot establish authority, biography, or a specific viewpoint without
additional verified evidence.

Minimalist suitability is a candidate, never an automatic downgrade. “No configured voice
provider”, “no local I2V”, or “FFmpeg is the only current executor” is not evidence that a
caption-led micro-short is the best creative direction.

When the source is verified at 50/60 fps and delivery is 25/30 fps, deliberate slow motion
may extend and emphasize the action without synthetic interpolation. Record source fps,
delivery fps, speed, resulting duration, and the exact problem the speed change solves. Do
not infer frame rate from appearance, use slow motion to hide an unusable take, or label
low-frame-rate interpolation as source-derived slow motion.

## 4. Choose Presenter, Visual Backbone, and Layout

### Presenter mode

- `none`: observed action, montage, or animation is sufficient;
- `real_original`: retain strong authorized original speech;
- `real_rerecord`: the real subject should speak but source audio is missing or structurally weak;
- `authorized_avatar`: use only with likeness rights and when repeatable delivery is worth the authenticity tradeoff;
- `authorized_voice_clone`: use only with explicit voice authorization and a sample gate.

Never choose an avatar or cloned voice merely because the tool is available.

### Visual backbone

- `real_source`: real person/animal behavior or environment is the evidence;
- `approved_character_assets`: virtual character/mascot design is the identity truth and animation may be primary;
- `presenter_plus_broll`: direct address supplies meaning while B-roll proves or enriches it;
- `narrated_source_story`: source footage supplies truth while narration supplies structure;
- `mixed_support`: generated/graphic support fills named gaps around a coherent anchor.

### Layout strategy

Choose full-screen, picture-in-picture, upper/lower split, comparison, or overlay only when it
solves simultaneous meaning, proof, demonstration, or platform legibility. Split-screen is
not a default for presenter-plus-footage; use full-screen alternation when simultaneous view
adds no information.

## 5. Choose the Audio Treatment

Select an explicit primary meaning carrier and music decision:

| Situation | Preferred treatment | Reject |
| --- | --- | --- |
| strong authorized human speech | original voice + captions + supportive BGM/natural sound | replacing authentic speech with generic TTS |
| animal behavior story | narration or expressive captions + emotionally shaped BGM + selected natural sound | pretending the animal literally spoke or felt an unverified motive |
| quiet observational piece | minimal narration/captions + intentional music or approved music-free design + meaningful natural sound | accidental silence caused by missing providers |
| minimalist subject micro-short | one legible action + 2–4 expressive text beats + intentional BGM, with verified high-frame-rate slow motion when useful | calling limited footage “insufficient” before testing the smallest complete form |
| expert/authority episode | original/rerecorded voice, restrained music, clarity-first captions | playful voice that weakens credibility |
| virtual character/mascot | approved character voice or caption-led performance + designed music/SFX | unapproved voice or inconsistent character delivery |

If narration is essential and no authorized/available voice path exists, offer recording,
bring-your-own audio, a configured provider, or block. Do not silently deliver natural sound
as the finished audio plan. Music-free treatment needs a creative reason and approval.

## 5b. Select Duration Editorially

If duration is not supplied, compare at least two plausible bands. Judge each against hook
time, number of evidence beats, spoken-copy feasibility, source variety, platform rhythm,
CTA/readability clearance, and the intended emotional landing. Log `duration_selection`
with alternatives and evidence. Do not default all batch members to one range; a batch may
share a range only when each member's concept independently justifies it.

The exact runtime becomes binding at proposal. Later stages may change it only through a new
logged decision with cross-artifact updates and the proper approval actor.

## 5c. Multi-Output Batch Ownership

When one user command requests multiple new videos, the OpenMontage Agent owns portfolio
direction. Run one separate OpenMontage Project and canonical artifact chain per deliverable,
serially or as isolated jobs. Before directing the next deliverable, read the prior projects'
approved concepts and deliberately vary at least two substantive dimensions such as episode
role, narrative driver, hook, source subset, audio carrier, emotional curve, duration
rationale, or ending. Do not accept a Golden Key-authored concept matrix or prewritten
variant as creative truth. Golden Key may create job identities and pass prior OpenMontage
artifact references, but may not choose the differences.

If the evidence cannot honestly support the requested count without cosmetic repetition,
reduce the portfolio or stop with a source-coverage blocker rather than padding quantity.

## 6. Decide Whether Support or I2V Is Needed

For every proposed support layer, record the problem it solves. Use it only if the source or
approved character assets cannot solve that problem more honestly.

Use I2V/generated video only when:

1. motion has a named narrative purpose;
2. source/approved reference identity anchors are sufficient;
3. the selected provider can preserve the required elements;
4. the invented motion is not presented as documentary evidence;
5. a sample, attempt budget, disclosure, and fallback are approved.

Prefer a real select, real reshoot, static composition, restrained camera move, or graphic
explanation when those options solve the need with less identity or truth risk. Block if the
only available generation path would change identity, fabricate behavior, or violate rights.

## 7. PlatformProfile Application

Translate resolved platform rules into stage decisions:

- idea: audience promise, emotional value, hook window, and endpoint;
- proposal: concept ranking, pacing range, audio density, visual grammar, and cost priority;
- script: sentence length, hook form, information/emotion balance, and CTA intensity;
- scene/edit: first frame, shot rhythm, caption safe zones, subject scale, and overlay limits;
- publish/review: cover, copy, metadata, disclosures, and platform-specific failure checks.

Record the applied rule IDs. A platform reference with zero applied rules is a critical
finding, not a valid implementation.

## 8. Candidate Scoring and Vetoes

Generate at least three concepts as required by `proposal_packet`, but rank them internally
before presenting the recommended direction.

First apply vetoes: rights, truth, identity preservation, required capability, and primary
goal mismatch. A vetoed concept cannot win on style or cost.

An unavailable required capability does not veto the creative concept at Director
acceptance. It vetoes immediate execution and creates an explicit execution blocker. Compare
creative merit independently from immediate executability, then report both.

Score remaining concepts from 0–5 on:

- primary-goal fit,
- subject authenticity/continuity,
- evidence and source coverage,
- PlatformProfile fit,
- emotional or authority clarity,
- capability feasibility,
- cost/time proportionality.

Record the selected concept, options considered, rejected reasons, execution requirements, and
approved fallback. Golden Key customers see one recommended natural-language direction;
the full technical shortlist remains available to the designated OpenMontage approval actor.

## 9. Required Recipe Projection

The selected proposal and downstream canonical artifacts must allow a derived view of:

- `episode_role`, `narrative_driver`, `presenter_mode`, `visual_sources`,
- `layout_strategy`, `text_layer_direction`, `audio_treatment`, `source_support_policy`,
- `image_to_video_plan`, `platform_profile_ref`, `execution_requirements`,
- `review_obligations`.

These fields live in existing artifact metadata and decisions. They are not a new canonical
`ProductionRecipe` artifact.

`text_layer_direction` is selected by content role before typography: distinguish continuous
captions from expressive emphasis, titles/sections, CTA, and annotations; then record the
existing subtitle or overlay renderer path and reason. Do not use one character-count rule
as a proxy for this decision.
