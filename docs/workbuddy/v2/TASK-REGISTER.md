# WorkBuddy Shell V2 任务账本

状态：`V2-S3-RUNTIME-PREPARE-BUILDER1 / AUTHORIZED_NOT_STARTED`

更新时间：2026-08-18

## 当前任务

```text
task_id: V2-S3-RUNTIME-PREPARE-BUILDER1
task_status: AUTHORIZED_NOT_STARTED
task_kind: STAGE3_IMPLEMENTATION / BOUNDED_OPTIONAL_CAPABILITY_DETECTION_AND_USER_AUTHORIZED_INTEGRATION
user_authorization: 2026-08-18 / 用户明确要求现在启动阶段三、独立Builder和Reviewer、跟踪至完成、禁止膨胀
stage_3_execution_user_authorization: 2026-08-18 / GRANTED / 启动阶段三执行；独立Builder与Reviewer；持续跟踪直至阶段三完成；严禁边界膨胀
implementation_authorization: GRANTED
immutable_code_baseline: 061ac8428823c8732f241b01a7fd9e54a732599a
builder_start_commit: THIS_COMMIT / 语义为包含本授权的正式提交；未来Builder必须先验证HEAD=实时origin/codex/workbuddy-shell-v2=本授权提交
previous_contract_candidate: 061ac8428823c8732f241b01a7fd9e54a732599a / APPROVE / FORMALLY_PROMOTED
start_commit: 061ac8428823c8732f241b01a7fd9e54a732599a
result_commit: THIS_COMMIT
branch: codex/v2-s3-runtime-authorize1
formal_target_branch: origin/codex/workbuddy-shell-v2
formal_target_at_start: 061ac8428823c8732f241b01a7fd9e54a732599a
review_range: 061ac8428823c8732f241b01a7fd9e54a732599a..THIS_COMMIT
reviewer_range: THIS_COMMIT..BUILDER_RESULT_COMMIT / INDEPENDENT_ZERO_WRITE
independent_review: PREVIOUS_CONTRACT_CANDIDATE=APPROVE / P0=0 / P1=0 / P2=0
formal_promotion: PREVIOUS_CONTRACT_061AC8428823C8732F241B01A7FD9E54A732599A=COMPLETED / THIS_AUTHORIZATION_COMMIT=NOT_STARTED / BUILDER_MUST_NOT_START_BEFORE_THIS_COMMIT_IS_FORMALLY_PROMOTED
repository_allowed_paths: docs/workbuddy/v2/TASK-REGISTER.md
production_code_changes: 0
test_changes: 0
ci_changes: 0
new_tracked_files: 0
tracked_files_expected: 33
external_writes_performed: NONE
task_temp_root_status: NOT_CREATED
previous_contract_result: STAGE_3_BOUNDED_DETECT_REPORT_AND_USER_AUTHORIZED_INTEGRATION_CONTRACT_CORRECTED
previous_planning_result: USER_PRODUCT_MODEL_CORRECTION_REVIEW_APPROVED / FORMALLY_PROMOTED_AT_061AC8428823C8732F241B01A7FD9E54A732599A
current_correction_reason: USER_PRODUCT_MODEL_CORRECTION / remove inflated Package Release declaration, capability Lock, Registration and task-only Package gates from Stage3; optional capabilities are detected and integrated only by explicit user consent
user_correction_record: a real candidate Release is not a Stage3 input; Remotion and HyperFrames are optional OpenMontage capabilities; Stage3 may implement after this five-document correction is formally promoted and an exact Builder packet is granted
stage_3_true_remaining_inputs: THIS_AUTHORIZATION_COMMIT_FORMAL_PROMOTION_ONLY
single_transaction: bounded detect Remotion and HyperFrames -> report PRESENT/MISSING/INCOMPATIBLE -> zero-download per-capability plan -> WorkBuddy asks -> approve integrates only named items / decline or defer returns SKIPPED -> verify and report
product_code_paths: golden_key_openmontage_workbuddy/runtime_prepare.py; export-only golden_key_openmontage_workbuddy/__init__.py; tests/workbuddy/test_runtime_prepare.py
acceptance_infrastructure_paths: tests/workbuddy/test_repository_hygiene.py; .github/workflows/ci.yml
future_builder_exact_path_count: 5 / 3 product paths + 2 existing acceptance-infrastructure edits
acceptance_infrastructure_reason: current fixed-33 hygiene assertions forbid the two new tracked files and current CI omits the direct Stage3 test; both must change atomically with implementation so the accepted tree and executed suite remain exact
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
validation_diff_check: PASS / exact one-file scope / untracked 0 / git diff --check exit 0 / current Stage3 authorization fields consistent
validation_full_test: NOT_RUN / repository .venv absent / no global Python or dependency installation used
validation_scope: docs/workbuddy/v2/TASK-REGISTER.md only / production=0 / tests=0 / CI=0 / new tracked=0 / tracked total=33
future_final_package_gate_rule: final persistent Release/sidecar, production PackageRoot and production Registration/Activation move to later final-delivery or Installer closeout; complete no later than Stage5 real WorkBuddy entry and production acceptance
future_cleanup_rule: always remove task-owned temp/staging on success or failure; never touch foreign objects; explicitly report any partial Release/PackageRoot/Registration state
forbidden_scope: Release; Registration; Installer; Launcher; WorkBuddy; Provider; media; CLI; MCP; service; database; second public entry; generic framework; any sixth path
next_authorized_task: V2-S3-RUNTIME-PREPARE-BUILDER1
next_task_authorization: GRANTED
next_task_start_commit_rule: THIS_AUTHORIZATION_COMMIT must first be formally promoted; then Builder must verify HEAD=live origin/codex/workbuddy-shell-v2=that exact authorization commit before any write
exact_allowed_paths: golden_key_openmontage_workbuddy/runtime_prepare.py; golden_key_openmontage_workbuddy/__init__.py; tests/workbuddy/test_runtime_prepare.py; tests/workbuddy/test_repository_hygiene.py; .github/workflows/ci.yml
next_task_exact_allowed_paths: golden_key_openmontage_workbuddy/runtime_prepare.py; golden_key_openmontage_workbuddy/__init__.py; tests/workbuddy/test_runtime_prepare.py; tests/workbuddy/test_repository_hygiene.py; .github/workflows/ci.yml
next_task_forbidden_scope: Release; Registration; Installer; Launcher; WorkBuddy; Provider; media; second public entry; generic runtime framework; any sixth path
```

本次按用户权威撤销膨胀模型：真实Package、Registration和Package绑定能力元数据都不是Stage 3输入。Stage 3只对Remotion和HyperFrames做有界探测与事实报告，对缺失/不兼容项生成零下载计划，并在WorkBuddy取得用户逐能力明确同意后集成批准项；拒绝或暂缓返回`SKIPPED/NOT_INTEGRATED`。没有新增生产代码、测试、CI、Package字节或外部写入。未来实现仍为三个产品路径加两个验收基础设施路径。阶段2临时ZIP `f00e83d6154e7593b765a3d6c863b6653fc642818133acd7924f3fd91aab5d03`只保留历史证据边界，不是Stage 3输入。

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

纠偏后的Stage 3编码顺序只剩：本五文档纠偏完成独立审阅和正式推广，然后由live authority给出精确Builder基线、五路径白名单和Reviewer范围。不得增加Package、Registration、Package绑定能力元数据、task-only登记验证或Stage 5输入Gate。持久最终Package与生产Registration仍在后续最终交付或Installer Gate收口，但不阻塞Stage 3编码。当前任务不授权生产实现、外部对象或DataRoot写入。

## 当前正式状态

```text
formal_branch: codex/workbuddy-shell-v2
accepted_authority_result: ba0a84d93a4b26c09eaf7e2469d09c064c27710e
formal_handoff_before_current_correction: 068408f02c87a1eabeda58ea1ebce3df606c0a0c
accepted_correction_result: 7ba6ad64270c7ccdd7500e2a59b05cf55c73d7ed
formal_head_after_closeout: THIS_COMMIT
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
repository_tracked_files: 33
final_package_artifact: NOT_MATERIALIZED
installed_production_package_root: NOT_CREATED
production_package_registration: NOT_CREATED
production_package_activation: NOT_CREATED
stage_3_planning_authorization: CONSUMED_COMPLETE
stage3_planning: PASS_ACCEPTED_FORMALLY_PROMOTED_AT_061AC8428823C8732F241B01A7FD9E54A732599A
stage_3_implementation_authorization: GRANTED
stage_3_conditional_authorization: GRANTED / START_CONDITION=THIS_AUTHORIZATION_COMMIT_FORMAL_PROMOTION
stage_3_start_gate: BLOCKED_THIS_AUTHORIZATION_COMMIT_FORMAL_PROMOTION_ONLY
stage_3_final_package_dependency: NOT_REQUIRED_FOR_CODING_START
final_package_gate: DEFERRED_TO_FINAL_DELIVERY_OR_INSTALLER_CLOSEOUT_BEFORE_STAGE5_PRODUCTION_ACCEPTANCE
stage_3_package_release_input: NOT_REQUIRED
stage_3_registration_input: NOT_REQUIRED
stage_3_package_bound_capability_metadata: REMOVED_FROM_INPUT_MODEL
stage_3_consumer_interface_contract: PASS_ACCEPTED_FORMALLY_PROMOTED_AT_061AC8428823C8732F241B01A7FD9E54A732599A
stage_3_product_execution_contract: PASS_ACCEPTED_FORMALLY_PROMOTED_AT_061AC8428823C8732F241B01A7FD9E54A732599A
real_workbuddy_validation: DEFERRED_TO_STAGE_5_ACCEPTANCE
stage_3_execution_packet: AUTHORIZED / EXACT_5_PATHS
stage3_implementation: AUTHORIZED_NOT_STARTED
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
stage_3_to_6_scope_reduction: ACTIVE_REPLANNED_BOUNDARY
runtime_correction: REQUIRED_TOOLCHAIN_REFRESH_PASS_ACCEPTED
```

`709c8e880b144fa9e9be26e9feb5d776dd6025e2`完成了Stage 2必带工具链和Registration/Locator的真实临时证明；该历史事实不重开，但也不再作为Stage 3输入。五文档纠偏已由独立Reviewer批准并正式推广为`061ac8428823c8732f241b01a7fd9e54a732599a`，live authority现已精确授权Builder；当前唯一启动阻塞是包含本授权的提交自身尚未正式推广。

仓库卫生最终树基线仍为`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`，tracked精确33且等于固定白名单；该对象是已审规划结果`72719c758f092868fc6446e44a803d13eeae44a6`的祖先。阶段2刷新和阶段3规划都没有恢复已清理内容或增加tracked文件。

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
stage_3_future_builder_exact_allowlist_rule: exactly the 3 product paths plus the 2 existing acceptance-infrastructure paths; no other path; the latter only updates fixed tracked/API/source assertions and the one CI pytest command
stage_4_scope: 基础固定工具调用接受阶段2必带工具链事实；执行Remotion/HyperFrames前接受阶段3对该能力的PRESENT或INTEGRATED证据；缺失时可由OpenMontage选择其他已有/基础能力；阶段4不自行安装、不启动第二Agent、无任意Shell、无自动重试。
stage_5_scope: 用户实际运行起点；只保留一种真实WorkBuddy显式入口，literal user_message不变，技术控制独立。
stage_6_scope: 直接转交Runtime计划/准备事实与Launcher回执；仅有真实格式转换缺口时才允许独立实现；不解释、不安装、不重试。
stage_6_zero_code_exit: STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE
```

上述范围是规划边界，不是实现授权。任何需要阶段3扫描盘符、发现/下载/替换包内Python/FFmpeg/Node、一次安装全部可选能力、选择渲染引擎/版本、使用未批准海外默认源或覆盖外来目录，阶段4启动第二Agent、解析意图或调度任务，阶段5建立第二聊天Agent，阶段6解释Artifact或自动重试的方案，必须停止并返回`STOPPED_SCOPE_EXPANSION`。

## 阶段3重新规划合同

上一版阶段3执行包、`prepare_runtime_on_demand(...)`签名，以及Package绑定能力元数据、Registration绑定和零能力零代码模型全部`SUPERSEDED`，不得交给Builder。新阶段3只做Remotion和HyperFrames的有界探测、事实报告、零下载计划、逐能力用户决定和批准项受管集成。

### 实现启动Gate

以下两项全部满足前，阶段3生产代码变化必须为0：

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

- 阶段4基础调用只消费阶段2必带工具链事实；执行Remotion/HyperFrames时校验阶段3的`PRESENT`或`INTEGRATED`能力证据，不能自行安装。
- 阶段5拥有用户对话、计划展示、明确同意和真实WorkBuddy继续动作；真实验收优先同任务继续，不能时固定提示“继续刚才的任务”；技术控制与用户原话分离。
- 阶段6优先原样转交探测、`CONSENT_REQUIRED`、`INTEGRATED`、`SKIPPED`、`BLOCKED`和Launcher事实；不安装、不解释Artifact、不自动重试。
- Shell不得声称已无缝继续；阶段5真实WorkBuddy测试证明同一任务可继续后才允许该说法，否则由WorkBuddy要求用户回复“继续刚才的任务”。

### 最小文件和交付

未来产品实现最多新增`golden_key_openmontage_workbuddy/runtime_prepare.py`，最小编辑`golden_key_openmontage_workbuddy/__init__.py`导出唯一入口，并新增`tests/workbuddy/test_runtime_prepare.py`。同一Builder还必须只为验收同步编辑现有`tests/workbuddy/test_repository_hygiene.py`和`.github/workflows/ci.yml`，使固定tracked白名单、公共导出/源码断言和唯一CI pytest命令覆盖Stage 3。这两个文件不承载产品逻辑，也不授权第六个路径。不新增通用Runtime框架、`host_tools.py`、CLI/MCP、服务、数据库、后台进程、UI或通用下载器。交付为单一入口、稳定结果集、有界探测/计划/用户决定/集成事实、直接测试证据和阶段4可消费合同；不是Installer、最终Package、WorkBuddy入口、Launcher或视频E2E。

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
