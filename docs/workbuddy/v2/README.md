# WorkBuddy Shell V2

This directory contains the compact current contracts for the WorkBuddy Shell
product. The live task authority is [`TASK-REGISTER.md`](TASK-REGISTER.md); if
authority documents conflict, stop and report the conflict.

## Product in one sentence

An ordinary user writes a natural-language request containing `金钥匙智能体` in
WorkBuddy. WorkBuddy is the only harness Agent and production decision-maker; the
verified OpenMontage Package supplies production semantics; Shell supplies only
mechanical installation, lookup, invocation, entry, and result relay.

WorkBuddy's internal reasoning, tool path, steps, wording, and intermediate
conclusions may vary for the same input. Skills and prompts do not force a preset
script. Process variation is acceptable unless it causes product failure, adds
ordinary-user technical burden, creates a second control plane, or produces a false
result.

## Four results

1. **R1 — COMPLETE:** installable Shell product and protected lifecycle. Formal
   commit `869358810ee41a0a61d10cec10c1b3b93c2c3450`; tree
   `3a623cb1eab9fee0d90854c0df271450f9779b9a`; Release SHA256
   `7e5585298e50a5c5713ecd8fc4df57cfb6e88381b39453364cec62fdea1c6280`.
2. **R2 — COMPLETE:** WorkBuddy `5.3.14` / Hy3 actually invoked the single
   `golden-key-openmontage` Skill and Shell for
   `用金钥匙智能体给我做新店开业视频` and returned a concrete business reply plus
   a checkable LauncherReceipt. Skill ZIP SHA256
   `c96ec03522b744e8771eb16f22f5521102c4007af50ccb27d895efb82b1fe3a6`.
3. **R3 — COMPLETE:** WorkBuddy `5.3.14` / `Hy3 0.00x` displayed and played a
   real 46.6-second H.264/AAC MP4; independent review passed.
4. **R4 — COMPLETE:** the reviewed formal closeout reached the historical branch
   by ordinary fast-forward; no additional WorkBuddy or media run occurred.

The R2 receipt state `INCOMPLETE / RESULT_POINTER_INVALID` only records that no
video file was produced in that run. It is an R3 artifact condition, not an R2
failure.

## Planned next phase

The completed historical baseline is `codex/workbuddy-shell-v2` at
`aa9cabfa0d4f75d93e22317466709b6bad3bc3b4`. The authorized planning branch is
`codex/workbuddy-capability-onboarding`; implementation is not authorized.

FFmpeg is the minimum production baseline. WorkBuddy will perform a light
first-use inventory of relevant optional enhancements, explain that the basic
path remains available, and let the user continue or configure. Later messages
containing `金钥匙智能体` may naturally inspect, configure, change, or retest the
same capabilities. Shell remains mechanical and does not select Providers,
models, or renderers.

## Contract index

- [`MODULE-DISPOSITION.md`](MODULE-DISPOSITION.md): six module responsibilities
  and prohibitions.
- [`PACKAGE-REGISTRATION-CONTRACT.md`](PACKAGE-REGISTRATION-CONTRACT.md): the
  active Registration/Activation/Locator API and validation contract.
- Repository-level authority: [`../../../AGENT_GUIDE.md`](../../../AGENT_GUIDE.md),
  [`../../../PROJECT-STATE.md`](../../../PROJECT-STATE.md),
  [`PROJECT-CHARTER.md`](PROJECT-CHARTER.md),
  [`ACCEPTANCE-MATRIX.md`](ACCEPTANCE-MATRIX.md),
  [`DRIFT-GUARD.md`](DRIFT-GUARD.md), and [`TASK-REGISTER.md`](TASK-REGISTER.md).

Only the project Python at
`D:\BlazingCD\Personal\.venvs\golden-key-openmontage-workbuddy-w0\Scripts\python.exe`
may be used. Temporary files belong on D:. Optional enhancement installation or
use may be deferred and does not block an FFmpeg-ready basic path. No second
Agent, MCP, router, or generic framework is part of the product.
