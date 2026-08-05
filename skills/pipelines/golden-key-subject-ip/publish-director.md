# Publish Director — Golden Key Subject IP Pipeline

## Purpose

Package the approved render so the subject becomes recognizable across episodes and the
actual platform receives coherent title, cover, copy, provenance, and disclosure guidance.

## Platform Packaging

Read `platform_profile_ref` and apply the approved profile to:

- title and opening promise,
- caption/body copy,
- cover frame or cover concept,
- hashtags/topics when appropriate,
- first-frame and autoplay behavior,
- ending and follow/next-episode CTA,
- review or moderation notes.

Do not reuse one generic caption across Xiaohongshu, Douyin, Kuaishou, and WeChat Channels.
Record the profile version used so operators can later audit or upgrade the packaging logic.

Apply the profile's performance packaging contract: the title names one truthful pain,
question, relationship, or value; the mobile cover has one visual focus and one information
promise; post copy carries only evidence-supported emotion; and tags match the subject,
episode, scene, and audience rather than unrelated trends. Request at most one primary
interaction action, and omit it when the approved ending is stronger without a CTA.

## Subject Continuity

Maintain a series-facing summary in `publish_log.metadata`:

- approved name and subject type,
- recurring traits established by this episode,
- visual/audio recognition devices,
- facts and interpretations introduced,
- continuity rules for the next episode,
- thumbnail/cover pattern without forcing a repetitive template.

The CTA should normally support recall, follow, conversation, or the next episode. Do not
insert an unrelated product, company, or lead-generation CTA at publish time.

## Rights and Disclosure

Confirm and record:

- source-media ownership or permission,
- person likeness/voice consent where applicable,
- animal welfare and owner permission where applicable,
- virtual-character/mascot usage rights,
- music and sound licenses,
- generated or materially altered media disclosure,
- platform-specific disclosure requirements supplied by the current profile.

## Export Package

Include the approved video, cover guidance or asset, platform copy, subtitle/caption files,
provenance references, decision-log reference, rights/disclosure notes, and any variant
exports. Clearly label master and derivatives.

## Quality Gate

- package matches the actual platform and profile version,
- copy reinforces the approved subject identity and episode promise,
- series continuity is recorded,
- CTA does not change the primary objective,
- rights and disclosures are complete,
- output validates against `publish_log.schema.json`.

## Gate Reminder

This stage requires human approval. Write `awaiting_human`, present the final package and
review, and end the turn. Publish externally only under separate explicit authorization.
