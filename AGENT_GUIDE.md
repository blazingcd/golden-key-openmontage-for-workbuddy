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

Stages 3 and 4 are built and accepted in numeric order; Stage 5 planning is accepted and its implementation result is recorded in the current mirror, while Stage 5 implementation closeout remains governed by that mirror. Stage 6 remains a later relay boundary and is not currently authorized. End-user use starts at the Stage 5 WorkBuddy entry. Stage 5 asks Stage 2 Locator to revalidate the retained production Package. Stage 4 may make a base fixed-tool call using only that verified required toolchain. WorkBuddy/OpenMontage then owns the renderer decision. A bundled-FFmpeg or other already available path continues when Remotion or HyperFrames is absent, declined, or deferred. Execution of a detected or newly integrated optional capability requires Stage 3 evidence for that capability and approved definition, but not a Package Release declaration or capability Lock. WorkBuddy owns pause, consent, and continuation; Shell never selects the renderer or automatically replays the original business request. Stage 6 only relays the resulting facts when separately authorized.

The previous Stage 3 execution packets that treated Python dependencies, FFmpeg, Node, Package identity metadata, or Package Registration as Stage 3 inputs are superseded. Stage 3 is `PASS_ACCEPTED`: implementation `a3f8959682d296301dc573c2835f8c705a52e8b2` and closeout `7c15aae4e77c579309312b21c79076f930970214` are formally promoted. Its one public entry is `prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`; accepted evidence is 55 direct, 10 repository-hygiene, and 199 full tests, all final exit 0 with no skip. This does not prove real third-party or mainland-mirror download, production DataRoot integration, WorkBuddy, Stage 4, Provider, media, or video E2E. Python, FFmpeg, and Node remain Stage 2 required toolchain facts and are never Stage 3 detection or download targets. `V2-FINAL-PACKAGE-MATERIALIZATION-AND-PRODUCTION-REGISTRATION-GATE1` remains a later final-delivery or Installer task due before Stage 5 real WorkBuddy production acceptance; it is not a Stage 3 or Stage 4 coding or planning prerequisite.

Stage 4 planning is `PASS_ACCEPTED`: the reviewed plan was promoted at `5cb3f585a0cddffbd823c785b1d39ebd1834c1df`, and its state closeout was promoted at `dfd97f3d2e05a4c448448fc14514d1cfe76836e8`. The six-authority implementation sync and the independently approved secret-nondisclosure clarification were subsequently promoted, so the former "waiting for authority sync/Builder takeover" state is historical and no longer a live blocker.

The bounded Stage 4 implementation was ordinary-fast-forwarded through `fa9adb8470ab94b88ec9900ede03cb26f7de0ebd` (tree `0809d1c4cccc9838180a016c75320b0d9fbce28a`) after eighth-round independent zero-write review returned `APPROVE / P0=0 / P1=0 / P2=0`. Official CI run `32367792637` then failed only because the test fixture incorrectly assumed the GitHub `setup-python` installation contained `pyvenv.cfg`; it did not identify a production Launcher defect. The one-test-file portability correction was independently approved with `P0=0 / P1=0 / P2=0`, ordinary-fast-forwarded as `13a3227b0c55bbe9039b46d7e92eba822b48f57e` (tree `d3ac89ec89b66789cabe92d94c3e827f9c2cc22f`), and official Ubuntu 24.04 / Python 3.11.16 CI run `32369588814` completed successfully with `357 passed / 1 skipped / exit 0`. Final Builder evidence is `158` direct, `11` repository-hygiene, and `358` combined tests on Windows, all exit 0 with no skip. The implementation changed exactly the five frozen paths and moved the tracked tree from 35 to 37.

Stage 4 implementation is `PASS_ACCEPTED`. Its fixed historical closeout anchor is `b63d8c2bc2214bc39f18378dbe47057ef538301e` (tree `02814c6a4a483913e7b1abe3e9ee6d025236c951`); `V2-S4-IMPLEMENTATION-CLOSEOUT-REVIEW1` returned `APPROVE / P0=0 / P1=0 / P2=0`, and closeout CI run `32371507874` completed successfully on Ubuntu 24.04 / Python 3.11.16 with `357 passed / 1 skipped`. The sentence "There is no active product task and no next authorized task" is a `HISTORICAL_STAGE4_CLOSEOUT_CONTEXT` snapshot only; it does not govern the current Stage 5 authority. The self-resolving mirror record below determines repository delivery only; it does not reopen or condition the already-effective Stage 4 product state.

The accepted minimum contract remains provider- and runtime-opaque: a release-specific immutable `PackageToolDefinitionV1` supplied by the approved Package definition/final-delivery Installer owner, one public `launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)` entry, exactly one fixed Package-tool spawn, and one recursively immutable `LauncherReceiptV1` whose outcome is limited to the nine accepted values. Stage 4 first calls `locate_active_package(data_root)` and revalidates the Package, required toolchain, definition, tool, and interpreter; it never guesses an entry from a Guide, directory, registry, caller command, or system PATH. Stage 4 has no WSL runtime dependency: WSL was used only for temporary Linux-equivalence validation and was cleaned and shut down after testing. Real production WorkBuddy/Launcher sessions, Provider or media execution, Stage 6, and final Package materialization/production registration remain `NOT_GRANTED` and unproven. The phrase "after closeout there is no next authorized task" is historical Stage 4 context only; current Stage 5 task and next-action values are read from `docs/workbuddy/v2/TASK-REGISTER.md`.

Stage 4 does not hard-code, select, configure, or route any Provider or runtime, including Remotion or HyperFrames. Provider configuration is separate external-service input and only definition-allowlisted environment names reach the child process. Local Stage 3 evidence is accepted only when `PackageToolDefinitionV1.required_local_capabilities` declares the same opaque capability and definition; the caller must pass the complete approved definition plus the unmodified original Stage 3 fact, and Stage 4 independently revalidates bytes using the accepted `managed`, `explicit`, or `PATH` source semantics. A base fixed-tool call never requires optional local-capability evidence. Stage 4 must not accept arbitrary shell or commands, parse user intent, read an unverified Package Guide, launch another Agent, install Runtime, choose a renderer, retry or replay, schedule work, run media production, create Artifacts, or advance Checkpoints. Literal `user_message` and `executor_controls` remain separate. Real WorkBuddy new-session behavior and continuation belong to Stage 5; Stage 6 first attempts direct `LauncherReceiptV1` reuse with zero production code.

Stage 5 is `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`. The `V2-S5-WORKBUDDY-ENTRY-BUILDER1` implementation and its six-document closeout are formally delivered as repository changes, but they prove only the entry-code/static contract layer; they do not make the whole Stage 5 `PASS_ACCEPTED`. Final Package/PackageRoot/Registration/Activation, a final installed Skill, and a real WorkBuddy-produced `LauncherReceiptV1` remain absent or unproved. R00 is formally promoted and consumed. The original R01 was separately authorized, executed, and formally closed at `9eefe8600d9bed0c8ea6024880e4b2d2ef4e3bfc`; the independent R01 refresh1 docs result `6c20371f1c72ee9d55147e1ad7feb8ede201858f` was independently approved and remains `BLOCKED_EXTERNAL_CONTRACT` for missing Skill-root cwd/bundled-relative resolution, not because PowerShell is non-native. No R02-R08 task is authorized by the blocked chain.

## Current Stage 5 remainder mirror

```text
entry_code_task: V2-S5-WORKBUDDY-ENTRY-BUILDER1 / CONSUMED_COMPLETE / ENTRY_CODE_COMPLETE
entry_code_formal_result: 0e7a0be65877b03fb386e1c6c6bc258c0b27db6c / tree 85c266edb7349c940e8cd45870cc0538c95726c0 / parent aa70c2cf9b6b4a29517d7354f0239ea0cdc9a5d3
entry_code_scope: EXACT_5_PATHS / tracked 37->40
entry_code_reviewer: APPROVE / P0=0 / P1=0 / P2=0
entry_code_windows_evidence: direct 19 passed / hygiene 11 passed / full 377 passed / final exit 0
entry_code_ci: run 32489111184 / completed / success / headSha=0e7a0be65877b03fb386e1c6c6bc258c0b27db6c / Ubuntu / Python 3.14.7 / 376 passed / 1 skipped / final exit 0
entry_closeout: V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1 / FORMALLY_DELIVERED_DOCS_ONLY / NOT_STAGE5_PASS
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
final_package_artifact: NOT_MATERIALIZED
production_package_root: NOT_CREATED
production_registration_activation: NOT_CREATED
final_installed_skill: NOT_CREATED
real_workbuddy_launcher_receipt: NOT_PROVED
current_task: NONE / NO_ACTIVE_TASK / R01_REFRESH1_ACCEPTED_BLOCKED_EXTERNAL_CONTRACT
after_r00_promotion: CONSUMED_COMPLETE / ORIGINAL_R01_EXECUTED_AND_FORMALLY_CLOSED
after_r01_closeout_promotion: ORIGINAL_R01 current_task=NONE / NO_ACTIVE_TASK / next_authorized_task=NONE / REFRESH1_ACCEPTED_BLOCKED_EXTERNAL_CONTRACT / R02-R08_BLOCKED_BY_CHAIN
next_planned_task: NONE / R02-R08_NOT_STARTED_NOT_AUTHORIZED_BY_CHAIN
```

The entry-code contract remains one WorkBuddy-managed Skill as the sole Agent/user entry, one package-private fixed CLI transport adapter, and exactly one accepted Stage 4 call with a real `LauncherReceiptV1`. It has no console script, subcommands, router, MCP, second Agent, retry or replay; JSON, provider-secret, fixed-environment identity, cancellation and receipt boundaries remain as frozen. Static, direct-test, hygiene and CI evidence does not prove a real WorkBuddy business/E2E session. The complete Stage 5 gate and ordered R01-R08 remainder are authoritative in `docs/workbuddy/v2/TASK-REGISTER.md`.

## [ORIGINAL R01 / FORMALLY CLOSED / PRESERVED] Stage 5 R01 evidence mirror

R00 is consumed. User authorization for Stage 5 continuation and per-task independent review was given on `2026-08-22`. R01 was executed only through official WorkBuddy documentation review and a controlled client attempt. The product-goal recheck is `PASS`: WorkBuddy remains the only running Agent and user entry; Shell remains limited to six modules and does not become a Director, FSM, second Agent, or media control plane. The scope-expansion audit is also `PASS`: the fixed internal CLI remains eligible only as an internal bridge inside the sole Skill; no arbitrary CLI bypass was authorized.

Official current sources used for the R01 record are WorkBuddy Skills (`https://cloud.tencent.com/document/product/1831/134432`, executable scripts/workflows and local upload/invocation shape), the local AI workbench task bar (`https://cloud.tencent.com/document/product/1831/134391`, installed Skill selection/automatic invocation in new tasks), and update notes (`https://cloud.tencent.com/document/product/1831/134324`, support history only, not exact execution semantics). `https://cloud.tencent.com/document/product/1831/134516` remains a CodeBuddy `PRODUCT_MISMATCH` and is not WorkBuddy contract proof.

The controlled client was WorkBuddy `5.3.14`. Baseline installed Skills were exactly `2` (`agent-browser`, `find-skills`). The reviewed temporary ZIP `r01-controlled-probe.zip` was uploaded; the safety scan was not skipped, the Skill was auto-installed, installed count became `3`, and the exact `golden-key-openmontage-r01-controlled-probe` identity appeared. An isolated new task attached that sole probe and selected `Hy3` (never Auto). The exact success-case prompt requested the relative bundled script, one literal JSON plus final LF on stdin, one fixed environment marker, and native stdout/stderr/final-exit/cwd/timeout capture.

The HY3 execution path exposed only Bash/PowerShell shell execution and no independent native bundled-script invocation/tool event. Generation was stopped before any shell or terminal execution. No probe script ran; no stdout, stderr, final exit, cwd, or timeout evidence exists. Under the frozen R01 contract, the whole R01 result is `BLOCKED_EXTERNAL_CONTRACT`; the non-zero and timeout cases were not run. Independent zero-write review returned `APPROVE / P0=0 / P1=0 / P2=0`, and the docs result was formally fast-forwarded at `9eefe8600d9bed0c8ea6024880e4b2d2ef4e3bfc`. The user then uninstalled the temporary Skill; WorkBuddy's installed-Skill view showed `2`, task history remained, and the two baseline Skills were untouched. The exact isolated D-drive probe folder and ZIP were deleted. R02-R08 are `NOT_STARTED / NOT_AUTHORIZED_BY_CHAIN`.

R01 evidence artifact hashes (historical; sources deleted after review and not tracked) are: `SKILL.md` `D1BE59EF9221BA739482555744385244C86B771F5604DB738F5E0952CCC1E1`; `scripts/r01_contract_probe.py` `52B1F6283FF376F99DE49AE87EF24781042DC12F679AAAF7F976F58F19307064`; ZIP `C55C90B7E86E9399F04EF13B8D78DF9228A8D72F7149B5B2A11B4362320F102D`. This docs-only mirror does not create or promote a Package, Registration, Installer, final Skill, Stage 4 spawn, Provider, media flow, or Stage 6.

## Current Stage 5 R01 Sandbox Refresh1 accepted result mirror (2026-08-22)

This is an independent refresh of the original R01 and does not rewrite the original record. The product-goal recheck and scope-expansion audit are `PASS`: WorkBuddy remains the only running Agent/user entry; the fixed CLI remains eligible only as an internal bridge inside that sole Skill, not a blanket CLI ban or a second control plane. Official WorkBuddy 134420 explicitly says enterprise Skill scripts execute in the client sandbox. In the controlled WorkBuddy observation, PowerShell is an `ELIGIBLE_CANDIDATE_SURFACE`, not an official exact execution contract. 134432 proves Skill script/workflow packaging and upload/invocation shape; 134516 remains CodeBuddy `PRODUCT_MISMATCH_NOT_CONTRACT_PROOF`. The remaining official gaps are bundled-relative resource resolution, Skill-root cwd, stdin/stdout/stderr/final-exit, and timeout semantics.

```text
task_id: V2-S5-R01-WORKBUDDY-SANDBOX-REFRESH1
candidate_branch: codex/v2-s5-r01-sandbox-refresh1-closeout
base_commit: 932bcabc5baf90d0190101b1039e4ccf087b2b08 / tree 2ed2cd0e67dd8628b7f0b1acf84df0a7d8b0d0fd / tracked 40
workbuddy: 5.3.14 / baseline=agent-browser,find-skills / HY3_ONLY / NEVER_AUTO
refresh1_hashes: SKILL=A369E89912B51C1627C972A7DE8F82111E55E2909622CB2E0E3276B45331FFF9 / SCRIPT=8A1D38A65945CC99C4B7F8EE95FDF4FF744D105303BC9904E5915E630DF58359 / ZIP=2284E6D6FE8FFD38689A357DD0A6653CEB23B923F0C531BF9EAC376178E9A28A
refresh1_source_root: ISOLATED_D_DRIVE_TEMP_ROOT / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / CLEANUP_COMPLETE / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND
install_observation: SAFETY_SCAN_NOT_SKIPPED / NO_NON_HIGH_RISK_AUTO_INSTALL_SELECTED / installed_count=3 / client_id=workbuddy-skill-1787379691395 / SKILL_MD_NO_METADATA_NAME / BODY_FIRST_LINE_MATCHED_PROBE / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
native_read_event: PRESENT / BUNDLED_SKILL_MD_AND_SCRIPT_READ / PHYSICAL_INSTALL_PATH_EXPOSED_CONTRACT_DEVIATION / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
frozen_success_observation: SESSION_WORKSPACE_CWD / FROZEN_RELATIVE_SCRIPT / NO_CD_NO_ABSOLUTE_PATH_NO_GUESSING_NO_COMMAND_MUTATION / SKILL_ROOT_CWD_NOT_EXPOSED / BUNDLE_RELATIVE_INVOCATION_NOT_EXPOSED / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
execution: POWERSHELL_NOT_STARTED / USER_CANCELLED / NO_SCRIPT_EXECUTION / NO_STDOUT_STDERR_FINAL_EXIT_CWD_CLASSIFICATION_TIMEOUT
reviewer_independent_observation: WORKBUDDY_5.3.14 / HY3 / USER_CANCELLED / NO_SUCCESS_STDOUT_STDERR_EXIT_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
result: BLOCKED_EXTERNAL_CONTRACT / MISSING_SKILL_ROOT_CWD_AND_BUNDLE_RELATIVE_RESOLUTION / NOT_BECAUSE_POWERSHELL_IS_NON_NATIVE
review: APPROVE / P0=0 / P1=0 / P2=0
nonzero_case: NOT_RUN
timeout_case: NOT_RUN
r02_r08_status: NOT_STARTED / NOT_AUTHORIZED_BY_CHAIN
temporary_skill: UNINSTALLED / USER_UNINSTALLED_TEMPORARY_SKILL / TEMP_SKILL_ID=workbuddy-skill-1787379691395_NOT_IN_INSTALLED_LIST / WORKBUDDY_MY_INSTALLED_SKILLS_2=agent-browser,find-skills / TASK_HISTORY_RETAINED / BASELINE_SKILLS_UNTOUCHED / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND
computer_use_transparency: LOW_IMPACT_OPERATIONAL_ANOMALY / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / EXISTING_EXPLORER_MISTAKEN_FOR_FILE_PICKER / ALT+N_MAY_OPEN_TAB_OR_WINDOW / NO_PATH_INPUT_NO_FILE_SELECTION_NO_WRITE_DELETE / STOPPED_AND_RECOVERED
accepted_result_commit: 6c20371f1c72ee9d55147e1ad7feb8ede201858f / tree 9eb4643f09d03cc9f39b0b46906773e5bcc9125d
docs_review: APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_ZERO_WRITE_REVIEW
candidate_current_task: NONE / NO_ACTIVE_TASK / R01_REFRESH1_ACCEPTED_BLOCKED_EXTERNAL_CONTRACT
candidate_next_authorized_task: NONE / R02-R08_BLOCKED_BY_CHAIN
candidate_test: NOT_RUN_DOCS_ONLY / product_code=0 / tests=0 / ci=0 / provider_media_package_stage4_stage6=0
candidate_push: FORMALLY_EFFECTIVE_IFF_LIVE_REMOTE_REF_CONTAINS_THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR
```

The refresh1 accepted result is not Stage 5 `PASS_ACCEPTED`; it keeps `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`. The original R01 “Bash/PowerShell-only” observation remains preserved as historical evidence, while refresh1’s blocker is only the missing Skill-root cwd/bundled-relative contract. Nonzero/timeout remain unrun, and no Provider, media, Package, Stage 4, Stage 6, or production flow ran.

## Stage 5 Expert Entry Feasibility1 closeout (2026-08-22)

This is a separate zero-product-state-change feasibility record. It does not rewrite either R01 record, create or publish an Expert, create or install a Skill or Package, add a new R01 gate, or authorize R02-R08. Official WorkBuddy documentation treats an Expert as a WorkBuddy role layer and says configured Skill/MCP can provide indirect file or external-service access; it gives no official proof that an Expert can replace an executable Skill. `DOES_NOT_SUPERSEDE_SOLE_SKILL_ENTRY` and `NOT_PROVED` below are this project's evidence ruling, not a Tencent official conclusion. The controlled-client observations below are not official execution-contract proof, and any model or built-in Skill self-report is explicitly non-authoritative.

```text
task_id: V2-S5-EXPERT-ENTRY-FEASIBILITY1
task_kind: OFFICIAL_DOCS_PLUS_CONTROLLED_CLIENT_STATIC_CLOSEOUT / ZERO_PRODUCT_STATE_CHANGE
official_sources: 134393=WORKBUDDY_EXPERT_ROLE_LAYER / 134393+134432=SKILL_OR_MCP_CAN_PROVIDE_INDIRECT_FILE_OR_EXTERNAL_SERVICE_ACCESS / 134421=EXPERT_PACKAGE_AND_MANAGEMENT / 134432=EXECUTABLE_SKILL_SCRIPTS_WORKFLOWS
official_source_urls: https://cloud.tencent.com/document/product/1831/134393 / https://cloud.tencent.com/document/product/1831/134421 / https://cloud.tencent.com/document/product/1831/134432
official_contract_gap: NO_OFFICIAL_PROOF_EXPERT_CAN_REPLACE_EXECUTABLE_SKILL
workbuddy_client: 5.3.14 / HY3_ONLY / NEVER_AUTO
client_expert_observation: MY_EXPERT_COUNT=0 / CREATE_ENTRY_OPENED_EXPERT_MANAGER_CONVERSATION / NO_EXPERT_CREATED_SAVED_OR_PUBLISHED
expert_manager_observation: CANNOT_DIRECTLY_BIND_INSTALLED_SKILL / CANNOT_LOCK_HY3 / SAME_CONVERSATION_MAY_PROMPT_GLOBAL_SKILL / BUNDLED_AUTOLOAD_NOT_PROVED
unofficial_observation_boundary: MODEL_OR_BUILTIN_SKILL_SELF_REPORT_NOT_OFFICIAL_CONTRACT
project_evidence_ruling: INCOMPLETE / EXPERT_AS_SOLE_VISIBLE_ENTRY_NOT_PROVED / DOES_NOT_SUPERSEDE_SOLE_SKILL_ENTRY / NOT_PROVED / R01_UNCHANGED_BLOCKED_EXTERNAL_CONTRACT
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
current_task: NONE / NO_ACTIVE_TASK
next_authorized_task: NONE / R02-R08_NOT_STARTED_NOT_AUTHORIZED_BY_CHAIN
review: APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_REVIEWER
anti_expansion: PASS / NO_EXPERT_OR_PACKAGE_OR_SKILL_CREATED / NO_NEW_R01_GATE / NO_PROVIDER_MEDIA_PACKAGE_STAGE4_STAGE6_OR_PRODUCTION
```

## External Package Guide

An external Package's `AGENT_GUIDE.md` is not this repository's operating guide. It may be read only by the downstream consumer authorized for a session, and only after Package Registration identity validation has succeeded and the Locator has returned the verified PackageRoot and Guide identity. Never scan disks, guess a Package, or read an unverified Guide as authority.

## Messages and controls

Keep the literal `user_message` separate from `executor_controls`. Package identity, paths, Python, cwd, retries, tests, stop conditions, routing, and evidence collection belong only in executor controls. Do not inject technical routing language into the user's message.

## State authority

`docs/workbuddy/v2/TASK-REGISTER.md` is the live authority for task, stage, authorization, exact Git object, and next action. Product responsibilities are in `PROJECT-CHARTER.md`; accepted Package Registration behavior is in `PACKAGE-REGISTRATION-CONTRACT.md`; stop and Git rules are in `DRIFT-GUARD.md`.

```text
formal_ref: refs/heads/codex/workbuddy-shell-v2
formal_head_resolution: LIVE_REMOTE_REF_REQUIRED
formal_tree_resolution: LIVE_REMOTE_REF_TREE_REQUIRED
mirror_result: THIS_COMMIT
mirror_effect: ZERO_PRODUCT_STATE_CHANGE
mirror_repository_delivery_resolution: zero-write APPROVE exists AND LIVE_REMOTE_REF contains THIS_COMMIT
```

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
