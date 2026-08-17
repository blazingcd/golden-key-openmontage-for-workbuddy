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

The Golden Key WorkBuddy delivery includes its own package-private Python bootstrap. Stage 3 must not discover or depend on system Python. Other closed-set runtime components may be discovered only from managed paths, an explicitly registered host-tool record, or normal command resolution; never scan drives. Missing components may be prepared only from an identity-locked missing-only plan, after explicit user consent. Mainland-China mirrors are mandatory except for the one temporarily approved, exactly locked FFmpeg asset from `gyan.dev`; that exception remains unusable until a no-proxy/no-VPN mainland-network access probe passes. No automatic overseas fallback is allowed for any component.

Stages 3, 4, 5, and 6 are built and accepted in numeric order, but the end-user runtime call starts at the Stage 5 WorkBuddy entry. That entry revalidates Stage 2 registration, asks Stage 3 for one of its fixed outcomes, calls Stage 4 only with a valid runtime-ready receipt, and lets Stage 6 relay facts. A missing/incompatible Stage 3 outcome requires a separately authorized missing-only preparation and a later explicit WorkBuddy invocation; the Shell never automatically retries the original request.

Stage 3 has conditional user authorization only: do not implement it until the refreshed Stage 2 Package and this planning correction are independently accepted and promoted to the formal branch, the exact Package/Manifest/Lock/Guide/private-Python identity is revalidated, the private Python bootstrap can actually install and import the locked dependencies without system Python, and the current Package inputs are sufficient to freeze an exact Runtime Lock as Stage 3's first step. Stage 3 is one production module, one public entry, one Runtime Lock, and one direct test file. It writes only product-owned targets under `<DataRoot>/Runtime` and caches under `<DataRoot>/Caches`; it never changes Package bytes, system Python, PATH, or the registry.

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
