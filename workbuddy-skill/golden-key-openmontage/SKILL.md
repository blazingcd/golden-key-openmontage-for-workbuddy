---
name: golden-key-openmontage
description: Use Golden Key OpenMontage in WorkBuddy for brand/company, lead-conversion, product-marketing, and subject-IP video production through the locked pipeline, stage-skill, artifact, reviewer, and checkpoint contracts.
---

# Golden Key OpenMontage for WorkBuddy

Treat this package as Pre-Alpha. WorkBuddy is the only Agent; never start or emulate a nested model-driven Agent Host.

## Preflight

1. Locate the checked-out Golden Key OpenMontage for WorkBuddy repository.
2. Run `golden-key-workbuddy doctor` from that repository. If the command is not installed yet, run `python -m golden_key_openmontage_workbuddy doctor`.
3. Read `AGENT_GUIDE.md` before production and obey Rule Zero.
4. Run `golden-key-workbuddy config inspect --json`. Keep the WorkBuddy conversation model separate from every Golden Key production Provider: WorkBuddy owns its conversation-model configuration, while the adapter only reports Tool Registry-backed production paths.
5. When a user wants a credential reference file, run `golden-key-workbuddy config template`. It writes a consumer-owned template under `D:/WorkBuddyData/Config`, records environment-variable names only, and never stores credential values.
6. Report missing local runtimes and production Provider configuration without silently changing the requested production path. A China-ecosystem model reached through a third-party gateway is not a direct domestic Provider path.

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
8. Start it with `golden-key-workbuddy task run`. This is a foreground command; WorkBuddy may place that process in the background, then use `golden-key-workbuddy task status` to read the durable record under `D:/WorkBuddyData/Jobs`.
9. Use `golden-key-workbuddy task cancel` only while the task is queued. A running blocking Tool is not safely cancelable under the current Core contract; report that limitation and do not claim it was cancelled or kill it externally.
10. If status reports an interrupted execution, use `golden-key-workbuddy task recover`. It marks the task failed without executing the Tool again. Because partial local side effects may exist, never retry automatically; inspect outputs and submit a new request only with user-aware judgment.
11. Write canonical Artifact JSON inside the project's `artifacts/` directory and run `golden-key-workbuddy artifact validate`.
12. Run the native Reviewer, then use `golden-key-workbuddy checkpoint submit`. For a gated Stage, submit `awaiting_human`, present the result, and end the turn; submit `completed --human-approved` only after explicit approval.

## Safety boundaries

- Do not call a real or paid Provider without explicit user approval.
- Do not bypass Stage Skills, Artifact validation, Reviewer, or Checkpoint gates.
- Keep local Tool execution inside the CLI's socket-denial boundary; do not replace it with an ad-hoc Python import or network call.
- Do not import, launch, or recreate `agent_host_authority`, `model_driven_agent_host`, or `openai_compatible_transport`.
- MCP is optional, local, and deterministic after the real WorkBuddy comparison Gate. Never treat it as a remote service, a second Agent, or a required replacement for the CLI fallback.
- Do not claim installation readiness, real WorkBuddy acceptance, or `OFFLINE ADAPTER READY`.
