# WorkBuddy Shell V2 — Current Project State

Date: 2026-08-27

The live authority is `docs/workbuddy/v2/TASK-REGISTER.md`. This file is a compact
state snapshot, not a second task ledger.

## Product

An ordinary user writes a natural-language request in WorkBuddy containing
`金钥匙智能体`. WorkBuddy is the only Agent and production decision-maker. The
OpenMontage Package supplies production semantics. Shell V2 supplies installation,
lifecycle, Registration/Locator, runtime preparation, fixed mechanical invocation,
WorkBuddy entry, and status/receipt relay. Shell is never a second control plane.

WorkBuddy is a harness Agent: the same input may yield different internal thoughts,
tool paths, steps, wording, and intermediate conclusions. Skills and prompts must
not force a preset internal script. Acceptance follows the user's observed result;
process variation is acceptable unless it causes product failure, technical burden,
a second control plane, or a false result.

## Four results

| Result | Current state | Evidence / next boundary |
|---|---|---|
| 1. Installable Shell | `COMPLETE` | Commit `869358810ee41a0a61d10cec10c1b3b93c2c3450`; tree `3a623cb1eab9fee0d90854c0df271450f9779b9a`; Release SHA256 `7e5585298e50a5c5713ecd8fc4df57cfb6e88381b39453364cec62fdea1c6280`. Lifecycle and data protection passed. |
| 2. WorkBuddy natural-language result | `COMPLETE` | WorkBuddy `5.3.14` / Hy3; exact ordinary request ran through the single Skill and Shell and returned a concrete business reply plus LauncherReceipt. |
| 3. Playable Golden Key video | `NEXT / NOT_STARTED` | Must use the same user path and produce a real playable video plus receipt. Not part of the current closeout. |
| 4. Ordinary-user acceptance and closeout | `NOT_STARTED` | Follows Result 3. |

Result 2 evidence: Skill ZIP SHA256
`c96ec03522b744e8771eb16f22f5521102c4007af50ccb27d895efb82b1fe3a6`; evidence
root `D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\evidence\product2-workbuddy-user-flow-20260826`.
The receipt's `INCOMPLETE / RESULT_POINTER_INVALID` means no video file was made
in that run. It is a Result 3 artifact condition, not a Result 2 failure.

## Repository state

Formal delivery target: `refs/heads/codex/workbuddy-shell-v2`. The current Result 2
integration and document closeout passed the one independent read-only review:
`APPROVE / P0=0 / P1=0 / P2=0`. This state is delivered only when the commit
containing this snapshot is the exact formal ref, reached by ordinary fast-forward.

## Current closeout

The repository portion of this closeout is complete when this snapshot is the
formal ref. Remaining operational closeout is limited to precisely verified
abandoned task-object cleanup and opening the clean follow-up Codex task. No
Result 3, WorkBuddy, media, Package rebuild, or unrelated audit is authorized here.

## Non-goals

Do not preserve old route plans, packet/pre-review systems, extra Agents, MCP/
routers, renderer selection, HyperFrames/Remotion integration, or generic
framework work in the current authority documents. Git history remains the place
for provenance.
