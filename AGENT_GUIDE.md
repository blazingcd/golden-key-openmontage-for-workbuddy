# WorkBuddy Shell V2 Agent Guide

Read this file completely before acting in this repository.

## Product boundary

- **WorkBuddy owns the user conversation.** It receives the user's literal business request and presents results.
- **The OpenMontage Agent owns production.** It runs from a verified, external OpenMontage Package and owns Pipeline, Stage, Artifact, Checkpoint, Reviewer, Tool, Provider, model, media, and creative decisions.
- **This repository owns only the Shell V2 six-module boundary:**
  1. installation and lifecycle;
  2. OpenMontage Package Registration and Locator;
  3. runtime preparation on demand;
  4. session Launcher;
  5. WorkBuddy entry;
  6. status and result relay.

The Shell must not become a second Director, workflow engine, Agent host, production FSM, or media control plane. Repository agents must not run a video Pipeline, Provider, media generation, or OpenMontage production work from this tree.

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
