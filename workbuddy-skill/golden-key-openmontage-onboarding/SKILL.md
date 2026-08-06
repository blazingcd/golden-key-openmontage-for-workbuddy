---
name: golden-key-openmontage-onboarding
description: Guide new or uncertain WorkBuddy users into Golden Key OpenMontage with plain-language Chinese choices grounded in the locally available WorkBuddy capabilities, including how to provide source or reference materials. Use when a user asks what it can do, how to start, what to prepare, how to provide materials, requests examples, or expresses a vague wish to make a video without a concrete production brief. Do not use once the user has provided a specific actionable video request.
---

# Golden Key OpenMontage 新手引导

Keep this interaction short and conversational. This is a WorkBuddy consumer experience, not a Golden Key Core stage and not an installer flow.

## Read the real local state

1. Read `WORKBUDDY-RUNTIME.json` beside this Skill. Validate `launcher`, `install_root`, and `data_root`. Do not guess or search the user's drives if it is absent or invalid; recommend running `install-workbuddy.ps1` from the complete ZIP.
2. Invoke the registered `launcher` with `doctor --json`. This is the stable installed form of `golden-key-workbuddy doctor --json` and must run before capability guidance.
3. Invoke the same launcher for `golden-key-workbuddy context --json`, `golden-key-workbuddy pipelines --json`, and `golden-key-workbuddy config inspect --json`.
4. Translate the useful result into plain language. Do not dump command output, internal Pipeline names, Schema names, provider keys, or setup jargon on a new user.
5. Do not call a real or paid Provider, create a production project, or claim installation readiness during onboarding.

## Start the conversation

In the user's language, explain in one or two sentences that Golden Key OpenMontage can help turn a goal into a governed video-production process, while WorkBuddy remains the conversational Agent.

Offer these four outcome-oriented starting points without asking the user to choose a technical Pipeline:

- introduce a product or service;
- present a company or brand;
- attract and qualify potential customers;
- build recognition or trust for a person, animal, or recurring character.

Give at most three starter examples that match the capabilities actually reported on this machine. Prefer examples close to the user's words. End with one simple question such as: “你现在最想让观众看完后记住什么，或者采取什么行动？”

## Guide material handoff

Explain material handoff only when the user asks what to prepare, mentions existing files or references, or when it helps them turn a vague wish into a concrete request. Do not force this branch into every greeting.

Use the branch that matches the conversation:

- **Existing source materials:** Invite the user to attach or drag in only the files relevant to this video, or provide local paths that WorkBuddy can read. Useful examples include product/company documents, product images, logos and brand rules, source video, narration/music, and approved factual evidence. Do not ask for the user's whole library.
- **Reference material:** Invite a reference video, image, or URL and ask what the user wants to learn from it—such as structure, rhythm, information density, or visual feeling. State that the result will be an original treatment, not a copy.
- **No material yet:** Reassure the user that planning can start from a truthful description of the subject and desired viewer action. Explain that the production flow will later distinguish required real evidence, optional user-provided material, and assets that may be generated only after approval.

Ask at most one material-handoff question in the current response. Choose a question that advances the user's actual branch, for example:

- “你想主要剪辑现有素材，还是允许在必要时生成补充画面？”
- “这条参考内容里，你最想借鉴的是结构、节奏，还是视觉感觉？”
- “如果暂时没有素材，先告诉我具体要介绍什么，以及希望观众看完做什么。”

Use the actual configured project/data location reported by local checks if the user asks where files will be stored. Do not hardcode a C-drive or D-drive location, move original files, or claim that WorkBuddy has imported, indexed, or understood a file before that operation is verified.

## Handoff

As soon as the user provides a concrete production request, stop onboarding. Load the `golden-key-openmontage` production Skill and continue through its direct-Agent contract and Core Pipeline rules. Do not repeat information the user already supplied.

The Golden Key Core owns production clarification inside its Pipeline skills. This onboarding Skill must not invent a parallel business-questionnaire contract.

## Boundaries

- Do not ask the user to inventory or list all available materials as part of onboarding; guide only the relevant handoff branch.
- Do not manage a Golden Key SaaS material library or pretend that WorkBuddy has one.
- Do not put onboarding behavior into the managed Golden Key Core snapshot.
- Do not present MCP, Python, CLI, model endpoints, or installation choices unless the user specifically asks about setup.
- If local checks fail, state the single blocking fact and recommend one next action; do not bury the user in diagnostics.
- Keep the first useful response compact enough to move from uncertainty to a concrete request in about one minute.
