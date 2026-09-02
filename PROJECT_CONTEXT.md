# WorkBuddy Shell V2 — Project Context

## Product path

```text
ordinary user -> WorkBuddy conversation -> Golden Key guidance Skill
             -> WorkBuddy uses verified OpenMontage rules and its own tools
             -> WorkBuddy presents the result
```

WorkBuddy is the only harness Agent, conversation owner, and production
decision-maker. For the same natural-language input, its internal reasoning, tool
path, steps, wording, and intermediate conclusions may vary. The Skill and prompt
must not force a preset script. This variation is acceptable unless it causes a
required product result to fail, adds technical burden to the ordinary user,
creates a second control plane, or produces a false result.

The OpenMontage Package is the production-semantic source. Shell V2 is limited to
Golden Key application lifecycle, Registration/Locator, fixed mechanical
invocation, and status/result relay. Optional configuration is guided by the Skill
and executed live by WorkBuddy. Shell does not choose or run creative production,
Pipeline/Stage, Provider, renderer, or media strategy. The
external Package `AGENT_GUIDE.md` is read by WorkBuddy only after a verified
PackageRoot and Guide identity are returned.

## Implementation map

| Responsibility | Main implementation | Boundary |
|---|---|---|
| Installation and lifecycle | `golden_key_openmontage_workbuddy/installer.py` | Assemble the PackageRoot, private toolchain, Manifest/Lock/binding, one-file guidance Skill, and lifecycle operations; never decide production. |
| Package Registration and Locator | `golden_key_openmontage_workbuddy/package_registration.py` | Validate explicit Package identity and locate one active Package; never scan, repair, download, launch, or choose fallback. |
| Historical runtime preparation | `golden_key_openmontage_workbuddy/runtime_prepare.py` | Preserved internal Shell source; the guidance-only Skill does not invoke it for optional configuration. |
| Fixed mechanical invocation | `golden_key_openmontage_workbuddy/session_launcher.py`, `fixed_child.py` | Validate the approved binding, perform the fixed transport, and return facts; never become an Agent or production workflow. |
| WorkBuddy guidance | `workbuddy-skill/golden-key-openmontage/SKILL.md` | Give WorkBuddy product rules and success criteria only; no machine-bound script, private action, receipt, or cached result. |
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
3. **R3 — COMPLETE.** WorkBuddy `5.3.14` / `Hy3 0.00x` displayed and played a
   real 46.6-second H.264/AAC MP4; independent review passed with no findings.
4. **R4 — COMPLETE.** The reviewed formal closeout reached the historical branch
   by ordinary fast-forward and did not run WorkBuddy or produce another video.

## Planned next phase

The historical baseline is `codex/workbuddy-shell-v2` at
`aa9cabfa0d4f75d93e22317466709b6bad3bc3b4`. The planning branch is
`codex/workbuddy-capability-onboarding`; the current guidance-only candidate is
authorized on `codex/workbuddy-m1-capability-onboarding` and remains uninstalled.

FFmpeg is the minimum production baseline. WorkBuddy owns live inspection of
relevant optional enhancements and the natural-language choice to continue or
configure. The Skill supplies mirror, compatibility, consent, Windows-location,
and acceptance rules; WorkBuddy performs installation and verification with its
own available system abilities. Optional absence does not block the FFmpeg-ready
basic path.

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
- Optional capability installation or use may be deferred and is not an R3
  prerequisite. First-use inventory and later natural-language reconfiguration
  belong to the planned WorkBuddy-owned next phase.
