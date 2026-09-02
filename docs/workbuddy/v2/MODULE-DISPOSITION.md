# WorkBuddy Shell V2 — Module Disposition

The historical product has six Shell modules. WorkBuddy remains the only harness
Agent and production decision-maker. The current optional-configuration Skill is
guidance only and does not invoke the Shell runtime-preparation or entry modules.

| Module | Main files | Owns | Must not do |
|---|---|---|---|
| Installation / lifecycle | `golden_key_openmontage_workbuddy/installer.py` | Assemble the final PackageRoot and private toolchain; create Manifest/Lock/binding; package the one-file guidance Skill; install, register, activate, uninstall, and protect user data. | Choose production; rewrite user intent; delete user data; create a second control plane. |
| Registration / Locator | `golden_key_openmontage_workbuddy/package_registration.py` | Explicit Package identity, immutable Registration objects, activation pointer, recovery, and read-only location. | Scan disks; guess or fallback; download; launch; repair during locate; choose a Package. |
| Historical runtime preparation | `golden_key_openmontage_workbuddy/runtime_prepare.py` | Preserve the bounded Shell implementation as historical/internal source. | Be invoked by the guidance-only Skill for optional configuration; own user consent; choose a renderer/provider. |
| Fixed mechanical invocation | `golden_key_openmontage_workbuddy/session_launcher.py`, `fixed_child.py` | Consume the approved binding, perform the fixed child transport, and emit mechanical facts. | Become an Agent, Director, workflow engine, provider/renderer selector, or media pipeline. |
| WorkBuddy guidance | `workbuddy-skill/golden-key-openmontage/SKILL.md` | Give WorkBuddy product rules and acceptance criteria only. | Call a Shell bridge, carry a private action, read a receipt, bind a machine path, or announce readiness. |
| Status / result relay | `user_entry.py`, `workbuddy_entry_cli.py`, `session_launcher.py` | Return status, receipt, and result facts to WorkBuddy. | Invent a video/Artifact, hide a failed operation as success, or make production decisions. |

## Cross-module rules

- The only wake condition is the original user message containing
  `金钥匙智能体`; the remainder of the request is open input.
- WorkBuddy may reason, read the verified Package Guide, ask business questions,
  call tools, retry, and adjust internal steps in its own harness. The same input
  may produce different internal paths and wording. This is acceptable unless it
  causes product failure, burdens the ordinary user technically, creates a second
  control plane, or produces a false result.
- The external Package `AGENT_GUIDE.md` is read by WorkBuddy only after
  Registration/Locator returns a verified PackageRoot and Guide identity.
- WorkBuddy performs live inspection of its current tools and Package-declared
  capabilities, explains the FFmpeg-ready basic path, and performs a consented
  optional configuration with its own available system abilities. The Skill
  supplies rules only and does not create a hidden installer or fixed workflow.
- Later natural-language messages containing `金钥匙智能体` may inspect,
  configure, change, or retest capabilities without a fixed command grammar.
- No module may add MCP, a second Agent, a router, a generic orchestration
  framework, or a hidden user-facing technical protocol.

## Current result boundary

R1, R2, R3, and R4 are `COMPLETE` in the historical
`codex/workbuddy-shell-v2` baseline at
`aa9cabfa0d4f75d93e22317466709b6bad3bc3b4`.
The R2 receipt `INCOMPLETE / RESULT_POINTER_INVALID` means only that the R2 run did
not create a video file; a file/result pointer is an R3 requirement. Optional
enhancement installation or use may be deferred and is not an R3 prerequisite,
but the planned next phase inventories relevant enhancements early and offers a
WorkBuddy-owned natural-language configuration entry without blocking the
FFmpeg-ready basic path.
