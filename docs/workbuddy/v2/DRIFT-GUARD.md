# WorkBuddy Shell V2 — Drift Guard

## One-line product test

Can an ordinary user type a natural-language message containing
`金钥匙智能体` in WorkBuddy and obtain the current product result without doing
internal technical work? If not, stop and report the exact missing user result.

## Ownership guard

- WorkBuddy is the only Agent, dialogue owner, and production decision-maker.
- OpenMontage Package is the production-semantic source.
- Shell is only installation/lifecycle, Registration/Locator, runtime preparation,
  fixed mechanical invocation, WorkBuddy entry, and status/receipt relay.
- Shell must not become a second Agent, Director, workflow engine, provider/
  renderer selector, media control plane, MCP, router, or generic framework.
- The external Package `AGENT_GUIDE.md` is read only by WorkBuddy after a verified
  PackageRoot and Guide identity are returned.

## User-input guard

The sole wake condition is the literal substring `金钥匙智能体` in the original
message. Do not hard-code the rest of a prompt, business description, material
path, or expected answer. Do not ask the user to construct path/hash/schema/env/
argv/pipe/command mechanics. WorkBuddy is a harness Agent: its internal reasoning,
tool path, steps, wording, and intermediate conclusions may vary for the same
input. Skills and prompts must not force a preset internal script.

Process variation is acceptable unless it directly causes product failure, adds
ordinary-user technical burden, creates a second control plane, or produces a false
result. Internal commands, tool choices, retries, and corrections are not failures
by themselves.

## Result guard

There are exactly four product results: R1 complete installable Shell; R2 complete
natural-language WorkBuddy invocation/reply/receipt; R3 next real playable video
and receipt; R4 ordinary-user acceptance and formal closeout. A result's review
must not import another result's gate. In particular, an absent video pointer in
R2 is not an R2 failure; it is the R3 artifact boundary.

Each result has one executor and one independent result review after a real
user-visible result. No packet, pre-review, multi-review, role maze, or repair loop.
The reviewer must judge the stated user goal first and may not invent architecture
requirements or a predetermined transcript. Internal state changes matter only
if they disprove that goal.

## Current closeout guard

The 2026-08-27 authorized closeout may slim and align the current authority,
entry, contract, and work-log documents, verify current R2 changes, perform one
independent read-only review, deliver the candidate to
`refs/heads/codex/workbuddy-shell-v2` by ordinary fast-forward, clean only verified
abandoned Git/task objects, and open a new follow-up task. It must not start R3,
WorkBuddy, media, or a Package rebuild.

## Engineering guard

- Project Python only:
  `D:\BlazingCD\Personal\.venvs\golden-key-openmontage-workbuddy-w0\Scripts\python.exe`.
- Temporary files only on D:, with exact post-review cleanup; preserve user data.
- Remotion and HyperFrames are deferrable and are not R3 prerequisites.
- Do not add a second Agent, MCP, router, or generic framework.

## Git and cleanup guard

- Formal ref: `refs/heads/codex/workbuddy-shell-v2`.
- Never force-push or `reset --hard`.
- Only ordinary fast-forward may advance the formal ref.
- Do not delete dirty worktrees, unmerged branches, branches with unique commits,
  or directories whose ownership/content has not been verified.
- Before any destructive action, resolve the exact absolute target, check that it
  is within the intended task scope, and use a recoverable operation when practical.
- After cleanup, verify the formal ref, worktree state, and retained evidence.
