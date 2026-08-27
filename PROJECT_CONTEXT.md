# WorkBuddy Shell V2 — Project Context

## Product path

```text
ordinary user -> WorkBuddy conversation -> one Golden Key Skill -> Shell mechanics
             -> verified OpenMontage Package -> WorkBuddy presents the result
```

WorkBuddy is the only harness Agent, conversation owner, and production
decision-maker. For the same natural-language input, its internal reasoning, tool
path, steps, wording, and intermediate conclusions may vary. The Skill and prompt
must not force a preset script. This variation is acceptable unless it causes a
required product result to fail, adds technical burden to the ordinary user,
creates a second control plane, or produces a false result.

The OpenMontage Package is the production-semantic source. Shell V2 is limited to
installation/lifecycle, Registration/Locator, runtime preparation, fixed mechanical
invocation, WorkBuddy entry, and status/receipt relay. Shell does not choose or run
creative production, Pipeline/Stage, Provider, renderer, or media strategy. The
external Package `AGENT_GUIDE.md` is read by WorkBuddy only after a verified
PackageRoot and Guide identity are returned.

## Implementation map

| Responsibility | Main implementation | Boundary |
|---|---|---|
| Installation and lifecycle | `golden_key_openmontage_workbuddy/installer.py` | Assemble the PackageRoot, private toolchain, Manifest/Lock/binding, stamped Skill, and lifecycle operations; never decide production. |
| Package Registration and Locator | `golden_key_openmontage_workbuddy/package_registration.py` | Validate explicit Package identity and locate one active Package; never scan, repair, download, launch, or choose fallback. |
| Runtime preparation | `golden_key_openmontage_workbuddy/runtime_prepare.py` | Bounded optional-capability detection/consent/integration; never replace required Python/FFmpeg/Node or choose a renderer. |
| Fixed mechanical invocation | `golden_key_openmontage_workbuddy/session_launcher.py`, `fixed_child.py` | Validate the approved binding, perform the fixed transport, and return facts; never become an Agent or production workflow. |
| WorkBuddy entry | `golden_key_openmontage_workbuddy/user_entry.py`, `workbuddy_entry_cli.py`, `workbuddy-skill/golden-key-openmontage/` | Carry the original user request through the single WorkBuddy Skill; never require user technical operations or rewrite business intent. |
| Status and result relay | `workbuddy_entry_cli.py`, `user_entry.py`, `session_launcher.py` | Return the mechanical status/receipt to WorkBuddy; never invent an Artifact or claim a result that was not produced. |

## Current results

1. **R1 — COMPLETE.** Commit `869358810ee41a0a61d10cec10c1b3b93c2c3450`,
   tree `3a623cb1eab9fee0d90854c0df271450f9779b9a`, Release SHA256
   `7e5585298e50a5c5713ecd8fc4df57cfb6e88381b39453364cec62fdea1c6280`; lifecycle
   and user-data protection passed.
2. **R2 — COMPLETE.** WorkBuddy `5.3.14` / Hy3, user input
   `用金钥匙智能体给我做新店开业视频`, actual single Skill/Shell invocation,
   concrete business reply, and checkable LauncherReceipt. Skill ZIP SHA256
   `c96ec03522b744e8771eb16f22f5521102c4007af50ccb27d895efb82b1fe3a6`; evidence
   root `D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\evidence\product2-workbuddy-user-flow-20260826`.
   `INCOMPLETE / RESULT_POINTER_INVALID` only means no video file was created; the
   file/result-pointer requirement belongs to R3.
3. **R3 — NEXT / NOT_STARTED.** Same ordinary-user path, real playable video and
   checkable receipt. Not part of the current document/repository closeout.
4. **R4 — NOT_STARTED.** Ordinary-user acceptance and formal closeout.

## Working constraints

- Only the original user message's inclusion of `金钥匙智能体` is the wake
  condition; do not freeze a full prompt.
- Ordinary users do not construct paths, hashes, schemas, environment variables,
  argv, pipes, or commands.
- One executor and one independent result review per product result; no packet,
  pre-review, multi-round review, or technical gate imported from another result.
- Project Python is only
  `D:\BlazingCD\Personal\.venvs\golden-key-openmontage-workbuddy-w0\Scripts\python.exe`.
  Temporary files are D:-only and user data is preserved.
- Remotion and HyperFrames may be deferred and are not R3 prerequisites.
