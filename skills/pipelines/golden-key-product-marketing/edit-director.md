# Edit Director — Golden Key Product Marketing

Build the source-led anchor cut first. Use exact `edit_decisions.cuts` source in/out values
from the canonical shot plan and explain why each range exists. Check full-duration coverage,
benefit-proof adjacency, first-three-second hook, hero moment, emotional/information curve,
CTA intensity, vertical crop safety, and fallback.

Then add only approved narration/source speech, music, natural sound, SFX, subtitles,
expressive overlays, and generated support. Preserve the proposal renderer family, runtime,
composition mode, audio architecture, claim boundary, and source truth without silent swap.

Record `edit_decisions.metadata.source_audio_policy` with an evidence-based `mode` (`mute`,
`replace`, `retain_selected`, or `duck_selected`), `reviewed: true`, reason, volume, exact
retained ranges with `source_asset_ref`, and persisted material audio-analysis evidence.
Retained ranges must not overlap crew direction, counting, prompting, or unrelated speech.
This is a per-concept Director decision, not a default mute/retain rule.

Record `metadata.text_layer_direction` and run `assert_text_layer_direction(..., require=True)`.
Continuous captions, emphasis, titles, annotations, and CTA must use their approved roles and
an attention policy when mixed. Do not use a fixed character count as Director logic.

Plan the ending as a named story beat, not merely the final source cut. Record an explicit
`metadata.ending_treatment` with the intended landing frame, last readable text time, visual
release (for example a natural action resolve, short hold, dissolve, or fade), audio tail, and
why that treatment closes this concept. A final hard cut is valid only when it is an intentional
high-energy punctuation that the concept and PlatformProfile support. It is a critical defect
when the last picture, caption, or music simply stops at the export boundary. Reserve enough
time after the final CTA or brand line for the viewer to read it and feel the close.
