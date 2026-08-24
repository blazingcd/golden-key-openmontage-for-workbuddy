# WorkBuddy Shell V2 Agent Guide

Read this file completely before acting in this repository.

> **Current authority (2026-08-24):** Phase B product execution is `PAUSED_BY_OWNER`. The rebaseline section at the end of this file and the matching latest section in `docs/workbuddy/v2/TASK-REGISTER.md` supersede every earlier fixed-CLI/fixed-child/B01-B07 execution statement when they conflict. Earlier Stage records remain historical evidence only; they do not authorize work.

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

The historical Stage 4 mechanical contract was provider- and runtime-opaque: a release-specific immutable `PackageToolDefinitionV1` supplied by the approved Package definition/final-delivery Installer owner, one public `launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)` primitive, exactly one fixed Package-tool spawn per invocation, and one recursively immutable `LauncherReceiptV1` whose outcome is limited to the nine accepted values. Those mechanics may be retained only as a per-tool primitive after C01/C02; they are superseded as the end-to-end WorkBuddy request contract. Stage 4 first calls `locate_active_package(data_root)` and revalidates the Package, required toolchain, definition, tool, and interpreter; it never guesses an entry from a Guide, directory, registry, caller command, or system PATH. Stage 4 has no WSL runtime dependency: WSL was used only for temporary Linux-equivalence validation and was cleaned and shut down after testing. Real production WorkBuddy/Launcher sessions, Provider or media execution, Stage 6, and final Package materialization/production registration remain unproven. The phrase "after closeout there is no next authorized task" is historical Stage 4 context only; current authority is the rebaseline mirror at the end of this file.

Stage 4 does not hard-code, select, configure, or route any Provider or runtime, including Remotion or HyperFrames. Provider configuration is separate external-service input and only definition-allowlisted environment names reach the child process. Local Stage 3 evidence is accepted only when `PackageToolDefinitionV1.required_local_capabilities` declares the same opaque capability and definition; the caller must pass the complete approved definition plus the unmodified original Stage 3 fact, and Stage 4 independently revalidates bytes using the accepted `managed`, `explicit`, or `PATH` source semantics. A base fixed-tool call never requires optional local-capability evidence. Stage 4 must not accept arbitrary shell or commands, parse user intent, read an unverified Package Guide, launch another Agent, install Runtime, choose a renderer, retry or replay, schedule work, run media production, create Artifacts, or advance Checkpoints. Literal `user_message` and `executor_controls` remain separate. Real WorkBuddy new-session behavior and continuation belong to Stage 5; Stage 6 first attempts direct `LauncherReceiptV1` reuse with zero production code.

Stage 5 is `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`. The `V2-S5-WORKBUDDY-ENTRY-BUILDER1` implementation and its six-document closeout are formally delivered as repository changes, but they prove only the entry-code/static contract layer; they do not make the whole Stage 5 `PASS_ACCEPTED`. Final Package/PackageRoot/Registration/Activation, a final installed Skill, and a real WorkBuddy-produced `LauncherReceiptV1` remain absent or unproved. R00 is formally promoted and consumed. The original R01, R01 refresh1, and Expert Entry Feasibility records remain preserved as `HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT`, including their historical `BLOCKED_EXTERNAL_CONTRACT` or `INCOMPLETE` outcomes. The R01 entry surface was accepted, but R02 was closed as `BLOCKED_PACKAGE_RELEASE` because the published candidate lacks the required safe fixed-tool and release-specific definition binding. No next task is authorized; R03-R08 remain ordered and blocked by chain. This R02 result is a docs-only mirror, not new product or client evidence.

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
current_task: NONE / NO_ACTIVE_TASK / R02_CLOSED_BLOCKED_PACKAGE_RELEASE
next_authorized_task: NONE / PACKAGE_OWNER_RELEASE_BINDING_REAUTHORIZATION_REQUIRED
after_r00_promotion: CONSUMED_COMPLETE / ORIGINAL_R01_EXECUTED_AND_FORMALLY_CLOSED
after_r01_closeout_promotion: HISTORICAL / ORIGINAL_R01_AND_REFRESH1_SUPERSEDED_ACCEPTANCE_CONTRACT
next_planned_task: NONE / R03-R08_NOT_STARTED_NOT_AUTHORIZED_BY_CHAIN
```

The entry-code contract remains one WorkBuddy-managed Skill as the sole Agent/user entry, one package-private fixed CLI transport adapter, and exactly one accepted Stage 4 call with a real `LauncherReceiptV1`. It has no console script, subcommands, router, MCP, second Agent, retry or replay; JSON, provider-secret, fixed-environment identity, cancellation and receipt boundaries remain as frozen. Static, direct-test, hygiene and CI evidence does not prove a real WorkBuddy business/E2E session. The corrected R01 entry-surface acceptance does not claim script execution, stdout/stderr/exit/cwd/timeout, or receipt proof; implementation and real proof remain deferred to R03-R07. The complete Stage 5 gate and ordered R01-R08 remainder are authoritative in `docs/workbuddy/v2/TASK-REGISTER.md`.

## [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / ORIGINAL R01 / FORMALLY CLOSED / PRESERVED] Stage 5 R01 evidence mirror

R00 is consumed. User authorization for Stage 5 continuation and per-task independent review was given on `2026-08-22`. R01 was executed only through official WorkBuddy documentation review and a controlled client attempt. The product-goal recheck is `PASS`: WorkBuddy remains the only running Agent and user entry; Shell remains limited to six modules and does not become a Director, FSM, second Agent, or media control plane. The scope-expansion audit is also `PASS`: the fixed internal CLI remains eligible only as an internal bridge inside the sole Skill; no arbitrary CLI bypass was authorized.

Official current sources used for the R01 record are WorkBuddy Skills (`https://cloud.tencent.com/document/product/1831/134432`, executable scripts/workflows and local upload/invocation shape), the local AI workbench task bar (`https://cloud.tencent.com/document/product/1831/134391`, installed Skill selection/automatic invocation in new tasks), and update notes (`https://cloud.tencent.com/document/product/1831/134324`, support history only, not exact execution semantics). `https://cloud.tencent.com/document/product/1831/134516` remains a CodeBuddy `PRODUCT_MISMATCH` and is not WorkBuddy contract proof.

The controlled client was WorkBuddy `5.3.14`. Baseline installed Skills were exactly `2` (`agent-browser`, `find-skills`). The reviewed temporary ZIP `r01-controlled-probe.zip` was uploaded; the safety scan was not skipped, the Skill was auto-installed, installed count became `3`, and the exact `golden-key-openmontage-r01-controlled-probe` identity appeared. An isolated new task attached that sole probe and selected `Hy3` (never Auto). The exact success-case prompt requested the relative bundled script, one literal JSON plus final LF on stdin, one fixed environment marker, and native stdout/stderr/final-exit/cwd/timeout capture.

The HY3 execution path exposed only Bash/PowerShell shell execution and no independent native bundled-script invocation/tool event. Generation was stopped before any shell or terminal execution. No probe script ran; no stdout, stderr, final exit, cwd, or timeout evidence exists. Under the frozen R01 contract, the whole R01 result is `BLOCKED_EXTERNAL_CONTRACT`; the non-zero and timeout cases were not run. Independent zero-write review returned `APPROVE / P0=0 / P1=0 / P2=0`, and the docs result was formally fast-forwarded at `9eefe8600d9bed0c8ea6024880e4b2d2ef4e3bfc`. The user then uninstalled the temporary Skill; WorkBuddy's installed-Skill view showed `2`, task history remained, and the two baseline Skills were untouched. The exact isolated D-drive probe folder and ZIP were deleted. R02-R08 are `NOT_STARTED / NOT_AUTHORIZED_BY_CHAIN`.

R01 evidence artifact hashes (historical; sources deleted after review and not tracked) are: `SKILL.md` `D1BE59EF9221BA739482555744385244C86B771F5604DB738F5E0952CCC1E1`; `scripts/r01_contract_probe.py` `52B1F6283FF376F99DE49AE87EF24781042DC12F679AAAF7F976F58F19307064`; ZIP `C55C90B7E86E9399F04EF13B8D78DF9228A8D72F7149B5B2A11B4362320F102D`. This docs-only mirror does not create or promote a Package, Registration, Installer, final Skill, Stage 4 spawn, Provider, media flow, or Stage 6.

## [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT] Stage 5 R01 Sandbox Refresh1 accepted result mirror (2026-08-22)

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

## [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT] Stage 5 Expert Entry Feasibility1 closeout (2026-08-22)

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

## [HISTORICAL / CONSUMED_BY_V2-S5-R02] Stage 5 R01 acceptance-contract correction1 (2026-08-22)

The original R01, Sandbox Refresh1, and Expert Entry Feasibility records above are explicitly `HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT`; their observed facts and old `BLOCKED_EXTERNAL_CONTRACT` or `INCOMPLETE` outcomes remain preserved. This is a user-authorized project acceptance-ownership correction, not new official WorkBuddy evidence.

```text
task_id: V2-S5-R01-ACCEPTANCE-CONTRACT-CORRECTION1
task_kind: DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE / USER_AUTHORIZED_ACCEPTANCE_CORRECTION
r01_acceptance: ENTRY_SURFACE_ACCEPTED / EXECUTION_PROOF_DEFERRED_TO_R03_R07
r01_entry_surface_evidence: SKILL_PACKAGING / UPLOAD / INSTALL / IDENTITY_APPEARED / SELECTION_HIT / CLIENT_SANDBOX_SCRIPTS / POWERSHELL_ELIGIBLE_CANDIDATE_SURFACE
r01_deferred_unproved_contract: SKILL_ROOT_CWD / BUNDLED_RELATIVE_RESOURCE_RESOLUTION / STDIN / STDOUT / STDERR / FINAL_EXIT / TIMEOUT / NOT_R01_HARD_GATE / DEFERRED_TO_R03_R07
deferred_execution_chain: LOCATOR -> FIXED_POWERSHELL_OR_PRIVATE_CLI -> LAUNCHER_RECEIPT / IMPLEMENTATION_AND_REAL_PROOF_DEFERRED_TO_R03_R07 / NOT_CURRENTLY_PROVED
no_overclaim: NO_SCRIPT_EXECUTION_PROOF / NO_STDOUT_STDERR_EXIT_CWD_TIMEOUT_PROOF / NO_LAUNCHER_RECEIPT_PROOF / NOT_STAGE5_PASS
hy3_policy: CURRENT_TEST_MODEL_ONLY / COST_AVOIDANCE / PRODUCT_MODEL_NEUTRAL / USER_SELECTED_MODEL / NOT_A_SKILL_OR_EXPERT_OR_SYSTEM_DEPENDENCY
client_test_policy: AUTHORIZED_CLIENT_TESTS_FOLLOW_USER_HY3_AND_NEVER_AUTO / PRODUCT_MODEL_NOT_LOCKED
preserved_boundaries: ONE_WORKBUDDY_SKILL_AND_ONE_USER_ENTRY / FIXED_CLI_INTERNAL_BRIDGE_ONLY / NO_ARBITRARY_CLI / NO_PATH_GUESSING / NO_SCAN / NO_PATH_FALLBACK / NO_MCP / NO_SECOND_SKILL / NO_SECOND_AGENT / NO_ROUTER / NO_RETRY / NO_REPLAY / FINAL_SKILL_INSTALLER_STAMPED_LOCATOR
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
current_task: HISTORICAL / R01_CORRECTED_ACCEPTED_ENTRY_SURFACE
next_authorized_task: HISTORICAL / V2-S5-R02-PACKAGE-RELEASE-TOOL-DEFINITION-BINDING1 / R02_AUTHORIZED_ONLY
chain: HISTORICAL / R01_CORRECTED_ACCEPTED -> R02_AUTHORIZED -> R03_R08_STRICT_ORDER / R03-R08_NOT_AUTHORIZED
```

## Current Stage 5 R02 Package Release/Tool Definition Binding1 closeout (2026-08-22)

R02 is a docs-only closeout. The published candidate exists and its identity matches the approved source subtree, but it is not a bindable final Release: the verified tree and metadata do not provide a real safe fixed tool or a release-specific `PackageToolDefinitionV1`/Manifest/Lock binding. This result does not select a media tool, invent a fixture or definition, or modify the external Package.

```text
task_id: V2-S5-R02-PACKAGE-RELEASE-TOOL-DEFINITION-BINDING1
published_repo: blazingcd/golden-key-openmontage / branch=codex/golden-key-openmontage-v0.3.24
published_commit: ef5f5b58fa1c2b494b0154989cf0e4e36615a701
published_root_tree: 0464861c5985c7c9072e789b94889d29cf9a937a / approved_source_commit=8395e578165e802990d53fef5a166f8b4cf0461a / approved_source_commit_tree=4624394238802a9577690248e43b8f0dff391a2b / approved_source_package_subtree=0464861c5985c7c9072e789b94889d29cf9a937a
published_tree_audit: REMOTE_RECURSIVE_TRUNCATED_FALSE / entries=2614 / binding_path_filter=(workbuddy|package.?tool.?definition|launcher|fixed.?tool|entry.?cli) / binding_related_paths=0 / local_same_tree_blobs=2155
release_metadata: GOLDEN_KEY_OPENMONTAGE_RELEASE.json / release_version=0.3.24 / console_script_entrypoint=null / python_load_probe=lib.pipeline_loader:load_pipeline / authority_entry=README.md
lock_metadata: GOLDEN_KEY_OPENMONTAGE.lock.json / NO_PackageToolDefinitionV1 / NO_workbuddy_entry_cli / NO_package_tool_definition / NO_launcher / NO_fixed_tool / NO_CORRESPONDING_TOP_LEVEL_FIELDS
r02_result: BLOCKED_PACKAGE_RELEASE / PUBLISHED_CANDIDATE_IDENTITY_VERIFIED / MISSING_SAFE_FIXED_TOOL_AND_RELEASE_SPECIFIC_DEFINITION
no_overclaim: PUBLISHED_CANDIDATE_EXISTS / NOT_BINDABLE_FINAL_RELEASE / NO_FINAL_PACKAGE_OR_REGISTRATION_OR_LAUNCHER_RECEIPT_PROOF
preserved_r01_hy3_policy: R01_ENTRY_SURFACE_ACCEPTED / HY3_CURRENT_TEST_MODEL_ONLY / COST_AVOIDANCE / PRODUCT_MODEL_NEUTRAL / USER_SELECTED_MODEL / NOT_A_SKILL_OR_EXPERT_OR_SYSTEM_DEPENDENCY
product_goal_and_anti_expansion: PASS / WorkBuddy_ONLY_AGENT_USER_ENTRY / FIXED_CLI_ONLY_SOLE_SKILL_INTERNAL_BRIDGE / NO_ARBITRARY_MEDIA_TOOL_SELECTION_OR_FIXTURE_OR_DEFINITION_OR_EXTERNAL_PACKAGE_MODIFICATION
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
current_task: NONE / NO_ACTIVE_TASK / R02_CLOSED_BLOCKED_PACKAGE_RELEASE
next_authorized_task: NONE / PACKAGE_OWNER_RELEASE_BINDING_REAUTHORIZATION_REQUIRED / R03-R08_NOT_AUTHORIZED_BY_CHAIN
unblock_condition: SEPARATE_PACKAGE_OWNER_TASK_MUST_APPROVE_RELEASE_DELIVERY_AND_INDEPENDENTLY_VERIFY_SAFE_FIXED_TOOL_PLUS_RELEASE_SPECIFIC_DEFINITION_PLUS_MANIFEST_LOCK_BINDING / THEN_REAUTHORIZE_R02
side_effects: NO_CLIENT / NO_PACKAGE_MATERIALIZATION / NO_REGISTRATION / NO_STAGE4 / NO_PROVIDER_MEDIA_STAGE6_OR_PRODUCTION
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

## Phase A architecture-recovery audit result mirror (2026-08-22; A7 formally promoted)

This is the single self-contained result of the independently reviewed A0-A6 architecture-recovery audit. The A7 documentation result is formally promoted into the formal branch; it is not a product correction or a Phase B authorization. Existing historical facts and historical PASS results remain historical; the current product-architecture disposition is recorded separately.

```text
task_id: V2-PROJECT-ARCHITECTURE-RECOVERY-PHASE-A1
formal_ref: refs/heads/codex/workbuddy-shell-v2
formal_baseline_parent: f338d9d50cad2cccf1398438ad4a8c8d45127a21 / tree 5ef5e8e524412f6220ad31f2cc38448c6b1dac8b
phase_a_audit_commit: 4727c5efda6ae53194ff2c16dd224c67178e8d8d
phase_a_audit_tree: ac6206950b36f71663eddfb89b7e311aa85b53e6
phase_a_result: A0-A6_INDEPENDENTLY_REVIEWED_APPROVED / A7_DOCS_FORMALLY_PROMOTED
phase_a_status: A0-A6_APPROVED / A7_DOCS_FORMALLY_PROMOTED
scope: DOCS_ONLY_EXACTLY_THE_SIX_ALLOWLISTED_FILES
effect: ZERO_PRODUCT_STATE_CHANGE
verification: NOT_RUN_DOCS_ONLY
review: APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_ZERO_WRITE
formal_promotion: ORDINARY_FAST_FORWARD / FORMALLY_PROMOTED / commit=4727c5efda6ae53194ff2c16dd224c67178e8d8d / tree=ac6206950b36f71663eddfb89b7e311aa85b53e6 / ci_run=32615371879 / completed=success / headSha=4727c5efda6ae53194ff2c16dd224c67178e8d8d
task_artifacts_cleanup: ORIGINAL_PHASE_A_WORKTREE_LOCAL_AND_REMOTE_TASK_BRANCH_CLEANED
state_closeout: THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR
phase_b: NOT_AUTHORIZED / A7_HISTORICAL_SNAPSHOT
```

### Product target and lineage ruling

The non-negotiable target is: an ordinary user gives a natural-language business request to WorkBuddy; WorkBuddy is the only running Agent and user-facing conversation owner; after Registration and Locator have validated the Package, WorkBuddy reads the verified Package Guide, Manifest, Pipeline/Stage/Artifact/Checkpoint/Reviewer/Tool/Provider contracts, makes production decisions, calls the deterministic Shell transport when required, and presents the result. The Shell remains the six-module support layer and must not become a Director, FSM, Supervisor, Agent Host, workflow engine, Provider selector, renderer selector, or media control plane. “OpenMontage Agent” is only the logical production role assumed by WorkBuddy after the verified Guide is read.

The reviewed lineage is: the original V2 refactor handoff and its eight-stage/eleven-step delivery commitments -> the current six-module Shell boundary -> Stage 1 governance -> Stage 2 Registration/Locator -> Stage 3 bounded optional-capability preparation -> Stage 4 deterministic launcher contract -> Stage 5 WorkBuddy entry and final-package integration -> Stage 6 status/result relay. A stage name, task renumbering, branch, or chat transition cannot erase an original commitment. The break found by A1-A6 is the loss of final-package/Installer/real-WorkBuddy ownership between the mechanical Stage 4 contract and Stage 5 real integration.

| Stage | Historical contract/evidence field | Current architecture disposition | A7 decision |
|---|---|---|---|
| Stage 1 | accepted six-module/Agent-first governance | remains aligned with the target | `KEEP` |
| Stage 2 | Registration/Locator and temporary assembled-Package proof accepted | useful but narrower than a final distributable Package/production Registration | `KEEP_WITH_NARROWING` |
| Stage 3 | bounded optional Remotion/HyperFrames preparation accepted | optional capability preparation only; required toolchain and final Package remain outside it | `KEEP_WITH_NARROWING` |
| Stage 4 | mechanical launcher contract/tests/CI accepted | proves the frozen mechanical contract only, not a real product or WorkBuddy session | `HISTORICAL_PASS_ONLY` |
| Stage 5 | entry-code/static layer delivered; real integration incomplete | final assembly, Guide-read observation, real receipt and control-variable acceptance must be reworked | `REWORK` |
| Stage 6 | later relay boundary designed but not authorized | no direct receipt reuse or implementation is justified by current evidence | `INSUFFICIENT_EVIDENCE` |

The required requirement classifications are:

```text
unique_WorkBuddy_Agent_and_six_module_Shell: FULFILLED_AND_RETAIN
natural_language_only_user_entry: FULFILLED_BUT_NARROW / REAL_WORKBUDDY_NOT_PROVED
OpenMontage_Agent_first_Guide_owned_production_decisions: UNPROVED / REWORK_REQUIRED
Stage2_Registration_Locator: FULFILLED_BUT_NARROW
Stage3_optional_capability_boundary: FULFILLED_BUT_NARROW
final_private_toolchain_and_final_PackageRoot: DEFERRED_WITH_VALID_OWNER / UNPROVED
Stage4_mechanical_contract: FULFILLED_BUT_NARROW / HISTORICAL_PASS_ONLY
Stage5_real_WorkBuddy_and_business_result: PARTIAL / UNPROVED / REWORK_REQUIRED
Stage6_receipt_relay: DEFERRED_WITH_VALID_OWNER / INSUFFICIENT_EVIDENCE
R02_package_defect_attribution: MISASSIGNED_TO_WRONG_LAYER
old_Stage2_alignment_branch: SUPERSEDED_WITH_VALID_REASON / PRESERVE_HISTORY
old_R03_R05_execution_packets: SUPERSEDED_WITH_VALID_REASON / REPLACED_BY_B02_B03
```

### Binding, Guide-read, and evidence boundary

The unique binding delivery owner is `V2 Final-delivery Installer / Release Assembly Owner`. The binding carrier is an independent `Shell-adapter` subtree inside the final WorkBuddy `PackageRoot`; it is not a WorkBuddy-specific addition to the immutable Golden Key OpenMontage 0.3.25 subtree. The Shell owns the binding schema and consumer. The current 0.3.25 Package, its source, Release metadata, Lock, and Guide remain immutable in this task. A final assembly Manifest/Lock/hash must bind the two subtrees without changing the 0.3.25 bytes.

The real required order is:

```text
Registration identity validation
 -> Locator returns verified PackageRoot and Guide identity/hash
 -> WorkBuddy receives the verified identity
 -> WorkBuddy reads Guide, Manifest, Pipeline and Stage Skills
 -> WorkBuddy makes Pipeline/Stage/creative/review/Checkpoint/tool decisions
 -> one fixed internal CLI transport
 -> one deterministic fixed child/tool
 -> immutable LauncherReceipt facts
 -> WorkBuddy presents Artifact/result to the user
```

The Guide-read and decision steps must be observable in an independently reviewable WorkBuddy/client event or equivalent authoritative client evidence, with verified identity/hash. Model self-report, child self-report, ordinary logs, a generated receipt, or static/CI tests alone cannot prove that WorkBuddy actually read and followed the Guide. The child is not an Agent and must not decide production, start another Agent, choose a renderer/provider, or implement a second Director.

The final distributable Package must always include Node.js `22+` together with `npm`/`npx` (because the current HyperFrames requirement is Node 22+), as well as its other required private toolchain. Stage 3 must not detect, download, replace, or upgrade Node/npm/npx; it continues to own only bounded, user-authorized optional capability preparation.

### R02 and residual-object ruling

The live R02 field remains exactly `R02_CLOSED_BLOCKED_PACKAGE_RELEASE`. A7 adds, without changing that live status:

```text
r02_live_status: R02_CLOSED_BLOCKED_PACKAGE_RELEASE
recommended_reclassification: SHELL_INSTALLER_ADAPTER_BINDING_REQUIRED + REAL_FIXED_CHILD_UNVERIFIED
recommended_reclassification_state: NOT_YET_EFFECTIVE
binding_delivery_owner: V2 Final-delivery Installer / Release Assembly Owner
binding_carrier: FINAL_WORKBUDDY_PACKAGEROOT / INDEPENDENT_SHELL_ADAPTER_SUBTREE
shell_ownership: BINDING_SCHEMA_AND_CONSUMER
package_0_3_24: IMMUTABLE / NO_WORKBUDDY_ADAPTER_EMBEDDING
```

The published 0.3.24 candidate identity check remains a historical fact. The recommended reclassification corrects responsibility attribution; it does not turn R02 into a pass, create a fixed child, create a PackageRoot, or authorize a Package change.

The old Stage 2 branch `codex/v2-s2-official-package-alignment-b1` at `86a7902465d8e215e0830b9640e7222d7c7f5188` (commits `9b8ebb2`, `8d4461d`, `86a7902`) is classified as `SUPERSEDED_WITH_VALID_REASON / PRESERVE_HISTORY / DO_NOT_MERGE / DO_NOT_DELETE`. Its checkout-alignment direction treated an assembled Package as a Git checkout and is not a basis for the correction. Any useful narrow safety idea must be reimplemented under a separately authorized current contract. The two dirty detached worktrees at `C:\Users\blazi\.codex\worktrees\aef5\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2` and `C:\Users\blazi\.codex\worktrees\df76\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2`, both at `4d74d6576773dc9d383efec091bdc8d42f0d480c`, are non-authoritative and are not to be copied, committed, recovered, or deleted by A7.

### [HISTORICAL / SUPERSEDED_BY_2026-08-24_REBASELINE] Correction execution boundary

The A7 correction plan was strictly serial `B01 -> B02 -> B03 -> B04 -> B05 -> B06 -> B07`; its 21-field contracts are historical records only. They are retained for provenance and must not run. The current plan is C01-C07 in the rebaseline section below.

`B01` freezes the corrected binding and Guide-read contract; `B02` implements only the one Skill/fixed transport/child boundary; `B03` materializes the final PackageRoot and lifecycle through the named Installer owner; `B04` proves the real flow with the fixed official Package; `B05` repeats it with the same Shell and 0.3.25; `B06` closes Stage 5 only when final Package, production Registration/Activation, final Skill, real WorkBuddy receipt, independent review, Git and CI evidence all exist; `B07` is the external portrait/business acceptance gate. No B task is product authorization merely because this planning candidate was pushed.

## [HISTORICAL / SUPERSEDED_BY_2026-08-24_REBASELINE] Phase B execution mirror: B01 authorized (2026-08-23)

The A7 `phase_b: NOT_AUTHORIZED` field above and this B01 authorization are historical snapshots. They are superseded by the 2026-08-24 rebaseline section below and provide no current execution authority.

```text
phase_b_authorization: USER_AUTHORIZED_2026-08-23 / B01_ONLY
current_task: B01 / CURRENT_DOCS_ONLY_CONTRACT_FREEZE
b01_scope: FREEZE_BINDING_GUIDE_READ_CONTRACT + PACKAGE_INPUT_MIGRATION + AUTHORIZATION_MIRROR
b01_effect: ZERO_PRODUCT_STATE_CHANGE / DOCS_ONLY
b01_not_do: NO_PRODUCT_CODE_EXECUTION_OR_B02_B03_B04_B05_B06_B07_EXECUTION / NO_PACKAGE_OR_EXTERNAL_REPO_CHANGE / NO_CLIENT_SKILL_REGISTRATION_ACTIVATION_PROVIDER_MEDIA_DATAROOT
b01_tests: NOT_RUN_DOCS_ONLY
official_current_input: checkout=D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-main-cd9f3c1f / commit=cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / tree=6cd1961d552dd9d2bcfba990b80ac06edfe4b061 / state=DETACHED_CLEAN
golden_key_current_input: release=0.3.25 / checkout=D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673 / commit=73cab67322451601a824875c0e426067d736dd44 / tree=29231e0464fa4bc7533c1928415849e9b3a48e7c / parents=ef5f5b58fa1c2b494b0154989cf0e4e36615a701+cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / state=DETACHED_CLEAN
historical_only_inputs: official_old=4eab34c5cfcccaa4f1970554928feccce73ee930,95e1c3d0ab93482159818560f6a8c8e866b9139f / Golden_Key_0.3.24=ef5f5b58fa1c2b494b0154989cf0e4e36615a701 / provenance_only / NEVER_FUTURE_CALL_OR_VERIFY
b01_result: THIS_COMMIT
b01_review_gate: INDEPENDENT_ZERO_WRITE_APPROVE_REQUIRED / NO_RESULT_PREWRITTEN
b01_repository_delivery_resolution: INDEPENDENT_ZERO_WRITE_APPROVE + LIVE_FORMAL_REF_CONTAINS_THIS_COMMIT + EXACT_HEAD_CI_SUCCESS
next: B02_ONLY_IF_B01_DELIVERED
b02_b07: BLOCKED_BY_CHAIN
builder_boundary: NO_FORMAL_PROMOTION
```

## Phase B 纠偏方案重基线守卫（2026-08-24）

Owner 已暂停原 Phase B。最初 V2 目标和 official OpenMontage Agent-first 合同重新成为唯一裁决标准：普通用户只向 WorkBuddy 提自然语言业务需求；WorkBuddy 是唯一 Agent，读取 verified Guide、Manifest、Pipeline 和 Stage Skills，逐阶段作出生产决策并调用 OpenMontage tools；Shell 只绑定安装对象、运行时、确定性工具执行与结果传递，不替代 WorkBuddy 编排。

```text
rebaseline_task: V2-PROJECT-ARCHITECTURE-RECOVERY-PLAN-REBASELINE-AUDIT1
phase_b: PAUSED_BY_OWNER / NO_ACTIVE_PRODUCT_EXECUTION
phase_a_a0: KEEP_PROCEDURAL_TAKEOVER_FACTS / PER_TASK_REVIEW_EVIDENCE_NOT_PRESERVED
phase_a_a1: TARGET_RECONSTRUCTION_CORRECT / REQUIRED_TRACE_MATRIX_INCOMPLETE
phase_a_a2: STAGE1_STAGE2_DISPOSITION_MOSTLY_CORRECT / LEGACY_BRANCH_CAPABILITY_AUDIT_INCOMPLETE
phase_a_a3: STAGE3_BOUNDARY_MOSTLY_CORRECT / ORIGINAL_DIRTY_WORKTREE_AUDIT_INCOMPLETE / NOW_CLASSIFIED_SUPERSEDED_HISTORY
phase_a_a4: MECHANICAL_PASS_NARROWING_CORRECT / CORE_WHOLE_REQUEST_HYPOTHESIS_UNRESOLVED
phase_a_a5: REAL_INTEGRATION_GAP_AND_R02_ATTRIBUTION_CORRECT / INHERITED_UNRESOLVED_A4_HYPOTHESIS
phase_a_a6: EARLIEST_EXPLICIT_WRONG_PLAN_DECISION / SUPERSEDE_EXECUTION_PLAN
phase_a_a7: HISTORICAL_PROMOTION_VALID / PROMOTED_PLAN_CONTENT_SUPERSEDED
b01: HISTORICAL_DOCS_RESULT / CONTRACT_SUPERSEDED
b02: HISTORICAL_MECHANICAL_IMPLEMENTATION / NOT_PRODUCT_ACCEPTED / REWORK_OR_REPLACE
b03: KEEP_LIFECYCLE_AND_REPRODUCIBILITY_EVIDENCE_ONLY / FINAL_SKILL_AND_EXECUTION_BINDING_SUPERSEDED
b04: INCOMPLETE / NEGATIVE_EVIDENCE_RETAINED / NO_SHELL_SUCCESS
current_effect: DOCS_ONLY / ZERO_PRODUCT_PACKAGE_WORKBUDDY_CHANGE
next_active_task: NONE / OWNER_REAUTHORIZATION_REQUIRED
```

一个用户入口不等于一次固定 child 调用完成整个生产请求。允许 WorkBuddy 在同一已验证 Shell 会话内按 official Guide 多次调用确定性 OpenMontage tool；禁止把 `PackageToolDefinitionV1`、哈希、绝对路径、环境白名单或完整 JSON 交给模型拼装，也禁止模型写辅助脚本、阅读 Shell 源码或临场发现技术路由。WorkBuddy 宿主可增加其沙箱环境；Shell 只能从宿主环境构造受限 child environment，不能以“宿主环境必须完全等于 Shell 白名单”为前提。

原 `A0-A6_APPROVED` 只能保留为历史记录，不能再作为整体有效性结论。后续唯一计划是 `C01 -> C02 -> C03 -> C04 -> C05 -> C06 -> C07`：先证明 WorkBuddy 原生可用交互面，再冻结合同，然后才允许实现、装配、official 实机验收、0.3.25 同路径验收和最终业务/推广收口。每步完成后必须做目标回归审计和独立零写审查；任一步出现模型技术编排、第二控制面、直接 fallback 冒充 Shell 成功或证据不足，立即停止。

The A7 formal result remains limited to these six existing files and has no product code, test, CI, Package, external repository, client, Provider, media, Registration, Activation, or DataRoot effect. Do not run pytest as part of this docs-only state closeout; the explicit verification label is `NOT_RUN_DOCS_ONLY`. The audit result was independently reviewed and formally promoted by ordinary fast-forward at `4727c5efda6ae53194ff2c16dd224c67178e8d8d` with successful CI run `32615371879`; the original Phase A task worktree and local/remote task branches were cleaned. This closeout uses `THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR`; both the A7 `NOT_AUTHORIZED` value and the later B01-only authorization are historical. Current authority is `PAUSED_BY_OWNER / NO_ACTIVE_PRODUCT_EXECUTION` in the 2026-08-24 rebaseline section above.
