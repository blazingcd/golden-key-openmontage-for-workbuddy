# WorkBuddy Shell V2 Agent Guide

## Mandatory routing

Read this file completely before acting in this repository or responding about it.
`docs/workbuddy/v2/TASK-REGISTER.md` is the current state and authorization authority.
`PROJECT-CHARTER.md` defines the product boundary, `ACCEPTANCE-MATRIX.md` defines
user-visible acceptance, and `DRIFT-GUARD.md` defines stop and Git rules. If the
six authority documents disagree, stop and report the conflict; do not infer from
chat history, old plans, tests, or Git history.

The only formal delivery ref is `refs/heads/codex/workbuddy-shell-v2`. Legacy
route labels and future lettered series are not execution authority.

## Product boundary

The product goal is one ordinary-user path:

1. The user writes a natural-language business request in WorkBuddy.
2. The request contains the wake word `金钥匙智能体`.
3. WorkBuddy is the only Agent, conversation owner, and production decision-maker.
4. WorkBuddy uses the verified OpenMontage Package as the production-semantic source.
5. The Shell supplies only installation/lifecycle, Registration/Locator, runtime
   preparation, fixed mechanical invocation, WorkBuddy entry, and status/receipt relay.

The Shell is not a second Agent, conversation owner, Director, workflow engine,
provider/renderer selector, media control plane, MCP/router, or general framework.
The OpenMontage Package is not a second running Agent. Its external `AGENT_GUIDE.md`
may be read by WorkBuddy only after a verified PackageRoot has been returned by
Registration/Locator.

The ordinary user never has to construct or operate internal paths, hashes,
schemas, environment variables, argv, pipes, or commands. WorkBuddy is a harness
Agent with its own reasoning. For the same natural-language input, its thought
process, tool path, steps, wording, and intermediate conclusions may vary. A Skill
or prompt must not force a preset script. WorkBuddy may read the Package Guide, ask
reasonable business questions, call tools, retry, or adjust internal steps. These
internal choices are not failures by themselves.

## Four product results

### Result 1 — COMPLETE

The installable Shell product is complete at commit
`869358810ee41a0a61d10cec10c1b3b93c2c3450`, tree
`3a623cb1eab9fee0d90854c0df271450f9779b9a`, Release SHA256
`7e5585298e50a5c5713ecd8fc4df57cfb6e88381b39453364cec62fdea1c6280`.
Installation, Registration, Activation, Uninstallation, Reinstallation, and user
data protection were completed.

### Result 2 — COMPLETE

In WorkBuddy 5.3.14 with Hy3, the ordinary-user input
`用金钥匙智能体给我做新店开业视频` actually invoked the single
`golden-key-openmontage` Skill and Shell. The user received a concrete business
reply and a checkable LauncherReceipt. The Skill ZIP SHA256 is
`c96ec03522b744e8771eb16f22f5521102c4007af50ccb27d895efb82b1fe3a6`; evidence is
under `D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\evidence\product2-workbuddy-user-flow-20260826`.

The receipt state `INCOMPLETE / RESULT_POINTER_INVALID` only says that this run
did not create a video file. A file and valid result pointer belong to Result 3;
they do not invalidate Result 2. The original independent review fact
`REJECT / P0=0 / P1=1 / P2=0` is retained only as history of a mismatched gate:
its P1 applied the Result 3 artifact standard. Owner correction is final and no
second Result 2 review is required.

### Result 3 — NEXT / NOT_STARTED

Use the same ordinary-user path to create a real playable Golden Key video. The
candidate materials are `D:\BlazingCD\Personal\测试素材\头头象花浴头疗素材\店内环境`
and `D:\BlazingCD\Personal\Golden Key Digital Human\resources\assets\default\_bgm`.
These are candidate inputs, not a fixed protocol. Result 3 is not authorized by
the current documentation closeout task.

### Result 4 — NOT_STARTED

Ordinary-user acceptance and formal project closeout.

## Acceptance and execution rules

- The only wake condition is that the original user message contains
  `金钥匙智能体`; do not freeze a full prompt or business description.
- Each result has one executor and exactly one independent result review after a
  real user-visible result exists. Do not create packet/pre-review/multi-review
  systems or extra roles.
- The reviewer judges the product result's user-visible goal first. It may not
  invent an architecture gate or require a preset internal sequence/wording.
  It must not compare the run against an evaluator-invented transcript or
  imagined intermediate output.
  Process variation is allowed unless it directly causes product failure, adds
  technical burden to the ordinary user, creates a second control plane, or
  produces a false result.
- Result 3 passes only with one ordinary-language entry, a real WorkBuddy path,
  a real playable video, and a checkable receipt. User-facing technical burden,
  absent Skill/Shell invocation, absent video/receipt, or Shell production
  decision-making fails it. WorkBuddy's internal commands, tool choice, retries,
  and corrections are not failures.

## Engineering and safety constraints

- Use only the project Python: `D:\BlazingCD\Personal\.venvs\golden-key-openmontage-workbuddy-w0\Scripts\python.exe`.
- Put temporary files only on D: and remove exact temporary task material after
  verification. Preserve user data.
- Remotion and HyperFrames may remain deferred; they are not Result 3 prerequisites.
- Do not add a second Agent, MCP, router, or general framework.
- Never force-push or reset hard. Advance the formal branch only by ordinary
  fast-forward. Before destructive cleanup, resolve exact paths, ensure no
  unmerged or unique work exists, and prefer recoverable deletion.

## Current closeout authorization

Owner authorized the 2026-08-27 repository closeout: slim and align the current
authority, entry, contract, and work-log documents; verify the existing Result 2
changes; perform one independent read-only result review; commit/push the candidate
and ordinarily fast-forward the formal ref; remove only verified abandoned
branches/worktrees/task directories; and open a clean follow-up Codex task. This
closeout must not start Result 3, WorkBuddy, media generation, or unrelated code
work.
