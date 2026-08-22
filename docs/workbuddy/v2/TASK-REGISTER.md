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

## 项目级架构纠偏审计 Phase A 账本镜像（A7 docs-only candidate，2026-08-22）

本节是 A0-A6 经独立零写 Reviewer 批准后的唯一项目级纠偏审计结论与最小执行方案。它不是 Stage 5 产品完成，也不是 Phase B 授权；既有历史记录和历史 PASS 不被改写。A7 候选只改六个现有权威文件，零产品状态变化。

```text
task_id: V2-PROJECT-ARCHITECTURE-RECOVERY-PHASE-A1
candidate_branch: codex/v2-architecture-recovery-audit-phase-a1
candidate_worktree: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_Architecture_Recovery_PhaseA1
formal_ref: refs/heads/codex/workbuddy-shell-v2
formal_anchor_commit: f338d9d50cad2cccf1398438ad4a8c8d45127a21
formal_anchor_tree: 5ef5e8e524412f6220ad31f2cc38448c6b1dac8b
candidate_base: EXACT_FORMAL_ANCHOR / CLEAN / DIVERGENCE=0/0
phase_a_status: A0-A6_APPROVED / A7_DOCS_CANDIDATE / NOT_PROMOTED
candidate_scope: EXACTLY_SIX_EXISTING_AUTHORITY_FILES / DOCS_ONLY
candidate_effect: ZERO_PRODUCT_STATE_CHANGE
test_label: NOT_RUN_DOCS_ONLY
phase_b: NOT_AUTHORIZED
```

### 统一审计结论

原始目标是：普通用户只用自然语言向 WorkBuddy 提出业务请求；WorkBuddy 是唯一运行 Agent、唯一用户对话主体和唯一入口；在 Registration/Locator 验证 Package identity 后，WorkBuddy 读取 Guide、Manifest、Pipeline/Stage/Artifact/Checkpoint/Reviewer/Tool/Provider 合同并作生产决策；Shell 只承担六模块支持职责。OpenMontage Agent 是 WorkBuddy 读取已验证 Guide 后承担的逻辑角色，不是第二 Agent。

A1-A6 的谱系结论是：Stage 4 的机械 Launcher 合同被错误地当成产品架构完成，Stage 5 没有把最终 Package/Installer/生产 Registration/Activation 和真实 WorkBuddy Guide-read 证据纳入同一条完成链；缺失责任应由最终交付 Installer/Release Assembly Owner 承担，不应把 Shell adapter 缺失归因成共享 0.3.24 Package 必须内置 WorkBuddy 入口。

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

旧 R03-R05 执行包由 B02/B03 `SUPERSEDED_WITH_VALID_REASON`，不得与 B01-B07 并行。纠偏任务严格串行：`B01 -> B02 -> B03 -> B04 -> B05 -> B06 -> B07`；B04 先用固定 official 对照组，B05 保持同一 Shell 路径仅切换到固定 0.3.24；B06 唯一下游为 `HANDOFF_TO_B07_ONLY`；B07 之后唯一动作是 `PROMOTE_AND_CLEANUP`，且仅允许普通 fast-forward。

### B01 冻结 binding 与 Guide-read 合同

```text
01_task_id: V2-ARCH-RECOVERY-B01-FREEZE-BINDING-GUIDE-READ-CONTRACT
02_confirmed_issue: Stage4机械合同与R02被当成产品架构/Package完成；binding owner、carrier、Guide-read真实顺序和可观察证据未冻结
03_why_correction_necessary: 没有先冻结责任和证据边界，B02以后会继续把Shell/Package/WorkBuddy职责混在一起并重复制造伪完成
04_correct_owner: V2 Project Architecture Recovery Coordinator / Shell contract owner
05_authoritative_inputs: A0-A6 approved result; AGENT_GUIDE.md; PROJECT-STATE.md; PROJECT-CHARTER.md; ACCEPTANCE-MATRIX.md; DRIFT-GUARD.md; fixed official commit 4eab34c5cfcccaa4f1970554928feccce73ee930; 0.3.24 candidate ef5f5b58fa1c2b494b0154989cf0e4e36615a701 read-only
06_exact_allowed_paths: AGENT_GUIDE.md; PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md; docs/workbuddy/v2/DRIFT-GUARD.md
07_concrete_actions: Freeze binding schema/consumer owner; final PackageRoot Shell-adapter carrier; immutable 0.3.24 boundary; Guide-read/decision/transport/child/receipt order; observable client evidence; anti-second-Agent/Director rules; stage dispositions and R02 recommended fields
08_explicitly_not_do: No product code, tests, CI, Package, external repository, WorkBuddy client, Skill install, Registration, Activation, Provider, media, or PhaseB execution
09_output_contract: Single mirrored PhaseA decision record; B02-B07 serial contract; r02_live_status unchanged and recommended_reclassification=NOT_YET_EFFECTIVE
10_positive_tests: Cross-file key/value agreement; exact six-file allowlist; stage dispositions present; B01-B07 order and owner/carrier fields present
11_negative_tests: Missing Guide-read evidence field; R02 live status changed; 0.3.24 made mutable; second control plane allowed; any unlisted path changed
12_independent_reviewer_checks: Zero-write review of exact candidate commit/tree; compare six files; verify historical facts preserved and no product-state wording is introduced
13_p0_p1_p2_standard: P0 any authority/branch/status mutation or second-Agent authorization; P1 missing owner/order/evidence boundary; P2 wording drift or incomplete cross-file mirror
14_fail_closed_conditions: Baseline/tree/branch mismatch; six-file whitelist violation; conflicting live authority; missing owner; inability to distinguish historical PASS from current state
15_upstream_dependency: A0-A6 independently approved and user authorization to solidify PhaseA docs
16_downstream_handoff: B02 only; no B03-B07 parallel start
17_real_workbuddy_required: NO
18_official_control_group: NO (fixed official identity may be read-only input only)
19_involves_0_3_24: NO (read-only identity/immutability input only)
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
08_explicitly_not_do: No second Skill, CLI subcommands, public CLI, MCP, Router, Agent/Director/FSM/Supervisor, arbitrary shell/command, path scan/guess/PATH fallback, renderer/provider selection, retry/replay, media logic, Package/0.3.24 modification
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
19_involves_0_3_24: NO; adapter is not embedded in the shared Package
20_proves_after_completion: Shell-side deterministic transport and final Skill static/unit contract within the six-module boundary
21_cannot_prove_after_completion: Final PackageRoot/Installer lifecycle, production Registration, real WorkBuddy Guide-read, real receipt/Artifact, or portrait business E2E
```

### B03 最终 Package、Installer 与生命周期

```text
01_task_id: V2-ARCH-RECOVERY-B03-FINAL-PACKAGE-INSTALLER-LIFECYCLE
02_confirmed_issue: Final PackageRoot, independent Shell-adapter carrier, real fixed child, Manifest/Lock/hash, private toolchain and production lifecycle are absent/unproved; R02 assigned this to the wrong layer
03_why_correction_necessary: Stage5 cannot accept a static entry without a reproducible final assembly, install/upgrade/rollback/uninstall and production Registration/Activation owner
04_correct_owner: V2 Final-delivery Installer / Release Assembly Owner
05_authoritative_inputs: B02 approved Shell adapter; Package Registration contract; immutable 0.3.24 candidate ef5f5b58fa1c2b494b0154989cf0e4e36615a701; required private toolchain rules; B01 binding contract
06_exact_allowed_paths: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_installer_source\ (owner source staging); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_final_assembly\ (assembly output); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_evidence\ (evidence); owner-designated Installer checkout exact absolute path and commit must be registered before start; no other path
07_concrete_actions: Assemble immutable OpenMontage subtree plus independent Shell-adapter subtree; materialize PackageToolDefinitionV1 and deterministic fixed child; create Manifest/Lock/hash; include private Python, FFmpeg/ffprobe and Node22+/npm/npx; implement install/upgrade/rollback/uninstall; create production Registration/Activation and fresh PackageRoot
08_explicitly_not_do: No modification of 0.3.24 bytes; no source-checkout substitution; no renderer/provider/media selection; no WorkBuddy Guide decision logic; no second Agent; no unregistered checkout or guessed path
09_output_contract: Reproducible final PackageRoot and lifecycle receipt with subtree hashes, fixed child identity, toolchain identities, Registration/Activation and rollback evidence
10_positive_tests: Fresh assembly hash/lock/manifest reconciliation; toolchain availability including Node22+/npm/npx; install/register/activate/locate; upgrade/rollback/uninstall; fixed child source/hash/argv/cwd identity
11_negative_tests: Tampered subtree/lock/guide; missing tool; wrong Node version; stale/foreign Registration; rollback failure; source checkout instead of assembled Package; 0.3.24 byte change
12_independent_reviewer_checks: Verify owner/path/commit; immutable 0.3.24 subtree hash; adapter isolation; complete lock/manifest; fresh lifecycle and exact evidence roots; no external Package write
13_p0_p1_p2_standard: P0 mutable 0.3.24, untrusted PackageRoot, secret/path escape or unsafe lifecycle; P1 missing hash/tool/rollback/Registration evidence; P2 reproducibility or evidence packaging defect
14_fail_closed_conditions: Owner checkout path not pre-registered; any source/tree/hash mismatch; missing Node22+/npm/npx or private toolchain; stale registration; mutable shared Package; incomplete rollback
15_upstream_dependency: B02 approved and exact owner authority for Installer checkout
16_downstream_handoff: B04 official fixed control-group acceptance; B05 later same assembly with 0.3.24
17_real_workbuddy_required: NO for assembly/lifecycle; B04/B05 consume it for real client proof
18_official_control_group: NO (control group is B04)
19_involves_0_3_24: YES, read-only immutable source/candidate; no bytes modified
20_proves_after_completion: Final package assembly, private toolchain, lifecycle, binding carrier and production Registration/Activation facts
21_cannot_prove_after_completion: WorkBuddy actually reading Guide, production decisions, real receipt/Artifact or business portrait E2E
```

### B04 official fixed control-group real acceptance

```text
01_task_id: V2-ARCH-RECOVERY-B04-OFFICIAL-FIXED-CONTROL-ACCEPTANCE
02_confirmed_issue: No independent real WorkBuddy evidence connects the final Shell/Skill/PackageRoot to Guide-read, fixed child facts and receipt/Artifact
03_why_correction_necessary: A known-working official Package is the control variable needed to distinguish Shell/Installer/WorkBuddy defects before switching to 0.3.24
04_correct_owner: Independent WorkBuddy integration Worker plus independent zero-write Reviewer and business-evidence owner
05_authoritative_inputs: B03 final assembly; fixed official audit checkout D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-audit-4eab34c5 at 4eab34c5cfcccaa4f1970554928feccce73ee930; B01/B02 contracts; WorkBuddy client contract
06_exact_allowed_paths: D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-audit-4eab34c5\ (read-only fixed official control); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_final_assembly\ (read-only B03 output); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B04_official_evidence\ (fresh evidence root); WorkBuddy client external state only
07_concrete_actions: Fresh install/register/activate; new-process Locator; verify Guide identity/hash; observe WorkBuddy Guide-read and decision path; invoke fixed child through same Shell; capture source/hash/argv/cwd/stdin/stdout/stderr/spawn/retry/cancel/timeout/receipt/Artifact evidence
08_explicitly_not_do: No reuse of stale PackageRoot/Registration; no model or child self-report as authority; no Shell/Skill/Installer modification during acceptance; no 0.3.24 modification; no Provider/media expansion
09_output_contract: Independently reviewable official-control evidence bundle with fresh identities, observable Guide-read, fixed child facts, one spawn/zero retry and real LauncherReceipt/Artifact
10_positive_tests: Fresh lifecycle; new-process locate; expected Guide/hash; success, cancellation and timeout semantics; receipt/Artifact consistency; spawn=1/retry=0
11_negative_tests: Wrong Guide/hash; wrong Package/Registration; missing tool; extra spawn/retry; unobserved Guide-read; receipt without child facts; reused state
12_independent_reviewer_checks: Zero-write review of evidence timestamps/identities and client observations; correlate exact package/Shell commits; reject self-report and stale state
13_p0_p1_p2_standard: P0 false real-integration claim, wrong package or second control plane; P1 missing independent Guide-read/receipt/child fact; P2 evidence correlation or cleanup defect
14_fail_closed_conditions: Fresh root/registration unavailable; official commit mismatch; Guide-read not observable; any missing final exit/cwd/stdout/stderr/timeout fact; spawn/retry mismatch; truncated output
15_upstream_dependency: B03 complete and reviewed; official fixed checkout verified read-only
16_downstream_handoff: B05 only; same Shell/assembly/Skill/Launcher/method must be retained
17_real_workbuddy_required: YES
18_official_control_group: YES / fixed commit 4eab34c5cfcccaa4f1970554928feccce73ee930
19_involves_0_3_24: NO
20_proves_after_completion: Real WorkBuddy/client integration path and evidence with the official control Package
21_cannot_prove_after_completion: Compatibility with 0.3.24, final business portrait gate, broad production scale or Stage6 relay
```

### B05 保持 Shell 不变切换 0.3.24

```text
01_task_id: V2-ARCH-RECOVERY-B05-SAME-SHELL-0_3_24-SWITCH
02_confirmed_issue: 0.3.24 identity was verified but its missing adapter was misclassified as a shared Package defect; same-Shell compatibility has not been proven
03_why_correction_necessary: Only a controlled one-variable Package switch can show whether the final Shell/Installer/Skill path works with the immutable 0.3.24 candidate
04_correct_owner: Independent Package-switch acceptance Worker and independent zero-write Reviewer
05_authoritative_inputs: B04 approved control evidence and exact Shell/Installer/Skill/Launcher/request/method; 0.3.24 candidate ef5f5b58fa1c2b494b0154989cf0e4e36615a701; B01 binding contract
06_exact_allowed_paths: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B05_0.3.24_evidence\ (fresh evidence root); D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_final_assembly\ (read-only assembly); blazingcd/golden-key-openmontage@ef5f5b58fa1c2b494b0154989cf0e4e36615a701 (read-only candidate object); WorkBuddy client external state only
07_concrete_actions: Create fresh PackageRoot/Registration; replace only the Package input; retain exact B04 Shell/Installer/Skill/Launcher/request/acceptance method; repeat Guide identity/read, fixed child, spawn/retry, receipt/Artifact evidence; compare control and candidate
08_explicitly_not_do: No Shell/Installer/Skill/Launcher/schema/request change; no reuse of B04 state; no 0.3.24 source/Release/Lock/Guide modification; no media tool selection or fixture invention
09_output_contract: Controlled comparison proving same Shell path against immutable 0.3.24, with fresh lifecycle and complete evidence or a precise fail-closed mismatch
10_positive_tests: Fresh install/register/activate/locate; same Guide-read order; same child/receipt facts; same spawn=1/retry=0; 0.3.24 subtree bytes/hash unchanged
11_negative_tests: Any changed Shell/Installer/Skill/request; stale registration; reused PackageRoot; candidate hash mismatch; mutable 0.3.24; missing Guide-read or receipt fact
12_independent_reviewer_checks: Compare B04/B05 inputs byte/commit-for-commit; verify only Package changed; check fresh roots, hashes, client observations and exact evidence
13_p0_p1_p2_standard: P0 two-variable test or Package mutation/false compatibility claim; P1 missing control comparison or real evidence; P2 non-material evidence correlation defect
14_fail_closed_conditions: B04 evidence not approved; any non-Package input differs; candidate identity/tree mismatch; fresh state unavailable; WorkBuddy evidence not independently visible
15_upstream_dependency: B04 APPROVE and retained exact control inputs
16_downstream_handoff: B06 Stage5 closeout only; no direct B07 or promotion
17_real_workbuddy_required: YES
18_official_control_group: YES / B04 retained as fixed control reference
19_involves_0_3_24: YES / read-only fixed candidate
20_proves_after_completion: Same Shell/assembly path can be evaluated against the immutable 0.3.24 candidate under controlled one-variable evidence
21_cannot_prove_after_completion: Portrait business success, all Providers/renderers, production scale, Stage6 relay or formal promotion
```

### B06 Stage 5 closeout and B07 handoff

```text
01_task_id: V2-ARCH-RECOVERY-B06-STAGE5-CLOSEOUT-HANDOFF
02_confirmed_issue: Stage5 entry-code completion was previously allowed to stand without final Package, production Registration, final Skill, real receipt and independent real integration evidence
03_why_correction_necessary: A bounded closeout must prevent another stage handoff with missing ownership/evidence and must not start Stage6 prematurely
04_correct_owner: Stage5 closeout Coordinator with independent zero-write Reviewer
05_authoritative_inputs: B03 lifecycle evidence; B04 official-control evidence; B05 0.3.24 comparison; TASK-REGISTER; PROJECT-STATE; ACCEPTANCE-MATRIX; Git/CI headSha evidence
06_exact_allowed_paths: AGENT_GUIDE.md; PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md; docs/workbuddy/v2/DRIFT-GUARD.md; D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B03_evidence\; D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B04_official_evidence\; D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B05_0.3.24_evidence\
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
19_involves_0_3_24: YES / consume B05 read-only evidence
20_proves_after_completion: Stage5 closeout readiness and a single permitted B07 handoff
21_cannot_prove_after_completion: Portrait/business gate, formal promotion, cleanup, Stage6 relay, or production scale
```

### B07 外部 portrait/business Gate D

```text
01_task_id: V2-ARCH-RECOVERY-B07-EXTERNAL-PORTRAIT-BUSINESS-GATE
02_confirmed_issue: Shell-level evidence cannot prove the final user-facing portrait Artifact or business acceptance; media/Core responsibility must remain external
03_why_correction_necessary: The original target is a natural-language business result, not only a process/receipt; the final gate must validate that result without turning Shell into media control
04_correct_owner: Independent Core/OpenMontage Owner plus independent business acceptance Owner
05_authoritative_inputs: B06 HANDOFF_TO_B07_ONLY; same approved Shell/Skill/Launcher/Installer path; Core-owned corrected Release; business acceptance contract
06_exact_allowed_paths: D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B07_portrait_evidence\ (fresh evidence root); Core Owner-designated release checkout exact absolute path and commit must be registered before start; Shell repository read-only for identity verification; WorkBuddy client external state only
07_concrete_actions: Use ordinary natural-language request; retain same Shell/Skill/Launcher; let WorkBuddy/OpenMontage choose portrait behavior; capture final portrait Artifact and independent business acceptance; correlate Package/Shell/Core identities
08_explicitly_not_do: No user-supplied technical 9:16 parameter as a substitute; no Shell media patch; no Provider/renderer hard-code; no 0.3.24 modification; no second Agent/Director; no promotion before acceptance
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
19_involves_0_3_24: YES / use only the approved immutable candidate path; never modify it
20_proves_after_completion: End-user portrait business outcome under the corrected Agent-first architecture
21_cannot_prove_after_completion: Other formats/capabilities, production scale, universal Provider behavior, or any unapproved architectural expansion
```

### A7 当前候选状态与推广边界

```text
a7_candidate_scope: SIX_EXISTING_DOCS_ONLY
a7_product_code_changes: 0
a7_test_code_changes: 0
a7_ci_changes: 0
a7_package_or_external_repo_changes: 0
a7_client_provider_media_registration_activation: 0
a7_verification_label: NOT_RUN_DOCS_ONLY
a7_reviewer: INDEPENDENT_ZERO_WRITE_REQUIRED
a7_promotion: USER_APPROVAL_REQUIRED / ORDINARY_FAST_FORWARD_ONLY
```

Reviewer APPROVE 不等于正式推广。只有 B07 完成、用户明确批准推广且最新正式对象经过 exact commit/tree/CI headSha 核验后，才允许唯一 `PROMOTE_AND_CLEANUP`；不得 merge/rebase `main`、force-push、修改 0.3.24，亦不得未经单独授权删除旧 Stage 2 分支或两个 dirty detached worktree。
