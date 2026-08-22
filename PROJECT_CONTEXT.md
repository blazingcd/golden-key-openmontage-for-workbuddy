# WorkBuddy Shell V2 Project Context

This repository is the WorkBuddy Shell V2 product, not an embedded OpenMontage production repository.

## Architecture

```text
User <-> WorkBuddy conversation
        |
        v
WorkBuddy Shell V2 six modules
        |
        v
verified Golden Key OpenMontage Package -> WorkBuddy assumes OpenMontage production role
```

Tencent WorkBuddy is the only running Agent. Shell V2 owns installation/lifecycle, Package Registration/Locator, runtime preparation, Launcher, WorkBuddy entry, and status/result relay. It verifies and binds Package/runtime identity but does not select or execute Pipeline, Stage, Provider, model, media, or creative work. "OpenMontage Agent" denotes the production role WorkBuddy assumes after reading the verified Package Guide, not a separately launched Agent process.

## Current implementation and evidence boundary

- `golden_key_openmontage_workbuddy/package_registration.py`: Stage 2 Package Registration and Locator implementation.
- `golden_key_openmontage_workbuddy/runtime_prepare.py`: accepted Stage 3 bounded optional-capability preparation.
- `golden_key_openmontage_workbuddy/session_launcher.py`: accepted Stage 4 fixed Package-tool Launcher.
- `tests/workbuddy/test_package_registration.py`, `tests/workbuddy/test_runtime_prepare.py`, and `tests/workbuddy/test_session_launcher.py`: direct contract evidence.
- `docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md`: accepted Stage 2 Registration/Locator contract and its non-Installer boundary.
- `golden_key_openmontage_workbuddy/workbuddy_entry_cli.py` and `workbuddy-skill/golden-key-openmontage/SKILL.md`: delivered Stage 5 entry-code transport assets; their existence is not real WorkBuddy acceptance.

Stage 2 has accepted the Registration/Locator implementation and one real temporary-Package validation containing the complete required private toolchain: a usable Python 3.10+ environment with locked core dependencies, FFmpeg/ffprobe, and Node/npm/npx at the highest current Package floor (currently Node 22+). The temporary Package was cleaned up. No retained final Release, installed production PackageRoot, or production Package Registration currently follows from that PASS; final Package materialization and production Registration remain a later final-delivery/Installer task due before Stage 5 production acceptance, not a Stage 3 or Stage 4 prerequisite.

Stage 3 planning and implementation are `PASS_ACCEPTED`. Its single public entry is `prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`, and its result set is exactly `DETECTION_REPORT / CONSENT_REQUIRED / INTEGRATED / SKIPPED / BLOCKED`. It performs bounded detection of optional Remotion and HyperFrames capabilities, returns a zero-download plan for missing or incompatible items, and integrates only a capability explicitly approved by the user. Stage 3 does not assemble the final Package, create production Registration, touch Python/FFmpeg/Node, select a renderer, scan drives, run video, or automatically replay a business request. Optional downloads use approved mainland-China mirrors with no automatic overseas fallback.

Stage 4 planning and implementation are also `PASS_ACCEPTED`. Its single public entry is `launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)`. The Launcher accepts only a release-specific immutable `PackageToolDefinitionV1` supplied by the approved Package definition/final-delivery Installer owner, spawns exactly one fixed Package tool, and returns a recursively immutable `LauncherReceiptV1` limited to nine outcomes. It remains Provider- and runtime-opaque; it does not select or configure Remotion, HyperFrames, or any Provider.

The current accepted repository tree tracks exactly 40 files. Stage 5 is `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`: the entry-code implementation and closeout are formally delivered, but final Package/PackageRoot/Registration/Activation, final installed Skill, and real WorkBuddy receipt evidence are not present. R00 is formally promoted and consumed. The original R01, Sandbox Refresh1, and Expert Entry Feasibility records remain `HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT`; their observed facts and old `BLOCKED_EXTERNAL_CONTRACT`/`INCOMPLETE` outcomes are preserved. R01 entry-surface acceptance is preserved, while R02 closed as `BLOCKED_PACKAGE_RELEASE` because the published candidate lacks a safe fixed tool and release-specific `PackageToolDefinitionV1`/Manifest/Lock binding. No next task is authorized; R03-R08 remain strict-order and blocked by chain. Stage 6 remains later and should first reuse `LauncherReceiptV1` directly when possible; whole-project business E2E is separate and is not Stage 7. WorkBuddy owns pause, consent, and continuation; Shell never auto-replays.

### [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / ORIGINAL R01 / FORMALLY CLOSED / PRESERVED] R01 controlled-client boundary

The product-goal recheck and scope-expansion audit both pass. WorkBuddy remains the only Agent/user entry, and the fixed CLI is allowed only as an internal bridge inside that sole Skill; no arbitrary CLI bypass or parallel control plane was introduced. WorkBuddy `5.3.14` started with exactly `agent-browser` and `find-skills`; the reviewed temporary probe ZIP was safety-scanned without skip, auto-installed as the exact `golden-key-openmontage-r01-controlled-probe`, and reached installed count `3`. A new isolated task used `Hy3` only. The client exposed only Bash/PowerShell shell execution, not an independent native bundled-script invocation/tool event, so execution was stopped before any shell/terminal run. No script, stdout/stderr, exit, cwd, or timeout evidence exists; the R01 result is therefore `BLOCKED_EXTERNAL_CONTRACT`. Independent review approved the docs closeout and formal fast-forward; the user uninstalled the temporary Skill, WorkBuddy showed `2` installed Skills, task history remained, both baseline Skills were untouched, and the exact D-drive probe folder/ZIP was deleted. No later R task may start.

### [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT] Current R01 Sandbox Refresh1 controlled-client boundary (accepted result mirror)

This is an independent refresh of the original R01. Official 134420 proves only that enterprise Skill scripts execute in the client sandbox. In the controlled WorkBuddy observation, PowerShell is recorded as an `ELIGIBLE_CANDIDATE_SURFACE`, not as an official exact execution contract. The remaining gaps are Skill-root cwd, bundled-relative resolution, and exact stdin/stdout/stderr/final-exit/timeout semantics. Reviewer-independent facts are limited to WorkBuddy `5.3.14`, `Hy3`, user cancellation, and no success/stdout/stderr/exit/cwd evidence; coordinator path/cwd reasoning is `COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER`.

```text
task_id: V2-S5-R01-WORKBUDDY-SANDBOX-REFRESH1 / ACCEPTED_BLOCKED_EXTERNAL_CONTRACT / NO_ACTIVE_TASK
accepted_result: 6c20371f1c72ee9d55147e1ad7feb8ede201858f / tree 9eb4643f09d03cc9f39b0b46906773e5bcc9125d / docs_review=APPROVE_P0_0_P1_0_P2_0
candidate_base: 932bcabc5baf90d0190101b1039e4ccf087b2b08 / tree 2ed2cd0e67dd8628b7f0b1acf84df0a7d8b0d0fd / tracked 40
product_goal_recheck: PASS / WorkBuddy sole Agent-user entry / fixed CLI only sole-Skill internal bridge / no second entry-control plane
official_134420: ENTERPRISE_SKILL_SCRIPTS_CLIENT_SANDBOX_ONLY
powershell_surface: ELIGIBLE_CANDIDATE_SURFACE / COORDINATOR_CLIENT_OBSERVATION / NOT_OFFICIAL_EXACT_CONTRACT
contract_gaps: SKILL_ROOT_CWD / BUNDLED_RELATIVE_RESOURCE_RESOLUTION / STDIN / STDOUT / STDERR / FINAL_EXIT / TIMEOUT
workbuddy: 5.3.14 / baseline=agent-browser,find-skills / HY3_ONLY / NEVER_AUTO
refresh1_artifacts: ISOLATED_D_DRIVE_TEMP_ROOT / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / CLEANUP_COMPLETE / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND / hashes=A369E89912B51C1627C972A7DE8F82111E55E2909622CB2E0E3276B45331FFF9,8A1D38A65945CC99C4B7F8EE95FDF4FF744D105303BC9904E5915E630DF58359,2284E6D6FE8FFD38689A357DD0A6653CEB23B923F0C531BF9EAC376178E9A28A
install_identity: WORKBUDDY_SKILL_GENERATED_IDENTITY / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / SKILL_MD_NO_METADATA_NAME / TRACEABILITY_DEFECT_ONLY
native_read: SKILL_MD_AND_BUNDLED_SCRIPT_READ / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / PHYSICAL_INSTALL_PATH_EXPOSURE_CONTRACT_DEVIATION
success_attempt: SESSION_WORKSPACE_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / FROZEN_RELATIVE_SCRIPT / NO_CD_NO_ABSOLUTE_PATH_NO_GUESSING_NO_COMMAND_MUTATION / SKILL_ROOT_CWD_NOT_EXPOSED / BUNDLE_RELATIVE_NOT_EXPOSED
execution: POWERSHELL_NOT_STARTED / USER_CANCELLED / NO_SCRIPT_EXECUTION / NO_SUCCESS_STDOUT_STDERR_FINAL_EXIT_CWD_TIMEOUT
reviewer_independent_observation: WORKBUDDY_5.3.14 / HY3 / USER_CANCELLED / NO_SUCCESS_STDOUT_STDERR_EXIT_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
result: BLOCKED_EXTERNAL_CONTRACT / SKILL_ROOT_AND_BUNDLED_RELATIVE_CONTRACT_MISSING / NOT_BECAUSE_POWERSHELL_IS_NON_NATIVE
review: APPROVE / P0=0 / P1=0 / P2=0
nonzero_timeout: NOT_RUN
r02_r08_status: NOT_STARTED / NOT_AUTHORIZED_BY_CHAIN
temporary_skill: UNINSTALLED / USER_UNINSTALLED_TEMPORARY_SKILL / TEMP_SKILL_ID=workbuddy-skill-1787379691395_NOT_IN_INSTALLED_LIST / WORKBUDDY_MY_INSTALLED_SKILLS_2=agent-browser,find-skills / TASK_HISTORY_RETAINED / BASELINE_SKILLS_UNTOUCHED / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND
computer_use: LOW_IMPACT_OPERATIONAL_ANOMALY / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / NO_PATH_INPUT_NO_FILE_SELECTION_NO_WRITE_DELETE / STOPPED_RECOVERED
next_authorized_task: NONE / R01_REMAINS_BLOCKED / ONLY_SEPARATE_R01_REOPEN_AUTHORIZATION_PLUS_ACCEPTED_SUCCESS_CONTRACT_EVIDENCE_CAN_UNLOCK_R02_R08
test_and_scope: NOT_RUN_DOCS_ONLY / product_code=0 / tests=0 / ci=0 / provider_media_package_stage4_stage6=0
```

## [HISTORICAL / CONSUMED_BY_V2-S5-R02] Current R01 acceptance-contract correction1

The historical R01, Sandbox Refresh1, and Expert Entry Feasibility records are preserved as `HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT`. Their old blocked/incomplete outcomes describe the evidence under the former execution-proof gate; this user-authorized correction changes the project acceptance ownership, not the underlying client facts or official documentation.

```text
r01_acceptance: ENTRY_SURFACE_ACCEPTED / EXECUTION_PROOF_DEFERRED_TO_R03_R07
r01_entry_surface: SKILL_PACKAGING / UPLOAD / INSTALL / IDENTITY_APPEARED / SELECTION_HIT / CLIENT_SANDBOX_SCRIPTS / POWERSHELL_ELIGIBLE_CANDIDATE_SURFACE
r01_execution_proof: NOT_CURRENTLY_PROVED / IMPLEMENTATION_AND_REAL_PROOF_DEFERRED_TO_R03_R07 / NO_SCRIPT_STDOUT_STDERR_EXIT_CWD_TIMEOUT_OR_RECEIPT_CLAIM
hy3: CURRENT_TEST_MODEL_ONLY / COST_AVOIDANCE / PRODUCT_MODEL_NEUTRAL / USER_SELECTED_MODEL / NOT_A_SKILL_OR_EXPERT_OR_SYSTEM_DEPENDENCY
boundaries: ONE_WORKBUDDY_SKILL_AND_ONE_USER_ENTRY / FIXED_CLI_INTERNAL_BRIDGE_ONLY / NO_ARBITRARY_CLI_PATH_GUESSING_SCAN_PATH_FALLBACK_MCP_SECOND_SKILL_SECOND_AGENT_ROUTER_RETRY_REPLAY
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
current_task: HISTORICAL / NONE / NO_ACTIVE_TASK / R01_CORRECTED_ACCEPTED_ENTRY_SURFACE
next_authorized_task: HISTORICAL / V2-S5-R02-PACKAGE-RELEASE-TOOL-DEFINITION-BINDING1 / R02_AUTHORIZED_ONLY / R03-R08_NOT_AUTHORIZED_BY_CHAIN
```

## Current R02 Package Release/Tool Definition Binding1 closeout (2026-08-22)

R02 is a docs-only closeout. The published candidate identity matches the approved source subtree, but the candidate is not bindable as a final Release: the remote recursive tree has `2614` entries with `truncated=false` and zero binding-related paths, the local immutable same-tree audit has `2155` blobs, and the release/lock metadata expose no safe fixed tool or release-specific `PackageToolDefinitionV1`/Manifest/Lock binding. No media tool was selected and no fixture or external Package was modified.

```text
task_id: V2-S5-R02-PACKAGE-RELEASE-TOOL-DEFINITION-BINDING1
published_candidate: blazingcd/golden-key-openmontage / codex/golden-key-openmontage-v0.3.24 / commit=ef5f5b58fa1c2b494b0154989cf0e4e36615a701 / tree=0464861c5985c7c9072e789b94889d29cf9a937a
release_metadata: version=0.3.24 / console_script_entrypoint=null / python_load_probe=lib.pipeline_loader:load_pipeline / authority_entry=README.md
lock_metadata: NO_PackageToolDefinitionV1 / NO_workbuddy_entry_cli / NO_package_tool_definition / NO_launcher / NO_fixed_tool / NO_CORRESPONDING_TOP_LEVEL_FIELDS
r02_result: BLOCKED_PACKAGE_RELEASE / PUBLISHED_CANDIDATE_IDENTITY_VERIFIED / MISSING_SAFE_FIXED_TOOL_AND_RELEASE_SPECIFIC_DEFINITION
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
current_task: NONE / NO_ACTIVE_TASK / R02_CLOSED_BLOCKED_PACKAGE_RELEASE
next_authorized_task: NONE / PACKAGE_OWNER_RELEASE_BINDING_REAUTHORIZATION_REQUIRED / R03-R08_NOT_AUTHORIZED_BY_CHAIN
unblock_condition: SEPARATE_PACKAGE_OWNER_APPROVAL_AND_INDEPENDENT_SAFE_FIXED_TOOL_DEFINITION_MANIFEST_LOCK_VERIFICATION / THEN_REAUTHORIZE_R02
product_goal_anti_expansion: PASS / WorkBuddy_ONLY_AGENT_USER_ENTRY / FIXED_CLI_ONLY_SOLE_SKILL_INTERNAL_BRIDGE / NO_ARBITRARY_TOOL_OR_FIXTURE_OR_DEFINITION_SELECTION / NO_CLIENT_PACKAGE_REGISTRATION_STAGE4_PROVIDER_MEDIA_STAGE6_OR_PRODUCTION
```

The previous Stage 3 execution packet, `prepare_runtime_on_demand(...)` and `prepare_optional_capability(...)` signatures, Shell-owned all-component Runtime Lock, Package-bound capability model, and pre-implementation Stage 4 gates are `SUPERSEDED`. They may remain only as explicitly historical evidence and do not override the accepted Stage 3/4 contracts above.

## Authority order

1. `docs/workbuddy/v2/TASK-REGISTER.md` — live state, exact objects, authorization, next task.
2. `docs/workbuddy/v2/PROJECT-CHARTER.md` — product roles and six-module responsibilities.
3. `docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md` — accepted Stage 2 complete-toolchain Registration/Locator contract and temporary-proof boundary.
4. `docs/workbuddy/v2/ACCEPTANCE-MATRIX.md` — evidence meanings and gates.
5. `docs/workbuddy/v2/DRIFT-GUARD.md` — stop rules and Git lifecycle.
6. `docs/workbuddy/v2/MODULE-DISPOSITION.md` — historical V1 capability disposition.

Git history preserves retired plans, prompts, reports, and evidence; they are not active authority.
