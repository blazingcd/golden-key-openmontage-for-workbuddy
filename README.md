# Golden Key WorkBuddy Shell V2

WorkBuddy Shell V2 connects Tencent WorkBuddy to a verified Golden Key OpenMontage
Package. WorkBuddy is the only Agent, conversation owner, and production
decision-maker. The Shell is a small mechanical support layer, not a second
control plane.

## Current product results

1. **Installable Shell product — COMPLETE.** Commit
   `869358810ee41a0a61d10cec10c1b3b93c2c3450`, tree
   `3a623cb1eab9fee0d90854c0df271450f9779b9a`, Release SHA256
   `7e5585298e50a5c5713ecd8fc4df57cfb6e88381b39453364cec62fdea1c6280`.
   Installation, Registration, Activation, Uninstallation, Reinstallation, and
   user-data protection passed.
2. **Natural-language WorkBuddy result — COMPLETE.** WorkBuddy `5.3.14` / Hy3
   actually invoked the single `golden-key-openmontage` Skill and Shell for
   `用金钥匙智能体给我做新店开业视频`, returned a concrete business reply, and
   produced a checkable LauncherReceipt. Skill ZIP SHA256:
   `c96ec03522b744e8771eb16f22f5521102c4007af50ccb27d895efb82b1fe3a6`.
3. **Real playable Golden Key video — NEXT / NOT_STARTED.** It must use the same
   ordinary-user path and produce a real playable video plus receipt.
4. **Ordinary-user acceptance and formal closeout — NOT_STARTED.**

`INCOMPLETE / RESULT_POINTER_INVALID` in the Result 2 receipt only means that no
video file was created in that run. A video file/result pointer belongs to Result 3
and does not invalidate Result 2.

## Product boundary

The user only writes a natural-language request containing `金钥匙智能体`; the
rest of the business request and any material paths are open input. WorkBuddy is a
harness Agent: the same input may produce different internal reasoning, tools,
steps, wording, and intermediate conclusions. Skills and prompts must not force a
preset script. Process variation is acceptable unless it causes a required result
to fail, burdens the ordinary user technically, creates a second control plane, or
produces a false result.

The Shell owns installation/lifecycle, Registration/Locator, runtime preparation,
fixed mechanical invocation, WorkBuddy entry, and status/receipt relay. It does
not choose production content, Pipeline/Stage, Provider, renderer, recovery, or
media strategy. The external Package `AGENT_GUIDE.md` is read by WorkBuddy only
after a verified PackageRoot is returned by Registration/Locator.

## Authority and constraints

The live state is in [`docs/workbuddy/v2/TASK-REGISTER.md`](docs/workbuddy/v2/TASK-REGISTER.md).
The other authority documents are [`AGENT_GUIDE.md`](AGENT_GUIDE.md),
[`PROJECT-STATE.md`](PROJECT-STATE.md),
[`docs/workbuddy/v2/PROJECT-CHARTER.md`](docs/workbuddy/v2/PROJECT-CHARTER.md),
[`docs/workbuddy/v2/ACCEPTANCE-MATRIX.md`](docs/workbuddy/v2/ACCEPTANCE-MATRIX.md),
and [`docs/workbuddy/v2/DRIFT-GUARD.md`](docs/workbuddy/v2/DRIFT-GUARD.md).

Use only the project Python at
`D:\BlazingCD\Personal\.venvs\golden-key-openmontage-workbuddy-w0\Scripts\python.exe`.
Temporary files belong on D: and must be cleaned up without deleting user data.
Remotion and HyperFrames may remain deferred; they are not Result 3 prerequisites.
Formal Git delivery targets `refs/heads/codex/workbuddy-shell-v2` and advances only
by ordinary fast-forward.
