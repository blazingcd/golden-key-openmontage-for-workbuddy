# WorkBuddy Shell V2 任务账本

状态：`STAGE_4_IMPLEMENTATION_PASS_ACCEPTED / FINAL_HANDOFF_HYGIENE_PASS_ACCEPTED / STAGE_5_IN_PROGRESS_ENTRY_CODE_COMPLETE_REAL_INTEGRATION_INCOMPLETE / R01_ENTRY_SURFACE_ACCEPTED / R02_BLOCKED_PACKAGE_RELEASE / NO_NEXT_AUTHORIZED_TASK`

更新时间：2026-08-22

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
stage_5_planning_authorization_history: V2-S5-PLANNING-AUTHORIZATION-BUILDER1 / DOCS_ONLY / CONSUMED_COMPLETE / HISTORICAL_BEFORE_V2-S5-T1-EVIDENCE1-CLOSEOUT-AND-CONTROLLED-CLIENT-AUTHORIZATION1
stage_5_planning_authorization_history_base: 67e39b345df954898a68c9c14645c9c04c380ac3 / tree c6bf74231434850fda07722ab9eed701797e48ff / tracked 37
stage_5_planning_authorization_history_branch: codex/v2-s5-planning-authorization1
stage_5_planning_authorization_history_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md
stage_5_planning_authorization_history_result: 042686039386a63866eba2f964f1fa9674bbec4b / ordinary fast-forward / origin/codex/workbuddy-shell-v2 / HISTORICAL_BEFORE_V2-S5-T1-EVIDENCE1-CLOSEOUT-AND-CONTROLLED-CLIENT-AUTHORIZATION1
stage_5_planning_authorized_next_task_history: V2-S5-PLAN-BUILDER1 / CURRENT_DOCS_ONLY_CANDIDATE / CONSUMED_COMPLETE / HISTORICAL_BEFORE_V2-S5-T1-EVIDENCE1-CLOSEOUT-AND-CONTROLLED-CLIENT-AUTHORIZATION1
stage_5_planning_next_task_allowed_paths_history: docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md / CONSUMED_COMPLETE / HISTORICAL_BEFORE_V2-S5-T1-EVIDENCE1-CLOSEOUT-AND-CONTROLLED-CLIENT-AUTHORIZATION1
stage_5_planning_next_task_kind_history: DOCS_ONLY / no production code / tests / CI / Package / real WorkBuddy / Launcher / Provider / media / WSL / CONSUMED_COMPLETE / HISTORICAL_BEFORE_V2-S5-T1-EVIDENCE1-CLOSEOUT-AND-CONTROLLED-CLIENT-AUTHORIZATION1
initial_product_goal_recheck: PASS / WorkBuddy is the only running Agent and the only user entry; after loading the verified Package Guide it assumes the OpenMontage logical production role
stage_5_t1_cli_boundary: CLI_NOT_A_BLANKET_BAN / forbid a second entry, parallel control plane, fallback, or arbitrary command/argv/Shell generation; a fixed CLI used internally by the one official WorkBuddy Skill remains eligible for controlled contract verification
stage_5_planning_t1_hard_stop: HISTORICAL_EXTERNAL_CONTRACT_STOP / superseded for the external-mechanism question; never fabricate an interface or use CLI/MCP/second-Skill fallback, and do not treat CLI presence alone as architecture unavailability
stage_5_planning_t1_current_state: HISTORICAL_PRE_ENTRY_IMPLEMENTATION / T1_EXTERNAL_MECHANISM_CONFIRMED / INTERNAL_FIXED_CLI_BRIDGE_FROZEN_FOR_PLANNING
stage_5_t1_evidence2_result_candidate: HISTORICAL_ARCHITECTURE_CONTRACT_UNAVAILABLE / SUPERSEDED_BY_CLI_BOUNDARY_CORRECTION / OFFICIAL_SOURCES_PLUS_READ_ONLY_CLIENT / CANDIDATE_UNTIL_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD / FORMALLY_PROMOTED_WHEN_THIS_COMMIT_IS_FORMAL
stage_5_t1_evidence2_result_candidate_base: 4515268d1f77211a14f22927a02344b578527c4a / tree 45b351bbf60419dc76833ddfcd61cd2ef52ff24c / tracked 37
stage_5_t1_evidence2_result_candidate_scope: EXACT_2_DOC_PATHS / NO_CODE / NO_TEST / NO_CI / NO_EXTERNAL_OBJECT
stage_5_t1_evidence2_authorization_history: V2-S5-T1-CONTRACT-CLOSURE-EVIDENCE2 / DOCS_ONLY / CONSUMED_BY_CANDIDATE_RESULT / FORMALLY_CONSUMED_WHEN_THIS_COMMIT_IS_FORMAL
stage_5_t1_evidence1_candidate_result: d11513907c3662b18fd06a200fac935efcb50055 / tree 81e38bc90dd37d586b46e20cc047db35b613759d / T1_EVIDENCE_INCOMPLETE
stage_5_t1_evidence1_independent_review: APPROVE / P0=0 / P1=0 / P2=0
stage_5_t1_evidence1_formal_promotion: ORDINARY_FAST_FORWARD / FORMALLY_PROMOTED
stage_5_t1_evidence_candidate: T1_EVIDENCE_INCOMPLETE / OFFICIAL_SOURCES_ONLY / CLIENT_NOT_AUTHORIZED / FORMALLY_PROMOTED
stage_5_t1_evidence_candidate_base: 44d89625c1fd71d07d1173e18681e64e7459cec2 / tree 10c8c4187299564fc83cef38a3f9ac65f4f9790a / tracked 37
stage_5_t1_evidence_candidate_scope: EXACT_4_DOC_PATHS / NO_CODE / NO_TEST / NO_CI / NO_EXTERNAL_OBJECT
stage_5_planning: PASS_ACCEPTED
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
stage_5_entry_code_task: V2-S5-WORKBUDDY-ENTRY-BUILDER1 / CONSUMED_COMPLETE / ENTRY_CODE_COMPLETE
stage_5_entry_code_formal_result: 0e7a0be65877b03fb386e1c6c6bc258c0b27db6c / tree 85c266edb7349c940e8cd45870cc0538c95726c0 / parent aa70c2cf9b6b4a29517d7354f0239ea0cdc9a5d3
stage_5_entry_code_scope: EXACT_5_PATHS / tracked 37->40
stage_5_entry_code_review: APPROVE / P0=0 / P1=0 / P2=0
stage_5_entry_code_windows_evidence: direct 19 passed / hygiene 11 passed / full 377 passed / final exit 0
stage_5_entry_code_ci: run 32489111184 / completed / success / headSha=0e7a0be65877b03fb386e1c6c6bc258c0b27db6c / Ubuntu / Python 3.14.7 / 376 passed / 1 skipped / final exit 0
stage_5_entry_closeout: V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1 / FORMALLY_DELIVERED_DOCS_ONLY / NOT_STAGE5_PASS
stage_5_implementation_authorization: ENTRY_CODE_RESULT_CONSUMED / R00_CONSUMED / R01_ENTRY_SURFACE_ACCEPTED / R02_BLOCKED_PACKAGE_RELEASE / EXECUTION_PROOF_DEFERRED_TO_R03_R07
stage_5_implementation: ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
current_task: NONE / NO_ACTIVE_TASK / R02_CLOSED_BLOCKED_PACKAGE_RELEASE
current_task_status: BLOCKED_PACKAGE_RELEASE / PUBLISHED_CANDIDATE_IDENTITY_VERIFIED / DOCS_ONLY_R02_CLOSEOUT
next_authorized_task: NONE / PACKAGE_OWNER_RELEASE_BINDING_REAUTHORIZATION_REQUIRED
next_planned_task: NONE / R03-R08_NOT_STARTED_NOT_AUTHORIZED_BY_CHAIN
stage_5_t1_evidence_authorization_history: V2-S5-T1-EVIDENCE1-CLOSEOUT-AND-CONTROLLED-CLIENT-AUTHORIZATION1 / DOCS_ONLY / CONSUMED_COMPLETE / FORMALLY_PROMOTED
stage_5_t1_controlled_client_evidence_candidate: HISTORICAL_V2-S5-T1-CONTROLLED-CLIENT-EVIDENCE1 / WORKBUDDY_5.3.13 / SUPERSEDED_BY_R01
stage_5_t1_controlled_client_proved: ORIGINAL_R01 / WORKBUDDY_5.3.14 / BASELINE_SKILLS_2_RETAINED / SAFETY_SCAN_NOT_SKIPPED / TEMP_PROBE_INSTALLED_COUNT_3 / EXACT_IDENTITY=golden-key-openmontage-r01-controlled-probe_APPEARED / ISOLATED_TASK_ATTACHED_SOLE_PROBE / HY3_SELECTED / NO_NATIVE_EVENT / NO_SCRIPT_EXECUTION / NO_STDOUT_STDERR_EXIT_CWD_TIMEOUT
stage_5_t1_controlled_client_unproved: native bundled-script invocation/tool event; script stdout/stderr/final exit/cwd/timeout capture; real LauncherReceiptV1
stage_5_t1_controlled_client_cleanup: COMPLETE / USER_UNINSTALLED_TEMPORARY_SKILL / WORKBUDDY_INSTALLED_SKILLS_2 / TASK_HISTORY_RETAINED / BASELINE_SKILLS_2_UNTOUCHED / PROBE_FOLDER_AND_ZIP_DELETED
pending_next_authorized_task: NONE
next_authorized_task_condition: R02_BLOCKED_PACKAGE_RELEASE / current_task=NONE / NO_ACTIVE_TASK / next_authorized_task=NONE; only a separate Package-owner task may approve Release delivery and independently verify safe fixed tool + release-specific PackageToolDefinitionV1 + Manifest/Lock binding, after which R02 must be separately reauthorized; R03-R08 remain strict-order and unauthorized
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
stage_6_status_result_relay_authorization: NOT_GRANTED
final_package_gate_authorization: NOT_GRANTED
final_package_artifact: NOT_MATERIALIZED
production_package_root: NOT_CREATED
production_registration_activation: NOT_CREATED
final_installed_skill: NOT_CREATED
real_workbuddy_launcher_receipt: NOT_PROVED
production_evidence_boundary: real WorkBuddy/Launcher session; final Package/PackageRoot/Registration/Activation; final installed Skill; Provider/media; Stage6 remain unproved or not created
```

该自解析记录不重新门禁Stage4 `PASS_ACCEPTED`，也不形成新的产品任务。六路径最终交接卫生结果`4636e27a62aad9f1b721e6c482e34b44d350503c`已经独立Reviewer最终`APPROVE / P0=0 / P1=0 / P2=0`、普通fast-forward和正式CI验证；该收口的历史状态（`HISTORICAL_BEFORE_V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE-AUTHORIZATION1`）是`current_task=NONE / current_task_status=NO_ACTIVE_TASK / historical_next_authorized_task=NONE`。2026-08-21的Stage5规划授权候选及其生效条件见下节；任何Stage5实现、Stage6或最终Package权限仍不得从本收口推导。

## [历史] Stage 5 T1 CLI边界纠偏与目标回读门禁（2026-08-21）

本节是对上一轮 `V2-S5-T1-CONTRACT-CLOSURE-EVIDENCE2` 候选的 **历史 superseding docs-level correction**。历史证据、候选提交和当时的 `ARCHITECTURE_CONTRACT_UNAVAILABLE` 文字均保留，不伪造或重写历史；本节只纠正当时把“CLI/MCP 不满足必要条件”误读成“CLI 一概禁止”的解释。它不再表示当前 live 阻断；当前覆盖以本账本下方 `V2-S5-T1-SKILL-CLI-CONTRACT-REASSESSMENT1` 节为准。

```text
initial_product_goal_recheck: PASS
initial_product_goal: Tencent WorkBuddy is the only running Agent and the only user entry; after loading the verified Golden Key OpenMontage Package Guide, WorkBuddy assumes the OpenMontage logical production role
product_goal_priority: product goal and official evidence outrank a candidate implementation preference
cli_rule: CLI is not prohibited merely because it is CLI
cli_allowed_condition: an officially supported fixed CLI may be an internal bridge invoked by the one WorkBuddy Skill, only if it remains within that Skill's single-entry/single-consumer contract and is directly evidenced and frozen
cli_forbidden_conditions: second user entry; parallel control plane; second Agent; fallback after an unsupported contract; arbitrary command/argv/Shell generation; unbounded intent interception; automatic retry/replay
mcp_rule: MCP is not an authorized second entry or parallel control plane; no MCP bridge is assumed without separate official contract evidence
t1_reopened_decision: REASSESS_OFFICIAL_SKILL_PLUS_FIXED_CLI_UNIQUE_ENTRY_CONTRACT
t1_blocker_meaning: HISTORICAL_ONLY / PLANNING_BLOCKED_EXTERNAL_CONTRACT was the pre-reassessment interpretation; it never meant the product or an internal fixed CLI bridge was impossible
t4_direct_python_rule: accepted Stage 4 implementation and launch_session_tool(...) contract remain PASS_ACCEPTED; direct Python is the current Stage 5/T1 consumption candidate; if official evidence identifies a fixed internal CLI bridge, compare and reconcile the Stage 5 binding under T1 rather than reopening or denying Stage 4 or the product goal
t4_preserved_boundary: Stage 5 still must not generate arbitrary command/argv/Shell strings or create a second control plane; any fixed bridge must be consumed only as its evidenced contract
stage_5_implementation_authorization: NOT_GRANTED
historical_next_authorized_task_after_correction: V2-S5-T1-SKILL-CLI-CONTRACT-REASSESSMENT1 / only after this historical correction was independently approved and ordinarily fast-forwarded
next_task_scope: reread initial product goal; recheck official Skill plus fixed-CLI internal bridge and its unique consumer/entry boundary; reconcile with Stage 4 without code or production execution
next_task_forbidden: second entry; second Agent; CLI/MCP fallback or parallel control plane; arbitrary command/argv/Shell; code; tests; CI; Provider; media; Package; Registration; Stage4 real spawn; Stage6
recheck_gate_for_every_future_stage5_task: initial_product_goal_recheck=PASS is mandatory before task start, evidence裁决, or implementation decision
```

该历史纠偏不使 Stage 5 规划或实现自动 `PASS_ACCEPTED`，也不授权真实 WorkBuddy/Stage 4/Provider/媒体/Package/Stage 6。当前外部机制阻断已由官方 `Skill + CLI` 资料和既有 HY3 exact Skill 会话在下方当前 T1 重新评估中解除；当前为 `IN_PROGRESS / T1_INTERNAL_BRIDGE_CONTRACT_PENDING`。本节只记录错误解释如何被纠正，不覆盖当前状态。

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

历史规划授权中的 T1 外部合同门禁文字仅适用于历史候选，现由当前 T1 重新评估 supersede：外部机制已确认，当前不是 `PLANNING_BLOCKED_EXTERNAL_CONTRACT`；当前为 `IN_PROGRESS / T1_INTERNAL_BRIDGE_CONTRACT_PENDING`。不可漂移的禁止项仍是第二入口、并行控制面、第二 Agent、CLI/MCP 兜底、任意命令/argv/Shell 生成和自动重试/重放；不得把 CLI 本身当成产品不可能或架构不可用。

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

state_record_scope: HISTORICAL_BEFORE_V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE-AUTHORIZATION1
current_task: NONE
current_task_status: NO_ACTIVE_TASK
historical_next_authorized_task: NONE
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

T1到T4是同一个单生产模块内的私有实现职责，不得为了任务编号拆成新模块。T5/T6只提供直接证据和固定仓库门禁。T7完成后Stage4仓库实现才可收口；当前Stage5整体为`IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`，真实WorkBuddy最终集成和Stage6仍保持未授权/未证明。

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

## 历史正式状态快照（HISTORICAL_BEFORE_V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE-AUTHORIZATION1）

```text
formal_ref: refs/heads/codex/workbuddy-shell-v2
formal_head_resolution: LIVE_REMOTE_REF_REQUIRED
formal_tree_resolution: LIVE_REMOTE_REF_TREE_REQUIRED
mirror_result: THIS_COMMIT
mirror_effect: ZERO_PRODUCT_STATE_CHANGE
mirror_repository_delivery_resolution: zero-write APPROVE exists AND LIVE_REMOTE_REF contains THIS_COMMIT
state_record_scope: HISTORICAL_BEFORE_V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE-AUTHORIZATION1
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
historical_next_authorized_task: NONE
effective_stage_4_launcher_authorization: NOT_GRANTED
effective_stage_5_workbuddy_entry_authorization: NOT_GRANTED
effective_stage_6_status_result_relay_authorization: NOT_GRANTED
effective_final_package_gate_authorization: NOT_GRANTED
stage_3_to_6_scope_reduction: ACTIVE_REPLANNED_BOUNDARY
runtime_correction: REQUIRED_TOOLCHAIN_REFRESH_PASS_ACCEPTED
```

`709c8e880b144fa9e9be26e9feb5d776dd6025e2`完成了Stage 2必带工具链和Registration/Locator的真实临时证明；该历史事实不重开，也不再作为Stage 3输入。Stage 3实现已经独立审阅并正式推广为`a3f8959682d296301dc573c2835f8c705a52e8b2`，closeout `7c15aae4e77c579309312b21c79076f930970214`也已正式推广，因此Stage 3继续为`PASS_ACCEPTED`。

CI状态断言修复`e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3`已经位于正式分支，精确代码差异仅为`tests/workbuddy/test_repository_hygiene.py`中的两条Stage3状态断言；正式CI run `32218904419`为`completed/success`，输出`198 passed / 1 skipped`。第一次独立Reviewer结论保持为`INCOMPLETE / P0=0 / P1=0 / P2=0`，原因只有当时authority mismatch，代码差异无finding。正式分支在账本收口前前移属于治理偏差，本closeout只同步实时权威，不改写审查或Git历史。

CI状态断言closeout已在`26bfe60ab9da62797559eb9a459b8daa345f8d80`正式收口。Stage4规划最终结果`5cb3f585a0cddffbd823c785b1d39ebd1834c1df`及规划closeout `dfd97f3d2e05a4c448448fc14514d1cfe76836e8`均已独立审查、普通fast-forward并由正式CI验证，因此`stage_4_planning=PASS_ACCEPTED`。实施结果`fa9adb8470ab94b88ec9900ede03cb26f7de0ebd`经第八轮独立审查`APPROVE / P0=0 / P1=0 / P2=0`进入formal；run `32367792637`随后只暴露测试夹具错误假定GitHub `setup-python`存在`pyvenv.cfg`，不是生产Launcher缺陷。单测试路径修复`13a3227b0c55bbe9039b46d7e92eba822b48f57e`也经独立审查`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward，正式Ubuntu CI run `32369588814`为`357 passed / 1 skipped / exit 0`。Stage4 closeout固定历史锚点`b63d8c2bc2214bc39f18378dbe47057ef538301e`、tree `02814c6a4a483913e7b1abe3e9ee6d025236c951`已经`V2-S4-IMPLEMENTATION-CLOSEOUT-REVIEW1`独立`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward，closeout CI run `32371507874`在Ubuntu 24.04 / Python 3.11.16上`357 passed / 1 skipped`，因此Stage4实现已是`PASS_ACCEPTED`。原三路径卫生尝试因发现三个额外陈旧当前入口文档而在零worktree、零修改、零测试、零提交/推送且WSL未启动的安全节点停止；该历史`INCOMPLETE`已由修订授权和正式六路径结果`4636e27a62aad9f1b721e6c482e34b44d350503c`闭合。最终卫生结果经独立`APPROVE / P0=0 / P1=0 / P2=0`及正式CI run `32386393634`验证；该历史快照为`current_task=NONE / current_task_status=NO_ACTIVE_TASK / historical_next_authorized_task=NONE`，不覆盖本提交进入formal后的顶部live direct authority。真实生产WorkBuddy/Launcher会话、Stage5、Stage6、Provider/媒体执行及final Package物化/生产登记仍为`NOT_GRANTED`或未证明。

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

## [HISTORICAL / SUPERSEDED_BY_FIXED_CLI_BRIDGE_CONTRACT] Stage 5规划冻结（V2-S5-PLAN-BUILDER1）

本节曾是 `V2-S5-PLAN-BUILDER1` 的 Stage 5规划蓝图，现明确为 `HISTORICAL / SUPERSEDED_BY_FIXED_CLI_BRIDGE_CONTRACT`。它保留当时冻结的产品目标、T1-T12执行顺序、输入/输出、物理承载和验收边界，不授权Stage 5实现、真实WorkBuddy、Stage 4真实Launcher、Provider、媒体、最终Package或Stage 6；其中的 fixed bridge `PENDING`、`UNFROZEN_PENDING_T1` 和旧下一步只作历史任务事实，不是 live authority。当前以顶部 live 字段及下方 `V2-S5-T1-FIXED-CLI-BRIDGE-PLAN1` 固定合同为准；若本节与当前 live 字段冲突，以当前 live 字段为准，不能确认时停止，不自行解释。

上方继承的“Stage 5规划授权候选”块是`0426860`进入formal前、且早于`V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE-AUTHORIZATION1`的授权候选历史记录；其状态只适用于`HISTORICAL_BEFORE_V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE-AUTHORIZATION1`。当前formal对象已在本任务接管前核验为本节的`base_commit/tree`；该历史块不覆盖本节顶部live direct authority，也不形成Stage 5实现或真实WorkBuddy授权。

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
state_record_scope: HISTORICAL_BEFORE_V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE-AUTHORIZATION1
candidate_status: HISTORICAL_CANDIDATE / NOT_FORMALLY_PROMOTED_AT_THAT_TIME
test: NOT_RUN_DOCS_ONLY
current_task_after_candidate: NONE
historical_next_authorized_task: NONE
```

### 1. Stage 5产品目标与唯一运行链路

Stage 5的产品目标只有一个：在真实腾讯WorkBuddy中建立一个、且仅一个可显式命中的入口；接收用户原样业务请求和素材引用；把技术控制、授权、经验证的Package身份和Stage 3事实放入独立输入；在读取已验证Package Guide之后，由WorkBuddy承担OpenMontage生产角色；调用已接受的Stage 4 `launch_session_tool(...)`；把事实和结果原样呈现给用户。腾讯WorkBuddy是唯一运行中的Agent，Shell不得成为第二Agent、Director、FSM、Supervisor、任务平台、Pipeline/Stage/Artifact/Checkpoint执行器、Provider/模型/渲染器/媒体选择器、CLI/MCP并行控制面或自动重试/重放/后台调度系统。这里的“不得成为CLI/MCP并行控制面”不是“CLI一概禁止”：若官方真实机制是唯一WorkBuddy Skill内部调用固定CLI，且它仍是同一唯一入口/消费者的受控桥梁，则必须由T1继续核验，不能仅因CLI存在就否定产品目标。

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

范围外包括：现在写任何生产入口或适配器代码；修改Stage 2/3/4实现、Package、Registration、Activation或CI；运行真实WorkBuddy、真实Launcher、Provider、网络下载、媒体或视频生产；物化最终Package；创建第二Skill、第二Agent、CLI/MCP并行控制面、旁路服务、数据库、队列、状态机或Stage 6代码；把Remotion、HyperFrames或任何Provider硬编码成Shell选择。唯一Skill内部固定CLI是否可作为受控桥梁属于T1合同核验，不得预先否定，也不得自行设计。

外部前置分为两类：

1. 规划可继续但生产验收前必须满足：最终Package物化、安装、生产Registration/Activation及新进程Locator验证；当前Release具体`PackageToolDefinitionV1`实例；真实WorkBuddy版本、Skill安装归属和会话证据。
2. 当前规划可以继续，但内部固定 CLI 桥梁合同尚未冻结：T1已由官方`Skill + CLI`形态和既有 HY3 exact Skill 命中确认外部机制可用；剩余 Skill 归属的 opaque 物理路径、固定 CLI identity/envelope、唯一消费者和 Stage4 字段映射属于本项目 docs-only 规划。当前状态为`IN_PROGRESS / T1_INTERNAL_BRIDGE_CONTRACT_PENDING`，不是`PLANNING_BLOCKED_EXTERNAL_CONTRACT`。Stage 5不得自行生成任意命令/argv/Shell字符串，不得用CLI/MCP作为第二入口、并行控制面或失败兜底；CLI本身不是失败条件。

### 3. T1-T12固定执行蓝图

以下每项的“未来物理承载”是实施前的裁决，不是当前实现白名单；T1未闭合前禁止把占位路径当成真实接口。

#### T1：真实WorkBuddy唯一Skill入口身份

- **目标**：证明并冻结唯一真实WorkBuddy Skill的包结构、安装/导入归属、显式调用主体、调用机制和唯一消费者。
- **权威输入**：本仓库`AGENT_GUIDE.md`、本章程、`MODULE-DISPOSITION.md`；腾讯官方WorkBuddy资料；经另行授权的当前真实客户端证据；旧V1 Skill仅作`HISTORICAL/DROP`证据。
- **具体动作**：先核对官方资料；若官方合同不足，只在另行授权的独立真实客户端任务中验证安装、显式命中、新会话和调用Stage 4的实际协议（直接Python或官方固定CLI内部桥梁，以证据为准）；记录证据、版本、Skill身份和消费者；不修改旧Skill，不启动生产请求。
- **输出**：`T1_WORKBUDDY_ENTRY_CONTRACT`，至少含Skill包结构、安装归属、入口名/调用主体、消费者、固定CLI桥梁边界、Stage 4调用协议和版本证据；当前输出为`T1_EXTERNAL_MECHANISM_CONFIRMED / INTERNAL_FIXED_CLI_BRIDGE_CONTRACT_PENDING`，不等于实现通过。
- **未来文件/物理承载**：最多一个真实WorkBuddy入口资产；包内/用户级物理位置、文件名和导入形态均`UNFROZEN_PENDING_T1`；本规划不创建假Skill、假工具或候选文件。
- **验收**：官方或受控客户端证据能复现一个新会话的显式命中；不依赖第二入口、并行控制面或第二Skill；若官方合同是唯一Skill内部固定CLI，必须证明其为同一入口/消费者的受控桥梁；入口消费者唯一且与WorkBuddy唯一Agent边界一致。
- **Fail-closed**：任一固定CLI identity、envelope、唯一消费者或Stage4映射缺失/冲突，保持`T1_INTERNAL_BRIDGE_CONTRACT_PENDING`，不进入代码实现、不伪造参数、不用CLI/MCP作为第二入口、并行控制面或兜底；CLI本身的存在不是失败条件。
- **上下游**：上游为腾讯官方/真实客户端机制证据和已接受Stage4合同；下游是当前窄 docs-only `V2-S5-T1-FIXED-CLI-BRIDGE-CONTRACT-PLAN1` 及T2输入承载、T12精确文件白名单。内部合同未冻结前不授权实现；冻结后仍需独立审查、普通FF和用户另行实施授权。

#### T2：Stage 5输入合同

- **目标**：冻结用户原话与技术控制、授权和证据的类型/所有权边界。
- **权威输入**：Stage 4已接受的`launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)`合同，以及T1如实证据证明的唯一Skill内部固定CLI桥梁等价承载；Stage 2 Registration/Locator合同；Stage 3完整能力定义和未改写原始`PRESENT/INTEGRATED`事实；本章程消息与凭据边界。
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
- **具体动作**：只调用T1已经核验并冻结的唯一WorkBuddy入口合同；当前规划候选为`launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)`，但它不是排他性先验。若官方真实合同证明唯一Skill内部调用固定CLI，则按该受控桥梁合同传递同样的已验证事实，不得仅因CLI存在就否定产品目标；`user_message`仍原样传递；定义声明本地能力时原样传递完整approved capability definition和未改写original Stage 3 fact；Stage 5不生成任意命令、argv、Shell字符串、stdin替代包或本地能力摘要。
- **输出**：Stage 4原样的递归不可改写`LauncherReceiptV1`，以及Stage 5可呈现的事实引用；固定工具至多一次spawn由Stage 4负责。
- **未来文件/物理承载**：未来最多一个Stage 5生产模块/入口适配器；不新增Launcher、命令构造器、CLI/MCP旁路或第二进程；T1若证明官方唯一Skill内部固定CLI桥梁，该桥梁属于已冻结的唯一入口合同，不是新增控制面；实际调用物理承载依赖T1且当前`UNFROZEN_PENDING_T1`。
- **验收**：入口合同固定且唯一；函数参数域分离或固定CLI桥梁的等价字段承载均有直接证据；完整事实无摘要重包装、Stage 4定义/源语义自验证；Stage 5自身spawn=0且不生成任意Shell字符串；Stage 4仍`spawn<=1/retry=0`。
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

- **目标**：把未来实现授权所需的身份、基线、文件、测试、审查和推广规则冻结；T1已闭合为可规划内部桥梁，真实客户端/生产证据仍独立未证明。
- **权威输入**：本节T1-T11；届时实时`origin/codex/workbuddy-shell-v2`；用户后续明确原话“启动阶段五实施”；T1最终入口合同；Stage 2/3/4合同和正式状态。
- **具体动作**：未来唯一Builder ID固定为`V2-S5-WORKBUDDY-ENTRY-BUILDER1`；接管时重新解析实时formal HEAD/tree/tracked，不能直接使用历史SHA、main、旧长期分支或当前规划分支；先核验干净状态和精确白名单，再创建D盘独立临时worktree/branch。公共入口固定为1，新增生产模块上限为1，直接测试文件固定为1；Stage 6不预建。
- **输出**：T1闭合后的实施任务包已冻结：入口源资产`workbuddy-skill/golden-key-openmontage/SKILL.md`；唯一生产模块`golden_key_openmontage_workbuddy/workbuddy_entry_cli.py`；唯一直接测试`tests/workbuddy/test_workbuddy_entry_cli.py`；验收同步仅为`tests/workbuddy/test_repository_hygiene.py`与`.github/workflows/ci.yml`；不改`__init__.py`、`pyproject.toml`、`MODULE-DISPOSITION.md`；tracked精确`37 -> 40`。固定命令为direct/hygiene/full三组`python -m pytest -p no:cacheprovider ... -q`，详见本账本收口候选。
- **未来文件/物理承载**：实施恰好承载上述一个Skill源资产、一个生产模块和一个直接测试；hygiene/CI为既有文件的最小同步；Skill客户端物理安装路径保持opaque，由最终Installer/Package gate按release身份物化。若需要第N+1个路径，立即停止并回到用户重新授权。
- **验收**：实施前必须有“启动阶段五实施”明确授权；精确base/tree/tracked与formal等值；Builder只改白名单；项目D盘私有`.venv`；直接测试、hygiene、完整测试按冻结命令最终exit 0；`git diff --check`、tracked/clean/untracked/stash等值；Reviewer独立零写比较base..candidate；只有`APPROVE/P0=0/P1=0/P2=0`且formal仍等于base才可普通fast-forward。
- **Fail-closed**：T1未闭合、授权缺失、对象/路径/tracked不符、命令需猜测、需要第N+1路径、测试无最终exit、Reviewer非APPROVE或正式分支已前移时停止；不force push、不merge/rebase、不推广、不自动开启Stage 6。
- **上下游**：上游是T1闭合、Stage 2/3/4已接受合同和未来用户授权；下游是唯一Builder、独立Reviewer、普通FF及真实Stage 5验收。规划被接受也不等于实现被授权。

### [HISTORICAL / SUPERSEDED_BY_T1_FIXED_CLI_AND_PLANNING_CLOSEOUT] 4. 规划交付与治理出口

本段只记录旧三路径规划候选规则，已被 T1 固定桥梁和本文末六文档 closeout 候选 supersede；Builder不修改正式分支、不运行测试（`test=NOT_RUN_DOCS_ONLY`）、不运行真实WorkBuddy/Launcher/Provider/媒体/WSL、不物化Package、不创建Registration、不启动Stage 6。它不再约束当前 closeout 或未来实施 Builder。

Reviewer至少核对：WorkBuddy是否仍是唯一Agent；是否只有一个真实入口；是否错误预建CLI/MCP/第二Agent；是否硬编码Provider/Runtime；是否保持literal message与controls分离；是否完整消费Stage 2/3/4合同；是否区分最终Package与生产验收；是否含T1-T12和15类失败矩阵；是否保持Stage 6零代码出口；是否存在产品或文档范围膨胀。P0为架构/安全/权限/身份绕过或泄密；P1为可执行合同、映射、证据或边界缺口；P2为不影响合同的表述问题。只有`APPROVE / P0=0 / P1=0 / P2=0`才允许后续治理普通fast-forward；REQUEST_CHANGES只能回原Builder。

本段原先关于三路径、`PLANNING_BLOCKED_EXTERNAL_CONTRACT`、规划不得`PASS_ACCEPTED`和`next_authorized_task=NONE`的文字全部是历史条件，只适用于旧 Evidence1/旧规划候选；当前外部机制与 T1 内部桥梁已闭合，当前 closeout 候选的六路径、`PASS_ACCEPTED`条件和下一 Builder 以本文末为准。

## Stage 5 T1真实WorkBuddy入口合同证据核验授权候选（2026-08-21）

本节只固化用户对 T1 证据核验的授权，不表示证据已经完成，也不授权 Stage 5 实现、真实 WorkBuddy、Launcher、Provider、媒体、最终 Package 或 Stage 6。候选分支未进入 formal 前 `current_task=NONE`；本提交进入 formal 后，live direct authority 才生效为唯一的 `V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE1`。独立零写 Reviewer 与普通 fast-forward 仍是本候选的正式治理条件。

```text
task_id: V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE-AUTHORIZATION1
task_kind: STAGE5_T1_EVIDENCE_AUTHORIZATION / DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE
user_authorization: 2026-08-21 / 授权启动T1真实WorkBuddy唯一入口合同证据核验任务，仅核查官方资料和经另行允许的受控客户端证据，不写代码、不运行生产流程。
base_commit: 5840470728f3618e575eacab2298b37a177d7c28
base_tree: fc86e90d65369d4f421f5debec21514bf2fc5186
tracked_files_at_base: 37
candidate_branch: codex/v2-s5-t1-evidence-authorization1
formal_target_branch: origin/codex/workbuddy-shell-v2
candidate_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md
candidate_production_code_changes: 0
candidate_test_changes: 0
candidate_ci_changes: 0
candidate_package_registration_changes: 0
candidate_external_writes: NONE
candidate_real_workbuddy_execution: NOT_PERMITTED
candidate_launcher_provider_media_wsl_execution: NOT_PERMITTED
candidate_test: NOT_RUN_DOCS_ONLY
subsequent_task_id: V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE1
subsequent_task_effective: ONLY_AFTER_THIS_AUTHORIZATION_REVIEW_APPROVE_AND_ORDINARY_FAST_FORWARD
stage_5_planning: PLANNING_BLOCKED_EXTERNAL_CONTRACT
stage_5_implementation_authorization: NOT_GRANTED
current_task_before_promotion: NONE
next_authorized_task_before_promotion: NONE
candidate_status: CANDIDATE_UNTIL_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD / FORMAL_AUTHORITY_WHEN_THIS_COMMIT_IS_FORMAL
```

### T1五项核验范围

T1 只核查以下五项，不得扩展为实现设计或客户端生产验证：

1. 真实 WorkBuddy Skill 的包结构；
2. Skill 的安装/导入归属；
3. 显式调用主体和调用机制；
4. 唯一消费者，以及它与 WorkBuddy 唯一 Agent 边界的关系；
5. 一个 WorkBuddy Skill 内固定 CLI 桥梁是否能以单一、固定、非用户入口的 envelope 消费已接受 Stage 4 Python API `launch_session_tool(...)`；任意命令/argv/Shell 生成、第二入口、MCP旁路和自动重试/重放仍禁止。

第一阶段证据源只允许腾讯/WorkBuddy官方一手公开资料，以及本仓库已经存在的静态证据。网页证据必须记录 URL、标题、访问日期、原文直接支持的精确 claim 和仍未支持的 gap；搜索摘要、第三方文章、论坛、推测和旧 V1 Skill 均不得作为权威。旧 V1 Skill 只能标记为 `HISTORICAL/DROP`，不得复用或推导新的入口合同。

用户所说的“经另行允许的受控客户端证据”在本授权候选中冻结为 `NOT_AUTHORIZED_IN_THIS_TASK`：不得打开、操作或运行真实 WorkBuddy，不得上传、安装或调用 Skill。若官方资料不足，只能记录未来另行授权的最小客户端核验步骤及其待证明字段；本候选不得执行这些步骤。

### T1后续Evidence Builder边界与结果

后续唯一 Evidence Builder `V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE1` 的最大文档白名单冻结为：`PROJECT-STATE.md`、`docs/workbuddy/v2/TASK-REGISTER.md`、`docs/workbuddy/v2/PROJECT-CHARTER.md`、`docs/workbuddy/v2/ACCEPTANCE-MATRIX.md`；不得新增平行证据或规划文档，实际结果可以少改文件。Evidence Builder 只能提交 docs-only 证据候选和建议状态，必须经独立零写 Reviewer 与普通 fast-forward；即使五项均被官方资料证明，也不得自行标记 Stage 5 实现 PASS 或启动实现。

若官方资料不能同时证明五项，Evidence Builder 在 `AFTER_EVIDENCE1_COMPLETES_WITH_T1_EVIDENCE_INCOMPLETE` 时必须保持 `stage_5_planning=PLANNING_BLOCKED_EXTERNAL_CONTRACT`、`stage_5_implementation_authorization=NOT_GRANTED`、`next_authorized_task=NONE`；这不是本候选进入formal后的当前live值，不得填造路径、接口、参数，不得授权实施。即使官方资料足以形成五项证据，仍只能记为证据候选/待独立审查，随后另行进行权威状态收口；不得从 Evidence1 自动推导 Stage 5 实现授权。

本授权候选及其后续 Evidence1 均禁止：生产代码、测试、CI、pyproject、Package 字节、Registration/Activation、真实 WorkBuddy、Launcher、Provider、Runtime 下载、媒体、WSL、Stage 6、final Package、production Registration，以及第二 CLI/第二入口、MCP旁路、第二 Skill、第二 Agent、并行控制面、任意命令/argv/Shell生成。一个固定 CLI 作为唯一 Skill 的内部桥梁不属于“一概禁止”，但仍需本项目合同和证据闭合。

### 本授权候选治理出口（Evidence1 前置授权历史）

以下是 Evidence1 之前的授权候选历史治理出口，不是 Evidence1 的当前白名单。该前置候选只允许修改 `PROJECT-STATE.md` 与本账本两条路径；不得修改章程、验收矩阵或新增证据文档。Builder 不运行测试（`test=NOT_RUN_DOCS_ONLY`）、不运行真实 WorkBuddy/Launcher/Provider/媒体/WSL、不物化 Package、不创建 Registration、不启动 Stage 6。完成后必须核验精确两路径、tracked 仍为 37、`git diff --check` 通过、clean/untracked 0/stash 0，并以单一临时分支非force push；独立零写 Reviewer 只审该授权候选，`REQUEST_CHANGES` 只能回原 Builder。只有 `APPROVE / P0=0 / P1=0 / P2=0` 且 formal 仍等于 base 时，才允许普通 fast-forward；推广后唯一下一任务才生效为 `V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE1`。Evidence1 的当前白名单、证据范围和候选治理以其下方同名章节为准。

## Stage 5 T1 官方合同证据核验候选（历史候选，已被当前Skill+CLI重新评估取代）

本节是 Evidence1 的唯一候选结果。它只记录官方资料核验，不宣称真实客户端证据，不授权实现或生产。当前候选从实时 formal `44d89625c1fd71d07d1173e18681e64e7459cec2`、tree `10c8c4187299564fc83cef38a3f9ac65f4f9790a`、tracked 37 接管；默认工作目录不是该 formal 对象，Builder 已在 D 盘独立 worktree 中从精确 commit 建立候选。受控真实客户端在本任务冻结为 `NOT_AUTHORIZED_IN_THIS_TASK`。

```text
task_id: V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE1
task_kind: STAGE5_T1_OFFICIAL_CONTRACT_EVIDENCE / DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE
user_authorization: 2026-08-21 / 仅核查官方资料和经另行允许的受控客户端证据，不写代码、不运行生产流程
base_commit: 44d89625c1fd71d07d1173e18681e64e7459cec2
base_tree: 10c8c4187299564fc83cef38a3f9ac65f4f9790a
tracked_files_at_base: 37
candidate_branch: codex/v2-s5-t1-official-contract-evidence1
candidate_worktree: D:\\BlazingCD\\Personal\\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2-s5-t1-evidence1
candidate_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md
candidate_forbidden: code; tests; CI; pyproject; Package; Registration/Activation; real WorkBuddy; Launcher; Provider; Runtime download; media; WSL; Stage 6; final Package; CLI/MCP/second Skill/second Agent
official_sources_access_date: 2026-08-21
controlled_client_status: NOT_AUTHORIZED_IN_THIS_TASK
candidate_result: T1_EVIDENCE_INCOMPLETE
stage_5_planning_after_candidate: PLANNING_BLOCKED_EXTERNAL_CONTRACT
stage_5_implementation_authorization_after_candidate: NOT_GRANTED
current_task_after_candidate: NONE
next_authorized_task_after_candidate: NONE
test: NOT_RUN_DOCS_ONLY
```

### 官方一手来源清单

以下页面均为腾讯云/腾讯 WorkBuddy 官方公开资料；访问日期统一为 `2026-08-21`。页面的“最近更新时间”是页面自身标注，不等同于本次访问日期。

| ID | 完整 URL / 页面标题 / 发布主体 | 访问日期 | 页面更新时间 | 直接支持的 claim | 明确未支持的 gap |
|---|---|---|---|---|---|
| O1 | `https://cloud.tencent.cn/document/product/1831/134391` / `WorkBuddy Enterprise 新建任务栏（本地 AI 工作台）` / 腾讯云 | 2026-08-21 | 2026-08-03 15:25:00 | Skills 扩展 WorkBuddy 任务能力；对话框可选择已安装 Skill，执行任务时 WorkBuddy 自动调用对应能力；支持内置 Skill、OpenClaw 社区 Skill 导入和自然语言创建自定义 Skill。 | 未定义 Skill 压缩包/目录结构、必需文件、schema、安装后物理路径、用户级/工作区级归属、固定入口名，亦未定义直接加载本地 Python 模块或返回 receipt 的协议。 |
| O2 | `https://cloud.tencent.cn/document/product/1831/134324` / `WorkBuddy 更新记录` / 腾讯云 | 2026-08-21 | 2026-07-30 17:41:50 | 4.8.0 记录 Desktop Skills/SkillHub/Marketplace；4.9.1 记录 Skill 导入安全检查；5.0.0 记录项目级 Skill 及按角色权限编辑；5.1.0 记录企业自建 Skill/插件市场和一键安装能力。 | 更新记录证明产品能力存在及项目级概念，不给出本地客户端 Skill 包 schema、实际安装目录、当前 5.3.13 的导入落点或 Stage 4 Python API 调用合同。 |
| O3 | `https://cloud.tencent.cn/document/product/1831/134401` / `两个权限模式` / 腾讯云 | 2026-08-21 | 2026-07-20 19:49:32 | WorkBuddy 可读写文件并在权限控制下调用脚本或外部程序；工作空间是当前任务读写的文件夹，可由用户选择或由 WorkBuddy 创建；默认权限对脚本、命令或外部程序要求确认。 | 这是外部程序/脚本执行安全边界，不是本地 Python 模块直调；未定义 API 加载方式、参数承载、调用者身份、stdin/argv 规则或 `LauncherReceiptV1` 返回协议。 |
| O4 | `https://cloud.tencent.cn/product/workbuddy` / `WorkBuddy` / 腾讯 | 2026-08-21 | 页面未标注统一更新时间 | WorkBuddy 接收自然语言任务，可自主拆解规划、调用工具，并在用户授权目录内读写本地文件。 | 产品介绍未定义 Skill 包结构、安装/导入物理归属、唯一消费者证明或不经命令/argv/Shell 直接调用本仓库 Python API 的协议。 |

O1/O2/O3/O4 均没有证明“Skill 触发后在 WorkBuddy 进程内直接 import 本仓库模块并传递精确 `launch_session_tool(...)` 参数、再返回固定 receipt”。O3 中的“脚本/命令/外部程序”只能保留为产品已有的外部执行能力，不能被倒推为本项目所需的直调合同。搜索摘要、第三方文章、论坛、视频、自媒体和相邻腾讯产品的 Skill 规范未作为本表 contract proof。

### 已有仓库静态证据（只读）

- `docs/workbuddy/v2/MODULE-DISPOSITION.md` 的 V1 调用链记录：两个历史 Skill 通过 `WORKBUDDY-RUNTIME.json -> launcher -> CLI` 消费旧能力；V2 对 CLI/MCP 生产入口作 `DROP`，只允许未来重新证明一个唯一 WorkBuddy 入口。这是历史处置证据，不是新入口合同。
- `PROJECT-STATE.md`、`PROJECT-CHARTER.md`、`ACCEPTANCE-MATRIX.md` 的既有 Stage 5 硬停止：官方资料至多证明上传/选择/召唤，本机 5.3.13 的既有记录至多证明用户级 Skill 存在；Skill 包结构、安装归属、精确调用协议仍未证明。本任务未读取仓库外 WorkBuddy 安装目录，也未打开或操作真实客户端。
- Stage 4 已接受接口是本仓库内部已冻结的 `launch_session_tool(...)` 与 `LauncherReceiptV1`；官方 WorkBuddy 资料没有把该内部合同连接到一个真实 Skill 的直接调用路径。

### T1 五项逐项裁决

| 项目 | 状态 | 官方资料已证明 | 仍未证明 / 不得推断 |
|---|---|---|---|
| 1. 真实 Skill 包结构、必需文件、schema | `UNPROVED_OFFICIAL` | O1 证明 WorkBuddy 支持已安装 Skill、内置/社区导入和自定义 Skill；O2 证明存在导入安全检查和 Skill 市场。 | 未给出压缩包/目录形态、必需文件清单、manifest/schema、版本绑定或校验规则；不得从 OpenClaw、旧 V1 或相邻产品规范补猜。 |
| 2. 安装/导入归属、物理位置、用户级或 workspace 级语义 | `PARTIALLY_PROVED_OFFICIAL` | O1 证明选择的是“已安装 Skill”；O2 证明项目级 Skill 和一键安装能力；O3 证明工作空间属于任务文件读写边界。 | 未给出本地 Skill 安装根、用户级与项目/工作区级优先级、导入后的物理文件路径、所有权或持久化规则；不能把 O2 的项目级功能倒推为本地目录合同。 |
| 3. 显式调用主体、入口名、选择/触发机制 | `PARTIALLY_PROVED_OFFICIAL` | O1 证明对话框选择已安装 Skill 后由 WorkBuddy 自动调用；O2 的更新记录证明 Skill 列表/市场与模型驱动的 Skill 相关入口持续存在。 | 未给出当前版本固定 Skill 名/入口名、选择值如何绑定实际包、自动调用的内部 dispatch、会话边界或 WorkBuddy 到本地 Python 的调用协议；不能把自然语言触发、斜杠命令或 UI 选择互相等同。 |
| 4. 唯一真实消费者及 WorkBuddy 唯一 Agent 边界 | `PARTIALLY_PROVED_OFFICIAL` | O1/O4 将 WorkBuddy描述为任务执行者，Skill能力由 WorkBuddy任务调用；O3 将权限确认归于 WorkBuddy。 | 官方资料没有证明本项目所需的“唯一消费者=一个 Skill/一个 WorkBuddy Agent、无第二 Agent/CLI/MCP/并行入口”的边界，也未证明入口只服务本仓库而非市场/插件/连接器等其他消费者。 |
| 5. 固定 CLI 内部桥梁与 Stage 4 消费协议 | `UNPROVED_PROJECT_BRIDGE` | O1/O3 证明 WorkBuddy 能调用 Skill、脚本或外部程序；本轮 O2 官方连接器页面明确公开`Skill + CLI`形态。 | 本项目仍需冻结固定 CLI identity、单一 envelope、literal message/controls 分离、完整定义/原始事实传递、一次调用和`LauncherReceiptV1`逐字段映射；腾讯官方无需定义本仓库 Python API，且不得以外部脚本能力填造内部合同。 |

五项没有全部闭合，旧候选总裁决 `T1_EVIDENCE_INCOMPLETE` 仅作历史记录；本轮当前裁决见下方 `T1_CONTRACT_REASSESSMENT_INCOMPLETE`。不得填造 WorkBuddy 物理路径、固定 CLI 名称或未证实的运行协议，也不能由证据候选自动获得实现授权。

### 最小未来受控客户端验证卡（仅记录，不执行）

若要闭合 T1，必须另行授权一次受控客户端任务；本任务不创建 Skill、不导入 Skill、不读取安装目录、不上传、不安装、不调用、不运行生产请求。未来验证卡固定为：

1. 另行书面授权，锁定 WorkBuddy 精确版本、全新会话、全新隔离工作区和 D 盘证据保存位置；确认不接触现有 Golden Key Skill、Provider、媒体和生产 Package。
2. 制作一个最小、无生产副作用的 candidate Skill（仅在未来任务获授权后），记录上传前完整包字节、目录树、必需文件/schema 和每个文件的 SHA-256；不得沿用旧 V1 Skill。
3. 在全新会话中通过产品支持的显式方式导入/安装 candidate Skill，保存 UI 提示、Skill 名称/版本/hash（若产品展示）、导入结果和安装/导入归属；同时观察被另行授权的最小文件边界，确认用户级、项目级或 workspace 级语义及物理位置。
4. 显式命中 candidate Skill，记录入口名、选择值、触发方式、会话 ID、WorkBuddy 版本和唯一消费者；确认没有第二 CLI、MCP、第二 Skill、第二 Agent 或自动化旁路；若存在 CLI，只能是本项目定义的一个固定内部桥梁。
5. 让 candidate Skill 执行一个零生产副作用的探针，证明固定 CLI 是否能以不可变单一 envelope 消费本项目 `launch_session_tool(...)`，并原样传递完整参数；不得从用户输入动态生成命令/argv/Shell。若产品只支持外部脚本/命令而无法满足固定桥梁合同，必须记录为“不支持本项目桥梁”，不得把外部执行泛化为通过。
6. 观察并保存返回值是否逐字段对应 `LauncherReceiptV1`；确认 literal `user_message` 原样、`executor_controls` 独立、Provider/媒体/Package/Stage 4真实 spawn 均为 0；任何证据缺失、输出截断、对象漂移或副作用都保持 `INCOMPLETE`。
7. 证据位置、清理范围、客户端日志和截图的保存/删除必须由该未来任务另行授权；完成后由独立零写 Reviewer 复核，不能把客户端结果直接改成 PASS 或启动实施。

在上述受控客户端证据真正闭合前，T1 不得建议 `PASS_ACCEPTED`，T12 的精确入口路径、包结构、tracked 迁移和 CI 命令继续 `UNFROZEN_PENDING_T1`。

## [HISTORICAL / SUPERSEDED_BY_STAGE5_PLANNING_CLOSEOUT] Stage 5 T1 Skill+CLI合同重新评估候选（V2-S5-T1-SKILL-CLI-CONTRACT-REASSESSMENT1，2026-08-21）

本节是 closeout 前的 T1 重新评估结果，曾优先于上方历史 Evidence1/客户端候选中把“零 CLI 直调”写成必要条件的文字；现作为历史审计事实保留。当前 live 状态和下一任务以本文末 Stage5 规划收口候选及顶部字段为准。它只做官方资料、既有 Stage4 合同和既有受控客户端证据的 docs-only 裁决；不运行真实 WorkBuddy，不调用 Skill，不运行 Python/Stage4，不写代码、测试、CI、Provider、媒体、Package、Registration 或 Stage6。

```text
task_id: V2-S5-T1-SKILL-CLI-CONTRACT-REASSESSMENT1
task_kind: STAGE5_T1_CONTRACT_REASSESSMENT / DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE
user_authorization: 2026-08-21 / 好，那开始吧
initial_product_goal_recheck: PASS / WorkBuddy is the only running Agent and the only user entry; after loading the verified Package Guide it assumes the OpenMontage logical production role
base_commit: 24418c7cf5cc003c106a8282158adb3125bb0606
base_tree: d61a4a455a0e4f5202a2b4907476beb97a655201
tracked_files_at_base: 37
candidate_branch: codex/v2-s5-t1-skill-cli-reassessment1
candidate_worktree: D:\\BlazingCD\\Personal\\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2-s5-t1-skill-cli-reassessment1
formal_target_branch: origin/codex/workbuddy-shell-v2
candidate_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md
candidate_forbidden: code; tests; CI; pyproject; Package; Registration/Activation; new WorkBuddy client operations; Launcher/Python/Stage4 spawn; Provider; Runtime download; media; WSL; Stage6; second entry; MCP/second Skill/second Agent; arbitrary command/argv/Shell generation
official_sources_access_date: 2026-08-21
controlled_client_evidence: EXISTING_ONLY / WorkBuddy 5.3.13 / HY3 no-op Skill record; no new client operation in this task
stage_4_contract: PASS_ACCEPTED / launch_session_tool(...) + immutable LauncherReceiptV1 / unchanged
candidate_result: T1_EXTERNAL_MECHANISM_CONFIRMED / INTERNAL_FIXED_CLI_BRIDGE_CONTRACT_PENDING
stage_5_planning_after_candidate: IN_PROGRESS / T1_INTERNAL_BRIDGE_CONTRACT_PENDING
stage_5_implementation_authorization_after_candidate: NOT_GRANTED
current_task_after_candidate: NONE
next_authorized_task_after_candidate: V2-S5-T1-FIXED-CLI-BRIDGE-CONTRACT-PLAN1 / ONLY_AFTER_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD
test: NOT_RUN_DOCS_ONLY
candidate_status: CANDIDATE_UNTIL_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD
push_status: NOT_PUSHED
```

### 初始产品目标与两层证据

`initial_product_goal_recheck=PASS` 是本任务的强制起点。官方证据层（A）只回答 WorkBuddy 是否支持 Skill、脚本/工作流、用户授权执行和 `Skill + CLI` 技术形态；本项目内部桥梁层（B）负责冻结一个固定 CLI 的 identity、envelope、调用主体、消费者和与 Stage4 的字段映射。不得要求腾讯官方页面替本仓库定义 `launch_session_tool(...)` 的 Python 参数或 `LauncherReceiptV1` 字段，也不得用官方高层“可执行脚本”能力填造这些内部字段。

### 官方一手来源与证据矩阵

以下只使用腾讯/WorkBuddy官方页面；页面更新时间为页面自身标注，访问日期统一为 `2026-08-21`。每条来源均列出可证明与不可证明边界：

| ID | URL / 页面标题 | 直接可证明 | 不能证明、不得推断 |
|---|---|---|---|
| O1 | `https://cloud.tencent.com/document/product/1831/134432` /《WorkBuddy Enterprise 技能》 | Skill 可封装可执行脚本与工作流；可上传/查找/创建并启用；在对话中召唤后 WorkBuddy 自动调用；脚本、命令和第三方调用按用户身份/授权执行。 | 完整包 schema/目录、物理安装路径、用户/工作区/项目优先级、当前固定 dispatch、全局唯一消费者、项目 CLI identity/envelope 和 Stage4 receipt 映射。 |
| O2 | `https://cloud.tencent.com/document/product/1831/134525` /《WorkBuddy Enterprise 连接器》 | 官方公开技术形态包括 `MCP + CLI` 和 `Skill + CLI（内置脚本）`；连接器是 WorkBuddy 与外部能力的桥梁，支持授权与调用。 | 不证明本项目必须使用 MCP；不定义本项目固定 CLI 名称/sha/owner、单一 envelope、唯一消费者或 `launch_session_tool(...)`/`LauncherReceiptV1` 映射。 |
| O3 | `https://cloud.tencent.com/document/product/1831/134391` /《WorkBuddy Enterprise 新建任务栏（本地 AI 工作台）》 | 任务栏是 WorkBuddy 本地 AI 工作台入口；用户可选已安装 Skill，执行任务时自动调用对应能力；每个对话是独立任务/工作空间。 | “任务栏入口”不等于本项目全局唯一消费者证明；不定义 Skill 包、安装物理路径、固定 CLI 或 Stage4 API。 |
| O4 | `https://cloud.tencent.com/document/product/1831/134401` /《WorkBuddy Enterprise 两个权限模式》 | WorkBuddy 在工作空间/授权边界内读写文件；执行脚本、命令或外部程序可触发确认；取消确认则不执行。 | 不证明 Python 原生导入、参数承载、stdin/argv 规则、固定 CLI identity 或 receipt 字段。 |
| O5 | `https://cloud.tencent.com/document/product/1831/134324` /《WorkBuddy Enterprise WorkBuddy 更新记录》 | 既有版本记录支持 Desktop Skills/SkillHub/Marketplace、Skill 导入安全检查、企业自建 Skill/插件市场及 CLI 连接器相关能力。 | 更新记录不是当前版本的精确包 schema、安装路径、唯一 dispatch 或本项目 Stage4 适配合同。 |
| O6 | `https://cloud.tencent.com/document/product/1831/134516` /《WorkBuddy Enterprise Skills》 | 页面可作为相邻 Skills 产品资料线索。 | 页面面包屑和正文是 **CodeBuddy** 语境；`.codebuddy/skills` 不能作为 WorkBuddy 的安装路径、所有权、优先级或 5.3.13 合同证明。 |

### 当前 T1 五项裁决

| 项目 | 当前状态 | 已能冻结的内容 | 仍未证明/边界 |
|---|---|---|---|
| 1. 入口身份与 Skill 归属 | `EXTERNAL_MECHANISM_CONFIRMED / IMPLEMENTATION_PACKAGE_DETAILS_PENDING` | 一个 WorkBuddy-managed installed Skill catalog 入口；物理路径保持 `opaque`；WorkBuddy 是用户对话主体。 | 完整包 schema、版本/校验规则、物理落点和跨 user/workspace/project 优先级待后续内部合同/实现验收，不构成外部机制阻断。 |
| 2. 调用主体与触发 | `EXTERNAL_CALL_CONFIRMED / CLIENT_SESSION_PROVED` | WorkBuddy 选择/召唤已安装 Skill 后自动调用；现有 HY3 记录命中过 exact no-op Skill。 | 当前固定入口名、dispatch 绑定和生产入口的最终实现字段待内部合同规划/后续验收。 |
| 3. 固定 CLI 桥梁边界 | `SUPPORTED_FORM_CONFIRMED / FROZEN_FOR_PLANNING` | 官方明确支持 `Skill + CLI`；项目冻结 `one WorkBuddy Skill -> one fixed internal CLI bridge`，CLI 不是用户第二入口、并行控制面或失败兜底；固定 transport adapter 的模块、argv、schema、环境和 receipt 规则已在下方冻结。 | release-specific interpreter/module/schema/hash 资产值仍须由 Installer/Skill 资产写入并验证；不得使用 MCP 旁路、通用 console-script 或动态命令。 |
| 4. 唯一消费者与 WorkBuddy 唯一 Agent | `PROJECT_BOUNDARY_FROZEN / GLOBAL_RUNTIME_PROOF_PENDING` | 仓库产品边界冻结 WorkBuddy 唯一 Agent；Skill/CLI 只能是该 Agent 的内部桥梁，不能启动第二 Agent。 | 全局无第二 dispatch/消费者/并行入口属于后续内部合同和真实验收字段，不是官方机制不存在。 |
| 5. 与Stage4衔接 | `COMPATIBLE_INTERNAL_CONTRACT / BRIDGE_MAPPING_FROZEN_FOR_PLANNING` | Stage4 `launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)` 与不可变 `LauncherReceiptV1` 是唯一内部消费合同；固定 CLI 仅重建非秘密 controls、一次调用该 API，并逐字段输出 receipt wire mapping；不重开 Stage4。 | 实际代码、Installer 写入、真实客户端和 Stage4 spawn 尚未授权/证明；任何映射实现偏差必须 fail closed。 |

### 固化的唯一桥梁边界与裁决

允许冻结的逻辑链是：

```text
WorkBuddy conversation
  -> one WorkBuddy-managed Skill catalog entry
  -> one fixed internal CLI bridge (opaque physical path, non-user-facing)
  -> accepted launch_session_tool(...)
  -> one immutable LauncherReceiptV1
```

固定 CLI 合同已达到 `FROZEN_FOR_PLANNING`：release-specific identity/owner/hash 由 Installer/Skill 资产写入并可验证；执行形状固定为 Stage2 Locator 返回的 package-private Python、`-I -m golden_key_openmontage_workbuddy.workbuddy_entry_cli`，无 console-script、子命令或动态 argv。单一 stdin envelope 原样承载 `literal user_message`、非秘密 closed controls、完整 `PackageToolDefinitionV1` 和完整 approved capability definition+original Stage3 fact；Provider secret value 不进入 envelope，而只由 CLI 按 envelope 的 allowlisted names 从自身进程环境读取，重建 Stage4 `provider_environment` 后传入一次 API。`cancel_requested` 只表示入口前事实；continuation 只表示用户确认的新 envelope，禁止自动 replay。stdout 逐字段输出唯一 `LauncherReceiptV1` JSON mapping；pre-Stage4 JSON/环境/资产错误只允许固定脱敏 stderr 和非零退出，不伪造 receipt。Skill 不得从用户原话拼接 command/argv/Shell，不得同时保留 CLI/MCP/第二Skill入口，不得自动重试或重放；Stage4 固定 Package 工具最多 spawn 一次的合同不变。

官方能力形态加上既有 HY3 exact Skill 命中已足以确认 WorkBuddy 的外部机制可用，解除“外部机制不存在/不可用”的卡点。本候选已把内部固定 CLI identity、transport envelope、secret-safe controls、唯一消费者边界、Stage4 一次调用和 receipt 映射冻结为 `FROZEN_FOR_PLANNING`；它不是 `PASS_ACCEPTED`，也不授予实现。Stage5 规划保持 `IN_PROGRESS / T1_FIXED_CLI_BRIDGE_FROZEN_FOR_PLANNING`；Stage5 实现、真实 WorkBuddy、Provider、媒体、最终 Package、生产 Registration、Stage6 仍为 `NOT_GRANTED` 或未证明。下一步只允许在本候选独立零写 Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 并普通 fast-forward 后，启动窄范围 docs-only `V2-S5-PLANNING-CLOSEOUT-IMPLEMENTATION-HANDOFF-ASSESSMENT1`；不得自动进入代码或生产。

## [HISTORICAL / SUPERSEDED_BY_STAGE5_PLANNING_CLOSEOUT] Stage 5 T1固定 CLI内部桥梁合同冻结候选（`V2-S5-T1-FIXED-CLI-BRIDGE-CONTRACT-PLAN1`，2026-08-21）

本节是上一项 T1 的最小、可实现、docs-only 内部合同，现作为历史结果保留。它只冻结一个 WorkBuddy-managed Skill 内的固定 transport adapter，不创建代码、Skill 包、Installer、Package、生产入口或第二控制面；它不把腾讯官方页面冒充为本仓库 Python API 定义。官方 `Skill + CLI` 机制、既有 HY3 exact Skill 会话和已接受 Stage4 合同是外部/内部两层前提；本节把内部桥梁达到 `FROZEN_FOR_PLANNING`，其后续规划收口和实施交接以本文末当前候选为准。

```text
task_id: V2-S5-T1-FIXED-CLI-BRIDGE-CONTRACT-PLAN1
task_kind: STAGE5_T1_INTERNAL_BRIDGE_CONTRACT_PLAN / DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE
initial_product_goal_recheck: PASS / WorkBuddy is the only running Agent and the only user entry; after loading the verified Package Guide it assumes the OpenMontage logical production role
base_commit: 3eed285da6ae48e502d5be1f8ca726906d36b7cd
base_tree: c0b03c4e7d858d5f15c7ce328cf5e2b60b57978b
tracked_files_at_base: 37
candidate_branch: codex/v2-s5-t1-fixed-cli-bridge-plan1
candidate_worktree: D:\\BlazingCD\\Personal\\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2-s5-t1-fixed-cli-bridge-plan1
formal_target_branch: origin/codex/workbuddy-shell-v2
candidate_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md
candidate_forbidden: code; tests; CI; pyproject; new Skill install/call; WorkBuddy client; Python execution; Stage4 spawn; Provider; media; Package; Registration/Activation; Stage6; second entry; MCP; second Skill; second Agent; arbitrary command/argv/Shell generation
candidate_result: T1_INTERNAL_FIXED_CLI_BRIDGE_CONTRACT_FROZEN_FOR_PLANNING
t1_internal_contract_status: FROZEN_FOR_PLANNING
stage_5_planning_after_candidate: IN_PROGRESS / T1_FIXED_CLI_BRIDGE_FROZEN_FOR_PLANNING
stage_5_implementation_authorization_after_candidate: NOT_GRANTED
stage_5_workbuddy_entry_authorization_after_candidate: NOT_GRANTED
stage_6_status_result_relay_authorization_after_candidate: NOT_GRANTED
final_package_gate_authorization_after_candidate: NOT_GRANTED
current_task_after_candidate: NONE
next_authorized_task_after_candidate: V2-S5-PLANNING-CLOSEOUT-IMPLEMENTATION-HANDOFF-ASSESSMENT1 / ONLY_AFTER_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD
downstream_implementation_allowlist: UNFROZEN / MUST_BE_SEPARATELY_AUTHORIZED_IN_NEXT_HANDOFF_ASSESSMENT
test: NOT_RUN_DOCS_ONLY
push_status: NOT_PUSHED
candidate_status: CANDIDATE_UNTIL_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD
```

### T1.1 唯一入口与固定身份

唯一链路严格为：

```text
WorkBuddy conversation
  -> one WorkBuddy-managed installed Skill catalog entry
  -> one non-user-facing fixed CLI transport adapter
  -> one accepted launch_session_tool(...)
  -> one immutable LauncherReceiptV1
```

WorkBuddy-managed Skill catalog 是唯一逻辑安装归属；WorkBuddy 的物理安装路径仍为 `opaque`。Installer/Skill release asset 必须携带并可验证以下逻辑身份，但不得在本规划中猜测磁盘目录：`skill_identity`、`release_identity`、`authority_owner`、`bridge_contract_id`、`interpreter_binding`、`module_name`、`module_sha256`、`request_schema_id/hash`、`result_schema_id/hash`、`fixed_argv`、`fixed_argv_sha256`、`bridge_environment_names` 和 `allowed_provider_environment_names`。同一资产还必须固化并验证该 release 的绝对 package-private interpreter identity/path、固定 module asset identity/hash 与 schema identity/hash；Skill 物理安装路径仍为 opaque，调用者不可选择或替换。上述 release-specific 值必须从同一已验证 Release/Installer 资产读取；缺失、漂移、hash 不匹配或资产来源不明时，在 Stage4 之前停止。

桥梁身份固定为：

```text
bridge_contract_id: golden-key-workbuddy-skill-cli-bridge-v1
request_schema_id: golden-key-workbuddy-skill-cli-request-v1
result_schema_id: golden-key-workbuddy-launcher-receipt-v1
interpreter_binding: LOCATOR_PACKAGE_PYTHON
fixed_argv: ("-I", "-m", "golden_key_openmontage_workbuddy.workbuddy_entry_cli")
console_script: FORBIDDEN
subcommands: FORBIDDEN
shell: false
```

`LOCATOR_PACKAGE_PYTHON`必须是同次 Stage2 `locate_active_package(data_root)` 返回并由 Stage4 接受的 package-private Python；调用者不能从 `PATH`、用户输入、Skill 参数或系统 Python 选择解释器。固定模块是 release-specific Skill/Package 资产的一部分，Installer 写入其 hash 并验证；CLI 只做 transport adapter，不解析业务意图、不选择 Provider/Runtime/Renderer、不创建第二 Agent、不启动服务，不拥有任何子命令。T4 的“不得动态生成/追加 argv”禁止调用者、用户消息或 controls 生成 token；本任务的固定 argv 是 Installer/Skill release asset 预冻结的字面量模板，二者不矛盾，模板 hash 漂移即 fail closed。

### T1.2 单一 stdin envelope（secret-safe）

CLI stdin 只接受一个 `golden-key-workbuddy-skill-cli-request-v1` UTF-8 规范 JSON 对象。canonical 规则只约束 wire encoding、key order、数字形式和末尾换行：`ensure_ascii=False`、`allow_nan=False`、`sort_keys=True`、`separators=(",", ":")`、末尾一个 LF，写完立即关闭；不对 `user_message` 做 NFC/NFD、trim 或换行转换。桥接层只验证 Stage4 既有的 NFC/合法字符串前置：非 NFC、surrogate、无法合法编码为 UTF-8/JSON 或不满足 closed Stage4 string contract 时直接按 exit `64` fail closed；已满足前置的 Unicode code-point sequence 必须原样传给 Stage4，不得改写后重试。根和所有嵌套对象都是 closed shape；缺字段、未知字段、重复字段、类型/版本/规范化错误均为 pre-Stage4 bridge error。固定 envelope 为：

```text
schema_version: "golden-key-workbuddy-skill-cli-request-v1"
bridge_contract_id: "golden-key-workbuddy-skill-cli-bridge-v1"
data_root: str
user_message: str                         # literal，Unicode code-point sequence unchanged，不进argv
executor_controls:
  schema_version: "golden-key-workbuddy-launcher-executor-controls-v1"
  session_id: str
  request_id: str
  timeout_seconds: int
  termination_grace_seconds: int
  result_root: str
  provider_environment_source: "FIXED_CLI_PROCESS_ENV"
  provider_environment_names: tuple[str, ...]  # JSON array；ASCII、大小写折叠唯一、规范排序
package_tool_definition: Mapping             # 完整PackageToolDefinitionV1 wire object，不是摘要
local_capability_evidence: tuple[Mapping, ...] # 每项完整approved definition + original Stage3 fact
cancel_requested: bool
continuation:
  mode: "NONE" | "USER_CONFIRMED_NEW_REQUEST"
  prior_request_id: null | str
```

stdin **没有** `executor_controls.provider_environment` 或任何 secret value。`provider_environment_names` 只能是当前完整 `PackageToolDefinitionV1.allowed_environment_names` 的已授权子集；名称不允许重复、越权、动态拼接或由 `user_message` 推导。`package_tool_definition` 必须保持 Stage4 的完整 closed wire object；`local_capability_evidence` 每项必须保持 Stage4 所需的完整 `approved_capability_definition`、`approved_capability_definition_sha256`、未改写 `original_stage3_fact` 和 `original_stage3_fact_sha256`，不得只传摘要或 identity hash。`data_root/result_root` 的 PackageRoot、reparse、权限和归属验证仍由 Stage4/Locator 完成，CLI 不扫盘、不猜路径。

CLI 只从自身进程环境读取 envelope 明确列出的 provider names；它先按 release asset 的 closed `bridge_environment_names` 验证进程环境名称集合必须精确等于“固定桥梁运行时名称 + envelope `provider_environment_names`”，缺失、额外或不允许名称均为 pre-Stage4 fail closed。CLI 不读取未声明变量的 value，不继承或转发整份宿主环境；读取到的值只在内存中重建 Stage4 `executor_controls.provider_environment`，随后由 Stage4 按 `allowed_environment_names` 再验证并仅注入固定 child 环境。Provider secret value 不进入 stdin、argv、stdout、stderr、任何 hash、长度、异常、日志、receipt 或 continuation 字段；不能证明该 provenance 时必须停止。

### T1.3 一次调用与固定输出

解析成功且环境/bridge asset 通过后，CLI 只执行一次：

```text
launch_session_tool(
  data_root,
  literal user_message,
  reconstructed executor_controls,
  complete package_tool_definition,
  complete local_capability_evidence,
  local cancel_event,
)
```

不得 retry、replay、并行调用、第二 Skill、MCP、第二 Agent、Provider 选择或命令生成。Stage4 仍是唯一拥有 Locator、Package/tool preflight、固定 child spawn 和 `LauncherReceiptV1` 裁决的消费者；CLI 不复制 Stage4 控制面。

stdout 只允许一个 UTF-8 规范 JSON mapping，根 `schema_version` 必须是 `golden-key-workbuddy-launcher-receipt-v1`，其余字段逐字段、逐嵌套对象对应 immutable `LauncherReceiptV1` 全字段 wire mapping；不得包装成摘要、改变 outcome/reason、删字段或添加动态字段。Stage4 返回九值中的任何非成功 receipt 也必须原样序列化为该 mapping，CLI 不改写失败为成功。stderr 只允许预冻结、脱敏的固定诊断 token（例如 `BRIDGE_INPUT_INVALID`、`BRIDGE_ENVIRONMENT_INVALID`、`BRIDGE_ASSET_INVALID`、`BRIDGE_OUTPUT_INVALID`），不得输出异常、路径、命令、用户消息、secret、hash、长度或 child 原文。

pre-Stage4 JSON、schema、bridge identity、cancel/continuation envelope 或 user-message 编码错误：Stage4 调用次数为0，stdout 为空，stderr 仅固定 token。固定 asset、process-env 或 provider-name 配置/secret provenance 错误同样在 Stage4 前停止；不得伪造 `LauncherReceiptV1`。transport exit code 闭集固定为：`0` = Stage4 恰好调用一次且完整 receipt 已缓冲、验证、序列化并输出（任何真实 receipt outcome，包括失败，均为 `0`）；`64` = input/schema/bridge identity/cancel/continuation envelope 无效；`78` = fixed release asset、process-environment 或 provider-name 配置/provenance 无效；`70` = bridge internal failure，或 Stage4 调用后完整 receipt 序列化/输出前验证失败。除 `0/64/70/78` 外不得使用其他 transport exit code；stdout 必须先完整缓冲并验证，任一错误时保持为空。若 Stage4 已被调用但 receipt 无法按完整 schema 序列化，同样不得输出伪造 receipt，使用 `70`；Stage4 返回失败 receipt 仍退出 `0` 并由 WorkBuddy 消费真实 outcome。Stage4 的 child secret-nondisclosure、`spawn_count<=1`、`retry_count=0`、stdout/stderr 污染检测和11级优先级保持原合同，不由 CLI 重排。

### T1.4 取消与同任务继续

CLI 解析 `cancel_requested` 后创建本地 `threading.Event`：`true` 先 `set()`，`false` 传未 set 的 event 或 `None`；随后仍只调用 Stage4 一次。这样只冻结入口前 `CANCELLED/CANCELLED_BEFORE_SPAWN` 的真实语义；本规划不发明运行中取消信号、后台 watcher、IPC 或常驻服务。运行中 Host 终止/timeout 的实现和 T5 验收另行处理，CLI 不伪造 receipt。`continuation.mode=USER_CONFIRMED_NEW_REQUEST` 只表示用户明确决定发起一个带新 `request_id` 和新 envelope 的新请求，`prior_request_id` 只作审计关联；CLI 不读取旧消息、不自动重放、不把 continuation 当重试。

### T1.5 失败边界、下一步与授权

有效 envelope 但 Stage4 定义/能力/Locator/preflight 失败，必须仍由 Stage4 真实调用一次并返回其既定 receipt；只有 JSON/bridge/env/asset 无法安全进入 Stage4 的错误才是“无 receipt 的 pre-Stage4 bridge error”。两者不得混淆。任何动态命令、额外 argv、console-script、MCP/第二入口、secret value 进入非授权域、完整能力定义被摘要化、receipt 字段丢失/改写、重试/重放、第二 Agent 或第 N+1 生产路径，均 `STOPPED_SCOPE_EXPANSION`/`INCOMPLETE`。

本节只把合同冻结为 `FROZEN_FOR_PLANNING`；不冻结 WorkBuddy 物理目录，不生成真实 Skill/Installer 资产，不写代码/测试/CI，不运行客户端/Python/Stage4/Provider/媒体/Package/Registration/Stage6。下游实现白名单、tracked 迁移和测试命令已由当前 docs-only closeout 候选另行冻结；本历史段不得覆盖本文末的当前候选状态。

## [HISTORICAL / SUPERSEDED_BY_V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1] Stage 5规划收口与实施交接候选（`V2-S5-PLANNING-CLOSEOUT-IMPLEMENTATION-HANDOFF-ASSESSMENT1`，2026-08-21）

本节是前一轮六文档 docs-only authority-sync/closeout 候选及其历史条件。后续 Builder 已消费该 handoff 并完成实施；当前实施结果与本轮 `V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1` 以本文末新的 live mirror 为准。

```text
task_id: V2-S5-PLANNING-CLOSEOUT-IMPLEMENTATION-HANDOFF-ASSESSMENT1
task_kind: STAGE5_PLANNING_CLOSEOUT_AND_IMPLEMENTATION_HANDOFF / DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE
base_commit: e0bd0c45c9deec233b27b63f018fa6b4b89aab1a
base_tree: 79a2b44d0a7dcd52a1f8be168ee408dfab1ea17d
tracked_files_at_base: 37
initial_product_goal_recheck: PASS
user_authorization: 2026-08-21 / 启动阶段五实施
candidate_allowed_docs: AGENT_GUIDE.md; PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md; docs/workbuddy/v2/DRIFT-GUARD.md
candidate_result: STAGE5_PLANNING_PASS_ACCEPTED / EFFECTIVE_ONLY_AFTER_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD
stage_5_planning_after_candidate: PASS_ACCEPTED
stage_5_implementation_authorization_after_candidate: EXPLICIT_USER_AUTHORIZED / PENDING_BUILDER_TAKEOVER_FROM_LATEST_FORMAL
stage_5_real_workbuddy_production_acceptance: NOT_GRANTED / FINAL_PACKAGE_AND_REAL_CLIENT_EVIDENCE_PENDING
current_task_after_candidate: NONE
next_authorized_task_after_candidate: V2-S5-WORKBUDDY-ENTRY-BUILDER1
candidate_test: NOT_RUN_DOCS_ONLY
candidate_push: NOT_PUSHED
```

### 当前冻结的未来 Builder 最小实现白名单

唯一入口源资产为 `workbuddy-skill/golden-key-openmontage/SKILL.md`。这是仓库内唯一 WorkBuddy Skill 源资产；既有客户端已证明 folder/ZIP root `SKILL.md`、name/description YAML 的最小导入形态。WorkBuddy 实际安装路径仍保持 opaque。最终 Installer/Package gate 必须把该源资产与 release identity、owner、固定 CLI module/schema/argv/environment hash 绑定后物化；任何未解析 placeholder、身份漂移或来源不明均 fail closed，不能作为生产安装或真实客户端 PASS。

唯一生产模块为 `golden_key_openmontage_workbuddy/workbuddy_entry_cli.py`，只作 package-private `-I -m` transport adapter，不加入 `__init__.py` 公共导出，不建立 console script、子命令、路由、第二入口或第二控制面。唯一直接测试为 `tests/workbuddy/test_workbuddy_entry_cli.py`，覆盖 fixed envelope、literal message 原样、secret non-disclosure、pre-Stage4 fail-closed、一次 Stage4 调用、receipt/exit `0/64/70/78`、cancel/continuation 和无 retry/replay。

现有验收基础设施只允许两项同步：`tests/workbuddy/test_repository_hygiene.py` 更新固定 tracked/source inventory、唯一 Skill 源资产和 package-private module 断言；`.github/workflows/ci.yml` 仅把新直接测试加入现有唯一 pytest 命令，不改触发器、Python 版本或其他 CI 语义。`__init__.py`、`pyproject.toml`、`docs/workbuddy/v2/MODULE-DISPOSITION.md` 和其他文件均拒绝加入：现有 package 已自动包含新增 `.py`，且 pyproject 禁止 console script；Module-Disposition 既有唯一入口/CLI受控适配边界足够；Installer/最终 Package gate 承担 release 资产承载，不在本 Builder 伪造物理客户端路径。

tracked 目标精确为 `37 -> 40`（新增三项：Skill 源资产、CLI 模块、直接测试；hygiene/CI 为现有文件修改）。Builder 必须使用 D 盘 task-private 环境 `D:\BlazingCD\Personal\Temp\workbuddy-v2-s5-entry-builder1\.venv`，不得混用全局包。

固定命令（Builder 以该 `.venv\Scripts\python.exe` 执行；CI 使用同一 pytest 参数序列）：

```text
direct:  python -m pytest -p no:cacheprovider tests/workbuddy/test_workbuddy_entry_cli.py -q
hygiene: python -m pytest -p no:cacheprovider tests/workbuddy/test_repository_hygiene.py -q
full/CI: python -m pytest -p no:cacheprovider tests/workbuddy/test_package_registration.py tests/workbuddy/test_runtime_prepare.py tests/workbuddy/test_session_launcher.py tests/workbuddy/test_workbuddy_entry_cli.py tests/workbuddy/test_repository_hygiene.py -q
```

实施仍需 Builder commit、独立 zero-write Reviewer `APPROVE / P0=0 / P1=0 / P2=0`、ordinary fast-forward、tracked/clean/untracked/stash 验证和临时现场清理。该候选不冒充实施完成；真实 WorkBuddy 新会话、唯一入口命中、原话/授权/继续、最终 Package/Registration、Provider、媒体和业务效果仍是后续独立证据层。

## Stage 5 T1 Evidence1收口与受控客户端证据授权候选（2026-08-21）

本节是当前两文档授权候选的唯一新增任务边界。它机械收口已完成的官方 Evidence1，不改变其 `T1_EVIDENCE_INCOMPLETE` 结论；同时只把下一项受控客户端核验任务固化为条件授权。候选进入 formal 前 `current_task=NONE`、`next_authorized_task=NONE` 是历史/授权前状态；只有本候选经独立零写 Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 并普通 fast-forward 进入 `origin/codex/workbuddy-shell-v2` 后，顶部 live direct 才生效为唯一的 `V2-S5-T1-CONTROLLED-CLIENT-EVIDENCE1`。

```text
task_id: V2-S5-T1-EVIDENCE1-CLOSEOUT-AND-CONTROLLED-CLIENT-AUTHORIZATION1
task_kind: STAGE5_T1_EVIDENCE1_CLOSEOUT_AND_CONTROLLED_CLIENT_AUTHORIZATION / DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE
user_authorization: 2026-08-21 / 授权执行T1 Evidence1两文档机械收口，并启动受控真实WorkBuddy客户端证据核验；仅允许隔离工作区和临时无副作用Skill，禁止Provider、媒体、最终Package和Stage4真实spawn，额外权限必须停止。
base_commit: d11513907c3662b18fd06a200fac935efcb50055
base_tree: 81e38bc90dd37d586b46e20cc047db35b613759d
tracked_files_at_base: 37
candidate_branch: codex/v2-s5-t1-client-evidence-authorization1
candidate_worktree: D:\\BlazingCD\\Personal\\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2-s5-t1-client-auth1
formal_target_branch: origin/codex/workbuddy-shell-v2
candidate_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md
candidate_production_code_changes: 0
candidate_test_changes: 0
candidate_ci_changes: 0
candidate_package_registration_changes: 0
candidate_external_writes: NONE
candidate_real_workbuddy_execution: NOT_PERFORMED_IN_THIS_AUTHORIZATION_TASK
candidate_launcher_provider_media_wsl_execution: NOT_PERFORMED_IN_THIS_AUTHORIZATION_TASK
candidate_test: NOT_RUN_DOCS_ONLY
evidence1_candidate_result: d11513907c3662b18fd06a200fac935efcb50055 / tree 81e38bc90dd37d586b46e20cc047db35b613759d / T1_EVIDENCE_INCOMPLETE
evidence1_independent_review: APPROVE / P0=0 / P1=0 / P2=0
evidence1_formal_promotion: ORDINARY_FAST_FORWARD / FORMALLY_PROMOTED
stage_5_planning: PLANNING_BLOCKED_EXTERNAL_CONTRACT
stage_5_implementation_authorization: NOT_GRANTED
current_task_before_promotion: NONE
next_authorized_task_before_promotion: NONE / HISTORICAL_PRE_AUTHORIZATION
next_authorized_task_after_promotion: V2-S5-T1-CONTROLLED-CLIENT-EVIDENCE1 / ONLY_AFTER_THIS_COMMIT_IS_FORMAL
candidate_status: CANDIDATE_UNTIL_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD
```

### 后续唯一受控客户端任务：`V2-S5-T1-CONTROLLED-CLIENT-EVIDENCE1`

该任务只核查 T1 的五项缺口，不写生产代码、不运行生产流程、不解除规划硬阻断。它必须从本候选正式推广后的最新 formal 精确接管；客户端任务结束后 `current_task=NONE`、`next_authorized_task=NONE`，除非另行授权。

固定边界：

- 只操作预先存在的腾讯 WorkBuddy 客户端和现有登录态。若未登录或出现认证界面，立即停止并交用户处理，不自动认证。
- 隔离根固定为 `D:\\BlazingCD\\Temp\\Golden_Key_WorkBuddy_S5_T1_Client_Evidence1`；任务开始前必须验证精确绝对路径，禁止写 C 盘或项目生产目录。
- 第一阶段只观察 UI、客户端版本、Skill 入口/创建/导入页面和可见格式说明；不得猜 Skill 结构、schema、安装根、入口名或调用协议。
- 只有客户端 UI 或官方可见模板明确给出包格式后，才可以创建临时、无副作用 candidate Skill。candidate Skill 只能返回一个非敏感静态诊断标记并声明不执行工具；不得含脚本、命令、CLI、MCP、网络、文件读写、Python 执行、Stage 4 调用、Provider、媒体或生产逻辑。
- 导入/安装页面可以观察和导航；实际“上传/导入/安装/启用”是客户端状态改变，动作当时必须再次取得用户确认后才能点击，即使已有总体授权。
- 任何登录、Windows/浏览器权限、安全或隐私设置、管理员权限、额外目录、全局安装、插件/扩展安装、外部网络/第三方服务、收费、Provider、媒体、final Package、production Registration 或 Stage 4 真实 spawn 请求，立即 `STOP`；不接受权限提示。
- 不发送用户敏感数据；candidate Skill 只含非敏感静态诊断文本；不得打开终端或通过 UI 运行命令。

五项取证固定为：

1. Skill 包结构与 schema；
2. 安装/导入归属以及物理、用户级或项目级语义；
3. 显式调用主体、入口和触发机制；
4. 唯一消费者及其与 WorkBuddy 唯一 Agent 边界的关系；
5. 不生成 CLI、MCP、命令、argv 或 Shell 字符串即可直接调用已接受 Stage 4 Python API `launch_session_tool(...)` 的精确协议。

客户端不能证明的项目必须记为 `UNPROVED_CLIENT`，不得从 UI 文案、外部脚本能力、目录名称、自然语言触发或旧 V1 Skill 推断。Python 直调只允许检查 UI、模板、文档或可见合同；若要真实执行 Python 或 Stage 4 spawn，立即停止并记缺口。

证据与清理规则固定为：

- 后续客户端结果只能作为现有四份权威文档的后续候选写回：`PROJECT-STATE.md`、`docs/workbuddy/v2/TASK-REGISTER.md`、`docs/workbuddy/v2/PROJECT-CHARTER.md`、`docs/workbuddy/v2/ACCEPTANCE-MATRIX.md`；不得新增平行报告。
- 证据固化后清理临时 Skill 和隔离工作区；删除若触发 Windows UI 确认，必须在动作当时重新确认，或仅对已核验精确 D 盘路径执行项目规则允许的清理。正式文档只保留非敏感文字证据。
- 后续客户端任务仍禁止 Provider、媒体、最终 Package、production Registration、Stage 4 真实 spawn、Stage 6、CLI/MCP、第二 Skill、第二 Agent、并行入口；任何额外权限或范围要求均停止并报告 `INCOMPLETE`/`STOPPED_SCOPE_EXPANSION`。

本授权候选本身只修改本账本与 `PROJECT-STATE.md`，`test=NOT_RUN_DOCS_ONLY`；不打开 WorkBuddy、不创建/上传/安装 Skill、不运行代码/测试/CI/Launcher/Provider/媒体/WSL、不物化 Package、不创建 Registration、不启动 Stage 6。Reviewer 只审本候选的两文件差异及条件化下一任务，不能把 `T1_EVIDENCE_INCOMPLETE` 改为 `PASS_ACCEPTED`，也不能把 Stage 5 实现变为已授权。

## Stage 5 T1受控真实WorkBuddy客户端证据候选结果（2026-08-21）

该候选只消费上一节正式授权，任务级事实以本节为唯一权威。接管基线为 `5c7d76190be4cb76afafb5d32798219e09630153`、tree `9f042420ed82ac01ffacabc650cb2a0a42a49c74`、tracked 37；工作分支为 `codex/v2-s5-t1-controlled-client-evidence1`。用户在取证前已自行卸载两个旧 V1 Skill；该用户状态变化只用于建立零已安装 Skill 的干净观测起点，不证明新生产入口，也不是 Builder 删除动作。

```text
task_id: V2-S5-T1-CONTROLLED-CLIENT-EVIDENCE1
task_kind: STAGE5_T1_CONTROLLED_REAL_CLIENT_EVIDENCE / DOCS_ONLY_CLOSEOUT / ZERO_PRODUCT_CODE_CHANGE
base_commit: 5c7d76190be4cb76afafb5d32798219e09630153
base_tree: 9f042420ed82ac01ffacabc650cb2a0a42a49c74
tracked_files_at_base: 37
candidate_branch: codex/v2-s5-t1-controlled-client-evidence1
candidate_worktree: D:\\BlazingCD\\Personal\\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2-s5-t1-client-evidence1
isolation_root: D:\\BlazingCD\\Temp\\Golden_Key_WorkBuddy_S5_T1_Client_Evidence1
workbuddy_version: 5.3.13
required_test_model: HY3
candidate_skill_name: golden-key-s5-t1-noop-evidence
candidate_skill_source: D:\\BlazingCD\\Temp\\Golden_Key_WorkBuddy_S5_T1_Client_Evidence1\\t1-controlled-noop-skill\\SKILL.md
candidate_skill_zip: D:\\BlazingCD\\Temp\\Golden_Key_WorkBuddy_S5_T1_Client_Evidence1\\golden-key-s5-t1-noop-evidence.zip
candidate_skill_zip_sha256: 08AA43E11DD1BBBABA53A8DED33B60FB7E4FF0B26129800974F61342A8F4EBB5
hy3_invocation_result: T1_CONTROLLED_NOOP_OK / completed 8s / response labeled Hy3
auto_probe_result: T1_CONTROLLED_NOOP_OK / EXCLUDED_FROM_FINAL_MODEL_EVIDENCE / response labeled Auto (GLM-5.2)
permission_or_risk_prompt: NONE_OBSERVED
client_state_change: ONE_TEMPORARY_SKILL_INSTALLED_THEN_USER_UNINSTALLED / FINAL_CLIENT_INSTALLED_SKILLS_0
code_test_ci_launcher_provider_media_final_package_registration_stage4_spawn: NOT_RUN
candidate_result: T1_CLIENT_EVIDENCE_INCOMPLETE
stage_5_planning: PLANNING_BLOCKED_EXTERNAL_CONTRACT
stage_5_implementation_authorization: NOT_GRANTED
current_task_after_candidate: NONE
next_authorized_task_after_candidate: NONE
cleanup_status: COMPLETE / USER_UNINSTALLED_TEMPORARY_SKILL / CLIENT_INSTALLED_SKILLS_0 / D_DRIVE_ISOLATION_RECYCLED / SOURCE_PATH_ABSENT
candidate_status: CANDIDATE_UNTIL_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD
```

### 客户端机械证据

| 观测 | 客户端直接事实 | 裁决边界 |
|---|---|---|
| 干净起点 | WorkBuddy `5.3.13` 的“我安装的”按钮无计数，随后导入完成后显示 1；已安装页仅见 `golden-key-s5-t1-noop-evidence` | 证明本次会话开始时 UI 已安装集合从 0 变 1；不证明磁盘上不存在历史残留 |
| 导入格式 | 上传页明确接受包含 `SKILL.md` 的文件夹或 `.zip`；`.md` 的 YAML 需要 Skill 名称和描述 | 证明成功导入所需最小可见合同；没有证明完整 schema、所有可选文件或目录树 |
| 安全检测与安装 | 未选择“跳过检测，直接安装”；客户端先显示“安全检测中...”，完成后自动安装并在“我安装的”显示 exact name/description | 证明该 ZIP 经过客户端默认检测路径且成为当前用户可见已安装项；不证明检测内部规则或物理落点 |
| 显式入口 | 新任务输入框提示“`/` 调用技能与指令”；发送 `/golden-key-s5-t1-noop-evidence` 后形成 Skill chip、任务标题“访问 golden-key-s5-t1-noop-evidence”，响应过程显示“加载技能 golden-key-s5-t1-noop-evidence” | 证明当前版本/登录态/会话的显式 slash 触发和 exact Skill 绑定；不外推全部版本或其他入口 |
| HY3结果 | 用户要求不用 Auto 后，界面记录“模型已从 Auto 更改为 Hy3”；第二次 exact Skill 调用 8 秒完成，精确返回 `T1_CONTROLLED_NOOP_OK`，响应底部标注 `Hy3` | 这是最终模型证据；第一次 `Auto (GLM-5.2)` 结果仅为探测历史，排除出 HY3 验收 |
| 权限与副作用 | 整个导入/调用未出现登录、管理员、Windows/浏览器、隐私或额外目录权限提示；Skill 只返回静态标记 | 只证明本次受控路径未观察到额外权限；不证明客户端全局安全属性 |

### T1五项客户端裁决

| T1 项目 | 客户端状态 | 直接证明 | 仍缺口 |
|---|---|---|---|
| Skill 包结构/必需文件/schema | `PARTIALLY_PROVED_CLIENT` | root `SKILL.md` ZIP 成功导入；上传页要求 `SKILL.md`，且 Markdown YAML 含 name/description | 完整 schema、可选目录树、其他允许/禁止文件未给出 |
| 安装/导入归属与物理位置 | `PARTIALLY_PROVED_CLIENT` | 当前客户端“我安装的”集合从 0 变 1，并显示 exact Skill 身份 | 物理安装路径、账号/设备/工作区/项目的完整所有权与同步语义未显示 |
| 显式调用主体/入口/触发 | `PROVED_CLIENT_FOR_5.3.13_SESSION` | WorkBuddy 新任务输入框的 slash 入口命中 exact Skill；HY3 返回 exact marker | 不外推其他版本、账号或客户端；生产 Stage4 入口尚未实现/运行 |
| 唯一消费者/WorkBuddy唯一Agent边界 | `PARTIALLY_PROVED_CLIENT` | 干净起点仅一个临时已安装 Skill；调用、加载、响应均由同一 WorkBuddy UI 呈现 | 不能从 UI 证明全局唯一消费者、无第二 Agent、无其他 dispatch/CLI/MCP入口 |
| Stage4 Python直调协议 | `UNPROVED_CLIENT` | 客户端没有展示 Python 模块加载、参数或 receipt 合同 | 依授权禁止 Python/Stage4 真实 spawn，故未证明零命令/argv/Shell 的 `launch_session_tool(...)` 直调与 `LauncherReceiptV1` 回传 |

五项没有全部闭合，总结果必须为 `T1_CLIENT_EVIDENCE_INCOMPLETE`。它加强了真实 WorkBuddy `5.3.13` 的最小导入与 slash 调用合同，但没有解除 `PLANNING_BLOCKED_EXTERNAL_CONTRACT`，没有授权 Stage 5 实现，也不证明生产 Package、Registration、Provider、媒体、业务结果或 Stage 6。取证后由用户在 WorkBuddy 内手动卸载唯一临时 Skill；重新置前核验“我安装的”页面显示“还没有安装任何技能”。已核验的精确 D 盘隔离根随后以可恢复方式移入 Windows 回收站，源路径不存在；WorkBuddy 任务历史未删除。

## Stage 5内部T1 Evidence2授权候选（2026-08-21）

本节是 Stage 5 内部 T1 的极窄 Evidence2 授权候选，不是 Stage 5 的前置阶段或前置任务。它只授权继续闭合 T1 的外部 Skill/入口合同证据，不授权 Stage 5 实现、真实生产流程或任何替代接口设计。用户授权为 2026-08-21 的“那继续吧”。本候选进入 formal 前，顶部 `next_authorized_task` 只表达条件候选；只有本候选经独立零写 Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 并以普通 fast-forward 进入 formal，`V2-S5-T1-CONTRACT-CLOSURE-EVIDENCE2` 才成为唯一有效下一任务。

```text
task_id: V2-S5-T1-CONTRACT-CLOSURE-EVIDENCE2
task_kind: STAGE5_T1_CONTRACT_CLOSURE_EVIDENCE2_AUTHORIZATION / DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE
user_authorization: 2026-08-21 / “那继续吧”
base_commit: e1ce084a2b536daf6c8519af8d183d586ee641b6
base_tree: 0ab36de0e8d084c8dc0eeec696fad615da40c15e
tracked_files_at_base: 37
candidate_branch: codex/v2-s5-t1-evidence2-authorization1
candidate_worktree: D:\\BlazingCD\\Personal\\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2-s5-t1-evidence2-auth1
formal_target_branch: origin/codex/workbuddy-shell-v2
candidate_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md
candidate_max_documents: 2
candidate_production_code_changes: 0
candidate_test_changes: 0
candidate_ci_changes: 0
candidate_package_registration_changes: 0
candidate_external_writes: NONE
candidate_test: NOT_RUN_DOCS_ONLY
candidate_real_workbuddy_execution: READ_ONLY_OBSERVATION_ONLY_IF_SEPARATELY_TAKEN_OVER
candidate_launcher_provider_media_stage4_python_stage4_spawn_final_package_registration_stage6: NOT_PERMITTED
stage_5_planning: PLANNING_BLOCKED_EXTERNAL_CONTRACT
stage_5_implementation_authorization: NOT_GRANTED
current_task: NONE
next_authorized_task_before_promotion: NONE / HISTORICAL_PRE_AUTHORIZATION
next_authorized_task_after_promotion: V2-S5-T1-CONTRACT-CLOSURE-EVIDENCE2 / ONLY_AFTER_THIS_CANDIDATE_IS_INDEPENDENTLY_APPROVED_AND_ORDINARY_FAST_FORWARD_TO_FORMAL
candidate_status: CANDIDATE_UNTIL_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD
```

Evidence2 的只读核查范围严格限定为：

- 腾讯/WorkBuddy 官方 Skill 创建规范、完整 package/schema、物理安装路径，以及 user/workspace/project 归属与优先级语义；
- 当前 WorkBuddy 版本可见的 slash 入口、dispatch/选择绑定和唯一消费者/WorkBuddy 唯一 Agent 边界；
- 官方支持的本地工具/API 机制，重点核查是否存在不生成 CLI、MCP、命令、argv 或 Shell 字符串即可直接调用已接受 `launch_session_tool(...)` 并逐字段返回 `LauncherReceiptV1` 的真实合同；
- 受控客户端如被正式接管，只能只读查看官方创建指南、Skill 详情或已安装 Skill 的“打开文件夹”内容，不得上传、安装、启用或调用 Skill。

本候选及其后续 Evidence2 均禁止设置变更、敏感数据、代码、测试、CI、Python、Stage 4 真实 spawn、CLI、MCP、命令/argv/Shell 探针、Provider、媒体、final Package、production Registration 和 Stage 6。只能使用既有登录态；遇到登录、权限、安装、写入或收费提示立即 `STOP`，不得接受或绕过。Evidence2 最多修改本节所列两份文档，`test=NOT_RUN_DOCS_ONLY`。

上一轮受控客户端证据继续保留为历史/候选事实：WorkBuddy `5.3.13`、HY3 下临时 no-op Skill 导入和 slash 命中成功，但总裁决仍为 `T1_CLIENT_EVIDENCE_INCOMPLETE`，并已完成卸载/清理；不得把它改写为完整合同或 `PASS_ACCEPTED`。

`[HISTORICAL / SUPERSEDED_BY_CLI_BOUNDARY_CORRECTION]` 本授权候选当时把“不能证明零 CLI/MCP/命令/argv/Shell 的 `launch_session_tool(...)` 直调合同”作为 `ARCHITECTURE_CONTRACT_UNAVAILABLE` 条件；该条件保留为历史裁决，不再作为当前排他门槛。当前规则是继续核验唯一 WorkBuddy Skill 内部固定 CLI 是否为受控桥梁，且仍禁止第二入口、并行控制面、失败兜底和任意命令生成；该授权候选本身不推进 formal。

## Stage 5内部T1 Evidence2结果候选（2026-08-21）

本节消费上一节已经正式生效的 `V2-S5-T1-CONTRACT-CLOSURE-EVIDENCE2` 授权，只记录本轮允许的官方资料与受控客户端只读证据结果。Evidence2 是 Stage 5 内部 T1 的执行，不是 Stage 5 的前置阶段或前置任务；本候选不授权 Stage 5 实现、真实生产流程或任何替代接口。**本节为 HISTORICAL RESULT，已由上方 CLI 边界纠偏 supersede；历史证据与原始结果保留，但当前任务不得再把 CLI 存在本身当作架构阻断。**候选未推广前，formal 仍以 `4515268d1f77211a14f22927a02344b578527c4a`、tree `45b351bbf60419dc76833ddfcd61cd2ef52ff24c`、tracked 37 为权威；只有本候选经独立零写 Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 并以普通 fast-forward 进入 `origin/codex/workbuddy-shell-v2` 后，以下结果与“授权消费完成且无下一任务”才成为 formal live 状态。

```text
task_id: V2-S5-T1-CONTRACT-CLOSURE-EVIDENCE2
task_kind: STAGE5_T1_CONTRACT_CLOSURE_EVIDENCE2_RESULT / DOCS_ONLY_CLOSEOUT / ZERO_PRODUCT_STATE_CHANGE
authorization_consumption: V2-S5-T1-CONTRACT-CLOSURE-EVIDENCE2 / CONSUMED_BY_THIS_CANDIDATE_RESULT / FORMALLY_CONSUMED_WHEN_THIS_COMMIT_IS_FORMAL
base_commit: 4515268d1f77211a14f22927a02344b578527c4a
base_tree: 45b351bbf60419dc76833ddfcd61cd2ef52ff24c
tracked_files_at_base: 37
formal_authority_before_promotion: 4515268d1f77211a14f22927a02344b578527c4a / tree 45b351bbf60419dc76833ddfcd61cd2ef52ff24c / tracked 37
candidate_branch: codex/v2-s5-t1-evidence2-result1
candidate_worktree: D:\\BlazingCD\\Personal\\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2-s5-t1-evidence2-result1
formal_target_branch: origin/codex/workbuddy-shell-v2
candidate_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md
candidate_production_code_changes: 0
candidate_test_changes: 0
candidate_ci_changes: 0
candidate_package_registration_changes: 0
candidate_external_writes: NONE
candidate_client_operations: READ_ONLY_ONLY
candidate_real_workbuddy_execution: NEW_READ_ONLY_UI_OBSERVATION_ONLY / NO_SKILL_UPLOAD_INSTALL_ENABLE_CALL / NO_TASK_OR_MODEL_CALL
candidate_launcher_provider_media_stage4_python_stage4_spawn_final_package_registration_stage6: NOT_RUN
candidate_test: NOT_RUN_DOCS_ONLY
workbuddy_version_observed: 5.3.13
installed_skill_count_observed: 0
candidate_result: ARCHITECTURE_CONTRACT_UNAVAILABLE
candidate_result_status: HISTORICAL_RESULT / SUPERSEDED_BY_CLI_BOUNDARY_CORRECTION / NOT_CURRENT_PRODUCT_IMPOSSIBILITY
candidate_result_reason: REQUIRED_OFFICIAL_CURRENT_VERIFIABLE_CONTRACT_UNAVAILABLE / NOT_PRODUCT_ABSOLUTE_IMPOSSIBILITY
stage_5_planning_after_result: PLANNING_BLOCKED_EXTERNAL_CONTRACT
stage_5_implementation_authorization_after_result: NOT_GRANTED
current_task_after_result: NONE
current_task_status_after_result: NO_ACTIVE_TASK
next_authorized_task_after_result: NONE
pending_next_authorized_task_after_result: NONE
stage_3_and_stage_4_status: PASS_ACCEPTED / UNCHANGED
stage_6_final_package_production_registration: NOT_GRANTED_OR_UNPROVED
candidate_temp_artifacts: NO_TEMP_SKILL_OR_FILES_CREATED
candidate_status: CANDIDATE_UNTIL_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD / FORMALLY_PROMOTED_WHEN_THIS_COMMIT_IS_FORMAL
```

### Evidence2官方一手来源（仅限腾讯云正式页面）

本轮只把以下五个腾讯云页面作为官方资料来源；页面更新时间按页面自身标注记录，不能扩写为页面未给出的本地实现合同。

| ID | 页面 | 页面更新时间 | 直接支持与边界 |
|---|---|---|---|
| O1 | `https://cloud.tencent.com/document/product/1831/134432`《技能》 | 2026-07-20 19:49:32 | 说明 WorkBuddy Skill 可封装脚本/工作流，UI 路径包括上传、查找、创建，启用后可在对话中召唤或自动调用；未给出完整 package/schema、物理安装位置、用户/工作区/项目归属与优先级，也未给出 Python 模块原生注册、参数或 receipt 合同。 |
| O2 | `https://cloud.tencent.com/document/product/1831/134525`《连接器》 | 2026-07-20 19:49:32 | 公开能力技术形态列为 `MCP + CLI` 与 `Skill + CLI`；历史候选当时按过宽的“禁止 CLI/MCP”条件记录为不满足，但该解释已由 CLI 边界纠偏 supersede。页面只能证明公开支持形态，不能扩写为“产品绝对不可能”，也不能单独证明唯一 Skill 内部固定 CLI 的完整合同。 |
| O3 | `https://cloud.tencent.com/document/product/1831/134391`《新建任务栏（本地 AI 工作台）》 | 2026-08-03 15:25:00 | 说明用户可选择已安装 Skill，WorkBuddy 自动调用；未给出所需 Python 直调、参数承载或 `LauncherReceiptV1` 返回合同。 |
| O4 | `https://cloud.tencent.com/document/product/1831/134324`《WorkBuddy 更新记录》 | 2026-07-30 17:41:50 | 4.8.0 有 Desktop Skills/SkillHub/Marketplace 与斜杠命令模型驱动调用，4.9.1 有导入安全检查，5.1.0 有企业自建 Skill/插件市场与 CLI 连接器修复，5.3.3 有 MCP 本地服务；版本记录仍没有所需原生 Python 函数绑定合同。这里只作支持范围证据，不作排他证明。 |
| O5 | `https://cloud.tencent.com/document/product/1831/134516`《Skills》 | 2026-08-14 09:56:30 | 属于 CodeBuddy Skill 管理/工作区语境，只能作为相邻产品上下文；标记为 `PRODUCT_MISMATCH_NOT_CONTRACT_PROOF`，不得把它转写为 WorkBuddy 5.3.13 的物理安装路径、所有权或优先级合同。 |

五个官方页面合计仍未给出完整 WorkBuddy package/schema、物理安装路径与 user/workspace/project 归属及优先级、当前精确 slash/选择/dispatch 与唯一消费者边界，也未给出在零 CLI/MCP/命令/argv/Shell 条件下原生直调本仓库 `launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)` 并逐字段回传 `LauncherReceiptV1` 的真实合同。O2 的公开支持形态不是绝对不可能证明；它只是不能满足本任务的必要条件。

### 本轮受控客户端只读证据

本轮只记录既有受控客户端的只读观察，不上传、安装、启用或调用 Skill，不发送 WorkBuddy 任务，不改变设置，不进行登录或权限操作，不接受收费/外部服务提示，也没有模型调用：

- WorkBuddy `5.3.13` 的“我安装的”显示没有任何技能，`installed_skill_count=0`；“添加技能”菜单仅显示“查找技能 / 上传技能 / 创建技能”。本轮没有新建临时 Skill。
- 搜索“技能创建指南”得到推荐结果与 SkillHub 结果；详情属于 SkillHub/ClawHub 社区包。其源视图只显示 `name/category/version/author` 及说明，不是腾讯官方工具绑定合同。
- 抽查推荐“腾讯微云”`v1.0.5` 的详情/源视图，仅显示 `name/slug/version` 与说明正文，没有工具注册、Python import、参数 schema 或 receipt schema。
- 上一轮 `5.3.13` 客户端的 HY3 证据只作为历史记录保留；HY3 不属于本轮新观察，不得把本轮结果写成使用了 HY3。

### T1五项Evidence2裁决

| T1 项目 | 建议状态 | 本轮可保留的证明 | 仍未证明与边界 |
|---|---|---|---|
| 1. 完整 WorkBuddy Skill package/schema | `UNPROVED_OFFICIAL_CURRENT` | O1 只证明 Skill 可封装脚本/工作流并可通过 UI 上传、查找、创建；当前客户端未安装任何 Skill，不能从社区包源视图补齐官方 schema。 | 完整包文件、目录树、必需/可选文件、版本与校验规则未给出。 |
| 2. 物理安装路径、user/workspace/project 归属与优先级 | `UNPROVED_OFFICIAL_CURRENT` | O1/O3 只证明“已安装 Skill”可被选择/自动调用；O5 是相邻产品，不能作为 WorkBuddy 路径证据。 | 物理落点、所有权、同步/持久化、层级优先级未给出；不得把 CodeBuddy 语境写成 WorkBuddy 路径。 |
| 3. slash/选择/自动 dispatch | `PARTIALLY_PROVED_OFFICIAL / PROVED_CLIENT_FOR_SESSION (HISTORICAL_5.3.13_HY3)` | O1/O3/O4 证明公开的选择/自动调用与斜杠模型驱动范围；上一轮 HY3 记录证明当时会话命中临时 Skill。 | 当前本轮未安装/未调用 Skill；全局唯一消费者与无替代 dispatch 仍为 `UNPROVED`，不得外推为本仓库入口合同。 |
| 4. 唯一消费者与 WorkBuddy 唯一 Agent 边界 | `PROJECT_BOUNDARY_ONLY / NOT_PUBLIC_PRODUCT_PROOF` | 本仓库 AGENT_GUIDE 的项目边界仍规定 WorkBuddy 是唯一运行 Agent。 | 这是项目治理边界，不是官方产品公开证明；全局唯一消费者、无第二 Agent/并行入口仍未证实。 |
| 5. 零 CLI/MCP/命令/argv/Shell 原生直调 `launch_session_tool(...)` 并逐字段回传 `LauncherReceiptV1` | `UNAVAILABLE_REQUIRED_CONTRACT` | 允许的官方资料和受控客户端只读观察均未给出模块加载方式、精确参数 schema、literal `user_message`/`executor_controls` 分离、返回类型或 receipt 字段合同；O2 公开形态明确包含 CLI，不能替代所需直调证明。 | 所需的官方/当前可验证合同不可用；这不是“产品绝对不可能”。 |

五项未闭合，故本候选的总裁决固定为 `candidate_result=ARCHITECTURE_CONTRACT_UNAVAILABLE`。该裁决只表示在本轮允许的官方资料与受控客户端只读证据中，所需的官方/当前可验证合同不可用；不声称产品绝对不可能。T1 与 Stage 5 继续 `stage_5_planning=PLANNING_BLOCKED_EXTERNAL_CONTRACT`，`stage_5_implementation_authorization=NOT_GRANTED`，`current_task=NONE`，`current_task_status=NO_ACTIVE_TASK`，结果后的 `next_authorized_task=NONE`、`pending_next_authorized_task=NONE`。不得提出或授权替代接口、第二 Skill、第二 Agent、CLI/MCP 旁路；Stage 3/4 既有 `PASS_ACCEPTED` 不变，Stage 6、final Package 与 production registration 仍未授权或未证明。

### 机械收口与治理门

本候选仅修改本账本与 `PROJECT-STATE.md` 两个白名单路径；production code/test/CI/Package/Registration 变更均为 0，客户端操作为 `READ_ONLY_ONLY`，清理为 `NO_TEMP_SKILL_OR_FILES_CREATED`。结果候选仍须独立零写 Reviewer 审查并普通 fast-forward；在此之前，本节是候选结果，不改变 formal 的 `4515268d1f77211a14f22927a02344b578527c4a` 权威。若审查与普通 FF 完成，Evidence2 授权历史才标为 consumed candidate/result，formal live 的 `next_authorized_task` 与 `pending_next_authorized_task` 均保持 `NONE`。

## [HISTORICAL / SUPERSEDED_BY_V2-S5-R00-REMAINDER-PLAN-STATE-CORRECTION1] Stage 5实施完成与入口收口候选（`V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1`，2026-08-21）

本节是前一轮六文档 closeout 的历史镜像；它保留入口代码已交付的事实，但旧的整体 `PASS_ACCEPTED`/closeout 表述已被当前 R00 状态纠偏取代。当前 Stage5 状态、五类最终证据和 R01-R08 任务链以本文末新的 R00 live mirror 为准。

```text
task_id: V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1
task_kind: STAGE5_IMPLEMENTATION_CLOSEOUT / DOCS_ONLY / EXACT_6_PATHS / ZERO_PRODUCT_STATE_CHANGE
base_commit: 0e7a0be65877b03fb386e1c6c6bc258c0b27db6c
base_tree: 85c266edb7349c940e8cd45870cc0538c95726c0
base_parent: aa70c2cf9b6b4a29517d7354f0239ea0cdc9a5d3
tracked_files_at_base: 40
initial_product_goal_recheck: PASS
implementation_task: V2-S5-WORKBUDDY-ENTRY-BUILDER1 / CONSUMED_COMPLETE
implementation_formal_result: 0e7a0be65877b03fb386e1c6c6bc258c0b27db6c / tree 85c266edb7349c940e8cd45870cc0538c95726c0 / parent aa70c2cf9b6b4a29517d7354f0239ea0cdc9a5d3
implementation_scope: EXACT_5_PATHS / tracked 37->40
implementation_reviewer: APPROVE / P0=0 / P1=0 / P2=0
implementation_windows_evidence: direct 19 passed / hygiene 11 passed / full 377 passed / final exit 0
implementation_ci: run 32489111184 / completed / success / headSha=0e7a0be65877b03fb386e1c6c6bc258c0b27db6c / Ubuntu / Python 3.14.7 / 376 passed / 1 skipped / final exit 0
candidate_allowed_docs: AGENT_GUIDE.md; PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md; docs/workbuddy/v2/DRIFT-GUARD.md
candidate_result: IMPLEMENTATION_EVIDENCE_MIRRORED / CLOSEOUT_CANDIDATE_NOT_DELIVERED
stage_5_planning: PASS_ACCEPTED
stage_5_implementation: PASS_ACCEPTED_ONLY_AFTER_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD
stage_5_real_workbuddy_production_acceptance: NOT_GRANTED / NOT_PROVED
current_task_after_closeout: NONE / NO_ACTIVE_TASK
next_authorized_task_after_closeout: NONE
candidate_test: NOT_RUN_DOCS_ONLY
candidate_push: NOT_PUSHED
```

唯一入口合同保持一个 WorkBuddy-managed Skill -> package-private fixed `-I -m golden_key_openmontage_workbuddy.workbuddy_entry_cli` -> 恰好一次 `launch_session_tool(...)` -> 真实 `LauncherReceiptV1`。无 console script、subcommands、router、MCP、第二 Agent、retry/replay；literal user message、closed JSON、provider-secret non-disclosure、固定 env 身份及 cancel/continuation 边界不变。精确五个实施路径为 `.github/workflows/ci.yml`、`workbuddy-skill/golden-key-openmontage/SKILL.md`、`golden_key_openmontage_workbuddy/workbuddy_entry_cli.py`、`tests/workbuddy/test_workbuddy_entry_cli.py`、`tests/workbuddy/test_repository_hygiene.py`。真实 WorkBuddy、最终 Installer/Package/Registration、Provider、媒体和 Stage6 均未由本收口授权或证明。

## [HISTORICAL / CONSUMED_BY_V2-S5-R01-WORKBUDDY-EXECUTION-CONTRACT-EVIDENCE1] Stage 5剩余计划与R00纠偏（`V2-S5-R00-REMAINDER-PLAN-STATE-CORRECTION1`，2026-08-21）

本节是 R00 已消费后的历史摘要；当前 live authority 为本文末 R01 镜像。原始产品目标回读为 `PASS`：WorkBuddy 是唯一运行中的 Agent/用户入口，Shell 仅负责六模块，不成为 Director/FSM/第二Agent/媒体控制面。Stage5整体是 `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`；入口代码与前一轮 closeout 已正式交付为子项，不能冒充整体 `PASS_ACCEPTED`。

```text
task_id: V2-S5-R00-REMAINDER-PLAN-STATE-CORRECTION1
task_kind: DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE / EXACT_12_EXISTING_DOCS
base_commit: 2207c9083ceabcf6539936e47b0935a4eaa77c46
base_tree: 8c66c3c38bf0dc00595c09743de715d7c1117c40
tracked_files_at_base: 40
initial_product_goal_recheck: PASS
entry_code_result: 0e7a0be65877b03fb386e1c6c6bc258c0b27db6c / tree 85c266edb7349c940e8cd45870cc0538c95726c0 / parent aa70c2cf9b6b4a29517d7354f0239ea0cdc9a5d3 / ENTRY_CODE_COMPLETE
entry_code_review_ci: APPROVE / P0=0 / P1=0 / P2=0 / Windows direct 19, hygiene 11, full 377 passed / CI 32489111184 success 376 passed 1 skipped
final_package_artifact: NOT_MATERIALIZED
production_package_root: NOT_CREATED
production_registration_activation: NOT_CREATED
final_installed_skill: NOT_CREATED
real_workbuddy_launcher_receipt: NOT_PROVED
candidate_allowed_paths: AGENT_GUIDE.md; README.md; README_zh-CN.md; PROJECT_CONTEXT.md; PROJECT-STATE.md; docs/workbuddy/v2/README.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md; docs/workbuddy/v2/DRIFT-GUARD.md; docs/workbuddy/v2/MODULE-DISPOSITION.md; docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md
candidate_test: NOT_RUN_DOCS_ONLY
candidate_push: NOT_PUSHED
after_promotion: current_task=NONE / NO_ACTIVE_TASK / next_authorized_task=NONE
next_planned_task: V2-S5-R01-WORKBUDDY-EXECUTION-CONTRACT-EVIDENCE1 / REQUIRES_SEPARATE_USER_AUTHORIZATION
```

### Stage 5整体PASS的五类必需证据

Stage5只有在以下五类证据全部存在时才可整体 `PASS_ACCEPTED`：

1. retained final Package Release + PackageRoot；
2. production Registration + Activation + new-process Locator；
3. zero-placeholder、已安装且唯一的 final WorkBuddy Skill；
4. HY3真实WorkBuddy成功取得真实 `LauncherReceiptV1`；
5. independent review + formal Git + CI + 无歧义 live authority。

任一缺失都保持 `REAL_INTEGRATION_INCOMPLETE`。临时Package、静态/direct/hygiene/CI、客户端导入或旧历史不能替代上述物证。

### S5-00 至 S5-08顺序、输出与停止边界

| 编号 / 任务 | scope与必须输出 | acceptance / stop boundary / 不证明 |
|---|---|---|
| S5-00 / `V2-S5-R00-REMAINDER-PLAN-STATE-CORRECTION1` | 十二份现有文档的 live truth、Stage5五类PASS门和R01-R08依赖；`DOCS_ONLY` | `test=NOT_RUN_DOCS_ONLY`；不改代码、不授权R01、不创建Package/Registration/Skill/客户端证据 |
| S5-01 / `V2-S5-R01-WORKBUDDY-EXECUTION-CONTRACT-EVIDENCE1` | **历史 / `SUPERSEDED_ACCEPTANCE_CONTRACT`**：原始 R01、refresh1 和专家可行性记录保留其事实及旧裁决；当前验收只接受 Skill 包装/上传/安装/身份出现/选择命中、客户端 sandbox scripts 与 PowerShell `ELIGIBLE_CANDIDATE_SURFACE` 的入口面 | 当前 `ENTRY_SURFACE_ACCEPTED / EXECUTION_PROOF_DEFERRED_TO_R03_R07`；Skill-root cwd、bundle-relative、stdin/stdout/stderr/final-exit/timeout 不再是 R01 硬门，但仍未证明；禁止任意CLI、路径猜测/扫描/PATH fallback、MCP、第二Skill/Agent、router、retry/replay；不证明最终Skill/Package/真实Launcher |
| S5-02 / `V2-S5-R02-PACKAGE-RELEASE-TOOL-DEFINITION-BINDING1` | 实时重验批准最终Package Release；`0.3.24/tree 0464861c`仅候选；绑定真实 safe fixed tool、release-specific `PackageToolDefinitionV1` 并纳入Manifest/Lock | 无真实Release=`BLOCKED_PACKAGE_RELEASE`；Shell不得臆造fixture/工具/定义 |
| S5-03 / `V2-S5-R03-EXECUTABLE-SKILL-BUNDLE1` | 单一可执行Skill bundle，含必要最小bundled helper、verified Guide/definition、canonical envelope、scrubbed env、固定private CLI一次、receipt映射、Stage3逐能力询问及确认后的新continuation；代码/Skill/测试/CI/独立Review/FF | 禁止第二Agent/MCP/router/retry/replay；具体路径须从届时live formal重新冻结，不由R00预造；不证明最终安装或真实客户端 |
| S5-04 / `V2-S5-R04-INSTALLER-LIFECYCLE1` | Installer install/update/repair/uninstall/stamp/rollback；组装approved OpenMontage、Shell、private Python+locked deps、FFmpeg/ffprobe、Node/npm/npx、tool definition、Manifest/Lock/ZIP/sidecar、Skill identity/schema/module/argv/interpreter；隔离D盘测试、ownership/staging/atomicity | 需代码/测试/CI/Review/FF；不证明正式Package已注册，未授权不得预造路径 |
| S5-05 / `V2-S5-R05-FINAL-PACKAGE-MATERIALIZATION-REGISTRATION1` | 用户另行确认正式D盘DataRoot；用R04物化并持久保留final Release/PackageRoot，register+activate+new-process locate，验证工具链/Guide/Manifest/Lock/Shell/tool definition | 未确认正式DataRoot即停止；成功产物不得清理为临时证据 |
| S5-06 / `V2-S5-R06-FINAL-SKILL-INSTALLATION1` | 导入Installer-stamped完整Skill folder/ZIP；零placeholder；客户端仅一个`golden-key-openmontage`、无旧V1/测试Skill；HY3 slash精确命中 | 不猜物理安装路径；导入命中不等于真实Launcher成功 |
| S5-07 / `V2-S5-R07-REAL-WORKBUDDY-ACCEPTANCE1` | HY3-only真实新会话，覆盖正常成功、取消/超时、并发/幂等、重启后定位；成功必须真实`LauncherReceiptV1`并比对WorkBuddy呈现与receipt字段 | 禁止Auto；Provider/媒体/完整业务E2E不在Stage5入口验收；身份/哈希不一致必须零spawn fail-closed，不伪造receipt |
| S5-08 / `V2-S5-R08-STAGE5-FINAL-CLOSEOUT1` | 仅在R01-R07齐备后独立Review、正式Git/CI、清理temporary而保留正式Package/Registration/Skill；唯一任务可把live `stage_5=PASS_ACCEPTED` | 不使用self-resolving candidate措辞冒充完成；Stage6另行授权 |

依赖严格为 `R01 -> R02 -> R03 -> R04 -> R05 -> R06 -> R07 -> R08`，任一阻断不得跳过。R03/R04未来即使合并，也必须另行授权并保留所有验收项。Stage5不要求Provider真实调用、媒体/视频生成、Remotion/HyperFrames下载安装、Stage6转换代码或完整业务E2E；optional缺失/decline/defer不阻断base。Stage5完成后，Stage6先判断是否可直接复用receipt（可直用则优先零代码），整个项目业务E2E另行授权，不称为Stage7。

## [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / ORIGINAL R01 / FORMALLY CLOSED / PRESERVED] Stage 5当前 R01受控执行合同证据结果（2026-08-22）

本节是当前 R01 正式结果镜像；R00 已正式推广并消费。产品目标回读与范围扩张审计均为 `PASS`：WorkBuddy 仍是唯一运行中的 Agent/用户入口，Shell 仍仅负责六模块；固定 CLI 仅允许作为唯一 Skill 内部桥梁，不构成任意 CLI 旁路。R01 结果不是 Stage5 整体 PASS，Stage5 仍为 `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`。

```text
task_id: V2-S5-R01-WORKBUDDY-EXECUTION-CONTRACT-EVIDENCE1
task_kind: CONTROLLED_CLIENT_EVIDENCE + DOCS_ONLY_CLOSEOUT / ZERO_PRODUCT_STATE_CHANGE
user_authorization: 2026-08-22 / Stage5继续执行、每个子任务独立审查、边界审计和产品目标回读
base_commit: d0a055689e9fc928a31edb24f3740e9408e123ef
base_tree: 50197a1eb103ffad42ac3e2952dcd3f9761a9512
base_parent: 2207c9083ceabcf6539936e47b0935a4eaa77c46
tracked_files_at_base: 40
initial_product_goal_recheck: PASS
scope_expansion_audit: PASS
official_sources: 134432 WorkBuddy Skills; 134391 local AI workbench task bar; 134324 update notes; 134516 CodeBuddy PRODUCT_MISMATCH_NOT_CONTRACT_PROOF
workbuddy_version_observed: 5.3.14
baseline_installed_skills: 2 / agent-browser; find-skills
temporary_probe_zip: r01-controlled-probe.zip / sha256 C55C90B7E86E9399F04EF13B8D78DF9228A8D72F7149B5B2A11B4362320F102D / DELETED_AFTER_REVIEW
temporary_probe_skill_sha256: D1BE59EF9221BA739482555744385244C86B771F5604DB738F5E0952CCC1E1E1 / HASH_ONLY_SOURCE_DELETED_AFTER_REVIEW
temporary_probe_script_sha256: 52B1F6283FF376F99DE49AE87EF24781042DC12F679AAAF7F976F58F19307064 / HASH_ONLY_SOURCE_DELETED_AFTER_REVIEW
client_safety_scan: NOT_SKIPPED / AUTO_INSTALL_ACCEPTED
installed_skill_observation: count 3 / exact golden-key-openmontage-r01-controlled-probe identity appeared
controlled_task_model: HY3 / NEVER_AUTO
requested_contract: relative scripts/r01_contract_probe.py + one literal JSON with final LF + fixed env marker + native stdout/stderr/final-exit/cwd/timeout capture
native_bundled_script_invocation_event: ABSENT
client_execution_path_observed: Bash/PowerShell only / no independent native bundled-script invocation/tool event
coordinator_stop: BEFORE_ANY_SHELL_OR_TERMINAL_EXECUTION
probe_script_execution: NOT_RUN
stdout_stderr_exit_cwd_timeout_evidence: NONE
nonzero_case: NOT_RUN
timeout_case: NOT_RUN
r01_result: BLOCKED_EXTERNAL_CONTRACT
r01_result_reason: each case requires an independent native bundled-script invocation/tool event; text/marker/JSON cannot substitute
r01_result_review: APPROVE / P0=0 / P1=0 / P2=0 / FORMALLY_FAST_FORWARDED_TO_ORIGIN_CODEX_WORKBUDDY_SHELL_V2 / COMMIT=9eefe8600d9bed0c8ea6024880e4b2d2ef4e3bfc
r02_r08_status: NOT_STARTED / NOT_AUTHORIZED_BY_CHAIN
temporary_skill_cleanup: COMPLETE / USER_UNINSTALLED_TEMPORARY_SKILL / WORKBUDDY_INSTALLED_SKILLS_2 / TASK_HISTORY_RETAINED / BASELINE_SKILLS_2_UNTOUCHED
baseline_skill_cleanup: NOT_TOUCHED / TWO_RETAINED_SKILLS
temporary_probe_cleanup: COMPLETE / EXACT_ISOLATED_WORKTREE_FOLDER_AND_ZIP_DELETED / GIT_STATUS_CLEAN
candidate_allowed_paths: AGENT_GUIDE.md; README.md; README_zh-CN.md; PROJECT_CONTEXT.md; PROJECT-STATE.md; docs/workbuddy/v2/README.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md; docs/workbuddy/v2/DRIFT-GUARD.md; docs/workbuddy/v2/MODULE-DISPOSITION.md; docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md
candidate_production_code_changes: 0
candidate_test_changes: 0
candidate_ci_changes: 0
candidate_package_registration_changes: 0
controlled_client_external_write: TEMPORARY_SKILL_UPLOAD_INSTALL / USER_UNINSTALLED_AFTER_REVIEW / WORKBUDDY_INSTALLED_SKILLS_2 / BASELINE_SKILLS_UNTOUCHED
docs_closeout_external_writes: NONE
candidate_real_workbuddy_execution: CONTROLLED_CLIENT_ATTEMPT_ONLY / NO_SCRIPT_EXECUTION / NO_SHELL_OR_TERMINAL_EXECUTION
candidate_test: NOT_RUN_DOCS_ONLY
candidate_push: R01_RESULT_FORMALLY_FAST_FORWARDED / origin/codex/workbuddy-shell-v2 / commit=9eefe8600d9bed0c8ea6024880e4b2d2ef4e3bfc
after_r01_closeout_promotion: current_task=NONE / NO_ACTIVE_TASK / next_authorized_task=NONE / R02-R08_BLOCKED_BY_CHAIN
```

官方资料只证明 Skill 的脚本/工作流打包、上传、选择和自动调用形态；没有给出精确 native command/cwd/env/stdin/stdout/stderr/exit/timeout 合同。WorkBuddy `5.3.14` 的受控路径只暴露 Bash/PowerShell，没有独立原生 bundled-script invocation/tool event；协调者在任何 shell/terminal 执行前停止。因此不运行 nonzero/timeout，不伪造 stdout/stderr/exit/cwd/timeout，不把 Skill 上传/安装或模型文字当作脚本执行证据。R01 最终结果固定为 `BLOCKED_EXTERNAL_CONTRACT`；独立审查已 `APPROVE / P0=0 / P1=0 / P2=0` 并正式 fast-forward，用户已卸载临时 Skill，WorkBuddy 显示安装技能数为 `2`，任务历史保留，精确隔离 probe folder/ZIP 已删除；R02-R08 不得启动。

## [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT] Stage 5 R01 Sandbox Refresh1 受控客户端正式结果镜像（2026-08-22）

本节是独立于原始 R01 正式关闭/清理记录的 refresh1 正式结果镜像；原始记录不改写。官方 134420 明示 enterprise Skill 的 scripts 在客户端沙箱执行。受控 WorkBuddy 客户端观察将 PowerShell 记录为 `ELIGIBLE_CANDIDATE_SURFACE`，不是官方精确执行合同；不得再用“PowerShell 非原生/只暴露 shell”作为阻断理由。134432 证明 Skill 可封装脚本/工作流并上传/调用；134516 仍为 CodeBuddy `PRODUCT_MISMATCH_NOT_CONTRACT_PROOF`。官方资料仍未给出 bundled-relative resource resolution、Skill-root cwd、stdin/stdout/stderr/final-exit/timeout 的精确合同。

```text
task_id: V2-S5-R01-WORKBUDDY-SANDBOX-REFRESH1
task_kind: CONTROLLED_CLIENT_EVIDENCE_REFRESH + DOCS_ONLY_CLOSEOUT / ZERO_PRODUCT_STATE_CHANGE
candidate_branch: codex/v2-s5-r01-sandbox-refresh1-closeout
base_commit: 932bcabc5baf90d0190101b1039e4ccf087b2b08
base_tree: 2ed2cd0e67dd8628b7f0b1acf84df0a7d8b0d0fd
tracked_files_at_base: 40
candidate_allowed_paths: AGENT_GUIDE.md; README.md; README_zh-CN.md; PROJECT_CONTEXT.md; PROJECT-STATE.md; docs/workbuddy/v2/README.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md; docs/workbuddy/v2/DRIFT-GUARD.md; docs/workbuddy/v2/MODULE-DISPOSITION.md; docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md
initial_product_goal_recheck: PASS / WorkBuddy唯一运行Agent和用户入口 / 固定CLI仅为唯一Skill内部桥梁 / no second entry or control plane
scope_expansion_audit: PASS
official_sources: 134420=CLIENT_SANDBOX_SCRIPTS_EXECUTION_ONLY / 134432=SKILL_SCRIPTS_WORKFLOWS_UPLOAD_CALL_SHAPE / 134516=CODEBUDDY_PRODUCT_MISMATCH_NOT_CONTRACT_PROOF
powershell_surface: ELIGIBLE_CANDIDATE_SURFACE_FROM_COORDINATOR_CLIENT_OBSERVATION / NOT_OFFICIAL_EXACT_CONTRACT
official_contract_gaps: BUNDLED_RELATIVE_RESOURCE_RESOLUTION / SKILL_ROOT_CWD / STDIN / STDOUT / STDERR / FINAL_EXIT / TIMEOUT
workbuddy_version_observed: 5.3.14
baseline_installed_skills: 2 / agent-browser; find-skills
refresh1_source_root: ISOLATED_D_DRIVE_TEMP_ROOT / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / CLEANUP_COMPLETE / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND
refresh1_skill_sha256: A369E89912B51C1627C972A7DE8F82111E55E2909622CB2E0E3276B45331FFF9
refresh1_script_sha256: 8A1D38A65945CC99C4B7F8EE95FDF4FF744D105303BC9904E5915E630DF58359
refresh1_zip_sha256: 2284E6D6FE8FFD38689A357DD0A6653CEB23B923F0C531BF9EAC376178E9A28A
client_safety_scan: NOT_SKIPPED / NO_NON_HIGH_RISK_AUTO_INSTALL_SELECTED / installed count 3
client_generated_skill_identity: workbuddy-skill-1787379691395 / SKILL_MD_NO_METADATA_NAME / BODY_FIRST_LINE_MATCHED_REVIEWED_PROBE / TRACEABILITY_DEFECT_ONLY
controlled_task_model: HY3 / NEVER_AUTO
native_skill_read_event: PRESENT / SKILL_MD_AND_scripts\\r01_contract_probe.py_READ / PHYSICAL_INSTALL_PATH_EXPOSED / CONTRACT_DEVIATION_SENSITIVE_MINIMIZATION_FAILURE / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
frozen_success_contract: .\\scripts\\r01_contract_probe.py / NO_CD / NO_ABSOLUTE_PATH / NO_GUESSING / NO_COMMAND_MUTATION
observed_session: SESSION_WORKSPACE_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / SKILL_ROOT_CWD_NOT_EXPOSED / BUNDLE_RELATIVE_INVOCATION_NOT_EXPOSED
execution_result: POWERSHELL_NOT_STARTED / USER_CANCELLED / NO_SCRIPT_EXECUTION / NO_STDOUT_STDERR_FINAL_EXIT_CWD_CLASSIFICATION_TIMEOUT
coordinator_stop: UI_STOPPED / DISPLAYED_USER_CANCELLED
refresh1_result: BLOCKED_EXTERNAL_CONTRACT
refresh1_result_reason: MISSING_SKILL_ROOT_CWD_AND_BUNDLE_RELATIVE_RESOLUTION / NOT_BECAUSE_POWERSHELL_IS_NON_NATIVE
review: APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_REVIEWER
reviewer_independent_observation: WORKBUDDY_5.3.14 / HY3 / USER_CANCELLED / NO_SUCCESS_STDOUT_STDERR_EXIT_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
nonzero_case: NOT_RUN
timeout_case: NOT_RUN
r02_r08_status: NOT_STARTED / NOT_AUTHORIZED_BY_CHAIN
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
temporary_skill_cleanup: COMPLETE / USER_UNINSTALLED_TEMPORARY_SKILL / TEMP_SKILL_ID=workbuddy-skill-1787379691395_NOT_IN_INSTALLED_LIST / WORKBUDDY_MY_INSTALLED_SKILLS_2=agent-browser,find-skills / TASK_HISTORY_RETAINED / BASELINE_SKILLS_2_UNTOUCHED / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND
computer_use_transparency: LOW_IMPACT_OPERATIONAL_ANOMALY / EXISTING_EXPLORER_MISTAKEN_FOR_FILE_PICKER / ALT+N_MAY_OPEN_TAB_OR_WINDOW / NO_PATH_INPUT_NO_FILE_SELECTION_NO_WRITE_DELETE / STOPPED_AND_RECOVERED
accepted_result_commit: 6c20371f1c72ee9d55147e1ad7feb8ede201858f / tree 9eb4643f09d03cc9f39b0b46906773e5bcc9125d
docs_review: APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_ZERO_WRITE_REVIEW
current_task: NONE / NO_ACTIVE_TASK / R01_REFRESH1_ACCEPTED_BLOCKED_EXTERNAL_CONTRACT
current_task_status: BLOCKED_EXTERNAL_CONTRACT / DOCS_REVIEW_APPROVED / R01_CHAIN_STOPPED
next_authorized_task: NONE / R01_REMAINS_BLOCKED / ONLY_SEPARATE_R01_REOPEN_AUTHORIZATION_PLUS_ACCEPTED_SUCCESS_CONTRACT_EVIDENCE_CAN_UNLOCK_R02_R08
candidate_test: NOT_RUN_DOCS_ONLY
candidate_product_code_changes: 0
candidate_test_changes: 0
candidate_ci_changes: 0
candidate_package_provider_media_stage4_stage6_changes: 0
candidate_push: FORMALLY_EFFECTIVE_IFF_LIVE_REMOTE_REF_CONTAINS_THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR
```

refresh1 的独立 Reviewer 已 `APPROVE / P0=0 / P1=0 / P2=0`。旧 R01 的原生事件阻断只保留为原始已关闭记录；本 refresh1 的唯一阻断理由是 Skill-root cwd/bundled-relative resource resolution 合同缺失。R01 链继续停止，不运行 nonzero/timeout，不启动 R02-R08，不触碰 Provider、媒体、Package、Stage4、Stage6 或生产流程。已验证事实：临时 Skill `workbuddy-skill-1787379691395` 已卸载且不在“我安装的”列表；列表仅有 `agent-browser`、`find-skills`；两个 R01 任务历史保留；隔离 source/ZIP 已删除且路径不存在。

## [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT] Stage 5 专家入口可行性核验收口（2026-08-22）

本节是独立的 docs-only / zero-product-state-change 结果，不改写原始 R01 或 refresh1，不创建、保存、发布专家，不创建或安装 Skill/Package，不增加新的 R01 门，不授权 R02-R08。官方资料把专家定义为 WorkBuddy 的角色层，并说明配置的 Skill/MCP 可以间接提供文件或外部服务访问；官方没有证明专家可以替代可执行 Skill。下方 `DOES_NOT_SUPERSEDE_SOLE_SKILL_ENTRY` 与 `NOT_PROVED` 是本项目的证据裁决，不是腾讯官方结论。客户端观察不构成官方精确执行合同；模型文字或内置 Skill 自报不替代原生事件证据。

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

## [HISTORICAL / CONSUMED_BY_V2-S5-R02] 当前 Stage 5 R01 验收归属纠正（V2-S5-R01-ACCEPTANCE-CONTRACT-CORRECTION1，2026-08-22）

原始 R01、Sandbox Refresh1 和专家入口可行性记录均明确标记为 `HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT`；其事实与旧 `BLOCKED_EXTERNAL_CONTRACT`/`INCOMPLETE` 裁决保留，不伪造脚本执行、stdout/stderr/exit/cwd/timeout 或 `LauncherReceiptV1`。本节是用户基于最初产品目标作出的项目验收归属纠正，不是新增官方 WorkBuddy 证据。

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
current_task: HISTORICAL / NONE / NO_ACTIVE_TASK / R01_CORRECTED_ACCEPTED_ENTRY_SURFACE
next_authorized_task: HISTORICAL / V2-S5-R02-PACKAGE-RELEASE-TOOL-DEFINITION-BINDING1 / R02_AUTHORIZED_ONLY
next_task_scope: PACKAGE_RELEASE_TOOL_DEFINITION_BINDING_ONLY / NO_R03_R08_EXECUTION_PROOF_IN_THIS_TASK
chain: HISTORICAL / R01_CORRECTED_ACCEPTED -> R02_AUTHORIZED -> R03_R04_R05_R06_R07_R08_STRICT_ORDER / R03-R08_NOT_AUTHORIZED
acceptance_correction_review_state: PENDING_INDEPENDENT_REVIEW / DOCS_ONLY_CANDIDATE
```

## 当前 Stage 5 R02 Package Release/Tool Definition Binding1 收口（2026-08-22）

R02 是 docs-only 收口。已发布候选存在且身份与批准 source subtree 匹配，但不是可绑定的 final Release：远程递归树 `truncated=false`、共 `2614` entries，按绑定关键词命中 `0` 条；本地同树不可变审计为 `2155` blobs。Release/lock 元数据没有真实 safe fixed tool，也没有 release-specific `PackageToolDefinitionV1`/Manifest/Lock binding。不得从媒体工具中随意挑选，不造 fixture/definition，不修改外部 Package。

```text
task_id: V2-S5-R02-PACKAGE-RELEASE-TOOL-DEFINITION-BINDING1
published_repo: blazingcd/golden-key-openmontage / branch=codex/golden-key-openmontage-v0.3.24
published_commit: ef5f5b58fa1c2b494b0154989cf0e4e36615a701
published_root_tree: 0464861c5985c7c9072e789b94889d29cf9a937a / approved_source_commit=8395e578165e802990d53fef5a166f8b4cf0461a / approved_source_commit_tree=4624394238802a9577690248e43b8f0dff391a2b / approved_source_package_subtree=0464861c5985c7c9072e789b94889d29cf9a937a
published_tree_audit: REMOTE_RECURSIVE_TRUNCATED_FALSE / entries=2614 / binding_path_filter=(workbuddy|package.?tool.?definition|launcher|fixed.?tool|entry.?cli) / binding_related_paths=0 / local_same_tree_blobs=2155
release_metadata: GOLDEN_KEY_OPENMONTAGE_RELEASE.json / release_version=0.3.24 / console_script_entrypoint=null / python_load_probe=lib.pipeline_loader:load_pipeline / authority_entry=README.md
lock_metadata: GOLDEN_KEY_OPENMONTAGE.lock.json / NO_PackageToolDefinitionV1 / NO_workbuddy_entry_cli / NO_package_tool_definition / NO_launcher / NO_fixed_tool / NO_CORRESPONDING_TOP_LEVEL_FIELDS
r02_result: BLOCKED_PACKAGE_RELEASE / PUBLISHED_CANDIDATE_IDENTITY_VERIFIED / MISSING_SAFE_FIXED_TOOL_AND_RELEASE_SPECIFIC_DEFINITION
preserved_r01_hy3_policy: R01_ENTRY_SURFACE_ACCEPTED / HY3_CURRENT_TEST_MODEL_ONLY / COST_AVOIDANCE / PRODUCT_MODEL_NEUTRAL / USER_SELECTED_MODEL / NOT_A_SKILL_OR_EXPERT_OR_SYSTEM_DEPENDENCY
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
current_task: NONE / NO_ACTIVE_TASK / R02_CLOSED_BLOCKED_PACKAGE_RELEASE
next_authorized_task: NONE / PACKAGE_OWNER_RELEASE_BINDING_REAUTHORIZATION_REQUIRED / R03-R08_NOT_AUTHORIZED_BY_CHAIN
unblock_condition: SEPARATE_PACKAGE_OWNER_APPROVAL_AND_INDEPENDENT_VERIFICATION_OF_SAFE_FIXED_TOOL_RELEASE_SPECIFIC_DEFINITION_MANIFEST_LOCK_BINDING / THEN_REAUTHORIZE_R02
product_goal_anti_expansion: PASS / WorkBuddy_ONLY_AGENT_USER_ENTRY / FIXED_CLI_ONLY_SOLE_SKILL_INTERNAL_BRIDGE / NO_ARBITRARY_MEDIA_TOOL_SELECTION_OR_FIXTURE_OR_DEFINITION_OR_EXTERNAL_PACKAGE_MODIFICATION
side_effects: NO_CLIENT / NO_PACKAGE_MATERIALIZATION / NO_REGISTRATION / NO_STAGE4 / NO_PROVIDER_MEDIA_STAGE6_OR_PRODUCTION
review_state: PENDING_INDEPENDENT_REVIEW / DOCS_ONLY_CANDIDATE
```

## [HISTORICAL / CONTENT_SUPERSEDED_BY_2026-08-24_REBASELINE] 项目级架构纠偏审计 Phase A 账本镜像（A7 docs-only 已正式推广，2026-08-22）

本节保存 A0-A7 当时经审查和推广的历史对象、结论与 B01-B07 方案；其内容权威已由本文末 2026-08-24 重基线取代，但 Git/CI/推广事实和历史 PASS 不被改写。它不是当前产品任务授权。

```text
task_id: V2-PROJECT-ARCHITECTURE-RECOVERY-PHASE-A1
formal_ref: refs/heads/codex/workbuddy-shell-v2
formal_baseline_parent: f338d9d50cad2cccf1398438ad4a8c8d45127a21 / tree 5ef5e8e524412f6220ad31f2cc38448c6b1dac8b
phase_a_audit_commit: 4727c5efda6ae53194ff2c16dd224c67178e8d8d
phase_a_audit_tree: ac6206950b36f71663eddfb89b7e311aa85b53e6
phase_a_status: A0-A6_APPROVED / A7_DOCS_FORMALLY_PROMOTED
scope: EXACTLY_SIX_EXISTING_AUTHORITY_FILES / DOCS_ONLY
effect: ZERO_PRODUCT_STATE_CHANGE
test_label: NOT_RUN_DOCS_ONLY
review: APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_ZERO_WRITE
formal_promotion: ORDINARY_FAST_FORWARD / FORMALLY_PROMOTED / commit=4727c5efda6ae53194ff2c16dd224c67178e8d8d / tree=ac6206950b36f71663eddfb89b7e311aa85b53e6 / ci_run=32615371879 / completed=success / headSha=4727c5efda6ae53194ff2c16dd224c67178e8d8d
task_artifacts_cleanup: ORIGINAL_PHASE_A_WORKTREE_LOCAL_AND_REMOTE_TASK_BRANCH_CLEANED
state_closeout: THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR
phase_b: NOT_AUTHORIZED / A7_HISTORICAL_SNAPSHOT
```

### 统一审计结论

原始目标是：普通用户只用自然语言向 WorkBuddy 提出业务请求；WorkBuddy 是唯一运行 Agent、唯一用户对话主体和唯一入口；在 Registration/Locator 验证 Package identity 后，WorkBuddy 读取 Guide、Manifest、Pipeline/Stage/Artifact/Checkpoint/Reviewer/Tool/Provider 合同并作生产决策；Shell 只承担六模块支持职责。OpenMontage Agent 是 WorkBuddy 读取已验证 Guide 后承担的逻辑角色，不是第二 Agent。

A1-A6 的谱系结论是：Stage 4 的机械 Launcher 合同被错误地当成产品架构完成，Stage 5 没有把最终 Package/Installer/生产 Registration/Activation 和真实 WorkBuddy Guide-read 证据纳入同一条完成链；缺失责任应由最终交付 Installer/Release Assembly Owner 承担，不应把 Shell adapter 缺失归因成历史共享 0.3.24 Package 必须内置 WorkBuddy 入口。该 0.3.24 对象仅作历史 R02/provenance 事实，未来纠偏使用当前 0.3.25 输入。

```text
stage_1_current_disposition: KEEP
stage_2_current_disposition: KEEP_WITH_NARROWING
stage_3_current_disposition: KEEP_WITH_NARROWING
stage_4_historical_contract: PASS_ACCEPTED_MECHANICAL_CONTRACT
stage_4_current_disposition: HISTORICAL_PASS_ONLY
stage_5_historical_repository_result: ENTRY_CODE_COMPLETE
stage_5_current_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
stage_5_current_disposition: REWORK
stage_6_current_disposition: INSUFFICIENT_EVIDENCE
```

需求分类：唯一 Agent/六模块为 `FULFILLED_AND_RETAIN`；Stage 2/3 为 `FULFILLED_BUT_NARROW`；Guide-first 生产决策、最终 PackageRoot、真实 WorkBuddy、真实 Artifact/业务 E2E 为 `PARTIAL/UNPROVED`；最终 Installer/工具链为 `DEFERRED_WITH_VALID_OWNER`；R02 责任归因为 `MISASSIGNED_TO_WRONG_LAYER`；旧 Stage 2 分支和旧 R03-R05 为 `SUPERSEDED_WITH_VALID_REASON`。

### R02 live 与推荐字段（不得混淆）

```text
r02_live_status: R02_CLOSED_BLOCKED_PACKAGE_RELEASE
recommended_reclassification: SHELL_INSTALLER_ADAPTER_BINDING_REQUIRED + REAL_FIXED_CHILD_UNVERIFIED
recommended_reclassification_state: NOT_YET_EFFECTIVE
binding_delivery_owner: V2 Final-delivery Installer / Release Assembly Owner
binding_carrier: FINAL_WORKBUDDY_PACKAGEROOT / INDEPENDENT_SHELL_ADAPTER_SUBTREE
shell_owns: BINDING_SCHEMA_AND_CONSUMER
openmontage_0_3_24: IMMUTABLE / NO_WORKBUDDY_ADAPTER_EMBEDDING
```

正确顺序是 `Registration identity validation -> Locator returns verified PackageRoot and Guide identity/hash -> WorkBuddy reads Guide/Manifest/Pipeline/Stage Skills -> WorkBuddy makes production decisions -> one fixed internal CLI transport -> deterministic fixed child/tool -> immutable LauncherReceipt mechanical facts -> WorkBuddy presents result`。Guide-read、identity/hash、决策主体和顺序必须有独立可见的 WorkBuddy/client 证据；模型自报、child 自报、普通日志、静态测试、CI、Skill 命中、CLI 启动或 receipt 单独不能证明真实集成。最终 Package 始终必带 Node.js `22+`、npm、npx 及其他必需 private toolchain；Stage 3 不探测、下载或替换 Node/npm/npx。

旧 Stage 2 分支 `codex/v2-s2-official-package-alignment-b1`（HEAD `86a7902465d8e215e0830b9640e7222d7c7f5188`，提交 `9b8ebb2`、`8d4461d`、`86a7902`）为 `SUPERSEDED_WITH_VALID_REASON / PRESERVE_HISTORY / DO_NOT_MERGE / DO_NOT_DELETE`。两个 dirty detached worktree `C:\Users\blazi\.codex\worktrees\aef5\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2` 与 `C:\Users\blazi\.codex\worktrees\df76\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2`（均在 `4d74d6576773dc9d383efec091bdc8d42f0d480c`）只登记，不复制、提交、回收或删除。

旧 R03-R05 执行包由 B02/B03 `SUPERSEDED_WITH_VALID_REASON`，不得与 B01-B07 并行。纠偏任务严格串行：`B01 -> B02 -> B03 -> B04 -> B05 -> B06 -> B07`；B04 先用固定 official 对照组，B05 保持同一 Shell 路径仅切换到固定 0.3.25；B06 唯一下游为 `HANDOFF_TO_B07_ONLY`；B07 之后唯一动作是 `PROMOTE_AND_CLEANUP`，且仅允许普通 fast-forward。

### B01 冻结 binding 与 Guide-read 合同

```text
01_task_id: V2-ARCH-RECOVERY-B01-FREEZE-BINDING-GUIDE-READ-CONTRACT
02_confirmed_issue: Stage4机械合同与R02被当成产品架构/Package完成；binding owner、carrier、Guide-read真实顺序和可观察证据未冻结
03_why_correction_necessary: 没有先冻结责任和证据边界，B02以后会继续把Shell/Package/WorkBuddy职责混在一起并重复制造伪完成
04_correct_owner: V2 Project Architecture Recovery Coordinator / Shell contract owner
05_authoritative_inputs: A0-A6 approved result; AGENT_GUIDE.md; PROJECT-STATE.md; PROJECT-CHARTER.md; ACCEPTANCE-MATRIX.md; DRIFT-GUARD.md; current official checkout D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-main-cd9f3c1f at cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / tree 6cd1961d552dd9d2bcfba990b80ac06edfe4b061 / state=DETACHED_CLEAN; current Golden Key OpenMontage 0.3.25 checkout D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673 at 73cab67322451601a824875c0e426067d736dd44 / tree 29231e0464fa4bc7533c1928415849e9b3a48e7c / parents=ef5f5b58fa1c2b494b0154989cf0e4e36615a701+cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / state=DETACHED_CLEAN read-only
06_exact_allowed_paths: AGENT_GUIDE.md; PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md; docs/workbuddy/v2/DRIFT-GUARD.md
07_concrete_actions: Freeze binding schema/consumer owner; final PackageRoot Shell-adapter carrier; immutable 0.3.25 boundary; Guide-read/decision/transport/child/receipt order; observable client evidence; anti-second-Agent/Director rules; stage dispositions and R02 recommended fields
08_explicitly_not_do: No product code execution or B02-B07 execution; no tests, CI, Package bytes, external repository, WorkBuddy client, Skill install, Registration, Activation, Provider, media, or DataRoot changes
09_output_contract: Single mirrored PhaseA decision record; B02-B07 serial contract; r02_live_status unchanged and recommended_reclassification=NOT_YET_EFFECTIVE
10_positive_tests: Cross-file key/value agreement; exact six-file allowlist; stage dispositions present; B01-B07 order and owner/carrier fields present
11_negative_tests: Missing Guide-read evidence field; R02 live status changed; 0.3.25 made mutable; second control plane allowed; any unlisted path changed
12_independent_reviewer_checks: Zero-write review of exact candidate commit/tree; compare six files; verify historical facts preserved and no product-state wording is introduced
13_p0_p1_p2_standard: P0 any authority/branch/status mutation or second-Agent authorization; P1 missing owner/order/evidence boundary; P2 wording drift or incomplete cross-file mirror
14_fail_closed_conditions: Baseline/tree/branch mismatch; six-file whitelist violation; conflicting live authority; missing owner; inability to distinguish historical PASS from current state
15_upstream_dependency: A0-A6 independently approved and user authorization to solidify PhaseA docs
16_downstream_handoff: B02 only; no B03-B07 parallel start
17_real_workbuddy_required: NO
18_official_control_group: NO (fixed official identity may be read-only input only)
19_involves_0_3_25: NO (read-only identity/immutability input only)
20_proves_after_completion: Correct ownership, scope, sequence, evidence and fail-closed contract for implementation
21_cannot_prove_after_completion: Any code correctness, final PackageRoot, real Guide-read, WorkBuddy execution, receipt, Artifact, or business E2E
```

### B02 实现 Shell adapter 与最终 Skill 合同

```text
01_task_id: V2-ARCH-RECOVERY-B02-SHELL-ADAPTER-FINAL-SKILL
02_confirmed_issue: Current entry/launcher layer proves only static/mechanical transport; final Skill-to-binding-to-fixed-child contract and Guide-read ownership are not real integrated proof
03_why_correction_necessary: Stage5 must provide one WorkBuddy-managed Skill and one deterministic internal bridge without creating a second Agent, Director, Router or arbitrary command surface
04_correct_owner: V2 Shell Adapter Worker under B01 contract, returned to the original Worker for revisions
05_authoritative_inputs: B01 approved contract; current session_launcher.py; current workbuddy_entry_cli.py; current final Skill; Stage4 historical mechanical contract; package registration contract
06_exact_allowed_paths: golden_key_openmontage_workbuddy/session_launcher.py; golden_key_openmontage_workbuddy/workbuddy_entry_cli.py; workbuddy-skill/golden-key-openmontage/SKILL.md; tests/workbuddy/test_session_launcher.py; tests/workbuddy/test_workbuddy_entry_cli.py; tests/workbuddy/test_repository_hygiene.py
07_concrete_actions: Implement/adjust one internal fixed transport; consume the approved binding; preserve literal user_message/executor_controls separation; resolve only Installer-stamped verified Package; invoke one deterministic fixed child; keep receipt mechanical and immutable; encode final Skill invocation contract
08_explicitly_not_do: No second Skill, CLI subcommands, public CLI, MCP, Router, Agent/Director/FSM/Supervisor, arbitrary shell/command, path scan/guess/PATH fallback, renderer/provider selection, retry/replay, media logic, Package/0.3.25 modification
09_output_contract: Reviewed code/test candidate with exactly one Skill, one fixed transport, one deterministic child call and mechanically bounded receipt; no claim of real WorkBuddy evidence
10_positive_tests: Direct/unit tests for verified binding, literal message/control separation, one spawn, fixed argv/cwd/I-O, cancellation/timeout and immutable receipt; repository hygiene passes
11_negative_tests: Reject unverified/mismatched Package or definition, arbitrary command/path, extra spawn/retry/replay, technical controls in user_message, second Agent/Router/MCP/provider/renderer selection
12_independent_reviewer_checks: Zero-write diff review of six allowed product/test paths; AST/import and spawn-count inspection; verify no new entry/control plane and exact allowlist
13_p0_p1_p2_standard: P0 second Agent/control plane, arbitrary execution or secret/path escape; P1 binding/receipt/message boundary failure; P2 test or documentation drift without boundary expansion
14_fail_closed_conditions: B01 absent; identity/hash mismatch; binding not Installer-stamped; more than one spawn; missing final exit/timeout classification; unapproved path or dependency
15_upstream_dependency: B01 complete and independently approved; current formal code baseline
16_downstream_handoff: B03 final-delivery Installer assembly only; no direct B04/B05 start
17_real_workbuddy_required: NO for implementation; real WorkBuddy proof remains B04/B05
18_official_control_group: NO
19_involves_0_3_25: NO; adapter is not embedded in the shared Package
20_proves_after_completion: Shell-side deterministic transport and final Skill static/unit contract within the six-module boundary
21_cannot_prove_after_completion: Final PackageRoot/Installer lifecycle, production Registration, real WorkBuddy Guide-read, real receipt/Artifact, or portrait business E2E
```

### B03 最终 Package、Installer 与生命周期

```text
01_task_id: V2-ARCH-RECOVERY-B03-FINAL-PACKAGE-INSTALLER-LIFECYCLE
02_confirmed_issue: Final PackageRoot, independent Shell-adapter carrier, real fixed child, Manifest/Lock/hash, private toolchain and production lifecycle are absent/unproved; R02 assigned this to the wrong layer
03_why_correction_necessary: Stage5 cannot accept a static entry without a reproducible final assembly, install/upgrade/rollback/uninstall and production Registration/Activation owner
04_correct_owner: V2 Final-delivery Installer / Release Assembly Owner
05_authoritative_inputs: B02 approved Shell adapter; Package Registration contract; immutable Golden Key OpenMontage 0.3.25 checkout D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673 at 73cab67322451601a824875c0e426067d736dd44 / tree 29231e0464fa4bc7533c1928415849e9b3a48e7c / parents=ef5f5b58fa1c2b494b0154989cf0e4e36615a701+cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / state=DETACHED_CLEAN; required private toolchain rules; B01 binding contract
06_exact_allowed_paths: D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673\ (read-only exact package input; commit=73cab67322451601a824875c0e426067d736dd44; tree=29231e0464fa4bc7533c1928415849e9b3a48e7c; parents=ef5f5b58fa1c2b494b0154989cf0e4e36615a701+cd9f3c1f03368be87b140af494914b8ee4e3c7a4; state=DETACHED_CLEAN); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_installer_source\ (owner source staging); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_final_assembly\ (assembly output); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_evidence\ (evidence); no other path
07_concrete_actions: Assemble immutable OpenMontage subtree plus independent Shell-adapter subtree; materialize PackageToolDefinitionV1 and deterministic fixed child; create Manifest/Lock/hash; include private Python, FFmpeg/ffprobe and Node22+/npm/npx; implement install/upgrade/rollback/uninstall; create production Registration/Activation and fresh PackageRoot
08_explicitly_not_do: No modification of 0.3.25 bytes; no source-checkout substitution; no renderer/provider/media selection; no WorkBuddy Guide decision logic; no second Agent; no unregistered checkout or guessed path
09_output_contract: Reproducible final PackageRoot and lifecycle receipt with subtree hashes, fixed child identity, toolchain identities, Registration/Activation and rollback evidence
10_positive_tests: Fresh assembly hash/lock/manifest reconciliation; toolchain availability including Node22+/npm/npx; install/register/activate/locate; upgrade/rollback/uninstall; fixed child source/hash/argv/cwd identity
11_negative_tests: Tampered subtree/lock/guide; missing tool; wrong Node version; stale/foreign Registration; rollback failure; source checkout instead of assembled Package; 0.3.25 byte change
12_independent_reviewer_checks: Verify owner/path/commit; immutable 0.3.25 subtree hash; adapter isolation; complete lock/manifest; fresh lifecycle and exact evidence roots; no external Package write
13_p0_p1_p2_standard: P0 mutable 0.3.25, untrusted PackageRoot, secret/path escape or unsafe lifecycle; P1 missing hash/tool/rollback/Registration evidence; P2 reproducibility or evidence packaging defect
14_fail_closed_conditions: Owner checkout path not pre-registered; any source/tree/hash mismatch; missing Node22+/npm/npx or private toolchain; stale registration; mutable shared Package; incomplete rollback
15_upstream_dependency: B02 approved and exact owner authority for Installer checkout
16_downstream_handoff: B04 official fixed control-group acceptance; B05 later same assembly with 0.3.25
17_real_workbuddy_required: NO for assembly/lifecycle; B04/B05 consume it for real client proof
18_official_control_group: NO (control group is B04)
19_involves_0_3_25: YES, read-only immutable source/candidate; no bytes modified
20_proves_after_completion: Final package assembly, private toolchain, lifecycle, binding carrier and production Registration/Activation facts
21_cannot_prove_after_completion: WorkBuddy actually reading Guide, production decisions, real receipt/Artifact or business portrait E2E
```

### B04 official fixed control-group real acceptance

```text
01_task_id: V2-ARCH-RECOVERY-B04-OFFICIAL-FIXED-CONTROL-ACCEPTANCE
02_confirmed_issue: No independent real WorkBuddy evidence connects the final Shell/Skill/PackageRoot to Guide-read, fixed child facts and receipt/Artifact
03_why_correction_necessary: A known-working official Package is the control variable needed to distinguish Shell/Installer/WorkBuddy defects before switching to 0.3.25
04_correct_owner: Independent WorkBuddy integration Worker plus independent zero-write Reviewer and business-evidence owner
05_authoritative_inputs: B03 final assembly; fixed official checkout D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-main-cd9f3c1f at cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / tree 6cd1961d552dd9d2bcfba990b80ac06edfe4b061 / state=DETACHED_CLEAN; B01/B02 contracts; WorkBuddy client contract
06_exact_allowed_paths: D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-main-cd9f3c1f\ (read-only fixed official control); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_final_assembly\ (read-only B03 output); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B04_official_evidence\ (fresh evidence root); WorkBuddy client external state only
07_concrete_actions: Fresh install/register/activate; new-process Locator; verify Guide identity/hash; observe WorkBuddy Guide-read and decision path; invoke fixed child through same Shell; capture source/hash/argv/cwd/stdin/stdout/stderr/spawn/retry/cancel/timeout/receipt/Artifact evidence
08_explicitly_not_do: No reuse of stale PackageRoot/Registration; no model or child self-report as authority; no Shell/Skill/Installer modification during acceptance; no 0.3.25 modification; no Provider/media expansion
09_output_contract: Independently reviewable official-control evidence bundle with fresh identities, observable Guide-read, fixed child facts, one spawn/zero retry and real LauncherReceipt/Artifact
10_positive_tests: Fresh lifecycle; new-process locate; expected Guide/hash; success, cancellation and timeout semantics; receipt/Artifact consistency; spawn=1/retry=0
11_negative_tests: Wrong Guide/hash; wrong Package/Registration; missing tool; extra spawn/retry; unobserved Guide-read; receipt without child facts; reused state
12_independent_reviewer_checks: Zero-write review of evidence timestamps/identities and client observations; correlate exact package/Shell commits; reject self-report and stale state
13_p0_p1_p2_standard: P0 false real-integration claim, wrong package or second control plane; P1 missing independent Guide-read/receipt/child fact; P2 evidence correlation or cleanup defect
14_fail_closed_conditions: Fresh root/registration unavailable; official commit mismatch; Guide-read not observable; any missing final exit/cwd/stdout/stderr/timeout fact; spawn/retry mismatch; truncated output
15_upstream_dependency: B03 complete and reviewed; official fixed checkout verified read-only
16_downstream_handoff: B05 only; same Shell/assembly/Skill/Launcher/method must be retained
17_real_workbuddy_required: YES
18_official_control_group: YES / fixed commit cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / tree 6cd1961d552dd9d2bcfba990b80ac06edfe4b061
19_involves_0_3_25: NO
20_proves_after_completion: Real WorkBuddy/client integration path and evidence with the official control Package
21_cannot_prove_after_completion: Compatibility with 0.3.25, final business portrait gate, broad production scale or Stage6 relay
```

### B05 保持 Shell 不变切换 0.3.25

```text
01_task_id: V2-ARCH-RECOVERY-B05-SAME-SHELL-0_3_25-SWITCH
02_confirmed_issue: Historical R02/0.3.24 identity and its missing adapter were misclassified as a shared Package defect; the current exact 0.3.25 input is a future verification target, and same-Shell compatibility has not been proven
03_why_correction_necessary: Only a controlled one-variable Package switch can show whether the final Shell/Installer/Skill path works with the immutable 0.3.25 candidate
04_correct_owner: Independent Package-switch acceptance Worker and independent zero-write Reviewer
05_authoritative_inputs: B04 approved control evidence and exact Shell/Installer/Skill/Launcher/request/method; Golden Key OpenMontage 0.3.25 checkout D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673 at 73cab67322451601a824875c0e426067d736dd44 / tree 29231e0464fa4bc7533c1928415849e9b3a48e7c / parents=ef5f5b58fa1c2b494b0154989cf0e4e36615a701+cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / state=DETACHED_CLEAN; B01 binding contract
06_exact_allowed_paths: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B05_0.3.25_evidence\ (fresh evidence root); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_final_assembly\ (read-only assembly); D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673\ (read-only exact candidate; commit=73cab67322451601a824875c0e426067d736dd44; tree=29231e0464fa4bc7533c1928415849e9b3a48e7c; parents=ef5f5b58fa1c2b494b0154989cf0e4e36615a701; state=DETACHED_CLEAN); WorkBuddy client external state only
07_concrete_actions: Create fresh PackageRoot/Registration; replace only the Package input; retain exact B04 Shell/Installer/Skill/Launcher/request/acceptance method; repeat Guide identity/read, fixed child, spawn/retry, receipt/Artifact evidence; compare control and candidate
08_explicitly_not_do: No Shell/Installer/Skill/Launcher/schema/request change; no reuse of B04 state; no 0.3.25 source/Release/Lock/Guide modification; no media tool selection or fixture invention
09_output_contract: Controlled comparison proving same Shell path against immutable 0.3.25, with fresh lifecycle and complete evidence or a precise fail-closed mismatch
10_positive_tests: Fresh install/register/activate/locate; same Guide-read order; same child/receipt facts; same spawn=1/retry=0; 0.3.25 subtree bytes/hash unchanged
11_negative_tests: Any changed Shell/Installer/Skill/request; stale registration; reused PackageRoot; candidate hash mismatch; mutable 0.3.25; missing Guide-read or receipt fact
12_independent_reviewer_checks: Compare B04/B05 inputs byte/commit-for-commit; verify only Package changed; check fresh roots, hashes, client observations and exact evidence
13_p0_p1_p2_standard: P0 two-variable test or Package mutation/false compatibility claim; P1 missing control comparison or real evidence; P2 non-material evidence correlation defect
14_fail_closed_conditions: B04 evidence not approved; any non-Package input differs; candidate identity/tree mismatch; fresh state unavailable; WorkBuddy evidence not independently visible
15_upstream_dependency: B04 APPROVE and retained exact control inputs
16_downstream_handoff: B06 Stage5 closeout only; no direct B07 or promotion
17_real_workbuddy_required: YES
18_official_control_group: YES / B04 retained as fixed control reference
19_involves_0_3_25: YES / read-only fixed candidate 73cab67322451601a824875c0e426067d736dd44
20_proves_after_completion: Same Shell/assembly path can be evaluated against the immutable 0.3.25 candidate under controlled one-variable evidence
21_cannot_prove_after_completion: Portrait business success, all Providers/renderers, production scale, Stage6 relay or formal promotion
```

### B06 Stage 5 closeout and B07 handoff

```text
01_task_id: V2-ARCH-RECOVERY-B06-STAGE5-CLOSEOUT-HANDOFF
02_confirmed_issue: Stage5 entry-code completion was previously allowed to stand without final Package, production Registration, final Skill, real receipt and independent real integration evidence
03_why_correction_necessary: A bounded closeout must prevent another stage handoff with missing ownership/evidence and must not start Stage6 prematurely
04_correct_owner: Stage5 closeout Coordinator with independent zero-write Reviewer
05_authoritative_inputs: B03 lifecycle evidence; B04 official-control evidence; B05 0.3.25 comparison; TASK-REGISTER; PROJECT-STATE; ACCEPTANCE-MATRIX; Git/CI headSha evidence
06_exact_allowed_paths: AGENT_GUIDE.md; PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md; docs/workbuddy/v2/DRIFT-GUARD.md; D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_evidence\; D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B04_official_evidence\; D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B05_0.3.25_evidence\
07_concrete_actions: Verify five evidence classes (final Package, production Registration/Activation, final Skill, real WorkBuddy receipt, independent Review/Git/CI/live authority); set Stage5 closeout only if complete; record sole handoff B07
08_explicitly_not_do: No new product code; no promotion; no cleanup; no Stage6 implementation; no Provider/media execution; no R02 live rewrite; no parallel task authorization
09_output_contract: Stage5 closeout or fail-closed INCOMPLETE record; if complete, exact downstream value HANDOFF_TO_B07_ONLY
10_positive_tests: Evidence matrix complete; exact commit/tree and CI headSha match; all five classes independently visible; B04/B05 comparison retained
11_negative_tests: Any missing class; stale/mismatched headSha; receipt without Guide-read; final package absent; R02 live mutated; attempted Stage6/promotion/cleanup
12_independent_reviewer_checks: Zero-write exact-object review; cross-check evidence roots and status fields; confirm no product-state overclaim and only B07 handoff
13_p0_p1_p2_standard: P0 false Stage5 PASS/promotion or Stage6 start; P1 missing final evidence/owner or wrong handoff; P2 mirror wording/traceability defect
14_fail_closed_conditions: Any of five evidence classes absent, conflicting, stale, truncated or self-reported; Git/CI object mismatch; B04/B05 one-variable rule broken
15_upstream_dependency: B05 approved and all evidence retained
16_downstream_handoff: HANDOFF_TO_B07_ONLY
17_real_workbuddy_required: YES / consume B04-B05 evidence; no new client execution unless evidence gap is explicitly reauthorized
18_official_control_group: YES / consume B04
19_involves_0_3_25: YES / consume B05 read-only evidence
20_proves_after_completion: Stage5 closeout readiness and a single permitted B07 handoff
21_cannot_prove_after_completion: Portrait/business gate, formal promotion, cleanup, Stage6 relay, or production scale
```

### B07 外部 portrait/business Gate D

```text
01_task_id: V2-ARCH-RECOVERY-B07-EXTERNAL-PORTRAIT-BUSINESS-GATE
02_confirmed_issue: Shell-level evidence cannot prove the final user-facing portrait Artifact or business acceptance; media/Core responsibility must remain external
03_why_correction_necessary: The original target is a natural-language business result, not only a process/receipt; the final gate must validate that result without turning Shell into media control
04_correct_owner: Independent Core/OpenMontage Owner plus independent business acceptance Owner
05_authoritative_inputs: B06 HANDOFF_TO_B07_ONLY; same approved Shell/Skill/Launcher/Installer path; the Core-owned corrected Release is the exact Golden Key OpenMontage 0.3.25 input at checkout D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673 / commit 73cab67322451601a824875c0e426067d736dd44 / tree 29231e0464fa4bc7533c1928415849e9b3a48e7c / parents ef5f5b58fa1c2b494b0154989cf0e4e36615a701 + cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / DETACHED_CLEAN; business acceptance contract
06_exact_allowed_paths: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B07_portrait_evidence\ (fresh evidence root); D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673\ (read-only exact package input; commit=73cab67322451601a824875c0e426067d736dd44; tree=29231e0464fa4bc7533c1928415849e9b3a48e7c; parents=ef5f5b58fa1c2b494b0154989cf0e4e36615a701; state=DETACHED_CLEAN); Shell repository read-only for identity verification; WorkBuddy client external state only
07_concrete_actions: Use ordinary natural-language request; retain same Shell/Skill/Launcher; let WorkBuddy/OpenMontage choose portrait behavior; capture final portrait Artifact and independent business acceptance; correlate Package/Shell/Core identities
08_explicitly_not_do: No user-supplied technical 9:16 parameter as a substitute; no Shell media patch; no Provider/renderer hard-code; no 0.3.25 modification; no second Agent/Director; no promotion before acceptance
09_output_contract: Independent Gate D business acceptance with portrait Artifact, user-level request, exact identities and evidence, or fail-closed defect owner handoff
10_positive_tests: Natural-language request produces correct portrait Artifact; same Shell path and receipt/result correlation; independent business acceptance passes
11_negative_tests: Missing/landscape/wrong Artifact; technical parameter required from user; identity mismatch; self-report only; Shell change needed to pass; missing independent business approval
12_independent_reviewer_checks: Verify Core/Package/Shell identities, user input, Artifact semantics, reviewer independence and no Shell media changes
13_p0_p1_p2_standard: P0 false business PASS, unsafe second control plane or identity substitution; P1 wrong Artifact or missing independent acceptance; P2 evidence packaging/traceability defect
14_fail_closed_conditions: B06 handoff absent; Core release path/commit unregistered; natural-language flow unavailable; Artifact or independent business evidence missing; any scope expansion into Shell media
15_upstream_dependency: B06 complete with HANDOFF_TO_B07_ONLY
16_downstream_handoff: PROMOTE_AND_CLEANUP only after B07 APPROVE; otherwise return to named owner
17_real_workbuddy_required: YES
18_official_control_group: YES / preserve B04 control lineage where applicable
19_involves_0_3_25: YES / exact checkout D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673 / commit=73cab67322451601a824875c0e426067d736dd44 / tree=29231e0464fa4bc7533c1928415849e9b3a48e7c / parents=ef5f5b58fa1c2b494b0154989cf0e4e36615a701+cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / state=DETACHED_CLEAN / never modify
20_proves_after_completion: End-user portrait business outcome under the corrected Agent-first architecture
21_cannot_prove_after_completion: Other formats/capabilities, production scale, universal Provider behavior, or any unapproved architectural expansion
```

### A7 正式推广状态与后续边界

```text
a7_scope: SIX_EXISTING_DOCS_ONLY
a7_product_code_changes: 0
a7_test_code_changes: 0
a7_ci_changes: 0
a7_package_or_external_repo_changes: 0
a7_client_provider_media_registration_activation: 0
a7_verification_label: NOT_RUN_DOCS_ONLY
a7_reviewer: APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_ZERO_WRITE
a7_audit_commit: 4727c5efda6ae53194ff2c16dd224c67178e8d8d
a7_audit_tree: ac6206950b36f71663eddfb89b7e311aa85b53e6
a7_formal_promotion: ORDINARY_FAST_FORWARD / FORMALLY_PROMOTED / ci_run=32615371879 / completed=success / headSha=4727c5efda6ae53194ff2c16dd224c67178e8d8d
a7_task_artifacts_cleanup: ORIGINAL_PHASE_A_WORKTREE_LOCAL_AND_REMOTE_TASK_BRANCH_CLEANED
a7_state_closeout: THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR
phase_b: NOT_AUTHORIZED / A7_HISTORICAL_SNAPSHOT
```

A7 审计结果已完成用户批准、exact commit/tree/CI headSha 核验和普通 fast-forward 推广；原 Phase A 临时任务工作树、本地任务分支和远端任务分支已清理。上方 `phase_b: NOT_AUTHORIZED` 与下方 B01-only 都只作历史；当前权威是 2026-08-24 重基线的 `PAUSED_BY_OWNER`。后续纠偏任务仍须遵守普通 fast-forward、禁止 merge/rebase `main` 和 force-push 的边界，旧 Stage 2 分支与两个 dirty detached worktree不得触碰。

## [HISTORICAL / SUPERSEDED_BY_2026-08-24_REBASELINE] Phase B 执行镜像：B01 已授权（2026-08-23）

本节只保存 2026-08-23 当时的 B01-only 授权和 package 输入，已被 2026-08-24 重基线取代，不提供当前执行授权。

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

## [HISTORICAL / SUPERSEDED_WHEN_D_ROUTE_CANDIDATE_IS_FORMALLY_PROMOTED] Phase B 暂停与纠偏方案重基线审计（2026-08-24）

```text
task_id: V2-PROJECT-ARCHITECTURE-RECOVERY-PLAN-REBASELINE-AUDIT1
owner_authority: OWNER_APPROVED_REBASELINE_AUDIT
formal_baseline: 6457d475ee43b291c7ac34ad42f9f48aaaaa1390 / tree d296e4ab98f8d6908e03360bea7d9c04b8ea06cc
scope: EXACT_SIX_EXISTING_AUTHORITY_DOCS_ONLY
phase_b: PAUSED_BY_OWNER
product_code_package_workbuddy_provider_media_changes: 0
tests: NOT_RUN_DOCS_ONLY
current_product_task: NONE
next_product_task: NONE / OWNER_REAUTHORIZATION_REQUIRED
```

### 最初目标与 official Agent-first 裁决

最初 V2 目标要求普通用户只在 WorkBuddy 中提出自然语言业务需求，WorkBuddy 是唯一对话 Agent，读取 exact OpenMontage Guide 后由 Core 原生完成 Pipeline、Stage Director、Reviewer、Checkpoint、Tool Registry 和 Artifact 链。official `AGENT_GUIDE.md` 进一步要求 Agent 选择 pipeline、读取 manifest、逐阶段读取 Stage Director Skill、调用 registry tools 并自审；明确禁止跳过 pipeline、临场写 Python 直调工具或绕过 review/checkpoint。

Phase A 的审计完整性在 A1-A3 已出现缺口。A4 正确把 Stage4 缩为 mechanical historical pass，却没有裁决“one fixed child 能否完成整个 Agent-first 请求”这一核心反例；A6 是最早把该未证假设明确固化为错误纠偏计划的节点，B02 是最早把它落地为产品实现的节点。A6/B02 把正确的“一个用户入口、一个 WorkBuddy Agent、一个受限 Shell transport”错误收窄成“一个复杂请求 JSON、一次固定 child/spawn、一个 receipt”，并把本应由 Installer/Shell 隐藏绑定的 `PackageToolDefinitionV1`、hash、schema、路径和环境细节暴露给模型。

### A0-A7 与 B01-B04 重裁决

| 对象 | 真实结果 | 为什么错误或不足 | 当前处置 |
|---|---|---|---|
| A0 | `4727c5e` 的 parent 精确为 `f338d9d`，正式文档记录独立 branch/worktree、clean、0/0 divergence 和残留对象 | 当前正式仓库没有保存 A0 独立 Worker/Reviewer artifact，A0 事实不能为后续推理背书 | `KEEP_PROCEDURAL_FACTS / REVIEW_EVIDENCE_NOT_PRESERVED` |
| A1 | 唯一 WorkBuddy Agent、六模块 Shell、自然语言目标重建正确 | Phase A 正式交付没有按要求保留原八阶段、十一步、T1-T12、R01-R08 的完整逐项追踪矩阵和事实/建议/待验证分栏 | `KEEP_TARGET / REQUIRED_DELIVERABLE_INCOMPLETE` |
| A2 | Stage1 `KEEP`、Stage2 `KEEP_WITH_NARROWING` 与“临时 Package 不是 final delivery”正确；遗留分支确实把 portable Package 错改成 official Git checkout | 直接写成“错误方向/保留历史”不足：`8d4461d/86a7902` 含 Windows stable-handle、reparse 与 Git identity hardening 思路，正式 portable schema 未原样包含；是否选择性重做未被审完 | `PARTIAL_KEEP / LEGACY_BRANCH_MAINLINE_REJECT / HARDENING_IDEAS_OUT_OF_SCOPE_CANDIDATE` |
| A3 | bounded optional Remotion/HyperFrames、逐项授权、Shell 不选 renderer/provider 的边界基本符合六模块 | Phase A 未逐项比较两个 dirty worktree；本次只读比较确认它们是旧 Stage3 contract-freeze 迭代，相关 public entry/test/CI 已被后续正式实现取代，不应合入 | `KEEP_WITH_NARROWING / RESIDUAL_CONTENT_NOW_CLASSIFIED_SUPERSEDED_HISTORY` |
| A4 | 正确区分 Stage4 mechanical PASS 与 product PASS | 没有完成核心反例裁决，留下 `one fixed child` 能否支撑整个请求和 `PackageToolDefinitionV1` 是否模型可见两个未决项 | `HISTORICAL_PASS_NARROWING_KEEP / CORE_QUESTION_UNRESOLVED` |
| A5 | 正确识别 real WorkBuddy、final Package/Installer、R02 wrong-layer 和 Stage6 evidence gap | 仍继承 A4 未解决的 whole-request fixed-child 假设，未以 actual WorkBuddy interaction proof 作为合同前置 | `PARTIAL_KEEP / EXECUTION_PATH_REWORK` |
| A6 | 正确保留唯一 Agent、六模块、证据分层和串行闸门 | 首次把未证假设明确写成一次 fixed-child 的 B01-B07 执行计划 | `EARLIEST_EXPLICIT_WRONG_PLAN / SUPERSEDED` |
| A7 | 六文档审查、提交、CI、普通 fast-forward 推广事实有效 | 推广的是带错误实现预设的 B01-B07 计划 | `HISTORICAL_PROMOTION_VALID / CONTENT_SUPERSEDED` |
| B01 (`1911b1f`,`0c9aea0`) | package identity 与 docs-only 冻结真实存在 | 冻结了 `one fixed transport -> one deterministic child` 错误合同；台账之后未跟上真实执行 | `HISTORICAL_CONTRACT / SUPERSEDED` |
| B02 (`1efe56f`,`6457d47`) | Bridge/Skill/schema/环境校验与单测真实存在 | Skill 要模型拼完整 JSON/technical identities；Bridge exact-compare 整个 WorkBuddy 宿主环境；产品运行依赖模型读源码、写 helper script 和临场排错 | `HISTORICAL_MECHANICAL_WORK / NOT_PRODUCT_ACCEPTED / REWORK_OR_REPLACE` |
| B03 | final assembly、private toolchain、Registration/Activation、new-process Locator、immutable snapshot 等机械证据有价值 | 最终 Skill/Bridge 仍承载错误合同；placeholder gate 只检查已列 marker，漏掉通用 `<installer:...>` | `KEEP_INFRASTRUCTURE_WITH_NARROWING / FINAL_BINDING_SUPERSEDED` |
| B04 | Attempt 1 未闭合；Attempt 2 触达 Bridge 后因宿主额外 sandbox env 失败；Attempt 3 因残留 token 未触达 Bridge；均无有效 receipt | Attempt 2 的 helper-script/source-inspection 路径本身已违反普通用户产品目标；Attempt 3 直接策划产物是 fallback | `INCOMPLETE / NEGATIVE_EVIDENCE_RETAIN / NO_SHELL_SUCCESS` |

正式台账末尾此前仍写 `B01_ONLY`，而正式分支已经包含 B02 代码、外部已经产生 B03/B04 执行结果；这是状态权威漂移。原 Phase A 只留下 `A0-A6_APPROVED` 聚合自述，没有保存逐 A 证据和全部强制交付物，不能再作为总体 APPROVE。本节取代旧 current mirror 的执行权威，但保留所有历史文本和对象，不 reset、不删除、不倒写。

### 原 Phase A 强制交付物合规复核

原 Prompt 要求 23 项交付物、A0-A7 每项独立 Worker/Reviewer 证据，以及每项结束后的 10 问防膨胀审核。formal commit `4727c5e` 只保存了聚合结论和 B01-B07 计划，不能证明这些要求全部完成。

| 原要求 | 当前 formal 可复核结果 | 裁决 |
|---|---|---|
| 1-3 接管、分支/worktree、目标摘要 | exact parent/base 与目标摘要存在 | `FULFILLED_BUT_REVIEW_ARTIFACT_NOT_PRESERVED` |
| 4 阶段谱系图 | 原 formal 只有线性文字；本次在下方补齐 exact 谱系和逐项映射 | `ORIGINAL_PARTIAL / CLOSED_BY_THIS_READ_ONLY_REBASELINE` |
| 5 完整需求追踪矩阵 | 原 formal 未覆盖每一项；本次在下方补齐原八阶段、十一步、T1-T12、R01-R08 | `ORIGINAL_INCOMPLETE / CLOSED_BY_THIS_READ_ONLY_REBASELINE` |
| 6-9 Stage1-6、保留/缩小/重做 | 有聚合 Stage disposition | `PARTIAL / TOO_COARSE` |
| 10-12 `PackageToolDefinitionV1`、`launch_session_tool`、`workbuddy_entry_cli` 专项结论 | 原 formal 没有三个独立专项裁决；本次在下方逐项重裁决 | `ORIGINAL_INCOMPLETE / CLOSED_BY_THIS_READ_ONLY_REBASELINE` |
| 13 R02 归因 | 错层归因被正确识别 | `FULFILLED_AND_RETAIN` |
| 14 遗留 Stage2 分支 | 主方向判错成立；本次补齐 exact commits、hardening 证据与单独授权边界 | `ORIGINAL_PARTIAL / NOW_CLOSED_READ_ONLY` |
| 15 两个 dirty worktree | 只登记未裁决；本次只读比较后确认是已被后续正式 Stage3 取代的历史候选 | `ORIGINAL_INCOMPLETE / NOW_CLOSED_READ_ONLY` |
| 16 official -> same Shell -> candidate 顺序 | 已记录 | `FULFILLED_BUT_IMPLEMENTATION_ASSUMPTION_WRONG` |
| 17-19 最小架构、任务清单、每任务 21 字段 | B01-B07 形式完整 | `FORM_COMPLETE / CONTENT_SUPERSEDED` |
| 20 每阶段新 DoD 与下游接管 | 原 formal 只有部分 gate；本次由下方完整 C01-C07 21 字段合同和逐项 downstream/fail-closed 字段取代 | `ORIGINAL_INCOMPLETE / CLOSED_BY_THIS_PLAN` |
| 21 仍需用户决策 | 原 formal 未形成明确清单；本次在下方单列 | `ORIGINAL_INCOMPLETE / CLOSED_BY_THIS_PLAN` |
| 22-23 固化白名单与是否可固化 | 六文件与可固化判断存在 | `FULFILLED_PROCEDURALLY` |
| A0-A7 每项独立 Worker/Reviewer + 10问审核 | formal 仓库仅有 aggregate `A0-A6_APPROVED` | `NOT_INDEPENDENTLY_REPRODUCIBLE` |

因此，Phase A 不能整体判为“没问题”。当前有效结论只能逐项保留，不能沿用聚合 APPROVE。

### 原目标到当前对象的完整谱系

```text
ordinary_user_business_request
  -> one WorkBuddy Agent reads exact OpenMontage Guide/manifest/Stage Skills
  -> WorkBuddy selects pipeline and stage actions
  -> one WorkBuddy Skill entry uses Shell support surfaces
  -> Registration/Locator resolves an immutable installed Package
  -> Runtime preparation exposes only verified capabilities
  -> bounded tool execution invokes package-local registry tools as WorkBuddy decides
  -> status/receipt/Artifact facts return without Shell interpretation
  -> real WorkBuddy control proof
  -> same-path Golden Key 0.3.25 proof
  -> real business video acceptance
```

历史阶段发生过重排：原 Stage 3 Launcher 对应当前 Stage 4，原 Stage 4 Skill 对应当前 Stage 5，原 Stage 5 Runtime 对应当前 Stage 3；原 Stage 7 Installer/lifecycle 没有成为本仓库六模块产品代码，而应由 final-delivery Installer Owner 在 C04 承担。阶段改名不得让原任务消失。

### 原八阶段与十一步逐项追踪

| 原始项 | 当前规划/产出/证据 | 当前裁决 | 纠偏与下游 |
|---|---|---|---|
| Stage 1 冻结 V2 边界 | 当前 Stage 1 六模块、唯一 Agent 和分层证据合同存在 | `FULFILLED_BUT_NARROW`：目标保留，旧 fixed-child 推导废止 | 本重基线 + C02 |
| Stage 2 Core Registration | 当前 Stage 2 Registration/Locator 有正式代码与测试；final Package 身份仍需 Installer 物化 | `PARTIAL` | C04 fresh lifecycle；不把 Installer 塞入 Shell |
| Stage 3 Launcher | 重排为当前 Stage 4；`launch_session_tool` 机械合同通过，但 whole-request one-child 用法未证明 | `FULFILLED_BUT_NARROW` | C01 先取事实，C02/C03 冻结并实现 per-tool bounded execution |
| Stage 4 WorkBuddy production Skill | 重排为当前 Stage 5；B02 Skill 要模型拼技术 JSON，B04 无 Shell success | `MISASSIGNED_TO_WRONG_LAYER` | C01-C03 重做入口合同与实现 |
| Stage 5 progressive Runtime | 重排为当前 Stage 3；基础/可选能力、逐项授权与不选 Provider/Renderer 的边界有效 | `FULFILLED_AND_RETAIN` | C04 只消费，不扩张 Provider/media |
| Stage 6 reduce CLI/MCP | MCP 不进主链正确；固定 CLI 只可作为隐藏 transport，但旧实现成为模型技术编排入口 | `PARTIAL` | C02/C03；CLI 不得成为第二入口/控制面 |
| Stage 7 Installer/upgrade/migration | B03 有外部机械装配/lifecycle 证据，但绑定旧合同，未形成正式产品验收 | `DEFERRED_WITH_VALID_OWNER` | C04 final-delivery Installer Owner 重建 |
| Stage 8 layered real acceptance | B04 三次均不完整；direct HTML/Markdown 不是 Shell success | `UNPROVED` | C05 official、C06 0.3.25、C07 business |
| Step 1 架构决策/保留退出清单 | Phase A 曾完成但 A6 内容错误 | `SUPERSEDED_WITH_VALID_REASON` | 本重基线和 C02 替代 |
| Step 2 Registration 合同 | 正式 Stage 2 机械合同/测试存在 | `FULFILLED_BUT_NARROW` | C04 以 final Package 实例复验 |
| Step 3 Launcher 精确环境绑定 | 当前 Launcher/Bridge 有绑定，但 B02 错把整个 WorkBuddy host env 当 exact set | `PARTIAL` | C03 构造 closed child env，容忍不转发无关 host env |
| Step 4 重写 production Skill | B02 已写但产品合同错误 | `LOST_BETWEEN_STAGES` | C01-C03 重做 |
| Step 5 progressive Runtime | 当前 Stage 3 正式实现/测试存在 | `FULFILLED_AND_RETAIN` | C04/C05 只消费 |
| Step 6 Installer/upgrade/rollback/migration | B03 外部 evidence 有机械价值，final binding 被取代 | `PARTIAL` | C04 重建并复验 |
| Step 7 offline/security/fault tests | 旧测试通过的是错误 fixed-child 合同 | `FULFILLED_BUT_NARROW` | C03/C04 只对新合同重跑，不沿用产品 PASS |
| Step 8 first real WorkBuddy Shell | B04 没有 valid receipt/OpenMontage Artifact | `UNPROVED` | C01 interaction proof，C05 official acceptance |
| Step 9 corrected Core Release | exact Golden Key 0.3.25 已有 detached-clean release object，但未通过同路径 WorkBuddy | `DEFERRED_WITH_VALID_OWNER` | C06 one-variable switch |
| Step 10 portrait store business acceptance | 未完成；direct策划文档不是 Shell 业务 E2E | `UNPROVED` | C07 |
| Step 11 optional Chinese fork/MCP/more entries | 明确不是首条主链前置 | `DEFERRED_WITH_VALID_OWNER` | C07 后另行决策，不进入本计划 |

### Stage 5 T1-T12 与 R01-R08 逐项追踪

| 对象 | 可保留事实 | 错误/未证明 | 当前裁决与去向 |
|---|---|---|---|
| T1 唯一入口 | WorkBuddy Skill 导入/命中机制有客户端证据 | 固定 CLI envelope 被误当完整产品合同 | `PARTIAL` -> C01/C02/C05 |
| T2 输入合同 | literal user message、secret-safe control separation 原则有效 | `PackageToolDefinitionV1`/hash/path/env 被暴露给模型 | `MISASSIGNED_TO_WRONG_LAYER` -> C02/C03 |
| T3 验证顺序 | Registration/Locator/Guide fail-closed 顺序有效 | WorkBuddy 实际 Guide/manifest/Stage Skill/tool 顺序未证明 | `PARTIAL` -> C01/C05 |
| T4 Stage4 adapter | 单次 bounded call、receipt 机械事实可保留 | one whole request = one fixed child 错误 | `FULFILLED_BUT_NARROW` -> C02/C03 |
| T5 authorization/continuation | 授权与计划/会话绑定、拒绝不自动重试有效 | 不能让 Shell 成为授权/能力决策者 | `FULFILLED_BUT_NARROW` -> C02/C05 |
| T6 result mapping | 机械 status/receipt 原样转交有效 | 旧闭集不能解释多次 tool/Artifact 流，真实 consumer 未证明 | `PARTIAL` -> C02/C03/C05 |
| T7 credential privacy | allowlisted child env、禁止 chat/log/receipt 泄密有效 | B02 host-env exact-set 检查与 WorkBuddy sandbox 不兼容 | `PARTIAL` -> C03 |
| T8 failure closure | fail-closed、无隐式 retry/replay 原则有效 | 旧分类绑死单 child/单 receipt | `FULFILLED_BUT_NARROW` -> C02/C03 |
| T9 Package Gate | final Package/Registration/Activation/new-process Locator 才是生产门，正确 | B03 final binding 已被取代 | `PARTIAL` -> C04 |
| T10 evidence layers | 不得用静态/CI/Skill hit 替代真实 WorkBuddy/业务证据，正确 | B01-B04 实际推进违反该原则 | `FULFILLED_AND_RETAIN` -> 每步 Reviewer + C05-C07 |
| T11 Stage6 handoff | 优先直接复用原生 receipt/status 是合理建议 | 多 tool/Artifact 下是否足够没有 consumer evidence | `UNPROVED` -> C01/C02/C03，C05实证 |
| T12 implementation package | 独立 Builder/Reviewer、白名单、CI、普通 FF 治理有效 | 五/六路径实现包固化了错误合同 | `SUPERSEDED_WITH_VALID_REASON` -> C03 新六路径合同 |
| R01 entry surface | Skill 包装/上传/安装/选择命中事实保留 | 不证明 bundled execution 或 Agent-first tool flow | `FULFILLED_BUT_NARROW` -> C01 |
| R02 Package/definition binding | final Release 和 verified registry definitions 确需绑定 | 被错归为 Package 必须提供“whole-request fixed child”；模型不应组装 definition | `MISASSIGNED_TO_WRONG_LAYER` -> C02/C04 |
| R03 executable Skill bundle | 单一 Skill、无第二 Agent/MCP/router 原则有效 | B02/B03 bundle 要模型技术编排 | `PARTIAL` -> C03/C04 |
| R04 Installer lifecycle | B03 install/update/rollback/uninstall 机械证据可复用为方法 | 旧 Skill/Bridge identity 不可复用 | `FULFILLED_BUT_NARROW` -> C04 |
| R05 materialization/registration | B03 fresh root/Registration/Activation/Locator 证据有价值 | 不是正确合同的产品验收 | `FULFILLED_BUT_NARROW` -> C04 |
| R06 final Skill installation | exact ZIP 曾成功导入安装 | 导入不等于调用成功；最终绑定已被取代 | `PARTIAL` -> C05 |
| R07 real WorkBuddy acceptance | B04 负面 trace 可保留 | 三次均无 valid receipt/OpenMontage Artifact | `UNPROVED` -> C05/C06 |
| R08 Stage5 closeout | 五类证据门的分层原则正确 | 前置 R01-R07 未完成，不能 closeout | `UNPROVED` -> C07 |

### 三个关键接口与 R02 专项裁决

| 对象 | 当前裁决 | 保留边界 | 必须纠偏 |
|---|---|---|---|
| `PackageToolDefinitionV1` | `VALID_INTERNAL_PACKAGE_INSTALLER_CONTRACT / MODEL_INVISIBLE` | 可作为 Installer 校验并固化的 package-local registry tool 定义，由 Shell 在每个 bounded tool call 内机械消费 | 不得让 WorkBuddy 模型拼 schema/hash/path/env；不得把一个 definition 当整个 OpenMontage 请求的唯一 child |
| `launch_session_tool` | `MECHANICAL_PRIMITIVE_RETAIN_WITH_NARROWING` | Locator 重验、fixed argv/cwd、closed child env、单次调用的 cancel/timeout/status/receipt 可以保留 | 是否直接复用或最小适配必须由 C01 事实和 C02 合同决定；不得选 pipeline/stage/tool 顺序或成为第二 Director |
| `workbuddy_entry_cli` | `CURRENT_IMPLEMENTATION_NOT_PRODUCT_ACCEPTED` | 只保留其中可独立证明的输入清洗、fail-closed 和 receipt 机械思路 | 当前完整 technical JSON、whole-host-env exact comparison、whole-request fixed-child 路径必须在 C03 重做或替换 |
| R02 attribution | `WRONG_LAYER_CORRECTED` | Core/Package Owner 提供真实 release、Guide/manifest/registry definitions；Installer 负责 immutable assembly/stamp；Shell 负责验证/定位/机械调用 | Package Owner 不负责制造 Shell adapter 或 whole-request child；WorkBuddy 模型不负责技术 binding；R02 不能再阻断成“修改共享 Package” |

### 仍需 Owner 决策的精确清单

1. 本重基线候选独立 Reviewer 通过后，是否单独批准普通 fast-forward 推广；Reviewer 通过本身不等于推广授权。
2. 每个 C01-C07 都需要单独激活授权；任何一步通过都不会自动授权下一步。
3. C01/C05/C06/C07 如 WorkBuddy 弹出权限或安全设置，由 Owner 在客户端选择；Shell 不把“完全访问”或 sandbox 策略写成产品合同，只记录真实设置和行为。
4. C05/C06 仅使用 Owner 指定的可用 `0.00x` HY3（若当前客户端存在）；模型选择是测试成本控制，不是产品依赖。
5. C07 开始前由 Owner 冻结业务素材、期望成片与验收人；未冻结不得以技术成功替代业务 PASS。
6. 遗留 Stage2 分支和两个 dirty worktree 的删除/归档需另行明确授权；不属于本重基线或 C01-C07 的自动清理范围。

### A2/A3 残留对象只读证据锚点

```text
evidence_method: READ_ONLY_GIT_OBJECT_AND_WORKTREE_DIFF / NO_NEW_ARTIFACT / NO_MERGE / NO_DELETE / NO_COPY
legacy_stage2_branch: refs/heads/codex/v2-s2-official-package-alignment-b1
legacy_stage2_head: 86a7902465d8e215e0830b9640e7222d7c7f5188
legacy_stage2_commits: 9b8ebb2f7c0e910758ad97c91e885c0ba18fdd79 + 8d4461dd159d7aff2484e34c21088ddb9f239053 + 86a7902465d8e215e0830b9640e7222d7c7f5188
legacy_stage2_main_direction: REJECT_OFFICIAL_GIT_CHECKOUT_AS_PORTABLE_FINAL_PACKAGE
legacy_stage2_hardening_evidence: package_registration.py and PACKAGE-REGISTRATION-CONTRACT.md at branch HEAD contain CreateFileW + FILE_FLAG_OPEN_REPARSE_POINT + GetFinalPathNameByHandleW + POSIX O_NOFOLLOW and git_tree identity checks
legacy_stage2_disposition: HISTORICAL_ONLY / DO_NOT_MERGE / HARDENING_IDEAS_REQUIRE_SEPARATE_FUTURE_AUTHORIZATION
dirty_worktree_aef5: path=C:\Users\blazi\.codex\worktrees\aef5\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2 / HEAD=4d74d6576773dc9d383efec091bdc8d42f0d480c / tree=2d467467810d8752c0be0a84d44e1f97dff4738b / modified_docs=5 / diff=+167,-49
dirty_worktree_df76: path=C:\Users\blazi\.codex\worktrees\df76\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2 / HEAD=4d74d6576773dc9d383efec091bdc8d42f0d480c / tree=2d467467810d8752c0be0a84d44e1f97dff4738b / modified_docs=5 / diff=+144,-29
superseding_stage3_implementation: a3f8959682d296301dc573c2835f8c705a52e8b2 / tree=eca057c3643c36248cccbfb9606d9aea12b3dc42
superseding_stage3_closeout: 7c15aae4e77c579309312b21c79076f930970214 / tree=4219a12faec8dc7dfc74258a3f99fcd43f17242f
dirty_worktree_disposition: SUPERSEDED_STAGE3_CONTRACT_FREEZE_HISTORY / DO_NOT_MERGE / DO_NOT_COPY / DO_NOT_DELETE_IN_THIS_TASK
```

### 重基线后的不可变产品边界

```text
ordinary_user: BUSINESS_NATURAL_LANGUAGE_ONLY
sole_agent_and_decision_owner: WORKBUDDY
production_authority: VERIFIED_OPENMONTAGE_GUIDE_MANIFEST_PIPELINE_STAGE_SKILLS
shell_role: INSTALL_LIFECYCLE + REGISTRATION_LOCATOR + RUNTIME_PREP + BOUNDED_TOOL_EXECUTION + ENTRY_SUPPORT + STATUS_RESULT_RELAY
one_user_entry: YES
one_fixed_child_for_whole_request: NO
multiple_deterministic_tool_invocations_under_WorkBuddy_decisions: ALLOWED_AND_EXPECTED
model_builds_hash_schema_path_environment_or_transport_JSON: FORBIDDEN
model_reads_shell_source_or_writes_helper_scripts_to_start: FORBIDDEN
host_sandbox_environment: WORKBUDDY_OWNED / SHELL_BUILDS_CLOSED_CHILD_ENV
second_agent_director_fsm_supervisor_router_or_mcp_mainline: FORBIDDEN
shell_provider_renderer_media_decisions: FORBIDDEN
direct_WorkBuddy_fallback_counts_as_Shell_success: NEVER
```

### 新的最小纠偏执行方案

严格串行 `C01 -> C02 -> C03 -> C04 -> C05 -> C06 -> C07`。每一步完成后先做“最初目标十问”回归审计，再由独立零写 Reviewer 审 exact 对象；未通过时停止，后续任务不得作为修复窗口。

#### C01 WorkBuddy 原生交互面事实证明

```text
01_task_id: V2-REBASELINE-C01-WORKBUDDY-NATIVE-INTERACTION-PROOF
02_confirmed_issue: B04 never proved that an ordinary WorkBuddy session can enter the official Guide/manifest/Stage Skill/tool path without model-authored helper scripts or technical JSON
03_why_correction_necessary: Freezing another Shell contract before observing the real client interaction surface would repeat A4-A6 and invent unsupported WorkBuddy behavior
04_correct_owner: WorkBuddy Integration Investigator + independent zero-write Reviewer
05_authoritative_inputs: approved/promoted rebaseline; official checkout D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-main-cd9f3c1f at cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / tree 6cd1961d552dd9d2bcfba990b80ac06edfe4b061 / DETACHED_CLEAN; historical B04 official-control PackageRoot snapshot cc92528f3d228123576ff908b79e82b63cee85e5480286757558e2140ebe4951 as read-only mechanical probe carrier only; current WorkBuddy client; B04 negative evidence read-only
06_exact_allowed_paths: D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-main-cd9f3c1f\ (read-only); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B04_official_evidence\official-control-cd9f3c1f\assembly\PackageRoot\ (read-only historical mechanical probe carrier; old Skill/Bridge/fixed-child forbidden); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C01_probe_skill\ (task-only temporary source/ZIP); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C01_native_interaction_evidence\ (fresh evidence); no other filesystem write; WorkBuddy-managed external state is limited to one imported probe Skill identity+ZIP hash and one new task/session ID, all recorded before/after
07_concrete_actions: Build the smallest non-production probe Skill against the read-only carrier only to expose exact official Guide/manifest/Stage Skill files and one harmless package-local registry/preflight call; submit one ordinary natural-language request; observe the actual native WorkBuddy read/call trace; capture evidence and clean task-owned temporary probe state after review
08_explicitly_not_do: No repository product code/test/CI edit; no Package mutation; no B02/B03 repair; no old Skill/Bridge/fixed-child invocation; no Registration/Activation claim; no Provider/media/video; no technical routing in user message; no model-authored helper script/source inspection during the client run; no direct fallback acceptance
09_output_contract: Immutable evidence bundle or BLOCKED result describing the actual model-visible/callable WorkBuddy interaction surface, exact client/carrier/Skill identities, trace, cleanup and remaining unknowns; explicitly NOT an official-control Package or Shell acceptance
10_positive_tests: Ordinary input; exact Skill hit; exact Guide/manifest/Stage Skill reads; at least one real package-local registry tool call; no model technical assembly; complete trace/final status
11_negative_tests: Wrong/unverified Package or Guide; helper/source/technical prompt required; direct fallback; missing/truncated client trace; temporary-state cleanup mismatch
12_independent_reviewer_checks: Exact probe hashes; client/package identity; literal user message; trace order; absence of helper/source/technical assembly; no product/repository change; cleanup state
13_p0_p1_p2_standard: P0 false WorkBuddy/Agent-first claim or wrong Package; P1 missing authoritative trace, technical model routing, direct fallback or residue; P2 non-material evidence correlation defect
14_fail_closed_conditions: Interaction surface not independently visible; official identity mismatch; client requires model-authored technical assembly; any Provider/media action; any non-task-owned state change
15_upstream_dependency: Rebaseline independently approved and formally promoted; explicit Owner authorization for C01; fresh evidence roots verified absent
16_downstream_handoff: C02 only; no code or assembly task starts from a BLOCKED/INCOMPLETE result
17_real_workbuddy_required: YES
18_official_control_group: NO / official cd9f3c1f bytes identify the read-only interaction probe only; C05 is the official control acceptance
19_involves_0_3_25: NO; old official and 0.3.24 are historical-only and forbidden
20_proves_after_completion: The actual WorkBuddy Agent-first interaction surface needed to design one product entry
21_cannot_prove_after_completion: Production Shell correctness, final assembly, repeatable official success, 0.3.25 compatibility, video/business E2E or promotion readiness
```

#### C02 Agent-first Shell 合同冻结

```text
01_task_id: V2-REBASELINE-C02-AGENT-FIRST-SHELL-CONTRACT
02_confirmed_issue: The superseded B01 contract exposed technical binding to the model and conflated one user entry with one child for the whole request
03_why_correction_necessary: Implementation needs an evidence-backed boundary that keeps WorkBuddy in control while hiding identity/runtime mechanics inside Installer/Shell
04_correct_owner: Architecture Contract Owner + independent zero-write Reviewer
05_authoritative_inputs: C01 approved evidence; original V2 handoff; official cd9f3c1f Guide; current six-module contracts; exact current formal Git object
06_exact_allowed_paths: AGENT_GUIDE.md; PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md; docs/workbuddy/v2/DRIFT-GUARD.md
07_concrete_actions: Freeze one Skill entry, verified Locator/session binding, WorkBuddy-owned Guide/pipeline/stage decision loop, independent bounded tool-call transport, receipt/status/artifact relay, hidden Installer-stamped identities and exact observability requirements
08_explicitly_not_do: No code/test/CI/Package/WorkBuddy change; no invented client capability; no whole-request fixed child; no Agent/Director/FSM/router/MCP mainline; no Provider/Renderer/media decision in Shell
09_output_contract: Six-file exact contract candidate with model-visible and hidden-mechanical field sets, task-by-task DoD, negative gates, owner and consumer for each interface
10_positive_tests: Cross-file contract equality; every operation backed by C01; ordinary user message contains no technical control; multiple tool calls remain individually mechanical and WorkBuddy-ordered
11_negative_tests: Model-visible hash/schema/path/env/PackageToolDefinition; Shell call ordering/pipeline choice; second entry/control plane; unsupported WorkBuddy operation; old B01/B02 contract still active
12_independent_reviewer_checks: Six-file exact diff; C01 trace-to-contract mapping; user/WorkBuddy/Shell/OpenMontage responsibility table; current authority and historical mirrors; no implementation authorization
13_p0_p1_p2_standard: P0 second Agent/control plane or false client capability; P1 missing owner/consumer/evidence/negative gate; P2 cross-file wording or traceability drift
14_fail_closed_conditions: C01 not approved; any interface lacks observed client evidence; six-file inconsistency; formal base mismatch; more than six files changed
15_upstream_dependency: C01 APPROVE and explicit Owner authorization for C02; latest formal branch exact takeover
16_downstream_handoff: C03 only after independent APPROVE, separate Owner promotion approval and ordinary fast-forward into formal
17_real_workbuddy_required: NO new run; consumes C01 evidence only
18_official_control_group: NO / consumes C01 read-only probe evidence only; C05 is the official control acceptance
19_involves_0_3_25: NO; exact identity may be listed as future read-only input only
20_proves_after_completion: An evidence-backed minimal Agent-first Shell/Skill/Installer contract and implementation boundary
21_cannot_prove_after_completion: Code correctness, assembly/lifecycle, real official success, 0.3.25 compatibility, business E2E or promotion of product behavior
```

#### C03 最小实现与离线合同验证

```text
01_task_id: V2-REBASELINE-C03-MINIMAL-IMPLEMENTATION
02_confirmed_issue: B02 Skill/Bridge requires model technical assembly, exact-compares the whole host environment and binds the whole request to one fixed-child transaction
03_why_correction_necessary: The production entry must implement C02 without making WorkBuddy diagnose Shell internals or making Shell orchestrate OpenMontage
04_correct_owner: Shell Implementation Worker + independent zero-write Reviewer
05_authoritative_inputs: C02 approved/promoted contract; current session_launcher.py, workbuddy_entry_cli.py, final Skill and focused tests; B02/B04 failures as negative fixtures
06_exact_allowed_paths: golden_key_openmontage_workbuddy/session_launcher.py; golden_key_openmontage_workbuddy/workbuddy_entry_cli.py; workbuddy-skill/golden-key-openmontage/SKILL.md; tests/workbuddy/test_session_launcher.py; tests/workbuddy/test_workbuddy_entry_cli.py; tests/workbuddy/test_repository_hygiene.py
07_concrete_actions: Rework or replace the model-facing entry; load hidden Installer identities mechanically; build a closed child environment from approved names while tolerating unrelated host names; keep each tool invocation fixed, independent and decision-free; preserve literal user message and mechanical receipts
08_explicitly_not_do: No Installer output or Package bytes; no WorkBuddy client; no Provider/media; no second Agent/router/MCP; no arbitrary command/path scan; no Shell pipeline/stage/review ordering; no old whole-request fixed-child assumption
09_output_contract: Reviewed six-path code/test candidate implementing exact C02 interfaces, closed environment construction, zero model technical assembly and bounded receipt/status facts
10_positive_tests: Ordinary-message fixture; hidden binding load; host extra environment tolerated and not forwarded; child environment closed; one spawn per tool call; multiple calls chosen/ordered only by caller; receipt/status integrity
11_negative_tests: Arbitrary command/path; unknown binding; model-supplied hash/schema/env; second spawn inside one call; retry/replay; Shell production decision; secret leak; wrong Package identity
12_independent_reviewer_checks: Exact six-path diff; AST/import/subprocess surfaces; model-visible Skill text; environment read/forward boundary; per-call spawn count; no new public entry/control plane; focused/full tests and CI headSha
13_p0_p1_p2_standard: P0 arbitrary execution, secret leak or second control plane; P1 C02 mismatch, model technical assembly, environment incompatibility or Shell orchestration; P2 test/wording/traceability defect
14_fail_closed_conditions: C02 absent; path allowlist expansion; unapproved dependency; test/CI failure; any model technical identity; any Shell-owned production decision
15_upstream_dependency: C02 formally delivered; explicit Owner authorization for C03; branch from latest exact formal head
16_downstream_handoff: C04 only after independent APPROVE, Owner promotion approval, ordinary fast-forward and temporary Builder branch cleanup
17_real_workbuddy_required: NO; real client acceptance is C05
18_official_control_group: NO
19_involves_0_3_25: NO; Package inputs remain untouched
20_proves_after_completion: Static/unit/CI correctness of the minimal Agent-first support surface inside the six-module Shell
21_cannot_prove_after_completion: Installer assembly, real WorkBuddy Guide-read/tool calls, official success, 0.3.25 compatibility, business E2E or product completion
```

#### C04 Fresh assembly 与生命周期重建

```text
01_task_id: V2-REBASELINE-C04-FRESH-ASSEMBLY-LIFECYCLE
02_confirmed_issue: B03 lifecycle infrastructure is useful, but its final Skill/Bridge binding, hashes and placeholder gate encode the superseded contract
03_why_correction_necessary: Real acceptance needs newly materialized official and 0.3.25 assemblies that consume C03 while retaining exact immutable Package bytes and reproducible lifecycle
04_correct_owner: Final-delivery Installer Owner + independent zero-write Reviewer
05_authoritative_inputs: C03 formally delivered code; B03 installer source/evidence read-only; official cd9f3c1f and Golden Key 73cab673 exact detached clean checkouts; Package Registration contract
06_exact_allowed_paths: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_installer_source\ (read-only); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_evidence\ (read-only); D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-main-cd9f3c1f\ (read-only); D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673\ (read-only); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C04_shell_source\ (fresh exact checkout of the formally delivered C03 commit; source input only); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C04_installer_source\; D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C04_fresh_assembly\; D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C04_evidence\
07_concrete_actions: Resolve the live formal C03 commit/tree and create the exact fresh C04_shell_source checkout; recreate Installer source from that checkout plus reviewed B03 mechanical inputs; materialize separate fresh official and 0.3.25 assemblies; recompute all bindings/hashes; generic scan for any installer token; verify private toolchain, Manifest/Lock, register/activate/new-process locate, upgrade/rollback/uninstall and deterministic rebuild
08_explicitly_not_do: No Package source-byte mutation; no old PackageRoot/Registration/final Skill reuse; no WorkBuddy run; no Provider/media; no source checkout substituted for final assembly
09_output_contract: Two reproducible fresh assemblies plus lifecycle evidence with exact subtrees/toolchain/binding/Skill/archive/Registration identities and cleanup/rollback facts
10_positive_tests: Byte-identical rebuild; complete toolchain; generic zero-token scan; all stamp/hash reconciliation; fresh register/activate/locate; upgrade/rollback/uninstall; immutable Package snapshots
11_negative_tests: Any `<installer:` token; stale schema/module/Skill hash; missing tool; wrong Package commit/tree; tampered Manifest/Lock; stale Registration; rollback failure; Package byte change
12_independent_reviewer_checks: Exact inputs/paths; C03 object consumed; no B03 final identity reused; both Package subtrees immutable; deterministic output; complete lifecycle evidence; no external writes
13_p0_p1_p2_standard: P0 Package mutation, unsafe lifecycle or identity substitution; P1 stale binding/token/tool/lifecycle evidence; P2 reproducibility/evidence packaging defect
14_fail_closed_conditions: Any input identity drift; unregistered output path; any residual token/hash mismatch; toolchain/lifecycle failure; Package snapshot change; incomplete cleanup
15_upstream_dependency: C03 formally delivered; explicit Owner authorization for C04; all fresh write roots verified absent or task-owned empty
16_downstream_handoff: C05 only; no client acceptance from B03/B04 old assemblies
17_real_workbuddy_required: NO
18_official_control_group: YES / build fresh cd9f3c1f assembly
19_involves_0_3_25: YES / build fresh 73cab673 assembly read-only from exact input; old 0.3.24 forbidden
20_proves_after_completion: Fresh reproducible assembly, toolchain, binding and lifecycle mechanics for both exact Package inputs
21_cannot_prove_after_completion: WorkBuddy Agent-first behavior, real OpenMontage Artifact, same-path comparison, business E2E or product promotion
```

#### C05 official Agent-first 实机验收

```text
01_task_id: V2-REBASELINE-C05-OFFICIAL-AGENT-FIRST-WORKBUDDY
02_confirmed_issue: No fresh real WorkBuddy evidence proves the corrected entry can execute official Agent-first behavior and produce an OpenMontage Artifact
03_why_correction_necessary: Official is the known control needed to separate Shell/WorkBuddy defects from Golden Key package compatibility
04_correct_owner: WorkBuddy Acceptance Worker + independent zero-write Reviewer
05_authoritative_inputs: C04 fresh official assembly/evidence; official cd9f3c1f exact checkout identity; C01/C02 acceptance method; current WorkBuddy client; exact C04 Skill ZIP
06_exact_allowed_paths: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C04_fresh_assembly\ (read-only); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C04_evidence\ (read-only); D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-main-cd9f3c1f\ (read-only); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C05_official_evidence\ (fresh); no other filesystem write; WorkBuddy-managed external state is limited to the one exact C04 Skill identity+ZIP hash, one official Registration identity and two fresh task/session IDs, all recorded before/after
07_concrete_actions: Fresh install/register/activate and new-process locate; install exact Skill; use ordinary natural-language request; capture Guide/manifest/Stage Skill reads, WorkBuddy decisions, registry preflight/tool calls, review/checkpoint, receipts/status and real OpenMontage Artifact; repeat in a fresh session; clean task state after review
08_explicitly_not_do: No code/Skill/Installer/Package repair during acceptance; no helper script/source inspection; no technical user prompt; no direct fallback acceptance; no 0.3.25; no Provider/media expansion beyond the approved no-cost control capability
09_output_contract: Independently reviewable two-run official-control evidence bundle or precise INCOMPLETE/BLOCKED owner handoff, with exact client/Skill/Package/Registration/trace/receipt/Artifact identities
10_positive_tests: Two fresh ordinary-language runs; exact Guide/manifest/Stage Skill sequence; WorkBuddy-owned decisions; real tool calls; receipt/Artifact correlation; no model technical assembly
11_negative_tests: Wrong/stale Package or Registration; direct fallback; missing Guide/stage read; helper/source diagnosis; acceptance-time mutation; missing/truncated trace; Artifact without provenance
12_independent_reviewer_checks: Fresh roots/sessions; exact hashes; literal user message; trace order and decision owner; tool/receipt/Artifact correlation; repeatability; cleanup; no hidden repair
13_p0_p1_p2_standard: P0 false real-integration claim, wrong Package or second control plane; P1 missing Agent-first/tool/Artifact trace, direct fallback, mutation or residue; P2 evidence correlation defect
14_fail_closed_conditions: C04 not approved; fresh state unavailable; official identity mismatch; any technical model routing; trace/provenance missing; direct fallback; acceptance-time write outside evidence/client task state
15_upstream_dependency: C04 APPROVE; explicit Owner authorization for C05; WorkBuddy model fixed to user-approved 0.00x HY3 when available
16_downstream_handoff: C06 only after independent APPROVE; no repair inside C05
17_real_workbuddy_required: YES / two fresh sessions
18_official_control_group: YES / cd9f3c1f exact
19_involves_0_3_25: NO
20_proves_after_completion: Repeatable real WorkBuddy Agent-first integration with the official control through the corrected Shell path
21_cannot_prove_after_completion: 0.3.25 compatibility, paid Providers, broad media capability, business-quality video acceptance or formal closeout
```

#### C06 同路径切换 Golden Key 0.3.25

```text
01_task_id: V2-REBASELINE-C06-GOLDEN-KEY-0_3_25-SAME-PATH
02_confirmed_issue: The corrected Shell path has not been proven against exact Golden Key 0.3.25 under a one-variable Package switch
03_why_correction_necessary: Only the same WorkBuddy/Shell/Skill/Installer/request/method with a fresh 0.3.25 root can attribute compatibility correctly
04_correct_owner: Controlled Comparison Worker + independent zero-write Reviewer
05_authoritative_inputs: C05 approved official evidence and exact non-Package inputs; C04 fresh 0.3.25 assembly; Golden Key checkout 73cab67322451601a824875c0e426067d736dd44 / tree 29231e0464fa4bc7533c1928415849e9b3a48e7c / parents ef5f5b58fa1c2b494b0154989cf0e4e36615a701+cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / DETACHED_CLEAN
06_exact_allowed_paths: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C04_fresh_assembly\ (read-only); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C04_evidence\ (read-only); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C05_official_evidence\ (read-only); D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673\ (read-only); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C06_0.3.25_package_root\ (fresh installed PackageRoot from exact C04 0.3.25 assembly); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C06_0.3.25_data_root\ (fresh Registration/Activation state); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C06_0.3.25_evidence\ (fresh); no other filesystem write; WorkBuddy-managed external state is limited to the unchanged C05 Skill identity+ZIP hash, one fresh 0.3.25 Registration identity and one fresh task/session ID, all recorded before/after
07_concrete_actions: Verify byte-for-byte retained C05 non-Package inputs; install the exact C04 0.3.25 assembly into the fresh C06 PackageRoot and register/activate it only in the fresh C06 DataRoot; start a fresh WorkBuddy session; switch only Package; repeat exact natural-language method and capture the same Agent-first/tool/receipt/Artifact evidence; compare control versus candidate
08_explicitly_not_do: No Shell/Skill/Installer/schema/request/method change; no C05 state reuse; no old 0.3.24; no 0.3.25 mutation; no acceptance-time repair; no new Provider/media scope
09_output_contract: Exact one-variable comparison bundle or precise fail-closed mismatch, with fresh 0.3.25 identities and control/candidate diff
10_positive_tests: Fresh install/register/activate/locate; same Skill/request/method; same Guide/stage/tool/receipt/Artifact classes; 0.3.25 subtree unchanged
11_negative_tests: Any non-Package drift; stale root/registration/session; old input; package mutation; missing Agent-first trace; direct fallback; evidence reuse
12_independent_reviewer_checks: Byte/commit comparison of every non-Package input; fresh state; exact 0.3.25 identity; trace/Artifact correlation; no two-variable change or mutation
13_p0_p1_p2_standard: P0 false compatibility claim, two-variable test or Package mutation; P1 stale state, non-Package drift, missing real evidence or fallback; P2 comparison packaging defect
14_fail_closed_conditions: C05 not approved; any non-Package input mismatch; fresh state unavailable; exact package identity mismatch; incomplete/truncated evidence
15_upstream_dependency: C05 APPROVE and retained exact inputs; explicit Owner authorization for C06
16_downstream_handoff: C07 only after independent APPROVE; otherwise return to named owner without modifying C06 acceptance inputs
17_real_workbuddy_required: YES / fresh 0.3.25 session
18_official_control_group: YES / C05 immutable comparison reference
19_involves_0_3_25: YES / exact 73cab673; historical 0.3.24 forbidden
20_proves_after_completion: Same corrected Shell path works or fails precisely against immutable Golden Key 0.3.25 with only Package changed
21_cannot_prove_after_completion: Final business video quality, all Providers/renderers, production scale or formal promotion readiness
```

#### C07 真实业务验收、状态收口与推广闸门

```text
01_task_id: V2-REBASELINE-C07-BUSINESS-CLOSEOUT-PROMOTION-GATE
02_confirmed_issue: Shell/process evidence alone cannot prove the original ordinary-user business outcome or safe repository closeout
03_why_correction_necessary: The project is complete only when the same Agent-first path produces a real acceptable video and all evidence/Git state closes without leaving temporary branches
04_correct_owner: Business Acceptance Owner + Closeout Coordinator + independent zero-write Reviewer
05_authoritative_inputs: C05/C06 approved evidence; exact current formal Shell; exact 0.3.25 assembly; original business acceptance contract; live remote/CI authority
06_exact_allowed_paths: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C05_official_evidence\ (read-only); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C06_0.3.25_evidence\ (read-only); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_C07_business_evidence\ (fresh); AGENT_GUIDE.md; PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md; docs/workbuddy/v2/DRIFT-GUARD.md; no other filesystem write; WorkBuddy-managed external state is limited to the unchanged C06 Skill/Registration identities and one fresh business task/session ID, all recorded before/after
07_concrete_actions: Run one ordinary-user business request through the approved 0.3.25 path; capture Agent-first trace, real tools, final video and independent business acceptance; audit exact Git/CI/package/client state; create docs-only closeout candidate plus an exact proposed promotion-and-cleanup manifest; stop for Reviewer and separate Owner promotion approval; do not promote or delete in C07
08_explicitly_not_do: No Shell media patch; no technical user prompt; no false PASS; no code repair during business acceptance; no promotion before independent review and separate Owner approval; no deletion of unrelated/historical branches or dirty worktrees
09_output_contract: Business evidence plus six-file closeout candidate recording exact product/evidence/Git states, remaining limits, and a proposed exact promotion/cleanup manifest; no promotion or cleanup effect
10_positive_tests: Ordinary request; approved Agent-first trace; real tools; playable correct final video; independent business acceptance; exact identities; docs consistency; CI/live remote match
11_negative_tests: Technical prompt required; wrong/missing video; direct fallback; identity drift; missing evidence class; Shell media fix; unreviewed promotion; incomplete or non-exact proposed cleanup manifest
12_independent_reviewer_checks: User request and video semantics; C05/C06 lineage; exact package/Shell/Skill identities; evidence completeness; six-doc diff; Git/CI headSha; cleanup targets and non-targets
13_p0_p1_p2_standard: P0 false business PASS, unsafe promotion/deletion or identity substitution; P1 missing video/evidence/review/Git gate or Shell media expansion; P2 closeout/traceability/cleanup wording defect
14_fail_closed_conditions: C06 not approved; business result rejected; any evidence class missing; code repair required; formal/live object mismatch; cleanup target not exact
15_upstream_dependency: C06 APPROVE; explicit Owner authorization for C07; fresh evidence root and business acceptance owner confirmed
16_downstream_handoff: STOP_FOR_SEPARATE_OWNER_PROMOTION_APPROVAL; no next product task; only a separately Owner-authorized POST_C07_PROMOTION_AND_CLEANUP mechanical action may ordinary-fast-forward to codex/workbuddy-shell-v2, verify remote commit/tree and CI headSha, resolve exact task branch/worktree/file cleanup targets against the reviewed manifest, and then remove only fully integrated temporary correction objects
17_real_workbuddy_required: YES / real business session
18_official_control_group: YES / consume C05 comparison lineage, no new official run unless separately authorized
19_involves_0_3_25: YES / exact approved C06 assembly; historical 0.3.24 forbidden
20_proves_after_completion: Original ordinary-user Agent-first business outcome and a reviewed repository-closeout candidate
21_cannot_prove_after_completion: Universal production scale, every Provider/renderer/format or promotion before Owner approval
```

### 每步强制“最初目标十问”

1. 本步是否直接服务“普通用户只表达业务需求”的最初产品目标？
2. WorkBuddy 是否仍是唯一 Agent、唯一对话主体和唯一生产决策者，并有独立证据证明其读取 exact Guide、manifest 与 Stage Skills？
3. Shell 是否仍只提供六模块支持及其必要验收，没有复制 OpenMontage Pipeline、Stage Director、Reviewer、Checkpoint、Provider、Renderer 或媒体决策？
4. 是否新增了没有事实证据支撑的抽象、接口、模块、状态机或第二控制面？
5. 是否把 Shell 责任错误推给 Package、Core、WorkBuddy、外部 Owner 或下一任务？
6. 是否把外部 Owner 的产品实现偷偷纳入本仓库或本任务允许路径？
7. 是否修改或要求修改任何共享 OpenMontage Package；当前 0.3.25 是否始终只读，旧 official/0.3.24 是否始终只作历史证据？
8. 是否混淆静态、单元、CI、客户端、生产、Artifact 与业务效果证据，或让当前证据支持超过自身层级的声明？
9. 是否导致普通用户、WorkBuddy 模型或维护者需要理解原本应由 Installer/Shell 隐藏的 hash、schema、路径、环境或 transport JSON？
10. 当前产出是否能被下一步直接接管，且 TASK-REGISTER、Git、Package、WorkBuddy 与证据状态同步、无 repair-window 留置？

任一答案为 `NO`、显示越界/膨胀，或关键事实为 `NOT_PROVED`：本步不得 APPROVE，不得启动下一步。当前重基线只形成计划，不授权 C01，也不修改产品代码、Package 或 WorkBuddy；独立零写审查后停止。

## [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] 新任纠偏统筹：目标与执行路线重建候选历史快照（2026-08-24；D01-D08 路线）

本节及其所含 D01-D08 路线字段、21-field contracts 均为历史记录，不参与当前路由；当前唯一 authority/route 为最新 E01→E07 correction（`V2-E01-ROUTE-BOUNDARY-CORRECTION1`）及六文档同名 current 节。

> 本节是 `codex/v2-correction-execution-plan-audit1` 上的规划候选。只有独立零写 Reviewer `APPROVE`、Owner 另行批准规划推广、并且正式远端普通 fast-forward 包含本候选后，它才可取代上节 C01-C07。候选存在、提交或推送均不授权任何产品执行。

Append-only precedence：在本候选尚未进入正式 ref 时，正式 C01-C07 仍只是暂停中的旧候选且无执行授权；本候选经 Owner 批准、ordinary fast-forward 并完成远端对象核验后，前面所有指向 C01-C07 的 `current/next/only` 字段立即降为历史，本节成为唯一 planning authority。该推广仍不授权 D01。

```text
planning_task: V2-CORRECTION-EXECUTION-PLAN-AUDIT1
planning_kind: READ_ONLY_AUDIT + DOCS_ONLY_PLAN
planning_base: 5e8c7c1b1bf59d284996e16ff5aeea8ce55c614c / tree 829d506de0ca7e256eff9338dd33ec773d150155
product_code_baseline: 6457d475ee43b291c7ac34ad42f9f48aaaaa1390 / tree d296e4ab98f8d6908e03360bea7d9c04b8ea06cc
formal_ref: refs/heads/codex/workbuddy-shell-v2
candidate_branch: codex/v2-correction-execution-plan-audit1
candidate_result: THIS_COMMIT
scope: EXACT_SIX_EXISTING_AUTHORITY_DOCS_ONLY
effect: ZERO_PRODUCT_CODE_TEST_PACKAGE_WORKBUDDY_PROVIDER_MEDIA_STATE_CHANGE
tests: NOT_RUN_DOCS_ONLY
current_product_task: NONE
execution_authority: NONE
old_C01_C07: SUPERSEDED_CANDIDATE / NEVER_EXECUTE
new_route: D01 -> D02 -> D03 -> D04 -> D05 -> D06 -> D07 -> D08
promotion_after_D08: SEPARATE_OWNER_AUTHORIZED_MECHANICAL_ACTION_ONLY
```

### 1. 项目核心目标与真实成功路径

`FACT`：原始 V2 交接要求普通用户只在 WorkBuddy 中表达业务需求；WorkBuddy 是唯一对话 Agent；OpenMontage 的 Guide、manifest、Stage Skills、Reviewer、Checkpoint、Tool Registry 和 Artifact 合同是生产权威；Shell 只负责六模块支持；最终必须以真实 WorkBuddy、真实自然语言、真实成片和业务效果验收。

`FACT`：official `cd9f3c1f` 明确规定 Agent 选择一个可用的用户 Pipeline、读取 manifest、逐阶段读取 director/meta/Layer-3 Skills、由 Agent 作出选择并调用 registry tools、审查 Artifact、写 checkpoint 并处理 human gate。Python 是工具与持久化，不是第二导演。Golden Key `73cab673` 保留这一 Agent-first 基础，并新增四条按“用户购买的单一业务结果”选择的 Pipeline；`framework-smoke` 已明确 `selection_scope=framework_only`，不得作为用户业务 control。

`FACT`：B02 的最终 Skill 要求一个完整 technical JSON、完整 `PackageToolDefinitionV1`、hash/schema/path/environment；一次 `launch_session_tool` 只启动一个固定 child。B04 Attempt 2 证实 WorkBuddy sandbox 会增加宿主环境变量，旧 Bridge 因 exact-set 校验在 spawn 前失败；Attempt 3 又因最终 Skill 保留通用 `<installer:...>` token 而直接 fallback。三次均无有效 Shell receipt/OpenMontage Artifact。

`INFERENCE`：一次固定、受限、可审计的 child/tool 调用可以保留为机械原语，但不能承担整个 Agent-first 用户请求。WorkBuddy 需要在一个经验证的会话中多次读取权威资源、选择 Stage，并按 manifest/Skill 决定多次机械工具调用。Shell 可以机械核验身份、资源范围、Stage tool allowlist、进程和结果，但不能替 WorkBuddy 决定调用顺序或内容。

`PROPOSAL`：正确成功路径固定为：

```text
ordinary business request
 -> one WorkBuddy Skill and one WorkBuddy conversation
 -> Installer-managed, model-invisible Shell binding
 -> Registration/Locator validates one immutable Package and opens one bounded session
 -> WorkBuddy reads exact Guide, selected manifest and required Stage/meta Skills
 -> WorkBuddy decides pipeline/stage/review/checkpoint/tool actions
 -> each semantic OpenMontage operation is a separate bounded mechanical call
 -> Shell/adapter returns identity-bound status/receipt/Artifact facts without interpretation
 -> WorkBuddy continues the official pipeline and presents the result
```

`NOT PROVED`：WorkBuddy 当前可稳定使用哪一种 Skill-relative resource/script/call surface；应由 D01 先证明。`NOT PROVED`：现有 `launch_session_tool` 可原样复用到何种程度；D02 只能按 D01 证据裁决，D03 才实现。`NOT PROVED`：official `cd9f3c1f`、Golden Key `0.3.25` 和最终业务链是否成功；分别由 D06、D07、D08 证明。

### 2. Phase A 与 B01-B04 最终重裁决

| 对象 | 最终裁决 | 保留 | 废止/未证明 | 因果影响 |
|---|---|---|---|---|
| A0 | `KEEP_PROCEDURAL_FACTS_ONLY` | exact base、独立 worktree、残留对象登记 | 每 A 任务独立 Reviewer artifact 未保留 | 新计划重新保存逐步审查证据 |
| A1 | `KEEP_TARGET / DELIVERABLE_INCOMPLETE` | 唯一 Agent、六模块、自然语言目标 | 完整映射和事实分层原来缺失 | 本节重新补齐全部映射 |
| A2 | `PARTIAL_KEEP` | Stage1/2 薄 Shell、临时 Package 证据缩小 | 遗留分支 hardening 未完成产品归属审计 | 只列未来独立 hardening 候选，不进入 D 主链 |
| A3 | `KEEP_WITH_NARROWING` | optional capability 逐项授权、Shell 不选 renderer/provider | 两个 dirty worktree 原审计不完整 | 已分类 superseded history，继续保护 |
| A4 | `HISTORICAL_MECHANICAL_PASS_ONLY` | 单次固定调用的身份、进程、取消、receipt 思路 | whole-request fixed child 与 model-visible definition 未裁决 | D01/D02 必须先取证再定接口 |
| A5 | `PARTIAL_KEEP` | real WorkBuddy、final Package/Installer、R02 wrong-layer 和 Stage6 证据缺口 | 继承 A4 假设 | D02-D05 重建入口与 Installer |
| A6 | `EARLIEST_EXPLICIT_WRONG_PLAN / SUPERSEDED` | 串行闸门、独立审查 | B01-B07 固化 one-child whole-request | C 路线不再可执行 |
| A7 | `PROMOTION_FACT_VALID / CONTENT_SUPERSEDED` | six-doc commit/review/CI/FF 事实 | 被推广计划内容 | 不 reset；只用新候选追加纠正 |
| B01 | `HISTORICAL_DOCS_ONLY / SUPERSEDED` | exact Package inputs、唯一 Agent/入口 | one transport -> one child whole request | D02 重写合同 |
| B02 | `MECHANICAL_CODE_EVIDENCE / NOT_PRODUCT_ACCEPTED` | input sanitation、single-call process safety、receipt/secret 思路 | model technical assembly、whole-host-env exact set、whole-request transaction | D03 选择性重写，不做补丁式续跑 |
| B03 | `INFRASTRUCTURE_METHOD_EVIDENCE_ONLY` | deterministic assembly、private toolchain、Registration/Activation/Locator、rollback/uninstall 方法 | Installer 只存在 D 盘临时脚本；final Skill/binding/placeholder gate 错误 | D04 把 Installer 变成版本化产品；D05 fresh materialization |
| B04 | `INCOMPLETE / NEGATIVE_EVIDENCE_RETAIN` | sandbox env、CRLF、Skill token、direct fallback 的真实失败机制 | 无 valid receipt、无 OpenMontage Artifact、无 Shell success | D01 先证实原生 surface；D06 才做 official control |

### 3. 为什么 C01-C07 不能直接执行

| 旧候选 | 缺陷 | 新去向 |
|---|---|---|
| C01 | 用 superseded B04 carrier 和临时 probe 同时尝试 Guide/Stage Skill/registry，混淆 client surface 与产品 path；未先证明 Skill-relative script/resource 语义 | D01 只证 WorkBuddy 原生 surface，不接 official/Package；D06 才做 official product proof |
| C02 | 方向正确，但在 C01 混合证据上冻结合同，仍预写“bounded tool-call transport”形态 | D02 只消费 D01 exact trace，冻结 model-visible semantic operations 与 hidden binding |
| C03 | 六路径 allowlist 仍预设现有 Bridge 可改成正确入口，未包含版本化 Package adapter | D03 增加一份版本化、无决策的 OpenMontage operation adapter，并以 D02 决定是否保留 bundled script |
| C04 | 继续在 D 盘临时脚本中“recreate Installer”；无法形成可升级、可审查、可发布的产品资产 | D04 版本化 Installer；D05 才 materialize/verify 两个 fresh Package |
| C05 | 只要求 real Artifact，可能把第一阶段 Artifact 当完整 official 可运行证明；下游仍可能成为修复窗口 | D06 要求两次完整、无付费、本地成片 control，包括 Guide/Stage/tool/review/checkpoint/video lineage |
| C06 | 要求 Package 切换时 Skill identity+ZIP hash 不变，但旧 Skill 把 Package identity 盖进文本，逻辑冲突 | D02-D05 使 Skill 字节 Package-agnostic；D07 只改变 Package-derived binding/Registration |
| C07 | closeout 与业务验收方向正确，但依赖上述不足，且业务任务之前没有完整 control/candidate 本地成片 | D08 只在 D06/D07 full local E2E 后做真实业务和 docs closeout；推广仍是单独动作 |

### [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] 4. 旧纠偏执行路线：严格串行 D01-D08

本节所含 D01-D08 21-field contracts 均为历史合同，不参与当前路由；当前唯一 authority/route 为最新 E01→E07 correction（`V2-E01-ROUTE-BOUNDARY-CORRECTION1`）及六文档同名 current 节。

以下每项先保留正式 21 字段结构，再追加本次 Owner 要求的逐任务补充合同。两部分共同构成完整合同。每项只能在前项正式交付、Owner 单独授权、从最新正式 HEAD 建立独立分支/worktree 后启动；Worker 与 Reviewer 必须不同，Reviewer 零写入。未来前序提交、tree、客户端版本或 evidence manifest 尚未产生时，必须明确记录为 `NOT_PROVED_FUTURE_INPUT`，并在任务接管时解析成完整对象后才能执行，不能伪造未来 SHA。任何失败只能回到该任务的 named owner，不能进入下游修复。

#### [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] D01 WorkBuddy 原生 Skill 资源与调用面证明

```text
01_task_id: V2-CORRECTION-D01-WORKBUDDY-NATIVE-SURFACE-PROOF
02_confirmed_issue: B04 did not establish one stable WorkBuddy-supported way to read bundled Skill resources and invoke one fixed bundled operation without guessed paths, model-written helpers or Shell technical JSON
03_why_correction_necessary: Product contract cannot be frozen from speculation or from a probe already coupled to the superseded Package carrier
04_correct_owner: WorkBuddy Surface Investigator Worker + independent zero-write Reviewer
05_authoritative_inputs: Current WorkBuddy client; official Tencent WorkBuddy Skill documentation only as documentary evidence; B04 traces read-only; no OpenMontage Package input
06_exact_allowed_paths: Probe Worker write only D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D01_probe_skill\ and D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D01_native_surface_evidence\ plus WorkBuddy-managed state limited to one task-only probe Skill and two fresh task/session IDs; after probe, Closeout Worker may write only the six authority docs to record result/review/status, never product code
07_concrete_actions: Build a non-production Skill containing fixed text fixtures and a pre-reviewed harmless script catalog that exercises only client primitives: Skill-relative resource read, enum-selected fixed script calls, structured stdin/stdout/stderr, repeated sequential calls, final exit, cwd, timeout and cancel; record ZIP/file hashes; import with normal safety scan; cover the catalog across two fresh ordinary-language tasks; record every client action; uninstall probe and clean task-owned source/ZIP only after Reviewer evidence capture
08_explicitly_not_do: No official/GK Guide, Package, Registration, Locator, Shell product code, B02/B03/B04 carrier, Provider, media or product-success claim; no absolute-path prompt; no helper authored during the run; no disabling WorkBuddy security
09_output_contract: Immutable evidence bundle or precise BLOCKED result naming the exact usable/unusable native surface, client/Skill/session identities, trace and cleanup state
10_positive_tests: Two fresh ordinary-language runs; exact Skill hit; fixture resource read; every fixed harmless primitive shape exercised, including at least two sequential enum-selected calls; complete observable results; no model technical assembly
11_negative_tests: Wrong Skill, guessed install path, model-created helper, direct fallback, missing final exit/trace, unclean probe residue, security bypass
12_independent_reviewer_checks: Exact hashes and client version; literal prompts; trace completeness; surface classification; no Package/product effect; before/after installed-Skill state and cleanup
13_p0_p1_p2_standard: P0 false native-surface claim or security bypass; P1 missing trace, helper/path dependence or residue; P2 correlation/wording defect
14_fail_closed_conditions: Surface not independently visible; any Package/product action; incomplete trace; non-task state change; security setting changed without Owner action
15_upstream_dependency: This plan formally promoted; explicit Owner authorization for D01; fresh D-drive roots absent
16_downstream_handoff: D02 only if one exact surface is APPROVE; BLOCKED returns to Owner with no contract invention
17_real_workbuddy_required: YES / two fresh diagnostic sessions
18_official_control_group: NO
19_involves_0_3_25: NO
20_proves_after_completion: The real client resource/invocation/result primitives available to a production Skill, not any OpenMontage semantic operation
21_cannot_prove_after_completion: Shell contract/code, Package binding, official/GK run, media/video, business E2E or promotion
```

补充合同：

```text
22_project_target: Prove the real ordinary-language WorkBuddy Skill surface before any product interface is designed
23_deviation_to_remove: Guessed Skill paths, model-written helpers and coupling a client probe to the superseded Shell/Package carrier
24_input_commit_tree: Shell formal commit/tree = NOT_PROVED_FUTURE_INPUT, resolve to full 40-hex commit/tree containing this promoted plan at takeover; Package commit/tree = NONE; WorkBuddy client version/binary hash and B04 evidence-manifest SHA256 = NOT_PROVED_FUTURE_INPUT, record before first action or BLOCK
25_prerequisites: Promoted plan, separate Owner D01 authorization, absent fresh D01 roots, installed-Skill/task baseline snapshot and Owner-present client
26_exact_allowlist: WRITE probe_skill root + native_surface_evidence root + task-only WorkBuddy Skill/two sessions; CLOSEOUT_WRITE six authority docs only; READ current client documentation and B04 evidence only
27_exact_denylist: ALL filesystem paths, repository files and external state not named in 26; especially Shell product code/tests, any OpenMontage Package/Registration/Locator, Provider and media
28_product_code_change: NO
29_workbuddy_user_action: YES / Owner performs import, security/permission decisions, fresh task submission and uninstall; Worker supplies frozen probe and observes; no unattended permission choice
30_package_action: NONE / no install, replace, register, activate or locate
31_exact_steps: Resolve inputs -> snapshot client state -> build/hash fixed primitive catalog probe -> safety-scan/import -> two fresh ordinary-language runs covering every catalog primitive -> capture trace -> uninstall -> capture after-state -> Closeout Worker records result -> Reviewer zero-write review
32_positive_acceptance: Fields 10 and 12 plus exact before/after state, two correlated traces and cleanup manifest
33_negative_assertions: Field 11; absence of every denylisted path/state change; no Package/Shell success claim
34_failure_conditions: Field 14 or unresolved field 24; result becomes BLOCKED_WORKBUDDY_SURFACE and D02 remains unauthorized
35_evidence_location: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D01_native_surface_evidence\ with immutable manifest/hashes; six-doc closeout stores identities, verdict and manifest hash only
36_worker_reviewer_split: Surface Worker creates/runs probe and evidence; Closeout Worker edits docs; independent Reviewer writes nothing and rechecks literal prompts/hashes/state
37_rollback_recovery: Restore pre-task installed-Skill set by uninstalling only exact task Skill; close both task sessions; preserve evidence; any failed restoration is P1 and blocks closeout
38_temp_cleanup: After Reviewer evidence capture remove exact probe source/ZIP and task-only client Skill/session artifacts; retain reviewed evidence root until Owner-authorized project cleanup
39_git_gates: Commit candidate result only after Reviewer APPROVE; push candidate only after clean exact commit/tree check; formal result promotion only after separate Owner approval; D02 authorization is a fourth separate decision
40_end_drift_audit: Record Q1-Q10 EXECUTION_GATE after actual cleanup and before commit; any NO/NOT_PROVED blocks commit except facts explicitly assigned as later-task nonclaims
41_not_proved_after_task: All field 21 items remain NOT_PROVED
42_no_downstream_repair: D02 may map official semantic operations only onto APPROVE client primitives; it cannot invent, patch or re-probe a missing primitive, and D01 does not claim OpenMontage semantics
```

#### [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] D02 Agent-first 产品合同与证据合同冻结

```text
01_task_id: V2-CORRECTION-D02-AGENT-FIRST-CONTRACT-FREEZE
02_confirmed_issue: Current contract conflates one user entry with one whole-request child and exposes hidden binding to the model
03_why_correction_necessary: D03-D08 need one evidence-backed division among WorkBuddy decisions, OpenMontage authority, Shell mechanics and Installer binding
04_correct_owner: Product Architecture Contract Worker + independent zero-write Reviewer
05_authoritative_inputs: D01 APPROVE trace; original V2 handoff; official cd9f3c1f Guide/manifests/Stage/meta Skills/tool registry contracts; Golden Key 73cab673 release and four-pipeline semantics; current six-module contracts
06_exact_allowed_paths: AGENT_GUIDE.md; PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md; docs/workbuddy/v2/DRIFT-GUARD.md
07_concrete_actions: Freeze one Package-agnostic Skill; one model-invisible session binding; logical authority-resource reads; WorkBuddy-owned pipeline/stage/review/checkpoint loop; semantic operations for project/checkpoint/preflight/registry-tool execution; one bounded process per operation; manifest/Stage allowlist validation without Shell ordering; identity-bound mechanical status/receipt/Artifact relay; separate PLAN_GATE and EXECUTION_GATE interpretations of the exact ten questions
08_explicitly_not_do: No code/test/client/Package change; no unsupported WorkBuddy surface; no package identity/hash/path/env in Skill text; no whole-request child; no Shell pipeline/stage/provider/renderer/media choice; no MCP/router/second Agent
09_output_contract: Six-file exact contract with model-visible semantic fields, hidden Installer/Shell fields, operation inventory, owner/consumer, evidence class, negative gates and per-stage DoD
10_positive_tests: Every operation maps to one or more D01-proved client primitives plus an exact official semantic contract; Skill bytes are Package-agnostic; multiple calls are caller-ordered in contract fixtures; user prompt stays business-only; final Gate B/C/D mapping is complete
11_negative_tests: Model-visible hash/schema/absolute path/env/definition; Shell ordering or creative decision; arbitrary command; second entry/control plane; framework-smoke as user control; unsupported client behavior
12_independent_reviewer_checks: Exact six-doc diff; D01 trace-to-interface matrix; official/GK source citations; responsibility table; all original mappings; no execution authorization
13_p0_p1_p2_standard: P0 second Agent/control plane, false client capability or Package mutation requirement; P1 missing owner/evidence/negative gate or unresolved logical contradiction; P2 cross-file wording/trace defect
14_fail_closed_conditions: D01 not APPROVE; any interface unobserved; formal base mismatch; more than six docs; any task left to downstream as repair window
15_upstream_dependency: D01 formally delivered; explicit Owner authorization for D02; latest exact formal takeover
16_downstream_handoff: D03 only after Reviewer APPROVE, separate Owner promotion approval and ordinary fast-forward
17_real_workbuddy_required: NO new run
18_official_control_group: NO / contract input only
19_involves_0_3_25: YES / read-only contract input only
20_proves_after_completion: Evidence-backed product and implementation contract
21_cannot_prove_after_completion: Code, Installer, assembly, real official/GK/video/business success
```

补充合同：

```text
22_project_target: Freeze the evidence-backed ordinary-user/sole-Agent/OpenMontage-authority/Shell-support product contract
23_deviation_to_remove: Whole-request fixed child, model-visible binding and any unobserved client interface
24_input_commit_tree: Shell formal commit/tree containing D01 result = NOT_PROVED_FUTURE_INPUT, resolve full 40-hex at takeover; official = cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / 6cd1961d552dd9d2bcfba990b80ac06edfe4b061; GK = 73cab67322451601a824875c0e426067d736dd44 / 29231e0464fa4bc7533c1928415849e9b3a48e7c; D01 evidence-manifest SHA256 = NOT_PROVED_FUTURE_INPUT
25_prerequisites: All dynamic identities in 24 recorded, D01 formally delivered, separate Owner D02 authorization and clean fresh docs-only worktree
26_exact_allowlist: READ D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D01_native_surface_evidence\; D:\BlazingCD\Personal\Golden_Key_OpenMontage_for_WorkBuddy\docs\workbuddy\WORKBUDDY-SHELL-V2-REFACTOR-HANDOFF-2026-08-15.md; under each exact official/GK checkout only AGENT_GUIDE.md, pipeline_defs\, skills\pipelines\, skills\meta\, skills\core\, tools\base_tool.py, tools\tool_registry.py, lib\checkpoint.py, lib\pipeline_loader.py, schemas\pipelines\ and schemas\checkpoints\; under GK additionally GOLDEN_KEY_OPENMONTAGE_RELEASE.json and GOLDEN_KEY_OPENMONTAGE_0_3_25_MIGRATION.json; WRITE only the six authority docs named in field 06
27_exact_denylist: ALL other filesystem paths and external state; no product code/test/client/Package/Registration/Provider/media writes
28_product_code_change: NO / docs-only
29_workbuddy_user_action: NO new run or client action
30_package_action: NONE / exact official and GK trees read-only
31_exact_steps: Resolve identities -> derive D01 trace matrix -> map official/GK authority -> freeze role/operation/evidence contracts -> map all original deliverables -> Q1-Q10 -> independent review -> candidate commit/push/promotion gates
32_positive_acceptance: Fields 9-12 with every semantic operation traceable to D01-proved primitives and exact official semantic authority; fixture calls are caller-ordered, not claimed as real WorkBuddy evidence
33_negative_assertions: Field 11 plus zero non-six-doc diff and no prewritten client/product PASS
34_failure_conditions: Field 14 or any unresolved 24 input; remain BLOCKED_CONTRACT and do not start D03
35_evidence_location: Six authority docs plus read-only D01 evidence manifest referenced by exact SHA256
36_worker_reviewer_split: Contract Worker writes six docs; independent Reviewer writes nothing and validates original mapping, D01 trace and exact external authority
37_rollback_recovery: Candidate branch can be abandoned without formal effect; if promoted content is later wrong, append a new reviewed correction, never reset history
38_temp_cleanup: Remove only task-created diff-export/check artifacts after review; keep no new temp root; never touch D01 retained evidence or historical dirty worktrees
39_git_gates: Reviewer APPROVE -> commit -> exact tree/diff check -> push candidate -> separate Owner result-promotion approval -> ordinary FF/remote+CI verify -> separate D03 authorization
40_end_drift_audit: Actual Q1-Q10 EXECUTION_GATE before commit and after any repair; no P0/P1
41_not_proved_after_task: Code, Installer, assemblies and every client/video/business result stay NOT_PROVED
42_no_downstream_repair: D03 implements only the promoted exact contract and cannot decide unresolved architecture or client behavior
```

#### [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] D03 最小 Agent-first Shell/Skill/Package-operation adapter 实现

```text
01_task_id: V2-CORRECTION-D03-MINIMAL-AGENT-FIRST-IMPLEMENTATION
02_confirmed_issue: B02 cannot support the official multi-operation Agent loop without technical model assembly and a whole-request fixed child
03_why_correction_necessary: The repository must expose D02 semantic operations while keeping all identity/process mechanics hidden and decision-free
04_correct_owner: Shell Implementation Worker + independent zero-write Reviewer
05_authoritative_inputs: D02 formally delivered contract; current session_launcher/workbuddy_entry_cli/Skill; official BaseTool/ToolRegistry/checkpoint contracts; B02/B04 negative fixtures
06_exact_allowed_paths: Product Worker write only golden_key_openmontage_workbuddy/session_launcher.py; golden_key_openmontage_workbuddy/workbuddy_entry_cli.py; golden_key_openmontage_workbuddy/openmontage_operation_adapter.py; workbuddy-skill/golden-key-openmontage/SKILL.md; workbuddy-skill/golden-key-openmontage/scripts/invoke.ps1; tests/workbuddy/test_session_launcher.py; tests/workbuddy/test_workbuddy_entry_cli.py; tests/workbuddy/test_openmontage_operation_adapter.py; tests/workbuddy/test_repository_hygiene.py and D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D03_evidence\; Closeout Worker additionally write only the six authority docs
07_concrete_actions: Rework the model-facing entry to accept only D02 semantic operations; mechanically load active binding; expose verified authority resources by logical identifier; validate requested tool against verified selected manifest/stage; call package-local registry/checkpoint/project functions through one versioned decision-free adapter; keep each process bounded; build closed child env while ignoring/not forwarding unrelated host env; emit correlated receipts/status/Artifact pointers
08_explicitly_not_do: No Installer/Package bytes/client/Provider/media; no arbitrary command/path/import; no Shell stage ordering, retries, review or checkpoint choice; no second Agent/router/MCP; no model-visible binding
09_output_contract: Reviewed exact-path code/test candidate implementing D02; optional invoke.ps1 must remain absent if D01 selected a different surface
10_positive_tests: Authority-read; project/checkpoint operations; registry preflight; two caller-ordered contract-fixture tool calls; Stage allowlist enforcement; unrelated host env tolerated and not forwarded; closed child env; receipt/Artifact correlation
11_negative_tests: Unknown logical resource/tool/stage; manifest mismatch; model-supplied identity; arbitrary command/path/import; second spawn inside one operation; retry/replay; secret leak; direct fallback; wrong Package
12_independent_reviewer_checks: Exact diff and conditional script path; AST/import/subprocess surfaces; Skill model-visible text; D02 operation matrix; focused/full tests; exact CI headSha
13_p0_p1_p2_standard: P0 arbitrary execution, secret leak or second control plane; P1 D02 mismatch, unsupported official operation, environment incompatibility or Shell orchestration; P2 test/trace wording defect
14_fail_closed_conditions: Path expansion; unapproved dependency; any failing test/CI; model technical field; Package mutation; downstream repair note
15_upstream_dependency: D02 formally delivered; explicit Owner authorization; latest exact formal head; project .venv only
16_downstream_handoff: D04 only after Reviewer APPROVE, Owner promotion approval, ordinary FF and Builder cleanup
17_real_workbuddy_required: NO
18_official_control_group: NO
19_involves_0_3_25: NO writes; read-only contract fixtures only
20_proves_after_completion: Offline implementation correctness of the semantic Agent-first support surface
21_cannot_prove_after_completion: Installer, assembly, real client, real OpenMontage/video/business success
```

补充合同：

```text
22_project_target: Implement the smallest decision-free support surface that lets WorkBuddy execute its official Agent loop
23_deviation_to_remove: Technical model assembly, whole-host-env exact rejection and whole-request transaction control
24_input_commit_tree: Shell formal commit/tree containing promoted D02 = NOT_PROVED_FUTURE_INPUT, resolve full 40-hex at takeover; official contract input = cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / 6cd1961d552dd9d2bcfba990b80ac06edfe4b061; D01 evidence-manifest SHA256 = NOT_PROVED_FUTURE_INPUT and must be recorded before edit
25_prerequisites: Field 24 resolved, D02 formal, separate Owner D03 authorization, fresh worktree, project .venv verified, D03 evidence root absent and exact write paths frozen absent/unmodified baseline
26_exact_allowlist: WRITE only the nine product/test paths, D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D03_evidence\ and six authority docs in field 06; READ D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D01_native_surface_evidence\, the six promoted D02 authority docs, and under D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-main-cd9f3c1f\ only AGENT_GUIDE.md, pipeline_defs\, skills\pipelines\, skills\meta\, skills\core\, tools\base_tool.py, tools\tool_registry.py, lib\checkpoint.py, lib\pipeline_loader.py, schemas\pipelines\ and schemas\checkpoints\; project .venv only for Python
27_exact_denylist: ALL other repository/filesystem/external state; Package bytes, Installer files, client, Registration, Provider and media forbidden
28_product_code_change: YES / only product paths in 06; no dependency change unless pyproject is separately added by Owner, so current task must stop if required
29_workbuddy_user_action: NO
30_package_action: NONE / no install, replace, register or activate; exact authority fixtures read-only
31_exact_steps: Resolve identities -> freeze path baselines -> write failing focused tests -> implement D02 operations -> focused tests -> full suite -> hygiene/secret scans -> Q1-Q10 -> closeout docs -> zero-write review -> CI candidate
32_positive_acceptance: Fields 10 and 12; caller-ordered offline fixtures only; exact CI headSha after candidate push
33_negative_assertions: Field 11 plus no non-allowlisted diff, no second entry/control plane and no real-client claim
34_failure_conditions: Field 14, any unresolved input, new dependency need, test/CI failure or path drift; keep D04 blocked
35_evidence_location: Versioned tests/code, six-doc closeout and D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D03_evidence\ for command logs/CI URL/headSha
36_worker_reviewer_split: Implementation Worker owns nine product/test paths; Closeout Worker owns six docs; independent Reviewer zero-write inspects exact diff/tests/CI and model-visible text
37_rollback_recovery: Before promotion, abandon candidate branch/worktree; after promotion, use a new reviewed revert/correction commit only; no destructive reset
38_temp_cleanup: Delete only task-created .pytest/cache/build intermediates inside verified task roots after evidence capture; retain required CI/test logs; do not clean user or historical worktrees
39_git_gates: Focused/full PASS -> Reviewer APPROVE -> commit -> push candidate/CI -> Reviewer confirms exact CI headSha -> separate Owner promotion -> ordinary FF verify -> separate D04 authorization
40_end_drift_audit: Run Q1-Q10 after implementation/tests and again after any repair; real WorkBuddy ordering remains NOT_PROVED
41_not_proved_after_task: Installer, assembly, client, OpenMontage tool/video and business success remain NOT_PROVED
42_no_downstream_repair: D04 may package only an approved D03 surface; D03 code/test defects cannot be deferred to Installer or acceptance
```

#### [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] D04 版本化 Installer、Package assembly 与 lifecycle 实现

```text
01_task_id: V2-CORRECTION-D04-VERSIONED-INSTALLER-LIFECYCLE
02_confirmed_issue: B03 Installer exists only as task-temp scripts and therefore is not an auditable/upgradable repository product asset
03_why_correction_necessary: Installation/lifecycle is a Shell six-module responsibility and cannot disappear after external mechanical evidence
04_correct_owner: Installer/Lifecycle Implementation Worker + independent zero-write Reviewer
05_authoritative_inputs: D03 formally delivered code; Stage2 Registration contract; B03 scripts/evidence read-only as method evidence; exact official/GK release metadata
06_exact_allowed_paths: Product Worker write only golden_key_openmontage_workbuddy/installer.py; golden_key_openmontage_workbuddy/package_assembly.py; tests/workbuddy/test_installer.py; tests/workbuddy/test_package_assembly.py; tests/workbuddy/test_repository_hygiene.py; pyproject.toml; D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D04_test_roots\ and D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D04_evidence\; read exact D03 workbuddy-skill/golden-key-openmontage/ tree byte-for-byte; Closeout Worker additionally write only the six authority docs
07_concrete_actions: Implement deterministic assembly from an exact immutable Package source plus exact Shell adapter/toolchain inputs; copy the exact D03 Package-agnostic Skill tree byte-for-byte rather than generating or stamping it; keep Package-specific identity only in model-invisible Manifest/Lock/Registration binding; validate generic placeholder tokens; implement install/register/activate/update/rollback/uninstall with CAS and user-data preservation; make every output reproducible and reviewable
08_explicitly_not_do: No materialization into production roots; no WorkBuddy; no Package source mutation; no Provider/media; no reuse of B03 final Skill/binding/hash; no C-drive cache except system-required package metadata
09_output_contract: Versioned Installer/assembly/lifecycle code and tests on the formal branch
10_positive_tests: Deterministic byte-identical build fixture; package-agnostic Skill hash across Package identities; exact hidden binding; private toolchain closure; register/activate/locate/update/rollback/uninstall; preservation of DataRoot/projects/credentials
11_negative_tests: Generic installer token; stale binding; Package mutation; missing toolchain; wrong commit/tree; unsafe removal; cross-root write; old B03 identity reuse
12_independent_reviewer_checks: Exact allowlisted product-path diff plus six-doc closeout; ownership and filesystem boundaries; reproducibility; lifecycle recovery; Package-agnostic Skill proof; focused/full tests and CI
13_p0_p1_p2_standard: P0 unsafe install/delete or Package mutation; P1 unreproducible artifact, visible binding, lifecycle/data-preservation defect; P2 evidence/packaging defect
14_fail_closed_conditions: D03 absent; output path escape; global dependency use; any destructive target not exact; test/CI failure; B03 final identity reused
15_upstream_dependency: D03 formally delivered; explicit Owner authorization; project .venv only
16_downstream_handoff: D05 only after reviewed ordinary FF and cleanup of task-only build intermediates
17_real_workbuddy_required: NO
18_official_control_group: NO / fixtures only
19_involves_0_3_25: Read-only release metadata/fixture only
20_proves_after_completion: A versioned, reviewable Installer/lifecycle implementation exists
21_cannot_prove_after_completion: Fresh real assemblies, client, official/GK/video/business success
```

补充合同：

```text
22_project_target: Make Installer/assembly/lifecycle a versioned Shell product responsibility while preserving immutable OpenMontage
23_deviation_to_remove: Temp-only B03 scripts and Package-stamped Skill/binding
24_input_commit_tree: Shell formal commit/tree containing promoted D03 = NOT_PROVED_FUTURE_INPUT, resolve full 40-hex at takeover; official = cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / 6cd1961d552dd9d2bcfba990b80ac06edfe4b061; GK = 73cab67322451601a824875c0e426067d736dd44 / 29231e0464fa4bc7533c1928415849e9b3a48e7c; B03 evidence plus installer-source file-list/SHA256 manifest = NOT_PROVED_FUTURE_INPUT and must be recorded before read
25_prerequisites: Dynamic objects resolved, D03 formal, separate Owner D04 authorization, project .venv/write baselines verified and D04 test/evidence roots absent
26_exact_allowlist: WRITE six product/test paths, D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D04_test_roots\, D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D04_evidence\ and six authority docs; READ workbuddy-skill\golden-key-openmontage\ from the promoted D03 formal tree; D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673\GOLDEN_KEY_OPENMONTAGE_RELEASE.json; D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-golden-key-v0.3.25-73cab673\GOLDEN_KEY_OPENMONTAGE_0_3_25_MIGRATION.json; D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_evidence\B03-EVIDENCE.json; D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_evidence\B03-REPORT.md; and B03 installer source scripts only after their exact file list/SHA256 manifest is recorded in field 24 at takeover
27_exact_denylist: ALL other paths/state; no WorkBuddy/client, real PackageRoot/production Registration, Provider/media, Package-source mutation or C-drive engineering cache
28_product_code_change: YES / only installer.py, package_assembly.py, three named tests and pyproject.toml
29_workbuddy_user_action: NO
30_package_action: NO real install/replace/register/activate; immutable Package fixtures and temp test assemblies only
31_exact_steps: Resolve inputs -> freeze read/write hashes -> write lifecycle/reproducibility failure tests -> implement versioned Installer/assembly -> full lifecycle/fault tests -> full suite/CI -> cleanup fixtures -> Q1-Q10 -> closeout/review
32_positive_acceptance: Fields 10 and 12, including byte-for-byte copy of D03 Skill and deterministic fixture assemblies
33_negative_assertions: Field 11 plus zero Package/client state change and zero non-allowlisted diff
34_failure_conditions: Field 14, unresolved input, data-loss risk, need for non-allowlisted write, test/CI failure or non-identical build
35_evidence_location: Versioned code/tests, six-doc closeout and D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D04_evidence\
36_worker_reviewer_split: Installer Worker owns product/test paths; Closeout Worker owns docs; independent Reviewer zero-write checks destructive boundaries, reproducibility and CI
37_rollback_recovery: Tests use disposable roots and restore activation pointer from captured CAS state; before promotion abandon branch; after promotion only reviewed revert/correction commit
38_temp_cleanup: Remove exact disposable test assemblies/tool caches after manifest and Reviewer capture; preserve user DataRoot/projects/credentials and retained evidence
39_git_gates: Tests PASS -> Reviewer APPROVE -> commit -> push/CI -> exact headSha review -> separate Owner promotion -> ordinary FF -> separate D05 authorization
40_end_drift_audit: Q1-Q10 after lifecycle/cleanup and after every repair; D05 real assembly remains NOT_PROVED
41_not_proved_after_task: Fresh distributions, real WorkBuddy, official/GK runtime/video and business result remain NOT_PROVED
42_no_downstream_repair: D05 only materializes approved D04 behavior; it cannot repair Installer code, lifecycle or reproducibility
```

#### [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] D05 双对象 fresh assembly、Registration 与 lifecycle 证明

```text
01_task_id: V2-CORRECTION-D05-FRESH-DUAL-ASSEMBLY
02_confirmed_issue: No fresh artifact exists from D03/D04, and B03 outputs bind superseded code
03_why_correction_necessary: D06/D07 require clean reproducible official and 0.3.25 inputs without acceptance-time repair
04_correct_owner: Release Assembly Worker + independent zero-write Reviewer
05_authoritative_inputs: D03/D04 exact formal commits; official cd9f3c1f/tree 6cd1961d detached clean; GK 73cab673/tree 29231e04 parents exact detached clean; Package Registration contract
06_exact_allowed_paths: Read-only exact official/GK checkouts; write only D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D05_shell_source\ (fresh exact checkout), D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D05_assembly\, D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D05_evidence\ and task-owned Registration/Activation records under those roots; Closeout Worker additionally write only the six authority docs
07_concrete_actions: Build official and GK assemblies twice from D04; prove Package subtree immutability, same Skill ZIP/hash, separate hidden bindings, complete private Python/FFmpeg/ffprobe/Node/npm/npx, Manifest/Lock coverage, register/activate/new-process locate, update/rollback/uninstall and cleanup; retain exact reviewed acceptance artifacts
08_explicitly_not_do: No WorkBuddy; no old B03 roots/registrations/Skill; no Package mutation; no Provider/media; no source checkout treated as installed PackageRoot
09_output_contract: Two independently reproducible fresh assemblies, one Package-agnostic Skill ZIP, Package-specific hidden binding records, lifecycle/evidence bundle
10_positive_tests: Double-build byte equality; same Skill hash; Package identities exact; toolchain/import/version; generic token scan; registration/lifecycle; immutable snapshots
11_negative_tests: Non-Package drift; stale token/hash; wrong parent/tree; unlisted byte; shared mutable PackageRoot; rollback/uninstall failure; residue outside task roots
12_independent_reviewer_checks: Exact inputs/outputs/hashes; D03/D04 objects consumed; both Package subtrees unchanged; Skill equality; lifecycle; cleanup and retained-evidence manifest
13_p0_p1_p2_standard: P0 identity substitution, Package mutation or unsafe lifecycle; P1 stale binding/toolchain/reproducibility failure; P2 evidence packaging defect
14_fail_closed_conditions: Input identity drift; task roots not fresh; any byte/token/toolchain/lifecycle mismatch; cleanup target ambiguous
15_upstream_dependency: D04 formally delivered; explicit Owner authorization; all fresh roots verified absent
16_downstream_handoff: D06 only; old B04 client evidence is negative reference only
17_real_workbuddy_required: NO
18_official_control_group: YES / fresh assembly prepared
19_involves_0_3_25: YES / fresh assembly prepared
20_proves_after_completion: Both exact distributions are reproducibly installable through the same versioned Shell/Installer with one identical Skill
21_cannot_prove_after_completion: WorkBuddy behavior, real OpenMontage tools/video, same-path runtime compatibility or business effect
```

补充合同：

```text
22_project_target: Produce reproducible fresh official/GK installed inputs with one identical model-facing Skill
23_deviation_to_remove: Reuse of B03 superseded output, temp Installer identity and Package-specific Skill bytes
24_input_commit_tree: Shell formal commit/tree containing promoted D04 = NOT_PROVED_FUTURE_INPUT, resolve full 40-hex at takeover; official = cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / 6cd1961d552dd9d2bcfba990b80ac06edfe4b061; GK = 73cab67322451601a824875c0e426067d736dd44 / 29231e0464fa4bc7533c1928415849e9b3a48e7c with parents ef5f5b58fa1c2b494b0154989cf0e4e36615a701 + cd9f3c1f03368be87b140af494914b8ee4e3c7a4
25_prerequisites: Field 24 resolved, D04 formal, separate Owner D05 authorization, all fresh roots/Registration IDs absent and exact cleanup targets predeclared
26_exact_allowlist: READ two exact external checkouts; WRITE only D05 shell_source, assembly, evidence roots, task-owned Registration/Activation records under those roots and six authority docs
27_exact_denylist: ALL other paths/state; WorkBuddy/client, B03/B04 installed outputs/registrations, Package source, Provider/media and production roots forbidden
28_product_code_change: NO / consume exact promoted Installer
29_workbuddy_user_action: NO
30_package_action: YES / assemble, install, register, activate, locate, update, rollback and uninstall only two task-owned fresh distributions; no source mutation or production replacement
31_exact_steps: Resolve/freeze inputs -> assert roots/IDs absent -> two independent builds each Package -> hash/Skill equality/toolchain checks -> lifecycle on task-owned roots -> immutable before/after snapshots -> cleanup disposable copies -> closeout/Q1-Q10/review
32_positive_acceptance: Fields 9-12 plus full 40-hex source lineage, identical Skill ZIP SHA256 and lifecycle recovery state
33_negative_assertions: Field 11 plus no client state and no write outside exact D05 roots/six docs
34_failure_conditions: Field 14, any lifecycle recovery failure, Package-source diff, different Skill byte or untracked residue; D06 stays blocked
35_evidence_location: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D05_evidence\ with immutable manifest/hashes; reviewed assemblies remain in D05 assembly root; six docs store exact identities/verdict
36_worker_reviewer_split: Assembly Worker runs versioned Installer/lifecycle; Closeout Worker writes docs; independent Reviewer zero-write rehashes objects and verifies cleanup/immutability
37_rollback_recovery: Restore prior task activation pointer or uninstall exact task Registration using D04 CAS; never alter production/current user Registration; preserve failed roots read-only for review
38_temp_cleanup: Remove double-build scratch roots, installer download/cache and uninstalled disposable roots after evidence capture; retain only reviewed assemblies/evidence until post-D08 manifest cleanup
39_git_gates: External evidence APPROVE -> docs result commit -> push candidate -> exact review -> separate Owner result promotion -> ordinary FF -> separate D06 authorization; assembly existence alone creates no promotion
40_end_drift_audit: Q1-Q10 after lifecycle and cleanup; client/video claims must remain NOT_PROVED
41_not_proved_after_task: WorkBuddy behavior, real registry tools/checkpoints/video, same-path compatibility and business outcome remain NOT_PROVED
42_no_downstream_repair: D06 may only consume immutable approved assemblies; any toolchain/binding/lifecycle defect returns to D05/D04 and requires a new reviewed object
```

#### [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] D06 official 完整本地成片 control acceptance

```text
01_task_id: V2-CORRECTION-D06-OFFICIAL-LOCAL-VIDEO-CONTROL
02_confirmed_issue: Current official cd9f3c1f has no repeatable full WorkBuddy+Shell local-video proof
03_why_correction_necessary: First-Artifact or receipt-only evidence would leave tool/checkpoint/compose defects for the GK comparison to discover
04_correct_owner: Official Control Acceptance Worker + independent zero-write Reviewer
05_authoritative_inputs: D05 fresh official assembly and exact Skill; D01/D02 acceptance method; official Guide and a user-selectable production Pipeline; one frozen no-paid-provider media fixture/brief; current WorkBuddy client
06_exact_allowed_paths: Read-only D05 assembly/evidence and frozen D06 control input; write only D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D06_official_data_root\, D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D06_official_evidence\ and WorkBuddy state limited to one exact Skill, one official Registration and two fresh sessions; Closeout Worker additionally write only the six authority docs
07_concrete_actions: Fresh install/register/activate/new-process locate; install exact Package-agnostic Skill; run the same ordinary business brief twice; WorkBuddy must select a user Pipeline (never framework-smoke), read exact Guide/manifest/Stage/meta Skills, run preflight, create canonical artifacts/checkpoints/reviews, invoke real local registry tools through Shell, compose and validate a playable local video; capture complete lineage and clean task state after review
08_explicitly_not_do: No code/Installer/Skill/Package repair; no helper/source diagnosis; no technical prompt; no direct fallback; no paid Provider; no GK; no security bypass
09_output_contract: Two-run official evidence bundle with exact client/Skill/Package/Registration/session/resource-read/operation/receipt/checkpoint/Artifact/video identities, or precise INCOMPLETE owner handoff
10_positive_tests: Two fresh end-to-end videos; ordinary prompts; Agent-first order; WorkBuddy decisions; real local tools; schema-valid lineage; playable video/ffprobe; identical method with bounded allowed variability
11_negative_tests: framework-smoke selection; wrong Package; missing Guide/Stage read; direct fallback; receipt without Artifact/video; mutation; hidden repair; truncated trace; Package-root writes outside projects/results
12_independent_reviewer_checks: Exact hashes/prompts/sessions; full trace; decision owner; manifest tool allowlist; receipt/Artifact/video correlation; repeatability; residue
13_p0_p1_p2_standard: P0 false real-video claim, wrong Package or second control plane; P1 missing Agent-first/tool/checkpoint/video evidence, fallback/mutation/residue; P2 correlation defect
14_fail_closed_conditions: D05 not APPROVE; frozen fixture unavailable; identity mismatch; any technical model routing; missing provenance; acceptance-time repair
15_upstream_dependency: D05 APPROVE; explicit Owner authorization; Owner performs any client permission decision; user-approved low-cost model if available
16_downstream_handoff: D07 only after independent APPROVE; failure returns to named Shell/Installer/Package/WorkBuddy owner without changing D06 inputs
17_real_workbuddy_required: YES / two fresh full sessions
18_official_control_group: YES / cd9f3c1f exact
19_involves_0_3_25: NO
20_proves_after_completion: Repeatable full local-video Agent-first integration for current official through the corrected Shell
21_cannot_prove_after_completion: GK compatibility, paid Providers, portrait business quality or formal project closeout
```

补充合同：

```text
22_project_target: Prove the corrected WorkBuddy+Shell path can repeatedly complete the current official Agent-first local-video flow
23_deviation_to_remove: Treating receipt/first Artifact/direct fallback as official product success
24_input_commit_tree: Shell formal commit/tree containing promoted D05 result and D03/D04 code = NOT_PROVED_FUTURE_INPUT, resolve full 40-hex at takeover; official = cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / 6cd1961d552dd9d2bcfba990b80ac06edfe4b061; D05 assembly/evidence manifest SHA256, Skill ZIP SHA256, client version/binary hash and frozen fixture manifest SHA256 = NOT_PROVED_FUTURE_INPUT
25_prerequisites: Every field 24 identity recorded, D05 formal, separate Owner D06 authorization, fresh D06 data/evidence roots, frozen no-paid fixture and Owner-present permission decisions
26_exact_allowlist: READ D05 assembly/evidence and frozen D06 control input; WRITE only D06 official_data_root, official_evidence, one exact WorkBuddy Skill/official Registration/two sessions and six authority docs
27_exact_denylist: ALL other paths/state; code/test/Installer/Skill source/ZIP/Package source, GK, paid Provider, unrelated WorkBuddy tasks/Skills and media outside frozen fixture forbidden
28_product_code_change: NO
29_workbuddy_user_action: YES / Owner performs client permissions, exact Skill install and two ordinary-language task submissions; no technical routing or security bypass
30_package_action: YES / install/register/activate/locate exact D05 official assembly in fresh task DataRoot; no replace/mutate/repair; uninstall only per rollback
31_exact_steps: Resolve inputs -> before-state -> fresh install/register/activate/new-process locate -> Skill hash verify -> two identical ordinary briefs -> full trace/video capture -> ffprobe/business-neutral technical inspection -> cleanup/after-state -> closeout/Q1-Q10/review
32_positive_acceptance: Fields 10 and 12; each run reaches a full playable local video with Guide/manifest/Stage/meta/tool/review/checkpoint lineage
33_negative_assertions: Field 11 plus no Package-owned or non-Package input mutation, no paid call and no acceptance-time diagnosis/edit
34_failure_conditions: Field 14 or any missing second video/lineage/cleanup fact; classify exact owner and keep D07 blocked
35_evidence_location: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D06_official_evidence\ with immutable trace/video manifest; six docs store exact verdict/hashes
36_worker_reviewer_split: Acceptance Worker operates exact client path/captures evidence; Owner makes permissions only; Closeout Worker writes docs; independent Reviewer zero-write inspects both videos/lineage/state
37_rollback_recovery: Uninstall only exact D06 Skill and official Registration, restore captured pre-task activation pointer and preserve failed evidence/DataRoot read-only until review
38_temp_cleanup: Remove task session scratch, duplicate downloads and non-evidence intermediates after Reviewer capture; retain frozen input, accepted data/evidence and exact failure artifacts until project cleanup
39_git_gates: No product commit; Reviewer APPROVE -> six-doc result commit -> push -> separate Owner result promotion -> ordinary FF/remote verify -> separate D07 authorization
40_end_drift_audit: Q1-Q10 after two runs and cleanup; any first-artifact shortcut, technical prompt or fallback is NO
41_not_proved_after_task: GK compatibility, paid capability, portrait business quality, scale and closeout remain NOT_PROVED
42_no_downstream_repair: D07 receives immutable D06 inputs/method; an official defect cannot be hidden by changing GK or acceptance method
```

#### [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] D07 仅切换 Golden Key 0.3.25 的同路径完整成片比较

```text
01_task_id: V2-CORRECTION-D07-GK-0_3_25-SAME-PATH-VIDEO
02_confirmed_issue: GK 0.3.25 has not run through the approved official path with only Package-derived binding changed
03_why_correction_necessary: Full same-path comparison is required before the final store use case so D08 is not a repair window
04_correct_owner: Controlled Package Comparison Worker + independent zero-write Reviewer
05_authoritative_inputs: D06 approved immutable non-Package inputs; D05 fresh GK assembly; GK 73cab673/tree/parents exact; identical Package-agnostic Skill ZIP
06_exact_allowed_paths: Read-only D05 assembly/evidence and D06 control input/evidence; write only D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D07_gk_data_root\, D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D07_gk_evidence\ and WorkBuddy state limited to unchanged Skill ZIP, one fresh GK Registration and two fresh sessions; Closeout Worker additionally write only the six authority docs
07_concrete_actions: Prove every non-Package byte/method unchanged; install/register/activate GK in fresh DataRoot; run the exact D06 brief twice; capture the same structural Agent-first/full-video evidence and compare; Package-owned Guide, manifests, Stage/meta Skills, tool registry, selected user Pipeline and their resource identities may differ only as direct consequences of the exact Package switch; WorkBuddy must choose according to each Package's own authority, so the Pipeline ID is not forced equal
08_explicitly_not_do: No Shell/Installer/Skill source/ZIP/prompt/fixture/model/method change; no old 0.3.24; no Package mutation; no acceptance-time repair; no Provider/media expansion
09_output_contract: Exact one-variable full-video comparison or precise fail-closed owner attribution
10_positive_tests: Same Skill hash and inputs; fresh GK binding; exact Guide/GK selected manifest/Stage Skills; real local tools/checkpoints/video; two-run repeatability; immutable Package
11_negative_tests: Any non-Package byte/method drift; any Package-owned semantic difference not traceable to the two exact immutable Package trees; forced equal Pipeline ID against the Package Guide; stale state; old input; Package mutation; direct fallback; evidence reuse; technical prompt
12_independent_reviewer_checks: Byte comparison of all non-Package inputs; source-object proof for every Package-owned Guide/manifest/Stage/tool/Pipeline difference; exact GK identity; trace/Artifact/video correlation; no non-Package second variable
13_p0_p1_p2_standard: P0 false compatibility, two-variable test or Package mutation; P1 stale/non-matching input, missing real video evidence or fallback; P2 comparison defect
14_fail_closed_conditions: D06 not APPROVE; any non-Package mismatch; fresh state unavailable; exact GK mismatch; incomplete evidence
15_upstream_dependency: D06 APPROVE; explicit Owner authorization
16_downstream_handoff: D08 only after independent APPROVE; otherwise return to named owner and preserve D07 inputs
17_real_workbuddy_required: YES / two fresh full sessions
18_official_control_group: YES / immutable D06 reference
19_involves_0_3_25: YES / exact 73cab673; 0.3.24 forbidden
20_proves_after_completion: Corrected path is compatible or precisely incompatible with GK 0.3.25 under one-variable full-video comparison
21_cannot_prove_after_completion: Real store portrait business quality, paid/provider breadth, scale or closeout
```

补充合同：

```text
22_project_target: Prove GK 0.3.25 compatibility through the same structural path while changing only the immutable Package-owned authority/binding variable
23_deviation_to_remove: Two-variable comparison or forcing official pipeline semantics onto a Package that legitimately adds Golden Key user Pipelines
24_input_commit_tree: Shell formal commit/tree containing promoted D06 result = NOT_PROVED_FUTURE_INPUT, resolve full 40-hex at takeover; official control = cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / 6cd1961d552dd9d2bcfba990b80ac06edfe4b061; GK = 73cab67322451601a824875c0e426067d736dd44 / 29231e0464fa4bc7533c1928415849e9b3a48e7c; D05/D06 manifest, Skill ZIP, client/model/fixture/method hashes = NOT_PROVED_FUTURE_INPUT
25_prerequisites: All field 24 identities resolved, D06 formal, separate Owner D07 authorization, fresh GK root/Registration/sessions and exact one-variable comparison manifest frozen
26_exact_allowlist: READ D05/D06 approved inputs/evidence and exact GK checkout; WRITE only D07 GK data/evidence roots, unchanged Skill installation, one fresh GK Registration/two sessions and six authority docs
27_exact_denylist: ALL other paths/state; any Shell/Installer/Skill/prompt/fixture/client/model/method change, official/GK source mutation, 0.3.24, Provider/media expansion and D06 evidence edit forbidden
28_product_code_change: NO
29_workbuddy_user_action: YES / Owner repeats the exact D06 permission and ordinary-language procedure; no technical routing
30_package_action: YES / install/register/activate exact fresh GK assembly in its own DataRoot; only PackageRoot/Registration/hidden binding and Package-owned Guide/manifest/Stage/meta/tool/Pipeline identities/semantics may differ; no mutation
31_exact_steps: Resolve/freeze byte comparison -> assert fresh state -> install/activate GK -> verify same Skill -> run exact brief twice -> capture full lineage/videos -> attribute every difference to Package tree or reject -> cleanup -> closeout/Q1-Q10/review
32_positive_acceptance: Fields 10 and 12; structural sequence and non-Package bytes/method identical; WorkBuddy may select the correct Package-specific user Pipeline under that Package's Guide
33_negative_assertions: Field 11; forced Pipeline-ID equality, untraceable semantic difference or any non-Package second variable is failure
34_failure_conditions: Field 14, incomplete source attribution, missing full video/run, non-Package drift or cleanup failure; D08 remains blocked
35_evidence_location: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D07_gk_evidence\ plus immutable cross-package comparison manifest and six-doc exact verdict
36_worker_reviewer_split: Comparison Worker performs frozen procedure; Owner handles identical client decisions; Closeout Worker writes docs; independent Reviewer zero-write rehashes all non-Package inputs and source-attributes differences
37_rollback_recovery: Uninstall exact GK Registration/Skill only, restore pre-D07 activation pointer without changing D06 evidence, preserve failed GK DataRoot/evidence read-only
38_temp_cleanup: Remove session scratch and non-evidence intermediates after review; retain exact D05-D07 accepted/failure evidence until post-D08 cleanup authorization
39_git_gates: Reviewer APPROVE -> six-doc result commit -> push -> separate Owner result promotion -> ordinary FF/remote verify -> separate D08 authorization
40_end_drift_audit: Q1-Q10 after comparison/cleanup; Q5 passes only when all method bytes are equal and Package semantic differences have exact source provenance
41_not_proved_after_task: Store portrait business quality, paid/provider breadth, scale and project closeout remain NOT_PROVED
42_no_downstream_repair: D08 must consume the approved unchanged GK path; any compatibility or video defect returns to its named owner and cannot be repaired during business acceptance
```

#### [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] D08 真实门店业务验收、项目状态收口候选与推广清单

```text
01_task_id: V2-CORRECTION-D08-BUSINESS-ACCEPTANCE-CLOSEOUT
02_confirmed_issue: Technical local-video evidence cannot prove the original portrait store outcome or repository delivery readiness
03_why_correction_necessary: Project completion requires an ordinary-user real business task, correct process, accepted video and exact closeout state
04_correct_owner: Business Acceptance Owner + Closeout Worker + independent zero-write Reviewer
05_authoritative_inputs: D06/D07 approved evidence; exact formal Shell/Installer; exact GK assembly; Owner-frozen source material, portrait requirements, rights, cost/provider approvals and acceptance owner; live remote/CI authority
06_exact_allowed_paths: Frozen business source roots read-only; D06/D07 evidence read-only; D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D08_business_evidence\ (fresh); the six authority docs only for closeout candidate; WorkBuddy state limited to unchanged Skill/GK Registration and one fresh business session
07_concrete_actions: Run one ordinary business request through approved GK path; allow WorkBuddy/OpenMontage to select the correct Golden Key user Pipeline, observe all distinct human/provider/cost gates, use only separately approved real capabilities, produce and independently inspect the portrait video; obtain business acceptance; audit exact Git/CI/Package/client/residue; write six-doc closeout candidate and an exact proposed promotion/cleanup manifest; stop
08_explicitly_not_do: No Shell media/creative patch; no technical prompt; no silent Provider/fallback; no code repair during acceptance; no promotion/delete in D08; no unrelated branch/worktree cleanup
09_output_contract: Business evidence, accepted/rejected decision, six-doc closeout candidate and exact proposed promotion/cleanup manifest with zero promotion effect
10_positive_tests: Ordinary request; correct GK Pipeline semantics; real tools and approval receipts; playable portrait video with expected source/orientation/audio/subtitle/lineage; independent business acceptance; exact Git/CI/state
11_negative_tests: Technical prompt; wrong orientation/video; fabricated evidence; direct fallback; identity drift; missing gate/evidence; Shell creative fix; unreviewed promotion or ambiguous cleanup target
12_independent_reviewer_checks: Business brief/material rights/video semantics; D06/D07 lineage; exact identities; provider/cost approvals; full evidence; six-doc diff; Git/CI and cleanup manifest
13_p0_p1_p2_standard: P0 false business PASS, unsafe promotion/delete, identity substitution or unauthorized spend; P1 missing video/gate/review/Git evidence or Shell media expansion; P2 closeout trace defect
14_fail_closed_conditions: D07 not APPROVE; inputs/rights/acceptance owner not frozen; business result rejected; evidence missing; code repair required; live object mismatch
15_upstream_dependency: D07 APPROVE; explicit Owner authorization; business acceptance contract and any paid/provider authorization frozen separately
16_downstream_handoff: STOP_FOR_SEPARATE_OWNER_PROMOTION_APPROVAL; only later exact mechanical FF/remote+CI verification/manifest-bounded cleanup is eligible
17_real_workbuddy_required: YES / one real business session
18_official_control_group: YES / consumes D06 lineage, no new official run
19_involves_0_3_25: YES / exact approved D07 assembly
20_proves_after_completion: Original ordinary-user business outcome and a reviewed project closeout candidate
21_cannot_prove_after_completion: Universal scale, every Provider/renderer/format, or formal promotion before Owner approval
```

补充合同：

```text
22_project_target: Prove the original ordinary-user store outcome and prepare an exact, reviewable repository closeout without executing promotion/cleanup
23_deviation_to_remove: Technical PASS substituted for business acceptance, Shell creative repair and closeout mixed with destructive promotion/cleanup
24_input_commit_tree: Shell formal commit/tree containing promoted D07 result = NOT_PROVED_FUTURE_INPUT, resolve full 40-hex at takeover; GK = 73cab67322451601a824875c0e426067d736dd44 / 29231e0464fa4bc7533c1928415849e9b3a48e7c; D06/D07 evidence manifests, unchanged Skill ZIP, business-source/rights/brief/acceptance manifest, client/model/provider identities = NOT_PROVED_FUTURE_INPUT
25_prerequisites: All field 24 inputs and rights frozen, D07 formal, separate Owner D08 authorization, named business accepter, explicit provider/cost ceilings and fresh evidence root
26_exact_allowlist: READ frozen business sources and D06/D07 evidence; WRITE only D08 business evidence, unchanged approved WorkBuddy/GK session state and six authority docs; proposed cleanup manifest is data only
27_exact_denylist: ALL other paths/state; product code/tests/Installer/Skill/Package mutation, unapproved Provider/spend, unrelated client state, formal branch promotion and any deletion forbidden
28_product_code_change: NO
29_workbuddy_user_action: YES / Owner submits ordinary business request and alone approves permissions/provider/cost/human gates; independent business accepter evaluates final portrait video
30_package_action: NO replace; reuse exact approved D07 GK assembly/Skill/binding, validate identity only; no install mutation except exact task session state
31_exact_steps: Resolve/freeze inputs/gates -> before-state -> ordinary store request -> capture Agent-first/human/provider/tool lineage -> inspect portrait video -> business decision -> Git/CI/client/residue audit -> write six-doc closeout and proposed manifest -> Q1-Q10 -> zero-write review -> stop
32_positive_acceptance: Fields 9-12 plus explicit accepted/rejected business decision, playable portrait result, exact rights/cost receipts and complete closeout manifest
33_negative_assertions: Field 11 plus zero product repair, zero formal promotion/delete and no result claim beyond accepted evidence
34_failure_conditions: Field 14, rejected video, unauthorized cost, identity/evidence mismatch or any required repair; project remains INCOMPLETE and no closeout promotion
35_evidence_location: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D08_business_evidence\ and six authority docs; exact promotion/cleanup manifest contains targets and protected non-targets
36_worker_reviewer_split: Business Run Worker captures path; Owner handles approvals; independent Business Accepter judges video; Closeout Worker writes docs/manifest; independent zero-write Reviewer audits all layers
37_rollback_recovery: Stop/cancel exact task, preserve evidence, restore pre-D08 task/session state only; no code rollback is allowed because no code change; failed business output stays evidence, not PASS
38_temp_cleanup: During D08 remove only task session scratch explicitly listed in before/after manifest; retain business evidence and every promotion/cleanup target; actual project cleanup waits for later Owner authorization
39_git_gates: Reviewer APPROVE permits candidate closeout commit; push is separate; formal closeout promotion requires separate Owner approval and ordinary FF/remote+CI verification; actual manifest-bounded cleanup is another separately authorized action
40_end_drift_audit: Q1-Q10 after business decision and closeout diff; final report repeats Q1-Q10 and stops
41_not_proved_after_task: Universal scale, every Provider/renderer/format and formal closeout remain NOT_PROVED until separate promotion; acceptance cannot generalize beyond frozen case
42_no_downstream_repair: There is no product downstream task; rejection or defect returns to the named D03-D07 owner under a new authorization, never repaired inside closeout/promotion
```

### 5. 原始八阶段、十一步、T1-T12、R01-R08 全量映射

| 原始对象 | 新任务覆盖 | 验收证据 | 废止/边界依据 |
|---|---|---|---|
| Stage1 冻结边界 | D02 | six-doc contract + Reviewer | 旧 fixed-child 推导废止 |
| Stage2 Registration | D04-D05 | versioned Installer tests + fresh register/locate | 原实现保留；临时 proof 不等 final |
| Stage3 Launcher | D02-D03 | semantic operation contract/code/tests | whole-request child 废止 |
| Stage4 WorkBuddy Skill | D01-D03,D06 | native surface + Package-agnostic Skill + real client | B02 Skill 废止 |
| Stage5 progressive Runtime | D04-D07 | private toolchain + optional capability facts | Stage3 accepted boundary保留 |
| Stage6 reduce CLI/MCP | D02-D03 | one internal semantic surface; no MCP/router | arbitrary/technical CLI 废止 |
| Stage7 Installer/upgrade/migration | D04-D05 | versioned code + lifecycle + deterministic assemblies | B03 temp-only Installer 废止 |
| Stage8 layered acceptance | D06-D08 | official, GK, business three layers | receipt/Artifact-only不算完整 |
| Step1 architecture | D02 | target/role/negative gates | Phase A A6 superseded |
| Step2 Registration | D04-D05 | exact final objects | Stage2 proof narrowed |
| Step3 Launcher binding | D02-D03 | hidden binding + bounded calls | host-env exact set废止 |
| Step4 production Skill | D01-D03 | real surface + package-agnostic Skill | B02 Skill废止 |
| Step5 Runtime | D04-D07 | toolchain/capabilities | 保留 current Stage3 |
| Step6 Installer/lifecycle | D04-D05 | versioned implementation + real lifecycle | 不再用 temp-only scripts |
| Step7 offline/security/fault | D03-D05 | focused/full/CI + assembly fault matrix | 旧错误合同测试仅历史 |
| Step8 first real WorkBuddy | D06 | two full official local videos | first Artifact不足 |
| Step9 corrected Core | D07 | exact GK same-path videos | old 0.3.24历史-only |
| Step10 store acceptance | D08 | portrait video + business approval | technical PASS不替代 |
| Step11 optional fork/MCP/more entries | post-D08 separate decision | separate future evidence | 本主链明确不覆盖 |
| T1 entry | D01-D03,D06 | native surface/Skill/client | fixed envelope废止 |
| T2 input | D02-D03 | business user message + semantic ops | model-visible binding废止 |
| T3 validation order | D02-D07 | identity/resource-read trace | 未验证 Guide禁止 |
| T4 adapter | D02-D03 | per-operation receipts | whole-request call废止 |
| T5 auth/continuation | D02,D06-D08 | distinct gate receipts | Shell不作授权决定 |
| T6 result mapping | D02-D03,D06 | operation/status/Artifact lineage | one receipt闭集不足 |
| T7 privacy | D03-D08 | closed child env/secret checks | host env exact ownership废止 |
| T8 failures | D02-D08 | per-task fail-closed handoff | 下游 repair window禁止 |
| T9 Package gate | D04-D05 | final assemblies/Registration | old B03 binding废止 |
| T10 evidence layers | all D tasks | explicit evidence matrix | static/client/business分离 |
| T11 Stage6 relay | D02-D03,D06 | direct mechanical relay first | 是否需额外代码由真实证据决定 |
| T12 implementation package | D03-D05 | exact allowlists/review/CI | old six-path packet废止 |
| R01 surface | D01 | two-session native proof | old blocked evidence历史保留 |
| R02 binding | D02,D04-D05 | hidden binding + immutable Package | Package defect attribution废止 |
| R03 Skill bundle | D03-D05 | package-agnostic exact ZIP | B02/B03 Skill废止 |
| R04 Installer lifecycle | D04-D05 | versioned code + real lifecycle | B03 methods only参考 |
| R05 materialization | D05 | two fresh roots/registrations | old B03 outputs不复用 |
| R06 Skill install | D06-D07 | same ZIP installed and hit | upload不等 success |
| R07 real WorkBuddy | D06-D08 | official/GK/business sessions | B04 remains incomplete |
| R08 closeout | D08 + later promotion action | business/review/Git/CI/manifest | D08本身不推广 |

### 6. 原 Phase A 23 项交付物映射

| # | 交付物 | 本候选位置/未来证据 |
|---|---|---|
| 1 | 接管核验 | planning header + final Git evidence |
| 2 | 分支/worktree身份 | planning header + final Git evidence |
| 3 | 一页目标 | section 1 |
| 4 | 谱系图 | section 1 success path |
| 5 | 完整追踪矩阵 | sections 5-6 |
| 6 | Stage1-5审查 | section 2 + mapping |
| 7 | Stage6交接 | T11 mapping + D02/D03/D06 |
| 8 | 可保留部分 | section 2 retain column |
| 9 | 缩小/重做/删除/归属 | sections 2-3 |
| 10 | PackageToolDefinitionV1 | D02 hidden binding; model-invisible; per-operation only |
| 11 | launch_session_tool | D02/D03 mechanical primitive; no whole request |
| 12 | workbuddy_entry_cli | D03 rework against D01/D02 |
| 13 | R02归因 | section 2 + D02/D04 |
| 14 | 遗留Stage2分支 | historical-only; hardening separate future authorization |
| 15 | dirty worktrees | protected superseded history; no merge/copy/delete |
| 16 | official->same Shell->GK | D06->D07 |
| 17 | 最小目标架构 | section 1 |
| 18 | 最小任务清单 | D01-D08 |
| 19 | 每任务路径/边界/验收/Reviewer | 21-field packets |
| 20 | 新DoD/下游条件 | fields 9-16 each task |
| 21 | Owner决策 | section 8 below |
| 22 | 文档白名单 | exact six docs in planning header |
| 23 | 是否可固化 | Reviewer+Owner promotion gate; no execution |

### 7. 十问防偏：规划门与执行门

十问原文仍为本文件上节 2712-2721 行。为避免“上游任务因尚未产生下游证据而永远不能批准”的逻辑错误，使用两个严格模式：

- `PLAN_GATE`：逐题证明任务合同直接服务目标、明确 Owner/边界、把尚未证明项列为本任务输出并阻断下游。未知事实不得被当成真，但可以被正确封装为当前任务的 fail-closed 验收目标。
- `EXECUTION_GATE`：逐题检查实际结果；任何要求的事实为 `NOT_PROVED`、证据不足或答案为 NO，当前任务不得 APPROVE，下一任务不得启动。

规划节点逐题结果如下；每格都给出通过依据，不以“已检查”代替：

| 节点 | Q1 用户目标 | Q2 WorkBuddy/Guide | Q3 Shell边界 | Q4 新抽象 | Q5 责任归属 | Q6 外部Owner | Q7 Package只读 | Q8 证据分层 | Q9 用户/模型负担 | Q10 接管/repair |
|---|---|---|---|---|---|---|---|---|---|---|
| 审计开始 | PASS-只读重建 | PASS-唯一Agent为基线 | PASS-零产品动作 | PASS-不预设接口 | PASS-逐层核验 | PASS-无外部实现 | PASS-exact只读 | PASS-FACT分层 | PASS-无用户动作 | PASS-先停执行 |
| 目标模型 | PASS-自然语言到成片 | PASS-Guide/Stage为权威 | PASS-六模块 | PASS-只定义职责 | PASS-Installer回到Shell模块 | PASS-Package生产不纳入 | PASS-0.3.25只读 | PASS-未知显式 | PASS-隐藏binding | PASS-完整链 |
| A/B裁决 | PASS-定位最早偏离 | PASS-A4未证被纠正 | PASS-B02越界废止 | PASS-不美化旧抽象 | PASS-R02回归正确层 | PASS-B03方法非产品 | PASS-历史保留 | PASS-mechanical≠product | PASS-技术JSON废止 | PASS-C路线不续跑 |
| D01计划 | PASS-为真实入口取证 | PASS-只证surface不伪称Guide | PASS-无Shell实现 | PASS-临时probe非产品抽象 | PASS-client事实归WorkBuddy | PASS-无外部产品实现 | PASS-不接Package | PASS-仅client surface | PASS-普通提示 | PASS-BLOCKED不进D02 |
| D02计划 | PASS-冻结正确主链 | PASS-明确决策与资源读 | PASS-机械operation | PASS-仅D01支持的surface | PASS-四方owner清楚 | PASS-Package只供合同 | PASS-无Package写 | PASS-contract-only | PASS-无hash/path/json | PASS-D03 exact handoff |
| D03计划 | PASS-实现可用入口 | PASS-调用顺序归WorkBuddy | PASS-单operation机械 | PASS-adapter有限且无决策 | PASS-Installer未偷入 | PASS-不改Package | PASS-只读fixtures | PASS-offline only | PASS-semantic inputs | PASS-D04不修D03 |
| D04计划 | PASS-补回可交付Installer | PASS-不触碰Agent决策 | PASS-install/lifecycle模块 | PASS-版本化替代temp脚本 | PASS-Installer归本仓库 | PASS-不吞Package Owner | PASS-source只读 | PASS-code evidence | PASS-Skill package-agnostic | PASS-D05只物化 |
| D05计划 | PASS-形成真实输入 | PASS-不声称client | PASS-装配/注册 | PASS-无新控制面 | PASS-只消费D04 | PASS-外部输入只读 | PASS-双Package immutable | PASS-assembly only | PASS-同Skill | PASS-D06禁止修复 |
| D06计划 | PASS-official完整控制 | PASS-完整Guide/Stage证据 | PASS-Shell不选流程 | PASS-无新接口 | PASS-故障归named owner | PASS-无Package修补 | PASS-official immutable | PASS-full video gate | PASS-自然语言 | PASS-D07只在APPROVE后 |
| D07计划 | PASS-GK同路径 | PASS-GK Guide/Stage证据 | PASS-Shell不变 | PASS-无新抽象 | PASS-one-variable attribution | PASS-Package bug回owner | PASS-GK immutable | PASS-control/candidate分离 | PASS-同Prompt/Skill | PASS-D08非修复窗 |
| D08计划 | PASS-真实业务成片 | PASS-GK生产权威 | PASS-无Shell媒体逻辑 | PASS-只closeout | PASS-业务/推广Owner分离 | PASS-Provider逐项授权 | PASS-Package只读 | PASS-business独立层 | PASS-用户只说业务 | PASS-推广另闸 |
| 完整路线 | PASS-全承诺映射 | PASS-唯一Agent全程 | PASS-六模块闭合 | PASS-8任务有必要性 | PASS-无责任丢失 | PASS-外部动作显式 | PASS-old inputs禁用 | PASS-每层独立 | PASS-内部复杂度隐藏 | PASS-每步硬停 |

Reviewer、提交前和最终汇报三个节点必须在实际发生后追加同样 Q1-Q10 的逐题依据；不得预写 PASS。

### 8. Owner 决策、已证明、未证明与硬停止

Owner 仍需逐项决定：规划候选是否推广；D01-D08 是否逐任务授权；每次 WorkBuddy 权限选择；D06/D07 冻结 control fixture 和低成本模型；D08 素材、权利、Provider/费用、验收人；post-D08 promotion/cleanup。任何一次决定不继承为下一次授权。

已证明：实时 formal 对象、official/GK exact 输入、B02代码事实、B03机械方法证据、B04三次负面事实、当前无产品执行授权。未证明：D01 surface、正确代码、版本化 Installer、fresh assemblies、official/GK/业务 E2E。已废止：B01 whole-request contract、B02产品接受、B03 final binding、C01-C07执行候选。明确禁止：当前启动任何 D/C 任务、产品代码/Package/WorkBuddy/Provider/media动作、正式推广或清理历史对象。

### 9. 第一次独立 Reviewer 报告与本任务内纠正

独立零写 Reviewer 在未修改、未 fetch/commit/push、未操作 WorkBuddy/Package 的前提下给出 `REJECT / P0=0 / P1=4 / P2=1`。问题与当前处置如下：

| Finding | Reviewer 结论 | 当前任务内纠正 |
|---|---|---|
| P1-1 | 规划推广与 D08 后项目推广共用 `ONLY_AFTER_D08`，形成 D01 无法启动的死锁 | 拆分 plan promotion、per-task result promotion、post-D08 project closeout/cleanup 三类闸门 |
| P1-2 | D 任务缺完整输入 identity 与 allowlist/denylist；未来输入用动态描述 | 每项新增 24/26/27；固定输入写 full 40-hex，未来对象写 `NOT_PROVED_FUTURE_INPUT` 并成为 takeover hard gate；六文档 closeout 路径逐项补齐 |
| P1-3 | Owner 要求的产品代码、用户操作、Package action、回滚、清理、Git gate 等未逐任务显式 | 每项新增 22-42 共 21 个补充字段，禁止依赖推测 |
| P1-4 | D07 “只变 binding”与 GK 自有 Guide/Pipeline/Stage 语义矛盾 | 固定所有非 Package 输入；允许并只允许 exact immutable Package-owned authority/derived binding 差异；不强制 Pipeline ID 相同，每项差异必须 source-attributed |
| P2-1 | D02/D03 离线阶段误写 `WorkBuddy-ordered` | 改为 `caller-ordered contract fixture`；真实 WorkBuddy 顺序只由 D06/D07 证明 |

Reviewer 完成节点 Q1-Q10：Q1 `PASS-审查直接阻止错误路线固化`；Q2 `PASS-指出离线证据不得冒充 WorkBuddy`；Q3 `PASS-未扩大 Shell 职责`；Q4 `PASS-识别而非掩盖合同矛盾`；Q5 `PASS-纠正 D07 同路径定义`；Q6 `PASS-无 fallback/mock 产品声明`；Q7 `PASS-Reviewer 全程零写`；Q8 `PASS-原始逐任务附加合同缺口被追回`；Q9 `PASS-P0/P1/P2 有 exact diff 证据`；Q10 `PASS-全部问题留在当前规划任务纠正，未交给 D01-D08`。

纠正完成节点 Q1-Q10：Q1 `PASS-D 路线仍直达普通用户真实成片`；Q2 `PASS-唯一 Agent 和 Package-owned authority 更明确`；Q3 `PASS-per-operation Shell 边界不变`；Q4 `PASS-未来 identity 不伪造且 fail-closed`；Q5 `PASS-official/GK 非 Package 方法冻结`；Q6 `PASS-离线 caller fixture 不再冒充 client`；Q7 `PASS-仍仅六文档修改`；Q8 `PASS-每任务 21+21 字段覆盖附加要求`；Q9 `PASS-固定事实与未来 gate 分层`；Q10 `PASS-回滚/清理/推广/repair-window 逐任务封闭`。当前仍须由同一 Reviewer 对修正后的 exact diff 复审；不得预写 `APPROVE`。

### 10. 第二次独立 Reviewer 报告与再次纠正

第二轮零写复审仍为 `REJECT / P0=0`。已关闭：每项 21+21 字段、D04 Skill 边界、D07 one-variable 定义、D02/D03 caller-ordered offline 证据。剩余 P1：较早 C 路线未显式建立 append-only precedence；D02-D04 部分 read allowlist 仍是概念描述且 D03 的 D01 evidence 未标 `NOT_PROVED_FUTURE_INPUT`；D01 单一操作无法支撑 D02 全 operation 映射。

本任务再次纠正：六份文档把较早 C 节标成“仅在本 D 候选正式推广后 superseded”，并在最新节建立明确 append-only precedence；D02-D04 列出可读的 exact root/subtree/file allowlist，D03 evidence identity 改为接管 hard gate；D01 改为只证明 resource/invocation/result primitive catalog，D02 每个 semantic operation 必须同时映射到 D01-proved primitive 和 exact official semantic contract，不再要求 D01 假装证明 OpenMontage 语义。

第二次 Reviewer 节点 Q1-Q10：Q1 `PASS-继续阻止死锁规划`；Q2 `PASS-要求真实 client 证据边界`；Q3 `PASS-未把语义归给 Shell`；Q4 `PASS-指出概念 allowlist 不可执行`；Q5 `PASS-D07 已确认同路径`；Q6 `PASS-离线/真实证据已分开`；Q7 `PASS-零写审查`；Q8 `PASS-检查 42 字段和路线优先级`；Q9 `PASS-P1 有 exact 行证据`；Q10 `PASS-问题仍在规划内修复`。再次纠正节点 Q1-Q10：Q1 `PASS-primitives 服务真实入口`；Q2 `PASS-WorkBuddy 仍按 official 语义决策`；Q3 `PASS-Shell 只承载已证 primitive`；Q4 `PASS-没有从 probe 发明业务语义`；Q5 `PASS-D06/D07 方法不变`；Q6 `PASS-primitive probe 不称产品成功`；Q7 `PASS-仍仅六文档`；Q8 `PASS-无 C/D 双 authority`；Q9 `PASS-未来 identity 仍 fail-closed`；Q10 `PASS-D02 不补 D01 primitive`。当前仍须第三次复审，不得预写结论。

### 11. 第三次独立 Reviewer APPROVE 与提交前防偏

第三轮独立零写 Reviewer 对修正后的 exact uncommitted six-doc diff 给出 `APPROVE / P0=0 / P1=0 / P2=0`。Reviewer 只读核验了：六个旧 C 节与最新 append-only precedence；D02-D04 exact read allowlist 与 future-input hard gates；D01 primitive/D02 semantic contract 双重映射；D01-D08 每项 21+21 字段；`git diff --check`；未提交修改严格只有六个 authority 文档。Reviewer 明确声明：该结论不构成执行授权、规划推广授权或产品验收。

第三次 Reviewer 完成节点 Q1-Q10：Q1 `PASS-APPROVE 仅服务规划正确性`；Q2 `PASS-唯一 WorkBuddy Agent 及真实证据边界已复核`；Q3 `PASS-Shell primitive 与 OpenMontage semantics 分离`；Q4 `PASS-未发现推测合同或新 P0/P1`；Q5 `PASS-D06/D07 non-Package 同路径和 Package-owned 差异清楚`；Q6 `PASS-无 fallback/mock/离线证据升级`；Q7 `PASS-Reviewer 零写且范围仍六文档`；Q8 `PASS-全量映射与 42 字段未丢失`；Q9 `PASS-结论由 exact diff 和机械检查支持`；Q10 `PASS-无问题转嫁 D01-D08`。

准备提交节点 Q1-Q10：Q1 `PASS-提交只固化审计与路线`；Q2 `PASS-不启动 WorkBuddy 或 Agent 流程`；Q3 `PASS-无产品代码/Shell 行为改变`；Q4 `PASS-提交不创造运行事实`；Q5 `PASS-official/GK objects 只读且方法未执行`；Q6 `PASS-NOT_RUN_DOCS_ONLY 明确`；Q7 `PASS-exact six-doc diff`；Q8 `PASS-八阶段/十一步/T1-T12/R01-R08/23项和任务合同均在候选`；Q9 `PASS-Reviewer P0/P1/P2 清零`；Q10 `PASS-提交/推送不推广正式分支且不授权 D01`。若提交前机械核验不再满足这些依据，必须停止并重审。

## [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] D01 合同纠偏候选 Replacement1 历史状态快照（2026-08-24；仅 docs correction，不改变正式 authority）

本节及其所含 D01 Replacement1 合同均为历史记录，不参与当前路由；当前唯一 authority/route 为最新 E01→E07 correction（`V2-E01-ROUTE-BOUNDARY-CORRECTION1`）及六文档同名 current 节。

本节是对上方 D01 42 字段的 append-only replacement candidate。它的纠偏基线是已经正式存在的 D 计划对象 `99bc5c3d727671d7d2ea7313c6851792583efe66` / tree `b995a9a02add77f1e61769f364dd86b341137403`；该基线事实不等于本节已推广或已授权执行。当前本节只允许修改六份权威文档，`NOT_RUN_DOCS_ONLY`，不运行 WorkBuddy，不创建、导入或运行 probe，不修改产品代码、Package、Provider、media，也不启动 D02-D08。

本节在独立零写 Reviewer 复审、Owner 单独批准推广、ordinary fast-forward 进入正式 ref 并完成远端对象核验以前，不改变正式路线；原 D01 仍保留为当前历史对象。只有该候选正式推广后，原 D01 才标记为 `HISTORICAL / SUPERSEDED_BY_D01_CONTRACT_CORRECTION1`，本节才成为 D01 的最新合同。下列 `PRE_RUN_APPROVE`、`APPROVE_FOR_TASK_CLEANUP`、`FINAL_APPROVE` 均为未来执行时必须实际产生的结果，当前不预写任何 Reviewer 结论。

### D01 replacement contract（完整 42 字段）

```text
01_task_id: V2-CORRECTION-D01-WORKBUDDY-NATIVE-SURFACE-PROOF / CONTRACT_REPLACEMENT1
02_confirmed_issue: B04 did not establish one stable WorkBuddy-supported way to read bundled Skill resources and invoke one fixed bundled operation without guessed paths, model-written helpers or Shell technical JSON
03_why_correction_necessary: D01 cannot start from an unreviewed probe, an undefined B04 evidence universe, or an ambiguous cleanup/review sequence; each must be fixed before any client mutation
04_correct_owner: WorkBuddy Surface Investigator Worker + independent zero-write Reviewer; Owner performs all client permission and cleanup actions
05_authoritative_inputs: Current WorkBuddy client; official Tencent WorkBuddy Skill documentation only as documentary evidence; the exact B04 negative-evidence manifest defined below; B04 files read-only; no OpenMontage Package input
06_exact_allowed_paths: Probe Worker may write only D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D01_probe_skill\ and D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D01_native_surface_evidence\; the evidence root may contain only the named Gate-0 record, probe freeze/trace/closeout evidence and manifest; WorkBuddy-managed state is limited to one task-only probe Skill and two fresh task/session IDs; after execution, Closeout Worker may write only the six authority docs to record result/review/status
07_concrete_actions: Gate 0 freezes formal/client/B04 identities and writes the exact B04 manifest plus its SHA256 record before any probe/client mutation; Gate 1 freezes the exact probe source tree, fixtures, ZIP listing/bytes/hash, two literal ordinary-language prompts, permissions and evidence plan and requires an independent zero-write PRE_RUN_APPROVE before import; Gate 2 is Owner-controlled import and two fresh sessions covering the frozen catalog; Gate 3 freezes all run evidence and requires APPROVE_FOR_TASK_CLEANUP before uninstall or deletion; Gate 4 is Owner cleanup/after-state/closeout followed by an independent zero-write final review
08_explicitly_not_do: No official/GK Guide, Package, Registration, Locator, Shell product code, B02/B03/B04 carrier, PackageRoot or assembly, Provider, media or product-success claim; no B04 read outside the exact B04 file set; no absolute-path prompt; no helper authored during the run; no disabling WorkBuddy security; no cleanup before the Gate-3 approval
09_output_contract: Immutable evidence bundle or precise BLOCKED result naming the exact usable/unusable native surface, client/Skill/session identities, Gate-0 manifest hash, every review decision actually reached, explicit NOT_REACHED states for later Gates, trace and after-state where reached; no review result is recorded before it occurs
10_positive_tests: Two fresh ordinary-language runs; exact Skill hit; fixture resource read; every fixed harmless primitive shape exercised, including at least two sequential enum-selected calls; complete observable results; no model technical assembly; Gate 1 contains PRE_RUN_APPROVE, Gate 3 contains APPROVE_FOR_TASK_CLEANUP, and Gate 4 contains FINAL_APPROVE
11_negative_tests: Wrong Skill; guessed install path; model-created helper; direct fallback; missing or drifted B04 manifest; missing PRE_RUN_APPROVE; import/client mutation before Gate 1; missing final exit/trace; cleanup before APPROVE_FOR_TASK_CLEANUP; unclean probe residue; security bypass; after-state mismatch; missing FINAL_APPROVE
12_independent_reviewer_checks: Before import, independently verify exact probe source tree, fixtures, ZIP listing/bytes/hash, literal prompts, permissions/evidence plan, Gate-0 identity records and B04 manifest hash, then return PRE_RUN_APPROVE or block; after both runs, independently verify frozen traces and return APPROVE_FOR_TASK_CLEANUP or block; after Owner cleanup/after-state and Closeout Worker result/Q1-Q10, independently recheck the complete exact final evidence/docs and return FINAL_APPROVE or block; Reviewer is zero-write, changes no reviewed bytes and never performs client actions; the coordinator may preserve an exact copy of each external review result without changing the bytes that result reviewed
13_p0_p1_p2_standard: P0 false native-surface claim, security bypass, Package/assembly read, or unapproved client mutation; P1 missing/ambiguous pre-run review, manifest scope/hash, evidence freeze, cleanup order, after-state or final review; P2 correlation/wording defect that cannot change the gate decision
14_fail_closed_conditions: Any Gate 0-4 failure; any input identity mismatch or unresolved future input; any exact-set B04 item missing/changed or any extra manifest entry; any client mutation before PRE_RUN_APPROVE; any incomplete trace; any non-task state change; any security setting change without Owner action; any cleanup before APPROVE_FOR_TASK_CLEANUP; any exact final evidence/docs change after FINAL_APPROVE; any missing FINAL_APPROVE
15_upstream_dependency: D plan and this replacement must be formally promoted; separate Owner authorization for D01; fresh D-drive roots absent; installed-Skill/task baseline snapshot and Owner-present client; the execution formal HEAD and client identity must be resolved at Gate 0
16_downstream_handoff: D02 only if Gate 4 FINAL_APPROVE, the D01 result is independently reviewed and formally promoted by a separate Owner decision; BLOCKED returns to the named D01 owner with no contract invention or downstream repair
17_real_workbuddy_required: YES / two fresh diagnostic sessions after PRE_RUN_APPROVE
18_official_control_group: NO
19_involves_0_3_25: NO
20_proves_after_completion: The real client resource/invocation/result primitives available to a production Skill, with a bounded, independently reviewed evidence and cleanup chain
21_cannot_prove_after_completion: Shell contract/code, Package binding, official/GK run, media/video, business E2E or promotion
22_project_target: Prove the real ordinary-language WorkBuddy Skill surface before any product interface is designed
23_deviation_to_remove: Guessed Skill paths, model-written helpers, undefined B04 evidence scope, and ambiguous evidence-review-uninstall-cleanup timing
24_input_commit_tree: correction_candidate_base_formal_commit=99bc5c3d727671d7d2ea7313c6851792583efe66 / tree=b995a9a02add77f1e61769f364dd86b341137403; D01_execution_formal_commit_tree=NOT_PROVED_FUTURE_INPUT and must be resolved to the full 40-hex formal HEAD at takeover; Package commit/tree=NONE; WorkBuddy client version/binary SHA256 and B04 manifest SHA256=NOT_PROVED_FUTURE_INPUT and must be recorded at Gate 0 before any probe/client mutation or BLOCK
25_prerequisites: This replacement formally promoted; separate Owner D01 execution authorization; exact fresh D01 roots absent; installed-Skill/task baseline snapshot; Owner-present client; assigned independent zero-write Reviewer; no unresolved Gate-0 identity
26_exact_allowlist: WRITE probe_skill root + native_surface_evidence root and its named records; task-only WorkBuddy Skill/two sessions; after execution WRITE only the six authority docs; CONTROL_READ live formal Git identity and the six formal authority docs required for takeover; TASK_READ current client documentation, current WorkBuddy binary identity and only the exact B04 source root/file set below; no assembly or PackageRoot read
27_exact_denylist: ALL filesystem paths, repository files and external state not named in 26; especially every Package/PackageRoot/assembly path, Shell product code/tests, OpenMontage Registration/Locator, Provider, media, DataRoot and non-task WorkBuddy state
28_product_code_change: NO
29_workbuddy_user_action: YES / Owner performs import, safety/permission decisions, fresh task submission, session close and exact uninstall/cleanup; Worker supplies frozen probe and observes; no unattended permission choice
30_package_action: NONE / no install, replace, register, activate, locate or read of any Package/PackageRoot/assembly
31_exact_steps: Gate 0 resolve the formal execution HEAD, six formal authority docs, client version/binary SHA256 and exact B04 manifest; write inputs/B04-NEGATIVE-EVIDENCE-MANIFEST.v1.json and records/GATE-0-TAKEOVER.v1.json, record the manifest SHA256 and stop on any mismatch; Gate 1 freeze probe source/fixtures/ZIP/prompt/permission/evidence bytes and obtain independent PRE_RUN_APPROVE before import; Gate 2 Owner imports through normal safety scan and runs exactly two fresh ordinary-language sessions covering the catalog, recording all client actions; Gate 3 freezes raw trace, correlated results and pre-clean state, then the independent Reviewer returns APPROVE_FOR_TASK_CLEANUP or blocks; Gate 4 only after that token Owner uninstalls the exact task Skill, closes both sessions, removes exact task source/ZIP and captures after-state, Closeout Worker records the result and Q1-Q10, then the independent zero-write Reviewer reviews the exact final evidence/docs and returns FINAL_APPROVE or blocks; any Gate failure stops immediately, prevents the next Gate and keeps D02 unauthorized
32_positive_acceptance: Fields 10 and 12 plus a canonical B04 manifest with exactly 13 files, a Gate-0 record containing its full-byte SHA256, two correlated traces, frozen pre-clean evidence, exact cleanup evidence, exact after-state and all three actual review decisions
33_negative_assertions: Field 11 plus absence of every denylisted path/state change; no Package/Shell success claim; no review token, identity or hash may be prewritten as a result
34_failure_conditions: Field 14 or unresolved field 24; result becomes BLOCKED_WORKBUDDY_SURFACE; preserve the evidence needed to explain the block, do not enter the next Gate, and D02 remains unauthorized
35_evidence_location: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D01_native_surface_evidence\; manifest=inputs/B04-NEGATIVE-EVIDENCE-MANIFEST.v1.json; Gate-0 record=records/GATE-0-TAKEOVER.v1.json; retained evidence root is not deleted by D01 cleanup; six-doc closeout stores identities, verdict, Gate decisions and manifest SHA256 only
36_worker_reviewer_split: Surface Worker creates/runs the probe only after PRE_RUN_APPROVE and captures evidence; Owner performs client actions and cleanup; Closeout Worker edits docs and records exact copies of externally returned review decisions; the independent Reviewer writes no repository/evidence/client state, performs no client action and separately returns PRE_RUN_APPROVE, APPROVE_FOR_TASK_CLEANUP and FINAL_APPROVE decisions
37_rollback_recovery: Before Gate 1 no client mutation is permitted; after any failed Gate stop and preserve exact evidence; after Gate 3 approval restore only the pre-task installed-Skill set by uninstalling the exact task Skill, close both task sessions and verify after-state; any failed restoration blocks FINAL_APPROVE and downstream
38_temp_cleanup: Never remove probe source/ZIP or task Skill/session artifacts before APPROVE_FOR_TASK_CLEANUP; after that exact token Owner performs only exact task uninstall/close/delete and captures after-state/closeout; the retained evidence root and B04 source remain read-only retained inputs until a separately authorized project cleanup
39_git_gates: This correction candidate may be committed only after its own independent zero-write Reviewer approves the exact final six-doc diff; correction push and formal promotion are later separate decisions. For a future D01 result, candidate commit requires Gate-4 FINAL_APPROVE and exact six-doc/result checks, push requires exact commit/tree checks, formal result promotion requires separate Owner approval and ordinary fast-forward, and D02 authorization is a fourth separate decision
40_end_drift_audit: After Gate 4 actual cleanup/after-state, Closeout Worker records the ten-question EXECUTION_GATE before final review; any NO, NOT_PROVED or identity drift blocks FINAL_APPROVE except facts explicitly assigned as later-task nonclaims. The independent Reviewer then reviews the exact final evidence/docs; any change to those reviewed bytes after FINAL_APPROVE invalidates it and requires re-review before a D01 result commit
41_not_proved_after_task: All field 21 items remain NOT_PROVED unless the actual D01 evidence and all Gate decisions support the narrow primitive claim; no Package, Shell product, official/GK/video/business result is upgraded
42_no_downstream_repair: D02 may map official semantic operations only onto APPROVE client primitives; it cannot invent, patch, reinterpret or re-probe a missing primitive, and D01 does not claim OpenMontage semantics
```

### D01 B04 negative-evidence manifest（Gate 0 normative input）

The only permitted B04 read root is `D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B04_official_evidence\workbuddy-client\`. It is read-only. The manifest is written to `D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D01_native_surface_evidence\inputs\B04-NEGATIVE-EVIDENCE-MANIFEST.v1.json` before any probe import, Skill installation, task creation, session creation or other WorkBuddy/client mutation. The manifest does not authorize reading any assembly or `PackageRoot`.

The schema is exactly `B04NegativeEvidenceManifestV1`. Its only content is `schema`, exact `source_root`, and `entries`; `entries` is exactly the following 13 direct relative paths, in ascending `relative_path` order. No other file, directory, metadata or recursive discovery is allowed:

```text
B04-OWNER-PRODUCT-GOAL-RULING1.json
B04-OWNER-PRODUCT-GOAL-RULING1.md
B04-WORKBUDDY-FULL-ACCESS-ATTEMPT3-INCOMPLETE.json
B04-WORKBUDDY-FULL-ACCESS-ATTEMPT3-INCOMPLETE.md
B04-WORKBUDDY-FULL-ACCESS-ATTEMPT3-REVIEW1.json
B04-WORKBUDDY-FULL-ACCESS-ATTEMPT3-REVIEW1.md
B04-WORKBUDDY-SUCCESS-ATTEMPT1-INCOMPLETE.json
B04-WORKBUDDY-SUCCESS-ATTEMPT1-INCOMPLETE.md
B04-WORKBUDDY-SUCCESS-ATTEMPT1-REVIEW1.json
B04-WORKBUDDY-SUCCESS-ATTEMPT2-INCOMPLETE.json
B04-WORKBUDDY-SUCCESS-ATTEMPT2-INCOMPLETE.md
B04-WORKBUDDY-SUCCESS-ATTEMPT2-REVIEW1.json
B04-WORKBUDDY-SUCCESS-ATTEMPT2-REVIEW1.md
```

Each `entries` item has exactly `{relative_path,size_bytes,sha256}`: `relative_path` is one of the 13 names above using `/`, `size_bytes` is the non-negative byte length, and `sha256` is lowercase 64-hex SHA256 of the exact file bytes. The manifest itself is canonical JSON bytes encoded as UTF-8 without BOM, with `sort_keys=true`, `separators=(',',':')`, `allow_nan=false`, the 13-entry array already in the fixed relative-path order, no extra whitespace, and exactly one terminal LF. It contains no timestamp, generator, absolute per-file path, Package/assembly field, or self-hash. Compute SHA256 over the complete manifest bytes and record that value separately in `records/GATE-0-TAKEOVER.v1.json`; the manifest must not contain its own hash. Any missing, extra, renamed, newly selected, byte-drifted or rehashed-inconsistently item is `BLOCKED` before any probe/client mutation.

### D01 replacement candidate state guard

```text
replacement_status: DOCS_ONLY / CANDIDATE_NOT_FORMAL / NOT_RUN_DOCS_ONLY
correction_base: 99bc5c3d727671d7d2ea7313c6851792583efe66 / tree b995a9a02add77f1e61769f364dd86b341137403
product_code_change: 0
package_change: 0
workbuddy_change: 0
provider_or_media_change: 0
review_status: APPROVE_D01_CONTRACT_CORRECTION_FOR_CANDIDATE_COMMIT / P0=0 / P1=0 / P2=0 / INDEPENDENT_ZERO_WRITE_REVIEW1
promotion_status: NOT_REQUESTED_HERE
execution_authority: NONE
downstream: D02-D08 NOT_AUTHORIZED
```

本 replacement 修复只停留在规划/合同层；独立零写 Reviewer 必须重新检查 exact six-doc diff、Gate 0-4 时序、13 项 manifest、canonical 规则、无 PackageRoot 读取边界和三枚未来 review token。复审结论、Owner 推广决定及 D01 执行授权必须分别在实际发生后记录，不得由本节代填。

### D01 Replacement1 独立零写复审与提交前十问

独立 Reviewer 对 exact uncommitted six-doc diff 给出 `APPROVE_D01_CONTRACT_CORRECTION_FOR_CANDIDATE_COMMIT / P0=0 / P1=0 / P2=0`。Reviewer 核验了完整 01-42 字段、B04 exact 13-file manifest、canonical/no-self-hash 规则、Gate 0-4 唯一时序、Reviewer 零写边界、终审后字节变更失效规则、exact six paths、product code diff 0 与 `git diff --check`。该结论只允许形成候选 commit；不授权 push、formal promotion、D01 execution 或 D02-D08。

纠偏任务提交前 Q1-Q10：Q1 `PASS-纠偏只服务 ordinary-language WorkBuddy native surface 取证`；Q2 `PASS-WorkBuddy 仍是唯一 Agent`；Q3 `PASS-Shell/Product/Package 变更为 0`；Q4 `PASS-B04 输入固定为 13 个负面事实文件且禁止 PackageRoot/assembly`；Q5 `PASS-PRE_RUN_APPROVE 在 import 前`；Q6 `PASS-APPROVE_FOR_TASK_CLEANUP 在卸载清理前`；Q7 `PASS-result/Q1-Q10 在 FINAL_APPROVE 前且终审后变更失效`；Q8 `PASS-Reviewer 零写且客户端动作只归 Owner`；Q9 `PASS-六文档、42字段、diff check 与无产品代码效果均机械核验`；Q10 `PASS-候选不推广、不执行 D01、不授权 D02-D08`。任何一项在 commit 前失效都必须停止并重新审查 exact final diff。

## [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] V2-PROJECT-GOAL-AND-D-ROUTE-REAUDIT1 旧授权/状态快照（2026-08-24；目标/路线骨架保留）

本节保留目标与 E01→E07 路线骨架；formal base、旧授权、current task、权限、角色和 Git/status 字段均为历史快照。最新唯一 current authority 是下方 `V2-E01-ROUTE-BOUNDARY-CORRECTION1` 同名节；不得从本节恢复旧执行权。

### [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] 旧任务合同快照

| 字段 | 冻结值 |
|---|---|
| `task_id` | `V2-PROJECT-GOAL-AND-D-ROUTE-REAUDIT1` |
| `task_kind` | `READ_ONLY_FACT_AUDIT + PLANNING_DOCS_CORRECTION_ONLY` |
| `formal_base` | `b7bd6bc201f821f83d019c5b7addd8ec198d7ecf` / tree `daa4ed62e94cf9105358cb452b4950a134d7e2ef` |
| `product_goal` | `LOWER_ORDINARY_USER_THRESHOLD + GUIDED_CONTINUATION` |
| `guidance_scope` | `MISSING_ENVIRONMENT_OR_CONFIG + COMMAND_GUIDANCE + PROMPT_CONTENT_GUIDANCE + NEXT_STEP_GUIDANCE` |
| `agent_boundary` | `WORKBUDDY_ONLY_RUNNING_AGENT_AND_PRODUCTION_DECISION_OWNER` |
| `shell_boundary` | `SUPPORT_AND_GUIDANCE_LAYER / NOT_SECOND_AGENT_OR_DIRECTOR_OR_FSM` |
| `technical_surface_ruling` | `POWERSHELL_BASH_CLI_NOT_AUTOMATIC_FAILURE` |
| `D01_D08` | `UNTRUSTED_PENDING_REAUDIT / DO_NOT_CONTINUE` |
| `D01_observation` | `PRESERVE_RAW_FACTS_ONLY` |
| `D01_old_verdict` | `BLOCKED_WORKBUDDY_SURFACE_WITHDRAWN_AS_PRODUCT_CONCLUSION` |
| `D01_current_classification` | `D01_TEST_DESIGN_MISALIGNED` |
| `allowed_read` | `ORIGINAL_GOAL + FORMAL_AUTHORITY_DOCS + FORMAL_BASE_CURRENT_SKILL_SOURCE + PRESERVED_FACT_EVIDENCE + exact official cd9f3c1f AGENT_GUIDE.md` |
| `allowed_write` | `EXACT_SIX_AUTHORITY_DOCS_ONLY` |
| `forbidden` | `WORKBUDDY_PROBE + PRODUCT_CODE + PACKAGE + PROVIDER + MEDIA + D02_D08_EXECUTION` |
| `tests` | `NOT_RUN_DOCS_ONLY` |
| `commit_push_formal_delivery` | `NOT_AUTHORIZED` |
| `next` | `COMPLETE_FULL_GOAL_AND_ROUTE_REAUDIT -> INDEPENDENT_ZERO_WRITE_REVIEW -> OWNER_DECISION` |

### 立即失效的旧路由权

此前 D01 Replacement1 的 42 字段、Gate 0-Gate 4、`PRE_RUN_APPROVE`、`APPROVE_FOR_TASK_CLEANUP`、`FINAL_APPROVE` 和 `BLOCKED_WORKBUDDY_SURFACE` 结论全部只保留为历史合同/事实记录。它们不能继续驱动客户端、清理或 D02-D08，也不能作为新路线的默认前提。旧 Reviewer 的 `APPROVE` 只说明 frozen contract 内部一致，未证明该合同服务 Owner 的产品目标。

### 目标真实性第一硬闸门

每个拟议任务必须先逐项回答：

1. 它具体消除普通用户的哪一项门槛？
2. 用户是否仍只需提出自然语言业务需求并按引导继续？
3. WorkBuddy 是否仍读取 verified OpenMontage authority 并拥有生产决策？
4. Shell 是否只提供支撑和引导，且没有变成第二控制面？
5. 是否把内部路径、哈希、绑定、命令拼装或技术路由要求普通用户理解/构造/看到，或要求 WorkBuddy/model 猜测、自由合成或从用户输入推导？
6. 是否把某种未由产品目标要求的技术表面误设为成功前提？

第 1 题不能给出直接、可验收的用户价值，或第 2-6 题出现偏离，即 `STOP_MISALIGNED`，不得进入下一步。硬闸门自身也必须接受独立零写 Reviewer 的“目标吻合性”审查，不能只查字段完整性。

## [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] V2-PROJECT-GOAL-AND-D-ROUTE-REAUDIT1 审计结果与 E 路线候选快照（2026-08-24；目标/路线骨架保留）

历史快照：本节建立时是未提交、未推送、未 `FORMALLY_DELIVERED` 的 docs-only 规划；其中总路线后来形成并推送为 commit `533fb410fda837259afa29e2bb2fdee76caca599`、tree `b0b0879cd84962eb3676f9cda43b9a89cf7238b5`，但尚未 `FORMALLY_DELIVERED`。其中“当前未提交/未推送”、current task、角色与权限字段均只记录当时状态，不是 current authority。E01→E07 目标/路线骨架保留；最新唯一 current authority 是下方 `V2-E01-ROUTE-BOUNDARY-CORRECTION1` 同名节。

### 1. 核心目标重建结论

`FACT`：原始 V2 handoff 的用户问题不是“WorkBuddy 缺少一种专用原生脚本事件”，而是官方/Golden Key OpenMontage 虽可在真实 WorkBuddy 中有限运行，但普通用户仍需依赖模型临场判断与技术路径提示；目标是把它产品化为普通用户可稳定使用、无需在业务提示中写 `.venv`/Python/Pipeline/Stage/CLI 的 WorkBuddy 外壳。来源：`D:\BlazingCD\Personal\Golden_Key_OpenMontage_for_WorkBuddy\docs\workbuddy\WORKBUDDY-SHELL-V2-REFACTOR-HANDOFF-2026-08-15.md` 第 13、17-23、263-271 行。

`FACT`：Shell 的产品价值是把普通用户从 OpenMontage 内部技术中隔离出来，同时给 WorkBuddy 足够的、面向用户目标的引导，使 WorkBuddy 能读取已验证的 OpenMontage Guide 并继续原生 Pipeline。Shell 不复制 Pipeline、Stage Director、Reviewer、Checkpoint、Tool Registry、Provider/Renderer 或创意决策。

`FACT`：exact official OpenMontage `cd9f3c1f03368be87b140af494914b8ee4e3c7a4` / tree `6cd1961d552dd9d2bcfba990b80ac06edfe4b061` 的 `AGENT_GUIDE.md` 第 7-15 行把 onboarding 设为 vague request 的第一入口，第 49-86 行规定 Pipeline/manifest/Stage Skills/preflight/tool/review/checkpoint 的 Agent-first 主循环，并明确 Python 不是编排者。由这些事实可直接得出：Shell 必须把 WorkBuddy 带到 verified authority；“因此不应另造 semantic-operation API”属于本审计的架构裁决，不是 official 原文声明。

`FACT`：formal base `b7bd6bc201f821f83d019c5b7addd8ec198d7ecf` / tree `daa4ed62e94cf9105358cb452b4950a134d7e2ef` 中 `workbuddy-skill/golden-key-openmontage/SKILL.md` 第 13-31、35-71 行要求 one versioned JSON、完整 `PackageToolDefinitionV1`、installer-stamped schema/hash/argv/interpreter 和 exact environment allowlist。该文件没有 Owner 要求的普通用户环境/配置缺漏、提示词内容或下一步引导；这是 current Skill content 与 Owner 目标的直接对比结论。

`HISTORICAL_FACT`：formal TASK-REGISTER 的原 R01/Sandbox Refresh1/D01 记录及保留 raw evidence 记载了 Skill 资源读取、PowerShell/Bash 候选执行面和 physical managed path；这些记录只证明当时客户端观测，不证明产品成功。`INFERENCE`：缺少专用 native bundled-operation event 不能推出 WorkBuddy 不可用；PowerShell/Bash/CLI 也不因技术形态自动失败。

`INFERENCE`：最早需要纠正的不是 WorkBuddy surface，而是产品成功定义。此前规划把“用户能在引导下完成 OpenMontage 任务”替换成了“模型不出现 shell 命令且客户端产生一种冻结的 native event”，随后又围绕这一替代目标设计 fixed child、model-invisible semantic operations、Package-agnostic identical Skill 和 exact one-variable byte comparison。

`PROPOSAL`：正确产品路径是：

```text
ordinary user request or vague request
 -> one Golden Key WorkBuddy Skill gives plain-language capability/prompt/setup guidance
 -> existing Registration/Locator/Runtime/Launcher support hides identity/path/environment mechanics
 -> WorkBuddy reads the verified Package Guide and any Guide-routed onboarding/manifest/Stage/meta Skills
 -> WorkBuddy remains the production decision owner and uses the Package's native tools/contracts
 -> Shell reports missing prerequisites and mechanical results in actionable user language
 -> WorkBuddy guides the user through consent/configuration/recovery and presents the result
```

### 2. Phase A、B01-B04 与当前实现重裁决

| 对象 | 新裁决 | 可保留 | 必须撤销/重审 |
|---|---|---|---|
| Phase A 治理 | `PARTIAL_KEEP` | exact Git、独立 worktree、证据分层、独立零写 Reviewer、逐任务授权 | Reviewer 不能只查 frozen contract 自洽；必须先查用户目标吻合性 |
| A1/A7 目标 | `PARTIAL_KEEP` | WorkBuddy 唯一 Agent、Shell 非第二控制面、real WorkBuddy/business acceptance | 把 Shell 主要描述成确定性传输而弱化“降低门槛与引导” |
| B01 | `SUPERSEDED_PRODUCT_CONTRACT` | literal user request 与内部控制分离 | one transport/one child/完整定义成为 whole-request 成功中心 |
| B02 | `MECHANICAL_EVIDENCE_ONLY` | 输入校验、secret、进程、receipt、fail-closed 可作为内部原语参考 | model-visible technical JSON、exact host-env、whole-request fixed call 不可作为产品入口 |
| B03 | `PARTIAL_METHOD_EVIDENCE` | 装配、Registration、Locator、rollback/uninstall 方法 | 临时 Installer、Package-stamped Skill、被错误合同绑定的 final artifact |
| B04 | `NEGATIVE_FACTS_ONLY` | sandbox env、CRLF、placeholder、fallback 失败机制 | 无 Shell/OpenMontage success；不得据此发明 native event gate |
| 当前 Registration/Runtime/Launcher | `REUSE_CANDIDATE_PENDING_GAP_AUDIT` | 已有严格机械能力，不因新路线自动重写 | 只有 E02 能判定哪些真实阻碍用户路径；历史 PASS 不能代替产品价值 |
| 当前 WorkBuddy Skill/entry | `REWORK_REQUIRED` | 单一入口与用户原话边界 | 当前主体是内部合同，不是用户引导；必须回到产品入口与 verified Guide handoff |

### 3. D01-D08 逐项裁决

| 旧任务 | 裁决 | 原因 | 新去向 |
|---|---|---|---|
| D01 native surface probe | `DELETE_AS_PRODUCT_GATE` | 没有直接消除用户门槛；把专用 native event 发明成成功前提；已观测 PowerShell/资源读取不等于失败 | raw facts 保留；真实入口可靠性在 E03 离线验证与 E05 产品验收中验证 |
| D02 semantic contract freeze | `REPLACE` | WorkBuddy/OpenMontage 已拥有 Guide/Pipeline/Stage/tool 语义；Shell semantic operations 会形成第二套控制面 | E01 固化产品边界；E02 只冻结用户旅程、现有资产与最小改动 |
| D03 operation adapter | `DELETE_UNLESS_E02_PROVES_NECESSARY` | project/checkpoint/preflight/registry-tool adapter 镜像 OpenMontage 原生职责 | E03 只实现 guided entry、机械 bootstrap/locator/launcher 补缺，不实现生产语义 |
| D04 versioned Installer/lifecycle | `PARTIAL_KEEP` | 安装/升级/回滚/卸载确属 Shell 责任 | E04 只补 E02 证明缺失的产品化 Installer/assembly；不生产 adapter 或 identical-Skill 教条 |
| D05 dual fresh assembly | `REWRITE` | fresh materialization 有价值；双包同 Skill ZIP/hash 与两次 byte-identical build 不是核心目标 | E04 生成受审产品分发；official/GK 各自身份精确，但用户入口体验一致即可 |
| D06 official two-video control | `REWRITE` | official control 必要；两次完整视频、专用 surface trace 不是默认必要条件 | E05 验证一次完整普通用户路径，并专门验收缺漏配置/下一步引导 |
| D07 exact one-variable GK comparison | `REWRITE` | 同路径应指同一用户体验与 Shell 职责，不是冻结所有非 Package 字节/模型/方法 | E06 用同一用户入口、同一责任边界和同类验收方法验证 GK 0.3.25 |
| D08 business closeout | `KEEP_WITH_NARROWING` | 真实业务验收与独立 `FORMAL_DELIVERY` 闸门正确 | E07；Provider/费用仅在实际方案需要且 Owner 单独批准时进入 |

### 4. 新路线：E01-E07

#### E01 项目目标、用户旅程与路线固化

```text
01_task_id: V2-E01-GOAL-USER-JOURNEY-ROUTE-FREEZE
02_user_threshold_removed: 防止团队继续把内部技术合同当成产品目标，让所有后续工作先对准普通用户能否被引导完成任务
03_confirmed_issue: 现有 D 路线与当前 Skill 弱化用户引导，并发明 native surface/semantic adapter 等硬条件
04_correct_owner: Project Audit/Planning Worker + independent zero-write Reviewer
05_authoritative_inputs: Owner 最新目标；原始 V2 handoff；正式六文档；current Skill/source/tests；official Guide/onboarding；保留的 B/D raw evidence
06_exact_allowed_paths: WRITE 仅六份 authority docs；其他输入只读
07_concrete_actions: 重建用户问题、成功路径、责任边界；重裁决 Phase A/B/D；冻结 E 路线与全局硬闸门
08_explicitly_not_do: 不运行 WorkBuddy/probe/test，不改产品/Package/Provider/media，不 commit/push/FORMAL_DELIVERY
09_output_contract: 六文档一致的目标、裁决、路线、已证明/未证明和当前禁令
10_positive_acceptance: 每个 E 任务有明确用户门槛、用户可见结果、边界、失败条件和下一步授权
11_negative_tests: 任何任务只描述内部机制；PowerShell/CLI 自动判失败；Shell 接管 OpenMontage；Reviewer 只查字段自洽
12_independent_reviewer_checks: Owner 目标逐句追踪；原始 handoff；current Skill 事实；D01-D08 裁决；六文档 diff；零非文档改动
13_p0_p1_p2_standard: P0 恢复错误执行权或第二 Agent；P1 用户目标/任务路线/事实分层错误；P2 跨文档措辞/追踪缺陷
14_fail_closed_conditions: 目标冲突、事实不足、六文档不一致或 Reviewer 非 APPROVE
15_upstream_dependency: Owner 当前明确授权；formal base `b7bd6bc201f821f83d019c5b7addd8ec198d7ecf` / tree `daa4ed62e94cf9105358cb452b4950a134d7e2ef`
16_downstream_handoff: 仅在 E01 独立复审、Owner 授权并完成 `FORMAL_DELIVERY`、且 Owner 单独授权后进入 E02
17_real_workbuddy_required: NO
18_official_control_group: NO / read-only authority
19_involves_0_3_25: NO action / read-only authority if needed
20_proves_after_completion: 目标与路线是否可作为后续规划基线
21_cannot_prove_after_completion: 任何产品代码、安装、WorkBuddy、视频或业务效果
```

#### E02 现有用户旅程与最小改动包审计

```text
01_task_id: V2-E02-CURRENT-JOURNEY-MINIMAL-CHANGE-AUDIT
02_user_threshold_removed: 明确普通用户从安装/首次打开到提交业务需求会卡在哪里，避免凭想象重写系统
03_confirmed_issue: 现有 Registration/Runtime/Launcher 有大量机械能力，但当前 Skill 缺少用户引导；尚未证明还需哪些产品代码改动
04_correct_owner: Owner explicitly assigns Planning/Audit Coordinator; distinct Execution Worker; distinct Closeout Worker; independent zero-write Reviewer (four-way separation)
05_authoritative_inputs: E01；current source/tests/Skill；old guided Skill history；official onboarding/Guide；B04/D01 raw facts；原始安装/升级资产
06_exact_allowed_paths: READ_ONLY 源/历史输入（原始 V2 handoff、official Guide/onboarding、current Skill/source/tests、Installer/assembly 历史资产、B04/D01 raw facts 和 Git history）；唯一 E02 evidence root 为 `D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_E02_User_Journey_Minimal_Change_Audit1`；WRITE 域固定为 Planner 仅写该 root 的 `packet/`、`inputs/`，且仅在 Owner 授权后记录 `handoff/E02TakeoverV1.json`，Execution Worker 仅写 `reports/`、`evidence/`，Closeout Worker 仅写六份 authority docs，Reviewer 零写
07_concrete_actions: 画出十条旅程（安装/首次打开/环境就绪、specific request、vague request/guided entry、Package absent/unverified、environment missing、configuration/consent/optional capability、verified Guide/manifest handoff、execution error/recovery、result/receipt/video relay、safe uninstall/rollback/data preservation）；逐文件分类 KEEP/REWORK/REMOVE；冻结 E03/E04 exact change allowlist
08_explicitly_not_do: 不设计 semantic operation API，不探测 WorkBuddy，不修改代码，不把历史 PASS 当成用户旅程 PASS
09_output_contract: 用户旅程、阻断点、现有能力复用矩阵、exact minimal change packet、可见文案验收和非目标；唯一五载体为 `packet/E02ExecutionPacketV1.json`、`inputs/E02InputManifestV1.json`、`handoff/E02TakeoverV1.json`、`reports/E02ExecutionReportV1.json`、`evidence/E02EvidenceIndexV1.json`，均按 UTF-8 no BOM/LF/final LF 与 raw-byte SHA256 绑定
10_positive_acceptance: 每个拟改路径对应一个具体用户阻断；未证明需要修改的文件保持不动
11_negative_tests: 全量重写；技术 JSON 暴露；复制 onboarding/Pipeline 决策；发明新客户端 surface；无用户价值的 security gate
12_independent_reviewer_checks: 源码/测试/历史 Skill 证据；每项改动到用户阻断的双向映射；exact path allowlist；无运行动作
13_p0_p1_p2_standard: P0 第二控制面/错误权限；P1 缺旅程或无证据改动；P2 文案/映射缺陷
14_fail_closed_conditions: 任一改动无法对应用户阻断、必须先获取未知 WorkBuddy primitive、或 E03 allowlist 不精确
15_upstream_dependency: E01 正式交付对象 `NOT_PROVED_FUTURE_INPUT`；Owner 单独授权 E02；接管时解析 full 40-hex formal commit/tree 并核验远端，否则 BLOCK
16_downstream_handoff: E03/E04 只能实现 E02 证明且冻结的缺口；无 repair window
17_real_workbuddy_required: NO
18_official_control_group: NO / official Guide/onboarding read-only
19_involves_0_3_25: NO action / exact Guide/release inputs read-only
20_proves_after_completion: 现有资产哪些能直接复用，以及最小产品改动是什么
21_cannot_prove_after_completion: 改动正确性、客户端可用性、成片或业务结果
```

#### E03 最小 guided entry 与支撑层纠正

```text
01_task_id: V2-E03-MINIMAL-GUIDED-ENTRY-CORRECTION
02_user_threshold_removed: 用户无需理解 Core 路径、Python、hash/schema、命令拼装或 OpenMontage 内部路由，并在缺配置时得到可执行下一步
03_confirmed_issue: current Skill 是内部传输合同而非产品引导；E02 将给出其余最小缺口
04_correct_owner: Guided Entry Implementation Worker + independent zero-write Reviewer
05_authoritative_inputs: `FORMALLY_DELIVERED` E02 exact change packet；current formal code；official onboarding/Guide；approved UX copy contract
06_exact_allowed_paths: 仅 E02 冻结的 Skill/entry/locator/runtime/launcher/test 路径、任务证据根与六份 closeout docs；不得预扩张
07_concrete_actions: 重写一个产品入口；对 vague/specific request 给提示；机械读取 verified Package identity/Guide；把环境/配置缺漏翻译成普通语言；提供用户可执行下一步；保留用户原话；调用现有受控支撑入口；机械 relay 结果；全程 `OFFLINE_CONTRACT_ONLY`
08_explicitly_not_do: 不实现 Pipeline/Stage/Reviewer/Checkpoint/Tool Registry 语义，不写 helper/任意命令路由，不选择 Provider/Renderer/内容，不要求专用 native event
09_output_contract: 一个 guided WorkBuddy Skill 和最小支撑改动；`OFFLINE_CONTRACT_ONLY` 直到另有 `OwnerClientActionAuthorizationV1`；普通用户不被要求理解、构造或看到内部身份/路径/命令
10_positive_acceptance: 离线旅程测试覆盖首次使用、环境 ready/missing、配置 missing、具体/模糊需求、取消/失败；原始请求保持；verified Guide handoff 明确
11_negative_tests: technical JSON、绝对路径猜测、用户手拼命令、Shell 生产决策、直接 fallback 冒充成功、无下一步的报错
12_independent_reviewer_checks: exact diff；用户可见文案；Guide handoff；职责边界；project .venv 测试与 CI；无非 allowlist 改动
13_p0_p1_p2_standard: P0 任意执行/secret/第二 Agent；P1 用户仍需内部技术或 Guide 被绕过；P2 文案/追踪缺陷
14_fail_closed_conditions: 需要 E02 外新抽象、任何测试/CI 失败、或无法隐藏内部技术
15_upstream_dependency: E02 正式交付对象 `NOT_PROVED_FUTURE_INPUT`；Owner 单独授权 E03；接管时解析 full formal commit/tree、project .venv、fresh worktree/evidence root，否则 BLOCK
16_downstream_handoff: E04 只产品化已审 E03；E05 不得修代码
17_real_workbuddy_required: NO / client truth stays NOT_PROVED
18_official_control_group: NO / contract fixtures only
19_involves_0_3_25: NO writes
20_proves_after_completion: 最小 guided Shell 的离线产品合同和代码正确性
21_cannot_prove_after_completion: WorkBuddy 实际体验、安装分发、official/GK/video/business success
```

#### E04 安装、装配与生命周期产品化

```text
01_task_id: V2-E04-INSTALL-ASSEMBLY-LIFECYCLE-PRODUCTIZATION
02_user_threshold_removed: 用户无需手找仓库、Python、运行时或内部文件，并能安全安装、升级、回滚和卸载
03_confirmed_issue: V2 正式树尚无经用户旅程审计的最终 Installer/assembly；B03 仅是被旧合同绑定的临时方法证据
04_correct_owner: V2 Final-delivery Installer / Release Assembly Owner（责任主体唯一；执行职责可由其明确授权的 Worker 执行）
05_authoritative_inputs: immutable official/GK Package source owner（source 只读）；Shell-adapter owner（只负责 binding）；final assembly/Manifest/Lock owner（V2 Final-delivery Installer / Release Assembly Owner）；`FORMALLY_DELIVERED` E03；E02 reuse matrix；accepted Registration/runtime/lifecycle contracts；exact official/GK release inputs
06_exact_allowed_paths: E02/E03 冻结的 Installer/assembly/test 路径、D 盘 task roots 和六 docs；immutable official/GK Package source 只读；Shell-adapter binding 与 final assembly/Manifest/Lock 仅能在 E04 Owner 的 exact allowlist 内写；用户数据/历史对象只读保护
07_concrete_actions: 复用已验证机制，补齐版本化安装资产；生成可审查分发；安装 exact Package/Shell/runtime；验证 locator/Guide；测试 update/rollback/uninstall/data preservation；清理 task temp
08_explicitly_not_do: 不要求 official/GK Skill ZIP 字节相同，不生成 semantic adapter，不修改 Package source，不运行 WorkBuddy/Provider/media
09_output_contract: 可重复构建的 Golden Key 产品分发，以及 official control 所需的精确受控配置/装配；必须分别记录 immutable official/GK Package source owner、Shell-adapter owner 和 final assembly/Manifest/Lock owner 的边界，不在 E04 发明生产逻辑
10_positive_acceptance: clean install、missing prerequisite guidance inputs、upgrade/rollback/uninstall、DataRoot/projects/credentials preservation、D-drive placement
11_negative_tests: stale identity、generic token、路径猜测、C 盘工程缓存、用户数据删除、Package mutation、临时脚本冒充产品资产
12_independent_reviewer_checks: exact identities/diff；生命周期；恢复点；用户数据；分发内容；project .venv tests/CI；task temp cleanup
13_p0_p1_p2_standard: P0 unsafe delete/identity substitution；P1 不可安装/回滚/定位/保全；P2 包装证据缺陷
14_fail_closed_conditions: 非 exact target、数据风险、全局 Python、Package source change、测试/CI 失败或残留不清
15_upstream_dependency: E03 正式交付对象 `NOT_PROVED_FUTURE_INPUT`；Owner 单独授权 E04；接管时解析 formal commit/tree 与适用 Package/release identities；下载/写入/清理授权分别按实际动作确认
16_downstream_handoff: E05/E06 只消费 immutable reviewed release；验收期不得修复
17_real_workbuddy_required: NO
18_official_control_group: PREPARE_ONLY
19_involves_0_3_25: PREPARE_GK_RELEASE_ONLY
20_proves_after_completion: Shell 产品可以被安全分发、安装、定位、升级、回滚、卸载
21_cannot_prove_after_completion: WorkBuddy 用户体验、OpenMontage 执行、成片和业务效果
```

#### E05 official OpenMontage 用户路径 control

```text
01_task_id: V2-E05-OFFICIAL-GUIDED-USER-PATH-CONTROL
02_user_threshold_removed: 证明普通用户无需技术提示也能被 Shell 引导，从请求/环境缺漏一路进入 official OpenMontage 并得到完整本地成片
03_confirmed_issue: 当前没有纠正后 guided Shell 的真实 WorkBuddy 产品证据
04_correct_owner: Official Product Acceptance Worker + independent zero-write Reviewer
05_authoritative_inputs: E04 reviewed official control configuration；exact official Package；one frozen local fixture/brief；current WorkBuddy
06_exact_allowed_paths: 仅 fresh D-drive data/evidence roots、exact task Skill/Registration/session 和六 closeout docs；实际路径在接管前冻结
07_concrete_actions: 先验收至少一种真实缺漏/配置状态的 plain-language 指引与恢复；再用普通自然语言完成一个 official 用户 Pipeline 的本地视频；记录 Guide/manifest/Stage/tool/checkpoint/Artifact/video 与用户可见引导
08_explicitly_not_do: 不要求专用 native event；不技术提示、不修代码/Package、不 direct fallback、不强制两次视频、不调用付费 Provider
09_output_contract: 一份“引导有效 + official 完整本地视频”的真实客户端证据，或精确失败归属
10_positive_acceptance: 用户只给业务需求/作必要 consent；缺漏提示可执行；WorkBuddy 读取 verified authority；完整可播放视频；无用户手拼内部命令
11_negative_tests: 技术提示才能继续、路径猜测、Shell 生产决策、孤立 MP4/receipt 冒充完整成功、fallback、身份漂移
12_independent_reviewer_checks: literal prompts；用户操作；引导文案；client trace；Guide/Stage/tool/video lineage；身份/残留；无验收期 repair
13_p0_p1_p2_standard: P0 false product/video PASS 或第二控制面；P1 引导失败/技术负担/证据缺失；P2 trace 文案缺陷
14_fail_closed_conditions: 任何技术路由来自用户、Guide 未读、完整视频/证据缺失、需要改代码或客户端状态无法恢复
15_upstream_dependency: E04 正式交付对象、official control artifact、client identity 与 frozen input manifest 均为 `NOT_PROVED_FUTURE_INPUT`；Owner 单独授权 E05；接管时逐项解析 exact identity/before-state，否则 BLOCK
16_downstream_handoff: E06 仅在 official control APPROVE 后；失败回 E03/E04 named owner，不在 E05 修复
17_real_workbuddy_required: YES
18_official_control_group: YES
19_involves_0_3_25: NO
20_proves_after_completion: corrected Shell 对 official 的实际降门槛与完整本地视频能力
21_cannot_prove_after_completion: Golden Key 兼容、真实门店质量、付费 Provider、规模
```

#### E06 Golden Key 0.3.25 同用户路径验收

```text
01_task_id: V2-E06-GK-0_3_25-GUIDED-USER-PATH
02_user_threshold_removed: 证明目标 Golden Key 产品在同一普通用户入口和同一 Shell 职责下可用，而不要求用户理解 Package 差异
03_confirmed_issue: Golden Key 0.3.25 尚未通过纠正后的 guided WorkBuddy Shell 完整运行
04_correct_owner: Golden Key Product Acceptance Worker + independent zero-write Reviewer
05_authoritative_inputs: E05 accepted method；E04 Golden Key release；exact 0.3.25 Package；同类 frozen local fixture/brief
06_exact_allowed_paths: fresh D-drive GK data/evidence roots、exact task Skill/Registration/session、六 closeout docs；接管前冻结
07_concrete_actions: 用同一用户入口、同一职责边界、同类普通提示与同层证据运行 Golden Key；允许 Package 自己的 Guide/Pipeline/Stage 语义不同；验证引导、完整本地视频和 Package identity
08_explicitly_not_do: 不要求 Skill ZIP/model/client/全部非 Package 字节机械相同；不修改 official/GK Package；不把 Pipeline 差异当失败；不验收期 repair
09_output_contract: Golden Key guided full-video product evidence and a goal-level comparison to official
10_positive_acceptance: 用户体验/责任边界一致；WorkBuddy 按 GK authority 选择；完整可播放视频；内部 Package 差异对用户透明
11_negative_tests: 要求用户切换技术路径、Shell 选择 GK Pipeline、旧 0.3.24、fallback、Package mutation、只做 byte comparison 不看用户结果
12_independent_reviewer_checks: user-facing journey equivalence；exact GK identity；Guide/Pipeline/Stage/tool/video lineage；差异归因；无 repair
13_p0_p1_p2_standard: P0 false GK PASS/Package mutation；P1 用户路径不一致或无完整视频；P2 比较/trace 缺陷
14_fail_closed_conditions: E05 不通过、GK 身份错误、需要用户技术知识、证据/视频缺失或需要修复
15_upstream_dependency: E05 正式交付对象/evidence manifest、E04 GK artifact、client identity 与 frozen input manifest 均为 `NOT_PROVED_FUTURE_INPUT`；Owner 单独授权 E06；接管时逐项解析 exact identity/before-state，否则 BLOCK
16_downstream_handoff: E07 仅在 E06 APPROVE；失败回 named owner
17_real_workbuddy_required: YES
18_official_control_group: YES / goal-level accepted reference
19_involves_0_3_25: YES / exact target
20_proves_after_completion: Golden Key 0.3.25 通过同一 guided product path 可用
21_cannot_prove_after_completion: 真实门店业务认可、所有 Provider/renderer、规模与正式 closeout
```

#### E07 真实门店业务验收与收口候选

```text
01_task_id: V2-E07-REAL-STORE-BUSINESS-ACCEPTANCE-CLOSEOUT
02_user_threshold_removed: 证明普通用户可用真实素材和自然语言得到可接受业务成片，并能安全结束项目
03_confirmed_issue: 技术/本地 fixture 成功不能替代门店业务效果
04_correct_owner: Business Acceptance Owner + Closeout Worker + independent zero-write Reviewer
05_authoritative_inputs: E06 approved GK path；Owner-frozen素材/权利/brief/验收人；实际需要时单独 Provider/费用授权；live Git/CI
06_exact_allowed_paths: frozen business sources read-only；fresh D-drive business evidence；unchanged approved product state；六 closeout docs
07_concrete_actions: 用户提交真实业务需求；WorkBuddy/OpenMontage 作生产决策并处理实际 human/provider gates；产出竖屏业务视频；独立业务验收；冻结并审计 Git/CI/client/residue；仅在 `G8 EVIDENCE_APPROVE_FOR_CLEANUP + OwnerCleanupAuthorizationV1` 后执行 manifest-bounded `TASK_CLEANUP` 并捕获 `G9 after-state`；Closeout Worker 随后生成 exact closeout/formal-delivery/project-cleanup candidates，交 G10 审核并停止
08_explicitly_not_do: 不在验收中修 Shell/Core 媒体逻辑；不技术提示；不未经授权花费；不在 E07 执行 `FORMAL_DELIVERY`、未授权 `TASK_CLEANUP` 或任何 `PROJECT_CLEANUP`
09_output_contract: accepted/rejected business evidence、六文档 closeout candidate、exact proposed formal-delivery manifest、separate task-cleanup manifest 与 project-cleanup manifest
10_positive_acceptance: 自然语言、正确素材/画幅/音频/字幕/流程、可播放成片、独立业务接受、权限/费用/残留清楚
11_negative_tests: 横竖屏错误、fallback/孤立输出、Shell creative fix、缺权利/费用授权、伪造 PASS、混合 `FORMAL_DELIVERY`/清理
12_independent_reviewer_checks: brief/素材权利/视频语义；E06 lineage；Provider/费用 receipts；Git/CI；exact cleanup targets/non-targets
13_p0_p1_p2_standard: P0 false business PASS/未授权费用/危险删除；P1 缺视频/权利/gate/review/Git；P2 closeout trace 缺陷
14_fail_closed_conditions: E06 未通过、素材/权利/验收人未冻结、业务拒绝、需修代码、证据缺失
15_upstream_dependency: E06 正式交付对象/evidence manifest、exact GK product state、business-source/rights/brief manifest、client/provider identities 均为 `NOT_PROVED_FUTURE_INPUT`；Owner 单独授权 E07 及任何费用/Provider；named accepter；接管时逐项解析或 BLOCK
16_downstream_handoff: STOP；`FORMAL_DELIVERY` 与清理均需独立 Owner 授权
17_real_workbuddy_required: YES
18_official_control_group: CONSUME_E05_LINEAGE_ONLY
19_involves_0_3_25: YES
20_proves_after_completion: 冻结业务案例中的原始用户目标与 closeout 候选
21_cannot_prove_after_completion: 所有 Provider/格式/规模，或尚未执行的 `FORMAL_DELIVERY`/清理
```

### 5. 全路线硬闸门

每一步均按以下顺序审查，任一失败立即停止：

1. `USER_VALUE_GATE`：写出具体消除的普通用户门槛和用户可见验收；缺一即停。
2. `GOAL_TRACE_GATE`：逐条追溯 Owner 目标、原始 handoff 和 official authority；不得只引用上一份计划。
3. `NO_INVENTION_GATE`：新接口、安全限制、客户端 surface 或证据要求必须有真实事实与维护必要性；否则删除。
4. `SOLE_AGENT_GATE`：WorkBuddy 决策、OpenMontage 权威、Shell 支撑三者不得混位。
5. `MINIMAL_CHANGE_GATE`：只改已证明阻断用户旅程的最小资产；历史代码不因“可能有用”被重写。
6. `EVIDENCE_LAYER_GATE`：docs/static/unit/CI/client/video/business 各自只证明本层。
7. `INDEPENDENT_REVIEW_GATE`：Reviewer 必须先审目标吻合性，再审事实支持，最后审合同/机械一致性。
8. `OWNER_GATE`：commit、push、`FORMAL_DELIVERY`、逐任务执行、Provider/费用和最终清理均分离授权。

### 6. 当前已证明、未证明与硬停止

```text
proved: formal base identity; original goal evidence; current Skill technical-contract content; preserved WorkBuddy resource/PowerShell observations; D01 test-design misalignment; six-doc-only current diff
not_proved: E02 exact minimal change packet; corrected product code; Installer release; real guided WorkBuddy success; official/GK full video; business acceptance
superseded: D01-D08 execution contracts; BLOCKED_WORKBUDDY_SURFACE product verdict; native-event success premise; semantic-operation adapter premise; identical Skill ZIP and byte-perfect one-variable comparison as core product gates
current_authority: E01 DOCS_ONLY AUDIT/CORRECTION
forbidden_now: WorkBuddy/probe; product/test code; Package/Registration/Installer action; Provider/media; D02-D08 or E02-E07 execution; commit/push/FORMAL_DELIVERY/cleanup
next_decision: independent zero-write review of exact six-doc E01 correction candidate, then separate Owner decisions for commit, push, and FORMAL_DELIVERY
```

### 7. E01-E07 执行控制补充矩阵

本矩阵补足 21 字段之外的执行控制。未来 SHA、evidence manifest、client identity 和实际 allowlist 未产生时只能写 `NOT_PROVED_FUTURE_INPUT`；任务接管时必须解析为 exact 值并先经独立接管审查，不得用本候选伪造未来对象。

| 任务 | 产品代码 | WorkBuddy 用户动作 | Package 动作 | 证据位置 | 回滚/恢复 | 临时清理 | Git/FORMAL_DELIVERY 硬门 | 下游禁止修复 |
|---|---|---|---|---|---|---|---|---|
| E01 | NO | NO | NONE | exact six-doc diff、formal base commit/tree 与独立 Reviewer 报告 | 放弃未提交 worktree 即零产品影响 | 无产品临时物；只保留重审 worktree | zero-write APPROVE -> Owner 决定是否允许 commit；commit/push/FORMAL_DELIVERY 各自另授权 | E02 不得纠正 E01 目标错误 |
| E02 | NO | NO | READ_ONLY | six docs；只读源码/历史/official facts | 放弃 docs candidate | 删除 task-owned diff/check export；不碰历史证据 | Reviewer -> candidate commit -> push -> FORMAL_DELIVERY -> E03 authorization 全分离 | E03 不得自行扩大 allowlist/架构 |
| E03 | YES，仅 E02 exact packet | NO | READ_ONLY fixtures only | versioned tests + D-drive E03 evidence | `FORMAL_DELIVERY` 前放弃分支；完成后只能新 reviewed correction | project .venv 产生的 exact cache/build 临时物按 manifest 清理 | tests -> Reviewer -> commit -> push/CI -> FORMAL_DELIVERY -> E04 authorization | E04 不得修 E03 guided entry/代码 |
| E04 | YES，仅 Installer/assembly/lifecycle packet | NO | task-owned assemble/install/register/activate/update/rollback/uninstall | D-drive E04 build/evidence + versioned tests | CAS/activation pointer + exact task Registration 回滚；用户数据保全 | 删除 scratch build/download/cache；保留 reviewed release/evidence | tests/lifecycle -> Reviewer -> commit -> push/CI -> FORMAL_DELIVERY -> E05 authorization | E05/E06 不得修 Installer/release |
| E05 | NO | YES，Owner 处理权限/consent 与普通业务输入 | exact official control install/register/activate only | fresh D-drive official DataRoot/evidence + client trace/video | 卸载 exact task Skill/Registration、恢复 before-state；失败证据只读保留 | 只清 task session scratch；清理前独立证据审核 | evidence freeze -> independent zero-write Reviewer APPROVE -> candidate docs commit -> separate push -> separate FORMAL_DELIVERY -> separate E06 authorization | E06 不得掩盖 official 或 Shell 缺陷 |
| E06 | NO | YES，同类普通用户动作 | exact GK 0.3.25 install/register/activate only | fresh D-drive GK DataRoot/evidence + client trace/video | 恢复 before-state；不修改 E05 evidence | 只清 task scratch；保留 comparison evidence | evidence freeze -> independent zero-write Reviewer APPROVE -> candidate docs commit -> separate push -> separate FORMAL_DELIVERY -> separate E07 authorization | E07 不得修兼容/完整视频缺陷 |
| E07 | NO | YES，Owner 决定权限/human/provider/cost；client/session 动作需 `OwnerClientActionAuthorizationV1` | reuse exact approved GK product state；不替换 | fresh D-drive business evidence + six-doc closeout | 取消 exact task/恢复 session state 分别需适用 client/rollback token；不改代码 | `TASK_CLEANUP = G8 EVIDENCE_APPROVE_FOR_CLEANUP + OwnerCleanupAuthorizationV1 -> G9 after-state -> Closeout Worker exact candidates -> G10`；`PROJECT_CLEANUP` 不在 E07 内 | G10 APPROVE -> candidate commit -> separate push -> separate FORMAL_DELIVERY；之后才可另行申请 `PROJECT_CLEANUP` Owner 授权 | 业务失败回 named E03-E06 owner 的新授权任务 |

所有 future task 在接管前只冻结与该任务动作实际相关的身份：每项都需要 full 40-hex formal commit/tree、fresh root/before-state、exact read/write allowlist 和 protected non-targets；只有读取或操作 Package 的 E04-E07 才需要对应 external Package/release identity；只有运行 WorkBuddy 的 E05-E07 才需要 client version/binary identity；只有消费既有 evidence/input 的任务才需要其 manifest SHA256。E01/E02 的 Package/client action 为 `NONE_NOT_APPLICABLE`，不得为了字段完整而虚构身份。任何“适用但 unresolved”的值都阻断执行。

### 8. 原始 8 阶段与 11 步骤的新映射

| 原始对象 | E 路线覆盖 | 验收证据 | 裁决 |
|---|---|---|---|
| Stage 1 冻结边界 | E01-E02 | Owner goal trace、用户旅程、minimal packet、Reviewer | 保留但改为 user-value-first |
| Stage 2 Registration | E02、E04 | reuse audit、install/register/locate/lifecycle | 保留；不因旧 PASS 自动免审 |
| Stage 3 Launcher | E02-E03 | minimal-gap map、guided bootstrap/support tests | 保留机械职责；whole-request child 废止 |
| Stage 4 WorkBuddy Skill | E02-E03、E05 | guided Skill 文案/测试/真实 client | 重写；semantic adapter/native event gate 废止 |
| Stage 5 progressive Runtime | E02-E06 | missing-env guidance、runtime/lifecycle、real client | 保留按需准备/逐项 consent |
| Stage 6 reduce CLI/MCP | E02-E03、E05 | 无任意路由/第二控制面；真实用户不需拼命令 | CLI/PowerShell 可作内部表面；不以名称判失败 |
| Stage 7 Installer/upgrade/migration | E04 | versioned release + update/rollback/uninstall/data preservation | 保留 |
| Stage 8 layered acceptance | E05-E07 | official guided video、GK guided video、business acceptance | 保留并以用户结果为中心 |
| Step 1 architecture | E01-E02 | target/journey/reuse packet | 重做 |
| Step 2 Registration | E02/E04 | exact product lifecycle | 保留/复核 |
| Step 3 Launcher binding | E02/E03 | minimal internal support | 去除 whole-request 教条 |
| Step 4 production Skill | E02/E03/E05 | guided entry + real client | 完整重写 |
| Step 5 Runtime | E02-E06 | plain-language gaps/consent/readiness | 保留 |
| Step 6 Installer/lifecycle | E04 | versioned Installer and recovery | 保留 |
| Step 7 offline/security/fault | E03-E04 | project .venv tests/CI/fault cases | 只验证真实产品合同 |
| Step 8 first real WorkBuddy | E05 | official complete guided path | 不再做 native probe |
| Step 9 corrected Core | E06 | GK 0.3.25 complete guided path | 保留 |
| Step 10 store acceptance | E07 | portrait business acceptance | 保留 |
| Step 11 optional fork/MCP/more entries | post-E07 separate decision | future independent evidence | 不进入当前主链 |

### 9. T1-T12 与 R01-R08 新映射

| 对象 | E 路线覆盖 | 证据/边界 |
|---|---|---|
| T1 entry | E02-E03/E05 | one guided Skill + real WorkBuddy；不要求 native event |
| T2 input | E02-E03 | business request 与 hidden mechanics 分离；不要求 technical JSON |
| T3 validation order | E03-E06 | verified Registration/Locator/Guide before production |
| T4 adapter | E02-E03 | only minimal mechanical bootstrap/relay if evidence requires；不镜像 OpenMontage semantics |
| T5 auth/continuation | E03/E05-E07 | WorkBuddy/Owner consent；Shell 只报告状态 |
| T6 result mapping | E03/E05-E06 | actionable status + OpenMontage Artifact/video lineage |
| T7 privacy | E03-E07 | secret redaction/least forwarding；不要求 host env exact-set equality |
| T8 failures | all E | plain-language next step + fail current task；无下游 repair |
| T9 Package gate | E04 | exact release/install/register/locate/lifecycle |
| T10 evidence layers | all E | docs/code/CI/client/video/business 分层 |
| T11 Stage 6 relay | E02-E03/E05 | 优先复用现有 status/result relay；新增代码必须有真实缺口 |
| T12 implementation packet | E02-E04 | exact minimal paths、tests、CI、release |
| R01 WorkBuddy surface | E02 existing-fact audit + E05 real product proof | 删除独立 native-surface product gate |
| R02 binding | E02-E04 | internal Locator/Installer binding；普通用户不被要求理解/构造/看到，WorkBuddy/model 不猜测或自由合成；由 verified Package/Shell 提供 exact mechanical operation |
| R03 Skill bundle | E03-E04 | guided product entry；不要求跨 Package ZIP identical |
| R04 Installer lifecycle | E04 | versioned install/update/rollback/uninstall |
| R05 materialization | E04 | reviewed product/control artifacts |
| R06 Skill install | E04-E06 | exact install/hit；安装本身不等产品 PASS |
| R07 real WorkBuddy | E05-E07 | official/GK/business layered sessions |
| R08 closeout | E07 + later separate actions | closeout candidate -> FORMAL_DELIVERY -> PROJECT_CLEANUP 三闸门 |

### 10. 原 23 项交付物新映射

| # | 交付物 | E 路线位置 |
|---|---|---|
| 1 | 接管核验 | E01 header/Git state |
| 2 | 分支/worktree 身份 | E01 state + final handoff |
| 3 | 一页核心目标 | E01 section 1 |
| 4 | 成功路径 | E01 section 1 product path |
| 5 | 完整追踪矩阵 | sections 8-10 |
| 6 | Stage 1-5 审查 | E01 section 2 + section 8 |
| 7 | Stage 6 交接 | T11 mapping + E02/E03/E05 |
| 8 | 可保留资产 | E01 section 2 + E02 deliverable |
| 9 | 缩小/重做/删除/归属 | E01 D matrix + E02 packet |
| 10 | PackageToolDefinitionV1 | E02 判为 internal primitive candidate；不再是 model-facing product contract |
| 11 | launch_session_tool | E02 复用审计；不得自动成为 whole-request contract |
| 12 | workbuddy_entry_cli/Skill | E02-E03 guided rework |
| 13 | R02 归因 | internal Shell/Installer binding in E02-E04 |
| 14 | 遗留 Stage2 分支 | protected historical object；另授权 hardening |
| 15 | dirty worktrees | protected non-targets；不 copy/delete |
| 16 | official -> same user path -> GK | E05 -> E06 |
| 17 | 最小目标架构 | E01 product path |
| 18 | 最小任务清单 | E01-E07 |
| 19 | 每任务边界/验收/Reviewer | section 4 21 fields + section 7 controls |
| 20 | DoD/下游条件 | each field 9-16 + control matrix |
| 21 | Owner 决策 | per-task/commit/push/FORMAL_DELIVERY/provider/cleanup gates |
| 22 | 文档白名单 | E01 exact six docs；future exact by E02 |
| 23 | 是否可固化 | E01 independent review + separate Owner decisions |

### 11. E01 提交前十问防偏记录

1. `PASS`：当前工作直接纠正“降低普通用户门槛与提供引导”的产品目标。
2. `PASS`：WorkBuddy 仍是唯一 Agent/生产决策者；OpenMontage Guide/Pipeline/Stage 为生产权威。
3. `PASS`：Shell 仅保留支撑与引导；semantic-operation adapter 被删除为默认方案。
4. `PASS`：native event、identical Skill ZIP、byte-perfect one-variable 等未经目标证明的限制已撤销。
5. `PASS`：official -> Golden Key 保持同一用户入口、Shell 职责和验收层级，不伪装成所有字节相同。
6. `PASS`：fallback、receipt、孤立 MP4、静态/单元证据不能冒充完整产品成功。
7. `PASS`：当前 diff 严格六文档；无客户端/产品/Package/Provider/media。
8. `PASS`：8 阶段、11 步骤、T1-T12、R01-R08、23 项已重新映射。
9. `PASS`：FACT/INFERENCE/PROPOSAL/NOT_PROVED 分离；future identities 不预写。
10. `PASS`：每步失败回当前/named owner；后续任务不是 repair window。

以上 PASS 是编写者提交前自审，不是独立 Reviewer 结论；Reviewer 必须重新逐题验证，任何 P0/P1 或目标吻合性失败即 REJECT。

## [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] V2-E01-EXECUTION-PACKETS-PLANNING-CORRECTION1 候选（2026-08-25）

本节保留首次执行包规划事实；“当前规划/审计对话”不再产生角色权限。最新 E01 纠正要求 Owner 显式指派 `Planning/Audit Coordinator` 并使用可审计 handoff；本节仍不授权 E02-E07 执行。

```text
task_id: V2-E01-EXECUTION-PACKETS-PLANNING-CORRECTION1
candidate_base: 533fb410fda837259afa29e2bb2fdee76caca599 / tree b0b0879cd84962eb3676f9cda43b9a89cf7238b5
candidate_branch: refs/heads/codex/v2-goal-and-route-reaudit1
candidate_remote_state: PRESENT_AT_533fb410fda837259afa29e2bb2fdee76caca599
formal_ref_at_takeover: refs/heads/codex/workbuddy-shell-v2 / b7bd6bc201f821f83d019c5b7addd8ec198d7ecf / tree daa4ed62e94cf9105358cb452b4950a134d7e2ef
formal_delivery: NOT_DONE
task_kind: DOCS_ONLY / PLANNING_EXECUTION_REVIEW_CONTRACT_CORRECTION
allowed_write: EXACT_SIX_AUTHORITY_DOCS_ONLY
forbidden: WORKBUDDY + PROBE + PRODUCT_OR_TEST_CODE + PACKAGE_REGISTRATION_INSTALLER_ACTION + PROVIDER + MEDIA + E02_E07_EXECUTION + COMMIT + PUSH + FORMAL_DELIVERY + CLEANUP
tests: NOT_RUN_DOCS_ONLY
current_product_execution: PAUSED
current_planning_work: E01_EXECUTION_PACKETS_CANDIDATE
E02_E07: NOT_AUTHORIZED
review_required: INDEPENDENT_ZERO_WRITE / GOAL_FIRST / FACTS_SECOND / MECHANICS_THIRD
delivery_gates: REVIEW_APPROVE -> OWNER_COMMIT_AUTHORIZATION -> CANDIDATE_COMMIT -> OWNER_PUSH_AUTHORIZATION -> CANDIDATE_PUSH -> OWNER_FORMAL_DELIVERY_AUTHORIZATION -> ORDINARY_FAST_FORWARD_FORMAL_REF -> REMOTE_COMMIT_TREE_VERIFICATION -> CI_HEADSHA_SUCCESS_IF_REQUIRED -> FORMALLY_DELIVERED -> OWNER_NEXT_TASK_AUTHORIZATION_SEPARATE
first_execution_gate: FORMAL_REF_CONTAINS_REVIEWED_PLAN + SEPARATE_OWNER_E02_AUTHORIZATION
```

### 12. 固定职责分离

| 角色 | 必须做 | 禁止做 | 产出 |
|---|---|---|---|
| `Planning/Audit Coordinator`（Owner 显式指派） | 读取最新正式 authority 和上一步正式结果；逐条重验用户目标；产生一个任务的完整执行包；解析适用身份；冻结 allowlist、Gate、验收、回滚和证据合同；执行后审计偏离并规划下一步 | 不在未授权时执行产品动作；不把未来事实写成 PASS；不因执行便利扩大目标；不得因聊天标题或历史自动继承 | `E0xExecutionPacketV1`、目标追踪、授权申请、结果审计、下一任务候选 |
| `Execution Worker`（新执行对话） | 只读完成接管核验；逐条执行已批准执行包；保存原始事实；Gate 失败立即停止并回报 | 不重新规划；不增加路径/命令/测试/客户端动作；不现场 repair；不把自己的说明当证据 | takeover record、原始执行证据、deviation/stop report、候选结果 |
| `Closeout Worker` | 只在原始证据已冻结且 Reviewer 已给出结果/清理判定后，把事实写入六份权威文档候选 | 不运行产品动作、不重解释证据、不修产品、不兼任本任务 Reviewer | 六文档 exact closeout diff、十问、Git/CI 候选清单 |
| `Independent zero-write Reviewer` | 与 Planner/Worker 不同；先审目标吻合，再审事实来源，最后审机械合同；对 exact packet、exact evidence、exact diff 分阶段复审 | 不写工作树、不修复 finding、不把字段完整等同产品正确 | `PLAN_APPROVE/REJECT`、`PRE_EXECUTION_APPROVE/REJECT`、`EVIDENCE_APPROVE_FOR_CLEANUP/REJECT`、`FINAL_RESULT_APPROVE/REJECT` |
| `Owner` | 分别决定规划固化、push、`FORMAL_DELIVERY`、单任务执行、Package/client/Provider/费用、rollback、cleanup 和下一任务 | 一次授权不自动覆盖后续 Gate；业务 consent 不等于 Git/清理授权 | 明确、范围有限且绑定 task/packet/动作的授权或拒绝 |
| `Business Accepter`（仅 E07） | 按冻结 brief 验收业务结果 | 不以工程测试代替业务判断，不在验收中指导修代码 | accepted/rejected business verdict |

Planner 可以在执行前根据已正式交付的上游事实完成下一份执行包，但不得提前冻结尚不存在的 SHA、manifest、client before-state 或实际路径。执行窗口若发现 packet 与现场冲突，只能输出 `STOP_PACKET_MISMATCH`；修正权回到 Planner，且修正后的 packet 必须重新独立复审。

E02 即使是 docs-only，也必须由 Planner/Audit Coordinator、Execution Worker、Closeout Worker、Independent Reviewer 四个不同主体分工：Planner 只写 `packet/`、`inputs/`，并且只能在 Owner 授权后记录 `handoff/E02TakeoverV1.json`；Execution Worker 只在唯一 evidence root 写 `reports/`、`evidence/` 并停止；Closeout Worker 才能依据冻结报告写六文档；Reviewer 与前三者均不同且永远零写。E03-E07 同样保持 Worker 与 Closeout Worker 分离。任何 E01 当前候选都不运行 WorkBuddy UI、Package、Provider 或媒体。

### 13. 每个 E 任务共同的十三道 Gate

| Gate | 通过条件 | 失败状态与动作 |
|---|---|---|
| `G0 FORMAL_AUTHORITY` | live formal commit/tree、当前 TASK-REGISTER、任务授权完全一致 | `STOP_AUTHORITY_MISMATCH`；零写停止 |
| `G1 USER_VALUE` | 明确一个普通用户门槛、可见改进和本任务可证明层级 | `STOP_MISALIGNED`；返回 Planner |
| `G2 INPUT_IDENTITY` | 只解析本任务适用的源、Package、client、fixture、manifest、before-state；未来项不得占位冒充 | `BLOCKED_INPUT_NOT_PROVED` |
| `G3 EXACT_PACKET` | `E0xExecutionPacketV1` 的读写路径、protected non-targets、步骤、测试、证据、回滚、清理、授权全部闭合 | `STOP_PACKET_INCOMPLETE` |
| `G4 PRE_EXECUTION_REVIEW` | 独立 Reviewer 返回 `PRE_EXECUTION_APPROVE`，P0/P1/P2 均为 0 | `REJECT`；不得执行或准备副作用 |
| `G4A OWNER_TASK_EXECUTION_AUTHORIZATION` | Owner 对 exact task、packet SHA256、formal commit/tree、允许动作/路径、有效范围和禁止动作签发单任务执行 token；适用的 Package、client、Provider/费用、rollback、cleanup 仍各需独立 token | 缺失、过期、对象/动作不符即 `STOP_NOT_AUTHORIZED` |
| `G5 BOUNDED_EXECUTION` | Worker 只按 packet 操作；每个动作记录最终 exit/可见结果；无临场修复 | 首个偏差即 `STOP_EXECUTION_DEVIATION` |
| `G6 EVIDENCE_FREEZE` | 原始证据、hash、manifest、Git/client/Package 状态和已证明/未证明分层冻结 | `INCOMPLETE_EVIDENCE`；不得清理或下游 |
| `G7 RESULT_REVIEW` | Reviewer 对目标、事实、结果和 exact diff 返回结果判定 | 非 APPROVE 保持当前任务失败/不完整 |
| `G8 CLEANUP_REVIEW` | 只有存在 task-owned 临时状态时，Reviewer 核验 exact targets/non-targets 并返回 `EVIDENCE_APPROVE_FOR_CLEANUP` | 无 token 不卸载、不删除、不关闭需保全会话 |
| `G9 CLEANUP_AFTER_STATE` | 仅清 packet 中已批准对象；捕获 after-state；用户数据和历史证据保持 | 任一目标漂移立即停止清理 |
| `G10 FINAL_CLOSEOUT_REVIEW` | 独立 Reviewer 核验执行、保全、清理、after-state、十问和六文档候选 | 非 `FINAL_RESULT_APPROVE` 不 commit |
| `G11 GIT_AND_NEXT` | Reviewer 先审 unstaged exact diff；本轮 Owner 条件授权仅允许审核通过后 candidate commit + 专用分支 push；commit 后须由零写核验 exact commit/tree 与已审字节一致并给出 post-commit binding `APPROVE`；`FORMAL_DELIVERY` 与 E02 仍不授权 | 任一未授权、post-commit binding 缺失或对象不符即停止 |

`G4` 通过不授权执行；只有 `G4A` 的 `OwnerTaskExecutionAuthorizationV1` 才授权 packet 中的基础动作。Package/install/register/activate 使用 `OwnerPackageActionAuthorizationV1`，WorkBuddy/client 使用 `OwnerClientActionAuthorizationV1`，Provider/费用使用 `OwnerProviderCostAuthorizationV1`，rollback 使用 `OwnerRollbackAuthorizationV1`，cleanup 使用 `OwnerCleanupAuthorizationV1`；这些 token 不能互相替代。`G7` 通过不授权 cleanup、commit/push/formal delivery；FORMALLY_DELIVERED 不授权下一任务。E02/E03 若无产品临时状态，`G8-G9` 只能以 `NOT_APPLICABLE_WITH_EVIDENCE` 关闭，不能借此删除历史材料。

```text
OwnerTaskExecutionAuthorizationV1:
  task_id
  owner_identity
  record_id
  issued_at
  expires_at
  packet_sha256
  carrier_path
  carrier_sha256
  formal_commit
  formal_tree
  allowed_actions
  allowed_paths
  effective_scope_or_expiry
  forbidden_actions
  optional_action_tokens_required
```

### 14. `E0xExecutionPacketV1` 必填字段

每一步执行前由 Planner 写全以下字段，并由 Reviewer 零写审核：

```text
packet_version
task_id
ordinary_user_barrier
user_visible_acceptance
formal_commit_and_tree
upstream_result_commit_tree_and_evidence_manifest
applicable_external_identities
read_allowlist
write_allowlist
protected_non_targets
fresh_worktree_and_task_roots
before_state
ordered_actions
forbidden_actions
positive_acceptance
negative_and_fault_cases
evidence_schema_and_locations
rollback_or_restore
cleanup_targets_and_non_targets
required_owner_authorizations
review_stages_and_tokens
stop_conditions
cannot_prove
downstream_handoff
```

任何适用字段为 unknown/unresolved 时，packet 状态只能是 `DRAFT_BLOCKED`。不适用字段必须说明 `NOT_APPLICABLE` 的事实理由，不得填假值凑齐。

每个 packet 还必须使用 canonical UTF-8 无 BOM manifest 或等价的仓库内闭合表格记录所有适用身份，并在 takeover record 中保存完整字节 SHA256。规划阶段只能冻结 schema；值尚未产生时写 `NOT_PROVED_FUTURE_INPUT / BLOCKS_EXECUTION`。

| 任务 | 必须生成或解析的身份载体 |
|---|---|
| E02 | `E02MinimalChangePacketV1`：十条 journey、固定 packet/input/takeover/report/evidence carrier 路径与写入域、path/symbol `KEEP/REWORK/REMOVE/NO_CHANGE`、双向用户阻断映射、E03/E04 allowlist/denylist、文案场景、测试/CI、rollback、evidence、cannot-prove；`packet_sha256`、`carrier_path`、`carrier_sha256` |
| E03 | `FORMALLY_DELIVERED` E02 packet SHA256；`UXCopyContractV1` 批准者/版本/SHA256；exact source/test/CI paths；project `.venv` identity；failed-candidate preservation manifest |
| E04 | official/GK source commit/tree；Python/FFmpeg/ffprobe/Node22+/npm/npx identities；Release Manifest/Lock；source/version/size/license/SHA256；install/update/interrupted-update/rollback/uninstall manifests |
| E05 | WorkBuddy version/binary SHA256；Skill/Registration identity；ordinary prompts；missing-state scenario；fixture/brief manifest SHA256；model/mode；fresh-session count；before-state；client/video/Artifact/Checkpoint/Reviewer correlation evidence manifest |
| E06 | exact GK 0.3.25 identity；E05 method/evidence SHA256；same-user-path comparison manifest，明确 same/allowed-different/fail differences；fresh E06 evidence，禁止复用 E05 运行证据 |
| E07 | business brief/source/rights/acceptance manifest；named accepter；Provider/cost manifest when applicable；closeout manifest；proposed formal-delivery manifest；proposed cleanup manifest |

统一结果枚举为：`APPROVE` 只用于本层完整通过；`REJECT` 表示事实存在且不满足合同；`INCOMPLETE` 表示所需证据未完整取得；`BLOCKED_EXTERNAL` 表示已证明的外部条件阻断；`NOT_PROVED` 表示不能作出事实结论。任何非 `APPROVE` 都不得启动下游。

### 15. E02 具体规划、执行与审核方案

#### 15.1 Planner 执行前产出

E02 是首个可在 E 路线 `FORMALLY_DELIVERED` 后规划并单独授权的任务。Owner 必须显式指派 `Planning/Audit Coordinator`，不能由对话标题、历史或“当前规划对话”自动继承权限。该 Coordinator 必须从届时 live formal HEAD 建 E02 专用 docs-only worktree，冻结六文档写 allowlist 和唯一 D 盘证据根，并冻结只读输入清单：原始 V2 handoff、official Guide/onboarding、当前 WorkBuddy Skill、Registration/Locator/Runtime/Launcher/relay 源码与测试、Installer/assembly 历史资产、旧 guided Skill 历史、B04/D01 raw facts。不得扫描未知目录；每一项输入写 exact repo/path/commit 或 `MISSING`。

#### 15.2 Worker 与 Closeout Worker 有序动作

1. 核验 live formal 已包含 E 路线正式规划对象，且只有 E02 被授权。
2. 对十条用户旅程分别建立事实表：`install-first-open-environment-ready`、`specific request`、`vague request-guided entry`、`Package absent/unverified`、`environment missing`、`configuration/consent/optional capability`、`verified Guide/manifest handoff`、`execution error/recovery`、`result/receipt/video relay`、`safe uninstall/rollback/data preservation`。数量、编号和目录必须在 packet、报告、证据索引及六文档中一致。
3. 每条旅程逐步记录：用户输入、WorkBuddy 应提供的可见引导、verified authority handoff、现有代码/文档行为、已证明阻断、证据来源、未证明事项。
4. 对现有资产逐路径/必要时逐 symbol 分类 `KEEP / REWORK / REMOVE / NO_CHANGE / NOT_PROVED`，每个 `REWORK/REMOVE` 必须反向绑定一个用户阻断；每个阻断必须正向绑定拟改路径或明确无需代码。
5. 形成 E03 exact minimal change packet：允许的 Skill/entry/support/test 路径、所需用户文案场景、禁止新增的语义控制面、离线验收。
6. 形成 E04 exact Installer/lifecycle packet：允许路径、复用资产、构建/安装/升级/回滚/卸载/数据保全缺口；未证明需要修改的路径排除。
7. 写出 `NO_CODE_CHANGE_REQUIRED` 候选也必须有证据，不能为了让 E03/E04 存在而制造改动。
8. Planning/Audit Coordinator 只能写 `packet/`、`inputs/`，并且只能在 Owner 授权后记录 `handoff/E02TakeoverV1.json`；Execution Worker 只能在固定 E02 evidence root 写 `reports/`、`evidence/`，不能写仓库；独立 Reviewer 先核验报告/索引未越界，再由不同的 Closeout Worker 只按 packet 更新六文档一致镜像并执行 `git diff --check`，不能改 evidence。任何主体都不得运行 pytest、WorkBuddy 或产品副作用。

#### 15.3 E02 独立审核

Reviewer 必须抽查每条旅程的原始输入、双向追踪、每个 allowlisted path 的证据、每个 protected non-target、FACT/INFERENCE/PROPOSAL 分层，以及 E03/E04 是否仍只是未来未授权 packet。以下任一成立即 P1/P0 REJECT：凭旧 PASS 跳过用户旅程、把 internal CLI/native event 当产品 Gate、复制 OpenMontage 生产语义、无证据扩大改动、无唯一 evidence carrier、把读审计变成客户端/Package 动作。

#### 15.4 E02 完成边界

E02 只证明“最小应改什么/不应改什么”。它不证明实现正确、Installer 可用、WorkBuddy 可用或视频成功。结果经 `FINAL_RESULT_APPROVE` 后也只能申请 docs candidate commit；push、`FORMAL_DELIVERY` 和 E03 授权继续分离。

### 16. E03 具体规划、执行与审核方案

#### 16.1 Planner 接管条件

只有 E02 正式结果存在并给出 exact allowlist 后，Owner 显式指派的 `Planning/Audit Coordinator` 才能解析 E03 packet。E03 packet 初始状态固定为 `OFFLINE_CONTRACT_ONLY`；在另有绑定当前 task/action 的 `OwnerClientActionAuthorizationV1` 前，不得执行任何 WorkBuddy/client 动作。packet 必须冻结项目 `.venv`、fresh worktree/evidence root、exact source/test paths、用户文案场景、现有可复用入口以及所有 protected non-targets。E02 未证明的抽象不得进入 E03。

#### 16.2 Worker 有序动作

1. 先以版本化测试固定普通用户场景：模糊/具体需求、ready/missing environment、missing configuration、取消、可恢复失败、verified Guide handoff、结果 relay。
2. 仅修改 E02 允许的一个 guided Skill/entry 和最小机械支撑；用户业务原话与内部 controls 保持分离。
3. 环境/配置/提示词/下一步必须使用普通语言；普通用户不得被要求理解、构造或看到内部 hash、path、schema、JSON、env、argv、transport；WorkBuddy/model 不得猜测、自由合成或从用户输入推导这些内部值；WorkBuddy/固定 Skill 可接收并调用由 verified Package/Shell 提供、identity-checked、allowlisted 的 exact mechanical operation。该调用不授予 Shell 生产决策权。
4. 只调用既有 Registration/Locator/Runtime/Launcher/relay 中被 E02 证明可复用的能力；如现有能力不足，停止回 Planner，不在 E03 新造语义 adapter。
5. 使用项目 `.venv` 运行 packet 指定的 direct、fault、hygiene 和 full tests；保留未截断输出、最终 exit、Git diff 和 residue manifest。
6. 冻结证据后停止；E03 保持 `OFFLINE_CONTRACT_ONLY`，在 `OwnerClientActionAuthorizationV1` 前不得运行 WorkBuddy/client；同时不得执行 Package 安装、Provider 或媒体。

#### 16.3 E03 审核与失败归属

Reviewer 对 exact diff、用户文案、双向旅程映射、Guide handoff、secret/controls 边界、测试/CI 和非 allowlist 0 修改进行复审。任何需要 E02 外路径、新控制面、测试失败或用户仍需内部技术均为 REJECT。失败回 E02/E03 Planner 形成新授权 correction，不得由 E04 修复。

### 17. E04 具体规划、执行与审核方案

#### 17.1 Planner 接管条件

只有 E03 正式结果和 E02 Installer packet 均存在时，Owner 显式指派的 `Planning/Audit Coordinator` 才能冻结 E04。E04 owner 固定为 `V2 Final-delivery Installer / Release Assembly Owner`；packet 必须解析 exact formal code、official/GK release identities、构建输入、D 盘 build/install/evidence roots、Registration/DataRoot before-state、用户数据保护范围、下载来源/大小/许可/镜像、写入/回滚/清理的分别授权。项目 Python 只用项目 `.venv`。

#### 17.2 Worker 有序动作

1. 捕获所有 target/non-target before-state，验证目标均为 packet 中的绝对 D 盘路径。
2. 复用 E02/E03 批准机制构建版本化分发；不得用临时脚本、手工拷贝或全局包冒充产品资产。
3. 在隔离 root 验证 clean install、Registration/Locator/Guide、private toolchain 和缺漏提示输入。
4. 依次验证 upgrade、interrupted-update recovery、rollback、uninstall 和 reinstall；每次验证 identity、activation pointer、DataRoot/projects/credentials preservation。
5. 生成 immutable official control artifact 与 Golden Key 0.3.25 artifact；精确记录各自身份，但不要求跨 Package Skill/model/全部字节相同。
6. 运行 packet 指定的项目 `.venv` 测试和 CI 候选；冻结 build/install/lifecycle/Git 证据。
7. `G8` 前不删除 build/install evidence；只有 Reviewer 返回 `EVIDENCE_APPROVE_FOR_CLEANUP` 且 Owner 另行签发绑定 exact scratch/download/cache targets 的 `OwnerCleanupAuthorizationV1` 后，才清这些临时物；保留 reviewed release 和证据。

#### 17.3 E04 审核与失败归属

Reviewer 必须核验可复现构建、exact identities、D 盘放置、生命周期、回滚点、数据保全、清理边界、Package source 0 修改和无 WorkBuddy/Provider/media。unsafe delete、身份替换或数据风险为 P0；无法安装/定位/升级/回滚/卸载为 P1。失败回 E04 correction，不得进入 E05 验收期修复。

### 18. E05 具体规划、执行与审核方案

#### 18.1 Planner 接管条件

Planner 必须从 E04 正式 official control artifact 解析 exact Package/Shell/Skill/Installer/Registration identities，冻结 current WorkBuddy binary/version、fresh D-drive DataRoot/evidence root、before-state、一个可恢复的真实缺漏/配置场景、一份本地且无需付费 Provider 的 fixture/brief、两条普通用户提示、允许的 Owner consent 和恢复方案。任何客户端或输入事实未解析，packet 为 `DRAFT_BLOCKED`。

#### 18.2 Worker 有序动作

1. `G4 PRE_EXECUTION_APPROVE` 通过后仍不得安装/注册/激活；只有再取得 `G4A OwnerTaskExecutionAuthorizationV1`、`OwnerPackageActionAuthorizationV1` 和 `OwnerClientActionAuthorizationV1` 三个绑定当前 task/packet/exact action 的独立 token，才允许安装/注册/激活 exact official control 和 exact Skill。
2. 先以普通用户操作触发冻结的缺漏/配置场景；Shell 可基于 verified mechanical state 返回 bounded/deterministic 的环境、配置、command、prompt、next-step remediation facts/options/material；Shell 不理解业务意图、不发起 consent、不选择 recovery、不推进生产；WorkBuddy 负责面向用户解释/呈现、取得 consent、选择 recovery/continue 并决定是否继续。
3. 建立 fresh session，用户只提交冻结的自然语言业务需求和必要 consent；不得提供 Python、路径、hash、Pipeline、Stage 或内部命令提示。
4. 记录 WorkBuddy 读取 verified Guide/manifest/Stage authority、作出生产决策、调用 native Package tools、通过 checkpoint/review 并产生完整本地视频的可独立审查证据。
5. 完整视频必须由真实 WorkBuddy、verified authority 和真实工具执行产生；不得是 fixture/mock/demo/fallback，必须是可播放、非零时长的竖屏视频，音视频 lineage 与 receipt 可审，且无手工绕行。完整视频、Artifact lineage、用户可见引导、client trace、Package identity 任一缺失，结果为 `INCOMPLETE/FAIL`；失败不得冒充成功，receipt、孤立 MP4 或 fallback 不得替代。
6. 不在会话中改代码、Package、Skill 或提示技术旁路；发现缺陷立即停止并归属 E03/E04。
7. 冻结证据并取得 `G8 EVIDENCE_APPROVE_FOR_CLEANUP` 后仍不得执行恢复或清理。卸载 exact task Skill/Registration 需绑定该动作的 `OwnerPackageActionAuthorizationV1`；关闭 task session 需 `OwnerClientActionAuthorizationV1`；恢复 before-state 需 `OwnerRollbackAuthorizationV1`；删除 task scratch 需 `OwnerCleanupAuthorizationV1`。四类 token 互不替代，失败证据保持只读。

#### 18.3 E05 审核

Reviewer 分三次：运行前审核 exact inputs/prompts/permissions/evidence plan；证据冻结后判定 user journey、Guide/tool/video lineage 和是否允许清理；after-state 后做最终结果审查。成功只证明 official control 的 guided product path，不证明 Golden Key 或门店业务。

### 19. E06 具体规划、执行与审核方案

#### 19.1 Planner 接管条件

只有 E05 正式 `APPROVE`，Owner 显式指派的 `Planning/Audit Coordinator` 才能冻结 E06。解析 exact Golden Key 0.3.25 release/artifact、E05 accepted method/evidence manifest、同类 fixture/brief、current client identity 和 fresh before-state。冻结“保持不变”的是 ordinary-language user journey、business brief/materials、applicable consent/cost scenario、Shell responsibilities、client/model where supported and frozen、acceptance/evidence method；不要求 Skill ZIP、model、client 或全部非-Package 字节机械相同；Package-owned Guide/Pipeline/Stage/tool、source-attributed package-specific Skill metadata/text/binding、derived creative decisions/artifacts 可不同。

#### 19.2 Worker 有序动作

1. 以 E05 同类的安装、缺漏引导、普通提示、consent 和证据方法运行 Golden Key 0.3.25。
2. WorkBuddy 必须读取 Golden Key 自身 verified Guide/Pipeline/Stage/tool authority；Shell 不选择或强制 official Pipeline。
3. 验证内部 Package 差异对普通用户透明、引导仍可执行、完整本地视频符合真实视频最低标准且 lineage 完整。same 轴固定为 ordinary-language user journey、business brief/materials、applicable consent/cost scenario、Shell responsibilities、client/model where supported and frozen、acceptance/evidence method；allowed-different 为 Package-owned Guide/Pipeline/Stage/tool、source-attributed package-specific Skill metadata/text/binding、derived creative decisions/artifacts；fail 为额外用户技术负担、第二控制面、手工绕行/fallback、未在 comparison manifest 归因的控制变量漂移。不要求 Skill ZIP、model、client 或全部非-Package 字节机械相同。
4. 不修改 official/GK Package，不以 byte comparison 代替用户结果，不在验收中 repair。
5. 冻结证据后由 Reviewer 做 E05/E06 目标级比较；取得 `G8 EVIDENCE_APPROVE_FOR_CLEANUP` 后，恢复 before-state 仍必须另有 `OwnerRollbackAuthorizationV1`。若恢复还包含卸载/注销、关闭 client/session 或删除 scratch，分别另需 `OwnerPackageActionAuthorizationV1`、`OwnerClientActionAuthorizationV1`、`OwnerCleanupAuthorizationV1`；任何 token 不得替代其他动作授权。

#### 19.3 E06 审核

Reviewer 核验 exact 0.3.25 identity、E05 lineage、用户入口与职责等价、Golden Key authority、完整视频、差异归因和 after-state。成功不证明门店业务质量、所有 Provider/Renderer 或规模。失败回 E03/E04/E06 named owner，不得由 E07 修复。

### 20. E07 具体规划、执行与审核方案

#### 20.1 Planner 接管条件

只有 E06 正式 `APPROVE` 后，Planner 与 Owner 冻结真实门店 brief、素材清单及权利、画幅/时长/字幕/音频等业务验收人可理解的标准、named Business Accepter、exact approved Golden Key product state、client/evidence roots 和 before-state。Provider/费用若实际需要，必须在执行前另列 source、用途、预算上限、secret handling 和单独 Owner 授权；没有授权时不得调用。

#### 20.2 Worker 有序动作

1. 用户以真实素材和自然语言业务需求进入已批准产品路径；Worker 不添加技术路由。
2. WorkBuddy 是唯一运行 Agent、用户对话主体和生产决策者；它在读取 verified OpenMontage Guide/Manifest/Pipeline/Stage/Tool/Reviewer/Checkpoint authority 后，按该 authority 作出 Pipeline/Stage/Tool/Review/Checkpoint/Provider/Renderer/内容决策；OpenMontage 是生产语义权威，不是第二运行 Agent；Shell 可基于 verified mechanical state 返回 bounded/deterministic 的环境、配置、command、prompt、next-step remediation facts/options/material 和机械 relay；Shell 不理解业务意图、不发起 consent、不选择 recovery、不推进生产。
3. 产出真实竖屏业务视频和完整 lineage，交给 named Business Accepter 按冻结 brief 接受或拒绝。
4. 业务拒绝、权利/费用不清、需修代码或证据不足均立即停止；不得现场修 Shell/Core/媒体逻辑。
5. 冻结业务、Git/CI/client/provider/residue 证据；task-session scratch 的 `TASK_CLEANUP` 必须严格按 `G8 EVIDENCE_APPROVE_FOR_CLEANUP + OwnerCleanupAuthorizationV1 -> G9 after-state -> Closeout Worker 生成 exact candidates -> G10 FINAL_CLOSEOUT_REVIEW`，不能仅凭结果审查删除。关闭 WorkBuddy/client/session 另需 `OwnerClientActionAuthorizationV1`，恢复 before-state 另需 `OwnerRollbackAuthorizationV1`。
6. 只生成 closeout、proposed formal-delivery manifest、task-cleanup manifest 和 separate project-cleanup manifest；E07 内不得执行 `FORMAL_DELIVERY` 或 `PROJECT_CLEANUP`。

#### 20.3 E07 审核与项目停止点

Business Accepter 的业务结论与 independent Reviewer 的工程/证据结论必须同时为 APPROVE；task-owned 临时状态必须先完成 `G8 + OwnerCleanupAuthorizationV1 -> TASK_CLEANUP -> G9 after-state`，随后 Closeout Worker 生成 exact six-doc/manifest candidates，再由 G10 审核该 exact candidate。只有 G10 `FINAL_RESULT_APPROVE` 后，才能分别申请 candidate commit、push、`FORMAL_DELIVERY` 与远端/适用 CI 核验。`PROJECT_CLEANUP` 只指项目级历史工作树/分支/证据根或其他 closeout manifest 对象，只能在 `FORMALLY_DELIVERED` 后由 Owner 另行授权；它不等于任务清理，也不得回删已审核证据。任一环节失败，项目保持未完成；不得用“技术上能播放”覆盖业务拒绝。

### 21. Planner 与执行窗口的逐步交接闭环

```text
Owner explicitly assigns Planning/Audit Coordinator with an auditable handoff record
 -> reads latest formal result
 -> drafts one E0xExecutionPacketV1
 -> independent PLAN/PRE_EXECUTION review
 -> Owner grants exactly one task
 -> fresh execution conversation performs takeover and bounded execution
 -> evidence freeze + independent result/cleanup review
 -> authorized task cleanup + after-state
 -> Closeout Worker exact six-doc/manifest candidates
 -> independent final review of exact candidates
 -> reviewed result candidate
 -> separate commit/push/FORMAL_DELIVERY decisions
 -> Planning/Audit Coordinator audits goal drift under the same task handoff
 -> only then drafts next E0xExecutionPacketV1
```

新执行对话不得把“接管核验”扩展为新规划。当前规划对话不得把“未来可补充”变成下游 repair window。任一步未正式交付时，下一任务状态固定为 `NOT_AUTHORIZED_BY_CHAIN`。

### 22. Git、CI、FORMAL_DELIVERY 与清理的不可变规则

唯一规范术语是 `FORMAL_DELIVERY`：它指 Owner 授权后，将已审核并已推送的 candidate commit 以 ordinary fast-forward 更新 `refs/heads/codex/workbuddy-shell-v2`，随后核验远端 commit/tree 和适用 CI。更早历史节中的旧交付字段不得用于本 E 合同，也不形成额外 Git 动作。规划候选与任务结果候选只是 payload 类型不同，状态机完全相同。

```text
REVIEW_APPROVE
 -> OWNER_COMMIT_AUTHORIZATION
 -> CANDIDATE_COMMIT
 -> OWNER_PUSH_AUTHORIZATION
 -> CANDIDATE_PUSH
 -> OWNER_FORMAL_DELIVERY_AUTHORIZATION
 -> ORDINARY_FAST_FORWARD_FORMAL_REF
 -> REMOTE_COMMIT_TREE_VERIFICATION
 -> CI_HEADSHA_SUCCESS_IF_REQUIRED
 -> FORMALLY_DELIVERED
 -> OWNER_NEXT_TASK_AUTHORIZATION_SEPARATE
```

1. Worker 的产品/证据改动与 Closeout Worker 的六文档改动必须按 packet 权限分离；E02 Planner 只写 `packet/`、`inputs/`，并且只能在 Owner 授权后写 `handoff/E02TakeoverV1.json`；Execution Worker 只写 evidence root 的 `reports/`、`evidence/`，Closeout Worker 只写六文档，Reviewer 永远零写。
2. Reviewer 必须先审 unstaged exact diff；candidate commit 只能包含 exact allowlist，提交前核验 parent、tree、changed paths、staged/untracked/stash 和 `git diff --check`。
3. commit 形成后必须由零写 Reviewer 核验 exact commit/tree 与已审字节一致并返回 post-commit binding `APPROVE`；只有该结果和本轮 Owner 条件授权同时存在，才可 push 到任务专用 `codex/` 分支；禁止 force-push。
4. `FORMAL_DELIVERY` 前 formal ref 必须仍等于 packet 基线；只允许 ordinary fast-forward；禁止 merge、rebase、force-push。
5. `FORMAL_DELIVERY` 后必须用 live remote ref 核验 commit/tree；需要 CI 的任务必须等待 `headSha == delivered commit` 且最终 success，未截断输出和最终 exit 存在。
6. `FORMALLY_DELIVERED` 不授权下一任务；下一 task packet 只能由 Planner 在读取正式结果后重新产生并独立审核。
7. 失败证据在 Reviewer 完成前不可卸载/删除；cleanup 只允许 manifest 的 exact targets，先核验 resolved absolute paths 和 non-targets，再清理并捕获 after-state。
8. accepted evidence、failed evidence、temporary scratch、用户数据和历史对象必须分类；历史 worktree、Package source、外来对象、用户项目/凭据永不因 task cleanup 被删除。
9. rollback 失败时立即停止 cleanup；`FORMAL_DELIVERY` 前可放弃尚未 delivered 的候选，完成后只能新建独立 reviewed correction，不得改写历史。

本节具有 append-only precedence：此前 pre-delivery status fields（明确标为 `HISTORICAL_PRE_DELIVERY_SNAPSHOT`）以及已完成的旧 route candidate commit/push 字段均不参与当前路由。当前 E01 correction candidate 的 commit/push 状态只以本文末 `V2-E01-ROUTE-BOUNDARY-CORRECTION1` current section 和六文档一致镜像为准；本次工作树尚未形成 commit，等待独立复审和 Owner 后续 Git 决定。

## [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] V2-E01-DOCS-FORMAL-CLOSEOUT1 候选（2026-08-25）

### 1. 首次正式交付事实

```text
planning_delivery_commit: 1ad4aa136b99d73e76a6f8847b7deb7d064649d0
planning_delivery_tree: 6db61922d6c07c3ff337dbaa761ca6d65c080bbf
planning_delivery_parent: 533fb410fda837259afa29e2bb2fdee76caca599
formal_ref: refs/heads/codex/workbuddy-shell-v2
delivery_method: ORDINARY_FAST_FORWARD / NO_FORCE_NO_MERGE_NO_REBASE
remote_commit_tree_verification: PASS
ci: run 32809470079 / completed / success / headSha=1ad4aa136b99d73e76a6f8847b7deb7d064649d0 / 395 passed / 1 skipped
planning_payload_state: FORMALLY_DELIVERED
```

### 2. Closeout 精确合同

```text
task_id: V2-E01-DOCS-FORMAL-CLOSEOUT1
task_kind: DOCS_ONLY_STATE_CLOSEOUT / EXACT_SIX_AUTHORITY_FILES / ZERO_PRODUCT_STATE_CHANGE
baseline: 1ad4aa136b99d73e76a6f8847b7deb7d064649d0 / tree 6db61922d6c07c3ff337dbaa761ca6d65c080bbf
allowlist: AGENT_GUIDE.md + PROJECT-STATE.md + docs/workbuddy/v2/TASK-REGISTER.md + docs/workbuddy/v2/PROJECT-CHARTER.md + docs/workbuddy/v2/ACCEPTANCE-MATRIX.md + docs/workbuddy/v2/DRIFT-GUARD.md
forbidden: WORKBUDDY_PRODUCT_TEST_PACKAGE_REGISTRATION_INSTALLER_PROVIDER_MEDIA_CLIENT_E02_E07_EXECUTION
local_tests: NOT_RUN_DOCS_ONLY
review_gate: INDEPENDENT_ZERO_WRITE_REVIEW_REQUIRED / ACCEPT_ONLY_IF_APPROVE_AND_P0_P1_P2_ZERO
candidate_commit: THIS_COMMIT
candidate_push: TASK_BRANCH_ONLY / ORDINARY_FAST_FORWARD / NO_FORCE
formal_delivery: OWNER_AUTHORIZED_DOCS_CONTINUATION / ORDINARY_FAST_FORWARD_ONLY
closeout_result: THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR
closeout_delivery_resolution: INDEPENDENT_ZERO_WRITE_APPROVE + LIVE_FORMAL_REF_CONTAINS_THIS_COMMIT + REMOTE_TREE_EXACT + EXACT_HEAD_CI_SUCCESS
E01_final_state: FORMALLY_DELIVERED_WHEN_CLOSEOUT_DELIVERY_RESOLUTION_IS_TRUE
current_task: NONE / NO_ACTIVE_TASK_AFTER_E01_CLOSEOUT
E02_E07: NOT_STARTED / NOT_AUTHORIZED
next_authorized_task: NONE / SEPARATE_OWNER_E02_AUTHORIZATION_REQUIRED_IN_NEW_TASK
cleanup: NOT_INCLUDED / SEPARATE_OWNER_AUTHORIZATION_REQUIRED
```

### 3. Append-only precedence 与停止点

本节保留首次 closeout 的提交、tree、CI 和交付事实；不再作为当前 E01 零缺陷或 E02 可启动结论。最新状态见下方 `V2-E01-ROUTE-BOUNDARY-CORRECTION1`。

E01 最终闭环只说明项目目标、用户旅程、E02-E07 packet、角色分离、证据/清理/回滚和 Git 硬门已成为正式文档 authority；它不证明产品代码、Installer、WorkBuddy、Provider、媒体或真实业务路径已经执行。Closeout 后必须停止，E02 保持 `NOT_STARTED / NOT_AUTHORIZED`，只允许 Owner 在新任务中另行授权。

## V2-E01-ROUTE-BOUNDARY-CORRECTION1（2026-08-25，当前候选）

本节是基于正式基线 `419373094e7ac4e1a5f092d25d8e62cef8a76a6d` / tree `bf2210f9c63661e10f16188faf860f27b2278390` 的最新 E01 目标边界纠正。此前 `V2-E01-DOCS-FORMAL-CLOSEOUT1` 的提交、tree、CI 和历史 closeout 事实保留，但不再作为“零缺陷、可直接启动 E02”的结论。后续 goal-boundary audit 已记录 `REJECT / P0=0 / P1=7 / P2=3`；因此 E01 重开为 docs-only correction candidate，E02-E07 保持阻断。

```text
task_id: V2-E01-ROUTE-BOUNDARY-CORRECTION1
task_kind: DOCS_ONLY_GOAL_AND_BOUNDARY_CORRECTION
baseline_commit: 419373094e7ac4e1a5f092d25d8e62cef8a76a6d
baseline_tree: bf2210f9c63661e10f16188faf860f27b2278390
candidate_branch: codex/v2-e01-route-boundary-correction1
allowlist: AGENT_GUIDE.md + PROJECT-STATE.md + docs/workbuddy/v2/TASK-REGISTER.md + docs/workbuddy/v2/PROJECT-CHARTER.md + docs/workbuddy/v2/ACCEPTANCE-MATRIX.md + docs/workbuddy/v2/DRIFT-GUARD.md
state: DOCS_ONLY / CORRECTION_CANDIDATE / NOT_FORMALLY_DELIVERED
route: E01 -> E02 -> E03 -> E04 -> E05 -> E06 -> E07
E02_E07: NOT_STARTED / NOT_AUTHORIZED / BLOCKED_BY_E01_CORRECTION
tests: NOT_RUN_DOCS_ONLY
verification: git diff --check ONLY
review_gate: INDEPENDENT_ZERO_WRITE_REVIEW_OF_EXACT_DIFF_REQUIRED
forbidden: PRODUCT_CODE + TEST_CODE + WORKBUDDY + PACKAGE + REGISTRATION + INSTALLER_ACTION + PROVIDER + MEDIA + CLIENT + E02_E07_EXECUTION + FORMAL_DELIVERY + CLEANUP
```

### E01 的唯一产品目标与反漂移裁决

最低成功标准是：普通用户在 WorkBuddy 中提出自然语言业务需求；WorkBuddy 是唯一运行 Agent、用户对话主体和生产决策者；它在读取 verified OpenMontage Guide/Manifest/Pipeline/Stage/Tool/Reviewer/Checkpoint authority 后，按该 authority 作出 Pipeline/Stage/Tool/Review/Checkpoint/Provider/Renderer/内容决策；OpenMontage 是生产语义权威，不是第二运行 Agent；Shell 只负责安装、环境/定位、受控机械执行、入口、状态/结果 relay 和可执行引导；最终必须能在真实 WorkBuddy 产出真实完整可播放视频。任何不能直接降低这条链路的用户门槛、不能支撑这条链路或会新增第二控制面的功能、模块、约束均不得进入后续 packet。

命令边界固定为：普通用户不得被要求理解、构造或看到内部 path/hash/schema/env/argv/transport；WorkBuddy/model 不得猜测、自由合成或从用户输入推导这些内部值；WorkBuddy/固定 Skill 可接收并调用由 verified Package/Shell 提供、identity-checked、allowlisted 的 exact mechanical operation。调用只是受控机械执行，不授予 Shell 生产决策权。

引导边界固定为：Shell 可基于 verified mechanical state 返回 bounded/deterministic 的环境、配置、command、prompt、next-step remediation facts/options/material；Shell 不理解业务意图、不发起 consent、不选择 recovery、不推进生产；WorkBuddy 是唯一用户对话主体，独占面向用户的解释/呈现、consent、recovery/continue、生产语义和业务决策。

### E02 唯一 evidence carrier 与写入域

E02 唯一 task root 固定为 `D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_E02_User_Journey_Minimal_Change_Audit1`，不得另建同义 evidence root。相对路径固定为：

```text
packet/E02ExecutionPacketV1.json
inputs/E02InputManifestV1.json
handoff/E02TakeoverV1.json
reports/E02ExecutionReportV1.json
evidence/E02EvidenceIndexV1.json
```

所有载体均为 UTF-8、无 BOM、LF、最终 LF；绑定使用原始字节 SHA256。被 hash 的文件不写自 hash；`E02TakeoverV1` 必须绑定 packet、formal commit/tree、task、allowlist、forbidden 和 Owner authorization；`E02EvidenceIndexV1` 必须绑定 packet、input manifest、takeover、execution report 的完整相对路径与原始字节 SHA256。任何 SHA、路径、对象或字节不一致均为 `STOP_PACKET_MISMATCH`。

Planning/Audit Coordinator 只可写 `packet/`、`inputs/`，并且只能在 Owner 授权后记录 `handoff/E02TakeoverV1.json`；Execution Worker 只可在该 task root 写 `reports/` 与 `evidence/`，不能写仓库；Closeout Worker 只可写六份 authority docs，不能改 evidence；Independent Reviewer 对仓库和 evidence 全零写。E02 报告和证据未冻结并通过审查前，不得清理。

### E02 用户旅程闭集

E02 固定审计十条旅程：

1. `install-first-open-environment-ready`：安装、首次打开、环境就绪的 happy path；
2. `specific-request`：用户直接提出具体自然语言需求；
3. `vague-request-guided-entry`：用户表达模糊需求并获得 guided entry；
4. `package-absent-or-unverified`：Package 缺失或 identity 未验证；
5. `required-environment-missing`：必需环境缺漏；
6. `configuration-consent-optional-capability`：配置、consent、可选能力或 Provider 决定；
7. `verified-guide-manifest-handoff`：WorkBuddy 接收 verified Guide/Manifest 并保持 OpenMontage 决策归属；
8. `execution-error-recovery`：机械执行错误、暂停和可恢复继续；
9. `result-receipt-video-relay`：结果、receipt、Artifact lineage 和视频返回用户；
10. `safe-uninstall-rollback-data-preservation`：安全卸载、回滚和用户数据保全。

任何 packet、report、evidence index、接受矩阵或后续 E03/E04 allowlist 改变数量、顺序或定义，都必须同步更新并重新独立审查；不得再使用与内容不匹配的旧数量简称。

### E04、E05、E06 的最小验收边界

E04 owner 固定为 `V2 Final-delivery Installer / Release Assembly Owner`。immutable official/GK Package source owner 只负责各自 Package 字节、Guide、Manifest、Lock 和 Release identity；Shell-adapter owner 只负责独立 binding schema/consumer；final assembly/Manifest/Lock owner 负责把两者按 immutable source 组装并核验 lineage。E04 只产品化安装、装配、生命周期和 binding，不发明 Pipeline、Stage、Tool、Review、Checkpoint、Provider、Renderer 或内容生产逻辑。

E05/E06 的真实完整视频最低标准相同：不是 fixture、mock、demo、fallback 或孤立 MP4；必须由真实 WorkBuddy、verified authority 和真实工具执行产生；视频可播放、非零时长、竖屏；音视频 lineage 与 receipt 可审；没有手工绕行；任何失败不得冒充成功。E05/E06 的 comparison axes 固定为：same = ordinary-language user journey、business brief/materials、applicable consent/cost scenario、Shell responsibilities、client/model where supported and frozen、acceptance/evidence method；allowed-different = Package-owned Guide/Pipeline/Stage/tool、source-attributed package-specific Skill metadata/text/binding、derived creative decisions/artifacts；fail = 额外用户技术负担、第二控制面、手工绕行/fallback、未在 comparison manifest 归因的控制变量漂移。不要求 Skill ZIP、model、client 或全部非-Package 字节机械相同。

### 角色、授权与 Git 边界

`Planning/Audit Coordinator` 只能由 Owner 显式指派；角色 handoff record 必须包含 Owner identity、record ID、issued、expires、exact formal commit/tree、task、packet SHA、allowlist 和 forbidden。`UXCopyContractV1` 的 approver 必须是 Owner 或 Owner 指定的 approver。E03 在另有 client authorization 前仅允许 `OFFLINE_CONTRACT_ONLY`，不得借文案合同启动客户端或真实 WorkBuddy。

本轮 Owner 条件授权为：独立 Reviewer 先审 unstaged exact diff 并返回 `APPROVE / P0=0 / P1=0 / P2=0` 后，允许 candidate commit；commit 后必须由零写核验 exact commit/tree 与已审字节一致并返回 post-commit binding `APPROVE`，随后允许 push 到本任务专用 `codex/` 分支。该授权不包含 `FORMAL_DELIVERY` 或 E02；push 仍不得改变 formal ref。

## V2-E02-EXECUTION-PLAN-FREEZE1（2026-08-25，当前 docs-only 候选）

本节是 E02 的完整具体执行规划与六文档镜像源。它只冻结规划，不执行 E02，不修改产品，不改变 E01 formal/candidate 状态；候选提交/推送仅形成 `THIS_COMMIT / SELF_RESOLVING_REMOTE_CANDIDATE_CONTAINMENT`，不等于 `FORMAL_DELIVERY` 或 E02 authorization。

```text
plan_freeze_task: V2-E02-EXECUTION-PLAN-FREEZE1
execution_task: V2-E02-CURRENT-JOURNEY-MINIMAL-CHANGE-AUDIT
scope: DOCS_ONLY / EXACT_SIX_AUTHORITY_FILES / ZERO_PRODUCT_STATE_CHANGE
formal_base: 271dee394bed5ca3dd5c31860c842a8cbfdfa536 / tree 8eea24e3bc3fc5f4c6eed536281799edaebdde40
packet_path: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_E02_User_Journey_Minimal_Change_Audit1\packet\E02ExecutionPacketV1.json
packet_sha256: ddbd68018506f4df90a6c0bb49bd3d2127c5d77ee980ea890d5e02da2bb0c1a0
input_manifest_path: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_E02_User_Journey_Minimal_Change_Audit1\inputs\E02InputManifestV1.json
input_manifest_sha256: 5345a83d628c22e45e8265509af30dd8d77abca7aaab5c44ff6dca8737cf1956
plan_review: INDEPENDENT_ZERO_WRITE_APPROVE / P0=0 / P1=0 / P2=0 / EXACT_HASHES_BOUND
candidate_result: THIS_COMMIT / SELF_RESOLVING_REMOTE_CANDIDATE_CONTAINMENT
e02_state: NOT_STARTED / NOT_AUTHORIZED
handoff: NOT_CREATED
execution_report: NOT_CREATED
evidence_index: NOT_CREATED
required_next: PRE_EXECUTION_REVIEW + OwnerTaskExecutionAuthorizationV1
e03_e04: BLOCKED_BY_E02_CHAIN
```

### 1. 目标和不可越界边界

E02 只回答一个问题：普通用户从安装、首次打开、提出自然语言需求到取得真实结果的路径上，哪一段有证据证明会阻断，现有能力能否复用，真正需要的最小后续动作属于谁。E02 不创建功能，不为 E03/E04 凑任务；证据不足必须保持 `NOT_PROVED`。

WorkBuddy 是唯一运行 Agent、用户对话主体和生产决策者；OpenMontage 是生产语义 authority；Shell 只做安装、定位、受控机械执行、入口、状态/结果 relay 和可执行引导。普通用户不得接触 path/hash/schema/env/argv/transport；Shell 不理解业务意图、不发起 consent、不选择 recovery、不推进生产、不成为第二控制面。E02 是 `STATIC_READ_ONLY_EVIDENCE_AUDIT_NO_CLIENT_NO_PRODUCT_EXECUTION`：执行授权前，只允许按 manifest 对精确列明的代码、Skill、测试、历史材料和 documentary checkout 做只读检查。禁止执行或修改产品代码、测试、Skill、历史资产和外部仓库；禁止外部仓库写入、commit、push；禁止 WorkBuddy、浏览器/客户端、Package、Registration、Installer、Provider、媒体、视频、测试运行和 CI。只有独立 `PRE_EXECUTION_REVIEW` 通过且 `OwnerTaskExecutionAuthorizationV1` 生效后，Execution Worker 才可在固定 task root 写入 exact `reports/` 与 `evidence/` carriers；其他六文档外写入及 cleanup 均禁止。

### 2. 九个阶段的实际执行顺序

| 阶段 | 执行内容 | 必须形成的结果/硬停条件 |
|---|---|---|
| P0 `TAKEOVER_AND_FAIL_CLOSED` | 核验 Owner token、exact packet/manifest、formal commit/tree、角色和写域 | 不一致即 `STOP_NOT_AUTHORIZED` 或 `STOP_PACKET_MISMATCH` |
| P1 `EXACT_INPUT_VERIFICATION` | 逐项核验 11 组 input 的 exact identity；不读 external OpenMontage `AGENT_GUIDE.md` | 缺失/额外/漂移/不可读即 `BLOCKED_INPUT_NOT_PROVED` |
| P2 `TARGET_JOURNEY_BASELINE` | 固定每条旅程的用户起点、动作、可见成功结果、责任链 | 十条旅程都能回答用户门槛且不产生第二控制面 |
| P3 `CURRENT_FLOW_STATIC_TRACE` | 只按 exact path/symbol 静态追踪代码、Skill、测试、历史材料；分开五种事实等级 | 每条旅程都有 evidence ref 或 `NOT_PROVED` |
| P4 `ASSET_CLASSIFICATION` | 审计七组资产，优先 KEEP/NO_CHANGE；REWORK/REMOVE 必须有 confirmed blocker | 每项分类唯一并带理由、用户价值、保护边界、不能证明 |
| P5 `MINIMAL_CHANGE_TRACE` | blocker→change、change→blocker 双向映射；拆分 E03/E04 | 无孤立 blocker、无无依据 change、无下游 repair window |
| P6 `REPORT_AND_EVIDENCE_FREEZE` | 固化 report/index、source identity、internal locator、after-state | 固定编码/行尾，hash 可复算，无 dangling/duplicate evidence |
| P7 `INDEPENDENT_RESULT_REVIEW` | 先审目标与用户价值，再审事实、旅程、映射、证据、写域 | `APPROVE / P0=0 / P1=0 / P2=0`，否则 `INCOMPLETE` |
| P8 `CLOSEOUT_BOUNDARY` | 结果审查后才可由 Closeout Worker 镜像六 docs；保留证据 | `NOT_APPLICABLE_WITH_EVIDENCE`，不自动启动下游 |

### 3. 十条固定旅程闭集

必须严格按以下顺序审计，数量、顺序和定义变化必须同步 packet/report/index/六文档并重新审查：

1. `install-first-open-environment-ready`：安装、首次打开、环境就绪；
2. `specific-request`：具体自然语言需求；
3. `vague-request-guided-entry`：模糊需求与 guided entry；
4. `package-absent-or-unverified`：Package 缺失或 identity 未验证；
5. `required-environment-missing`：必需环境缺漏；
6. `configuration-consent-optional-capability`：配置、consent、可选能力或 Provider 决定；
7. `verified-guide-manifest-handoff`：verified Guide/Manifest handoff 与决策归属；
8. `execution-error-recovery`：机械错误、暂停、恢复、继续；
9. `result-receipt-video-relay`：结果、receipt、Artifact lineage、视频 relay；
10. `safe-uninstall-rollback-data-preservation`：安全卸载、升级/回滚、用户数据保全。

### 4. 单一 16-field journey schema

每条记录必须独立填满：`journey_order`、`journey_id`、`ordinary_user_start_state`、`ordinary_user_action`、`expected_user_visible_outcome`、`responsibility_chain`、`exact_inputs_examined`、`current_static_capability`、`confirmed_user_blockers`、`evidence_refs`、`journey_status`、`candidate_disposition`、`candidate_change_refs`、`visible_copy_or_accessibility_risks`、`negative_case`、`cannot_prove`。

`journey_status` 只允许 `SUPPORTED_STATICALLY`、`PARTIAL`、`BLOCKED_BY_CONFIRMED_GAP`、`NOT_PROVED`；`candidate_disposition` 只允许 `NO_CODE_CHANGE_REQUIRED`、`E03_CANDIDATE`、`E04_CANDIDATE`、`E03_E04_SPLIT_CANDIDATE`、`NO_DOWNSTREAM_ACTION_NOT_PROVED`。

### 5. 七个结构化 output contracts

固定为：

1. `blocker_record`：blocker、用户影响、当前/预期状态、证据、事实等级、处置、不能证明；
2. `candidate_change_record`：change、owner、exact path/symbol、意图、linked blocker、用户价值、保护非目标、验收、证据、状态；
3. `bidirectional_trace_record`：blocker/change 双向完整性与孤立原因；
4. `downstream_boundary_record`：E03/E04 owner、用户阻断、exact allowlist/denylist、保护边界、验收、输入、不能证明、authorization；
5. `fact_record`：statement、五种事实等级、证据、使用方、限制；
6. `deviation_or_stop_record`：偏差/停止条件、阶段、状态、停止前写入、部分报告、下游状态、证据；
7. `evidence_index_record`：evidence identity、source kind/input、required `source_locator`、支持的 statement/blocker、证据限制。

Evidence 必须绑定 exact Git blob 或 external file；`source_locator` 必须是 `line_start + line_end`、`symbol`、`markdown_heading` 或 `json_pointer`，整文件 hash alone 不足以支持 blocker。动态 URL 在 E02 一律 `FORBIDDEN`。

### 6. 七组资产与四路最小处置

七组资产为：`current_registration_locator`、`current_optional_runtime`、`current_launcher_and_entry`、`current_package_exports_and_hygiene`、`historical_guidance_and_lifecycle`、`documentary_package_comparison`、`historical_raw_negative_evidence`。只审 packet 列明的 exact path/symbol；历史材料不得整包恢复或执行。

资产分类仅允许 `KEEP`、`REWORK`、`REMOVE`、`NO_CHANGE`、`NOT_PROVED`。`REWORK`/`REMOVE` 必须有 confirmed blocker、evidence、named owner；无 blocker 时优先 KEEP/NO_CHANGE。最小改动路由为：`E03_CANDIDATE`（入口、guided entry、可见引导、错误解释、呈现）、`E04_CANDIDATE`（安装、装配、版本化生命周期、binding）、`NO_CODE_CHANGE_REQUIRED`（现有能力/非代码合同已够）、`NOT_PROVED`（证据不足，不创建任务）。跨 E03/E04 必须拆分，每个 change 必须反向连接 blocker。

### 7. 十一组 exact inputs、载体和角色写域

11 组 input 固定为：`e01-current-authority`、`package-registration-contract-documentary`、`current-shell-source-tests-skill`、`original-v2-handoff-owner-snapshot`、`historical-v2-next-session-handoff`、`historical-guided-skill`、`historical-installer-lifecycle-assets`、`official-openmontage-documentary-source`、`golden-key-0.3.25-documentary-source`、`b04-raw-negative-evidence`、`d01-historical-manifest`。只有 E01 六 docs 是当前 authority；Package Registration 是 documentary input；external OpenMontage `AGENT_GUIDE.md` 仅 identity-only，禁止读取。

唯一 task root 为 `D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_E02_User_Journey_Minimal_Change_Audit1`，载体固定为 `packet/E02ExecutionPacketV1.json`、`inputs/E02InputManifestV1.json`、`handoff/E02TakeoverV1.json`、`reports/E02ExecutionReportV1.json`、`evidence/E02EvidenceIndexV1.json`。所有载体 UTF-8 no BOM/LF/final LF，原始字节 SHA256 绑定；被 hash 文件不写自 hash。Planner 只写 packet/input，Owner token 后才可写 takeover；Execution Worker 只写 root 下 reports/evidence；Closeout Worker 只写六 docs；Reviewer 全零写；证据冻结且审查前不得清理。

### 8. 审查、停止和授权顺序

已存在的 PLAN_REVIEW 只证明 exact packet/manifest 规划通过，不等于可执行。新执行对话必须先由独立零写 Reviewer 做 `PRE_EXECUTION_REVIEW`，复核 live formal commit/tree、11 组 inputs、packet/manifest hashes、角色写域、九阶段、十旅程、16 字段、7 contracts、7 assets、source locator 和 dynamic URL 禁止规则；然后 Owner 才能签发绑定 exact packet SHA/formal objects/allowlist/forbidden 的 `OwnerTaskExecutionAuthorizationV1`。任何 mismatch、越界、缺 evidence locator、dynamic URL、事实等级坍缩、无 blocker 的改动、Shell 生产决策、第二控制面、真实 WorkBuddy/Package/Provider/media/video overclaim 或提前 cleanup，立即 `STOP`；E03/E04 保持阻断。

### 9. 当前固化状态

本次 Closeout Worker 只固化上述六份 authority docs；E02 `NOT_STARTED / NOT_AUTHORIZED`，`handoff/report/evidence` `NOT_CREATED`，E03/E04 `BLOCKED_BY_E02_CHAIN`。E02 只有在 execution report/evidence index 完整冻结并经独立结果审查后，才能形成下游 candidate boundary；本候选不授权执行、产品改动、客户端操作、测试、Package/Provider/media、cleanup、`FORMAL_DELIVERY` 或下一任务。

## V2-E02-NONRECURSIVE-BINDING-CORRECTION1（2026-08-25，当前绑定纠偏）

本节只纠正 E02 的 formal lineage 绑定，完整 E02 执行合同仍由上方 `V2-E02-EXECUTION-PLAN-FREEZE1`、exact packet 和 exact input manifest 共同提供。旧 `formal_base == live formal` exact-live-equality 规则自本节起被取代；九阶段、十旅程、16-field schema、7 contracts、7 assets、11 inputs、载体、写域、dynamic URL `FORBIDDEN`、`NOT_PROVED`、WorkBuddy sole Agent 和 Shell support/mechanical 边界均不变。

```text
correction_task: V2-E02-NONRECURSIVE-BINDING-CORRECTION1
evidence_product_baseline: 271dee394bed5ca3dd5c31860c842a8cbfdfa536 / tree 8eea24e3bc3fc5f4c6eed536281799edaebdde40
formally_delivered_authority_floor: 1713ba8d0d3279233d702339548a242e40a1e759 / tree 38eddb5ccdbb000eb2048713c4b30a7f4e9e8d9b
packet_path: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_E02_User_Journey_Minimal_Change_Audit1\packet\E02ExecutionPacketV1.json
packet_sha256: 4120acf17e204d78cedd743d3eb84b6491bbf1aef2b607df49c645e59eb930d4
input_manifest_path: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_E02_User_Journey_Minimal_Change_Audit1\inputs\E02InputManifestV1.json
input_manifest_sha256: aeeae389aeade2b992efbcf8f46c4f7372c4a5df57b16bb84b87ea57be69cad2
live_formal: RESOLVE_LIVE_REMOTE_REF_AT_PRE_EXECUTION_REVIEW; OWNER_TOKEN_AND_E02TAKEOVER_LOCK_EXACT_COMMIT_TREE
floor_ancestry: authority floor MUST_BE_ANCESTOR_OF_LIVE_FORMAL
floor_to_live_scope: ONLY_AGENT_GUIDE_MD_PROJECT_STATE_MD_TASK_REGISTER_MD_PROJECT_CHARTER_MD_ACCEPTANCE_MATRIX_MD_DRIFT_GUARD_MD
manifest_baseline: current repository inputs remain exact at evidence/product baseline; historical/external inputs remain individually frozen exact identities
future_correction_commit: NOT_EMBEDDED_IN_PACKET
stop: STOP_FORMAL_LINEAGE_OR_SCOPE_MISMATCH
e02_state: NOT_STARTED / NOT_AUTHORIZED
```

### 非递归绑定硬合同

1. `evidence_product_baseline` is the fixed product/evidence comparison point. It is not the execution-time live formal object and is never rewritten to a future correction commit.
2. `formally_delivered_authority_floor` is the minimum planning authority. Before `PRE_EXECUTION_REVIEW` can approve, the live formal ref must resolve, the floor must be its ancestor, and the complete `floor..live` path set must be limited to the exact six authority docs listed above. Any product code, test, Skill or other path is `STOP_FORMAL_LINEAGE_OR_SCOPE_MISMATCH`.
3. The live formal commit/tree is resolved from the live remote ref immediately before authorization and is recorded exactly in `OwnerTaskExecutionAuthorizationV1` and `E02TakeoverV1`. A packet or chat value cannot substitute for that lock; no future correction commit is embedded here.
4. All current-repository manifest identities used as evidence must still match the fixed evidence/product baseline. Historical and external inputs remain their own frozen exact commit/tree/path/blob or path/size/SHA256 identities; any drift is `BLOCKED_INPUT_NOT_PROVED`.
5. The reviewer checks the above lineage and scope before content execution. The Execution Worker repeats it at takeover; failure stops before audit content writes, except the fixed partial stop-report rule already in the packet.

### 前置审查与结果边界更新

`PLAN_REVIEW` binds the exact corrected packet and manifest hashes. `PRE_EXECUTION_REVIEW` is a separate zero-write readiness check of those hashes, the fixed evidence baseline, authority-floor ancestry, exact-six-only `floor..live` scope, dynamically resolved live formal commit/tree, all manifest identities, role write domains and unchanged E02 boundaries. Only after it returns `PRE_EXECUTION_APPROVE / P0=0 / P1=0 / P2=0` may the Owner issue `OwnerTaskExecutionAuthorizationV1`; E02 remains `NOT_STARTED / NOT_AUTHORIZED` until that token and takeover exist. This correction does not authorize E02, E03, E04, product/client/test/Package/Provider/media actions, cleanup, commit, push or `FORMAL_DELIVERY`.
