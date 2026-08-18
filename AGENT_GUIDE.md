# WorkBuddy Shell V2 Agent Guide

Read this file completely before acting in this repository.

## Product boundary

- **Tencent WorkBuddy is the only running Agent and owns the user conversation.** It receives the user's literal business request, reads the verified Golden Key OpenMontage Package Guide, follows that Package's Pipeline/Stage/Artifact/Checkpoint/Reviewer/Tool/Provider contracts, and presents results.
- **"OpenMontage Agent" is a logical production role assumed by WorkBuddy after it loads the verified Package.** It is not a second Agent, nested Agent Host, or separately launched model process.
- **This repository owns only the Shell V2 six-module boundary:**
  1. installation and lifecycle;
  2. OpenMontage Package Registration and Locator;
  3. runtime preparation on demand;
  4. session Launcher;
  5. WorkBuddy entry;
  6. status and result relay.

The Shell must not become a Director, workflow engine, Agent host, production FSM, or media control plane. Repository agents must not run a video Pipeline, Provider, media generation, or OpenMontage production work from this tree.

The Golden Key WorkBuddy delivery must include its complete required private toolchain: a usable package-private Python 3.10+ environment with locked core dependencies, FFmpeg plus ffprobe, and Node.js plus npm/npx. Node must satisfy the highest current Package requirement; because current HyperFrames requires Node.js 22+, do not freeze only the README minimum of 18+. Stage 2 has accepted the Registration/Locator implementation and one real temporary-Package proof for these bytes, including real assembly, register, task-only activate, and new-process locate. That proof was cleaned up: it is not a retained final Release, installed production PackageRoot, or production Package Registration, but cleanup does not reopen or invalidate the accepted Stage 2 capability and evidence. Never report Stage 2 `PASS_ACCEPTED` as proof that the final distributable Package exists, and never repeat Stage 2 implementation as a new Stage 3 gate.

Stage 3 owns bounded detection and user-authorized integration of the optional OpenMontage capabilities Remotion and HyperFrames. Either capability may already exist, may be integrated later, or may remain absent; absence or a user decision to decline or defer integration is `SKIPPED/NOT_INTEGRATED`, not a Package or project failure. Detection may use only managed DataRoot paths, explicitly registered or configured candidate paths, and normal command resolution; it must never enumerate drives, system software inventories, global npm state, or guessed directories. For each `MISSING` or `INCOMPATIBLE` capability, Stage 3 returns a zero-download user-facing plan using source, version, size, license, target, and verification facts from the approved OpenMontage capability definition. WorkBuddy asks whether to download and integrate, and only explicit per-capability authorization permits the approved missing items. Shell never selects the renderer; OpenMontage decides whether production uses Remotion, HyperFrames, another available capability, or only the base toolchain. Mainland-China mirrors are mandatory for optional downloads and no automatic overseas fallback is allowed.

Stages 3, 4, 5, and 6 are built and accepted in numeric order, but end-user use starts at the Stage 5 WorkBuddy entry. Stage 5 asks Stage 2 Locator to revalidate the retained production Package. Stage 4 may make a base fixed-tool call using only that verified required toolchain. WorkBuddy/OpenMontage then owns the renderer decision. A bundled-FFmpeg or other already available path continues when Remotion or HyperFrames is absent, declined, or deferred. Execution of a detected or newly integrated optional capability requires Stage 3 evidence for that capability and approved definition, but not a Package Release declaration or capability Lock. WorkBuddy owns pause, consent, and continuation; Shell never selects the renderer or automatically replays the original business request. Stage 6 only relays the resulting facts.

The previous Stage 3 execution packets that treated Python dependencies, FFmpeg, Node, Package identity metadata, or Package Registration as Stage 3 inputs are superseded. Stage 3 is `PASS_ACCEPTED`: implementation `a3f8959682d296301dc573c2835f8c705a52e8b2` and closeout `7c15aae4e77c579309312b21c79076f930970214` are formally promoted. Its one public entry is `prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`; accepted evidence is 55 direct, 10 repository-hygiene, and 199 full tests, all final exit 0 with no skip. This does not prove real third-party or mainland-mirror download, production DataRoot integration, WorkBuddy, Stage 4, Provider, media, or video E2E. Python, FFmpeg, and Node remain Stage 2 required toolchain facts and are never Stage 3 detection or download targets. `V2-FINAL-PACKAGE-MATERIALIZATION-AND-PRODUCTION-REGISTRATION-GATE1` remains a later final-delivery or Installer task due before Stage 5 real WorkBuddy production acceptance; it is not a Stage 3 or Stage 4 coding or planning prerequisite.

Stage 4 is eligible for a separately authorized planning handoff only after the current nine-document sync is reviewed and formally promoted; Stage 4 implementation remains `NOT_GRANTED`. Its sole target is one immutable real-process receipt for one fixed Package tool call in a WorkBuddy-owned session: first call `locate_active_package(data_root)` and revalidate the active Package and required toolchain; only when the call explicitly executes an optional capability require Stage 3 `PRESENT` or `INTEGRATED` evidence for the same capability and definition. A base required-toolchain call never depends on Remotion or HyperFrames. Stage 4 must not accept arbitrary shell or commands, parse user intent, read an unverified Package Guide, launch another Agent, install Runtime, choose a renderer, retry or replay, schedule work, run media production, create Artifacts, or advance Checkpoints. Literal `user_message` and `executor_controls` remain separate and Stage 4 cannot rewrite the message.

The current Stage 2 Locator returns revalidated Registration, PackageRoot, required-toolchain, Guide, Manifest, and Lock identities, but no authoritative fixed Package tool-entry identity. The exact Stage 4 public entry and immutable receipt field names are also not frozen. A future Stage 4 planning authority must close those two items before any implementation grant; the approved OpenMontage Package definition and later final-delivery/Installer owner must supply a verifiable fixed tool identity without reopening Stage 2 or making final Package materialization a planning prerequisite. Real WorkBuddy new-session behavior, one WorkBuddy entry, per-capability questions, unchanged literal message, and same-task continuation belong to Stage 5. Stage 6 is evaluated only after a Stage 4 receipt and real Stage 5 consumer exist; direct consumption requires `STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE` with zero production code.

## External Package Guide

An external Package's `AGENT_GUIDE.md` is not this repository's operating guide. It may be read only by the downstream consumer authorized for a session, and only after Package Registration identity validation has succeeded and the Locator has returned the verified PackageRoot and Guide identity. Never scan disks, guess a Package, or read an unverified Guide as authority.

## Messages and controls

Keep the literal `user_message` separate from `executor_controls`. Package identity, paths, Python, cwd, retries, tests, stop conditions, routing, and evidence collection belong only in executor controls. Do not inject technical routing language into the user's message.

## State authority

`docs/workbuddy/v2/TASK-REGISTER.md` is the live authority for task, stage, authorization, exact Git object, and next action. Product responsibilities are in `PROJECT-CHARTER.md`; accepted Package Registration behavior is in `PACKAGE-REGISTRATION-CONTRACT.md`; stop and Git rules are in `DRIFT-GUARD.md`.

If those sources disagree, stop fail-closed and report the conflict. Do not infer authorization from old plans, prompts, chat history, tests, or Git history.

## Git task lifecycle

- Start every implementation task from the latest exact commit on `origin/codex/workbuddy-shell-v2` specified by the live task authority.
- A Builder branch is temporary isolation for one bounded task.
- A Reviewer is independent and read-only; review does not require a long-lived branch.
- Reviewer approval or user acceptance is not repository delivery. A task or stage is repository-complete only after its reviewed result is integrated into `origin/codex/workbuddy-shell-v2`.
- The formal branch advances only by fast-forward to a reviewed integration result. Do not merge or rebase advancing `main` or old long-lived branches into it.
- After promotion, delete fully integrated temporary remote branches that have no unmerged commits. Delete a local branch only after its worktree is closed.
- A later stage takes over only from the newest exact formal-branch commit, never from a task branch.

Use exact path allowlists, preserve unrelated worktrees and user data, and treat object mismatch, missing evidence, timeout, truncated output, or no final exit as `INCOMPLETE`.
