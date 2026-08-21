# WorkBuddy Shell V2 任务账本

状态：`STAGE_4_IMPLEMENTATION_PASS_ACCEPTED / FINAL_HANDOFF_HYGIENE_PASS_ACCEPTED / STAGE_5_PLANNING_BLOCKED_EXTERNAL_CONTRACT / NO_ACTIVE_TASK`

更新时间：2026-08-21

## Stage 4镜像自解析记录

```text
formal_ref: refs/heads/codex/workbuddy-shell-v2
formal_head_resolution: LIVE_REMOTE_REF_REQUIRED
formal_tree_resolution: LIVE_REMOTE_REF_TREE_REQUIRED
mirror_result: THIS_COMMIT
mirror_effect: ZERO_PRODUCT_STATE_CHANGE
mirror_repository_delivery_resolution: zero-write APPROVE exists AND LIVE_REMOTE_REF contains THIS_COMMIT
stage_4_planning: PASS_ACCEPTED
stage_4_implementation: PASS_ACCEPTED
stage_4_closeout_formal_result: b63d8c2bc2214bc39f18378dbe47057ef538301e
stage_4_closeout_formal_tree: 02814c6a4a483913e7b1abe3e9ee6d025236c951
stage_4_closeout_review: V2-S4-IMPLEMENTATION-CLOSEOUT-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_closeout_ci: run 32371507874 / Ubuntu 24.04 / Python 3.11.16 / completed / success / 357 passed / 1 skipped
stage_4_wsl_boundary: NO_RUNTIME_DEPENDENCY / temporary Linux-equivalence validation only / proof cleaned / WSL shut down after testing
final_handoff_hygiene_formal_result: 4636e27a62aad9f1b721e6c482e34b44d350503c
final_handoff_hygiene_formal_tree: fdf24f8450ac4bb48e5337cd7aa3477794796d19
final_handoff_hygiene_scope: EXACT_6_PATHS / tracked 37
final_handoff_hygiene_review: independent zero-write Reviewer / APPROVE / P0=0 / P1=0 / P2=0
final_handoff_hygiene_local_evidence: Python 3.14.7 / 11 hygiene passed / 358 combined passed / all final exit 0
final_handoff_hygiene_ci: run 32386393634 / completed / success / Python 3.14.7 / 357 passed / 1 skipped / actions v6 / no Node20 deprecation warning
stage_5_planning_authorization_candidate: V2-S5-PLANNING-AUTHORIZATION-BUILDER1 / DOCS_ONLY / FORMALLY_PROMOTED_AS_BASE_FOR_CURRENT_PLANNING
stage_5_planning_authorization_candidate_base: 67e39b345df954898a68c9c14645c9c04c380ac3 / tree c6bf74231434850fda07722ab9eed701797e48ff / tracked 37
stage_5_planning_authorization_candidate_branch: codex/v2-s5-planning-authorization1
stage_5_planning_authorization_candidate_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md
stage_5_planning_authorization_candidate_result: 042686039386a63866eba2f964f1fa9674bbec4b / ordinary fast-forward / origin/codex/workbuddy-shell-v2
stage_5_planning_authorized_next_task: V2-S5-PLAN-BUILDER1 / CURRENT_DOCS_ONLY_CANDIDATE
stage_5_planning_next_task_allowed_paths: docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md
stage_5_planning_next_task_kind: DOCS_ONLY / no production code / tests / CI / Package / real WorkBuddy / Launcher / Provider / media / WSL
stage_5_planning_t1_hard_stop: PLANNING_BLOCKED_EXTERNAL_CONTRACT when exact real WorkBuddy Skill/install/entry/call contract is not evidenced; never fabricate interface or use CLI/MCP/second-Skill fallback
stage_5_implementation_authorization: NOT_GRANTED
current_task: NONE
current_task_status: NO_ACTIVE_TASK
next_authorized_task: NONE / current planning candidate must be reviewed before any next task
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
final_package_gate_authorization: NOT_GRANTED
production_evidence_boundary: real WorkBuddy/Launcher session; Provider/media execution; Stage5; Stage6; final Package materialization and production registration remain unproven and NOT_GRANTED
```

该自解析记录不重新门禁Stage4 `PASS_ACCEPTED`，也不形成新的产品任务。六路径最终交接卫生结果`4636e27a62aad9f1b721e6c482e34b44d350503c`已经独立Reviewer最终`APPROVE / P0=0 / P1=0 / P2=0`、普通fast-forward和正式CI验证；该收口自身的历史状态是`current_task=NONE / current_task_status=NO_ACTIVE_TASK / next_authorized_task=NONE`。2026-08-21的Stage5规划授权候选及其生效条件见下节；任何Stage5实现、Stage6或最终Package权限仍不得从本收口推导。

## Stage 5 规划授权候选（2026-08-21）

本节只记录用户对 Stage 5 规划文档固化的授权，不授权 Stage 5 实现、真实 WorkBuddy 运行或任何 Package/Provider/媒体工作。候选完成后 `current_task` 必须回到 `NONE`；下一任务只有在本候选经独立零写 Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 且结果以普通 fast-forward 进入 `origin/codex/workbuddy-shell-v2` 后才生效。

```text
task_id: V2-S5-PLANNING-AUTHORIZATION-BUILDER1
task_kind: STAGE5_PLANNING_AUTHORIZATION / DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE
user_authorization: 2026-08-21 / 固化 Stage 5 T1-T12 规划执行边界并准备正式开启规划任务
start_commit: 67e39b345df954898a68c9c14645c9c04c380ac3
start_tree: c6bf74231434850fda07722ab9eed701797e48ff
tracked_files_at_start: 37
candidate_branch: codex/v2-s5-planning-authorization1
formal_target_branch: origin/codex/workbuddy-shell-v2
candidate_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md
candidate_production_code_changes: 0
candidate_test_changes: 0
candidate_ci_changes: 0
candidate_package_changes: 0
candidate_real_workbuddy_execution: NOT_PERMITTED
candidate_launcher_provider_media_wsl_execution: NOT_PERMITTED
next_task_id: V2-S5-PLAN-BUILDER1
next_task_base_rule: take over only from the exact latest live formal head/tree/tracked state at takeover; revalidate before editing
next_task_allowed_paths: docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md
next_task_scope: freeze the approved Stage 5 T1-T12 plan and acceptance boundaries in those three documents only
next_task_forbidden: production code; tests; CI/workflow; Package bytes or Registration; real WorkBuddy; Launcher; Provider; media; WSL; fourth planning file
stage_5_planning_status: AUTHORIZATION_PROMOTED / CURRENT_PLAN_CANDIDATE_UNDER_REVIEW
stage_5_implementation_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
final_package_gate_authorization: NOT_GRANTED
current_task_after_candidate: NONE
next_authorized_task_before_review: NONE
pending_next_authorized_task: NONE / current V2-S5-PLAN-BUILDER1 candidate must be independently reviewed
```

T1 的外部合同门禁是不可漂移的硬停止：如果官方资料或受控真实客户端证据仍不能证明真实 WorkBuddy Skill 的包结构、安装/导入归属、显式调用主体，以及不生成命令/argv/Shell 字符串即可调用 Stage 4 Python API 的精确协议，T1 必须记录为 `PLANNING_BLOCKED_EXTERNAL_CONTRACT`。不得伪造工具名、参数、Skill 结构或调用接口，不得用 CLI、MCP 或第二 Skill 作为兜底；此时规划停止在合同证据层，不进入实现授权。

该候选自身不得推广 formal、不得启动下一任务。候选最终报告必须给出 base commit/tree/tracked、candidate commit/tree、仅两条 diff path、docs-only 状态、`test=NOT_RUN_DOCS_ONLY` 与临时分支 push 状态；Reviewer 和推广由后续独立治理步骤处理。

## 已完成的Stage 4最终交接卫生收口

```text
task_id: V2-S4-FINAL-HANDOFF-HYGIENE-CLOSEOUT-BUILDER1
task_kind: FINAL_HANDOFF_HYGIENE_STATE_CLOSEOUT / DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE
start_commit: 4636e27a62aad9f1b721e6c482e34b44d350503c
start_tree: fdf24f8450ac4bb48e5337cd7aa3477794796d19
tracked_files_at_start: 37
result_commit: THIS_COMMIT
formal_target_branch: origin/codex/workbuddy-shell-v2
mirror_result: THIS_COMMIT
mirror_effect: ZERO_PRODUCT_STATE_CHANGE
mirror_repository_delivery_resolution: zero-write APPROVE exists AND LIVE_REMOTE_REF contains THIS_COMMIT
closeout_allowed_paths: docs/workbuddy/v2/TASK-REGISTER.md; PROJECT-STATE.md
closeout_production_code_changes: 0
closeout_test_changes: 0
closeout_ci_changes: 0
closeout_test_execution: NOT_RUN_DOCS_ONLY
closeout_wsl_execution: WSL_NOT_USED / ACTIVE_DISTRIBUTIONS_0

hygiene_builder_task: V2-S4-FINAL-HANDOFF-HYGIENE-BUILDER1
hygiene_builder_formal_result: 4636e27a62aad9f1b721e6c482e34b44d350503c
hygiene_builder_formal_tree: fdf24f8450ac4bb48e5337cd7aa3477794796d19
hygiene_builder_cumulative_scope: EXACT_6_PATHS / .github/workflows/ci.yml; docs/workbuddy/v2/README.md; docs/workbuddy/v2/MODULE-DISPOSITION.md; README.md; README_zh-CN.md; PROJECT_CONTEXT.md
hygiene_builder_tracked_files: 37
hygiene_builder_review: independent zero-write Reviewer / APPROVE / P0=0 / P1=0 / P2=0
hygiene_builder_local_evidence: task-private Python 3.14.7 / 11 hygiene passed / 358 combined passed / all final exit 0
hygiene_builder_formal_ci: run 32386393634 / completed / success / Python 3.14.7 / 357 passed / 1 skipped / actions/checkout@v6 / actions/setup-python@v6 / no Node20 deprecation warning

original_exact_three_path_attempt: V2-S4-FINAL-HANDOFF-HYGIENE-BUILDER1 / INCOMPLETE / STOPPED_SCOPE_EXPANSION / CLOSED_HISTORICAL
original_exact_three_path_root_cause: three additional current-entry documents were materially stale: README.md; README_zh-CN.md; PROJECT_CONTEXT.md
original_exact_three_path_effect: zero worktree / zero file changes / zero tests / zero commit or push / WSL not started

current_task: NONE
current_task_status: NO_ACTIVE_TASK
next_authorized_task: NONE
stage_3_status: PASS_ACCEPTED
stage_4_planning: PASS_ACCEPTED
stage_4_implementation: PASS_ACCEPTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
final_package_gate_authorization: NOT_GRANTED
```

该收口只把已经正式交付的卫生结果机械镜像到两份状态权威；它不授权Stage5/6、最终Package、真实WorkBuddy/Provider/媒体运行或任何产品变更。原三路径尝试的`INCOMPLETE`保留为已经由修订授权与最终六路径结果闭合的历史事实。

## 已完成的Stage 4实现权威同步（历史证据）

```text
task_id: V2-S4-IMPLEMENTATION-AUTHORITY-SYNC-FIX1
task_status: PASS_ACCEPTED / FORMALLY_PROMOTED
task_kind: STAGE4_IMPLEMENTATION_AUTHORITY_SYNC / DOCS_ONLY
user_authorization: 2026-08-20 / Stage4实施与审查执行授权已正式固化；在实现前一次性同步六权威，不扩大边界
start_commit: 2c3d87bedfa4a3cef3cfd952641199300f2715dc
start_tree: c196dbf6b094cad05076d01ac2496f7425cf6fac
result_commit: 3a64a0b4c103ea3cbe254fce60889396cd18ff30
branch: codex/v2-s4-impl-auth1
formal_target_branch: origin/codex/workbuddy-shell-v2
formal_target_at_start: 2c3d87bedfa4a3cef3cfd952641199300f2715dc
formal_tree_at_start: c196dbf6b094cad05076d01ac2496f7425cf6fac
review_range: 2c3d87bedfa4a3cef3cfd952641199300f2715dc..3a64a0b4c103ea3cbe254fce60889396cd18ff30
independent_review: V2-S4-IMPLEMENTATION-AUTHORITY-SYNC-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0 / ZERO_WRITE
formal_promotion: ORDINARY_FAST_FORWARD / origin/codex/workbuddy-shell-v2 included 3a64a0b4c103ea3cbe254fce60889396cd18ff30
repository_allowed_paths: AGENT_GUIDE.md; PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md; docs/workbuddy/v2/DRIFT-GUARD.md; docs/workbuddy/v2/PROJECT-CHARTER.md
production_code_changes: 0
test_changes: 0
ci_changes: 0
new_tracked_files: 0
tracked_files_expected: 35
stage_4_plan_formal_result: 5cb3f585a0cddffbd823c785b1d39ebd1834c1df
stage_4_plan_formal_tree: 144df76b3a307fa8944ccd7bd384bddb1b340516
stage_4_plan_promotion: ORDINARY_FAST_FORWARD / origin/codex/workbuddy-shell-v2=5cb3f585a0cddffbd823c785b1d39ebd1834c1df
stage_4_plan_reviewer: V2-S4-PLAN-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_plan_review_history_1: REQUEST_CHANGES / CLOSED / definition hash-cycle + receipt outcome/priority/invalid-input
stage_4_plan_review_history_2: REQUEST_CHANGES / CLOSED / forged-summary evidence + Stage3 managed/explicit/PATH handoff
stage_4_plan_ci: run 32337744225 / completed / success
embedded_plan_candidate_labels: HISTORICAL_CONDITIONAL_TEXT / review-and-promotion conditions satisfied by V2-S4-PLAN-REVIEW1 APPROVE and formal result 5cb3f585a0cddffbd823c785b1d39ebd1834c1df / not live authorization
stage_4_plan_closeout: PASS_ACCEPTED / dfd97f3d2e05a4c448448fc14514d1cfe76836e8 / tree 5eeb8a9337c5b38be60d3b0cef184b8898f2fedc
stage_4_plan_closeout_reviewer: V2-S4-PLAN-CLOSEOUT-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_plan_closeout_ci: run 32338998075 / completed / success / head_sha=dfd97f3d2e05a4c448448fc14514d1cfe76836e8
package_tool_definition_contract: FORMALLY_PROMOTED / PackageToolDefinitionV1
launcher_public_api_and_receipt_contract: FORMALLY_PROMOTED / launch_session_tool + nine-outcome recursively immutable LauncherReceiptV1
official_model_correction: dynamic capability/provider registry / Provider and local runtime are opaque to Shell / no hard-coded Provider or renderer routing in Stage4
stage_3_evidence_boundary: current implementation supplies local Remotion/HyperFrames evidence only; Stage4 accepts the complete approved definition plus the unmodified original Stage3 fact only when PackageToolDefinition declares a requirement, then independently applies the accepted managed/explicit/PATH source semantics and revalidates actual bytes
provider_boundary: image/video/TTS/music/stock/local-GPU and future Providers are optional external configuration selected by WorkBuddy/OpenMontage; Stage4 only passes allowlisted environment names and secret values to the fixed child process
stage_4_planning: PASS_ACCEPTED
stage_4_implementation_authorization_formal_result: 2c3d87bedfa4a3cef3cfd952641199300f2715dc
stage_4_implementation_authorization_formal_tree: c196dbf6b094cad05076d01ac2496f7425cf6fac
stage_4_implementation_authorization_review: V2-S4-IMPLEMENTATION-AUTHORIZATION-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_implementation_authorization_promotion: ORDINARY_FAST_FORWARD / origin/codex/workbuddy-shell-v2=2c3d87bedfa4a3cef3cfd952641199300f2715dc
stage_4_implementation_authorization_ci: run 32340096961 / completed / success / head_sha=2c3d87bedfa4a3cef3cfd952641199300f2715dc
stage_4_implementation_authorization: CONSUMED_COMPLETE
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
final_package_gate_authorization: NOT_GRANTED
next_authorized_task: V2-S4-IMPLEMENTATION-BUILDER1 / CONSUMED_COMPLETE

authority_sync_result: PASS_ACCEPTED / reviewer APPROVE and ordinary fast-forward conditions satisfied
effective_stage_4_implementation_authorization: CONSUMED_COMPLETE
effective_stage_4_launcher_authorization: NOT_GRANTED
effective_next_authorized_task: V2-S4-IMPLEMENTATION-BUILDER1 / CONSUMED_COMPLETE
effective_stage_5_workbuddy_entry_authorization: NOT_GRANTED
effective_stage_6_status_result_relay_authorization: NOT_GRANTED
effective_final_package_gate_authorization: NOT_GRANTED
implementation_builder_branch: codex/v2-s4-implementation-builder1
implementation_builder_base_rule: HISTORICAL_CONSUMED / implementation took over from the then-latest formal after this sync was approved and ordinary-fast-forwarded; the temporary sync branch was not used as implementation base
implementation_exact_allowed_paths: golden_key_openmontage_workbuddy/session_launcher.py; golden_key_openmontage_workbuddy/__init__.py; tests/workbuddy/test_session_launcher.py; tests/workbuddy/test_repository_hygiene.py; .github/workflows/ci.yml
implementation_tracked_files_transition: 35 -> 37
implementation_stop_scope_expansion: any sixth path; any edit to golden_key_openmontage_workbuddy/package_registration.py; golden_key_openmontage_workbuddy/runtime_prepare.py; pyproject.toml; any dynamic relaxation of the fixed tree contract
implementation_test_environment: implementation worktree private D-drive .venv only / no global Python packages
implementation_required_tests: Stage4 direct tests; repository hygiene; complete repository suite / every final exit 0 with untruncated output
implementation_delivery: one bounded Builder / non-force temporary-branch push / independent zero-write Reviewer / REQUEST_CHANGES only to original Builder / APPROVE P0=0 P1=0 P2=0 then ordinary fast-forward and formal CI
implementation_product_boundary: implements and tests only the approved Launcher contract / no real production Launcher execution / no WorkBuddy / no Provider or runtime choice / no media / no Stage5 or Stage6 / no final Package materialization
```

## 已完成的前置收口（历史证据）

```text
task_id: V2-CI-STAGE3-STATE-ASSERTION-CLOSEOUT-BUILDER1
task_status: WORKTREE_RESULT_READY_FOR_REVIEW
task_kind: CI_MAINTENANCE_STATE_CLOSEOUT / DOCS_ONLY
user_authorization: 2026-08-20 / 收口已进入正式分支的Stage3状态断言修复，并在独立审查与正式推广后衔接Stage4规划
start_commit: e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3
result_commit: THIS_COMMIT
branch: codex/v2-ci-stage3-state-assertion-closeout1
formal_target_branch: origin/codex/workbuddy-shell-v2
formal_target_at_start: e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3
formal_tree_at_start: a4d8034f6cf76c6eedd2f4bbe3c30dbe1b4e382a
review_range: e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3..THIS_COMMIT
independent_review: NOT_STARTED / REQUIRED_ZERO_WRITE
formal_promotion: NOT_STARTED / CLOSEOUT_EFFECTIVE_ONLY_AFTER_APPROVE_AND_ORDINARY_FAST_FORWARD
repository_allowed_paths: docs/workbuddy/v2/TASK-REGISTER.md; PROJECT-STATE.md; WORK-LOG.md
production_code_changes: 0
test_changes: 0
ci_changes: 0
new_tracked_files: 0
tracked_files_expected: 35
external_writes_performed: NON_FORCE_PUSH_OF_TEMPORARY_BRANCH_ONLY
task_temp_root_status: NOT_CREATED
ci_fix_authorization_commits: c258da0; ca27ae0
ci_fix_formal_result: e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3 / ALREADY_AT_FORMAL_HEAD
ci_fix_exact_implementation_allowlist: tests/workbuddy/test_repository_hygiene.py only
ci_fix_exact_change: exactly two Stage3 state assertions / stage3_implementation PASS_ACCEPTED / stage_3_implementation_authorization CONSUMED_COMPLETE
ci_fix_exact_diff: 1 changed path / 2 insertions / 2 deletions / no production or workflow change
ci_evidence_run: 32218904419 / codex/workbuddy-shell-v2 / head_sha=e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3
ci_evidence_result: completed / success / 198 passed / 1 skipped / final exit 0
ci_evidence_command: python -m pytest -p no:cacheprovider tests/workbuddy/test_package_registration.py tests/workbuddy/test_runtime_prepare.py tests/workbuddy/test_repository_hygiene.py -q
first_independent_review: INCOMPLETE / P0=0 / P1=0 / P2=0 / authority mismatch only / exact code diff had no finding
governance_deviation: formal branch advanced to e5ae6f8 before the live authority and state mirrors were closed out
governance_deviation_handling: retain Git and review history unchanged; close only the current authority mirrors; do not retroactively claim the first review was APPROVE
closeout_test_execution: NOT_RUN_DOCS_ONLY / official CI run 32218904419 is the retained execution evidence
stage_3_builder_base: 1c18edf9910e57541c37614c3e7cedf2fb11e372
stage_3_reviewed_implementation: a3f8959682d296301dc573c2835f8c705a52e8b2 / APPROVE / P0=0 / P1=0 / P2=0
stage_3_implementation_tree: eca057c3643c36248cccbfb9606d9aea12b3dc42
stage_3_implementation_commits: 300894359780684fed69a62f9b6c6b5902d51735; d77a69098e212ef2b5e0622ea589527798ec59d3; a3f8959682d296301dc573c2835f8c705a52e8b2
stage_3_closeout: 7c15aae4e77c579309312b21c79076f930970214 / FORMALLY_PROMOTED
stage_3_status: PASS_ACCEPTED
implementation_exact_changed_path_count: 5
implementation_exact_changed_paths: .github/workflows/ci.yml; golden_key_openmontage_workbuddy/__init__.py; golden_key_openmontage_workbuddy/runtime_prepare.py; tests/workbuddy/test_repository_hygiene.py; tests/workbuddy/test_runtime_prepare.py
stage_3_public_entry: prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)
stage_3_result_set: DETECTION_REPORT / CONSENT_REQUIRED / INTEGRATED / SKIPPED / BLOCKED
builder_direct_test_evidence: 55 passed / final exit 0 / no skip
builder_hygiene_test_evidence: 10 passed / final exit 0 / no skip
builder_ci_equivalent_evidence: 199 passed / final exit 0 / no skip
stage_3_reviewer_evidence: independent zero-write review of exact Git objects, code, test definitions and original Builder output / tests not rerun by Reviewer
evidence_boundary: no real third-party or mainland-mirror download; no production DataRoot integration; no WorkBuddy, Stage4, Provider, media or video E2E proof / these are not Stage3 failures or coding prerequisites
single_transaction: bounded detect Remotion and HyperFrames -> report PRESENT/MISSING/INCOMPATIBLE -> zero-download per-capability plan -> WorkBuddy asks -> approve integrates only named items / decline or defer returns SKIPPED -> verify and report
product_code_paths: golden_key_openmontage_workbuddy/runtime_prepare.py; export-only golden_key_openmontage_workbuddy/__init__.py; tests/workbuddy/test_runtime_prepare.py
acceptance_infrastructure_paths: tests/workbuddy/test_repository_hygiene.py; .github/workflows/ci.yml
accepted_builder_exact_path_count: 5 / 3 product paths + 2 acceptance-infrastructure edits
accepted_acceptance_infrastructure_reason: prior fixed-33 hygiene assertions forbade the two new tracked files and prior CI omitted the direct Stage3 test; the accepted implementation updated both atomically and the repository now tracks exactly 35 files
stage2_temporary_release_f00e83_status: STAGE2_TEMPORARY_PROOF_ONLY / MUST_NOT_PUBLISH_AS_FINAL / NOT_A_STAGE3_INPUT
optional_capability_catalog: remotion / hyperframes
capability_definition_rule: approved OpenMontage definitions provide source/version/size/hash/license/target facts; they are not Package Release declarations or capability Locks
bounded_detection_rule: managed DataRoot + explicitly registered/configured candidate paths + normal command resolution only / no drive or system-software enumeration
missing_or_declined_rule: MISSING or INCOMPATIBLE -> ask; decline/defer -> SKIPPED/NOT_INTEGRATED / not a Package or project blocker
consumer_interface_contract: CORRECTED_RESULT_TO_ACTION_MAPPING
consumer_mapping: DETECTION_REPORT=display_facts; CONSENT_REQUIRED=display_plan_and_ask; INTEGRATED=report_available; SKIPPED=continue_with_other_or_base_capabilities; BLOCKED=report_invalid_definition_or_failed_authorized_integration
consent_binding: capability + definition_sha256 + plan_sha256 / explicit per-capability approve only
real_workbuddy_evidence_stage: STAGE_5_ACCEPTANCE_ONLY
same_task_continuation_rule: verify in Stage5; if unsupported ask user to reply 继续刚才的任务; Shell never auto-replays
validation_diff_check: PASS / exact three-path allowlist / tracked 35 / untracked 0 / git diff --check exit 0 / state mirrors consistent
validation_full_test: NOT_RUN_DOCS_ONLY / official CI run 32218904419 already supplies the execution evidence
validation_scope: docs/workbuddy/v2/TASK-REGISTER.md; PROJECT-STATE.md; WORK-LOG.md / production=0 / tests=0 / CI=0 / new tracked=0 / tracked total=35
future_final_package_gate_rule: V2-FINAL-PACKAGE-MATERIALIZATION-AND-PRODUCTION-REGISTRATION-GATE1 is a later final-delivery or Installer task due before Stage5 real WorkBuddy production acceptance; it is not a Stage3 or Stage4 coding/planning prerequisite
future_cleanup_rule: always remove task-owned temp/staging on success or failure; never touch foreign objects; explicitly report any partial Release/PackageRoot/Registration state
historical_stage_4_takeover_boundary: PLANNING_ELIGIBLE / implementation_authorization=NOT_GRANTED
historical_stage_4_registration_audit: locate_active_package returns revalidated Registration, PackageRoot, required toolchain, Guide, Manifest and Lock identities; it does not return an authoritative fixed Package tool entry identity
historical_stage_4_contract_gap: exact public entry and immutable process receipt field names were not frozen; fixed Package tool identity source/path/hash/owner/fixed argv shape was not present in Registration output
historical_stage_4_gap_owner_package_tool_identity: approved OpenMontage Package definition plus later final-delivery or Installer owner / must provide a verifiable fixed tool identity without reopening Stage2 or making final Package a Stage4 planning prerequisite
historical_stage_4_gap_owner_launcher_api_and_receipt: separately authorized Stage4 planning task / freeze one public entry and exact immutable receipt fields before any implementation grant
historical_stage_5_deferred_scope: real new WorkBuddy session, single entry, unchanged literal user_message, per-capability authorization question and same-task continuation / implementation and acceptance only
historical_stage_6_deferred_rule: evaluate only after Stage4 receipt and Stage5 real consumer exist; direct consumption means STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE and production code 0
forbidden_scope: production code; docs other than this ledger; workflow; pyproject; Stage4/5/6 implementation; final Package; old main historical red runs; Node deprecation warning; any second implementation path
historical_next_authorized_task: V2-S4-PLAN-BUILDER1 / EFFECTIVE_ONLY_AFTER_THIS_CLOSEOUT_INDEPENDENT_REVIEW_APPROVE_AND_ORDINARY_FORMAL_FAST_FORWARD
historical_stage_4_planning: ELIGIBLE / START_NOT_PERMITTED_UNTIL_CURRENT_CLOSEOUT_APPROVE_AND_FORMAL_FAST_FORWARD
historical_stage_4_implementation_authorization: NOT_GRANTED
historical_stage_4_launcher_authorization: NOT_GRANTED
historical_stage_5_workbuddy_entry_authorization: NOT_GRANTED
historical_stage_6_status_result_relay_authorization: NOT_GRANTED
historical_final_package_gate_authorization: NOT_GRANTED
```

历史产品模型纠偏已撤销膨胀模型：真实Package、Registration和Package绑定能力元数据都不是Stage 3输入。Stage 3只对Remotion和HyperFrames做有界探测与事实报告，对缺失/不兼容项生成零下载计划，并在WorkBuddy取得用户逐能力明确同意后集成批准项；拒绝或暂缓返回`SKIPPED/NOT_INTEGRATED`。已接受实现严格落在三个产品路径加两个验收基础设施路径；该历史closeout没有新增生产代码、测试、CI、Package字节或外部写入。阶段2临时ZIP `f00e83d6154e7593b765a3d6c863b6653fc642818133acd7924f3fd91aab5d03`只保留历史证据边界，不是Stage 3输入。

## Stage 4执行任务包（已审并正式推广的规划合同）

### 产品目标与官方模型纠正

Stage 4只把一次WorkBuddy拥有的会话安全地交给一个经Release锁定的Package工具进程，并返回一次不可改写的真实进程回执。上游OpenMontage是instruction-driven、Agent-first且运行时查询动态capability/provider registry；生图、生视频、TTS、音乐、stock、local GPU及未来Provider都是可选外部配置，FFmpeg/Remotion/HyperFrames只是合成运行时类别，不是能力全集。上游没有可直接充当Golden Key固定Launcher身份的通用standalone入口，因此Stage 4不得从上游Guide、目录、registry或调用者命令猜工具入口。

Stage 4对Provider和Runtime保持opaque：不硬编码Provider、Remotion或HyperFrames，不配置、选择或执行registry routing。它只把`executor_controls.provider_environment`中已经由Stage 5/WorkBuddy解析的配置，按固定工具定义允许的环境变量名传给唯一子进程。Provider API key存在、缺失或错误永远不是Stage 3能力证据。当前Stage 3的Remotion/HyperFrames定义与原始回执只属于已实现的本地可选运行时证据来源；Stage 4公共接口只有在固定工具定义声明要求时才接受完整approved capability definition与未改写original Stage3 fact，并独立复核实际资产。

### V2-S4-T1：PackageToolDefinitionV1固定工具身份合同

权威来源冻结为：批准的Golden Key OpenMontage Package定义与最终交付/Installer owner为每个Package Release提供一个release-specific immutable `PackageToolDefinitionV1`实例。Stage 4只能消费该实例并与Locator事实交叉验证；调用者、未验证Guide、目录名、动态registry及系统PATH均无权生成或补全它。最终Package物化不是规划或编码前置，但真实启动前实例的每个release-specific字段都必须存在；缺实例或无法绑定时返回`PRELAUNCH_BLOCKED/TOOL_DEFINITION_UNBOUND`，spawn为0。

定义根对象必须是closed Mapping，字段、类型和规则精确如下：

```text
schema_version: Literal["golden-key-workbuddy-package-tool-definition-v1"]
definition_id: str                         # 1..128 NFC非空标识
definition_sha256: str                     # 64位小写hex；规范JSON排除本字段后计算
definition_relative_path: str              # 定义文件本身的规范Package内相对路径
authority_owner: str                       # 必须等于定义文件的精确Manifest owner
package_release: str                       # 必须等于Locator.openmontage_release
package_commit: str                        # 40位小写hex；等于Locator.openmontage_commit
tool_id: str                               # 1..128 NFC非空；Release内唯一
relative_path: str                         # 规范POSIX相对路径；Release实例必填
sha256: str                                # 工具文件64位小写hex；Release实例必填
size: int                                  # 工具文件正整数；Release实例必填
owner: str                                 # 精确Manifest owner；Release实例必填
execution_kind: Literal["PACKAGE_PYTHON_SCRIPT", "DIRECT_EXECUTABLE"]
interpreter_binding: Literal["LOCATOR_PACKAGE_PYTHON", "SELF"]
fixed_argv_template: tuple[str, ...]        # 每个token非空、无NUL；调用者不得追加
fixed_argv_placeholders: tuple[str, ...]    # 只能是()或("{verified_tool_path}",)
request_schema_sha256: Literal["c5b196bfe69c6a6db7073fb7fa7503a58837907e939fceeb5436fa7d19f80ce1"]
result_schema_sha256: Literal["8a96aceb463da2ea39549de44b06a765a3ac859260001ae277b99dbf2a8ca1b3"]
allowed_environment_names: tuple[str, ...] # ASCII env名，大小写折叠后唯一、规范排序
secret_environment_names: tuple[str, ...]  # allowed子集，规范排序
required_local_capabilities: tuple[Mapping, ...]
  each exact Mapping:
    evidence_schema_version: Literal["golden-key-workbuddy-local-capability-evidence-v1"]
    capability_id: str                     # opaque NFC非空，不设枚举
    definition_sha256: str                 # 64位小写hex
    compatibility_basis: Literal["EXACT_ASSET_IDENTITY"]
```

`PACKAGE_PYTHON_SCRIPT`必须使用`LOCATOR_PACKAGE_PYTHON`，且`fixed_argv_placeholders`精确为`("{verified_tool_path}",)`、模板中该占位符恰好一次；进程executable只能是Locator返回的私有Python。`DIRECT_EXECUTABLE`必须使用`SELF`且占位符闭集为空；进程executable只能是工具本身。所有业务数据均走stdin envelope，模板不得出现`user_message`、DataRoot、Provider值、shell元字符解释、会话命令或任意argv占位符。

两个schema hash的输入字节也已冻结，均为下列单行UTF-8、无BOM、无LF文本；不得由实现Builder重算另一种shape：

```text
request: {"fields":["schema_version","session_id","request_id","user_message","executor_controls","package","tool_definition_sha256","local_capability_evidence_identities"],"schema_version":"golden-key-workbuddy-package-tool-request-v1"}
result: {"fields":["schema_version","session_id","request_id","outcome","result_pointer","error"],"schema_version":"golden-key-workbuddy-package-tool-result-v1"}
```

规范JSON固定为UTF-8、NFC、`ensure_ascii=False/allow_nan=False/sort_keys=True/separators=(",", ":")`并以一个LF结尾；`definition_sha256`对同规则但排除自身字段的对象计算。定义字节只绑定稳定的Package release/commit、定义文件、工具、解释器、argv、环境名和本地能力要求；`registration_sha256/manifest_sha256/lock_sha256`绝不进入定义，避免定义文件被Manifest/Lock覆盖时形成hash环。

验证顺序固定为：先调用`locate_active_package(data_root)`并把当次Registration/Manifest/Lock身份保存在preflight事实与最终receipt，而不是写回定义；验证定义closed-schema与自hash；`package_release/package_commit`必须与Locator相同；`definition_relative_path`对应文件必须位于PackageRoot内、在当前Locator已验证的Manifest与Lock中各唯一覆盖、Manifest owner等于`authority_owner`，且其字节与传入Mapping的完整规范JSON字节完全相同；再从当前Manifest与Lock分别找到唯一工具条目并核对owner/hash/size；逐组件lstat并拒绝symlink/junction/reparse/ADS/保留名/别名/`..`；resolved路径必须在PackageRoot内且为regular file；核对工具hash/size；按execution kind核对解释器身份。spawn前再次调用Locator并逐字节复核Registration、Manifest、Lock、定义文件、工具、解释器及所有路径组件；任何替换或漂移均拒绝，spawn为0。不得修改Stage 2 Registration schema或实现。

### V2-S4-T2：唯一公共入口与输入合同

唯一公共入口冻结为：

```python
launch_session_tool(
    data_root: str | os.PathLike[str],
    user_message: str,
    executor_controls: Mapping[str, Any],
    package_tool_definition: Mapping[str, Any],
    local_capability_evidence: Sequence[Mapping[str, Any]] = (),
    cancel_event: threading.Event | None = None,
) -> Mapping[str, Any]
```

返回对象及所有后代Mapping/List必须递归冻结为`MappingProxyType`/tuple。`user_message`必须是原样UTF-8可编码、NFC、无surrogate的字符串；允许空白和业务文本，不解析、不规范化、不追加技术词。Launcher只记录UTF-8字节SHA-256和字节长度，不在receipt/log返回原文。

`executor_controls`为closed Mapping：

```text
schema_version: Literal["golden-key-workbuddy-launcher-executor-controls-v1"]
session_id: str                 # 1..128 ASCII [A-Za-z0-9._-]
request_id: str                 # 1..128 ASCII [A-Za-z0-9._-]
timeout_seconds: int            # 1..3600，bool拒绝
termination_grace_seconds: int  # 1..30，bool拒绝
result_root: str                # 已存在绝对非根目录，canonical且位于DataRoot内，无reparse
provider_environment: Mapping[str, str]
```

`provider_environment`的name必须为ASCII环境变量名、大小写折叠后唯一，并属于定义的`allowed_environment_names`；value必须是UTF-8可编码字符串。所有非空value无条件成为Provider-secret来源，不因name未列入`secret_environment_names`而降级；它们的唯一授权sink是固定child的环境。Receipt只记录经定义allowlist独立验证并规范排序的name。未提供Provider配置、Provider配置错误或Package动态registry未找到Provider，不触发Stage 3；若固定工具启动后因其业务配置退出，则保留真实非零退出。

定义中的allowed/secret环境名不得与`SystemRoot/WINDIR/COMSPEC/PATHEXT/TEMP/TMP/PATH/PYTHONNOUSERSITE/PYTHONUTF8/PYTHONUNBUFFERED`大小写折叠后相交。实现必须在函数入口保守提取raw `provider_environment`中所有可安全读取的非空字符串值及其完整UTF-8 bytes，先建立secret source set，再生成session/request/user-message hints、异常或日志；读取raw controls/value失败时不得回显对象，且对应未证实动态hints一律使用安全空值。Provider-secret来源不得经复制、切片、拼接、插值、编码、hash、长度或其他派生进入argv、canonical stdin、任何不可信动态receipt字段、log或exception；只有child环境可以持有原值。

non-disclosure按provenance而不是对最终receipt做无差别substring禁令：

1. 固定且不读取secret source构造的协议常量——`schema_version`、九值outcome、23个reason、receipt/result/request字段名、固定error origin和预冻结sanitized identifier text——即使与某个secret完整字节或子串偶然相同，也不构成Provider值回显/传播，不得因此改写闭集token或字段类型。
2. 独立authority偶然碰撞例外只覆盖receipt中能从已验证Package/PackageToolDefinition/Manifest+Lock/实际工具与解释器字节重建，且构造时不读取Provider value或caller fact的以下字段：`registration.registration_sha256`；`package.openmontage_release/openmontage_commit/package_root`；`manifest.sha256/size`；`lock.sha256/size/bundle_sha256`；`tool_definition.definition_id/definition_sha256/authority_owner`；`tool_file.tool_id/relative_path/path/sha256/size/owner`；`interpreter.binding/path/sha256/size`。环境变量name仅在能证明它来自raw Mapping key并被PackageToolDefinition allowlist独立验证、且从未读取value构造时可保留。固定argv只能从已验证PackageToolDefinition构造。上述字段闭集以外不存在概括的“本地能力身份”authority例外。
3. `original_stage3_fact`及caller提供或从其内容计算的全部字段都是动态域，包括`plan_sha256/original_stage3_fact_sha256/status/source/reused/runtime_root/verified_entrypoint/version_evidence`。receipt的每个`local_capability_evidence_identities` item同时混合独立资产事实与fact-derived字段，因此整个item视为动态对象，其任一子字段都不得套authority例外。session、request、user-message hints、result root/pointer、child error/message、stdout/stderr摘要及其他caller/child动态域同理。这些对象必须在进入canonical stdin或最终递归freeze前执行secret-source non-propagation检查；任一字段包含完整非空secret bytes或由secret-tainted值派生时，必须fail closed并清除该动态对象，不得让动态泄漏借“常量/authority例外”通过。

非cancel调用在session/request/user_message/result_root、`original_stage3_fact`、任一local capability identity item或其他待写stdin动态值中发现上述潜在传播时，固定为`PRELAUNCH_BLOCKED/INVALID_INPUT`、spawn 0。安全替换必须保持receipt全字段与原类型：schema允许nullable的str/int使用`None`，tuple字段使用空tuple而不是插入`None`；任一local capability identity item受污染时必须清空整个`local_capability_evidence_identities` tuple，不得保留混合item的部分字段。result pointer使用全`None`且`valid=false`，动态sanitized message使用预冻结secret-independent文本。若某个stdout/stderr流或由其解析出的动态字段受污染，该流的公开摘要固定为`size=0`、`sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`、`truncated=true`作为“已抑制”安全事实；不受污染的独立进程事实仍保留。最终freeze前必须再递归断言所有非固定、非字段级独立authority动态域对secret source零传播。

`local_capability_evidence`不是Stage 5重包装的摘要。每项必须原样携带完整批准定义和Stage 3原始事实，root为closed Mapping：

```text
schema_version: Literal["golden-key-workbuddy-local-capability-evidence-v1"]
approved_capability_definition: Mapping       # 原始完整批准定义，不删字段、不改字段
approved_capability_definition_sha256: str    # Stage3规范化定义内容的64位小写hex
original_stage3_fact: Mapping                 # 原始PRESENT capability fact或原始INTEGRATED item
original_stage3_fact_sha256: str              # 原始fact规范JSON的64位小写hex
```

`approved_capability_definition`必须按已接受Stage3 closed shape独立验证：根只含`capability/definition_sha256/version/verified_entrypoint/approved_mainland_sources/assets`及两个可选字段`explicit_registered_or_configured_candidate_paths/normal_command_name`；sources与assets子项字段也必须closed。Stage 4按Stage3已经冻结的规范化算法重算定义内容hash，要求同时等于定义内`definition_sha256`、input的`approved_capability_definition_sha256`及工具定义requirement的`definition_sha256`。`capability`值作为opaque字符串与requirement的`capability_id`相等，不在Stage4设置Remotion/HyperFrames枚举。

`original_stage3_fact`只允许两种未改写原始shape：`PRESENT`是Stage3 `capabilities`中的完整`capability/status/evidence`对象，source/runtime/entrypoint位于其`evidence`内；`INTEGRATED`是Stage3 `integrated`中的完整item，同一组evidence字段位于item根。Stage 4重算完整fact canonical hash，并核对其中capability、definition、status、runtime root、entrypoint和source与批准定义一致；fact里的`version_evidence/asset_evidence`只保留来源审计，绝不是信任依据。`INTEGRATED`必须`status=INTEGRATED/source=managed`，保留原始64位小写`plan_sha256`及`reused`字段，且`original_stage3_fact_sha256`必须覆盖这些未改写字段；非managed INTEGRATED或缺失/非法plan identity一律fail closed。

每个requirement的`compatibility_basis`固定为`EXACT_ASSET_IDENTITY`。Stage 4不得硬编码capability或Provider，但必须按原始fact的source精确镜像已接受Stage3来源语义并重新读实际文件：

1. `source=managed`：opaque capability必须是不设业务枚举的安全单路径段；`runtime_root`必须规范等于`<DataRoot>/Runtime/Composition/<opaque capability>/<definition_sha256>/`且是DataRoot内逐组件无symlink/junction/reparse的安全目录；entrypoint必须是定义内相对目标。实际文件集合、结构目录集合必须与定义全部assets及其父目录精确相等，全部asset逐项核对expected size/SHA-256；任何额外文件/目录也使closed-tree失败。
2. `source=explicit`：`runtime_root`必须是安全绝对目录，canonical identity必须精确等于完整批准定义的`explicit_registered_or_configured_candidate_paths`之一；entrypoint和定义全部assets按各自`managed_target`位于该root内，逐组件无reparse并逐项核对size/SHA-256。允许定义外的外来文件/目录存在，不做closed-tree；Stage 4只读，绝不删除、改写或清理它们。
3. `source=PATH`：完整批准定义必须声明非空`normal_command_name`；`runtime_root`与`verified_entrypoint`必须规范后完全相等，且是绝对、逐组件无reparse的regular command file。只用定义中`managed_target == verified_entrypoint`的唯一entrypoint asset核对该文件size/SHA-256；不要求目录、不核对其他assets、不做closed-tree，也不得重新查询宿主PATH或接收调用者命令。

上述source闭集只有`managed/explicit/PATH`；未知source、source与fact shape不符、路径/asset/entrypoint任一漂移均为`PRELAUNCH_BLOCKED/LOCAL_CAPABILITY_EVIDENCE_MISMATCH`，spawn为0。只有定义绑定且满足对应source profile的精确asset identity能够证明本次version相容性时才接受；Launcher不执行第二探针，也不信任调用者或fact中的version输出。若该source profile仍不足以唯一证明相容性，同样fail closed。

Launcher只按`required_local_capabilities`逐项消费上述完整对象；定义要求为空时，任何额外local evidence都返回`PRELAUNCH_BLOCKED/INVALID_INPUT`以避免隐式路由。Stage 5只能原样传递approved definition和original Stage3 fact，不得生成替代摘要或信任hash。Provider环境绝不映射成能力证据；未来扩展Stage3能力目录需另行授权，不能借Stage4通用字段扩大当前Stage3实现。

stdin只发送一个UTF-8规范JSON对象并立即关闭，closed shape为：

```text
schema_version: Literal["golden-key-workbuddy-package-tool-request-v1"]
session_id: str
request_id: str
user_message: str                         # 与入参逐字节相同
executor_controls:
  timeout_seconds: int
  result_root: str
  provider_environment_names: tuple[str, ...]
package:
  registration_sha256: str
  openmontage_release: str
  openmontage_commit: str
tool_definition_sha256: str
local_capability_evidence_identities: tuple[Mapping, ...]
  each: capability_id + definition_sha256 + approved_capability_definition_sha256 + original_stage3_fact_sha256 + status + source + plan_sha256 + entrypoint_sha256 + entrypoint_size
```

Provider secret值只进入子进程环境，不进入canonical stdin；`provider_environment_names`仅因其逐项来自已验证definition allowlist而可保留，绝不能从value生成。

### V2-S4-T3：单进程生命周期

1. 完成全部preflight后构造executable与不可追加的固定argv；`shell=False`，不调用`cmd.exe /c`、PowerShell、PATH工具发现或用户命令。
2. `cwd`精确为已重验PackageRoot。环境不继承整份宿主环境：Windows只复制启动所需`SystemRoot/WINDIR/COMSPEC/PATHEXT/TEMP/TMP`的安全值，PATH由Package内Python/FFmpeg/Node固定目录构造，并设置`PYTHONNOUSERSITE=1/PYTHONUTF8=1/PYTHONUNBUFFERED=1`；之后只注入定义allowlist内的Provider环境。保留名不得被Provider覆盖。
3. 为唯一子进程建立可终止的独立进程组/Windows Job Object；恰好一次spawn，`spawn_count`只可0或1，`retry_count`恒为0。
4. stdin只写上述单一envelope。stdout/stderr是不可信child输出，分别流式计数和SHA-256，内存保留上限各1 MiB；对每个非空secret的完整UTF-8 bytes做跨chunk匹配，匹配器必须保留足以发现边界命中的overlap。任一流任一位置命中都精确裁决`SECRET_DISCLOSURE_DETECTED`，固定协议常量偶然碰撞例外绝不适用于child输出。receipt不返回原文；受污染流只返回上述安全抑制摘要。仅stdout前64 KiB可用于解析单个结果envelope，超限或额外非空字节视为无效；即使raw bytes因JSON escape未直接命中，解析后的result pointer/error等动态字段重建出secret也必须同样阻断。
5. 正常退出保留真实exit code。timeout或`cancel_event.is_set()`后终止整个自有进程树，等待`termination_grace_seconds`，随后检测残留；不重试、不重放user message。
6. timeout、取消、进程退出、输出读取、结果校验或终止证据不完整时不得伪造成功；任务自有临时缓冲必须清理，不删除Package、result或外来对象。

固定工具stdout成功协议为单个UTF-8规范JSON对象：

```text
schema_version: Literal["golden-key-workbuddy-package-tool-result-v1"]
session_id: str                 # 与请求相同
request_id: str                 # 与请求相同
outcome: Literal["SUCCEEDED", "FAILED"]
result_pointer: null | Mapping
  exact Mapping: relative_path: str; sha256: str; size: int
error: null | Mapping
  exact Mapping: code: str; origin: str; message: str
```

`SUCCEEDED`要求exit 0、`error=null`和非空result pointer；`FAILED`要求exit 0、`result_pointer=null`和非空error，并映射为Launcher outcome/reason均为`CHILD_REPORTED_FAILURE`。pointer相对路径必须规范、安全，解析后位于`executor_controls.result_root`内，逐组件无reparse，目标为regular file且hash/size匹配。非零退出事实优先保留，不因stdout内容改写为成功或child-reported failure。

### V2-S4-T4：不可改写LauncherReceiptV1

公共函数对输入错误、preflight错误、spawn错误和运行结果一律返回receipt，不向调用者泄漏合同异常。结果闭集精确为`PRELAUNCH_BLOCKED`、`SPAWN_FAILED`、`EXITED_SUCCESS`、`EXITED_NONZERO`、`CHILD_REPORTED_FAILURE`、`TIMED_OUT`、`CANCELLED`、`INCOMPLETE`、`RESIDUAL_PROCESS`九值。若终止后仍有自有进程残留，最终outcome必须为`RESIDUAL_PROCESS`并保留timeout/cancel事实；exit 0但结果envelope或pointer无效为`INCOMPLETE`；exit 0且child明确返回`FAILED`为`CHILD_REPORTED_FAILURE`；只有exit 0、child `SUCCEEDED`、无泄密、无残留且有效pointer才可`EXITED_SUCCESS`。

Receipt为closed、递归冻结Mapping，根字段和嵌套类型精确如下：

```text
schema_version: Literal["golden-key-workbuddy-launcher-receipt-v1"]
outcome: 上述9值之一
reason_code: Literal[
  "NONE", "INVALID_INPUT", "CANCELLED_BEFORE_SPAWN", "LOCATOR_FAILED", "REGISTRATION_DRIFT",
  "TOOL_DEFINITION_INVALID", "TOOL_DEFINITION_UNBOUND", "TOOL_PATH_VIOLATION",
  "TOOL_IDENTITY_MISMATCH", "INTERPRETER_IDENTITY_MISMATCH",
  "LOCAL_CAPABILITY_EVIDENCE_REQUIRED", "LOCAL_CAPABILITY_EVIDENCE_MISMATCH",
  "ENVIRONMENT_NOT_ALLOWED", "SPAWN_OS_ERROR", "EXITED_NONZERO", "TIMEOUT",
  "CANCELLED", "CHILD_REPORTED_FAILURE", "OUTPUT_INVALID", "RESULT_POINTER_INVALID",
  "SECRET_DISCLOSURE_DETECTED", "EVIDENCE_INCOMPLETE", "RESIDUAL_PROCESS_DETECTED"]
session: {session_id: str | None}
request: {request_id: str | None}
registration: {registration_sha256: str | None}
package: {openmontage_release: str | None; openmontage_commit: str | None; package_root: str | None}
manifest: {sha256: str | None; size: int | None}
lock: {sha256: str | None; size: int | None; bundle_sha256: str | None}
tool_definition: {definition_id: str | None; definition_sha256: str | None; authority_owner: str | None}
tool_file: {tool_id: str | None; relative_path: str | None; path: str | None; sha256: str | None; size: int | None; owner: str | None}
interpreter: {binding: str | None; path: str | None; sha256: str | None; size: int | None}
user_message: {sha256: str | None; byte_length: int | None}
provider_environment_names: tuple[str, ...]
local_capability_evidence_identities: tuple[Mapping, ...]
  each: {capability_id: str; definition_sha256: str; approved_capability_definition_sha256: str; original_stage3_fact_sha256: str; status: Literal["PRESENT", "INTEGRATED"]; source: Literal["managed", "explicit", "PATH"]; plan_sha256: str | None; entrypoint_sha256: str; entrypoint_size: int} # PRESENT plan=None；INTEGRATED plan=原始64hex
launched: bool
spawn_count: int                 # 0|1
pid: int | None
started_at_utc: str | None       # RFC3339 UTC
ended_at_utc: str                # RFC3339 UTC
duration_ms: int                 # >=0
exit_code: int | None
timed_out: bool
cancelled: bool
retry_count: Literal[0]
stdout: {size: int; sha256: str; truncated: bool}
stderr: {size: int; sha256: str; truncated: bool}
result_pointer: {path: str | None; sha256: str | None; size: int | None; valid: bool}
error: null | {code: str; origin: Literal["PREFLIGHT", "SPAWN", "CHILD", "TIMEOUT", "CANCEL", "OUTPUT", "RESULT", "RESIDUAL"]; sanitized_message: str}
residual_process: {detected: bool; termination_attempted: bool; termination_succeeded: bool | None; observed_pids: tuple[int, ...]}
```

所有字段始终存在。`PRELAUNCH_BLOCKED/INVALID_INPUT`以及无法安全解析对应输入时，`session.session_id`、`request.request_id`、`user_message.sha256/byte_length`允许为`None`；已成功验证且可证明不来自secret source的动态字段填真实值，未到达或受污染字段按上述类型安全值替换，不得删除字段或改变tuple元素类型。固定协议常量与独立权威身份的偶然字节相同不算泄漏；Provider value从来源传播到任何不可信动态receipt字段、异常文本、日志或回传原文的次数必须为0。若child stdout/stderr完整secret bytes跨chunk命中，或解析动态字段重建出secret，丢弃原文并安全替换受污染动态域，outcome=`INCOMPLETE`、reason=`SECRET_DISCLOSURE_DETECTED`。

本节的“独立权威身份”精确限于T2列名的字段级闭集，不适用于任何local capability identity item；后者只要任一字段受污染，必须把整个`local_capability_evidence_identities`替换为空tuple。

结果裁决优先级精确如下，命中后不得被较低项覆盖；真实`exit_code/timed_out/cancelled/residual_process`字段始终保留：

| 优先级 | 条件 | outcome / reason | spawn_count |
|---|---|---|---|
| 1 | `cancel_event`类型无效，或其他输入无法安全读取且无法先确认有效取消对象 | `PRELAUNCH_BLOCKED / INVALID_INPUT` | 0 |
| 2 | 有效`cancel_event`在函数入口已经set；先于Locator和其他preflight裁决 | `CANCELLED / CANCELLED_BEFORE_SPAWN` | 0 |
| 3 | 输入/Locator/定义/路径/环境/本地证据任一preflight失败 | `PRELAUNCH_BLOCKED /`对应精确reason | 0 |
| 4 | OS创建唯一进程失败 | `SPAWN_FAILED / SPAWN_OS_ERROR` | 0 |
| 5 | spawn后终止宽限结束仍检测到自有残留进程 | `RESIDUAL_PROCESS / RESIDUAL_PROCESS_DETECTED` | 1 |
| 6 | 任一非空Provider secret完整UTF-8 bytes出现在不可信child stdout/stderr（含跨chunk），或解析动态字段重建出secret；无固定常量例外 | `INCOMPLETE / SECRET_DISCLOSURE_DETECTED` | 1 |
| 7 | timeout与cancel中先发生/先被monotonic观察者记录者；同一tick同时观察时cancel优先 | `TIMED_OUT / TIMEOUT`或`CANCELLED / CANCELLED` | 1 |
| 8 | child真实exit code非0 | `EXITED_NONZERO / EXITED_NONZERO` | 1 |
| 9 | 输出捕获、JSON envelope、session/request或result pointer无效/证据不完整 | `INCOMPLETE / OUTPUT_INVALID|RESULT_POINTER_INVALID|EVIDENCE_INCOMPLETE` | 1 |
| 10 | exit 0且有效result envelope明确`outcome=FAILED` | `CHILD_REPORTED_FAILURE / CHILD_REPORTED_FAILURE` | 1 |
| 11 | exit 0且有效`SUCCEEDED` envelope、有效pointer、无泄密和残留 | `EXITED_SUCCESS / NONE` | 1 |

preflight reason不得合并或留给Builder选择：closed input/type/range/未知字段错误，或Provider-secret潜在传播进入非cancel动态input/canonical stdin=`INVALID_INPUT`；Locator无活动Registration或首次读取失败=`LOCATOR_FAILED`；首次快照后Registration/Manifest/Lock身份变化=`REGISTRATION_DRIFT`；release-specific定义实例缺失、定义文件不在当前Manifest+Lock中各唯一覆盖、传入定义字节不等于Package文件、authority owner不绑定或release/commit不属于当前Locator=`TOOL_DEFINITION_UNBOUND`；定义closed shape/self-hash/execution kind/interpreter binding/argv/schema hash/env/local requirement非法=`TOOL_DEFINITION_INVALID`；工具路径逃逸或组件不安全=`TOOL_PATH_VIOLATION`；工具Manifest/Lock覆盖、hash/size/owner不匹配=`TOOL_IDENTITY_MISMATCH`；解释器路径或身份不匹配=`INTERPRETER_IDENTITY_MISMATCH`；声明能力但缺项=`LOCAL_CAPABILITY_EVIDENCE_REQUIRED`；能力完整定义、原始fact、实际asset或closed-tree任一不匹配=`LOCAL_CAPABILITY_EVIDENCE_MISMATCH`；环境名越权=`ENVIRONMENT_NOT_ALLOWED`；其余无法完成的preflight事实=`EVIDENCE_INCOMPLETE`。

非成功receipt的`error`必须非空且与最终reason同源：全部preflight=`PREFLIGHT`，spawn失败=`SPAWN`，残留=`RESIDUAL`，泄密/输出无效=`OUTPUT`，timeout=`TIMEOUT`，取消=`CANCEL`，非零和child FAILED=`CHILD`，pointer无效=`RESULT`；只有`EXITED_SUCCESS/NONE`的`error=null`。spawn=0时`launched=false/pid=None/started_at_utc=None/exit_code=None/timed_out=false/retry_count=0`，stdout/stderr固定为空字节的size/SHA-256/truncated事实，result pointer全`None`且`valid=false`，residual固定未检测/未终止/空PID；provider名称和local evidence identities只保留已完整验证项，否则为空tuple。

函数入口cancel不启动Locator、不访问Package、不spawn，但必须先从raw controls保守提取可安全读取的Provider secret source，再决定哪些session/request/message hints可公开；任何hint包含完整secret bytes、由secret派生或来源无法安全判断时，对应nullable字段为`None`，未验证的provider name tuple为空。即使secret value恰好等于session/request，最终仍必须是`CANCELLED/CANCELLED_BEFORE_SPAWN`、Locator 0、spawn 0，只是相关hints安全清空；固定schema/outcome/reason常量保持不变。spawn后timeout/cancel的“先发生”使用首次记录的`time.monotonic_ns()`；不得由线程调度顺序或Builder自行选择。任何未分类内部错误：spawn前映射`PRELAUNCH_BLOCKED/EVIDENCE_INCOMPLETE`，spawn后映射`INCOMPLETE/EVIDENCE_INCOMPLETE`。

### V2-S4-T5：直接与负面测试矩阵

未来直接测试必须至少覆盖原21项，并增加动态registry/Provider、定义可实例化和结果裁决边界：

1. 无活动Registration；2. Registration损坏/漂移；3. PackageRoot或任一必带工具链漂移；4. 定义缺字段/未知字段/自hash错误；5. 工具未被Manifest或Lock唯一覆盖；6. 工具hash/size/owner不匹配；7. 路径逃逸/ADS/别名；8. 任一路径组件symlink/junction/reparse；9. 任意命令/额外argv/placeholder注入；10. user_message字节被改写；11. controls拼入user_message；12. 定义要求的本地证据缺失；13. capability/definition/entrypoint身份不匹配；14. 定义不要求本地能力时不得要求Remotion/HyperFrames；15. 真实非零退出保真；16. timeout；17. result envelope/pointer缺失、越界、漂移或hash/size错误；18. stdout/stderr含secret时原文回传与日志为0；19. 残留子进程；20. spawn<=1且retry=0；21. 第二Agent/调度/服务/数据库/媒体/Artifact/Checkpoint代码为0；22. Provider和capability名无硬编码枚举；23. 未allowlist的任意env名拒绝且spawn=0；24. secret值不进入argv/stdin/receipt/hash前日志/异常；25. Provider配置缺失不会被映射为Stage3证据缺失；26. 只有定义明确声明的本地能力才校验证据；27. spawn前Registration/tool/interpreter替换漂移；28. cancel前/后及终止宽限；29. 输出截断仍保留真实size/hash且不产生成功；30. 所有返回Mapping递归不可修改；31. invalid input也总是返回全字段receipt，无法安全读取的session/request/message字段为`None`；32. 入口已取消为`CANCELLED/CANCELLED_BEFORE_SPAWN`、Locator访问0、spawn=0；33. OS spawn失败为`SPAWN_FAILED/SPAWN_OS_ERROR`、spawn_count=0；34. residual、secret、timeout/cancel先发生、nonzero、invalid output、child FAILED和success严格按优先级裁决；35. exit 0且child `FAILED`精确映射`CHILD_REPORTED_FAILURE/CHILD_REPORTED_FAILURE`；36. 定义closed字段不含Registration/Manifest/Lock hash，避免hash环；37. 使用真实Stage2 fixture组装含定义文件和工具文件的Package，完成`register -> locate -> Stage4 definition/tool validate`往返；38. Stage5摘要envelope或只给摘要hash必须拒绝，输入必须含完整批准定义和未改写Stage3原始fact；39. Stage4独立重验runtime root、entrypoint与source-specific asset identity，fact证据不得替代字节验证；40. caller/fact的version_evidence不受信，精确asset identity不足以证明相容性时fail closed；41. `managed/explicit/PATH`三种合法`PRESENT`原始交接分别成功且receipt保留source；42. managed root存在任一额外文件或目录时拒绝；43. explicit定义资产漂移时拒绝，但定义外额外文件/目录始终保留且零写入；44. PATH命令文件被替换、非绝对、非regular或任一组件不安全时拒绝；45. `INTEGRATED`使用explicit/PATH或缺失plan identity时拒绝；46. 合法managed `INTEGRATED`的receipt保留原始`plan_sha256`，`original_stage3_fact_sha256`绑定未改写`reused`；47. 未知source拒绝且spawn=0；48. secret为`-`或`I`并只与固定schema/outcome/reason/field name偶然碰撞时仍返回全字段、类型合法receipt；49. pre-cancel时secret完整值等于session/request，仍为`CANCELLED/CANCELLED_BEFORE_SPAWN`、Locator 0、spawn 0且相关hints为`None`；50. secret被复制/派生到user_message/session/request/result_root或其他canonical-stdin动态域时preflight阻断且安全替换；51. child stdout与stderr分别在单chunk和跨chunk出现完整secret bytes时均为`SECRET_DISCLOSURE_DETECTED`且受污染流只返回安全抑制摘要；52. child JSON escape后解析出的result pointer/error重建secret时同样阻断，动态pointer/message不传播；53. 经definition allowlist验证的env name或独立Package/definition identity与secret偶然相同不误报，并证明无value数据流；54. 动态域清除使用`None`/空tuple/固定文本且不向`tuple[str]`插入`None`、不删除receipt字段、不改变九值/23 reason/字段类型；55. argv、canonical stdin、最终动态receipt、log和exception对Provider-secret来源复制/派生均为0，最终递归non-propagation断言命中时fail closed。

成功测试至少覆盖`PACKAGE_PYTHON_SCRIPT`与`DIRECT_EXECUTABLE`各一次、空Provider环境、allowlisted动态Provider环境、required_local_capabilities为空和非空、exit 0有效pointer、Stage 6直接消费同一receipt shape。真实Stage2 fixture往返必须在临时DataRoot内创建由Manifest/Lock覆盖的定义文件与固定工具，调用现有registration API登记、激活并由Locator读取，再由Stage4完成定义/工具验证；它证明合同可实例化，但不要求最终交付Package成为实现前置。测试只用任务fixture进程，不运行真实WorkBuddy、Provider、媒体生产或未验证Package Guide。

第24项“secret值不进入”精确指Provider-secret source不得被Launcher复制/派生，不是禁止secret-independent固定常量或独立权威身份偶然字节相同。第29项“输出截断保留真实size/hash”只适用于未受secret污染的流；命中secret的流必须使用T2/T4冻结的安全抑制摘要，不能为保留真实digest而派生或传播secret。上述clarification的implementation-authority条件已经由`V2-S4-SECRET-NONDISCLOSURE-CONTRACT-CLARIFICATION-REVIEW1`独立`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward满足；原Implementation Builder随后完成修订，独立Reviewer复审`APPROVE / P0=0 / P1=0 / P2=0`，实现结果`fa9adb8470ab94b88ec9900ede03cb26f7de0ebd`也已普通fast-forward，因此该条件已消费完成。

第53项的“独立Package/definition identity”只指T2精确列名的字段级闭集，不包括任何local capability identity item。第55项必须分别使用otherwise-valid managed `INTEGRATED`和`PRESENT` fact反例：`plan_sha256/original_stage3_fact_sha256/status/source/reused/runtime_root/verified_entrypoint/version_evidence`或同一identity其他字段复制/派生Provider value时，必须`PRELAUNCH_BLOCKED/INVALID_INPUT`、spawn 0、receipt/log/exception原文0，并以空tuple清空整个`local_capability_evidence_identities`；不得保留混合identity的独立子字段。

### V2-S4-T6：未来实现精确文件白名单

未来实现只能评估并授权以下5个路径：

```text
golden_key_openmontage_workbuddy/session_launcher.py       # 唯一新增生产模块
golden_key_openmontage_workbuddy/__init__.py               # 只导出launch_session_tool
tests/workbuddy/test_session_launcher.py                    # 唯一新增直接测试
tests/workbuddy/test_repository_hygiene.py                  # 固定树/API/source断言35->37
.github/workflows/ci.yml                                    # 唯一pytest命令加入直接测试
```

新增生产文件与直接测试使tracked从35精确变为37；hygiene必须同步固定37文件白名单、4个Python源文件和唯一Stage4 API，否则新增合法文件会被现有固定35合同拒绝；CI必须把唯一Stage4直接测试加入现有唯一pytest命令，否则正式门禁不执行新合同。不得动态放宽树断言或使用glob接受未来文件。`package_registration.py`、`runtime_prepare.py`、`pyproject.toml`原则上禁止修改；任何需要它们或第6个路径的方案立即`STOPPED_SCOPE_EXPANSION`并回到用户重新授权。

### V2-S4-T7：Builder、Reviewer与推广

规划推广时要求用户另行明确说“启动阶段四实现”；该历史条件已由用户2026-08-20指令满足，并由正式授权结果`2c3d87bedfa4a3cef3cfd952641199300f2715dc`固化。实施Builder接管时live authority必须从最新`origin/codex/workbuddy-shell-v2`冻结精确base/tree/37目标文件合同，创建一个临时Builder分支，只允许上述5路径。Builder必须使用项目D盘独立`.venv`，运行Stage4直接测试、repository hygiene和完整仓库测试，保留未截断输出和最终exit 0；检查精确diff、37文件等值、clean/untracked0/stash0后提交并非force推送。独立Reviewer零写，只审精确base..candidate，核对公共合同最小性、fail-closed反例、secret为0和真实测试定义；`REQUEST_CHANGES`只回原Builder。只有`APPROVE/P0=0/P1=0/P2=0`、formal仍等于base、对象一致时才允许普通fast-forward推广。推广完成也不得自动启动Stage 5、Stage 6或最终Package Gate。

任务执行顺序、输入、交付与退出条件固定为：

| 任务 | 输入 | 交付输出 | PASS退出条件 / fail-closed停止 |
|---|---|---|---|
| T1 工具身份 | Locator当前返回合同、批准Package/Installer authority边界 | 不含Locator hash环的`PackageToolDefinitionV1`、外部Registration/Manifest/Lock绑定与真实fixture往返 | schema/authority/path/hash/size/owner/interpreter/argv全部唯一；`register -> locate -> validate`可实例化；具体Release缺实例时记录`TOOL_DEFINITION_UNBOUND`，不猜入口 |
| T2 公共入口 | T1定义、Stage2 Locator、Stage3现有证据边界 | 唯一`launch_session_tool(...)`、closed controls、完整批准能力定义+原始Stage3 fact、source-aware复核与stdin envelope | user message/controls/provider secret三者分离；managed/explicit/PATH按已接受语义独立重验；Provider缺失不转成Stage3缺失 |
| T3 生命周期 | T1/T2验证后对象 | cwd/env/stdin/output/timeout/cancel/termination/residual规则 | shell=false、spawn=1、retry=0；身份漂移或环境越权则spawn=0 |
| T4 回执 | T1身份、T3真实进程事实、结果envelope | 总是返回的全字段`LauncherReceiptV1`、9值outcome闭集、23 reason与11级裁决优先级 | provenance-aware动态域零传播、静态常量偶撞可表示、递归冻结；证据不完整不得成功 |
| T5 测试矩阵 | T1-T4合同及原21项反例 | 55类直接/负面测试、secret碰撞/传播、三类source交接、真实Stage2 fixture往返与成功夹具 | 所有反例断言spawn/outcome/reason/残留；外来explicit文件零改写；不运行真实Provider/媒体/WorkBuddy |
| T6 文件范围 | 当前35文件固定树与现有hygiene/CI | 精确5路径、37文件终态 | 只新增生产+直接测试两文件；第6路径或动态放宽立即停止 |
| T7 交付治理 | 最新formal精确对象、T1-T6 | Builder证据、零写Reviewer、普通FF推广路径 | REVIEW APPROVE且P0/P1/P2=0、对象/路径/测试/clean全匹配；否则只回原Builder |

T1到T4是同一个单生产模块内的私有实现职责，不得为了任务编号拆成新模块。T5/T6只提供直接证据和固定仓库门禁。T7完成后Stage4仓库实现才可收口，但Stage5/6仍保持未授权。

以下是规划推广时冻结的历史closeout目标；它已经由`V2-S4-PLAN-CLOSEOUT-REVIEW1`独立`APPROVE / P0=0 / P1=0 / P2=0`及`dfd97f3d2e05a4c448448fc14514d1cfe76836e8`普通fast-forward全部满足，不再是当前授权状态：

```text
historical_closeout_target_stage_4_planning: PASS_ACCEPTED
historical_closeout_target_stage_4_implementation_authorization: NOT_GRANTED
historical_closeout_target_stage_4_launcher_authorization: NOT_GRANTED
historical_closeout_target_next_authorized_task: NONE
historical_closeout_target_stage_5_workbuddy_entry_authorization: NOT_GRANTED
historical_closeout_target_stage_6_status_result_relay_authorization: NOT_GRANTED
historical_closeout_target_final_package_gate_authorization: NOT_GRANTED
```

这些字段只记录当时的历史目标，不得覆盖文件顶部的当前六权威同步候选和条件生效字段。

### 与Stage 5/6不断档

Stage 5只保留literal `user_message`，形成closed `executor_controls`、从已批准Package/Installer对象取得`PackageToolDefinitionV1`、按用户单独授权解析Provider环境，并在固定定义确有本地要求时原样传递完整approved capability definition和未改写original Stage3 fact；它不生成命令或argv，也不生成替代摘要。Stage 4按fact原始source独立复核定义与实际资产：managed closed-tree、explicit全部定义资产但允许且保留额外文件、PATH仅entrypoint asset；只启动一次并返回`LauncherReceiptV1`。Stage 6优先原样复用该receipt；若真实Stage 5消费者不需要转换，则以`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`和生产代码0完成。该规划不预建Stage 5/6。

## 阶段2已完成任务证据

```text
completed_task_id: V2-S2-REQUIRED-TOOLCHAIN-PACKAGE-REFRESH-BUILDER1
completed_task_start_commit: 55781b45ac9217693843f2c73cec994805e4024c
completed_task_initial_result_commit: 62a47afa2301eb187a8b63e33ad08f1b5476c318
completed_task_final_result_commit: 709c8e880b144fa9e9be26e9feb5d776dd6025e2
completed_task_review_range: 55781b45ac9217693843f2c73cec994805e4024c..709c8e880b144fa9e9be26e9feb5d776dd6025e2
completed_task_reviewer_verdict: APPROVE / P0=0 / P1=0 / P2=0
completed_task_promotion: ORDINARY_FAST_FORWARD / origin/codex/workbuddy-shell-v2=709c8e880b144fa9e9be26e9feb5d776dd6025e2
completed_task_authorization: CONSUMED_COMPLETE
review1_initial_verdict_history: REQUEST_CHANGES / P0=0 / P1=1 / P2=1 / resolved by 709c8e880b144fa9e9be26e9feb5d776dd6025e2
previous_contract_correction_status: PASS_ACCEPTED
previous_contract_correction_formal_commit: 29a890db22181db9532263a168dcbe5f708b7149
previous_contract_correction_review: INDEPENDENT_APPROVE_AND_FAST_FORWARD_PROMOTED
stage_2_completed_allowed_paths:
  - golden_key_openmontage_workbuddy/package_registration.py
  - tests/workbuddy/test_package_registration.py
  - docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md
  - docs/workbuddy/v2/TASK-REGISTER.md
production_code_limit: 1 file
test_change_limit: 1 file
documentation_change_limit: 2 files
source_repository: D:\BlazingCD\Personal\golden_key_short_video_agent-openmontage-agent-cleanroom
source_commit: 8395e578165e802990d53fef5a166f8b4cf0461a
source_package_tree_path: packages/golden-key-openmontage
source_package_tree: 0464861c5985c7c9072e789b94889d29cf9a937a
source_export_rule: 只允许从上述Git对象导出；不得触碰、修改或清理source repository当前dirty worktree
python_archive: D:\Downloads\Working\python-3.14.7-embed-amd64.zip
python_archive_size: 12673227
python_archive_sha256: d297e5ff019966817ad8502465176139f2d3d840fa4ed84b13bed399a6ab1f15
node_version: v22.23.2-win-x64
node_archive_url: https://npmmirror.com/mirrors/node/v22.23.2/node-v22.23.2-win-x64.zip
node_archive_size: 35683585
node_archive_sha256: 1177b4137ba5adaa56354ae40f1080c7450e8ae09cecb47da459d1c52ac99f97
ffmpeg_publisher_channel_label: 9.0 essentials
ffmpeg_actual_binary_version: 9.0.1-essentials_build
ffmpeg_archive_url: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.7z
ffmpeg_archive_size: 34372199
ffmpeg_archive_sha256: 49a73bdf0850092a252ac4641d922f3048d63ed113e196cc65ce1e4f7fb33e85
rejected_ffmpeg_archive: D:\Downloads\Working\ffmpeg-9.0-essentials_build.7z / SHA256 prefix ffb866 / MUST_NOT_USE
temporary_build_root: D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1
project_venv_rule: 必须使用该任务在D盘的独立.venv；不得混用系统或其他项目Python包
package_build_scope: 一次真实临时Package；源树+干净私有Python及锁定核心依赖+FFmpeg/ffprobe+Node/npm/npx
registration_scope: Stage2必须验证并返回全部必带工具身份与固定路径；负面测试fail closed
forbidden_scope: external source repo、官方OpenMontage、Installer、Runtime、Launcher、Stage3、Skill、config、其他测试、生产DataRoot激活、WorkBuddy、Provider、媒体
resolved_python_distributions: 47
offline_dependency_rebuild: 4555 files / missing=0 / extra=0 / changed=0
real_package_core_files: 2155
real_package_toolchain_files: 6670
real_package_manifest_entries: 8826
real_release_size: 223112435
real_release_sha256: f00e83d6154e7593b765a3d6c863b6653fc642818133acd7924f3fd91aab5d03
real_registration_sha256: aa5aba5ff543258d58acf944a0f4e87d80b9f38e62205268ae23b5266b78659b
real_register_activate_locate: PASS / task-only DataRoot
builder_changed_files_cumulative: production=1 / test=1 / docs=2
fix1_changed_files: production=1 / test=1 / docs=1
pre_fix_full_test_command: D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\.venv\Scripts\python.exe -m pytest -q
pre_fix_full_test_result: 141 passed in 22.49s / final exit 0
fix1_target_test_command: D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\.venv\Scripts\python.exe -m pytest tests/workbuddy/test_package_registration.py -q -k "required_toolchain_rejects_internal_and_cyclic or required_toolchain_resolve_runtime_error"
fix1_target_test_result: 3 passed / 131 deselected in 3.03s / final exit 0 / real Windows reparse tests not skipped
fix1_full_test_command: D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\.venv\Scripts\python.exe -m pytest -q
fix1_full_test_result: 144 passed in 20.46s / measured wrapper 20.84s / final exit 0
real_package_assembly_command: D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\.venv\Scripts\python.exe D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\assemble.py D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\export\package D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\release
real_package_assembly_result: final exit 0 / Release size and SHA-256 unchanged
real_registration_command: PYTHONPATH=<ShellRepo>; D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\.venv\Scripts\python.exe D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1\register_evidence.py D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1
real_registration_result: register + task-only activate + locate / final exit 0 / registration SHA-256 unchanged
real_tool_commands: bootstrap/python/python.exe -B -c <core imports + SSL + same-interpreter subprocess>; bootstrap/ffmpeg/bin/ffmpeg.exe -version; bootstrap/ffmpeg/bin/ffprobe.exe -version; bootstrap/node/node.exe --version; bootstrap/node/npm.cmd --version; bootstrap/node/npx.cmd --version
real_tool_results: Python 3.14.7/OpenSSL 3.5.7; FFmpeg+ffprobe 9.0.1; Node 22.23.2; npm+npx 10.9.8 / every command final exit 0
exit_evidence: Stage2 task-only Package build and DataRoot cleaned after evidence capture; no retained final Release, installed production PackageRoot, or production Registration
```

上述证据证明完整工具链组装能力、Stage 2 Registration/Locator实现，以及一次真实register、task-only activate和new-process locate已经完成并正式接受；临时实例清理不重开、不重做阶段2。它仍不证明最终交付Package持续存在。最终Package持久构建、安装、生产登记和激活仍是强制交付要求，但只属于后续最终交付或Installer收口门禁，最迟在Stage 5真实WorkBuddy入口和生产验收前完成；它绝不是Stage 3编码前置，也不得塞入Stage 3 Runtime代码。

历史Stage 3授权顺序要求五文档纠偏先完成独立审阅和正式推广，再由live authority给出精确Builder基线、五路径白名单和Reviewer范围；该顺序已完成并由上述正式实施结果消费。不得增加Package、Registration、Package绑定能力元数据、task-only登记验证或Stage 5输入Gate。持久最终Package与生产Registration仍在后续最终交付或Installer Gate收口，但不属于Stage 3失败或编码前置。开发或测试任务不得随意写入外部对象或DataRoot；未来产品运行时只有在用户对具体能力明确`approve`后，才允许Stage 3在受管DataRoot执行合同规定的staging和集成。已接受Builder没有进行真实第三方下载。

## 当前正式状态

```text
formal_ref: refs/heads/codex/workbuddy-shell-v2
formal_head_resolution: LIVE_REMOTE_REF_REQUIRED
formal_tree_resolution: LIVE_REMOTE_REF_TREE_REQUIRED
mirror_result: THIS_COMMIT
mirror_effect: ZERO_PRODUCT_STATE_CHANGE
mirror_repository_delivery_resolution: zero-write APPROVE exists AND LIVE_REMOTE_REF contains THIS_COMMIT
historical_formal_handoff_before_stage3_correction: 068408f02c87a1eabeda58ea1ebce3df606c0a0c
historical_accepted_stage3_correction_result: 7ba6ad64270c7ccdd7500e2a59b05cf55c73d7ed
stage_3_implementation_formal_result: a3f8959682d296301dc573c2835f8c705a52e8b2
stage_3_closeout_formal_result: 7c15aae4e77c579309312b21c79076f930970214
stage_3_to_stage_4_docs_sync_formal_result: 513e5ca10d1ba04878295be110096b013f47974a
stage_3_to_stage_4_docs_closeout_formal_result: a8d024ca9001184e9c2a5a995598d64024eef51b
ci_stage3_state_assertion_fix_formal_result: e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3
ci_stage3_state_assertion_fix_review_history: first independent review INCOMPLETE / P0=0 / P1=0 / P2=0 / authority mismatch only / code diff no finding
ci_stage3_state_assertion_fix_ci: run 32218904419 / completed / success / 198 passed / 1 skipped / final exit 0
ci_stage3_state_assertion_closeout: PASS_ACCEPTED / 26bfe60ab9da62797559eb9a459b8daa345f8d80 / FORMALLY_PROMOTED
stage_1_status: PASS_ACCEPTED
stage_2_status: PASS_ACCEPTED_REGISTRATION_AND_TEMPORARY_PACKAGE_PROOF_ONLY
stage_2_registration_implementation: PASS_ACCEPTED
stage_2_temporary_package_validation: PASS_ACCEPTED
stage_2_required_toolchain_refresh: PASS_ACCEPTED
stage_2_required_toolchain_refresh_result: 709c8e880b144fa9e9be26e9feb5d776dd6025e2
stage_2_required_toolchain_refresh_review: APPROVE / P0=0 / P1=0 / P2=0
stage_2_required_toolchain_refresh_promotion: origin/codex/workbuddy-shell-v2=709c8e880b144fa9e9be26e9feb5d776dd6025e2
stage_2_previous_package_status: PASS_ACCEPTED_HISTORICAL
stage_2_integration_commit: ca6e93b7da108732f2034239da340a986ba3da3a
repository_hygiene_status: PASS_ACCEPTED
repository_final_tree_commit: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
repository_final_audit: APPROVE
repository_final_audit_source: USER_ACCEPTED_HANDOFF_2026_08_17
repository_tracked_files: 37
final_package_artifact: NOT_MATERIALIZED
installed_production_package_root: NOT_CREATED
production_package_registration: NOT_CREATED
production_package_activation: NOT_CREATED
stage_3_planning_authorization: CONSUMED_COMPLETE
stage3_planning: PASS_ACCEPTED_FORMALLY_PROMOTED_AT_061AC8428823C8732F241B01A7FD9E54A732599A
stage_3_implementation_authorization: CONSUMED_COMPLETE
stage_3_conditional_authorization: CONSUMED_COMPLETE
stage_3_start_gate: PASS_ACCEPTED
stage_3_final_package_dependency: NOT_REQUIRED_FOR_CODING_START
final_package_gate: DEFERRED_TO_FINAL_DELIVERY_OR_INSTALLER_CLOSEOUT_BEFORE_STAGE5_PRODUCTION_ACCEPTANCE
stage_3_package_release_input: NOT_REQUIRED
stage_3_registration_input: NOT_REQUIRED
stage_3_package_bound_capability_metadata: REMOVED_FROM_INPUT_MODEL
stage_3_consumer_interface_contract: PASS_ACCEPTED_FORMALLY_PROMOTED_AT_061AC8428823C8732F241B01A7FD9E54A732599A
stage_3_product_execution_contract: PASS_ACCEPTED_FORMALLY_PROMOTED_AT_061AC8428823C8732F241B01A7FD9E54A732599A
real_workbuddy_validation: DEFERRED_TO_STAGE_5_ACCEPTANCE
stage_3_execution_packet: CONSUMED_COMPLETE / EXACT_5_PATHS
stage3_implementation: PASS_ACCEPTED
stage_3_status: PASS_ACCEPTED
stage_4_plan_formal_result: 5cb3f585a0cddffbd823c785b1d39ebd1834c1df
stage_4_plan_formal_tree: 144df76b3a307fa8944ccd7bd384bddb1b340516
stage_4_plan_promotion: ORDINARY_FAST_FORWARD / origin/codex/workbuddy-shell-v2=5cb3f585a0cddffbd823c785b1d39ebd1834c1df
stage_4_plan_review: V2-S4-PLAN-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_plan_ci: run 32337744225 / completed / success
stage_4_plan_closeout: PASS_ACCEPTED / dfd97f3d2e05a4c448448fc14514d1cfe76836e8 / tree 5eeb8a9337c5b38be60d3b0cef184b8898f2fedc
stage_4_plan_closeout_review: V2-S4-PLAN-CLOSEOUT-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_plan_closeout_ci: run 32338998075 / completed / success / head_sha=dfd97f3d2e05a4c448448fc14514d1cfe76836e8
stage_4_planning: PASS_ACCEPTED
stage_4_implementation_authorization_formal_result: 2c3d87bedfa4a3cef3cfd952641199300f2715dc
stage_4_implementation_authorization_formal_tree: c196dbf6b094cad05076d01ac2496f7425cf6fac
stage_4_implementation_authorization_review: V2-S4-IMPLEMENTATION-AUTHORIZATION-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_implementation_authorization_ci: run 32340096961 / completed / success / head_sha=2c3d87bedfa4a3cef3cfd952641199300f2715dc
stage_4_implementation_authorization: CONSUMED_COMPLETE
stage_4_implementation_formal_result: fa9adb8470ab94b88ec9900ede03cb26f7de0ebd / tree 0809d1c4cccc9838180a016c75320b0d9fbce28a / exact five paths / tracked 35->37
stage_4_implementation_review: V2-S4-IMPLEMENTATION-REVIEW1 / EIGHTH_ROUND_APPROVE / P0=0 / P1=0 / P2=0
stage_4_implementation_first_formal_ci: run 32367792637 / failed / test fixture assumed setup-python included pyvenv.cfg / no production Launcher finding
stage_4_ci_fixture_fix_formal_result: 13a3227b0c55bbe9039b46d7e92eba822b48f57e / tree d3ac89ec89b66789cabe92d94c3e827f9c2cc22f / one test path only
stage_4_ci_fixture_fix_review: APPROVE / P0=0 / P1=0 / P2=0
stage_4_formal_ci: run 32369588814 / Ubuntu 24.04 / Python 3.11.16 / success / 357 passed / 1 skipped / exit 0
stage_4_windows_evidence: 158 direct / 11 hygiene / 358 combined / all exit 0 / no skip
stage_4_implementation: PASS_ACCEPTED
stage_4_closeout_formal_result: b63d8c2bc2214bc39f18378dbe47057ef538301e
stage_4_closeout_formal_tree: 02814c6a4a483913e7b1abe3e9ee6d025236c951
stage_4_closeout_review: V2-S4-IMPLEMENTATION-CLOSEOUT-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_closeout_ci: run 32371507874 / Ubuntu 24.04 / Python 3.11.16 / completed / success / 357 passed / 1 skipped
stage_4_wsl_boundary: NO_RUNTIME_DEPENDENCY / temporary Linux-equivalence validation only / cleaned and shut down after testing
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
final_package_gate_authorization: NOT_GRANTED
final_handoff_hygiene_formal_result: 4636e27a62aad9f1b721e6c482e34b44d350503c
final_handoff_hygiene_formal_tree: fdf24f8450ac4bb48e5337cd7aa3477794796d19
final_handoff_hygiene_review: independent zero-write Reviewer / APPROVE / P0=0 / P1=0 / P2=0
final_handoff_hygiene_ci: run 32386393634 / completed / success / Python 3.14.7 / 357 passed / 1 skipped / actions v6 / no Node20 deprecation warning
current_task: NONE
current_task_status: NO_ACTIVE_TASK
next_authorized_task: NONE
effective_stage_4_launcher_authorization: NOT_GRANTED
effective_stage_5_workbuddy_entry_authorization: NOT_GRANTED
effective_stage_6_status_result_relay_authorization: NOT_GRANTED
effective_final_package_gate_authorization: NOT_GRANTED
stage_3_to_6_scope_reduction: ACTIVE_REPLANNED_BOUNDARY
runtime_correction: REQUIRED_TOOLCHAIN_REFRESH_PASS_ACCEPTED
```

`709c8e880b144fa9e9be26e9feb5d776dd6025e2`完成了Stage 2必带工具链和Registration/Locator的真实临时证明；该历史事实不重开，也不再作为Stage 3输入。Stage 3实现已经独立审阅并正式推广为`a3f8959682d296301dc573c2835f8c705a52e8b2`，closeout `7c15aae4e77c579309312b21c79076f930970214`也已正式推广，因此Stage 3继续为`PASS_ACCEPTED`。

CI状态断言修复`e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3`已经位于正式分支，精确代码差异仅为`tests/workbuddy/test_repository_hygiene.py`中的两条Stage3状态断言；正式CI run `32218904419`为`completed/success`，输出`198 passed / 1 skipped`。第一次独立Reviewer结论保持为`INCOMPLETE / P0=0 / P1=0 / P2=0`，原因只有当时authority mismatch，代码差异无finding。正式分支在账本收口前前移属于治理偏差，本closeout只同步实时权威，不改写审查或Git历史。

CI状态断言closeout已在`26bfe60ab9da62797559eb9a459b8daa345f8d80`正式收口。Stage4规划最终结果`5cb3f585a0cddffbd823c785b1d39ebd1834c1df`及规划closeout `dfd97f3d2e05a4c448448fc14514d1cfe76836e8`均已独立审查、普通fast-forward并由正式CI验证，因此`stage_4_planning=PASS_ACCEPTED`。实施结果`fa9adb8470ab94b88ec9900ede03cb26f7de0ebd`经第八轮独立审查`APPROVE / P0=0 / P1=0 / P2=0`进入formal；run `32367792637`随后只暴露测试夹具错误假定GitHub `setup-python`存在`pyvenv.cfg`，不是生产Launcher缺陷。单测试路径修复`13a3227b0c55bbe9039b46d7e92eba822b48f57e`也经独立审查`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward，正式Ubuntu CI run `32369588814`为`357 passed / 1 skipped / exit 0`。Stage4 closeout固定历史锚点`b63d8c2bc2214bc39f18378dbe47057ef538301e`、tree `02814c6a4a483913e7b1abe3e9ee6d025236c951`已经`V2-S4-IMPLEMENTATION-CLOSEOUT-REVIEW1`独立`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward，closeout CI run `32371507874`在Ubuntu 24.04 / Python 3.11.16上`357 passed / 1 skipped`，因此Stage4实现已是`PASS_ACCEPTED`。原三路径卫生尝试因发现三个额外陈旧当前入口文档而在零worktree、零修改、零测试、零提交/推送且WSL未启动的安全节点停止；该历史`INCOMPLETE`已由修订授权和正式六路径结果`4636e27a62aad9f1b721e6c482e34b44d350503c`闭合。最终卫生结果经独立`APPROVE / P0=0 / P1=0 / P2=0`及正式CI run `32386393634`验证；当前为`current_task=NONE / current_task_status=NO_ACTIVE_TASK / next_authorized_task=NONE`。真实生产WorkBuddy/Launcher会话、Stage5、Stage6、Provider/媒体执行及final Package物化/生产登记仍为`NOT_GRANTED`或未证明。

仓库卫生历史基线`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`为tracked精确33且等于当时固定白名单；Stage 3按已审五路径新增两个受控文件并同步更新卫生断言后，正式结果`a3f8959682d296301dc573c2835f8c705a52e8b2`为tracked精确35；Stage4又严格按五路径新增一个生产模块和一个直接测试并同步两项验收基础设施，正式结果为tracked精确37。没有恢复任何已清理内容。

## 阶段3至阶段6建设与交付顺序

```text
Stage 3: Runtime Preparation on Demand
Stage 4: Session Launcher
Stage 5: WorkBuddy Entry
Stage 6: Status and Result Relay
```

该顺序只表示建设、审阅和正式交付顺序，不是最终用户运行时的调用顺序。每个阶段都从当时最新的`origin/codex/workbuddy-shell-v2`精确提交开始，经单一有界Builder、独立只读Reviewer、普通非force fast-forward推广、远端临时分支清理和本地worktree关闭后，下一阶段才可接管。规划接受、Builder提交或Reviewer批准均不等于正式交付。

新的固定关系是：阶段4基础调用依赖阶段2必带工具链；阶段3有界探测Remotion和HyperFrames并报告事实，缺失/不兼容时由WorkBuddy询问用户，只有逐能力批准才集成。拒绝或暂缓不阻塞其他已有/基础能力。OpenMontage决定生产使用哪项实际可用能力；Shell不选渲染器、不自动重放原业务请求。

阶段3至阶段6共同约束：每阶段最多一个公共入口；没有可验证输入或直接下游消费者时必须零代码退出；不得预建通用Runtime管理器、CLI/MCP镜像、任务平台、后台服务、第二Agent Host、生产FSM或状态数据库。WorkBuddy是唯一运行中的Agent；所谓OpenMontage Agent只能指WorkBuddy读取已验证Package Guide后承担的逻辑生产角色。

## 阶段授权与零代码出口

```text
stage_3_scope: bounded detect Remotion and HyperFrames; report PRESENT/MISSING/INCOMPATIBLE; integrate only explicitly approved missing/incompatible items under managed DataRoot; decline/defer is SKIPPED/NOT_INTEGRATED; never detect/download Python/FFmpeg/Node
stage_3_public_entry: prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)
stage_3_result_set: DETECTION_REPORT / CONSENT_REQUIRED / INTEGRATED / SKIPPED / BLOCKED
stage_3_capability_fact_set: PRESENT / MISSING / INCOMPATIBLE / NOT_INTEGRATED
stage_3_zero_write_result: DETECTION_REPORT / CONSENT_REQUIRED / SKIPPED / BLOCKED(reason_code=INVALID_DEFINITION_OR_TARGET)
stage_3_download_policy: OPTIONAL_CAPABILITY_APPROVED_MAINLAND_CHINA_MIRRORS / NO_AUTOMATIC_OVERSEAS_FALLBACK
stage_3_definition_authority: APPROVED_OPENMONTAGE_CAPABILITY_DEFINITION / INDEPENDENT_OF_PACKAGE_IDENTITY_METADATA
stage_3_product_code_paths: golden_key_openmontage_workbuddy/runtime_prepare.py + export-only golden_key_openmontage_workbuddy/__init__.py + tests/workbuddy/test_runtime_prepare.py
stage_3_acceptance_infrastructure_paths: tests/workbuddy/test_repository_hygiene.py + .github/workflows/ci.yml
stage_3_accepted_builder_exact_allowlist_rule: exactly the 3 product paths plus the 2 acceptance-infrastructure paths; no other path; the latter only updates fixed tracked/API/source assertions and the one CI pytest command
stage_4_scope: 基础固定工具调用接受阶段2必带工具链事实；只在PackageToolDefinitionV1声明required_local_capabilities时接受完整approved capability definition与未改写original Stage3 fact并按managed/explicit/PATH原始source独立重验；Provider配置与本地能力证据分离；阶段4不硬编码Provider/Runtime、不查询registry、不自行安装、不启动第二Agent、无任意Shell、无自动重试。
stage_5_scope: 用户实际运行起点；只保留一种真实WorkBuddy显式入口，literal user_message不变，技术控制独立。
stage_6_scope: 直接转交Runtime计划/准备事实与Launcher回执；仅有真实格式转换缺口时才允许独立实现；不解释、不安装、不重试。
stage_6_zero_code_exit: STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE
```

上述范围定义产品边界，本身不单独产生实现授权；当前实施授权及接管条件只以文件顶部live authority为准。任何需要阶段3扫描盘符、发现/下载/替换包内Python/FFmpeg/Node、一次安装全部可选能力、选择渲染引擎/版本、使用未批准海外默认源或覆盖外来目录，阶段4启动第二Agent、解析意图或调度任务，阶段5建立第二聊天Agent，阶段6解释Artifact或自动重试的方案，必须停止并返回`STOPPED_SCOPE_EXPANSION`。

## 阶段3重新规划合同

上一版阶段3执行包、`prepare_runtime_on_demand(...)`签名，以及Package绑定能力元数据、Registration绑定和零能力零代码模型全部`SUPERSEDED`，不得交给Builder。新阶段3只做Remotion和HyperFrames的有界探测、事实报告、零下载计划、逐能力用户决定和批准项受管集成。

### 历史实现启动Gate（已满足并消费）

以下两项是Stage 3实现前的历史Gate，现已满足并由正式结果消费：

1. 当前五文档产品模型纠偏完成独立审阅，并正式fast-forward推广到`origin/codex/workbuddy-shell-v2`；
2. `TASK-REGISTER.md`基于当时最新正式Git对象明确授予精确Builder基线、五文件允许路径、直接测试和独立Reviewer范围。

不得再增加Package、Registration、Package绑定能力元数据、task-only登记验证或Stage 5输入Gate。授权前缺一项时零代码停止；不得创建占位实现、通用Runtime框架或测试假合同。

### 唯一输入合同

`capability_definitions`中Remotion和HyperFrames每项最少固定为：

```text
capability: remotion | hyperframes
definition_sha256
version
verified_entrypoint
approved_mainland_sources
assets: filename + size + sha256 + license + managed_target
explicit_registered_or_configured_candidate_paths: optional
normal_command_name: optional
```

能力定义来自批准的OpenMontage能力定义权威。调用方不能提供定义外URL、任意命令、任意安装目录、盘符扫描或系统软件枚举请求。`user_decisions`只能对精确`capability + definition_sha256 + plan_sha256`表达`approve/decline/defer`；任一事实变化使旧批准失效。literal `user_message`永远不进入本接口。

### 固定执行步骤

1. **定义验证**：验证两项批准OpenMontage能力定义的版本、入口、批准大陆来源、大小、SHA-256、许可证和受管目标；拒绝任意URL、命令和目标注入。
2. **有界探测**：只检查受管DataRoot目标、明确登记/配置的候选路径和正常命令解析；禁止遍历盘符、系统软件清单、全局npm状态和猜目录。
3. **事实报告**：分别报告Remotion和HyperFrames的`PRESENT/MISSING/INCOMPATIBLE`、入口、版本和来源。存在则复用；缺失或不兼容不是失败。
4. **零下载计划**：为每个缺失/不兼容项返回来源、版本、hash、大小、许可证、受管目标、总下载量和`plan_sha256`，状态`CONSENT_REQUIRED`；不得下载或写入。
5. **用户决定**：WorkBuddy逐项询问。`decline/defer`返回`SKIPPED/NOT_INTEGRATED`，不影响其他能力或基础能力。
6. **授权复核与集成**：仅对仍匹配`capability + definition_sha256 + plan_sha256`的`approve`项，使用阶段2必带Node/npm/npx从批准大陆来源下载到同卷staging，核验后发布到`<DataRoot>/Runtime/Composition/<capability>/<definition_sha256>/`。
7. **失败处理**：外来目标保留并fail closed；hash、大小、许可、来源、命令或探针失败即回滚，清除staging和任务临时文件，不修改系统PATH、注册表或全局npm，不自动海外回退。
8. **最终报告**：重新探针批准项，确认未批准能力和必带Python/FFmpeg/Node零变化后返回`INTEGRATED`及能力、定义、runtime root、入口、版本和资产证据。

### 后续阶段交接

- 阶段4基础调用只消费阶段2必带工具链事实；只有固定工具定义声明本地能力要求时才接收完整批准定义与未改写原始Stage3 fact，并按managed closed-tree、explicit定义资产、PATH entrypoint asset的原始source语义独立重验。当前Stage3的Remotion/HyperFrames定义与事实只是现有来源；Provider配置不是Stage3能力证据，Launcher不能自行安装或路由。
- 阶段5拥有用户对话、计划展示、明确同意和真实WorkBuddy继续动作；真实验收优先同任务继续，不能时固定提示“继续刚才的任务”；技术控制与用户原话分离。
- 阶段6优先原样转交探测、`CONSENT_REQUIRED`、`INTEGRATED`、`SKIPPED`、`BLOCKED`和Launcher事实；不安装、不解释Artifact、不自动重试。
- Shell不得声称已无缝继续；阶段5真实WorkBuddy测试证明同一任务可继续后才允许该说法，否则由WorkBuddy要求用户回复“继续刚才的任务”。

### 已接受的最小文件和交付

已接受产品实现只新增`golden_key_openmontage_workbuddy/runtime_prepare.py`，最小编辑`golden_key_openmontage_workbuddy/__init__.py`导出唯一入口，并新增`tests/workbuddy/test_runtime_prepare.py`；同一Builder只为验收同步编辑了`tests/workbuddy/test_repository_hygiene.py`和`.github/workflows/ci.yml`。正式结果保持单一入口、稳定结果集、有界探测/计划/用户决定/集成事实及直接测试证据；它不是Installer、最终Package、WorkBuddy入口、Launcher或视频E2E证明。

## 已接受对象与证据边界

```text
immutable_v1_code_baseline: 2a2bf09832d558388dc2816c54b32a2dce4aa607
stage_1_reviewed_commit: 041c6600dc8eb9094b5c93cb4a4ed088894578af
stage_1_integrated_boundary: fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9
stage_1_reviewer_task: 01a004a6-aab1-7992-abe0-6dcbe8490a71
stage_1_reviewer_verdict: APPROVE / P0=0 / P1=0 / P2=0
stage_2_contract_commit: 5dd144e40ff1bf8682c8b43ac9973e40fc0be946
stage_2_final_implementation_commit: ab1eddf474233859c6a3b32056a503f82ecdc117
stage_2_gate_prep_commit: 104fe684c0bae6604c278fcf756579700bd8e1e0
stage_2_integration_commit: ca6e93b7da108732f2034239da340a986ba3da3a
stage_2_final_reviewer_task: 01a005c3-692c-7761-9f11-45e178c0d599
stage_2_final_reviewer_verdict: APPROVE / P0=0 / P1=0 / P2=0
stage_2_integration_reviewer_task: 01a00606-a1d3-7ab3-ab75-8d16efd064fa
stage_2_integration_reviewer_verdict: APPROVE / P0=0 / P1=0 / P2=0
stage_1_stage_2_consolidation_audit: 01a00617-e037-72a3-b1e5-d88b3d0be19f / APPROVE
repository_hygiene_wave_a_result: 830d44ab7b910e20bfc9093bf2c505850860880a
repository_hygiene_wave_a_closeout: 385a20bbff9624703682eecba3b38fc3c6d2d6b9
repository_hygiene_sequence_authority: cf04dc20d428233e2d328578a1e5d58ebaca2feb
repository_hygiene_wave_b_result: a9e660d5f059a2b8e20cd35dde761b941811494d
repository_hygiene_wave_b_ci_scope_fix: 2f70e426d52a2ea939f5b00e276f9da6bc108a69
repository_hygiene_final_ci_freeze: 2e4858bdd5142a8f041d708bdb385a197c4436a9
repository_hygiene_wave_c_result: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
```

刷新前的旧Stage2对象只证明早期Package的Python登记合同；当前已接受对象另行证明完整必带工具链Registration/Locator实现及一次真实临时Package验证。两代证据都不证明最终Release仍然存在，也不证明生产安装/登记、Installer、Runtime、Launcher、真实WorkBuddy、Provider、SaaS、网络或媒体E2E。阶段3至阶段6不得读取未验证Package Guide、扫描磁盘猜测对象，或把技术控制词写入literal `user_message`。

老项目可迁移证据：`347272c`固定包内便携Python；`899592d`固定完整Runtime、hash、许可、DataRoot和大陆PyPI/npm/Node/浏览器镜像；`639978d`增加`managed`、`registered_host`、`PATH_host`、`missing`发现与missing-only准备。旧锁中的“FFmpeg 9.0 essentials”只提供候选来源标签；本次冻结URL与hash对应二进制实际报告`9.0.1-essentials_build`。它不形成阶段3下载授权，也不得扩展为其他可选能力的海外回退权。

## Stage 5规划冻结（V2-S5-PLAN-BUILDER1）

本节是本任务的唯一Stage 5规划蓝图。它冻结产品目标、T1-T12执行顺序、输入/输出、物理承载和验收边界；它不授权Stage 5实现、真实WorkBuddy、Stage 4真实Launcher、Provider、媒体、最终Package或Stage 6。若本节与旧历史Prompt、旧任务包或聊天内容冲突，以本节、`PROJECT-CHARTER.md`、`ACCEPTANCE-MATRIX.md`和顶部live字段为准；不能确认时停止，不自行解释。

上方继承的“Stage 5规划授权候选”块是`0426860`进入formal前的授权候选历史记录；当前formal对象已在本任务接管前核验为本节的`base_commit/tree`。该历史块不覆盖本节当前规划状态，也不形成Stage 5实现或真实WorkBuddy授权。

```text
task_id: V2-S5-PLAN-BUILDER1
task_kind: STAGE5_PLANNING / DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE
base_commit: 042686039386a63866eba2f964f1fa9674bbec4b
base_tree: 6d6f3f0352eeb75c57170f2fe9e854c79564416c
tracked_files_at_base: 37
builder_branch: codex/v2-s5-plan-builder1
builder_worktree: D:\\BlazingCD\\Personal\\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2-s5-plan1
allowed_paths: docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md
forbidden: production code; tests; CI/workflow; pyproject; Package bytes; Registration/Activation; real WorkBuddy; Launcher; Provider; media; WSL; fourth planning path
stage_5_planning: PLANNING_BLOCKED_EXTERNAL_CONTRACT
stage_5_planning_blocker: T1 exact WorkBuddy Skill package/install/consumer/Stage4-Python-call contract is not evidenced
stage_5_implementation_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
final_package_gate_authorization: NOT_GRANTED
candidate_status: READY_FOR_INDEPENDENT_ZERO_WRITE_REVIEW / NOT_FORMALLY_PROMOTED
test: NOT_RUN_DOCS_ONLY
current_task_after_candidate: NONE
next_authorized_task: NONE
```

### 1. Stage 5产品目标与唯一运行链路

Stage 5的产品目标只有一个：在真实腾讯WorkBuddy中建立一个、且仅一个可显式命中的入口；接收用户原样业务请求和素材引用；把技术控制、授权、经验证的Package身份和Stage 3事实放入独立输入；在读取已验证Package Guide之后，由WorkBuddy承担OpenMontage生产角色；仅调用已接受的Stage 4 `launch_session_tool(...)`；把事实和结果原样呈现给用户。腾讯WorkBuddy是唯一运行中的Agent，Shell不得成为第二Agent、Director、FSM、Supervisor、任务平台、Pipeline/Stage/Artifact/Checkpoint执行器、Provider/模型/渲染器/媒体选择器、CLI/MCP并行控制面或自动重试/重放/后台调度系统。

```text
WorkBuddy唯一显式入口
  -> Stage 2 locate_active_package(data_root)
  -> 验证Registration / PackageRoot / Manifest / Lock / Guide身份 / Python+FFmpeg+ffprobe+Node+npm+npx
  -> 只有验证成功后才读取已验证Package Guide
  -> 取得当前Release提供的PackageToolDefinitionV1
  -> Stage 4 launch_session_tool（固定工具最多spawn一次）
  -> WorkBuddy/OpenMontage按Package合同作Pipeline/Provider/媒体/创意决策
  -> Stage 6原样转交事实与LauncherReceiptV1
```

建设顺序是`Stage 3 -> Stage 4 -> Stage 5 -> Stage 6`，用户实际运行从Stage 5开始。Stage 3五结果和Stage 4九种outcome是两个独立闭集；Stage 6先尝试直接消费同一`LauncherReceiptV1`。任何一层的PASS都不能替代另一层的真实证据。

### 2. 范围内、范围外与外部前置

范围内只有：唯一真实入口身份的合同核验；literal `user_message`、素材、closed `executor_controls`、PackageToolDefinitionV1、Provider环境、完整Stage 3能力定义/原始事实和cancel/continuation的边界；Locator到Guide再到Stage 4的顺序；授权/暂停/继续及结果映射；隐私、凭据、失败闭集；Stage 4至Stage 6事实交接；未来最小Builder任务包和分层验收。

范围外包括：现在写任何生产入口或适配器代码；修改Stage 2/3/4实现、Package、Registration、Activation或CI；运行真实WorkBuddy、真实Launcher、Provider、网络下载、媒体或视频生产；物化最终Package；创建第二Skill、CLI、MCP、服务、数据库、队列、状态机或Stage 6代码；把Remotion、HyperFrames或任何Provider硬编码成Shell选择。

外部前置分为两类：

1. 规划可继续但生产验收前必须满足：最终Package物化、安装、生产Registration/Activation及新进程Locator验证；当前Release具体`PackageToolDefinitionV1`实例；真实WorkBuddy版本、Skill安装归属和会话证据。
2. 规划本身的硬阻断：T1必须证明Skill包结构、安装/导入归属、显式调用主体、唯一消费者，以及不生成命令/argv/Shell字符串即可调用Stage 4 Python API的精确协议。现有官方材料只证明可上传本地Skill并在对话中选择/召唤；本机WorkBuddy 5.3.13只证明存在用户级Skills；两个现存Golden Key Skill属于V1双入口/旧CLI形态，不能复用。T1未闭合时必须保持`PLANNING_BLOCKED_EXTERNAL_CONTRACT`。

### 3. T1-T12固定执行蓝图

以下每项的“未来物理承载”是实施前的裁决，不是当前实现白名单；T1未闭合前禁止把占位路径当成真实接口。

#### T1：真实WorkBuddy唯一Skill入口身份

- **目标**：证明并冻结唯一真实WorkBuddy Skill的包结构、安装/导入归属、显式调用主体、调用机制和唯一消费者。
- **权威输入**：本仓库`AGENT_GUIDE.md`、本章程、`MODULE-DISPOSITION.md`；腾讯官方WorkBuddy资料；经另行授权的当前真实客户端证据；旧V1 Skill仅作`HISTORICAL/DROP`证据。
- **具体动作**：先核对官方资料；若官方合同不足，只在另行授权的独立真实客户端任务中验证安装、显式命中、新会话和调用Stage 4 Python API的实际协议；记录证据、版本、Skill身份和消费者；不修改旧Skill，不启动生产请求。
- **输出**：`T1_WORKBUDDY_ENTRY_CONTRACT`，至少含Skill包结构、安装归属、入口名/调用主体、消费者、Stage 4调用协议和版本证据；当前输出只能是`PLANNING_BLOCKED_EXTERNAL_CONTRACT`。
- **未来文件/物理承载**：最多一个真实WorkBuddy入口资产；包内/用户级物理位置、文件名和导入形态均`UNFROZEN_PENDING_T1`；本规划不创建假Skill、假工具或候选文件。
- **验收**：官方或受控客户端证据能复现一个新会话的显式命中；不依赖CLI/MCP/第二Skill；入口消费者唯一且与WorkBuddy唯一Agent边界一致。
- **Fail-closed**：任一包结构、安装归属、调用主体、精确API或唯一消费者缺失/冲突，状态保持`PLANNING_BLOCKED_EXTERNAL_CONTRACT`，不进入T2实现冻结、不伪造参数、不用CLI/MCP兜底。
- **上下游**：上游为腾讯官方/真实客户端合同；下游是T2输入承载和T12精确文件白名单。T1没有通过时T2-T12只能做合同规划，不能产生实现授权。

#### T2：Stage 5输入合同

- **目标**：冻结用户原话与技术控制、授权和证据的类型/所有权边界。
- **权威输入**：Stage 4已接受的`launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)`合同；Stage 2 Registration/Locator合同；Stage 3完整能力定义和未改写原始`PRESENT/INTEGRATED`事实；本章程消息与凭据边界。
- **具体动作**：分别接收literal `user_message`、素材引用、closed `executor_controls`、完整当前Release `PackageToolDefinitionV1`、Provider环境、完整approved capability definition+original Stage 3 fact、cancel和continuation事实；禁止把路径、Python、cwd、命令、Package身份、重试或证据控制拼入用户消息。
- **输出**：一份可审计的Stage 5输入合同及字段来源表；`local_capability_evidence`只能原样承载完整批准定义和原始事实，不能传摘要、摘要hash或重包装对象。
- **未来文件/物理承载**：仅进入T1确定的唯一入口适配边界和最多一个生产模块；用户原话留在WorkBuddy会话域，控制/凭据留在受控调用域，不能落入PackageRoot、日志或新数据库。
- **验收**：字节级`user_message`不变；素材引用独立；controls闭集；Provider环境只含定义允许名字；Stage 3定义和事实完整、同一能力/definition绑定；cancel与continuation不混为重试。
- **Fail-closed**：未知字段、非法类型、跨域注入、缺完整定义/原始事实、未授权Provider环境或无法安全隔离时停止并不调用Stage 4；不修剪成“看似可用”的摘要。
- **上下游**：上游为T1入口与Stage 2/3/4合同；下游是T3顺序、T4适配、T7隐私和T8失败裁决。

#### T3：Package与Guide验证顺序

- **目标**：保证WorkBuddy只在活动Package和必带工具链被同次Locator验证后读取Guide和取得工具定义。
- **权威输入**：`PACKAGE-REGISTRATION-CONTRACT.md`；Stage 2 `locate_active_package(data_root)`；当前Registration、PackageRoot、Manifest、Lock、Guide和Python/FFmpeg/ffprobe/Node/npm/npx身份。
- **具体动作**：严格执行“显式入口 -> `locate_active_package(data_root)` -> 验证Registration/PackageRoot/Manifest/Lock/Guide身份和完整必带工具链 -> 成功后读取已验证Guide -> 取得当前Release的PackageToolDefinitionV1 -> 形成Stage 4调用”；不扫盘、不猜目录/最新版、不由调用方构造定义。
- **输出**：同次、可追溯的Locator验证事实、已验证Guide身份和当前Release工具定义绑定；失败只产生阻断事实。
- **未来文件/物理承载**：Locator仍为Stage 2既有实现；Guide只由下游消费者在身份验证成功后读取；Stage 5不复制Guide、Registration或Package。
- **验收**：每次新会话验证同一活动Registration；Guide读取前所有身份通过；任何漂移均不进入Stage 4；无盘符遍历、猜路径或未验证Guide读取。
- **Fail-closed**：无活动Registration、Package/必带工具链漂移、Guide未验证或定义无法绑定时Locator/Stage 4分别按合同停止，spawn为0；不选择备用Package。
- **上下游**：上游为T1/T2；下游为T4 Stage 4适配和T6结果映射；Stage 4不能跳过本顺序。

#### T4：Stage 4调用适配

- **目标**：把已验证事实传给一个已接受的Stage 4调用，不复制其控制面。
- **权威输入**：Stage 4正式固定签名、`PackageToolDefinitionV1`和`LauncherReceiptV1`合同；T2输入；T3同次Locator事实。
- **具体动作**：只调用`launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)`；`user_message`原样传递；定义声明本地能力时原样传递完整approved capability definition和未改写original Stage 3 fact；Stage 5不生成命令、argv、Shell字符串、stdin替代包或本地能力摘要。
- **输出**：Stage 4原样的递归不可改写`LauncherReceiptV1`，以及Stage 5可呈现的事实引用；固定工具至多一次spawn由Stage 4负责。
- **未来文件/物理承载**：未来最多一个Stage 5生产模块/入口适配器；不新增Launcher、命令构造器、MCP桥或第二进程；实际调用物理承载依赖T1且当前`UNFROZEN_PENDING_T1`。
- **验收**：函数参数域分离、完整事实无摘要重包装、Stage 4定义/源语义自验证；Stage 5自身spawn=0且不含Shell字符串；Stage 4仍`spawn<=1/retry=0`。
- **Fail-closed**：定义缺失/不匹配、能力证据缺失/漂移、输入跨域或协议不确定时不伪造调用；由Stage 4既定九值/11级优先级裁决，不由Stage 5重排。
- **上下游**：上游为T2/T3；下游为T5授权、T6映射、T11回执转交。

#### T5：用户授权、暂停与同任务继续

- **目标**：把能力、外部服务、网络/下载和费用授权拆开，并保证拒绝/暂缓不被伪装成失败或自动重放。
- **权威输入**：Stage 3五结果/逐能力`capability+definition_sha256+plan_sha256`批准合同；Package Guide的实际要求；WorkBuddy会话与用户授权；Stage 4 cancel/continuation边界。
- **具体动作**：每个可选能力、外部服务和费用独立询问；批准绑定definition、plan、session，校验当前事实仍一致；`decline/defer`走基础或其他已有能力路径；同任务继续优先由真实WorkBuddy完成，客户端不支持时固定提示“继续刚才的任务”；Shell不保存、不自动重放原业务请求。
- **输出**：逐项授权/拒绝/暂缓事实、绑定身份、失效原因、继续提示或用户可见的暂停状态。
- **未来文件/物理承载**：授权只保留在当前WorkBuddy受控会话和本次调用域；不建授权数据库、不把原请求落盘成可重放队列，不写Provider目录。
- **验收**：定义/计划/session或探测事实任一变化使批准失效；拒绝/暂缓能继续基础能力（若Package/用户业务允许）；取消与继续不改变原话、不多spawn。
- **Fail-closed**：授权缺失、过期、definition/plan不一致、费用未授权或客户端继续语义不明时暂停并提示；不得静默替代Provider、自动重试或声称无缝继续。
- **上下游**：上游为T3/T4和WorkBuddy用户对话；下游为T6结果动作、T7凭据注入和真实验收第7层。

#### T6：结果到用户动作映射

- **目标**：为Stage 3五结果和Stage 4九种Launcher outcome建立闭集映射，保持错误事实和业务语义不变。
- **权威输入**：Stage 3结果闭集`DETECTION_REPORT/CONSENT_REQUIRED/INTEGRATED/SKIPPED/BLOCKED`；Stage 4九值`PRELAUNCH_BLOCKED/SPAWN_FAILED/EXITED_SUCCESS/EXITED_NONZERO/CHILD_REPORTED_FAILURE/TIMED_OUT/CANCELLED/INCOMPLETE/RESIDUAL_PROCESS`及其11级优先级；用户授权事实。
- **具体动作**：只展示事实、展示计划并询问、报告准备完成、报告阻断/取消/超时/失败/泄密/残留或返回结果指针；不解释Artifact业务含义、不改变Stage 4 outcome/reason、不自动重试。
- **输出**：用户动作矩阵和可审计原始receipt/Stage 3事实；下游可直接消费的状态，不新增平行状态服务。
- **未来文件/物理承载**：优先在唯一入口适配层作确定性映射；若Stage 6能直接消费则不新增文件；不得建立解释器、任务库或结果数据库。
- **验收**：
  - `DETECTION_REPORT`：展示两能力事实，不替OpenMontage选能力；`CONSENT_REQUIRED`：展示绑定计划并逐项询问；`INTEGRATED`：报告已验证就绪但不宣称已被生产使用；`SKIPPED`：报告`NOT_INTEGRATED`并继续其他/基础能力；`BLOCKED`：报告无效定义或已授权集成失败，能力单纯缺失不误报。
  - `PRELAUNCH_BLOCKED`：展示安全阻断原因，未spawn的请求终止；若仅是可选能力未满足，只能由WorkBuddy在用户明确选择后形成新的基础能力请求；`SPAWN_FAILED`：报告启动失败；`EXITED_SUCCESS`：仅返回有效结果指针；`EXITED_NONZERO`：报告真实非零退出；`CHILD_REPORTED_FAILURE`：报告child明确失败；`TIMED_OUT`：报告超时；`CANCELLED`：报告取消；`INCOMPLETE`：报告证据/输出不完整或secret disclosure；`RESIDUAL_PROCESS`：报告残留进程阻断。九值均不改写为成功。
- **Fail-closed**：任何未列举映射、优先级竞争、缺receipt字段或业务解释需求停止；Stage 4既定11级优先级不得被Stage 5覆盖。
- **上下游**：上游为T3-T5和Stage 3/4；下游为T10证据分层与T11 Stage 6。

#### T7：凭据与隐私边界

- **目标**：保证Provider secret只到达PackageToolDefinition允许的child环境，不进入用户对话或任何非授权域。
- **权威输入**：Stage 4 secret-nondisclosure合同；T2 `provider_environment`；当前Release工具定义allowlist；WorkBuddy单独Provider/费用授权。
- **具体动作**：仅传递定义allowlist中的环境变量名和值；secret只进入固定child环境；在生成message、stdin、receipt、日志和异常前建立secret source并做provenance-aware non-propagation检查；Key存在不等于能力可用、调用成功或费用授权；Provider选择和回退由WorkBuddy/OpenMontage已验证Package合同决定，Shell不推荐/排序/回退。
- **输出**：allowlisted环境名、授权状态和安全receipt；secret原文永不出现在chat、`user_message`、argv、stdin非授权域、日志、receipt或错误文本。
- **未来文件/物理承载**：不建立Provider配置仓库、密钥数据库或日志服务；值只存在当前调用的child环境和必要内存生命周期。
- **验收**：非空secret进入唯一授权sink；任一日志/receipt/error/stdin/argv传播为0；无授权Provider不调用；配置缺失不被解释为Stage 3能力缺失。
- **Fail-closed**：环境名越权、值传播、无法证明来源、child输出泄密或费用授权缺失时阻断；不以hash、长度、摘要或固定常量掩盖传播。
- **上下游**：上游为T2/T5；下游为T4 Stage 4 child、T6安全错误映射和真实验收第9层。

#### T8：失败闭集与优先级

- **目标**：为用户列出的15类失败固定Locator/Stage 4/spawn/用户结果/基础能力/全请求终止裁决；不创造第二套优先级。
- **权威输入**：Stage 2 Locator合同；Stage 4九值和11级优先级；T2-T7闭集；用户授权状态。
- **具体动作与输出**：按下表机械映射。`Stage4=是`表示调用已接受API后由Stage 4返回阻断/结果；Stage 5不自行spawn。任何“可继续基础能力”都要求WorkBuddy在用户明确选择后形成新的请求，绝不自动重放原话。

| 失败类别 | Locator | Stage 4 | spawn | 用户结果 | 基础能力继续 | 终止当前请求 |
|---|---:|---:|---:|---|---|---:|
| 无活动Registration | 是 | 否 | 0 | `PRELAUNCH_BLOCKED/LOCATOR_FAILED`，提示Package不可用 | 否 | 是 |
| Package或必带工具链漂移 | 是 | 否 | 0 | 身份漂移阻断，提示重新安装/修复 | 否 | 是 |
| Guide未验证 | 是 | 否 | 0 | Guide读取前阻断 | 否 | 是 |
| PackageToolDefinitionV1缺失或不匹配 | 是 | 是（preflight） | 0 | `PRELAUNCH_BLOCKED/TOOL_DEFINITION_UNBOUND`或精确reason | 仅当WorkBuddy另行选择不需该定义的基础请求 | 是 |
| 用户输入非法 | 否（入口闭集先拒绝） | 否 | 0 | 输入无效，要求修正；不暴露内部合同 | 可在用户修正后重新提交，不自动继续 | 是 |
| 可选能力证据缺失或漂移 | 是 | 是（preflight） | 0 | `LOCAL_CAPABILITY_EVIDENCE_REQUIRED/MISMATCH` | 用户明确改走基础能力时可新请求 | 是 |
| Provider配置未授权 | 是 | 否（入口授权门禁） | 0 | 告知需单独授权；不调用Provider | 是（不需要该Provider时） | 否，暂停该分支 |
| 用户拒绝或暂缓 | 是（如已完成探测） | 否（对应可选能力） | 0 | `SKIPPED/NOT_INTEGRATED`，展示继续选项 | 是，其他/基础能力继续 | 否；若业务硬依赖则由WorkBuddy报告无法完成 |
| 入口前取消 | 否 | 否 | 0 | `CANCELLED/CANCELLED_BEFORE_SPAWN`语义 | 否 | 是 |
| 启动失败 | 是 | 是 | 0 | `SPAWN_FAILED/SPAWN_OS_ERROR` | 否；不得自动重试 | 是 |
| child报告失败 | 是 | 是 | 1 | `CHILD_REPORTED_FAILURE`，保留child事实 | 仅用户明确新计划时 | 是 |
| timeout | 是 | 是 | 1 | `TIMED_OUT/TIMEOUT`，保留终止/残留事实 | 否；不得重放 | 是 |
| secret disclosure | 是 | 是 | 1 | `INCOMPLETE/SECRET_DISCLOSURE_DETECTED`，仅安全抑制摘要 | 否 | 是 |
| result pointer非法 | 是 | 是 | 1 | `INCOMPLETE/RESULT_POINTER_INVALID`，不返回伪成功指针 | 否 | 是 |
| 残留进程 | 是 | 是 | 1 | `RESIDUAL_PROCESS/RESIDUAL_PROCESS_DETECTED` | 否；等待人工/治理处理 | 是 |

Stage 4已接受的11级优先级（invalid input、pre-cancel、preflight、spawn fail、residual、secret、timeout/cancel、nonzero、invalid output、child failed、success）优先于本表用户呈现；本表不重排、不覆盖、不把失败解释为Artifact业务失败。

- **验收**：15类每类都有Locator/Stage4/spawn/用户结果/基础继续/终止字段；冲突分支按Stage 4优先级；任何未定义失败为`INCOMPLETE/EVIDENCE_INCOMPLETE`或对应既定reason，不得成功。
- **Fail-closed**：出现第16类未分类失败、没有最终退出、对象/证据不一致或需要自动重试时停止并返回`INCOMPLETE`/`STOPPED_SCOPE_EXPANSION`。
- **未来文件/物理承载**：失败映射只存在唯一入口和回执呈现边界；不新增失败服务、队列、数据库或重试器。
- **上下游**：上游为T1-T7、Stage 2/4合同；下游为T10分层证据和T12直接负面测试。

#### T9：最终Package Gate关系

- **目标**：把规划、受控fixture和真实生产Package身份分层，避免临时Package或缺定义被误报为生产PASS。
- **权威输入**：`PACKAGE-REGISTRATION-CONTRACT.md`、当前`PROJECT-STATE.md`和验收矩阵；Stage 4 release-specific `PackageToolDefinitionV1`规则。
- **具体动作**：规划不要求最终Package已物化；未来代码/fixture可以使用受控测试Package验证输入/Locator/定义绑定，但必须标记fixture；真实WorkBuddy生产验收前必须完成最终Package物化、安装、production Registration/Activation和新进程Locator验证；真实调用缺具体Release定义实例时必须preflight fail closed。
- **输出**：三个独立状态`FINAL_PACKAGE_MATERIALIZED`、`PRODUCTION_PACKAGE_REGISTERED`和`TOOL_DEFINITION_BOUND`；当前仍为`NOT_MATERIALIZED/NOT_CREATED/未绑定具体实例`。
- **未来文件/物理承载**：最终Package由后续最终交付/Installer任务承载；Stage 5入口模块不得物化、安装、登记、激活或写PackageRoot。
- **验收**：fixture只证明合同可实例化；生产验收必须有持久Release、安装Root、Registration/Activation、新进程Locator和当前Release定义全套身份；任何一层缺失不启动真实生产。
- **Fail-closed**：把临时ZIP、静态Guide、旧V1 Skill、Stage 4单测或目录名当生产对象时立即停止并纠正状态。
- **上下游**：上游为Stage 2/最终Installer；下游为T10真实证据第8层、未来T12实施前置和真实Stage 5验收。

#### T10：真实验收与证据分层

- **目标**：让每一层证据只裁决自己的问题，前层PASS永远不能替代后层。
- **权威输入**：验收矩阵独立状态定义、Stage 2/3/4已接受边界、真实WorkBuddy授权卡和T1合同。
- **具体动作与输出**：分别记录以下10层：`(1)`静态合同审查；`(2)`单元/负面测试；`(3)`Stage 2/3/4接口集成测试；`(4)`真实腾讯WorkBuddy新会话；`(5)`唯一入口命中；`(6)`literal `user_message`不变；`(7)`用户授权与同任务继续；`(8)`最终Package生产身份；`(9)`真实Provider或媒体证据；`(10)`业务效果。每层记录对象、命令/动作、最终exit、输出、时间和边界。
- **未来文件/物理承载**：静态/测试证据留在未来任务审查包；真实客户端证据只在受控D盘证据目录和正式验收卡中保存；不在代码中伪造生产/业务结果。
- **验收**：每层可独立给`PASS/FAIL/BLOCKED/INCOMPLETE/NOT_TESTED/NOT_APPLICABLE`；真实Provider、媒体、成片和业务效果不由Stage 5单测宣称完成。
- **Fail-closed**：缺对象、输出截断、无最终exit、客户端状态不明、跨层代替或历史证据混用时保持`INCOMPLETE/NOT_PROVED`，不升级下一层。
- **上下游**：上游为T1-T9；下游为T12 Reviewer/正式验收和未来Stage 6裁决。

#### T11：Stage 6不断档

- **目标**：只冻结Stage 5向Stage 6交付的真实事实，不提前建设第二个结果系统。
- **权威输入**：Stage 4递归不可改写`LauncherReceiptV1`；Stage 3五结果；真实Stage 5消费者字段需求（尚未证明）。
- **具体动作**：Stage 6首先尝试直接复用同一`LauncherReceiptV1`和Stage 3事实；只有真实消费者存在明确字段转换缺口时才提出一次确定性转换；本阶段不预建任何Stage 6代码。
- **输出**：若无缺口，固定为`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`、`production code changes=0`；若有缺口，提交真实字段差异、唯一消费者和单一转换方案，另行授权。
- **未来文件/物理承载**：当前为零文件、零模块、零服务；不得预建状态数据库、轮询器、解释器或重试器。
- **验收**：事实、错误、取消、超时、残留和结果指针原样可追溯；没有业务Artifact解释或成功改写。
- **Fail-closed**：没有真实Stage 5消费者、无法证明格式缺口或直接消费可行时，保持零代码，不假设需要转换。
- **上下游**：上游为T4/T6的Stage 4 receipt和Stage 3事实；下游是未来独立Stage 6授权。

#### T12：未来Stage 5实施任务包

- **目标**：把未来实现授权所需的身份、基线、文件、测试、审查和推广规则冻结，同时诚实保留T1未闭合导致的未冻结项。
- **权威输入**：本节T1-T11；届时实时`origin/codex/workbuddy-shell-v2`；用户后续明确原话“启动阶段五实施”；T1最终入口合同；Stage 2/3/4合同和正式状态。
- **具体动作**：未来唯一Builder ID固定为`V2-S5-WORKBUDDY-ENTRY-BUILDER1`；接管时重新解析实时formal HEAD/tree/tracked，不能直接使用历史SHA、main、旧长期分支或当前规划分支；先核验干净状态和精确白名单，再创建D盘独立临时worktree/branch。公共入口固定为1，新增生产模块上限为1，直接测试文件固定为1；Stage 6不预建。
- **输出**：T1闭合后才能写入的实施任务包：精确入口资产路径、最多一个生产模块、一个直接测试、必要的单次`__init__.py`导出、CI现有命令的最小更新（如确有消费者需求）、tracked `37 -> N`和固定命令。当前这些字段必须是`UNFROZEN_PENDING_T1`，不能伪造路径、N或命令。
- **未来文件/物理承载**：实施最多承载一个真实WorkBuddy入口资产、一个生产模块、一个直接测试；`__init__.py`仅在T1证明需要时允许；CI是否修改、具体路径、物理安装归属和包结构全部待T1。若需要第N+1个路径，立即停止并回到用户重新授权。
- **验收**：实施前必须有“启动阶段五实施”明确授权；精确base/tree/tracked与formal等值；Builder只改白名单；项目D盘私有`.venv`；直接测试、hygiene、完整测试按冻结命令最终exit 0；`git diff --check`、tracked/clean/untracked/stash等值；Reviewer独立零写比较base..candidate；只有`APPROVE/P0=0/P1=0/P2=0`且formal仍等于base才可普通fast-forward。
- **Fail-closed**：T1未闭合、授权缺失、对象/路径/tracked不符、命令需猜测、需要第N+1路径、测试无最终exit、Reviewer非APPROVE或正式分支已前移时停止；不force push、不merge/rebase、不推广、不自动开启Stage 6。
- **上下游**：上游是T1闭合、Stage 2/3/4已接受合同和未来用户授权；下游是唯一Builder、独立Reviewer、普通FF及真实Stage 5验收。规划被接受也不等于实现被授权。

### 4. 规划交付与治理出口

本候选只允许三条路径：`docs/workbuddy/v2/TASK-REGISTER.md`、`docs/workbuddy/v2/PROJECT-CHARTER.md`、`docs/workbuddy/v2/ACCEPTANCE-MATRIX.md`。Builder不修改正式分支、不运行测试（`test=NOT_RUN_DOCS_ONLY`）、不运行真实WorkBuddy/Launcher/Provider/媒体/WSL、不物化Package、不创建Registration、不启动Stage 6。候选必须以单一临时分支非force push，报告base/candidate/tree/三路径/status；独立零写Reviewer只审文档准确性和范围，不得把产品规划变成`PASS_ACCEPTED`。

Reviewer至少核对：WorkBuddy是否仍是唯一Agent；是否只有一个真实入口；是否错误预建CLI/MCP/第二Agent；是否硬编码Provider/Runtime；是否保持literal message与controls分离；是否完整消费Stage 2/3/4合同；是否区分最终Package与生产验收；是否含T1-T12和15类失败矩阵；是否保持Stage 6零代码出口；是否存在产品或文档范围膨胀。P0为架构/安全/权限/身份绕过或泄密；P1为可执行合同、映射、证据或边界缺口；P2为不影响合同的表述问题。只有`APPROVE / P0=0 / P1=0 / P2=0`才允许后续治理普通fast-forward；REQUEST_CHANGES只能回原Builder。

候选经Reviewer批准和普通fast-forward后，只正式固化这三份规划文档，不因此把Stage 5规划记为`PASS_ACCEPTED`；只要T1合同证据未闭合，当前状态仍必须保持`PLANNING_BLOCKED_EXTERNAL_CONTRACT`。只有未来T1合同证据闭合、完成独立审查并经过另行权威状态收口后，才能评估Stage 5规划是否达到`PASS_ACCEPTED`；该评估仍不授权Stage 5实现。当前仍须保持`stage_5_implementation_authorization=NOT_GRANTED`、`next_authorized_task=NONE`。下一步不是自动写代码，而是先完成独立零写文档审查、普通FF和临时现场清理；之后若要进入实施，用户必须另行明确“启动阶段五实施”，再按T12重新接管实时formal对象。
