# Project State

更新时间：2026-08-22

## 当前状态

```text
product: WorkBuddy Shell V2
formal_ref: refs/heads/codex/workbuddy-shell-v2
formal_head_resolution: LIVE_REMOTE_REF_REQUIRED
formal_tree_resolution: LIVE_REMOTE_REF_TREE_REQUIRED
mirror_result: THIS_COMMIT
mirror_effect: ZERO_PRODUCT_STATE_CHANGE
mirror_repository_delivery_resolution: zero-write APPROVE exists AND LIVE_REMOTE_REF contains THIS_COMMIT
stage_1: PASS_ACCEPTED
stage_2_registration_implementation: PASS_ACCEPTED
stage_2_temporary_package_validation: PASS_ACCEPTED
final_package_artifact: NOT_MATERIALIZED
production_package_registration: NOT_CREATED
repository_hygiene: PASS_ACCEPTED
repository_tracked_files: 40
stage_3_implementation: PASS_ACCEPTED / a3f8959682d296301dc573c2835f8c705a52e8b2
stage_3_closeout: PASS_ACCEPTED / 7c15aae4e77c579309312b21c79076f930970214
stage_3_evidence: 55 direct / 10 hygiene / 199 full / all exit 0 / no skip
stage_3_evidence_boundary: no real third-party or mainland-mirror download, production DataRoot, WorkBuddy, Stage4, Provider, media or video E2E proof
ci_stage3_state_assertion_fix: FORMAL / e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3 / exactly two assertions in tests/workbuddy/test_repository_hygiene.py
ci_stage3_state_assertion_evidence: run 32218904419 / completed / success / 198 passed / 1 skipped / final exit 0
ci_stage3_state_assertion_review_history: first independent review INCOMPLETE / P0=0 / P1=0 / P2=0 / authority mismatch only / code diff no finding
ci_stage3_state_assertion_governance_deviation: formal advanced before authority closeout / history retained / current mirrors only are being repaired
stage_4_plan_formal_result: 5cb3f585a0cddffbd823c785b1d39ebd1834c1df / tree 144df76b3a307fa8944ccd7bd384bddb1b340516
stage_4_plan_promotion: ORDINARY_FAST_FORWARD / origin/codex/workbuddy-shell-v2=5cb3f585a0cddffbd823c785b1d39ebd1834c1df
stage_4_plan_review: V2-S4-PLAN-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_plan_review_history: two REQUEST_CHANGES rounds closed definition hash-cycle, receipt outcome/priority/invalid-input, forged-summary evidence, and managed/explicit/PATH handoff findings
stage_4_plan_ci: run 32337744225 / completed / success
embedded_plan_candidate_labels: HISTORICAL_CONDITIONAL_TEXT / review-and-promotion conditions satisfied by V2-S4-PLAN-REVIEW1 APPROVE and formal result 5cb3f585a0cddffbd823c785b1d39ebd1834c1df / not live authorization
stage_4_plan_closeout: PASS_ACCEPTED / dfd97f3d2e05a4c448448fc14514d1cfe76836e8 / tree 5eeb8a9337c5b38be60d3b0cef184b8898f2fedc
stage_4_plan_closeout_review: V2-S4-PLAN-CLOSEOUT-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_plan_closeout_ci: run 32338998075 / completed / success / head_sha=dfd97f3d2e05a4c448448fc14514d1cfe76836e8
stage_4_planning: PASS_ACCEPTED
stage_4_implementation_authorization_formal_result: 2c3d87bedfa4a3cef3cfd952641199300f2715dc / tree c196dbf6b094cad05076d01ac2496f7425cf6fac
stage_4_implementation_authorization_review: V2-S4-IMPLEMENTATION-AUTHORIZATION-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_implementation_authorization_ci: run 32340096961 / completed / success / head_sha=2c3d87bedfa4a3cef3cfd952641199300f2715dc
stage_4_implementation_authorization: CONSUMED_COMPLETE
stage_4_implementation_formal_result: fa9adb8470ab94b88ec9900ede03cb26f7de0ebd / tree 0809d1c4cccc9838180a016c75320b0d9fbce28a / exact five paths / tracked 35->37
stage_4_implementation_review: V2-S4-IMPLEMENTATION-REVIEW1 / EIGHTH_ROUND_APPROVE / P0=0 / P1=0 / P2=0
stage_4_implementation_first_formal_ci: run 32367792637 / failed / test-fixture-only pyvenv.cfg assumption under setup-python / no production Launcher finding
stage_4_ci_fixture_fix_formal_result: 13a3227b0c55bbe9039b46d7e92eba822b48f57e / tree d3ac89ec89b66789cabe92d94c3e827f9c2cc22f / tests/workbuddy/test_session_launcher.py only
stage_4_ci_fixture_fix_review: APPROVE / P0=0 / P1=0 / P2=0
stage_4_formal_ci: run 32369588814 / Ubuntu 24.04 / Python 3.11.16 / success / 357 passed / 1 skipped / exit 0
stage_4_windows_evidence: 158 direct / 11 hygiene / 358 combined / all exit 0 / no skip
stage_4_implementation: PASS_ACCEPTED
stage_4_closeout_formal_result: b63d8c2bc2214bc39f18378dbe47057ef538301e / tree 02814c6a4a483913e7b1abe3e9ee6d025236c951
stage_4_closeout_review: V2-S4-IMPLEMENTATION-CLOSEOUT-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_closeout_ci: run 32371507874 / Ubuntu 24.04 / Python 3.11.16 / success / 357 passed / 1 skipped
stage_4_wsl_boundary: NO_RUNTIME_DEPENDENCY / temporary Linux-equivalence validation only / cleaned and shut down after testing
final_handoff_hygiene_formal_result: 4636e27a62aad9f1b721e6c482e34b44d350503c / tree fdf24f8450ac4bb48e5337cd7aa3477794796d19 / exact six paths / tracked 37
final_handoff_hygiene_review: independent zero-write Reviewer / APPROVE / P0=0 / P1=0 / P2=0
final_handoff_hygiene_local_evidence: Python 3.14.7 / 11 hygiene passed / 358 combined passed / all final exit 0
final_handoff_hygiene_ci: run 32386393634 / completed / success / Python 3.14.7 / 357 passed / 1 skipped / actions v6 / no Node20 deprecation warning
stage_5_planning_authorization_history: V2-S5-PLANNING-AUTHORIZATION-BUILDER1 / DOCS_ONLY / CONSUMED_COMPLETE / HISTORICAL_FORMALLY_PROMOTED
stage_5_planning_authorization_history_base: 67e39b345df954898a68c9c14645c9c04c380ac3 / tree c6bf74231434850fda07722ab9eed701797e48ff / tracked 37
stage_5_planning_authorization_history_branch: codex/v2-s5-planning-authorization1
stage_5_planning_authorization_history_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md
stage_5_planning_authorization_history_result: 042686039386a63866eba2f964f1fa9674bbec4b / tree 6d6f3f0352eeb75c57170f2fe9e854c79564416c / ordinary fast-forward / FORMALLY_PROMOTED
stage_5_planning_authorization_history_consumption: V2-S5-PLAN-BUILDER1 / CURRENT_PLANNING_DOCUMENT_CANDIDATE / AUTHORIZATION_CONSUMED
stage_5_planning_authorization_history_scope: DOCS_ONLY / no production code / tests / CI / Package / real WorkBuddy / Launcher / Provider / media / WSL
initial_product_goal_recheck: PASS / WorkBuddy is the only running Agent and the only user entry; after loading the verified Package Guide it assumes the OpenMontage logical production role
stage_5_t1_cli_boundary: CLI_NOT_A_BLANKET_BAN / forbid a second entry, parallel control plane, fallback, or arbitrary command/argv/Shell generation; a fixed CLI used internally by the one official WorkBuddy Skill remains eligible for controlled contract verification
stage_5_planning_t1_hard_stop: HISTORICAL_EXTERNAL_CONTRACT_STOP / superseded for the external-mechanism question; never fabricate an interface or use CLI/MCP/second-Skill fallback, and do not treat CLI presence alone as architecture unavailability
stage_5_planning_t1_current_state: HISTORICAL_PRE_CLOSEOUT_T1_STATE / SUPERSEDED_BY_V2-S5-R00 / T1_EXTERNAL_MECHANISM_CONFIRMED / INTERNAL_FIXED_CLI_BRIDGE_FROZEN_FOR_PLANNING; current live state is the Stage5 R01 formally promoted result mirror below
stage_5_t1_fixed_cli_bridge_status: FROZEN_FOR_PLANNING / one WorkBuddy-managed Skill -> one non-user-facing fixed transport adapter -> one accepted Stage4 consumer
stage_5_t1_fixed_cli_bridge_command: LOCATOR_PACKAGE_PYTHON / -I -m golden_key_openmontage_workbuddy.workbuddy_entry_cli / no console-script / no subcommands / shell=false
stage_5_t1_fixed_cli_bridge_user_message_boundary: wire canonicalization only / no NFC-NFD-trim-newline rewrite / verify Stage4 NFC+UTF-8 precondition / non-NFC exit64 / valid Unicode code-point sequence unchanged
stage_5_t1_fixed_cli_bridge_secret_boundary: stdin names/source only; values read only from fixed CLI process environment and reconstructed into Stage4 provider_environment; then Stage4 allowlisted child env only
stage_5_t1_fixed_cli_bridge_cancel_boundary: cancel_requested bool -> local threading.Event before one Stage4 call; runtime cancel/Host termination deferred to T5/implementation
stage_5_t1_fixed_cli_bridge_exit_codes: 0=one Stage4 call+fully buffered validated receipt output; 64=input/schema/identity/cancel/continuation or user_message NFC/UTF-8 precondition; 78=asset/process-env/provider-name/provenance; 70=bridge-internal or post-call receipt serialization/output validation; no other code
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
stage_5_planning_status: T1_FIXED_CLI_BRIDGE_FROZEN_FOR_PLANNING / FORMALLY_ACCEPTED
stage_5_implementation_task: V2-S5-WORKBUDDY-ENTRY-BUILDER1 / CONSUMED_COMPLETE
stage_5_implementation_formal_result: 0e7a0be65877b03fb386e1c6c6bc258c0b27db6c / tree 85c266edb7349c940e8cd45870cc0538c95726c0 / parent aa70c2cf9b6b4a29517d7354f0239ea0cdc9a5d3
stage_5_implementation_scope: EXACT_5_PATHS / tracked 37->40
stage_5_implementation_review: APPROVE / P0=0 / P1=0 / P2=0
stage_5_implementation_windows_evidence: direct 19 passed / hygiene 11 passed / full 377 passed / final exit 0
stage_5_implementation_ci: run 32489111184 / completed / success / headSha=0e7a0be65877b03fb386e1c6c6bc258c0b27db6c / Ubuntu / Python 3.14.7 / 376 passed / 1 skipped / final exit 0
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
stage_5_implementation: ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
stage_5_entry_code_formal_result: 0e7a0be65877b03fb386e1c6c6bc258c0b27db6c / tree 85c266edb7349c940e8cd45870cc0538c95726c0 / parent aa70c2cf9b6b4a29517d7354f0239ea0cdc9a5d3
stage_5_entry_code_scope: EXACT_5_PATHS / tracked 37->40
stage_5_entry_code_review: APPROVE / P0=0 / P1=0 / P2=0
stage_5_entry_code_ci: run 32489111184 / completed / success / Ubuntu / Python 3.14.7 / 376 passed / 1 skipped / final exit 0
stage_5_entry_closeout: V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1 / FORMALLY_DELIVERED_DOCS_ONLY / NOT_STAGE5_PASS
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry: ENTRY_CODE_COMPLETE / REAL_WORKBUDDY_INTEGRATION_INCOMPLETE
stage_6_status_result_relay: NOT_GRANTED
stage_5_implementation_authorization: ENTRY_CODE_RESULT_CONSUMED / R00_CONSUMED / R01_ENTRY_SURFACE_ACCEPTED / R02_BLOCKED_PACKAGE_RELEASE / EXECUTION_PROOF_DEFERRED_TO_R03_R07
current_task: NONE / NO_ACTIVE_TASK / R02_CLOSED_BLOCKED_PACKAGE_RELEASE
current_task_status: BLOCKED_PACKAGE_RELEASE / PUBLISHED_CANDIDATE_IDENTITY_VERIFIED / DOCS_ONLY_R02_CLOSEOUT
stage_4_contract_status: CLOSED_BY_FORMAL_PLAN_RESULT / PackageToolDefinitionV1 + launch_session_tool + nine-outcome immutable LauncherReceiptV1
next_authorized_task: NONE / PACKAGE_OWNER_RELEASE_BINDING_REAUTHORIZATION_REQUIRED
next_planned_task: NONE / R03-R08_NOT_STARTED_NOT_AUTHORIZED_BY_CHAIN
stage_5_t1_evidence_authorization_history: V2-S5-T1-EVIDENCE1-CLOSEOUT-AND-CONTROLLED-CLIENT-AUTHORIZATION1 / DOCS_ONLY / CONSUMED_COMPLETE / FORMALLY_PROMOTED
stage_5_t1_controlled_client_evidence_candidate: HISTORICAL_V2-S5-T1-CONTROLLED-CLIENT-EVIDENCE1 / WORKBUDDY_5.3.13 / SUPERSEDED_BY_R01
stage_5_t1_controlled_client_proved: ORIGINAL_R01 / WORKBUDDY_5.3.14 / BASELINE_SKILLS_2_RETAINED / SAFETY_SCAN_NOT_SKIPPED / TEMP_PROBE_INSTALLED_COUNT_3 / EXACT_IDENTITY=golden-key-openmontage-r01-controlled-probe_APPEARED / ISOLATED_TASK_ATTACHED_SOLE_PROBE / HY3_SELECTED / NO_NATIVE_EVENT / NO_SCRIPT_EXECUTION / NO_STDOUT_STDERR_EXIT_CWD_TIMEOUT
stage_5_t1_controlled_client_unproved: ORIGINAL_R01 / native bundled-script invocation/tool event; script stdout/stderr/final exit/cwd/timeout capture; real LauncherReceiptV1
stage_5_t1_controlled_client_cleanup: ORIGINAL_R01 / COMPLETE / USER_UNINSTALLED_TEMPORARY_SKILL / WORKBUDDY_INSTALLED_SKILLS_2 / TASK_HISTORY_RETAINED / BASELINE_SKILLS_2_UNTOUCHED / PROBE_FOLDER_AND_ZIP_DELETED
pending_next_authorized_task: NONE
next_authorized_task_condition: R02_BLOCKED_PACKAGE_RELEASE / current_task=NONE / NO_ACTIVE_TASK / next_authorized_task=NONE; only a separate Package-owner task may approve Release delivery and independently verify safe fixed tool + release-specific PackageToolDefinitionV1 + Manifest/Lock binding, after which R02 must be separately reauthorized; R03-R08 remain strict-order and unauthorized
effective_stage_4_launcher_authorization: NOT_GRANTED
effective_stage_5_workbuddy_entry_authorization: NOT_GRANTED
effective_stage_6_status_result_relay_authorization: NOT_GRANTED
effective_final_package_gate_authorization: NOT_GRANTED
final_package_artifact: NOT_MATERIALIZED
production_package_root: NOT_CREATED
production_registration_activation: NOT_CREATED
final_installed_skill: NOT_CREATED
real_workbuddy_launcher_receipt: NOT_PROVED
final_package_gate: R04/R05_FINAL_DELIVERY_OWNERSHIP / NOT_GRANTED / NOT_MATERIALIZED
stage_5_r01_original_closeout: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / FORMALLY_PROMOTED / BLOCKED_EXTERNAL_CONTRACT / COMMIT=9eefe8600d9bed0c8ea6024880e4b2d2ef4e3bfc / PRESERVED
stage_5_r01_refresh1_task: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / V2-S5-R01-WORKBUDDY-SANDBOX-REFRESH1 / CONTROLLED_CLIENT_EVIDENCE_REFRESH + DOCS_ONLY_CLOSEOUT / ZERO_PRODUCT_STATE_CHANGE
stage_5_r01_refresh1_candidate_base: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / 932bcabc5baf90d0190101b1039e4ccf087b2b08 / tree 2ed2cd0e67dd8628b7f0b1acf84df0a7d8b0d0fd / tracked 40
stage_5_r01_refresh1_product_goal_recheck: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / PASS / WorkBuddy唯一运行Agent和用户入口 / 固定CLI仅为唯一Skill内部桥梁 / no second entry or control plane
stage_5_r01_refresh1_official_contract: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / 134420=CLIENT_SANDBOX_SCRIPTS_EXECUTION_ONLY / 134432=SKILL_SCRIPTS_WORKFLOWS_UPLOAD_CALL_SHAPE / 134516=CODEBUDDY_PRODUCT_MISMATCH_NOT_CONTRACT_PROOF
stage_5_r01_refresh1_client_surface: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / POWERSHELL=ELIGIBLE_CANDIDATE_SURFACE_FROM_COORDINATOR_CLIENT_OBSERVATION / NOT_OFFICIAL_EXACT_CONTRACT
stage_5_r01_refresh1_contract_gaps: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / BUNDLED_RELATIVE_RESOURCE_RESOLUTION / SKILL_ROOT_CWD / STDIN / STDOUT / STDERR / FINAL_EXIT / TIMEOUT
stage_5_r01_refresh1_workbuddy: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / 5.3.14 / BASELINE_SKILLS_2=agent-browser,find-skills / HY3_ONLY / NEVER_AUTO
stage_5_r01_refresh1_artifacts: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / source_root=ISOLATED_D_DRIVE_TEMP_ROOT / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / CLEANUP_COMPLETE / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND / skill_sha256=A369E89912B51C1627C972A7DE8F82111E55E2909622CB2E0E3276B45331FFF9 / script_sha256=8A1D38A65945CC99C4B7F8EE95FDF4FF744D105303BC9904E5915E630DF58359 / zip_sha256=2284E6D6FE8FFD38689A357DD0A6653CEB23B923F0C531BF9EAC376178E9A28A
stage_5_r01_refresh1_install_observation: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / SAFETY_SCAN_NOT_SKIPPED / NO_NON_HIGH_RISK_AUTO_INSTALL_SELECTED / INSTALLED_COUNT_3 / CLIENT_ID=workbuddy-skill-1787379691395 / SKILL_MD_NO_METADATA_NAME / BODY_FIRST_LINE_MATCHED_PROBE
stage_5_r01_refresh1_native_read_event: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / PRESENT / SKILL_MD_AND_scripts\\r01_contract_probe.py_READ / PHYSICAL_INSTALL_PATH_EXPOSED_CONTRACT_DEVIATION_SENSITIVE_MINIMIZATION_FAILURE / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
stage_5_r01_refresh1_execution_observation: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / SESSION_WORKSPACE_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / FROZEN_RELATIVE_SCRIPT_NO_CD_NO_ABSOLUTE_PATH_NO_GUESSING_NO_COMMAND_MUTATION / SKILL_ROOT_CWD_NOT_EXPOSED / BUNDLE_RELATIVE_INVOCATION_NOT_EXPOSED / POWERSHELL_NOT_STARTED
stage_5_r01_refresh1_evidence: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / USER_CANCELLED / NO_SCRIPT_EXECUTION / NO_STDOUT_STDERR_FINAL_EXIT_CWD_CLASSIFICATION_TIMEOUT
stage_5_r01_refresh1_result: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / BLOCKED_EXTERNAL_CONTRACT / MISSING_SKILL_ROOT_CWD_AND_BUNDLE_RELATIVE_RESOLUTION / NOT_BECAUSE_POWERSHELL_IS_NON_NATIVE
stage_5_r01_refresh1_review: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_REVIEWER
stage_5_r01_refresh1_reviewer_independent_observation: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / WORKBUDDY_5.3.14 / HY3 / USER_CANCELLED / NO_SUCCESS_STDOUT_STDERR_EXIT_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
stage_5_r01_refresh1_cleanup: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / COMPLETE / USER_UNINSTALLED_TEMPORARY_SKILL / TEMP_SKILL_ID=workbuddy-skill-1787379691395_NOT_IN_INSTALLED_LIST / WORKBUDDY_MY_INSTALLED_SKILLS_2=agent-browser,find-skills / TASK_HISTORY_RETAINED / BASELINE_SKILLS_2_UNTOUCHED / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND
stage_5_r01_refresh1_nonzero_timeout: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / NOT_RUN / R02-R08_NOT_STARTED_NOT_AUTHORIZED_BY_CHAIN
stage_5_r01_refresh1_computer_use_transparency: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / LOW_IMPACT_OPERATIONAL_ANOMALY / EXISTING_EXPLORER_MISTAKEN_FOR_FILE_PICKER / ALT+N_MAY_OPEN_TAB_OR_WINDOW / NO_PATH_INPUT_NO_FILE_SELECTION_NO_WRITE_DELETE / STOPPED_AND_RECOVERED
stage_5_r01_refresh1_candidate_test: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / NOT_RUN_DOCS_ONLY / candidate_product_code_changes=0 / candidate_test_changes=0 / candidate_ci_changes=0 / candidate_external_product_state_changes=0
stage_5_r01_refresh1_accepted_result: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / 6c20371f1c72ee9d55147e1ad7feb8ede201858f / tree 9eb4643f09d03cc9f39b0b46906773e5bcc9125d / DOCS_REVIEW=APPROVE_P0_0_P1_0_P2_0
stage_5_r01_refresh1_candidate_push: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / FORMALLY_EFFECTIVE_IFF_LIVE_REMOTE_REF_CONTAINS_THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR
stage_5_expert_entry_feasibility1: HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / INCOMPLETE / EXPERT_AS_SOLE_VISIBLE_ENTRY_NOT_PROVED / DOES_NOT_SUPERSEDE_SOLE_SKILL_ENTRY / R01_UNCHANGED_BLOCKED_EXTERNAL_CONTRACT
stage_5_expert_entry_feasibility1_official_contract: EXPERT_IS_WORKBUDDY_ROLE_LAYER / SKILL_OR_MCP_CAN_PROVIDE_INDIRECT_FILE_OR_EXTERNAL_SERVICE_ACCESS / NO_OFFICIAL_PROOF_EXPERT_CAN_REPLACE_EXECUTABLE_SKILL
stage_5_expert_entry_feasibility1_client: WORKBUDDY_5.3.14 / HY3_ONLY / MY_EXPERT_COUNT=0 / CREATE_ENTRY_OPENED_EXPERT_MANAGER_CONVERSATION / NO_EXPERT_CREATED_SAVED_OR_PUBLISHED
stage_5_expert_entry_feasibility1_expert_manager_observation: CANNOT_DIRECTLY_BIND_INSTALLED_SKILL / CANNOT_LOCK_HY3 / SAME_CONVERSATION_MAY_PROMPT_GLOBAL_SKILL / BUNDLED_AUTOLOAD_NOT_PROVED
stage_5_expert_entry_feasibility1_self_report_boundary: MODEL_OR_BUILTIN_SKILL_SELF_REPORT_NOT_OFFICIAL_CONTRACT
stage_5_expert_entry_feasibility1_review: APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_REVIEWER
stage_5_expert_entry_feasibility1_anti_expansion: PASS / NO_EXPERT_OR_PACKAGE_OR_SKILL_CREATED / NO_NEW_R01_GATE / NO_PROVIDER_MEDIA_PACKAGE_STAGE4_STAGE6_OR_PRODUCTION
stage_5_expert_entry_feasibility1_current_task: HISTORICAL / NONE / NO_ACTIVE_TASK
stage_5_expert_entry_feasibility1_next_authorized_task: HISTORICAL / NONE / R02-R08_NOT_STARTED_NOT_AUTHORIZED_BY_CHAIN
stage_5_r01_acceptance_correction1: HISTORICAL / CONSUMED_BY_V2-S5-R02 / ENTRY_SURFACE_ACCEPTED / EXECUTION_PROOF_DEFERRED_TO_R03_R07 / USER_AUTHORIZED_PROJECT_ACCEPTANCE_CORRECTION / NOT_NEW_OFFICIAL_EVIDENCE
stage_5_r01_acceptance_correction1_entry_surface_evidence: HISTORICAL / CONSUMED_BY_V2-S5-R02 / SKILL_PACKAGING / UPLOAD / INSTALL / IDENTITY_APPEARED / SELECTION_HIT / CLIENT_SANDBOX_SCRIPTS / POWERSHELL_ELIGIBLE_CANDIDATE_SURFACE
stage_5_r01_acceptance_correction1_deferred_unproved_contract: HISTORICAL / CONSUMED_BY_V2-S5-R02 / SKILL_ROOT_CWD / BUNDLED_RELATIVE_RESOURCE_RESOLUTION / STDIN / STDOUT / STDERR / FINAL_EXIT / TIMEOUT / NOT_R01_HARD_GATE / DEFERRED_TO_R03_R07
stage_5_r01_acceptance_correction1_execution_chain: HISTORICAL / CONSUMED_BY_V2-S5-R02 / LOCATOR -> FIXED_POWERSHELL_OR_PRIVATE_CLI -> LAUNCHER_RECEIPT / IMPLEMENTATION_AND_REAL_PROOF_DEFERRED_TO_R03_R07 / NOT_CURRENTLY_PROVED
stage_5_r01_acceptance_correction1_no_overclaim: HISTORICAL / CONSUMED_BY_V2-S5-R02 / NO_SCRIPT_EXECUTION_PROOF / NO_STDOUT_STDERR_EXIT_CWD_TIMEOUT_PROOF / NO_LAUNCHER_RECEIPT_PROOF / NOT_STAGE5_PASS
stage_5_r01_acceptance_correction1_hy3_policy: HISTORICAL / CONSUMED_BY_V2-S5-R02 / CURRENT_TEST_MODEL_ONLY / COST_AVOIDANCE / PRODUCT_MODEL_NEUTRAL / USER_SELECTED_MODEL / NOT_A_SKILL_OR_EXPERT_OR_SYSTEM_DEPENDENCY
stage_5_r01_acceptance_correction1_boundaries: HISTORICAL / CONSUMED_BY_V2-S5-R02 / ONE_WORKBUDDY_SKILL_AND_ONE_USER_ENTRY / FIXED_CLI_INTERNAL_BRIDGE_ONLY / NO_ARBITRARY_CLI / NO_PATH_GUESSING / NO_SCAN / NO_PATH_FALLBACK / NO_MCP / NO_SECOND_SKILL / NO_SECOND_AGENT / NO_ROUTER / NO_RETRY / NO_REPLAY / FINAL_SKILL_INSTALLER_STAMPED_LOCATOR
stage_5_r01_acceptance_correction1_review_state: HISTORICAL / CONSUMED_BY_V2-S5-R02 / PENDING_INDEPENDENT_REVIEW / DOCS_ONLY_CANDIDATE
stage_5_r01_acceptance_correction1_current_task: HISTORICAL / CONSUMED_BY_V2-S5-R02 / NONE / NO_ACTIVE_TASK / R01_CORRECTED_ACCEPTED_ENTRY_SURFACE
stage_5_r01_acceptance_correction1_next_authorized_task: HISTORICAL / CONSUMED_BY_V2-S5-R02 / V2-S5-R02-PACKAGE-RELEASE-TOOL-DEFINITION-BINDING1 / R02_AUTHORIZED_ONLY / R03-R08_NOT_AUTHORIZED_BY_CHAIN
stage_5_r02_package_release_tool_definition_binding1: BLOCKED_PACKAGE_RELEASE / PUBLISHED_CANDIDATE_IDENTITY_VERIFIED / MISSING_SAFE_FIXED_TOOL_AND_RELEASE_SPECIFIC_DEFINITION
stage_5_r02_published_candidate: blazingcd/golden-key-openmontage / branch=codex/golden-key-openmontage-v0.3.24 / published_commit=ef5f5b58fa1c2b494b0154989cf0e4e36615a701 / published_root_tree=0464861c5985c7c9072e789b94889d29cf9a937a / approved_source_commit=8395e578165e802990d53fef5a166f8b4cf0461a / approved_source_commit_tree=4624394238802a9577690248e43b8f0dff391a2b / approved_source_package_subtree=0464861c5985c7c9072e789b94889d29cf9a937a
stage_5_r02_tree_audit: REMOTE_RECURSIVE_TRUNCATED_FALSE / entries=2614 / binding_path_filter=(workbuddy|package.?tool.?definition|launcher|fixed.?tool|entry.?cli) / binding_related_paths=0 / local_same_tree_blobs=2155
stage_5_r02_release_metadata: GOLDEN_KEY_OPENMONTAGE_RELEASE.json / release_version=0.3.24 / console_script_entrypoint=null / python_load_probe=lib.pipeline_loader:load_pipeline / authority_entry=README.md
stage_5_r02_lock_metadata: GOLDEN_KEY_OPENMONTAGE.lock.json / NO_PackageToolDefinitionV1 / NO_workbuddy_entry_cli / NO_package_tool_definition / NO_launcher / NO_fixed_tool / NO_CORRESPONDING_TOP_LEVEL_FIELDS
stage_5_r02_no_overclaim: PUBLISHED_CANDIDATE_EXISTS_AND_IDENTITY_MATCHES / NOT_BINDABLE_FINAL_RELEASE / NO_ARBITRARY_MEDIA_TOOL_SELECTION / NO_FIXTURE_OR_DEFINITION / NO_EXTERNAL_PACKAGE_MODIFICATION
stage_5_r02_preserved_r01_hy3_policy: R01_ENTRY_SURFACE_ACCEPTED / HY3_CURRENT_TEST_MODEL_ONLY / COST_AVOIDANCE / PRODUCT_MODEL_NEUTRAL / USER_SELECTED_MODEL / NOT_A_SKILL_OR_EXPERT_OR_SYSTEM_DEPENDENCY
stage_5_r02_product_goal_anti_expansion: PASS / WorkBuddy_ONLY_AGENT_USER_ENTRY / FIXED_CLI_ONLY_SOLE_SKILL_INTERNAL_BRIDGE / NO_CLIENT_PACKAGE_REGISTRATION_STAGE4_PROVIDER_MEDIA_STAGE6_OR_PRODUCTION
stage_5_r02_current_task: NONE / NO_ACTIVE_TASK / R02_CLOSED_BLOCKED_PACKAGE_RELEASE
stage_5_r02_next_authorized_task: NONE / PACKAGE_OWNER_RELEASE_BINDING_REAUTHORIZATION_REQUIRED / R03-R08_NOT_AUTHORIZED_BY_CHAIN
stage_5_r02_unblock_condition: SEPARATE_PACKAGE_OWNER_APPROVAL_AND_INDEPENDENT_VERIFICATION_OF_SAFE_FIXED_TOOL_RELEASE_SPECIFIC_DEFINITION_MANIFEST_LOCK_BINDING / THEN_REAUTHORIZE_R02
```

## [HISTORICAL / SUPERSEDED_BY_FIXED_CLI_BRIDGE_CONTRACT] Stage 5 T1 CLI边界纠偏与目标回读门禁（2026-08-21）

本节是对上一轮 `V2-S5-T1-CONTRACT-CLOSURE-EVIDENCE2` 候选的 **superseding docs-level correction**，现明确为 `HISTORICAL / SUPERSEDED_BY_FIXED_CLI_BRIDGE_CONTRACT`。历史证据、候选提交和当时的 `ARCHITECTURE_CONTRACT_UNAVAILABLE` 文字均保留，不伪造或重写历史；其中的 `IN_PROGRESS / T1_INTERNAL_BRIDGE_CONTRACT_PENDING`、direct Python 当前候选和下一步固定 CLI 计划只作审计事实，不是 live authority。当前 live 以顶部字段及下方固定 CLI 桥梁镜像为准：`T1_FIXED_CLI_BRIDGE_FROZEN_FOR_PLANNING`，下一任务为窄 docs-only `V2-S5-PLANNING-CLOSEOUT-IMPLEMENTATION-HANDOFF-ASSESSMENT1`。

```text
initial_product_goal_recheck: PASS
initial_product_goal: Tencent WorkBuddy is the only running Agent and the only user entry; after loading the verified Golden Key OpenMontage Package Guide, WorkBuddy assumes the OpenMontage logical production role
product_goal_priority: product goal and official evidence outrank a candidate implementation preference
cli_rule: CLI is not prohibited merely because it is CLI
cli_allowed_condition: an officially supported fixed CLI may be an internal bridge invoked by the one WorkBuddy Skill, only if it remains within that Skill's single-entry/single-consumer contract and is directly evidenced and frozen
cli_forbidden_conditions: second user entry; parallel control plane; second Agent; fallback after an unsupported contract; arbitrary command/argv/Shell generation; unbounded intent interception; automatic retry/replay
mcp_rule: MCP is not an authorized second entry or parallel control plane; no MCP bridge is assumed without separate official contract evidence
t1_reopened_decision: REASSESS_OFFICIAL_SKILL_PLUS_FIXED_CLI_UNIQUE_ENTRY_CONTRACT
t1_blocker_meaning: historical external-contract wording is superseded for the mechanism question; current state is IN_PROGRESS / T1_INTERNAL_BRIDGE_CONTRACT_PENDING, and it does not mean the product or an internal fixed CLI bridge is impossible
t4_direct_python_rule: accepted Stage 4 implementation and launch_session_tool(...) contract remain PASS_ACCEPTED; direct Python is the current Stage 5/T1 consumption candidate; if official evidence identifies a fixed internal CLI bridge, compare and reconcile the Stage 5 binding under T1 rather than reopening or denying Stage 4 or the product goal
t4_preserved_boundary: Stage 5 still must not generate arbitrary command/argv/Shell strings or create a second control plane; any fixed bridge must be consumed only as its evidenced contract
stage_5_implementation_authorization: NOT_GRANTED
next_authorized_task_after_correction: V2-S5-T1-FIXED-CLI-BRIDGE-CONTRACT-PLAN1 / only after this reassessment is independently approved and ordinarily fast-forwarded
next_task_scope: reread initial product goal; recheck official Skill plus fixed-CLI internal bridge and its unique consumer/entry boundary; reconcile with Stage 4 without code or production execution
next_task_forbidden: second entry; second Agent; CLI/MCP fallback or parallel control plane; arbitrary command/argv/Shell; code; tests; CI; Provider; media; Package; Registration; Stage4 real spawn; Stage6
recheck_gate_for_every_future_stage5_task: initial_product_goal_recheck=PASS is mandatory before task start, evidence裁决, or implementation decision
```

该纠偏不使 Stage 5 规划或实现自动 `PASS_ACCEPTED`，也不授权真实 WorkBuddy/Stage 4/Provider/媒体/Package/Stage 6。当前外部机制已由官方 `Skill + CLI` 资料和既有 HY3 exact Skill 会话确认；剩余固定 CLI identity/envelope/Stage4 mapping 是下一项窄 docs-only 内部合同规划，不再作为外部机制阻断。它把 T1 从“CLI 存在即否定”纠正为“在唯一 Skill 内冻结受控固定 CLI 桥梁”。

## Stage 5 规划授权历史记录（2026-08-21）

本节只记录用户对 Stage 5 规划文档固化的授权，不授权 Stage 5 实现、真实 WorkBuddy 运行或任何 Package/Provider/媒体工作。该授权已随 `042686039386a63866eba2f964f1fa9674bbec4b` 的普通 fast-forward 正式推广，并由当前 `V2-S5-PLAN-BUILDER1` 规划候选消费完成；以下是历史记录，不是当前任务或下一授权。当前四文档候选即使未来经独立零写 Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 并普通 fast-forward，也只正式固化规划文档，不使规划达到 `PASS_ACCEPTED`，不授权 Stage 5 实现；T1 外部合同未闭合时，实时规划仍为 `PLANNING_BLOCKED_EXTERNAL_CONTRACT`。

```text
task_id: V2-S5-PLANNING-AUTHORIZATION-BUILDER1
task_kind: STAGE5_PLANNING_AUTHORIZATION / DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE
task_status: CONSUMED_COMPLETE / HISTORICAL_FORMALLY_PROMOTED
user_authorization: 2026-08-21 / 固化 Stage 5 T1-T12 规划执行边界并准备正式开启规划任务
start_commit: 67e39b345df954898a68c9c14645c9c04c380ac3
start_tree: c6bf74231434850fda07722ab9eed701797e48ff
tracked_files_at_start: 37
candidate_branch: codex/v2-s5-planning-authorization1
formal_target_branch: origin/codex/workbuddy-shell-v2
candidate_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md
formal_promotion_result: 042686039386a63866eba2f964f1fa9674bbec4b / tree 6d6f3f0352eeb75c57170f2fe9e854c79564416c / ORDINARY_FAST_FORWARD / FORMALLY_PROMOTED
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
next_task_consumption: CURRENT_PLANNING_DOCUMENT_CANDIDATE / AUTHORIZATION_CONSUMED
stage_5_planning_status_after_consumption: PLANNING_BLOCKED_EXTERNAL_CONTRACT / T1_EXTERNAL_CONTRACT_UNCLOSED
stage_5_implementation_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
final_package_gate_authorization: NOT_GRANTED
current_task_after_candidate: NONE
next_authorized_task_after_consumption: NONE
```

T1 的外部合同门禁是不可漂移的硬停止：如果官方资料或受控真实客户端证据仍不能证明真实 WorkBuddy Skill 的包结构、安装/导入归属、显式调用主体，以及不生成命令/argv/Shell 字符串即可调用 Stage 4 Python API 的精确协议，T1 必须记录为 `PLANNING_BLOCKED_EXTERNAL_CONTRACT`。不得伪造工具名、参数、Skill 结构或调用接口，不得用 CLI、MCP 或第二 Skill 作为兜底；此时规划停止在合同证据层，不进入实现授权。

该历史授权自身不构成当前任务，也不得覆盖上方实时字段。当前规划候选仍须由独立 Reviewer 和普通 fast-forward 独立治理；无论治理结果如何，T1 未闭合时不得把规划记为 `PASS_ACCEPTED` 或启动 Stage 5 实现。

## Stage 5 T1真实WorkBuddy入口合同证据核验授权候选（2026-08-21）

本节只固化用户对 T1 证据核验的授权边界，不代表 T1 证据已经完成，也不授权 Stage 5 实现、真实 WorkBuddy、Launcher、Provider、媒体、最终 Package 或 Stage 6。候选分支未进入 formal 前 `current_task=NONE`；本提交进入 formal 后，live direct authority 才生效为唯一的 `V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE1`。独立零写 Reviewer 与普通 fast-forward 仍是本候选的正式治理条件。

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

T1 只核查以下五项，不得扩展为实现设计或客户端生产验证：

1. 真实 WorkBuddy Skill 的包结构；
2. Skill 的安装/导入归属；
3. 显式调用主体和调用机制；
4. 唯一消费者，以及它与 WorkBuddy 唯一 Agent 边界的关系；
5. 不生成 CLI、MCP、命令、argv 或 Shell 字符串即可直接调用已接受 Stage 4 Python API `launch_session_tool(...)` 的精确协议。

第一阶段证据源只允许腾讯/WorkBuddy官方一手公开资料，以及本仓库已经存在的静态证据。网页证据必须记录 URL、标题、访问日期、原文直接支持的精确 claim 和仍未支持的 gap；搜索摘要、第三方文章、论坛、推测和旧 V1 Skill 均不得作为权威。旧 V1 Skill 只能标记为 `HISTORICAL/DROP`，不得复用或推导新的入口合同。

用户所说的“经另行允许的受控客户端证据”在本授权候选中冻结为 `NOT_AUTHORIZED_IN_THIS_TASK`：不得打开、操作或运行真实 WorkBuddy，不得上传、安装或调用 Skill。若官方资料不足，只能记录未来另行授权的最小客户端核验步骤及其待证明字段；本候选不得执行这些步骤。

后续唯一 Evidence Builder `V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE1` 的最大文档白名单冻结为：`PROJECT-STATE.md`、`docs/workbuddy/v2/TASK-REGISTER.md`、`docs/workbuddy/v2/PROJECT-CHARTER.md`、`docs/workbuddy/v2/ACCEPTANCE-MATRIX.md`；不得新增平行证据或规划文档，实际结果可以少改文件。Evidence Builder 只能提交 docs-only 证据候选和建议状态，必须经独立零写 Reviewer 与普通 fast-forward；即使五项均被官方资料证明，也不得自行标记 Stage 5 实现 PASS 或启动实现。

若官方资料不能同时证明五项，Evidence Builder 在 `AFTER_EVIDENCE1_COMPLETES_WITH_T1_EVIDENCE_INCOMPLETE` 时必须保持 `stage_5_planning=PLANNING_BLOCKED_EXTERNAL_CONTRACT`、`stage_5_implementation_authorization=NOT_GRANTED`、`next_authorized_task=NONE`；这不是当前 live 值，不得填造路径、接口、参数，不得授权实施。即使官方资料足以形成五项证据，仍只能记为证据候选/待独立审查，随后另行进行权威状态收口；不得从 Evidence1 自动推导 Stage 5 实现授权。

本授权候选及其后续 Evidence1 均禁止：生产代码、测试、CI、pyproject、Package 字节、Registration/Activation、真实 WorkBuddy、Launcher、Provider、Runtime 下载、媒体、WSL、Stage 6、final Package、production Registration，以及 CLI/MCP/第二 Skill/第二 Agent/并行入口。

## Stage 5 T1官方合同证据核验候选结果（2026-08-21）

本候选只固化 T1 官方资料核验结果，不宣称真实客户端证据，不授权 Stage 5 实现或生产流程。Evidence Builder 从实时 formal `44d89625c1fd71d07d1173e18681e64e7459cec2`、tree `10c8c4187299564fc83cef38a3f9ac65f4f9790a`、tracked 37 接管；受控真实客户端在本任务中为 `NOT_AUTHORIZED_IN_THIS_TASK`。

```text
task_id: V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE1
candidate_branch: codex/v2-s5-t1-official-contract-evidence1
candidate_worktree: D:\\BlazingCD\\Personal\\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2-s5-t1-evidence1
candidate_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md
candidate_result: T1_EVIDENCE_INCOMPLETE
stage_5_planning_after_candidate: PLANNING_BLOCKED_EXTERNAL_CONTRACT
stage_5_implementation_authorization_after_candidate: NOT_GRANTED
current_task_after_candidate: NONE
next_authorized_task_after_candidate: NONE
test: NOT_RUN_DOCS_ONLY
```

官方来源及五项矩阵的完整记录以 `docs/workbuddy/v2/TASK-REGISTER.md` 的同名 Evidence1 章节为任务级权威；本状态文件只镜像最终裁决。官方资料截至 2026-08-21 仅能证明 WorkBuddy 存在 Skill 导入/安装、对话选择和自动调用能力，不能证明包结构/schema、安装物理归属、当前精确入口分派、唯一消费者边界或直接调用 Stage 4 Python API 的参数/receipt 协议。五项未全部 `PROVED_OFFICIAL`，因此不得填造任何路径、文件、入口名、参数或返回值，也不得使用 CLI/MCP/旧 V1 Skill 补缺。

未来若要继续，只能另行授权最小受控客户端验证卡：全新会话和隔离工作区、最小无生产副作用 candidate Skill、显式导入/命中、可观察安装归属、唯一消费者、无命令/argv/Shell 的 Python 直调探针、完整 receipt 对照、Provider/媒体/Package/Stage4真实spawn为0，以及另行授权的证据保存/清理。该验证卡本候选只记录不执行。

## Stage 5 T1受控真实WorkBuddy客户端证据授权候选（2026-08-21）

本节只固化 Evidence1 收口后的下一项受控客户端证据授权，不表示客户端证据已经取得，也不授权 Stage 5 实现、真实 Launcher、Provider、媒体、最终 Package 或 Stage 6。候选进入 formal 前 `current_task=NONE`、`next_authorized_task=NONE` 仅为历史/授权前状态；只有本候选经独立零写 Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 并普通 fast-forward 进入 formal 后，顶部 live direct 才生效为唯一的 `V2-S5-T1-CONTROLLED-CLIENT-EVIDENCE1`。

```text
task_id: V2-S5-T1-EVIDENCE1-CLOSEOUT-AND-CONTROLLED-CLIENT-AUTHORIZATION1
task_kind: STAGE5_T1_EVIDENCE1_CLOSEOUT_AND_CONTROLLED_CLIENT_AUTHORIZATION / DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE
user_authorization: 2026-08-21 / 授权执行T1 Evidence1两文档机械收口，并启动受控真实WorkBuddy客户端证据核验；仅允许隔离工作区和临时无副作用Skill，禁止Provider、媒体、最终Package和Stage4真实spawn，额外权限必须停止。
base_commit: d11513907c3662b18fd06a200fac935efcb50055
base_tree: 81e38bc90dd37d586b46e20cc047db35b613759d
tracked_files_at_base: 37
candidate_branch: codex/v2-s5-t1-client-evidence-authorization1
candidate_worktree: D:\\BlazingCD\\Personal\\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2-s5-t1-client-auth1
candidate_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md
candidate_production_code_changes: 0
candidate_test_changes: 0
candidate_ci_changes: 0
candidate_external_writes: NONE
candidate_real_workbuddy_execution: NOT_PERFORMED_IN_THIS_AUTHORIZATION_TASK
candidate_test: NOT_RUN_DOCS_ONLY
current_task_before_promotion: NONE
next_authorized_task_before_promotion: NONE / HISTORICAL_PRE_AUTHORIZATION
next_authorized_task_after_promotion: V2-S5-T1-CONTROLLED-CLIENT-EVIDENCE1 / ONLY_AFTER_THIS_COMMIT_IS_FORMAL
stage_5_planning: PLANNING_BLOCKED_EXTERNAL_CONTRACT
stage_5_implementation_authorization: NOT_GRANTED
candidate_status: CANDIDATE_UNTIL_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD
```

后续受控客户端任务的边界固定如下：

- 只操作预先存在的腾讯 WorkBuddy 客户端和现有登录态。出现登录/认证界面立即停止并交用户处理，不自动认证。
- 隔离根固定为 `D:\\BlazingCD\\Temp\\Golden_Key_WorkBuddy_S5_T1_Client_Evidence1`；开始前必须核验精确绝对路径，禁止写入 C 盘或项目生产目录。
- 第一阶段只观察客户端 UI、版本、Skill 入口/创建/导入页面及可见格式说明，不猜包结构、schema、路径或入口。
- 只有客户端 UI 或官方可见模板明确给出包格式后，才可创建临时 candidate Skill。它只能返回唯一非敏感静态诊断标记并声明不执行工具；不得含脚本、命令、CLI、MCP、网络、文件读写、Python 执行、Stage 4 调用、Provider、媒体或生产逻辑。
- 观察或导航到导入/安装页面可以继续；实际“上传/导入/安装/启用”是客户端状态改变，动作当时必须再次取得用户确认后才能点击，即使已有总体授权。
- 任何登录、Windows/浏览器权限、安全或隐私设置、管理员权限、额外目录、全局安装、插件/扩展安装、外部网络/第三方服务、收费、Provider、媒体、final Package、production Registration 或 Stage 4 真实 spawn 请求，立即 `STOP`；不接受权限提示。
- 不发送敏感数据；candidate Skill 只能包含非敏感静态诊断文本；不得打开终端或通过 UI 运行命令。
- 只取证五项：Skill 包结构/schema；安装/导入归属与物理/项目级语义；显式调用主体/入口/触发；唯一消费者/唯一 Agent 边界；无 CLI/MCP/命令/argv/Shell 字符串的本地 Python 直调 `launch_session_tool(...)` 协议。客户端不能证明的项目记 `UNPROVED_CLIENT`，不得推断。
- Python 直调只允许检查 UI、模板、文档或可见合同；若需要真实 Python 执行或 Stage 4 spawn，立即停止并记录缺口。
- 证据固化只能写现有四份权威文档的后续候选：`PROJECT-STATE.md`、`docs/workbuddy/v2/TASK-REGISTER.md`、`docs/workbuddy/v2/PROJECT-CHARTER.md`、`docs/workbuddy/v2/ACCEPTANCE-MATRIX.md`，不得新增平行报告；任务完成后 `current_task=NONE`、`next_authorized_task=NONE`，除非另行授权。
- 证据固化后清理临时 Skill 和隔离工作区；删除若触发 Windows UI 确认，必须在动作当时重新确认，或仅对已核验精确 D 盘路径执行项目规则允许的清理。正式文档只保留非敏感文字证据。

本授权候选本身仍只修改 `PROJECT-STATE.md` 与 `TASK-REGISTER.md`，不打开 WorkBuddy、不创建/上传/安装 Skill、不运行代码/测试/CI/Launcher/Provider/媒体/WSL，不物化 Package、不创建 Registration、不启动 Stage 6；后续客户端任务须在本候选正式推广后，按顶部唯一 `next_authorized_task` 单独接管。

## Stage 5 T1受控真实WorkBuddy客户端证据候选结果（2026-08-21）

本候选从正式授权对象 `5c7d76190be4cb76afafb5d32798219e09630153`、tree `9f042420ed82ac01ffacabc650cb2a0a42a49c74`、tracked 37 接管，只核查 `V2-S5-T1-CONTROLLED-CLIENT-EVIDENCE1`。隔离根为 `D:\\BlazingCD\\Temp\\Golden_Key_WorkBuddy_S5_T1_Client_Evidence1`，candidate Skill 为唯一临时无副作用入口；用户在取证前已自行卸载两个旧 V1 Skill，该用户动作不作为新入口实现证据。未运行生产代码、测试、CI、Provider、媒体、最终 Package、production Registration、Stage 4 真实 spawn、Python、CLI 或 MCP。

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
candidate_skill: golden-key-s5-t1-noop-evidence
candidate_skill_zip_sha256: 08AA43E11DD1BBBABA53A8DED33B60FB7E4FF0B26129800974F61342A8F4EBB5
hy3_invocation_result: T1_CONTROLLED_NOOP_OK / completed 8s / response labeled Hy3
auto_probe_result: T1_CONTROLLED_NOOP_OK / EXCLUDED_FROM_FINAL_MODEL_EVIDENCE / response labeled Auto (GLM-5.2)
permission_or_risk_prompt: NONE_OBSERVED
provider_media_final_package_stage4_spawn: NOT_RUN
candidate_result: T1_CLIENT_EVIDENCE_INCOMPLETE
stage_5_planning: PLANNING_BLOCKED_EXTERNAL_CONTRACT
stage_5_implementation_authorization: NOT_GRANTED
current_task_after_candidate: NONE
next_authorized_task_after_candidate: NONE
cleanup_status: COMPLETE / USER_UNINSTALLED_TEMPORARY_SKILL / CLIENT_INSTALLED_SKILLS_0 / D_DRIVE_ISOLATION_RECYCLED / SOURCE_PATH_ABSENT
candidate_status: CANDIDATE_UNTIL_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD
```

客户端直接证明：上传页接受“包含 `SKILL.md` 的文件夹或 `.zip`”，并要求 `.md` 的 YAML 含 Skill 名称与描述；未勾选跳过检测时客户端完成安全检测后自动安装；“我安装的”从 0 变为 1，且显示 YAML 中的名称与描述；新任务输入框明确提示“`/` 调用技能与指令”；发送 `/golden-key-s5-t1-noop-evidence` 后，消息被识别为该 Skill、界面显示“加载技能 golden-key-s5-t1-noop-evidence”，在明确选择 `Hy3` 后 8 秒精确返回 `T1_CONTROLLED_NOOP_OK`，响应底部标注 `Hy3`。第一次 Auto 调用只保留为探测历史，不计入最终 HY3 证据。

客户端仍未证明完整 Skill schema/可选目录树、安装后的物理路径和完整用户级/workspace级/项目级归属、全局唯一消费者及不存在其他 dispatch，也未给出不生成 CLI/MCP/命令/argv/Shell 字符串的本地 Python 模块直调 `launch_session_tool(...)` 与逐字段回传 `LauncherReceiptV1` 的合同。第五项依授权禁止真实 Python/Stage 4 spawn，因此保持 `UNPROVED_CLIENT`。五项没有全部闭合，T1 结果仍为 `T1_CLIENT_EVIDENCE_INCOMPLETE`，Stage 5 规划继续 `PLANNING_BLOCKED_EXTERNAL_CONTRACT`，不得启动实现。

取证后由用户在 WorkBuddy 内手动卸载唯一临时 Skill；重新置前核验“我安装的”页面显示“还没有安装任何技能”。已核验的精确隔离根随后以可恢复方式移入 Windows 回收站，源路径检查为不存在。该清理不删除 WorkBuddy 任务历史，也不改变上述证据裁决。

## 已完成的Stage 4最终交接卫生收口

原三路径卫生授权已在`78ee170678f80b71b3a88de95703a522a1f80cbc`正式推广。其实际Builder在创建worktree、修改文件、运行测试或提交推送前发现`README.md`、`README_zh-CN.md`、`PROJECT_CONTEXT.md`也是 materially stale 的当前入口，依第4路径停止规则报告`INCOMPLETE / STOPPED_SCOPE_EXPANSION`；该尝试为零worktree、零修改、零测试、零提交/推送，WSL未启动。该历史结果已经由后续修订授权和最终六路径结果闭合。

最终卫生Builder从正式授权对象接管，累计只修改`.github/workflows/ci.yml`、`docs/workbuddy/v2/README.md`、`docs/workbuddy/v2/MODULE-DISPOSITION.md`、`README.md`、`README_zh-CN.md`、`PROJECT_CONTEXT.md`六个路径；正式结果为`4636e27a62aad9f1b721e6c482e34b44d350503c`、tree `fdf24f8450ac4bb48e5337cd7aa3477794796d19`、tracked精确37。独立Reviewer最终返回`APPROVE / P0=0 / P1=0 / P2=0`；本地Python 3.14.7证据为11 hygiene、358 combined且全部exit 0；正式CI run `32386393634`为`completed/success`、Python 3.14.7、`357 passed / 1 skipped`、actions v6且没有Node20 deprecation warning。

本收口只把上述已交付事实机械镜像到`PROJECT-STATE.md`与`docs/workbuddy/v2/TASK-REGISTER.md`，采用恒定self-resolving mirror规则，不形成新的产品任务。该收口的历史状态（`HISTORICAL_BEFORE_V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE-AUTHORIZATION1`）为`current_task=NONE / current_task_status=NO_ACTIVE_TASK / next_authorized_task=NONE`；它不覆盖本提交进入formal后的顶部 live direct authority。Stage3/4继续`PASS_ACCEPTED`，Stage5、Stage6、最终Package物化和生产登记继续保持`NOT_GRANTED`或未证明。任何后续任务都必须另行明确授权。

腾讯WorkBuddy是唯一运行中的Agent；它读取已验证金钥匙版OpenMontage Package Guide后承担生产角色。阶段2已经接受完整必带工具链的Registration/Locator实现和一次真实临时Package验证。阶段3已完成Remotion与HyperFrames的有界探测、报告、逐能力授权集成合同实现并正式收口；两项始终是OpenMontage候选能力，Shell不选择渲染器，缺失、拒绝或延期不阻塞基础工具链路径。

## 已接受对象

- 阶段1已审对象：`041c6600dc8eb9094b5c93cb4a4ed088894578af`；正式集成边界：`fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9`。
- 阶段2完整工具链登记实现：`709c8e880b144fa9e9be26e9feb5d776dd6025e2`；状态收口：`95eeeff175060f06ca2f549737e724160edc9e14`。它证明登记能力、负面测试和一次临时Package组装/登记，不证明最终Package已经保留。
- 阶段3实现：`a3f8959682d296301dc573c2835f8c705a52e8b2`，独立`APPROVE / P0=0 / P1=0 / P2=0`并正式推广；closeout：`7c15aae4e77c579309312b21c79076f930970214`，已正式推广。
- 阶段3证据：55 direct、10 hygiene、199 full，全部最终退出0且无skip；未证明真实第三方/大陆镜像下载、生产DataRoot集成、WorkBuddy、Stage4、Provider或媒体/视频E2E。
- 阶段4规划：`5cb3f585a0cddffbd823c785b1d39ebd1834c1df`，`V2-S4-PLAN-REVIEW1`最终`APPROVE / P0=0 / P1=0 / P2=0`并正式推广；正式CI run `32337744225`为`completed/success`。两轮历史`REQUEST_CHANGES`已经闭合定义hash环、receipt结果/优先级/非法输入、可伪造摘要证据及Stage3 `managed/explicit/PATH`交接问题。
- 阶段4实现结果`fa9adb8470ab94b88ec9900ede03cb26f7de0ebd`经第八轮独立只读审查`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward；随后仅修复GitHub `setup-python`无`pyvenv.cfg`时的测试夹具，修复结果`13a3227b0c55bbe9039b46d7e92eba822b48f57e`也经独立审查`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward。正式树tracked精确37。
- 官方Ubuntu CI run `32369588814`为`357 passed / 1 skipped / exit 0`；Windows最终证据为158 direct、11 hygiene、358 combined，全部exit 0且无skip。WSL仅用于临时Linux等价验证，测试后已清理并关闭，不是Stage4运行依赖。
- 阶段4closeout固定历史锚点为`b63d8c2bc2214bc39f18378dbe47057ef538301e`、tree `02814c6a4a483913e7b1abe3e9ee6d025236c951`；closeout独立审查为`APPROVE / P0=0 / P1=0 / P2=0`，正式CI run `32371507874`在Ubuntu 24.04 / Python 3.11.16上`357 passed / 1 skipped`。因此阶段4实现已是`PASS_ACCEPTED`；最终交接卫生结果`4636e27a62aad9f1b721e6c482e34b44d350503c`也已独立批准、正式推广并由CI验证；`HISTORICAL_STAGE4_CLOSEOUT_CONTEXT`：当时“当前不存在活动任务或下一授权任务”仅为Stage4 closeout历史快照，不覆盖当前Stage5 live authority。
- 最终Release、生产PackageRoot和生产Registration仍属于后续最终交付/Installer任务，最迟在Stage5真实WorkBuddy生产验收前完成；它们不是Stage4规划或编码前置，也未被Stage4证据证明。

## 阶段3至阶段6建设顺序与实际运行链路

建设、审阅和交付严格按`阶段3 -> 阶段4 -> 阶段5 -> 阶段6`推进；这不等于最终用户的调用顺序。实际运行从阶段5开始：

```text
User -> Stage 5 WorkBuddy entry -> Stage 2 Locator revalidation
     -> Stage 4 one fixed Package-tool call with bundled required toolchain
        -> no declared local requirement: continue without Stage 3 evidence
        -> declared opaque local requirement: require the matching complete approved definition and original Stage 3 fact, then source-aware revalidate
     -> WorkBuddy/OpenMontage owns Provider/runtime routing and production decisions
     -> Stage 6 fact relay
```

- Python及核心依赖、FFmpeg/ffprobe、Node/npm/npx是阶段2登记对象，阶段3不得扫描、下载、替换或用系统PATH补救。
- 阶段3公共入口是`prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`；结果闭集是`DETECTION_REPORT/CONSENT_REQUIRED/INTEGRATED/SKIPPED/BLOCKED`。
- 阶段4先调用`locate_active_package(data_root)`；基础固定工具调用只依赖阶段2必带工具链。只有本次明确执行某可选能力时，才要求同一capability+definition的`PRESENT`或`INTEGRATED`证据。
- 阶段5拥有真实WorkBuddy新会话、唯一入口、literal `user_message`不变、逐能力询问和同任务继续的实现/验收；这些不是Stage4前置。
- 阶段6只在Stage4回执和Stage5真实消费者存在后判断；可直接消费时以`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`和生产代码0结束。

详细实时字段只以`docs/workbuddy/v2/TASK-REGISTER.md`为准；Git历史中的Wave A/B/C记录不是当前任务授权。

## Stage 4接管审计摘要

规划结果已冻结两个原合同缺口：固定工具身份来自批准Package定义/最终交付Installer owner提供的release-specific immutable `PackageToolDefinitionV1`；唯一公共入口为`launch_session_tool(...)`；输出为九值闭集、递归不可改写的`LauncherReceiptV1`。Stage4对Provider和Runtime保持opaque，不硬编码Remotion、HyperFrames或任何Provider；只有固定定义声明本地要求时才接收完整approved capability definition与未改写original Stage3 fact，并按`managed/explicit/PATH`原始source重新验证实际字节。

Stage 4规划、实现、closeout及最终交接卫生均已完成独立审查、普通fast-forward并由正式CI验证，`stage_4_planning=PASS_ACCEPTED`且`stage_4_implementation=PASS_ACCEPTED`。六权威同步、secret nondisclosure澄清、五路径实现、单文件CI夹具修复、产品closeout和六路径最终入口卫生都已进入历史；原三路径卫生Builder的安全停止也已闭合。`HISTORICAL_STAGE4_CLOSEOUT_CONTEXT`：当时“当前没有活动任务或下一授权任务”仅为Stage4 closeout历史快照，不覆盖当前Stage5 live authority。`mirror_result/mirror_effect/mirror_repository_delivery_resolution`不改变或重新门禁产品状态。Stage5整体当前为`IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`；真实生产WorkBuddy/Launcher会话、Stage5最终集成、Stage6、Provider/媒体执行及final Package物化/生产登记仍为`NOT_GRANTED`或未证明。

## Stage 5内部T1 Evidence2授权候选（2026-08-21）

本节是 Stage 5 内部 T1 的极窄 Evidence2 授权候选，不是 Stage 5 的前置阶段或前置任务。**本节为 HISTORICAL AUTHORIZATION，已由上方 CLI 边界纠偏 supersede；历史授权范围保留，但不得再把 CLI 存在当作架构不可用。**它只授权继续闭合 T1 的外部 Skill/入口合同证据，不授权 Stage 5 实现、真实生产流程或任何替代接口设计。用户授权为 2026-08-21 的“那继续吧”。本候选进入 formal 前，顶部 `next_authorized_task` 只表达条件候选；只有本候选经独立零写 Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 并以普通 fast-forward 进入 formal，`V2-S5-T1-CONTRACT-CLOSURE-EVIDENCE2` 才成为唯一有效下一任务。

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

`[HISTORICAL / SUPERSEDED_BY_CLI_BOUNDARY_CORRECTION]` 本授权候选当时把“不能证明零 CLI/MCP/命令/argv/Shell 的 `launch_session_tool(...)` 直调合同”作为 `ARCHITECTURE_CONTRACT_UNAVAILABLE` 条件；该条件保留为历史裁决，不再作为当前排他门槛。当前规则是继续核验唯一 WorkBuddy Skill 内部固定 CLI 是否为受控桥梁，且仍禁止第二入口、并行控制面、失败兜底和任意命令生成；本授权候选本身不推进 formal。

## Stage 5内部T1 Evidence2结果候选（2026-08-21）

本节消费上一节已经正式生效的 `V2-S5-T1-CONTRACT-CLOSURE-EVIDENCE2` 授权，只记录本轮允许的官方资料与受控客户端只读证据结果。Evidence2 是 Stage 5 内部 T1 的执行，不是 Stage 5 的前置阶段或前置任务；**本节为 HISTORICAL RESULT，已由上方 CLI 边界纠偏 supersede；历史证据与原始结果保留，但当前任务不得再把 CLI 存在本身当作架构阻断。**本候选不授权 Stage 5 实现、真实生产流程或任何替代接口。候选未推广前，formal 仍以 `4515268d1f77211a14f22927a02344b578527c4a`、tree `45b351bbf60419dc76833ddfcd61cd2ef52ff24c`、tracked 37 为权威；只有本候选经独立零写 Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 并以普通 fast-forward 进入 `origin/codex/workbuddy-shell-v2` 后，以下结果与“授权消费完成且无下一任务”才成为 formal live 状态。

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

## [HISTORICAL / SUPERSEDED_BY_2026-08-24_REBASELINE] Stage 5 T1 Skill+CLI合同重新评估候选（2026-08-21）

本节曾是 2026-08-21 的 superseding docs-level result，现已被 2026-08-24 重基线取代；它只保留此前 Evidence1/Evidence2 的历史证据，以及“CLI 本身不等于第二 Agent”的窄结论。最初产品目标仍是 Tencent WorkBuddy 作为唯一运行中的 Agent 和唯一用户入口，读取已验证 Package Guide 后承担 OpenMontage 逻辑生产角色。

```text
task_id: V2-S5-T1-SKILL-CLI-CONTRACT-REASSESSMENT1
task_kind: STAGE5_T1_CONTRACT_REASSESSMENT / DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE
initial_product_goal_recheck: PASS
base_commit: 24418c7cf5cc003c106a8282158adb3125bb0606
base_tree: d61a4a455a0e4f5202a2b4907476beb97a655201
tracked_files_at_base: 37
candidate_branch: codex/v2-s5-t1-skill-cli-reassessment1
candidate_worktree: D:\\BlazingCD\\Personal\\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2-s5-t1-skill-cli-reassessment1
candidate_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md
formal_target_branch: origin/codex/workbuddy-shell-v2
official_sources_access_date: 2026-08-21
controlled_client_evidence: EXISTING_ONLY / WorkBuddy 5.3.13 / HY3 no-op Skill record; no new client operation
stage_4_contract: PASS_ACCEPTED / launch_session_tool(...) + immutable LauncherReceiptV1 / unchanged
candidate_result: T1_INTERNAL_FIXED_CLI_BRIDGE_CONTRACT_FROZEN_FOR_PLANNING
stage_5_planning_after_candidate: IN_PROGRESS / T1_FIXED_CLI_BRIDGE_FROZEN_FOR_PLANNING
stage_5_implementation_authorization_after_candidate: NOT_GRANTED
current_task_after_candidate: NONE
next_authorized_task_after_candidate: V2-S5-PLANNING-CLOSEOUT-IMPLEMENTATION-HANDOFF-ASSESSMENT1 / ONLY_AFTER_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD
test: NOT_RUN_DOCS_ONLY
push_status: NOT_PUSHED
candidate_status: CANDIDATE_UNTIL_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD
```

### 两层证据裁决

官方证据层只证明 WorkBuddy Skill 能封装脚本/工作流、在用户授权下执行脚本/命令/外部程序，并且官方连接器公开 `Skill + CLI（内置脚本）`形态；它不负责定义本仓库的 Python API。项目内部桥梁层冻结：一个 WorkBuddy-managed installed Skill catalog 入口可以内部调用一个固定 CLI；该 CLI 不是用户第二入口，不是第二 Agent，不是并行控制面，不是失败兜底，也不得由用户原话拼接任意 command/argv/Shell。固定 CLI 的 release-specific identity/owner/hash、单一 input/output envelope、唯一消费者和与 Stage4 API/receipt 的真实绑定仍需项目证据闭合。

官方来源逐条记录（完整矩阵、标题和 claim/gap 见 `docs/workbuddy/v2/TASK-REGISTER.md` 当前 T1 章节）：

| ID | URL / 标题 | 可证明 | 不可证明 |
|---|---|---|---|
| O1 | `https://cloud.tencent.com/document/product/1831/134432` /《WorkBuddy Enterprise 技能》 | Skill 脚本/工作流、导入/启用、对话召唤和自动调用、用户授权执行。 | 包 schema、物理路径、优先级、唯一消费者、项目固定 CLI 和 Stage4 映射。 |
| O2 | `https://cloud.tencent.com/document/product/1831/134525` /《WorkBuddy Enterprise 连接器》 | 官方公开 `MCP + CLI` 与 `Skill + CLI（内置脚本）`形态。 | 不证明本项目必须使用 MCP，也不定义固定 CLI identity/envelope 或 Stage4 receipt 映射。 |
| O3 | `https://cloud.tencent.com/document/product/1831/134391` /《WorkBuddy Enterprise 新建任务栏（本地 AI 工作台）》 | WorkBuddy 任务栏可选择已安装 Skill 并自动调用；对话是独立任务入口。 | 不证明本项目全局唯一消费者、固定路径或内部 API。 |
| O4 | `https://cloud.tencent.com/document/product/1831/134401` /《WorkBuddy Enterprise 两个权限模式》 | 工作空间、脚本/命令/外部程序执行和确认边界。 | 不证明 Python 直调、参数/receipt 或固定 CLI。 |
| O5 | `https://cloud.tencent.com/document/product/1831/134324` /《WorkBuddy Enterprise WorkBuddy 更新记录》 | Desktop Skills、SkillHub/Marketplace、导入安全、项目级/企业自建 Skill 与 CLI 相关产品能力记录。 | 不证明当前精确包 schema、dispatch、唯一消费者或 Stage4 绑定。 |
| O6 | `https://cloud.tencent.com/document/product/1831/134516` /《WorkBuddy Enterprise Skills》 | 仅相邻 Skills 页面线索。 | 页面面包屑/正文是 CodeBuddy；`.codebuddy/skills` 不是 WorkBuddy 路径合同。 |

### 五项当前状态

```text
entry_identity: EXTERNAL_MECHANISM_CONFIRMED / historical PROVED_CLIENT_FOR_5.3.13_SESSION / implementation_package_details_pending
logical_install_owner: WorkBuddy-managed installed Skill catalog / physical path OPAQUE
call_subject: EXTERNAL_CALL_CONFIRMED / WorkBuddy conversation selecting one Skill / exact production dispatch pending internal contract
fixed_cli_bridge: SUPPORTED_FORM_CONFIRMED / FROZEN_FOR_PLANNING / LOCATOR_PACKAGE_PYTHON -I -m golden_key_openmontage_workbuddy.workbuddy_entry_cli / secret-safe stdin controls
unique_consumer: PROJECT_BOUNDARY_FROZEN / GLOBAL_RUNTIME_PROOF_PENDING
stage4_binding: COMPATIBLE_INTERNAL_CONTRACT / FIXED_CLI_TO_LAUNCH_SESSION_TOOL_MAPPING_FROZEN_FOR_PLANNING
```

故上一节结果为 `T1_INTERNAL_FIXED_CLI_BRIDGE_CONTRACT_FROZEN_FOR_PLANNING`，不是旧的 `ARCHITECTURE_CONTRACT_UNAVAILABLE`，也不是 `PASS_ACCEPTED`；该上一节及其“下一任务为规划收口”的镜像现在是 `HISTORICAL_SUPERSEDED_BY_STAGE5_PLANNING_CLOSEOUT`。Stage4既有合同不重开。固定 CLI 仅以 `LOCATOR_PACKAGE_PYTHON -I -m golden_key_openmontage_workbuddy.workbuddy_entry_cli` 作为无子命令 transport adapter；stdin 只含非秘密 controls、完整定义/原始事实和 provider names/source，secret value 只从 CLI 进程环境按 allowlist 重建后进入 Stage4；stdout 只输出完整 `LauncherReceiptV1` mapping，pre-Stage4 错误不伪造 receipt；`cancel_requested` 只传本地 Event，不建后台 IPC。当前收口候选的结果、实施白名单和下一任务以下节为准。

## [HISTORICAL / SUPERSEDED_BY_STAGE5_PLANNING_CLOSEOUT] Stage 5 T1固定 CLI桥梁合同候选镜像

```text
task_id: V2-S5-T1-FIXED-CLI-BRIDGE-CONTRACT-PLAN1
base_commit: 3eed285da6ae48e502d5be1f8ca726906d36b7cd
base_tree: c0b03c4e7d858d5f15c7ce328cf5e2b60b57978b
tracked_files_at_base: 37
candidate_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md; docs/workbuddy/v2/PROJECT-CHARTER.md; docs/workbuddy/v2/ACCEPTANCE-MATRIX.md
initial_product_goal_recheck: PASS
t1_internal_contract_status: FROZEN_FOR_PLANNING
bridge_contract_id: golden-key-workbuddy-skill-cli-bridge-v1
fixed_argv: -I -m golden_key_openmontage_workbuddy.workbuddy_entry_cli
installer_identity: absolute package-private interpreter identity/path + module/schema/argv/environment identities and hashes; WorkBuddy Skill physical path remains opaque
input_transport: one canonical versioned JSON stdin object; wire-only canonicalization; no user_message Unicode normalization; Stage4 NFC/UTF-8 precondition verified, non-NFC exit64; no provider secret values
provider_secret_transport: fixed CLI process env names -> reconstructed Stage4 provider_environment -> Stage4 allowlisted child env only
output_transport: one complete golden-key-workbuddy-launcher-receipt-v1 JSON mapping on stdout; fixed sanitized stderr only
transport_exit: closed set 0=one Stage4 call+fully buffered validated receipt output (including failure outcome); 64=input/schema/identity/cancel/continuation or user_message NFC/UTF-8 precondition; 78=asset/process-env/provider-name/provenance; 70=bridge-internal or post-call receipt serialization/output validation; errors empty stdout/no fake receipt
cancel_boundary: cancel_requested bool -> local threading.Event before one call; no runtime IPC/replay
stage_5_planning: IN_PROGRESS / T1_FIXED_CLI_BRIDGE_FROZEN_FOR_PLANNING
stage_5_implementation_authorization: NOT_GRANTED
downstream_implementation_allowlist: UNFROZEN / separate docs-only handoff assessment required
next_authorized_task: V2-S5-PLANNING-CLOSEOUT-IMPLEMENTATION-HANDOFF-ASSESSMENT1 / conditional on independent APPROVE and ordinary fast-forward
candidate_test: NOT_RUN_DOCS_ONLY
candidate_push: NOT_PUSHED
```

## [HISTORICAL / SUPERSEDED_BY_V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1] Stage 5规划收口与实施交接候选（`V2-S5-PLANNING-CLOSEOUT-IMPLEMENTATION-HANDOFF-ASSESSMENT1`，2026-08-21）

本节记录前一轮六文档 docs-only handoff 候选及其历史条件；实施已经由后续 `V2-S5-WORKBUDDY-ENTRY-BUILDER1` 消费完成。当前实施和本轮 closeout 以本文末新的六文档镜像为准；历史条件不覆盖当前 live 状态。

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

未来 Builder 精确实现白名单（仅在本候选正式推广后使用）：

1. `workbuddy-skill/golden-key-openmontage/SKILL.md`：唯一仓库 WorkBuddy Skill 源资产；其 root `SKILL.md` 形态与既有客户端导入事实一致。WorkBuddy 实际安装路径仍 opaque；Installer/最终 Package gate 必须以 release identity、owner、module/schema/argv/environment hash 固化后承载，未解析 placeholder 或身份漂移时 fail closed。
2. `golden_key_openmontage_workbuddy/workbuddy_entry_cli.py`：唯一 package-private `-I -m` transport adapter，不加入 `__init__.py` 公共导出，不建立 console script、子命令或第二控制面。
3. `tests/workbuddy/test_workbuddy_entry_cli.py`：唯一新增直接测试文件，覆盖 closed envelope、literal message 原样、secret non-disclosure、一次 Stage4 调用、receipt/exit `0/64/70/78`、cancel/continuation 和无重试/重放。
4. `tests/workbuddy/test_repository_hygiene.py`：仅同步固定 tracked/source inventory、唯一 Skill 资产和新增 package-private module 的卫生断言。
5. `.github/workflows/ci.yml`：仅把新直接测试加入既有唯一 pytest 命令，不改触发器、Python 版本或其他工作流语义。

`__init__.py`、`pyproject.toml`、`docs/workbuddy/v2/MODULE-DISPOSITION.md` 和其他文件均拒绝加入：前者不应暴露 CLI 公共 API；pyproject 已包含既有 package 且禁止 console script，新增 `.py` 自动属于该 package；Installer/最终 Package gate 负责 Skill 源资产 release 承载；MODULE-DISPOSITION 现有 `REWRITE`/唯一入口边界已足够。tracked 目标精确为 `37 -> 40`。项目私有环境必须位于 D 盘 task-private 路径 `D:\BlazingCD\Personal\Temp\workbuddy-v2-s5-entry-builder1\.venv`，不得混用全局包。

固定命令（Builder 使用上述 `.venv\Scripts\python.exe`；CI 使用同一参数序列）：

```text
direct:  python -m pytest -p no:cacheprovider tests/workbuddy/test_workbuddy_entry_cli.py -q
hygiene: python -m pytest -p no:cacheprovider tests/workbuddy/test_repository_hygiene.py -q
full/CI: python -m pytest -p no:cacheprovider tests/workbuddy/test_package_registration.py tests/workbuddy/test_runtime_prepare.py tests/workbuddy/test_session_launcher.py tests/workbuddy/test_workbuddy_entry_cli.py tests/workbuddy/test_repository_hygiene.py -q
```

实施仍必须经历 Builder commit、独立 zero-write Reviewer `APPROVE / P0=0 / P1=0 / P2=0`、ordinary fast-forward、tracked/clean/untracked/stash 验证和临时现场清理。该候选不等于实施完成；真实 WorkBuddy 新会话、唯一入口命中、原话/授权/继续、最终 Package/Registration、Provider、媒体和业务效果仍是后续独立证据层。

## [HISTORICAL / SUPERSEDED_BY_V2-S5-R00-REMAINDER-PLAN-STATE-CORRECTION1] Stage 5实施完成与入口收口候选（`V2-S5-WORKBUDDY-ENTRY-CLOSEOUT1`，2026-08-21）

本节是本轮六文档 docs-only 机械镜像；它不修改产品代码状态。Stage 5 planning 已是 `PASS_ACCEPTED`，实施 Builder 结果已在正式分支存在并经独立 Reviewer/CI 证实；但本 closeout 自身在独立 Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 与普通 fast-forward 进入 formal 前仍是候选，不能自称已交付。只有该推广完成后，`stage_5_implementation=PASS_ACCEPTED`；收口后 `current_task=NONE / NO_ACTIVE_TASK / next_authorized_task=NONE`。

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

唯一入口合同保持：WorkBuddy 是唯一 Agent/用户入口；一个 Skill 只调用 package-private fixed `-I -m golden_key_openmontage_workbuddy.workbuddy_entry_cli` transport adapter，随后恰好一次 `launch_session_tool(...)` 并输出真实 `LauncherReceiptV1`。无 console script、subcommands、router、MCP、第二 Agent、retry/replay；literal message、closed JSON、provider secret non-disclosure、固定环境身份、cancel/continuation 和 receipt 约束不变。静态/direct/hygiene/CI 证据不等于真实 WorkBuddy 生产、业务或 E2E 证据。

实施的精确五路径为：`.github/workflows/ci.yml`、`workbuddy-skill/golden-key-openmontage/SKILL.md`、`golden_key_openmontage_workbuddy/workbuddy_entry_cli.py`、`tests/workbuddy/test_workbuddy_entry_cli.py`、`tests/workbuddy/test_repository_hygiene.py`。最终 Installer-stamped Skill、最终 Package 物化/Registration、真实 WorkBuddy、Provider/媒体和 Stage6 均需后续独立授权与证据；本 closeout 不自动产生下一任务。

## [HISTORICAL / CONSUMED_BY_V2-S5-R01-WORKBUDDY-EXECUTION-CONTRACT-EVIDENCE1] Stage 5剩余计划与当前纠偏（`V2-S5-R00-REMAINDER-PLAN-STATE-CORRECTION1`，2026-08-21）

本节是当前十二文档 docs-only 候选。产品目标回读为 `PASS`：WorkBuddy 是唯一运行中的 Agent 和唯一用户入口，Shell 只负责六模块，不成为 Director/FSM/第二 Agent/媒体控制面。Stage 5 整体必须保持 `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`；入口代码、固定 CLI、Stage4 `launch_session_tool(...)`、Reviewer、正式 Git/CI 是已交付子项，不等于 Stage5整体PASS。该候选推广后 `current_task=NONE / NO_ACTIVE_TASK / next_authorized_task=NONE`；`next_planned_task=V2-S5-R01-WORKBUDDY-EXECUTION-CONTRACT-EVIDENCE1 / REQUIRES_SEPARATE_USER_AUTHORIZATION`，本候选不自动授权 R01。

```text
task_id: V2-S5-R00-REMAINDER-PLAN-STATE-CORRECTION1
task_kind: DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE / EXACT_12_EXISTING_DOCS
base_commit: 2207c9083ceabcf6539936e47b0935a4eaa77c46
base_tree: 8c66c3c38bf0dc00595c09743de715d7c1117c40
tracked_files_at_base: 40
initial_product_goal_recheck: PASS
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
entry_code_result: 0e7a0be65877b03fb386e1c6c6bc258c0b27db6c / tree 85c266edb7349c940e8cd45870cc0538c95726c0 / tracked 37->40
entry_code_review_ci: APPROVE / P0=0 / P1=0 / P2=0 / Windows 19+11+377 passed / CI 32489111184 success 376 passed 1 skipped
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

### Stage 5整体完成定义

只有以下五类证据全部存在，Stage 5 才能整体 `PASS_ACCEPTED`：

1. 持久保留的 final Package Release 与 PackageRoot；
2. production Registration + Activation + new-process Locator 返回一致身份；
3. 无 placeholder、已安装且唯一的 final WorkBuddy Skill；
4. HY3 真实 WorkBuddy 成功取得真实 `LauncherReceiptV1`；
5. 独立 Review、正式 Git/CI，以及无歧义的 live authority。

缺任一项都只能保持 `REAL_INTEGRATION_INCOMPLETE`，不得用静态测试、临时Package、客户端导入、Skill命中或 closeout 文档替代。

### S5-00 至 S5-08 严格顺序

| 编号 / 任务 | 作用、输出与验收 | 停止边界 / 不证明 |
|---|---|---|
| S5-00 / `V2-S5-R00-REMAINDER-PLAN-STATE-CORRECTION1` | 本十二文档 live truth 纠偏；固定 Stage5 状态、五类完成定义和 R01-R08 依赖；`DOCS_ONLY`、测试不运行 | 不实现产品、不授权 R01，不创建Package、Registration、Skill或客户端证据 |
| S5-01 / `V2-S5-R01-WORKBUDDY-EXECUTION-CONTRACT-EVIDENCE1` | 原始 R01 由 134432 证明公开形态；refresh1 由 134420 明示 enterprise Skill scripts 在客户端沙箱执行；134516 保持 CodeBuddy `PRODUCT_MISMATCH`。refresh1 复核 Skill-root cwd/bundled-relative resolution 与精确 stdin/stdout/stderr/final-exit/timeout 语义 | PowerShell 资格仅来自受控客户端观察，不是 134420 的精确执行合同；不得以 PowerShell 非原生作为阻断；缺少 Skill-root/bundled-relative 合同仍为 `BLOCKED_EXTERNAL_CONTRACT`；禁止 MCP、第二Skill、任意CLI旁路；不证明最终Skill、Package或真实Launcher成功 |
| S5-02 / `V2-S5-R02-PACKAGE-RELEASE-TOOL-DEFINITION-BINDING1` | 实时重验批准的最终Package Release；`0.3.24/tree 0464861c`仅为候选，需live复核；绑定真实存在的 safe fixed tool 与 release-specific `PackageToolDefinitionV1`，纳入Manifest/Lock | 无真实Release即 `BLOCKED_PACKAGE_RELEASE`，Shell不得臆造fixture、工具或定义 |
| S5-03 / `V2-S5-R03-EXECUTABLE-SKILL-BUNDLE1` | 构建单一可执行Skill bundle：最小bundled helper、verified Guide/definition、canonical envelope、scrubbed env、固定private CLI一次、receipt映射、Stage3逐能力询问和用户确认的新continuation；须代码/Skill/测试/CI/独立Review/FF | 禁止第二Agent、MCP、router、retry/replay；具体路径必须届时从live formal另行冻结，不由R00预造 |
| S5-04 / `V2-S5-R04-INSTALLER-LIFECYCLE1` | 实现当前缺失的Installer/lifecycle：approved OpenMontage、Shell包、private Python+locked deps、FFmpeg/ffprobe、Node/npm/npx、tool definition、Manifest/Lock/ZIP/sidecar、Skill identity/schema/module/argv/interpreter stamping，以及fresh/repair/upgrade/rollback/uninstall、数据保留/ownership/staging/atomicity | 先D盘隔离测试；未获实现授权不得改代码或预造路径；不证明生产Package已登记 |
| S5-05 / `V2-S5-R05-FINAL-PACKAGE-MATERIALIZATION-REGISTRATION1` | 用户另行确认正式D盘DataRoot；用R04物化并持久保留final Release/PackageRoot，register+activate+new-process locate，验证工具链、Guide、Manifest/Lock/Shell/tool definition | 未经用户确认不得操作正式DataRoot；成功产物不得删除为临时证据 |
| S5-06 / `V2-S5-R06-FINAL-SKILL-INSTALLATION1` | 导入Installer-stamped完整Skill folder/ZIP；零placeholder；客户端仅一个`golden-key-openmontage`，无旧V1/测试Skill；HY3 slash精确命中 | 不猜物理安装路径；不把导入成功当作Stage5整体PASS |
| S5-07 / `V2-S5-R07-REAL-WORKBUDDY-ACCEPTANCE1` | HY3-only真实新会话覆盖正常成功、取消/超时、并发/幂等、重启后定位；成功必须真实`LauncherReceiptV1`，并核对WorkBuddy呈现与receipt字段 | 不使用Auto；Provider、媒体、业务E2E不在本任务；任一身份/证据缺失即阻断，不伪造receipt |
| S5-08 / `V2-S5-R08-STAGE5-FINAL-CLOSEOUT1` | 仅在R01-R07全部证据齐备后独立Review、正式Git/CI、清理temporary但保留正式Package/Registration/Skill；唯一任务可把live `stage_5=PASS_ACCEPTED` | 不使用self-resolving candidate冒充完成；Stage6只在另行授权后接管 |

依赖严格为 `R01 -> R02 -> R03 -> R04 -> R05 -> R06 -> R07 -> R08`；任一阻断不得跳过。R03/R04即使未来证据允许合并，也必须另行授权并保留全部验收项。Stage5不要求Provider真实调用、媒体/视频生成、Remotion/HyperFrames下载安装、Stage6转换代码或完整业务E2E；optional缺失/decline/defer不阻断base。Stage5之后先判断Stage6能否直接复用receipt（可直用则优先零代码），整个项目最终业务E2E另行授权，不称为Stage7。

## [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / ORIGINAL R01 / FORMALLY CLOSED / PRESERVED] 当前 R01 受控执行合同证据收口（2026-08-22）

```text
task_id: V2-S5-R01-WORKBUDDY-EXECUTION-CONTRACT-EVIDENCE1
task_kind: CONTROLLED_CLIENT_EVIDENCE + DOCS_ONLY_CLOSEOUT / ZERO_PRODUCT_STATE_CHANGE
user_authorization: 2026-08-22 / 启动阶段五并要求每个子任务独立审核、边界审计和产品目标回读
base_commit: d0a055689e9fc928a31edb24f3740e9408e123ef
base_tree: 50197a1eb103ffad42ac3e2952dcd3f9761a9512
base_parent: 2207c9083ceabcf6539936e47b0935a4eaa77c46
tracked_files_at_base: 40
initial_product_goal_recheck: PASS
scope_expansion_audit: PASS
stage_5_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
official_sources: 134432 WorkBuddy Skills; 134391 local AI workbench task bar; 134324 WorkBuddy update notes; 134516 CodeBuddy PRODUCT_MISMATCH_NOT_CONTRACT_PROOF
workbuddy_version_observed: 5.3.14
baseline_installed_skills: 2 / agent-browser; find-skills
temporary_probe_zip: r01-controlled-probe.zip / sha256 C55C90B7E86E9399F04EF13B8D78DF9228A8D72F7149B5B2A11B4362320F102D / DELETED_AFTER_REVIEW
temporary_probe_skill_sha256: D1BE59EF9221BA739482555744385244C86B771F5604DB738F5E0952CCC1E1E1 / HASH_ONLY_SOURCE_DELETED_AFTER_REVIEW
temporary_probe_script_sha256: 52B1F6283FF376F99DE49AE87EF24781042DC12F679AAAF7F976F58F19307064 / HASH_ONLY_SOURCE_DELETED_AFTER_REVIEW
client_safety_scan: NOT_SKIPPED / AUTO_INSTALL_ACCEPTED
installed_skill_observation: count 3 / exact golden-key-openmontage-r01-controlled-probe identity appeared
controlled_task_model: HY3 / NEVER_AUTO
success_case_prompt: relative scripts/r01_contract_probe.py + one literal JSON with final LF + fixed env marker + native stdout/stderr/final-exit/cwd/timeout capture
native_bundled_script_invocation_event: ABSENT
client_execution_path_observed: ORIGINAL_R01 / Bash/PowerShell only / no independent native bundled-script invocation/tool event
coordinator_stop: BEFORE_ANY_SHELL_OR_TERMINAL_EXECUTION
probe_script_execution: NOT_RUN
stdout_stderr_exit_cwd_timeout_evidence: NONE
nonzero_case: NOT_RUN
timeout_case: NOT_RUN
r01_result: BLOCKED_EXTERNAL_CONTRACT
r01_result_reason: frozen contract requires one independent native bundled-script invocation/tool event per case; HY3 exposed only shell execution, so text/marker/JSON cannot substitute
r01_result_review: APPROVE / P0=0 / P1=0 / P2=0 / FORMALLY_FAST_FORWARDED_TO_ORIGIN_CODEX_WORKBUDDY_SHELL_V2 / COMMIT=9eefe8600d9bed0c8ea6024880e4b2d2ef4e3bfc
r02_r08_status: NOT_STARTED / NOT_AUTHORIZED_BY_CHAIN
temporary_skill_cleanup: COMPLETE / USER_UNINSTALLED_TEMPORARY_SKILL / WORKBUDDY_INSTALLED_SKILLS_2 / TASK_HISTORY_RETAINED / BASELINE_SKILLS_2_UNTOUCHED
baseline_skill_cleanup: NOT_TOUCHED / TWO_RETAINED_SKILLS
temporary_probe_cleanup: COMPLETE / EXACT_ISOLATED_WORKTREE_FOLDER_AND_ZIP_DELETED / GIT_STATUS_CLEAN
candidate_test: NOT_RUN_DOCS_ONLY
candidate_production_code_changes: 0
candidate_test_changes: 0
candidate_ci_changes: 0
candidate_package_registration_changes: 0
candidate_provider_media_stage4_stage6_changes: 0
candidate_push: R01_RESULT_FORMALLY_FAST_FORWARDED / origin/codex/workbuddy-shell-v2 / commit=9eefe8600d9bed0c8ea6024880e4b2d2ef4e3bfc
```

R01 的官方资料只证明 WorkBuddy Skill 可以封装脚本/工作流、可上传和在任务中选择/自动调用；更新记录只作支持范围证据，未给出精确 command/cwd/env/stdin/stdout/stderr/exit/timeout 语义。由于真实客户端没有产生独立原生 bundled-script invocation/tool event，R01 的三个 case 不能逐项继续；不运行非零或 timeout case，不把客户端安装成功当作脚本执行成功，也不把模型文字、自报或匹配诊断当作事件证据。R01 最终裁决仍为 `BLOCKED_EXTERNAL_CONTRACT`；独立 zero-write Review 已 `APPROVE / P0=0 / P1=0 / P2=0` 并正式 fast-forward，用户已卸载临时 Skill，WorkBuddy 显示安装技能数为 `2`，任务历史保留，精确隔离 probe folder/ZIP 已删除。R01 失败只阻断 R01->R02 链，不改变 Stage 3/4 已接受状态，也不扩大 Shell 为第二控制面。

## [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT] Stage 5 R01 Sandbox Refresh1 受控客户端正式结果镜像（2026-08-22）

本节是独立于已关闭原始 R01 的 refresh1 正式结果镜像；原始 R01 记录、其清理结果和正式提交均保留，不被改写。官方 134420 只证明 enterprise Skill scripts 在客户端沙箱执行。受控 WorkBuddy 客户端观察将 PowerShell 记录为 `ELIGIBLE_CANDIDATE_SURFACE`，不是官方精确执行合同；不能再以“PowerShell 非原生/只暴露 shell”作为阻断理由。当前真正缺少的是 Skill-root cwd 与 bundled-relative resource resolution 合同，以及 stdin/stdout/stderr/final-exit/timeout 的精确合同。

```text
task_id: V2-S5-R01-WORKBUDDY-SANDBOX-REFRESH1
task_kind: CONTROLLED_CLIENT_EVIDENCE_REFRESH + DOCS_ONLY_CLOSEOUT / ZERO_PRODUCT_STATE_CHANGE
candidate_branch: codex/v2-s5-r01-sandbox-refresh1-closeout
candidate_base: 932bcabc5baf90d0190101b1039e4ccf087b2b08 / tree 2ed2cd0e67dd8628b7f0b1acf84df0a7d8b0d0fd / tracked 40
product_goal_recheck: PASS / WorkBuddy唯一运行Agent和用户入口 / 固定CLI仅为唯一Skill内部桥梁 / 无第二入口或控制面
official_contract: 134420=CLIENT_SANDBOX_SCRIPTS_EXECUTION_ONLY / 134432=SKILL_SCRIPTS_WORKFLOWS_UPLOAD_CALL_SHAPE / 134516=CODEBUDDY_PRODUCT_MISMATCH_NOT_CONTRACT_PROOF
powershell_surface: ELIGIBLE_CANDIDATE_SURFACE_FROM_COORDINATOR_CLIENT_OBSERVATION / NOT_OFFICIAL_EXACT_CONTRACT
contract_gaps: BUNDLED_RELATIVE_RESOURCE_RESOLUTION / SKILL_ROOT_CWD / STDIN / STDOUT / STDERR / FINAL_EXIT / TIMEOUT
workbuddy: 5.3.14 / baseline=agent-browser,find-skills / HY3_ONLY / NEVER_AUTO
refresh1_source_root: ISOLATED_D_DRIVE_TEMP_ROOT / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / CLEANUP_COMPLETE / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND
refresh1_hashes: SKILL=A369E89912B51C1627C972A7DE8F82111E55E2909622CB2E0E3276B45331FFF9 / SCRIPT=8A1D38A65945CC99C4B7F8EE95FDF4FF744D105303BC9904E5915E630DF58359 / ZIP=2284E6D6FE8FFD38689A357DD0A6653CEB23B923F0C531BF9EAC376178E9A28A
install_observation: SAFETY_SCAN_NOT_SKIPPED / NO_NON_HIGH_RISK_AUTO_INSTALL_SELECTED / INSTALLED_COUNT_3 / CLIENT_ID=workbuddy-skill-1787379691395 / SKILL_MD_NO_METADATA_NAME / BODY_FIRST_LINE_MATCHED_PROBE
native_read_event: PRESENT / SKILL_MD_AND_scripts\\r01_contract_probe.py_READ / PHYSICAL_INSTALL_PATH_EXPOSED_CONTRACT_DEVIATION_SENSITIVE_MINIMIZATION_FAILURE / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
execution_observation: SESSION_WORKSPACE_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / FROZEN_RELATIVE_SCRIPT=.\\scripts\\r01_contract_probe.py / NO_CD_NO_ABSOLUTE_PATH_NO_GUESSING_NO_COMMAND_MUTATION / SKILL_ROOT_CWD_NOT_EXPOSED / BUNDLE_RELATIVE_INVOCATION_NOT_EXPOSED / POWERSHELL_NOT_STARTED
coordinator_stop: UI_STOPPED / USER_CANCELLED
probe_evidence: NO_SCRIPT_EXECUTION / NO_STDOUT_STDERR_FINAL_EXIT_CWD_CLASSIFICATION_TIMEOUT
refresh1_result: BLOCKED_EXTERNAL_CONTRACT / MISSING_SKILL_ROOT_CWD_AND_BUNDLE_RELATIVE_RESOLUTION / NOT_BECAUSE_POWERSHELL_IS_NON_NATIVE
review: APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_REVIEWER
reviewer_independent_observation: WORKBUDDY_5.3.14 / HY3 / USER_CANCELLED / NO_SUCCESS_STDOUT_STDERR_EXIT_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
nonzero_case: NOT_RUN
timeout_case: NOT_RUN
r02_r08_status: NOT_STARTED / NOT_AUTHORIZED_BY_CHAIN
temporary_skill: UNINSTALLED / USER_UNINSTALLED_TEMPORARY_SKILL / TEMP_SKILL_ID=workbuddy-skill-1787379691395_NOT_IN_INSTALLED_LIST / WORKBUDDY_MY_INSTALLED_SKILLS_2=agent-browser,find-skills / TASK_HISTORY_RETAINED / BASELINE_SKILLS_UNTOUCHED / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND
computer_use_transparency: LOW_IMPACT_OPERATIONAL_ANOMALY / EXISTING_EXPLORER_MISTAKEN_FOR_FILE_PICKER / ALT+N_MAY_OPEN_TAB_OR_WINDOW / NO_PATH_INPUT_NO_FILE_SELECTION_NO_WRITE_DELETE / STOPPED_AND_RECOVERED
accepted_result_commit: 6c20371f1c72ee9d55147e1ad7feb8ede201858f / tree 9eb4643f09d03cc9f39b0b46906773e5bcc9125d
docs_review: APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_ZERO_WRITE_REVIEW
candidate_current_task: NONE / NO_ACTIVE_TASK / R01_REFRESH1_ACCEPTED_BLOCKED_EXTERNAL_CONTRACT
candidate_next_authorized_task: NONE / R01_REMAINS_BLOCKED / ONLY_SEPARATE_R01_REOPEN_AUTHORIZATION_PLUS_ACCEPTED_SUCCESS_CONTRACT_EVIDENCE_CAN_UNLOCK_R02_R08
candidate_test: NOT_RUN_DOCS_ONLY / product_code=0 / tests=0 / ci=0 / provider_media_package_stage4_stage6=0
candidate_push: FORMALLY_EFFECTIVE_IFF_LIVE_REMOTE_REF_CONTAINS_THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR
```

该正式结果镜像不改变 Stage 5 的 `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`，不运行 nonzero/timeout，不创建或推广 Package、Registration、Installer、最终 Skill、Stage 4 spawn、Provider、媒体或 Stage 6。旧 R01 的“PowerShell-only”事实仅属于原始已关闭记录；refresh1 的阻断理由必须保持为缺少 Skill-root cwd/bundled-relative resolution 合同。

## 当前项目级架构纠偏审计 Phase A 镜像（A7 docs-only 已正式推广，2026-08-22）

以下是 A0-A6 经独立零写 Reviewer 批准后的单一自包含结论。A7 docs-only 结果已正式推广到 formal branch；它固化的是审计结果和最小纠偏任务方案，不是产品纠偏完成，也不改变任何产品状态。历史合同 PASS 与当前产品架构状态分开记录；旧记录不被改写。

```text
task_id: V2-PROJECT-ARCHITECTURE-RECOVERY-PHASE-A1
formal_ref: refs/heads/codex/workbuddy-shell-v2
formal_baseline_parent: f338d9d50cad2cccf1398438ad4a8c8d45127a21 / tree 5ef5e8e524412f6220ad31f2cc38448c6b1dac8b
phase_a_audit_commit: 4727c5efda6ae53194ff2c16dd224c67178e8d8d
phase_a_audit_tree: ac6206950b36f71663eddfb89b7e311aa85b53e6
phase_a_status: A0-A6_APPROVED / A7_DOCS_FORMALLY_PROMOTED
scope: EXACTLY_SIX_EXISTING_AUTHORITY_FILES / DOCS_ONLY
effect: ZERO_PRODUCT_STATE_CHANGE
tests: NOT_RUN_DOCS_ONLY
review: APPROVE / P0=0 / P1=0 / P2=0 / INDEPENDENT_ZERO_WRITE
formal_promotion: ORDINARY_FAST_FORWARD / FORMALLY_PROMOTED / commit=4727c5efda6ae53194ff2c16dd224c67178e8d8d / tree=ac6206950b36f71663eddfb89b7e311aa85b53e6 / ci_run=32615371879 / completed=success / headSha=4727c5efda6ae53194ff2c16dd224c67178e8d8d
task_artifacts_cleanup: ORIGINAL_PHASE_A_WORKTREE_LOCAL_AND_REMOTE_TASK_BRANCH_CLEANED
state_closeout: THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR
phase_b: NOT_AUTHORIZED / A7_HISTORICAL_SNAPSHOT
phase_b_authorization: NOT_AUTHORIZED / A7_HISTORICAL_SNAPSHOT
```

### 原始目标、谱系和需求分类

原始目标是让普通用户只需在 WorkBuddy 中用自然语言提出业务需求，由 WorkBuddy 作为唯一运行 Agent 和唯一用户对话主体，读取经 Registration/Locator 验证的 OpenMontage Package Guide、Manifest、Pipeline/Stage/Artifact/Checkpoint/Reviewer/Tool/Provider 合同，作出生产决策并展示结果。Shell 只提供安装与生命周期、Registration/Locator、按需运行时准备、确定性 Launcher、WorkBuddy 入口支持、状态/结果转交六个模块；OpenMontage Agent 是 WorkBuddy 读取 Guide 后承担的逻辑生产角色，不是第二 Agent。

谱系为：原始 V2 重构交接目标及八阶段/十一步承诺 -> 六模块 Shell 边界 -> Stage 1 治理 -> Stage 2 Registration/Locator -> Stage 3 可选能力准备 -> Stage 4 机械 Launcher 合同 -> Stage 5 WorkBuddy/最终 Package 真实集成 -> Stage 6 结果转交。A1-A6 确认断档发生在 Stage 4 机械合同和 Stage 5 真实集成之间：最终 Package/Installer/生产 Registration 的 Owner 与真实 WorkBuddy Guide-read 证据没有被前置纳入完成条件。

| 领域 | 需求分类 | 当前结论 |
|---|---|---|
| 唯一 WorkBuddy Agent、六模块 Shell、自然语言用户入口 | `FULFILLED_AND_RETAIN` / `FULFILLED_BUT_NARROW` | 边界保留；真实客户端链仍未完成证明 |
| OpenMontage Agent-first、Guide 驱动生产决策 | `UNPROVED` | 必须在真实 WorkBuddy 中观察 Guide-read 与决策顺序 |
| Stage 2 Registration/Locator | `FULFILLED_BUT_NARROW` | 临时 assembled-Package 证据不等于最终生产 Package |
| Stage 3 可选能力 | `FULFILLED_BUT_NARROW` | 只处理显式授权的可选 Remotion/HyperFrames，不拥有必带工具链 |
| 最终 PackageRoot、私有工具链、Installer/生命周期 | `DEFERRED_WITH_VALID_OWNER` / `UNPROVED` | 归最终交付 Installer Owner，Node 22+ 必须随最终 Package 提供 |
| Stage 4 `PackageToolDefinitionV1`/Launcher/Receipt | `FULFILLED_BUT_NARROW` | 历史机械合同 PASS；当前产品架构仅 `HISTORICAL_PASS_ONLY` |
| Stage 5 真实 WorkBuddy、Artifact/Receipt、业务 E2E | `PARTIAL` / `UNPROVED` | `REWORK`，不得称 Stage 5 PASS |
| Stage 6 直接复用 Receipt | `DEFERRED_WITH_VALID_OWNER` / `INSUFFICIENT_EVIDENCE` | 保持零代码，等待真实消费者证据 |
| R02 阻断责任归属 | `MISASSIGNED_TO_WRONG_LAYER` | 推荐移到 Shell/Installer 装配责任，live 状态不改 |
| 旧 Stage 2 对齐分支 | `SUPERSEDED_WITH_VALID_REASON` | 只保留历史，禁止合并/删除 |
| 旧 R03-R05 任务包 | `SUPERSEDED_WITH_VALID_REASON` | 被 B02/B03 替代，禁止并行执行 |

### 阶段当前处置（历史字段与当前字段分离）

```text
stage_1_historical_contract: PASS_ACCEPTED
stage_1_current_disposition: KEEP
stage_2_historical_contract: PASS_ACCEPTED_FOR_REGISTRATION_LOCATOR_AND_TEMPORARY_PACKAGE
stage_2_current_disposition: KEEP_WITH_NARROWING
stage_3_historical_contract: PASS_ACCEPTED
stage_3_current_disposition: KEEP_WITH_NARROWING
stage_4_historical_contract: PASS_ACCEPTED_MECHANICAL_CONTRACT
stage_4_current_disposition: HISTORICAL_PASS_ONLY
stage_5_historical_repository_result: ENTRY_CODE_COMPLETE
stage_5_current_status: IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE
stage_5_current_disposition: REWORK
stage_6_historical_design_result: LATER_RELAY_BOUNDARY_ONLY
stage_6_current_disposition: INSUFFICIENT_EVIDENCE
```

### 绑定与 R02 当前状态

唯一 binding delivery owner 是 `V2 Final-delivery Installer / Release Assembly Owner`。Carrier 是最终 WorkBuddy `PackageRoot` 内独立的 `Shell-adapter` 子树；Shell 拥有 schema 和 consumer；当前 Golden Key OpenMontage 0.3.25 子树、Release、Lock、Guide 和源码保持不可变。最终 Manifest/Lock/hash 负责两棵子树的确定性绑定。

```text
r02_live_status: R02_CLOSED_BLOCKED_PACKAGE_RELEASE
recommended_reclassification: SHELL_INSTALLER_ADAPTER_BINDING_REQUIRED + REAL_FIXED_CHILD_UNVERIFIED
recommended_reclassification_state: NOT_YET_EFFECTIVE
binding_delivery_owner: V2 Final-delivery Installer / Release Assembly Owner
binding_carrier: FINAL_WORKBUDDY_PACKAGEROOT / INDEPENDENT_SHELL_ADAPTER_SUBTREE
shell_owns: BINDING_SCHEMA_AND_CONSUMER
openmontage_0_3_25: IMMUTABLE / NO_WORKBUDDY_ADAPTER_EMBEDDING
```

正确的真实顺序是 `Registration identity validation -> Locator 返回已验证 PackageRoot/Guide identity/hash -> WorkBuddy 读取 Guide/Manifest/Pipeline/Stage Skills -> WorkBuddy 作生产决策 -> 隐藏的 bounded Shell transport -> WorkBuddy 按需发起一个或多个独立 deterministic package-local tool calls -> 机械 receipt/status/Artifact facts -> WorkBuddy 继续 review/checkpoint 并展示结果`。每个 tool call 内最多一个 fixed child；不得把整项用户请求锁成一个 child。Guide-read、identity/hash 和顺序必须由独立可见的 WorkBuddy/client 证据证明；模型自报、child 自报、普通日志、静态测试、CI 或 receipt 单独不能替代。最终 Package 必带 Node.js `22+`、npm、npx；Stage 3 不探测、下载或替换 Node/npm/npx。

### [HISTORICAL / SUPERSEDED_BY_2026-08-24_REBASELINE] A7 残留对象与 B01-B07 执行边界

旧 Stage 2 分支 `codex/v2-s2-official-package-alignment-b1`（`86a7902465d8e215e0830b9640e7222d7c7f5188`，含 `9b8ebb2`、`8d4461d`、`86a7902`）为 `SUPERSEDED_WITH_VALID_REASON / PRESERVE_HISTORY / DO_NOT_MERGE / DO_NOT_DELETE`。它把 assembled Package 对齐成 Git checkout 的方向不属于当前合同；需要的安全点只能在另行授权下按当前模型重做。两个 dirty detached worktree `C:\Users\blazi\.codex\worktrees\aef5\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2`、`C:\Users\blazi\.codex\worktrees\df76\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2`（均 `4d74d6576773dc9d383efec091bdc8d42f0d480c`）仅登记，不复制、不提交、不回收、不删除。

A7 当时的纠偏计划为 `B01 -> B02 -> B03 -> B04 -> B05 -> B06 -> B07`；其 21 字段合同只保留为历史 provenance，已无执行效力。随后一轮当时的唯一候选是 C01-C07；若本文 D 路线候选正式推广，该句只记录历史时序，不再提供路由。

本 Phase A 状态镜像只涉及六个既有权威文件，保持 `DOCS_ONLY / ZERO_PRODUCT_STATE_CHANGE / NOT_RUN_DOCS_ONLY`，不触碰产品代码、测试、CI、Package、外部仓库、客户端、Provider、媒体、Registration、Activation 或 DataRoot。A7 审计结果已由用户批准并以普通 fast-forward 正式推广；本次状态收口提交使用 `THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR`，避免自引用 hash。原 Phase A 任务工作树、本地任务分支和远端任务分支已清理；旧 Stage 2 分支与两个 dirty detached worktree 继续保留。上方 Phase A 镜像中的 `NOT_AUTHORIZED` 与下方 B01-only 镜像都只作历史；当前权威是 2026-08-24 重基线的 `PAUSED_BY_OWNER`。

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

## [HISTORICAL / SUPERSEDED_WHEN_D_ROUTE_CANDIDATE_IS_FORMALLY_PROMOTED] 当前状态：Phase B 已暂停并完成方案重基线候选（2026-08-24）

```text
current_authority: V2-PROJECT-ARCHITECTURE-RECOVERY-PLAN-REBASELINE-AUDIT1
phase_b: PAUSED_BY_OWNER
current_product_task: NONE
product_code_change: 0
package_change: 0
workbuddy_change: 0
provider_or_media_change: 0
formal_baseline: 6457d475ee43b291c7ac34ad42f9f48aaaaa1390 / tree d296e4ab98f8d6908e03360bea7d9c04b8ea06cc
official_input: cd9f3c1f03368be87b140af494914b8ee4e3c7a4 / tree 6cd1961d552dd9d2bcfba990b80ac06edfe4b061 / DETACHED_CLEAN
golden_key_input: 73cab67322451601a824875c0e426067d736dd44 / tree 29231e0464fa4bc7533c1928415849e9b3a48e7c / DETACHED_CLEAN
historical_next_active_task: NONE / C01_REQUIRES_OWNER_AUTHORIZATION / SUPERSEDED_WHEN_D_ROUTE_CANDIDATE_IS_FORMALLY_PROMOTED
```

真实裁决：原 `A0-A6_APPROVED` 聚合状态降级为历史自述，不再是当前权威判断。A0 的精确基线/分支接管事实可保留，但当前仓库没有逐任务 Reviewer 证据；A1 的目标重建正确但原强制追踪矩阵缺失，本重基线已在 TASK-REGISTER 逐项补齐；A2 原先没有审清遗留 Stage 2 分支内的 Windows stable-handle/reparse hardening，本重基线只读分类为独立未来候选；A3 原先没有逐项裁决两个 dirty worktree，本重基线已确认其为被正式 Stage3 取代的历史计划；A4 正确把 Stage4 降为机械合同历史 PASS，却没有裁决 fixed child 能否支撑完整用户请求；A5 正确识别真实集成与 R02 归属问题，但继承了 A4 未解决假设；A6 首次把该未证假设明确写成错误执行计划；A7 只保留推广事实。B01 是被取代的历史合同；B02 是最早落地这一偏差的产品实现，只有机械实现事实，未达到产品目标；B03 的装配、工具链、Registration/Locator 和生命周期证据可复用，但最终 Skill/Bridge 绑定不可复用为正确方案；B04 三次均未形成 Shell 成功，直接生成的策划文档属于 `DIRECT_WORKBUDDY_FALLBACK`。

正式台账在此前只记录到“B01 已授权”，而正式分支已包含 B02 代码且外部已产生 B03/B04 结果。该状态漂移由本重基线显式封闭；历史提交和证据保留，不 reset、不删除、不倒写成从未发生。

## [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] 新任纠偏执行路线候选状态历史快照（2026-08-24；D01-D08 路线）

本节及其所含 D01-D08 路线字段均为历史记录，不参与当前路由；当前唯一 authority/route 为最新 E01→E07 correction（`V2-E01-ROUTE-BOUNDARY-CORRECTION1`）及六文档同名 current 节。

优先级规则：候选未被 Owner 推广时不改变正式状态；候选经 ordinary fast-forward 进入正式 ref 后，本文件所有较早指向 C01-C07 的 `current/next/only` 字段立即降为历史，下面的 D01-D08 候选状态成为最新 planning authority，但仍保持 `execution_authority: NONE`。

```text
candidate_authority: V2-CORRECTION-EXECUTION-PLAN-AUDIT1 / NOT_FORMAL
planning_base: 5e8c7c1b1bf59d284996e16ff5aeea8ce55c614c / tree 829d506de0ca7e256eff9338dd33ec773d150155
product_code_baseline: 6457d475ee43b291c7ac34ad42f9f48aaaaa1390 / tree d296e4ab98f8d6908e03360bea7d9c04b8ea06cc
candidate_branch: codex/v2-correction-execution-plan-audit1
scope: SIX_AUTHORITY_DOCS_ONLY
tests: NOT_RUN_DOCS_ONLY
product_code_change: 0
package_change: 0
workbuddy_change: 0
provider_or_media_change: 0
current_product_task: NONE
execution_authority: NONE
old_C01_C07: SUPERSEDED_CANDIDATE / NEVER_EXECUTE
new_route: D01 -> D02 -> D03 -> D04 -> D05 -> D06 -> D07 -> D08
next_possible_action: OWNER_REVIEWS_PLAN_CANDIDATE
```

现行 C01-C07 不能安全续跑：C01 把 client surface probe 与产品路径混测；C04 仍把 Installer 留在 D 盘临时脚本；C05 允许用首个 Artifact 代替完整成片；C06 同时要求 Skill hash 不变又继承把 Package identity 写进 Skill 的旧合同。新候选把证据链拆成八个不可并行、不可跨越的任务：D01 client-native surface；D02 Agent-first 合同；D03 最小产品实现；D04 版本化 Installer；D05 fresh 双 assembly；D06 official 完整成片 control；D07 只切 0.3.25 的同路径完整成片；D08 真实业务与 closeout 候选。

当前已证明的只包括 exact Git/Package 输入、B02 的机械代码事实、B03 的装配/生命周期方法证据和 B04 的三次负面事实。D01 surface、正确实现、版本化 Installer、fresh assemblies、official/GK 完整成片及业务 E2E 均为 `NOT_PROVED`。候选 Reviewer 只能判断规划是否完整且未偏离，不能把任何 `NOT_PROVED` 项升级为产品 PASS。

## [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] D01 合同纠偏候选 Replacement1 状态镜像历史快照（2026-08-24）

本节及其所含 D01 Replacement1 合同均为历史记录，不参与当前路由；当前唯一 authority/route 为最新 E01→E07 correction（`V2-E01-ROUTE-BOUNDARY-CORRECTION1`）及六文档同名 current 节。

本节为 append-only 当前优先级候选；在独立零写 Reviewer、单独 Owner 推广批准、ordinary fast-forward 进入 live formal ref 并核验远端对象之前，仍是 `CANDIDATE_NOT_FORMAL`，不改变 `PAUSED_BY_OWNER`，不授权 D01。纠偏基线固定为 `99bc5c3d727671d7d2ea7313c6851792583efe66` / tree `b995a9a02add77f1e61769f364dd86b341137403`；`tests=NOT_RUN_DOCS_ONLY`，product/package/workbuddy/provider/media changes 均为 `0`。候选 commit 只允许在独立纠偏 Reviewer 审核 exact final six-doc diff 通过后形成；push 与正式推广是后续分离决定。

Gate0 只读核验 live formal、正式 authority 与当前 WorkBuddy binary identity；B04 read scope 仅为唯一 root `D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_B04_official_evidence\workbuddy-client\` 下的精确 13 项。`B04NegativeEvidenceManifestV1` canonical manifest 输出到 `D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_D01_native_surface_evidence\inputs\B04-NEGATIVE-EVIDENCE-MANIFEST.v1.json`，manifest self-hash 不写入，完整字节 SHA256 仅记录在 Gate-0 takeover；不得读取 PackageRoot/assembly。Gate1 在任何 import/client mutation 前由独立零写 Reviewer 对 exact source tree/fixtures/ZIP listing+bytes+hash、两条 literal ordinary-language prompts、permissions/evidence plan 返回 `PRE_RUN_APPROVE`；Gate2 由 Owner 导入并完成两 fresh sessions；Gate3 冻结证据并返回 `APPROVE_FOR_TASK_CLEANUP`；仅在该 token 后 Gate4 Owner 卸载 exact Skill、关闭两 session、删除 exact source+ZIP、捕获 after-state，由 Closeout Worker 写 result 与十问，再由独立零写 Reviewer 对 exact final evidence/docs 返回 `FINAL_APPROVE`。任一 Gate 失败保持 `D02-D08 NOT_AUTHORIZED`，禁止补探测或 repair window。

## [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] Owner 紧急目标重置：旧项目状态快照（2026-08-24；目标/路线骨架保留）

本节保留目标与 E01→E07 路线骨架；其 formal base、active/current task、D01-D08 status、权限、角色和 Git 状态字段均为历史快照。最新唯一 current authority 是下方 `V2-E01-ROUTE-BOUNDARY-CORRECTION1` 节及 TASK-REGISTER 同名节。

```text
active_task: V2-PROJECT-GOAL-AND-D-ROUTE-REAUDIT1
active_scope: READ_ONLY_FACT_AUDIT + EXACT_SIX_PLANNING_DOCS_CORRECTION
formal_base: b7bd6bc201f821f83d019c5b7addd8ec198d7ecf / tree daa4ed62e94cf9105358cb452b4950a134d7e2ef
D01_D08: UNTRUSTED_PENDING_REAUDIT / NO_EXECUTION_AUTHORITY
D01_raw_observation: RETAIN_AS_HISTORICAL_FACT_ONLY
D01_old_product_conclusion: INVALIDATED_BY_MISALIGNED_TEST_DESIGN
current_execution: PAUSED_BY_OWNER
tests: NOT_RUN_DOCS_ONLY
commit_push_formal_delivery: NOT_AUTHORIZED
```

当时只允许核对原始目标、既有事实和规划内容。Shell 的产品价值是降低普通用户门槛并提供继续完成任务所需的环境、配置、命令和提示词引导；WorkBuddy 是唯一 Agent 和生产决策者。PowerShell/Bash/CLI 不因其技术形态自动失败。任何不能直接说明所消除用户门槛、要求模型猜内部路径/绑定/命令、绕过 OpenMontage Guide/Pipeline、或让 Shell 接管生产决策的路线都必须停止。禁止继续 WorkBuddy 探测、产品代码、Package、Provider、媒体和 D02-D08 执行。

### [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] E01 审计候选结果镜像状态快照

```text
candidate_route: E01 -> E02 -> E03 -> E04 -> E05 -> E06 -> E07
E01: IN_PROGRESS / DOCS_ONLY_CANDIDATE / UNCOMMITTED
E02_E07: NOT_AUTHORIZED
D01: DELETE_AS_PRODUCT_GATE / RAW_FACTS_ONLY
D02_D03: REPLACE_SEMANTIC_OPERATION_AND_ADAPTER_PREMISES
D04_D08: KEEP_ONLY_USER_GOAL_ALIGNED_PARTS
current_changes: EXACT_SIX_AUTHORITY_DOCS_ONLY
```

历史快照中的下一步曾是 E01 exact six-doc diff 的独立零写复审；该字段不授权 commit、push、`FORMAL_DELIVERY` 或 E02。

## [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] E 系列逐任务执行包规划状态快照（2026-08-25；E01→E07 路线骨架保留）

```text
route_candidate_commit: 533fb410fda837259afa29e2bb2fdee76caca599
route_candidate_tree: b0b0879cd84962eb3676f9cda43b9a89cf7238b5
route_candidate_branch: refs/heads/codex/v2-goal-and-route-reaudit1
route_candidate_remote: PRESENT
formal_head: b7bd6bc201f821f83d019c5b7addd8ec198d7ecf
formal_tree: daa4ed62e94cf9105358cb452b4950a134d7e2ef
formal_delivery: NOT_DONE
current_docs_task: V2-E01-EXECUTION-PACKETS-PLANNING-CORRECTION1 / UNCOMMITTED_SIX_DOC_CANDIDATE
current_effect: DOCS_ONLY / ZERO_PRODUCT_CLIENT_PACKAGE_EFFECT
planner: OWNER_EXPLICIT_PLANNING_AUDIT_COORDINATOR / HANDOFF_REQUIRED
executor: FUTURE_FRESH_EXECUTION_CONVERSATION / ONE_APPROVED_PACKET_ONLY
closeout_worker: DISTINCT_FROM_EXECUTION_WORKER / AUTHORITY_DOCS_ONLY_AFTER_EVIDENCE_FREEZE
reviewer: INDEPENDENT_ZERO_WRITE
E02_E07: NOT_AUTHORIZED
forbidden_now: WORKBUDDY_PROBE_CODE_TEST_PACKAGE_REGISTRATION_INSTALLER_PROVIDER_MEDIA_COMMIT_PUSH_FORMAL_DELIVERY_CLEANUP
next: COMPLETE_PACKET_DOCS -> INDEPENDENT_ZERO_WRITE_REVIEW -> OWNER_GIT_DECISION
```

旧的“E01 未提交/未推送”字段以及上方 route/formal/status/role 字段均为候选首次交付前历史快照。E01→E07 目标/路线骨架保留；新的详细合同只以 TASK-REGISTER 最后同名纠正节为准：每项必须先通过 formal authority、用户价值、输入身份、exact packet、独立 pre-execution review 和绑定 packet SHA256 的 Owner 单任务执行 token；适用 Package/client/Provider/rollback/cleanup 各自另 token。执行后必须先冻结证据，再审核、再获 Reviewer cleanup verdict 与 Owner cleanup token、再捕获 after-state。最新唯一 current authority 是下方 `V2-E01-ROUTE-BOUNDARY-CORRECTION1` 节及 TASK-REGISTER 同名节。

Git 唯一状态机是 `REVIEW_APPROVE -> OWNER_COMMIT_AUTHORIZATION -> CANDIDATE_COMMIT -> OWNER_PUSH_AUTHORIZATION -> CANDIDATE_PUSH -> OWNER_FORMAL_DELIVERY_AUTHORIZATION -> ORDINARY_FAST_FORWARD_FORMAL_REF -> REMOTE_COMMIT_TREE_VERIFICATION -> CI_HEADSHA_SUCCESS_IF_REQUIRED -> FORMALLY_DELIVERED -> OWNER_NEXT_TASK_AUTHORIZATION_SEPARATE`。E 路线不复用更早历史节中的旧交付标签，也不存在额外 Git 动作。

## [HISTORICAL / SUPERSEDED_BY_V2-E01-ROUTE-BOUNDARY-CORRECTION1] E01 文档正式收口候选（2026-08-25）

```text
closeout_task: V2-E01-DOCS-FORMAL-CLOSEOUT1
scope: DOCS_ONLY / EXACT_SIX_AUTHORITY_FILES / ZERO_PRODUCT_STATE_CHANGE
planning_delivery_commit: 1ad4aa136b99d73e76a6f8847b7deb7d064649d0
planning_delivery_tree: 6db61922d6c07c3ff337dbaa761ca6d65c080bbf
planning_delivery_ref: refs/heads/codex/workbuddy-shell-v2 / VERIFIED
planning_delivery_method: ORDINARY_FAST_FORWARD / NO_FORCE_NO_MERGE_NO_REBASE
planning_delivery_ci: run 32809470079 / completed / success / headSha=1ad4aa136b99d73e76a6f8847b7deb7d064649d0 / 395 passed / 1 skipped
planning_payload_state: FORMALLY_DELIVERED
closeout_review_gate: INDEPENDENT_ZERO_WRITE_APPROVE_REQUIRED
closeout_result: THIS_COMMIT / SELF_RESOLVING_FORMAL_MIRROR
closeout_delivery_resolution: INDEPENDENT_ZERO_WRITE_APPROVE + LIVE_FORMAL_REF_CONTAINS_THIS_COMMIT + EXACT_HEAD_CI_SUCCESS
E01_final_state: FORMALLY_DELIVERED_WHEN_CLOSEOUT_DELIVERY_RESOLUTION_IS_TRUE
current_task: NONE / NO_ACTIVE_TASK_AFTER_E01_CLOSEOUT
E02_E07: NOT_STARTED / NOT_AUTHORIZED
next_authorized_task: NONE / SEPARATE_OWNER_E02_AUTHORIZATION_REQUIRED_IN_NEW_TASK
local_tests: NOT_RUN_DOCS_ONLY
cleanup: NOT_INCLUDED / SEPARATE_OWNER_AUTHORIZATION_REQUIRED
```

本节保留首次 closeout 的历史事实；其 `FORMALLY_DELIVERED` 结论不再代表当前 E01 零缺陷或 E02 可启动。最新状态见下方 `V2-E01-ROUTE-BOUNDARY-CORRECTION1`。

## V2-E01-ROUTE-BOUNDARY-CORRECTION1（2026-08-25，当前候选）

本候选基于正式基线 `419373094e7ac4e1a5f092d25d8e62cef8a76a6d` / tree `bf2210f9c63661e10f16188faf860f27b2278390`，只允许六份 authority docs。此前 E01 closeout 事实保留为历史；后续 goal-boundary audit 记录为 `REJECT / P0=0 / P1=7 / P2=3`，所以 E01 重开为 docs-only correction candidate，E02-E07 阻断。

```text
task_id: V2-E01-ROUTE-BOUNDARY-CORRECTION1
branch: codex/v2-e01-route-boundary-correction1
state: DOCS_ONLY / CORRECTION_CANDIDATE / NOT_FORMALLY_DELIVERED
allowlist: EXACT_SIX_AUTHORITY_DOCS
route: E01 -> E02 -> E03 -> E04 -> E05 -> E06 -> E07
E02_E07: NOT_STARTED / NOT_AUTHORIZED / BLOCKED_BY_E01_CORRECTION
tests: NOT_RUN_DOCS_ONLY
review: INDEPENDENT_ZERO_WRITE_REVIEW_OF_EXACT_DIFF_REQUIRED
```

最低目标是普通用户在 WorkBuddy 中用自然语言请求结果；WorkBuddy 是唯一运行 Agent、用户对话主体和生产决策者；它在读取 verified OpenMontage Guide/Manifest/Pipeline/Stage/Tool/Reviewer/Checkpoint authority 后，按该 authority 作出 Pipeline/Stage/Tool/Review/Checkpoint/Provider/Renderer/内容决策；OpenMontage 是生产语义权威，不是第二运行 Agent；Shell 只承担安装、环境/定位、受控机械执行、入口、状态/结果 relay 和可执行引导，最终在真实 WorkBuddy 产出真实完整可播放视频。不能直接降低该链路用户门槛的功能、模块或约束不得进入后续任务。

内部命令边界：普通用户不得被要求理解、构造或看到内部 path/hash/schema/env/argv/transport；WorkBuddy/model 不得猜测、自由合成或从用户输入推导这些值；WorkBuddy/固定 Skill 可接收并调用由 verified Package/Shell 提供、identity-checked、allowlisted 的 exact mechanical operation。引导边界：Shell 可基于 verified mechanical state 返回 bounded/deterministic 的环境、配置、command、prompt、next-step remediation facts/options/material；Shell 不理解业务意图、不发起 consent、不选择 recovery、不推进生产；WorkBuddy 独占面向用户的解释/呈现、consent、recovery/continue、生产语义和业务决策。

E02 evidence root 固定为 `D:\BlazingCD\Temp\Golden_Key_WorkBuddy_V2_E02_User_Journey_Minimal_Change_Audit1`，固定载体为 `packet/E02ExecutionPacketV1.json`、`inputs/E02InputManifestV1.json`、`handoff/E02TakeoverV1.json`、`reports/E02ExecutionReportV1.json`、`evidence/E02EvidenceIndexV1.json`；UTF-8 no BOM/LF/final LF，原始字节 SHA256 绑定。Planner 只写 `packet/`、`inputs/`，并且只能在 Owner 授权后记录 `handoff/E02TakeoverV1.json`；Execution Worker 只写 evidence root 的 `reports/`、`evidence/`，Closeout Worker 只写六文档，Reviewer 全零写。

E02 固定十条旅程：安装/首次打开/环境就绪、具体需求、模糊需求/guided entry、Package 缺失/未验证、环境缺漏、配置/consent/可选能力、verified Guide/Manifest handoff、执行错误/恢复、结果/receipt/video relay、安全卸载/回滚/数据保全。E04 owner 为 `V2 Final-delivery Installer / Release Assembly Owner`，并分离 immutable official/GK source、Shell-adapter binding、final assembly/Manifest/Lock 责任；E04 不发明生产逻辑。

E05/E06 视频必须由真实 WorkBuddy、verified authority 和真实工具产生，非 fixture/mock/demo/fallback，竖屏、可播放、非零时长，lineage/receipt 可审且无手工绕行。same=ordinary-language user journey、business brief/materials、applicable consent/cost scenario、Shell responsibilities、client/model where supported and frozen、acceptance/evidence method；allowed-different=Package-owned Guide/Pipeline/Stage/tool、source-attributed package-specific Skill metadata/text/binding、derived creative decisions/artifacts；fail=额外用户技术负担、第二控制面、手工绕行/fallback、未在 comparison manifest 归因的控制变量漂移。不要求 Skill ZIP、model、client 或全部非-Package 字节机械相同。Planner 只能是 Owner 显式指派的 `Planning/Audit Coordinator`，handoff 绑定 Owner identity、record ID、issued/expires、exact formal commit/tree/task/packet SHA/allowlist/forbidden；E03 仅 `OFFLINE_CONTRACT_ONLY` 直到另有 `OwnerClientActionAuthorizationV1`。

本轮 Owner 条件授权为：独立 Reviewer 先审 unstaged exact diff 并通过后允许 candidate commit；commit 后由零写核验 exact commit/tree 与已审字节一致并给出 post-commit binding `APPROVE`，随后允许 push 到专用候选分支。该候选不等于 `FORMAL_DELIVERY`，不授权 E02。禁止产品代码、测试、WorkBuddy、Package/Registration/Installer、Provider、媒体、客户端和 cleanup。

## V2-E02-EXECUTION-PLAN-FREEZE1（2026-08-25，docs-only 候选镜像）

本节与 TASK-REGISTER 同名节镜像 E02 的完整执行规划；它只形成 `THIS_COMMIT / SELF_RESOLVING_REMOTE_CANDIDATE_CONTAINMENT`，不改变 E01 formal/candidate 状态，不启动 E02。

```text
plan_freeze_task: V2-E02-EXECUTION-PLAN-FREEZE1
execution_task: V2-E02-CURRENT-JOURNEY-MINIMAL-CHANGE-AUDIT
scope: DOCS_ONLY / EXACT_SIX_AUTHORITY_FILES / ZERO_PRODUCT_STATE_CHANGE
formal_base: 271dee394bed5ca3dd5c31860c842a8cbfdfa536 / tree 8eea24e3bc3fc5f4c6eed536281799edaebdde40
packet_sha256: ddbd68018506f4df90a6c0bb49bd3d2127c5d77ee980ea890d5e02da2bb0c1a0
input_manifest_sha256: 5345a83d628c22e45e8265509af30dd8d77abca7aaab5c44ff6dca8737cf1956
plan_review: INDEPENDENT_ZERO_WRITE_APPROVE / P0=0 / P1=0 / P2=0
e02_state: NOT_STARTED / NOT_AUTHORIZED
handoff_report_evidence: NOT_CREATED
required_before_execution: PRE_EXECUTION_REVIEW + OwnerTaskExecutionAuthorizationV1
e03_e04: BLOCKED_BY_E02_CHAIN
```

目标是只读找出普通用户从安装、首次打开、自然语言需求到真实结果之间的真实阻断，并将其路由到最小后续动作；不为 E03/E04 凑功能。九阶段固定为 `P0 TAKEOVER_AND_FAIL_CLOSED`、`P1 EXACT_INPUT_VERIFICATION`、`P2 TARGET_JOURNEY_BASELINE`、`P3 CURRENT_FLOW_STATIC_TRACE`、`P4 ASSET_CLASSIFICATION`、`P5 MINIMAL_CHANGE_TRACE`、`P6 REPORT_AND_EVIDENCE_FREEZE`、`P7 INDEPENDENT_RESULT_REVIEW`、`P8 CLOSEOUT_BOUNDARY`。

十条固定旅程按此顺序：`install-first-open-environment-ready`、`specific-request`、`vague-request-guided-entry`、`package-absent-or-unverified`、`required-environment-missing`、`configuration-consent-optional-capability`、`verified-guide-manifest-handoff`、`execution-error-recovery`、`result-receipt-video-relay`、`safe-uninstall-rollback-data-preservation`。每条必须填同一 16 字段：`journey_order`、`journey_id`、`ordinary_user_start_state`、`ordinary_user_action`、`expected_user_visible_outcome`、`responsibility_chain`、`exact_inputs_examined`、`current_static_capability`、`confirmed_user_blockers`、`evidence_refs`、`journey_status`、`candidate_disposition`、`candidate_change_refs`、`visible_copy_or_accessibility_risks`、`negative_case`、`cannot_prove`。

七个结构化输出合同为 `blocker_record`、`candidate_change_record`、`bidirectional_trace_record`、`downstream_boundary_record`、`fact_record`、`deviation_or_stop_record`、`evidence_index_record`。证据必须绑定 exact Git blob 或 external file，并有必需 `source_locator`（行号范围、symbol、markdown heading 或 json pointer）；动态 URL 在 E02 中禁止。七组资产为 `current_registration_locator`、`current_optional_runtime`、`current_launcher_and_entry`、`current_package_exports_and_hygiene`、`historical_guidance_and_lifecycle`、`documentary_package_comparison`、`historical_raw_negative_evidence`；资产只可 `KEEP/REWORK/REMOVE/NO_CHANGE/NOT_PROVED`。十一组 exact input 为 `e01-current-authority`、`package-registration-contract-documentary`、`current-shell-source-tests-skill`、`original-v2-handoff-owner-snapshot`、`historical-v2-next-session-handoff`、`historical-guided-skill`、`historical-installer-lifecycle-assets`、`official-openmontage-documentary-source`、`golden-key-0.3.25-documentary-source`、`b04-raw-negative-evidence`、`d01-historical-manifest`。

最小路由只有 `E03_CANDIDATE`（入口/引导/错误解释/呈现）、`E04_CANDIDATE`（安装/装配/生命周期/binding）、`NO_CODE_CHANGE_REQUIRED` 和 `NOT_PROVED`；每个改动必须有普通用户 blocker，跨 E03/E04 必须拆分。WorkBuddy 是 sole Agent，OpenMontage 是 semantic authority，Shell 仅 support/mechanical；禁止第二控制面、技术负担和真实客户端/视频 overclaim。E02 仍为 static read-only；Planner、Execution Worker、Closeout Worker、Reviewer 四方分离，分别受 packet 写域约束；计划固化不等于执行授权、formal delivery 或 cleanup。

## V2-E02-NONRECURSIVE-BINDING-CORRECTION1（2026-08-25，状态镜像）

旧 exact-live-equality 绑定已由本节取代；本节只镜像非递归 lineage，不改变 E02 的完整执行合同或任何产品边界。

```text
evidence_product_baseline: 271dee394bed5ca3dd5c31860c842a8cbfdfa536 / tree 8eea24e3bc3fc5f4c6eed536281799edaebdde40
formally_delivered_authority_floor: 1713ba8d0d3279233d702339548a242e40a1e759 / tree 38eddb5ccdbb000eb2048713c4b30a7f4e9e8d9b
floor_to_live_scope: exact six authority docs only; floor must be live formal ancestor
live_formal: resolve at PRE_EXECUTION_REVIEW; OwnerTaskExecutionAuthorizationV1 and E02TakeoverV1 lock exact commit/tree
packet_sha256: 4120acf17e204d78cedd743d3eb84b6491bbf1aef2b607df49c645e59eb930d4
input_manifest_sha256: aeeae389aeade2b992efbcf8f46c4f7372c4a5df57b16bb84b87ea57be69cad2
future_correction_commit: NOT_EMBEDDED_IN_PACKET
lineage_stop: STOP_FORMAL_LINEAGE_OR_SCOPE_MISMATCH
e02: NOT_STARTED / NOT_AUTHORIZED
```

Current-repository manifest inputs remain exact at the evidence/product baseline; historical and external inputs retain their own frozen identities. Any unresolved live object, non-six-doc floor-to-live delta, baseline drift or token mismatch stops before execution.
