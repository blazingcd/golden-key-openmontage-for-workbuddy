# Compose Director — Golden Key Subject IP Pipeline

## Purpose

Render the approved subject-led edit and produce canonical `render_report` and
`final_review` artifacts. Composition is execution of approved decisions, not a new creative
route-selection stage.

## Runtime Routing (MANDATORY First Step)

Read `edit_decisions.render_runtime` and compare it with
`proposal_packet.production_plan.render_runtime`.

- `remotion`: compose source footage, captions, React overlays, and timed media.
- `hyperframes`: use only when the approved treatment is HTML/CSS/GSAP-native.
- `ffmpeg`: use only for an explicitly approved simple source-led cut.

Pass `proposal_packet` to `video_compose.execute()` so runtime swap detection can run. A
silent Remotion/HyperFrames/FFmpeg substitution is a critical governance violation. If the
locked runtime is unavailable, stop, report the blocker, present alternatives, obtain user
approval, and append a revised `render_runtime_selection` decision before proceeding.

## Caption Routing Through Existing OpenMontage Tools

Read the existing `edit_decisions.subtitles` object; do not invent a second caption artifact
or extend its Schema during compose.

Before routing, preserve the approved text-layer role from proposal/edit decisions. Do not
treat every user-visible Chinese text element as the same kind of subtitle:

- Continuous speech/narration captions carry complete reading content. Sentence integrity,
  punctuation, reading speed, safe zones, font size, and aspect ratio determine their lines.
  In a typical vertical ordinary-caption treatment, roughly 12-15 Chinese characters per
  line can be a useful starting recommendation, but it is not a universal minimum, maximum,
  or acceptance rule.
- Expressive emphasis text, kinetic typography, large keyword callouts, section titles, and
  CTAs are display/overlay treatments. They may deliberately use one short phrase, four
  characters, two characters per line, or even a single character when the approved visual
  hierarchy and rhythm justify it. Route them through the approved Remotion overlay or
  HyperFrames component path instead of forcing ordinary-caption pagination onto them.
- A video may use both layers. Keep the continuous caption readable and use emphasis text
  selectively; do not duplicate every spoken phrase as a competing large text layer.

The Director must record the text layer's content role, visual treatment, and reason in
`decision_log` / `edit_decisions.metadata` before compose. Compose executes that decision;
it does not infer a universal character count.

- `style: sentence` with `render_runtime: ffmpeg`: use the existing subtitle path in
  `video_compose`. `bottom-center` is the normal social-video position; use `top-center` only
  when the approved subject-safe zone or platform UI makes the lower area unusable.
- `style: word-by-word` with `render_runtime: remotion`: resolve the source video and the
  word-timed subtitle asset from `asset_manifest`, then call `remotion_caption_burn`. Reuse an
  existing browser and prepared `remotion-composer`; do not allow a first-run browser or npm
  download during compose. For CJK captions, preserve semantic tokens, use
  explicit `page_id` and `line_break_after` boundaries when the language needs semantic
  layout. For ordinary continuous Chinese captions, prioritize complete sentences and
  punctuation, then apply the approved task-specific line capacity and safe-zone treatment.
  Character counts and line counts are layout inputs selected for that composition, not
  universal Chinese-caption rules. Split at a natural phrase boundary only when the approved
  continuous-caption layout cannot keep the clause intact.
  `max_words_per_line` remains a compatibility fallback for assets without explicit layout.
  Visually verify that a token is
  never split across lines.
- HyperFrames caption components are available only when `render_runtime: hyperframes` was
  approved. Run `hyperframes_compose` doctor and use its existing Registry component path for
  a templated composition. After scaffold/add/wiring and visual approval, render that existing
  workspace through `hyperframes_compose` operation `render_workspace`; do not bypass the tool
  with a direct CLI call. Do not describe a component as Pipeline-qualified until the
  canonical workspace passes lint, validate, visual inspection, and render.

If a selected caption path is unavailable, stop. Do not silently convert word highlighting
or editorial emphasis into ordinary FFmpeg subtitles.

## Composition Checks

Render exactly the approved scene order, crop plan, overlays, captions, transitions, grade,
and ending. Do not introduce a new template look at compose time. For atelier mode, follow
the approved art direction and project-local composition; for templated mode, stay within
the approved component treatment.

## Subject Identity QA

Inspect representative frames and all synthetic transitions for applicable anchors:

- face/voice/body consistency for people,
- markings/proportions/gait and welfare for animals,
- silhouette/palette/design/lore for virtual characters,
- approved design and role for mascots.

Record pass/fail evidence in `final_review`. Synthetic content must not appear to prove an
unrecorded real behavior or event.

## Audio QA

Verify:

- narration or source speech is intelligible,
- captions match the approved carrier and timing,
- BGM follows the approved emotional curve and ducks under speech,
- natural-sound moments remain audible where planned,
- loudness and transitions feel like one finished mix,
- no approved audio layer disappeared as an unlogged fallback.

## Platform and Technical QA

Check duration, frame size, frame rate, codec, audio stream, full decode, crop safety, caption
safe zones, first frame, cover candidates, and end-frame readability. Apply the referenced
PlatformProfile's review rules, not only generic ffprobe validation.

Inspect the ending as motion and sound. Sample approximately `duration-1.0s`,
`duration-0.5s`, and `duration-0.1s`, play through the audio tail, and record
`final_review.checks.ending_closure`. An evenly sampled contact sheet is insufficient. Fail the
review when the subject beat, final text, or audio is cut off by the export boundary, even when
ffprobe, decode, and duration checks pass.

## Deliverables

The `render_report` must record runtime, composition mode, output paths, encoding profile,
tool/provider decisions, technical validation, audio checks, and decision-log reference.
The `final_review` must record subject identity, story, platform, disclosure, and audio
findings with blockers clearly separated from warnings.

## Quality Gate

- runtime and composition mode match approvals,
- output exists and passes ffprobe plus full decode,
- identity and disclosure QA pass,
- audio feels finished,
- ending closure has dedicated tail evidence and passes,
- platform review passes,
- both artifacts validate against their schemas.
