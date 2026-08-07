---
name: golden-key-openmontage
description: Use Golden Key OpenMontage in WorkBuddy for brand/company, lead-conversion, product-marketing, and subject-IP video production through the locked pipeline, stage-skill, artifact, reviewer, and checkpoint contracts.
---

# Golden Key OpenMontage for WorkBuddy

Treat this package as Pre-Alpha. WorkBuddy is the only Agent; never start or emulate a nested model-driven Agent Host.

## Preflight

1. Read `WORKBUDDY-RUNTIME.json` beside this Skill. Validate that it provides `launcher`, `install_root`, and `data_root`. Do not guess or search the user's drives when the locator is absent or invalid; tell the user to run `install-workbuddy.ps1` from the complete ZIP.
2. Invoke the registered `launcher` with `doctor --json`. This is the stable installed form of `golden-key-workbuddy doctor`; do not require the user to find a repository or construct the command manually.
3. If `doctor` reports missing Python packages, invoke the launcher with `runtime plan --json`. Explain that preparation downloads packages into `<data_root>/Runtime/Python`, can use the selected D-drive data root, and does not modify the system Python. Run `runtime prepare --confirm-download --json` only after the user explicitly agrees, then rerun `doctor --json`. Never infer consent from the original video request.
4. Treat the runtime roles accurately: Python is required; FFmpeg is required for compose and local media tools; Node is optional unless the approved plan selects Remotion or HyperFrames. Do not install Node merely because it is missing.
5. Read `AGENT_GUIDE.md` before production from the reported `install_root` and obey Rule Zero.
6. Invoke the same launcher with `config inspect --json` (the registered form of `golden-key-workbuddy config inspect --json`). Keep the WorkBuddy conversation model separate from every Golden Key production Provider: WorkBuddy owns its conversation-model configuration, while the adapter only reports Tool Registry-backed production paths.
7. When a user wants a credential reference file, invoke the launcher with `config template` (the registered form of `golden-key-workbuddy config template`). It writes a consumer-owned template under the registered `data_root`, records environment-variable names only, and never stores credential values.
8. Report missing local runtimes and production Provider configuration without silently changing the requested production path. A China-ecosystem model reached through a third-party gateway is not a direct domestic Provider path.
9. Invoke `config guide --json` before proposing a generated-image, generated-video, TTS, avatar, or other API-backed production path. Start from its Chinese goal labels and recommend only the one or two Providers needed by the approved plan. For each, state direct-vendor or gateway status, friendly credential-field names, the `official account or key-management link`, account/permission caveat, billing notice, and current state; keep technical environment-variable names out of the normal conversation.
10. Do not ask the user to paste an API Key into WorkBuddy chat. Ask whether they want to configure now. After explicit opt-in, use `Start-Process` when local command execution is available to open the registered `配置API密钥.cmd` in a visible interactive window; otherwise tell them how to double-click it. Never put a Key in process arguments. Wait for the local hidden-input wizard to finish, then rerun `config guide --json`. Treat `present_unverified` as “已录入但未验证”, not as a successful connection.
11. Saving a Key does not authorize a Provider call, connectivity test, or paid generation. Obtain separate explicit approval before any network or Provider validation.

## Production contract

The direct CLI is the canonical fallback. After the W2 real-client comparison, the local stdio MCP is an optional structured-tool adapter. When `golden-key-openmontage` MCP is enabled and healthy, WorkBuddy may use its `golden_key_*` tools instead of spelling the equivalent CLI command. Both entries call the same consumer functions and must preserve the same Pipeline, Stage Skill, Artifact, Reviewer, Checkpoint, task, cost, and network gates. Do not mix CLI and MCP retries for the same operation.

1. Run `golden-key-workbuddy context --json` and `golden-key-workbuddy pipelines --json` to read the callable contracts. Only WorkBuddy selects the Pipeline from the user's request and grounded evidence:
   - `golden-key-brand-company`
   - `golden-key-lead-conversion`
   - `golden-key-product-marketing`
   - `golden-key-subject-ip`
2. Create the project with `golden-key-workbuddy project create`; pass the Pipeline WorkBuddy selected. Resume with `golden-key-workbuddy project status`.
3. Run `golden-key-workbuddy stage inspect`, then read the returned manifest-declared Stage Skill before doing Stage work.
4. Run `golden-key-workbuddy tool list` for the project. Use only the returned current-Stage allowlist; do not rank or select a Pipeline in the CLI.
5. Before execution, read every returned `agent_skills` entry at `.agents/skills/<name>/SKILL.md`. Write the tool input JSON inside the project's `artifacts/` directory, keep every tool path inside the project, then run `golden-key-workbuddy tool execute --ack-agent-skill <name>` (repeat the acknowledgement for every required Layer 3 Skill).
6. Treat `API or Hybrid` execution as blocked unless a separately authorized Provider path exists. The W2 offline entry intentionally refuses it before status probing, execution, or network access; never retry it through an ad-hoc call.
7. For a local Tool that may take time, run `golden-key-workbuddy task submit` instead of direct execution. Submit validates and queues the immutable request but does not run it. Keep the returned task ID.
8. Start it with `golden-key-workbuddy task run --timeout-seconds <seconds>`. This is a foreground command; WorkBuddy may place that process in the background, then use `golden-key-workbuddy task status` to read the durable record under the registered `<data_root>/Jobs`. Only one local Tool task may execute per data root. If another task owns the slot, keep this task queued and do not retry automatically.
9. Treat the runtime deadline as observation only: when status reports `timeout_exceeded=true`, explain that the blocking Core Tool is still running and wait or inspect it. Never claim the deadline forcibly terminated or safely cancelled the Tool.
10. Use `golden-key-workbuddy task cancel` only while the task is queued. A running blocking Tool is not safely cancelable under the current Core contract; report that limitation and do not claim it was cancelled or kill it externally.
11. If status reports an interrupted execution, use `golden-key-workbuddy task recover`. It marks the task failed and releases that task's stale global execution slot without executing the Tool again. Because partial local side effects may exist, never retry automatically; inspect outputs and submit a new request only with user-aware judgment.
12. Write canonical Artifact JSON inside the project's `artifacts/` directory and run `golden-key-workbuddy artifact validate`.
13. Run the native Reviewer, then use `golden-key-workbuddy checkpoint submit`. For a gated Stage, submit `awaiting_human`, present the result, and end the turn; submit `completed --human-approved` only after explicit approval.

## Safety boundaries

- Do not call a real or paid Provider without explicit user approval.
- Do not bypass Stage Skills, Artifact validation, Reviewer, or Checkpoint gates.
- Keep local Tool execution inside the CLI's offline boundary; it denies socket access in the current Python process and inherited Python/Node subprocesses. Do not replace it with an ad-hoc import, subprocess environment, or network call.
- Treat CLI/MCP/task output as redacted diagnostic data. Never copy credentials into Artifact content, filenames, prompts, or ad-hoc logs, and never attempt to recover a value replaced with `[REDACTED]`.
- Do not import, launch, or recreate `agent_host_authority`, `model_driven_agent_host`, or `openai_compatible_transport`.
- MCP is optional, local, and deterministic after the real WorkBuddy comparison Gate. Never treat it as a remote service, a second Agent, or a required replacement for the CLI fallback.
- Do not claim installation readiness, real WorkBuddy acceptance, or `OFFLINE ADAPTER READY`.
