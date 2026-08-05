# Text Layer Direction

Use this skill whenever a video may contain subtitles, word highlighting, expressive text,
titles, annotations, or CTA copy. It guides a Director decision inside existing OpenMontage
artifacts; it does not add a new pipeline, renderer, or canonical artifact.

## Decide the Content Role First

Classify each approved visible-text layer by what it does:

1. `continuous_caption`: carries complete source speech or narration for reading;
2. `expressive_emphasis`: selectively amplifies a keyword, emotion, contrast, or beat;
3. `title_or_section`: introduces the piece or a structural section;
4. `cta`: asks for one approved audience action;
5. `annotation`: labels evidence, a person, place, product element, number, or context.

Do not classify by appearance alone. A four-character phrase can be a complete ordinary
caption in one task and a large emphasis card in another. The content role, reading burden,
timing, hierarchy, platform, subject-safe zone, and approved visual treatment decide.

## Route Through Existing Capabilities

| Role | Canonical delivery | Existing renderer paths |
| --- | --- | --- |
| Continuous caption | `edit_decisions.subtitles` | `subtitle_gen` + FFmpeg sentence burn, or `subtitle_gen` + `remotion_caption_burn` for active-word treatment |
| Expressive emphasis | `edit_decisions.overlays` | Remotion Overlay or HyperFrames component; static approved assets may use `video_compose` overlay |
| Title / section | `edit_decisions.overlays` | Remotion, HyperFrames, or approved static `video_compose` overlay |
| CTA | `edit_decisions.overlays` | Remotion, HyperFrames, or approved static `video_compose` overlay |
| Annotation | `edit_decisions.overlays` | Remotion callout, HyperFrames component, or approved static `video_compose` overlay |

One video may use continuous captions and a small number of emphasis overlays. Record an
`attention_policy` explaining when the emphasis layer appears and how it avoids competing
with the continuous caption, subject, or evidence.

## Layout Is Task-Specific

For continuous Chinese captions, preserve sentence and clause readability, but do not turn
a common character-count recommendation into a universal rule. Determine line capacity from
the selected font, frame, safe zone, speech speed, sentence structure, and approved density.

Expressive text may deliberately use four characters, two characters per line, or a single
character. Its line shape is part of the approved motion and hierarchy, not ordinary-caption
pagination.

## Record and Validate

Write `edit_decisions.metadata.text_layer_direction` with:

- `layers[]`: `layer_id`, `role`, `delivery`, `renderer`, and `reason`;
- `asset_ids` for overlay-delivered layers;
- `attention_policy` when subtitle and overlay text coexist.

Use a `motion_commitment` decision-log entry for the selected text-layer treatment and
rejected alternatives. Before the edit checkpoint, run
`lib.text_layer_direction.assert_text_layer_direction(edit_decisions, require=True)`.

The validator checks role/delivery/renderer/runtime consistency and overlay asset references.
It deliberately does not impose universal character counts, line counts, or font sizes.
