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

The Golden Key WorkBuddy delivery must include its complete required private toolchain: a usable package-private Python 3.10+ environment with locked core dependencies, FFmpeg plus ffprobe, and Node.js plus npm/npx. Node must satisfy the highest current Package requirement; because current HyperFrames requires Node.js 22+, do not freeze only the README minimum of 18+. Stage 2 has accepted the Registration/Locator implementation and one real temporary-Package proof for these bytes. That proof was cleaned up: it is not a retained final Release, installed production PackageRoot, or production Package Registration. Never report Stage 2 `PASS_ACCEPTED` as proof that the final distributable Package exists.

Stage 3 owns only optional capability preparation requested by a verified WorkBuddy/OpenMontage production decision, currently Remotion or HyperFrames and only the exact browser/runtime assets declared by that selected capability. Shell does not select the renderer, and ordinary users approve the locked download plan rather than choosing technical components. Optional discovery may use only managed paths, an explicitly registered capability record, or normal command resolution; never scan drives. Mainland-China mirrors are mandatory for end-user optional downloads and no automatic overseas fallback is allowed.

Stages 3, 4, 5, and 6 are built and accepted in numeric order, but end-user use starts at the Stage 5 WorkBuddy entry. Stage 5 asks Stage 2 Locator to revalidate the retained production Package. Stage 4 may make a base fixed-tool call using only that verified required toolchain. WorkBuddy/OpenMontage then owns the renderer decision. A bundled-FFmpeg path continues without Stage 3; an optional Remotion or HyperFrames execution additionally requires a Stage 3 receipt bound to the same Registration and Package-owned capability Lock. WorkBuddy owns pause, consent, and continuation; Shell never selects the renderer or automatically replays the original business request. Stage 6 only relays the resulting facts.

The previous Stage 3 execution packet that treated Python dependencies, FFmpeg, and Node as discover/install targets is superseded. Replanned Stage 3 has one proposed public entry, `prepare_optional_capability(data_root, capability_request, authorization_receipt=None)`, and at most one new production module plus one export-only edit and one direct test file. Its Lock is owned by the verified Package, not duplicated by Shell. Planning may proceed, but implementation remains `NOT_GRANTED` until a final Package is retained and production-registered, Locator revalidation succeeds in a new process, the real WorkBuddy/OpenMontage consumer contract and Package-owned optional capability Lock are frozen, and the live task authority grants the exact Builder packet.

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
