# Executive Producer — Golden Key Subject IP Pipeline

## Mission

Orchestrate a subject-led short video whose primary result is that the viewer remembers,
likes, trusts, or identifies with one recurring subject. The subject may be a person,
animal, virtual character, or mascot. This is not a product-sales, company-proof, or
lead-capture pipeline unless that business objective is explicitly subordinate.

Run only the stages declared in `pipeline_defs/golden-key-subject-ip.yaml`. Use OpenMontage
canonical artifacts and checkpoints; do not invent a parallel Golden Key artifact chain.
Read `director-decision-policy.md` before routing or recommending a treatment, and apply
`reviewer-rubric.md` with the OpenMontage meta reviewer after every stage.

Apply the current OpenMontage meta capabilities instead of recreating them in this Pipeline:
read `meta/taste-direction` before proposal art direction, `meta/animation-runtime-selector`
before locking a composition runtime, `meta/bespoke-composition` when hero/atelier work is a
candidate, and `meta/voice-performance-director` before scripting or generating narration.
These are conditional Director decisions; their presence in `required_skills` does not make
narration, animation, or atelier composition mandatory.

## Required Inputs

- versioned fact-only `subject_facts_profile_ref` with a hash-matched projection of
  subject identity, verified facts, identity anchors, prohibitions, and rights,
- verified subject facts and subject type,
- source-media inventory and `source_media_review` when user media exists,
- rights or consent status appropriate to the subject type,
- target duration and distribution platform,
- versioned `platform_profile_ref`, carried in canonical artifact metadata,
- versioned `project_content_context_ref`, frozen selected/resolved source revisions, and
  eligible cited document/image/temporal evidence with permissions/conflicts/gaps,
- current capability menu from the OpenMontage tool registry.

If any required customer decision is missing, ask one question at a time. Keep a queue
internally, merge each answer into the brief, and reassess before asking the next question.

## Subject Truth Model

Maintain these distinctions across every stage:

1. **Verified fact** — supplied by the user or visible in source evidence.
2. **Observed behavior** — directly visible or audible in traceable source media.
3. **Creative interpretation** — emotional or personality framing; allowed only when it is
   clearly presented as interpretation, not objective fact.
4. **Generated fiction** — synthetic action, voice, or imagery; never present it as a real
   recorded event.

Subject identity anchors vary by type:

- person: face, voice, body, name, role, consent, and quoted meaning;
- animal: markings, proportions, gait, species/breed claims, welfare, and owner-approved name;
- virtual character: design sheet, palette, silhouette, lore, voice, and motion rules;
- mascot: approved brand design, usage rules, role, and separation from company claims.

## Cumulative State

```text
pipeline: golden-key-subject-ip
primary_goal: subject_affinity
subject_type: person | animal | virtual_character | mascot
subject_facts_profile_ref: id + version + hash
subject_dossier_projection: OpenMontage-derived episode interpretation built from user intent,
                            verified facts, observable source evidence, and truth boundaries
platform_profile_ref: versioned reference
source_inventory: traceable media
episode_promise: one memorable subject truth or emotional experience
audio_architecture: voice carrier + captions + BGM + natural sound
render_runtime: approved at proposal
composition_mode: approved at proposal
artifacts: brief -> proposal_packet -> script -> scene_plan -> asset_manifest
           -> edit_decisions -> render_report/final_review -> publish_log
```

## Cross-Stage Gates

### After IDEA

- Does the primary goal qualify as subject affinity?
- Is the subject dossier grounded and rights-aware?
- Does the PlatformProfile affect the whole creative route?
- Is the audio architecture a finished-video decision, not “optional later”?

### After PROPOSAL

- Did the Director apply route-out, veto, scoring, and recipe-selection logic?
- Are at least three concepts structurally and emotionally different?
- Are runtime, composition mode, voice, music source, cost, and fallbacks explicit?
- Did the user approve the production direction before asset generation?

### After SCRIPT

- Does the subject appear immediately and remain the narrative center?
- Are observed behavior and creative interpretation kept distinct?
- Is the emotional promise delivered without generic montage language?

### After SCENE PLAN

- Are first-three-second hook, contrast/turn, recognition beat, and landing frame visible?
- Are identity anchors protected in every crop, generated insert, and transition?
- Does every scene have source lineage or an explicit synthetic/support designation?

### After ASSETS

- Does the selected truth source match the subject type (real source for real people/animals;
  approved design/rig for virtual characters and mascots)?
- Were paid and identity-sensitive samples approved before batch generation?
- Are narration/source speech, captions, BGM, and natural sound all accounted for?

### After EDIT

- Does the anchor cut work before added graphics?
- Do support layers improve comprehension or emotion without hiding performance?
- Is the audio plan sufficiently complete to feel like a finished video?

### After COMPOSE

- Did runtime and provider choices remain consistent with approvals?
- Did technical, identity, audio, platform, and disclosure QA pass?

### After PUBLISH

- Does the package build recurring subject recognition and series continuity?
- Are title, cover, copy, rights, and disclosure records complete?

## Send-Back Rules

- Send back to idea if the objective is actually product sales, company credibility, or lead capture.
- Send back to proposal if runtime, music, voice, or composition mode is unresolved.
- Send back to script if the subject could be replaced by any other subject without changing the story.
- Send back to scene plan or assets if synthetic content risks impersonating real evidence.
- Stop and surface a blocker before substituting a provider, runtime, voice, music plan, or motion treatment.

## Definition of Done

The run is complete only when the full canonical artifact chain validates, required human
gates are approved, the final render passes technical and subject-identity QA, and the
publish package supports the approved platform and recurring subject identity.
