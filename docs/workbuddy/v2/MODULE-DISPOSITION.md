# WorkBuddy Shell V2 — Module Disposition

The product has exactly six Shell responsibilities. WorkBuddy remains the only
harness Agent and production decision-maker; the Shell only supports the verified
Package and relays mechanical facts.

| Module | Main files | Owns | Must not do |
|---|---|---|---|
| Installation / lifecycle | `golden_key_openmontage_workbuddy/installer.py` | Assemble the final PackageRoot and private toolchain; create Manifest/Lock/binding; stamp the single Skill; install, register, activate, uninstall, and protect user data. | Choose production; rewrite user intent; delete user data; create a second control plane. |
| Registration / Locator | `golden_key_openmontage_workbuddy/package_registration.py` | Explicit Package identity, immutable Registration objects, activation pointer, recovery, and read-only location. | Scan disks; guess or fallback; download; launch; repair during locate; choose a Package. |
| Runtime preparation | `golden_key_openmontage_workbuddy/runtime_prepare.py` | Bounded detection and explicit consent/integration for optional capabilities. | Replace required Python/FFmpeg/Node; choose a renderer/provider; scan unrelated paths; run media. |
| Fixed mechanical invocation | `golden_key_openmontage_workbuddy/session_launcher.py`, `fixed_child.py` | Consume the approved binding, perform the fixed child transport, and emit mechanical facts. | Become an Agent, Director, workflow engine, provider/renderer selector, or media pipeline. |
| WorkBuddy entry | `golden_key_openmontage_workbuddy/user_entry.py`, `workbuddy_entry_cli.py`, `workbuddy-skill/golden-key-openmontage/` | Offer one Skill entry, preserve the original natural-language request, and call the Shell bridge. | Demand technical commands/paths/schema/env/argv from the user; force preset reasoning; create another Skill/Agent/router. |
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
- No module may add MCP, a second Agent, a router, a generic orchestration
  framework, or a hidden user-facing technical protocol.

## Current result boundary

R1 and R2 are `COMPLETE`; R3 is `NEXT / NOT_STARTED`; R4 is `NOT_STARTED`.
The R2 receipt `INCOMPLETE / RESULT_POINTER_INVALID` means only that the R2 run did
not create a video file; a file/result pointer is an R3 requirement. Remotion and
HyperFrames may be deferred and are not R3 prerequisites.
