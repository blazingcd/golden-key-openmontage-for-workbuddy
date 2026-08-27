# WorkBuddy Shell V2 — Task Register

## Authority

This is the live task, product-result, authorization, and Git-state authority.
Read it together with `AGENT_GUIDE.md`, `PROJECT-CHARTER.md`,
`ACCEPTANCE-MATRIX.md`, and `DRIFT-GUARD.md`. If any of the six documents conflict,
stop. Old routes, chat statements, tests, and Git history cannot authorize work.

Formal delivery ref: `refs/heads/codex/workbuddy-shell-v2`.
No legacy route label or future lettered series is current.

## Product contract

The only product path is:

`ordinary user -> WorkBuddy -> golden-key-openmontage Skill -> Shell mechanics -> WorkBuddy result`

WorkBuddy is the only Agent, user-facing conversation owner, and production
decision-maker. OpenMontage Package Guide/Manifest/Pipeline/Stage/Tool semantics
are the production source. Shell owns only installation/lifecycle,
Registration/Locator, runtime preparation, fixed mechanical invocation, WorkBuddy
entry, and status/receipt relay. Shell cannot become a second Agent, Director,
workflow engine, provider/renderer selector, media control plane, MCP, router, or
general framework.

The only wake condition is the literal presence of `金钥匙智能体` in the original
user message. The rest of the user's business request and any material paths are
open input and must not be turned into a fixed full-prompt protocol. Ordinary users
do not operate internal path/hash/schema/env/argv/pipe/command mechanics.

WorkBuddy is a harness Agent. For the same input, its internal reasoning, tool
path, steps, wording, and intermediate conclusions may vary. A Skill or prompt
must not force a preset script. WorkBuddy may read the Package Guide, ask business
questions, call tools, retry, and adjust internal steps. These variations matter
only if they directly cause product failure, add ordinary-user technical burden,
create a second control plane, or produce a false result.

## Product results

### R1 — Installable Shell product: COMPLETE

- Commit: `869358810ee41a0a61d10cec10c1b3b93c2c3450`
- Tree: `3a623cb1eab9fee0d90854c0df271450f9779b9a`
- Release SHA256: `7e5585298e50a5c5713ecd8fc4df57cfb6e88381b39453364cec62fdea1c6280`
- Scope passed: installation, Registration, Activation, Uninstallation,
  Reinstallation, and user-data protection.

### R2 — WorkBuddy natural-language result: COMPLETE

- Client/model: WorkBuddy `5.3.14` / `Hy3`.
- Real user input: `用金钥匙智能体给我做新店开业视频`.
- Observed: the single `golden-key-openmontage` Skill and Shell were invoked;
  the ordinary user received a concrete business reply and a checkable
  LauncherReceipt.
- Skill ZIP SHA256:
  `c96ec03522b744e8771eb16f22f5521102c4007af50ccb27d895efb82b1fe3a6`.
- Evidence root:
  `D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\evidence\product2-workbuddy-user-flow-20260826`.

The observed receipt state `INCOMPLETE / RESULT_POINTER_INVALID` means only that
the run did not create a video file. A file and valid result pointer are required
by R3, not R2. The raw independent review `REJECT / P0=0 / P1=1 / P2=0` is kept as
a fact about the mismatched review; its only P1 used the R3 artifact standard.
Owner corrected the acceptance level, so R2 is complete and has no second review.

### R3 — Real playable Golden Key video: NEXT / NOT_STARTED

R3 must use the same ordinary-user WorkBuddy path and produce a real playable
video and checkable receipt. Candidate source directories are:

- `D:\BlazingCD\Personal\测试素材\头头象花浴头疗素材\店内环境`
- `D:\BlazingCD\Personal\Golden Key Digital Human\resources\assets\default\_bgm`

These paths and the fuller business wording are candidate inputs, not a frozen
protocol. R3 is not authorized in the current repository closeout.

### R4 — Ordinary-user acceptance and formal closeout: NOT_STARTED

R4 follows a successful R3 and is not authorized in the current closeout.

## Acceptance rules

1. Each result has one executor and one independent result review, performed only
   after a real user-visible result exists.
2. Do not create packet, pre-review, multi-round review, or role-separation
   machinery. A reviewer starts from the result's user-visible goal and may not
   invent an architecture gate or preset internal process.
3. WorkBuddy may use its own harness reasoning, Guide reading, questions, tools,
   retries, and internal corrections. These are not failures unless they make a
   required product result absent, burden the user technically, create a second
   control plane, or produce a false result.
4. R3 fails if an ordinary user must operate technical commands/paths/schema/env,
   the Skill/Shell is not actually called, no real playable video and receipt
   exist, or Shell makes production decisions as a second Agent.

## Engineering constraints

- Project Python only: `D:\BlazingCD\Personal\.venvs\golden-key-openmontage-workbuddy-w0\Scripts\python.exe`.
- Temporary task files only on D:; remove exact temporary material after review;
  preserve user data.
- Remotion and HyperFrames may be deferred and are not R3 prerequisites.
- No second Agent, MCP, router, or generic framework.

## Repository closeout result

Owner authorization dated 2026-08-27 covered:

- shrink and align the current authority, entry, contract, and work-log documents;
- verify the existing R2 changes;
- perform one independent read-only result review;
- commit/push the reviewed candidate and ordinary-fast-forward the formal ref;
- delete only precisely verified abandoned branches, closed worktrees, and task
  directories with no unique or unmerged work;
- create a clean follow-up Codex task for later planning.

The repository candidate passed its one independent read-only review:
`APPROVE / P0=0 / P1=0 / P2=0`. Focused verification passed with
`56 passed, 1 skipped`; `git diff --check --` passed. This repository result is
complete only when the commit containing this register is the exact formal ref by
ordinary fast-forward. External closeout then only removes precisely verified
abandoned task objects and opens the clean follow-up Codex task. This task must not
start R3, WorkBuddy, media, or a Package rebuild.

## Delivery state fields

```text
formal_ref: refs/heads/codex/workbuddy-shell-v2
result_1: COMPLETE
result_2: COMPLETE / REAL_WORKBUDDY_NATURAL_LANGUAGE_RESULT_AND_RECEIPT_OBSERVED
result_3: NEXT / NOT_STARTED / NOT_AUTHORIZED_IN_CLOSEOUT
result_4: NOT_STARTED
current_task: DOCUMENT_AND_REPOSITORY_CLOSEOUT / COMPLETE_ON_FORMAL_REF
workbuddy_or_media_in_current_task: FORBIDDEN
closeout_review: APPROVE / P0=0 / P1=0 / P2=0
formal_delivery: COMPLETE_WHEN_THIS_REGISTER_COMMIT_IS_EXACT_FORMAL_REF
```
