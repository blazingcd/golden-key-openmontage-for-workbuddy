# WorkBuddy Shell V2 — Project Charter

## Purpose

Make Golden Key OpenMontage usable by an ordinary user through one natural-language
WorkBuddy conversation. The user should only need to describe the business need
and provide optional business materials. The internal execution method belongs to
WorkBuddy and the verified Package, not to the user.

## Ownership

- **WorkBuddy:** the only Agent, conversation owner, and production decision-maker.
  It reads the verified OpenMontage Package Guide and follows its production
  semantics, asks business questions, chooses tools and steps, and presents results.
- **OpenMontage Package:** source of production meaning: Guide, Manifest, Pipeline,
  Stage, Artifact, Checkpoint, Reviewer, Tool, and Provider contracts.
- **Shell V2:** installation/lifecycle, Package Registration/Locator, runtime
  preparation, fixed mechanical invocation, WorkBuddy entry, and status/receipt
  relay.

Shell is not a second Agent or control plane. It does not decide creative content,
Pipeline/Stage order, Provider, renderer, recovery, or business acceptance. Do not
add an MCP, router, workflow engine, media framework, or second conversation path.

## User path

The only wake condition is that the original user message contains the literal
`金钥匙智能体`. Any additional natural-language business description, questions,
constraints, or material paths remain user input. Do not require a fixed complete
prompt. Do not require the user to see or operate path/hash/schema/env/argv/pipe
or command mechanics.

WorkBuddy is a harness Agent. The same input may lead to different internal
reasoning, tools, steps, wording, and intermediate conclusions. Skills and prompts
must not force a preset script. Variation is acceptable unless it directly causes
the product result to fail, burdens the ordinary user technically, creates a second
control plane, or produces a false result.

The external OpenMontage `AGENT_GUIDE.md` is read by WorkBuddy only after
Registration/Locator has returned and verified the PackageRoot and Guide identity.

## Four product results

1. **Installable Shell product — COMPLETE.** The final PackageRoot/binding,
   private runtime, Installer lifecycle, and data protection are represented by
   the accepted commit/release facts in the Task Register.
2. **WorkBuddy natural-language result — COMPLETE.** A real WorkBuddy 5.3.14 /
   Hy3 run invoked the single Skill and Shell from the ordinary request
   `用金钥匙智能体给我做新店开业视频` and returned a concrete business reply plus
   a checkable LauncherReceipt. No video file was required for this result.
3. **Real playable Golden Key video — NEXT / NOT_STARTED.** The same user path
   must produce a real playable video and receipt. This is the next product task,
   not part of the current document/repository closeout.
4. **Ordinary-user acceptance and formal closeout — NOT_STARTED.** This follows
   successful Result 3.

## Acceptance philosophy

Judge each result by what an ordinary user can accomplish and observe. WorkBuddy
may read the Guide, ask questions, call tools, retry, and adjust internal steps.
Its internal methods are not a failure. A failure is a missing required user-visible
result, technical burden on the ordinary user, a second control plane, or a false
result.

Each result gets one executor and one independent review after a real user-visible
result. Do not add packet/pre-review loops or technical gates that are not required
by that result.

## Out of scope

Result 3 may defer Remotion and HyperFrames; neither is a prerequisite. No current
work should add optional frameworks, a second Agent, a second Skill, or generalized
orchestration merely to prepare for hypothetical future work.
