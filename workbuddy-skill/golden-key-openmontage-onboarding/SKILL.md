---
name: golden-key-openmontage-onboarding
description: Guide new or uncertain WorkBuddy users into Golden Key OpenMontage with plain-language Chinese choices grounded in the locally available WorkBuddy capabilities, including how to provide source or reference materials. Use when a user asks what it can do, how to start, what to prepare, how to provide materials, requests examples, or expresses a vague wish to make a video without a concrete production brief. Do not use once the user has provided a specific actionable video request.
---

# Golden Key OpenMontage 新手引导

Keep this interaction short and conversational. This is a WorkBuddy consumer experience, not a Golden Key Core stage and not an installer flow.

## Read the real local state

1. Read `WORKBUDDY-RUNTIME.json` beside this Skill. Validate `launcher`, `install_root`, and `data_root`. Do not guess or search the user's drives if it is absent or invalid; recommend running `install-workbuddy.ps1` from the complete ZIP.
2. Invoke the registered `launcher` with `doctor --json`. This is the stable installed form of `golden-key-workbuddy doctor --json` and must run before capability guidance.
3. Invoke `golden-key-workbuddy config guide --json`; this goal-first guide remains available when optional Python packages have not yet been prepared.
4. If `doctor` reports missing Python packages, invoke `runtime plan --json`. Explain the download, registered DataRoot target, and isolation from system Python, then ask for explicit permission. Run `runtime prepare --confirm-download --json` only after consent and rerun `doctor`. Do not recommend reinstalling the ZIP for this dependency-only state. Defer `context`, `pipelines`, and strict `config inspect` until dependencies are ready.
5. Otherwise, invoke the same launcher for `golden-key-workbuddy context --json`, `golden-key-workbuddy pipelines --json`, and `golden-key-workbuddy config inspect --json`.
6. Translate the useful result into plain language. Do not dump command output, internal Pipeline names, Schema names, provider keys, or setup jargon on a new user.
7. Do not call a real or paid Provider, create a production project, or claim installation readiness during onboarding.

## Guide API Key setup

Use `config guide` to explain whether image generation, video generation, TTS, avatar, or related production capabilities have an API Key present. Say `已录入但未验证` for `present_unverified`; never describe key presence as a working connection.

Offer setup when the user asks how to make the package actually run, wants generated media, or the requested outcome needs an unconfigured capability. Start from the plain-language entries in `capability_choices`—生成图片、生成视频、中文配音、数字人或口型驱动、语音识别与内容分析—not from environment-variable names. Recommend only the `one or two recommended Providers` relevant to the current goal, explain what each unlocks, and distinguish direct vendor APIs from third-party gateways.

For each recommendation, present the Chinese Provider name, direct-vendor or gateway status, current credential state, required friendly field names, the `official account or key-management link`, account/region/permission caveat, and the billing notice reported by `config guide`. Do not invent a direct-vendor relationship or claim that every account has API access. Keep alternative Providers behind a short “查看其他接入” choice unless the user asks for them.

Do not ask the user to paste an API Key into WorkBuddy chat. If the user wants to configure now:

1. Ask whether they want to configure now; do not open a window merely because they mentioned a video goal.
2. After explicit opt-in, if local command execution is available, use `Start-Process` to open `<install_root>/配置API密钥.cmd` in a `visible interactive window`. Do not pass credential values or ordinary command-line arguments. If WorkBuddy cannot start it, tell the user to open the registered install directory and double-click the same file.
3. Explain that the local window uses hidden input and stores the Key with Windows current-user DPAPI protection under the registered data directory.
4. Wait for the user to say the local wizard finished, then rerun `golden-key-workbuddy config guide --json`.
5. Report only capability and Provider state. Never display, transcribe, log, or request the credential value.

Recording a Key does not authorize a Provider call, connectivity check, or paid generation. Ask separately before any network verification or production call.

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
