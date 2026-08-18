# WorkBuddy Shell V2 任务账本

状态：`V2_FINAL_PACKAGE_GATE_ORDER_CORRECTION / PASS_ACCEPTED_AFTER_REVIEW_AND_FORMAL_FAST_FORWARD；FINAL_PACKAGE_GATE / BLOCKED_PACKAGE_CAPABILITY_LOCK`

更新时间：2026-08-18

## 当前任务

```text
authority_task_id: V2-FINAL-PACKAGE-GATE-ORDER-CORRECTION1
authority_status: PASS_ACCEPTED_AFTER_REVIEW_AND_FORMAL_FAST_FORWARD
authority_start_commit: d2a2aa5ce9a0b4c8735ec81da8fb1723bfb0e9e2
authority_initial_result_commit: 037ed38e1fb1e04af241d99ddf5a8a07592ae85c
authority_initial_review: REQUEST_CHANGES / P0=0 / P1=3 / P2=1
authority_result_commit: ba0a84d93a4b26c09eaf7e2469d09c064c27710e
authority_branch: DELETED_AFTER_FORMAL_FAST_FORWARD
authority_review_range: d2a2aa5ce9a0b4c8735ec81da8fb1723bfb0e9e2..ba0a84d93a4b26c09eaf7e2469d09c064c27710e
authority_final_review: APPROVE / P0=0 / P1=0 / P2=0
authority_promotion: ORDINARY_FAST_FORWARD / origin/codex/workbuddy-shell-v2=ba0a84d93a4b26c09eaf7e2469d09c064c27710e
authority_allowed_paths: PROJECT-STATE.md; docs/workbuddy/v2/TASK-REGISTER.md
authority_activation_condition: CONSUMED_COMPLETE
task_id: V2-PACKAGE-OWNED-OPTIONAL-CAPABILITY-LOCK-INPUT-GATE1
task_status: BLOCKED_EXTERNAL_PACKAGE_INPUT_REQUIRED
task_kind: EXTERNAL_PACKAGE_INPUT_GATE / NO_SHELL_IMPLEMENTATION
user_authorization: 2026-08-18 / 开始并尽快收尾，以便尽快启动阶段三；不得扩充边界或膨胀功能
implementation_authorization: NOT_GRANTED_IN_SHELL_REPOSITORY
start_commit: NOT_CREATED
start_commit_resolution: final Package gate cannot start before Package-owned capability Locks exist
result_commit: NOT_CREATED
branch: NOT_CREATED
formal_target_branch: origin/codex/workbuddy-shell-v2
formal_target_at_authority_start: d2a2aa5ce9a0b4c8735ec81da8fb1723bfb0e9e2
repository_allowed_paths: none until a separately authorized external-Package result is accepted
production_code_changes: 0
test_changes: 0
tracked_files_expected: 33
external_writes_performed: 0
task_temp_root_status: NOT_CREATED
source_repository: D:\BlazingCD\Personal\golden_key_short_video_agent-openmontage-agent-cleanroom
source_commit: 8395e578165e802990d53fef5a166f8b4cf0461a
source_package_tree_path: packages/golden-key-openmontage
source_package_tree: 0464861c5985c7c9072e789b94889d29cf9a937a
source_rule: git-object export only; source dirty worktree read/write/cleanup forbidden
candidate_release_f00e83_status: STAGE2_TEMPORARY_PROOF_ONLY / MUST_NOT_PUBLISH_AS_FINAL
ordering_correction: Package-owned capability Locks must be accepted before one-time final Package materialization and production Registration
remotion_existing_package_lock: remotion-composer/package-lock.json / Manifest-covered but NOT_ELIGIBLE_AS_STAGE3_CAPABILITY_LOCK
remotion_blockers: resolved host registry.npmjs.org; no package size fields; 8 entries without license; no approved-mainland plan schema or Stage3 target/probe contract
hyperframes_existing_package_lock: MISSING
hyperframes_blockers: runtime package/version not frozen; current Package text includes unpinned npx behavior and conflicting public package-name guidance; no mirror/hash/size/license/browser/target/probe contract
required_external_package_result: new immutable Package commit/tree/version containing Manifest-covered Remotion and HyperFrames capability Locks with exact package closure, approved mainland mirrors, hashes, sizes, licenses, targets, probes and browser assets only where required
required_consumer_result: real WorkBuddy/OpenMontage pause/consent/continue request contract bound to capability and Lock identity
future_final_package_gate_rule: run once only after both inputs; freeze exact wheel filenames/sizes/SHA-256 and a hash-locked deterministic assembly procedure; publish/install/register only the resulting new Package identity
future_cleanup_rule: always remove task-owned temp/staging on success or failure; never touch foreign objects; explicitly report any partial Release/PackageRoot/Registration state
forbidden_scope: Shell production code/tests/CI; ad-hoc modification of external dirty worktree; Shell-owned capability Lock; publishing f00e83 as final; Stage3 code; optional installation; WorkBuddy/Launcher/Provider/media
next_authorized_task: NONE_IN_SHELL_REPOSITORY
next_task_authorization: NOT_GRANTED_PENDING_EXTERNAL_PACKAGE_AND_WORKBUDDY_INPUTS
```

Reviewer确认直接发布`f00e83d6154e7593b765a3d6c863b6653fc642818133acd7924f3fd91aab5d03`会造成必然返工：阶段3要求的Package-owned能力Lock尚不存在或不合格，一旦补入就会改变Manifest、Release SHA、PackageRoot和Registration。因此本次没有创建临时根、下载、Release、PackageRoot或生产Registration。Shell仓库只记录正确顺序，不替外部Package发明Lock，也不以旧npm lock冒充阶段3合同。

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

上述证据证明完整工具链组装和登记能力，不证明最终交付Package仍存在。阶段2生产实现边界不因本次规划而扩张；最终Package持久构建、安装、生产登记和激活属于阶段3实现前的交付门禁，不得塞入阶段3Runtime代码。

正确顺序已改为：先由外部Golden Key OpenMontage Package产出Manifest覆盖的Remotion/HyperFrames能力Lock，并由真实WorkBuddy冻结消费者合同；再只生成一次最终Package、安装、生产登记/激活并做新进程Locator；最后才冻结阶段3 Builder任务包。当前Shell任务不授权修改外部Package，也不授权最终Package门禁或阶段3实现。

## 当前正式状态

```text
formal_branch: codex/workbuddy-shell-v2
formal_handoff_commit: d2a2aa5ce9a0b4c8735ec81da8fb1723bfb0e9e2
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
stage_3_planning_authorization: GRANTED_FOR_CURRENT_DOCS_ONLY
stage3_planning: PASS_ACCEPTED_AFTER_CLOSEOUT_REVIEW_AND_FORMAL_FAST_FORWARD
stage_3_implementation_authorization: NOT_GRANTED
stage_3_conditional_authorization: NOT_GRANTED
stage_3_start_gate: BLOCKED_FINAL_PACKAGE_AND_CONSUMER_CONTRACT
final_package_gate: BLOCKED_PACKAGE_CAPABILITY_LOCK
package_owned_capability_lock: MISSING_OR_INELIGIBLE
real_workbuddy_consumer_contract: NOT_FROZEN
stage_3_execution_packet: REPLANNED_BOUNDARY_PASS_ACCEPTED / IMPLEMENTATION_NOT_GRANTED
stage3_implementation: NOT_GRANTED
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
stage_3_to_6_scope_reduction: ACTIVE_REPLANNED_BOUNDARY
runtime_correction: REQUIRED_TOOLCHAIN_REFRESH_PASS_ACCEPTED
```

`709c8e880b144fa9e9be26e9feb5d776dd6025e2`完成了必带Python及47个锁定依赖、FFmpeg/ffprobe、Node/npm/npx的一次真实临时Package组装、Registration/Locator验证、负测、独立审阅和正式推广。临时构建根和task-only DataRoot随后已清理，所以`stage_2_status`只表示登记实现与临时证明通过，不表示最终分发物存在。阶段3规划可收口，实施仍被最终Package和消费者合同阻断。

仓库卫生最终树基线仍为`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`，tracked精确33且等于固定白名单；该对象是已审规划结果`72719c758f092868fc6446e44a803d13eeae44a6`的祖先。阶段2刷新和阶段3规划都没有恢复已清理内容或增加tracked文件。

## 阶段3至阶段6建设与交付顺序

```text
Stage 3: Runtime Preparation on Demand
Stage 4: Session Launcher
Stage 5: WorkBuddy Entry
Stage 6: Status and Result Relay
```

该顺序只表示建设、审阅和正式交付顺序，不是最终用户运行时的调用顺序。每个阶段都从当时最新的`origin/codex/workbuddy-shell-v2`精确提交开始，经单一有界Builder、独立只读Reviewer、普通非force fast-forward推广、远端临时分支清理和本地worktree关闭后，下一阶段才可接管。规划接受、Builder提交或Reviewer批准均不等于正式交付。

上一版`阶段5 -> 阶段2 -> 阶段3全闭集检查 -> 阶段4`运行链路已失效。新的固定关系是：阶段5触发阶段2 Locator重验最终生产Package；阶段4的基础固定工具调用只依赖阶段2必带工具链；WorkBuddy/OpenMontage形成并锁定Remotion或HyperFrames能力要求后，只有执行该可选能力时才额外要求阶段3就绪回执。WorkBuddy拥有暂停、用户确认和继续；Shell不选渲染器、不自动重放原业务请求。若真实WorkBuddy不能在同一会话继续，阶段6只报告准备完成并要求一次新的显式WorkBuddy调用，不能由Shell伪造无缝继续。

阶段3至阶段6共同约束：每阶段最多一个公共入口；没有可验证输入或直接下游消费者时必须零代码退出；不得预建通用Runtime管理器、CLI/MCP镜像、任务平台、后台服务、第二Agent Host、生产FSM或状态数据库。WorkBuddy是唯一运行中的Agent；所谓OpenMontage Agent只能指WorkBuddy读取已验证Package Guide后承担的逻辑生产角色。

## 阶段授权与零代码出口

```text
stage_3_scope: 仅对WorkBuddy/OpenMontage已经锁定的可选Remotion或HyperFrames能力及其锁声明附属资产执行按需发现和用户确认后的准备；不得处理必带Python/FFmpeg/Node工具链。
stage_3_public_entry: prepare_optional_capability(data_root, capability_request, authorization_receipt=None)
stage_3_result_set: NO_OPTIONAL_CAPABILITY_REQUIRED / READY_REUSED / CONSENT_REQUIRED / READY_PREPARED / BLOCKED
stage_3_zero_write_result: NO_OPTIONAL_CAPABILITY_REQUIRED / READY_REUSED / CONSENT_REQUIRED / BLOCKED(reason_code=BLOCKED_BEFORE_PUBLISH)
stage_3_download_policy: OPTIONAL_CAPABILITY_APPROVED_MAINLAND_CHINA_MIRRORS / NO_AUTOMATIC_OVERSEAS_FALLBACK
stage_3_lock_authority: VERIFIED_PACKAGE_OWNED / SHELL_MUST_NOT_DUPLICATE
stage_3_maximum_code_paths: golden_key_openmontage_workbuddy/runtime_prepare.py + export-only golden_key_openmontage_workbuddy/__init__.py + tests/workbuddy/test_runtime_prepare.py
stage_4_scope: 基础固定工具调用接受阶段2必带工具链事实；执行已选Remotion/HyperFrames前还必须接受同一registration_sha256和capability_lock_sha256的阶段3就绪回执；缺少相应事实返回RUNTIME_NOT_READY；不启动第二Agent，无任意Shell、无自动重试。
stage_5_scope: 用户实际运行起点；只保留一种真实WorkBuddy显式入口，literal user_message不变，技术控制独立。
stage_6_scope: 直接转交Runtime计划/准备事实与Launcher回执；仅有真实格式转换缺口时才允许独立实现；不解释、不安装、不重试。
stage_6_zero_code_exit: STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE
```

上述范围是规划边界，不是实现授权。任何需要阶段3扫描盘符、发现/下载/替换包内Python/FFmpeg/Node、一次安装全部可选能力、选择渲染引擎/版本、使用未批准海外默认源或覆盖外来目录，阶段4启动第二Agent、解析意图或调度任务，阶段5建立第二聊天Agent，阶段6解释Artifact或自动重试的方案，必须停止并返回`STOPPED_SCOPE_EXPANSION`。

## 阶段3重新规划合同

上一版阶段3执行包、`prepare_runtime_on_demand(...)`签名和Shell-owned `WORKBUDDY-PRODUCTION-RUNTIME.lock.json`全闭集形状全部`SUPERSEDED`，不得交给Builder。新阶段3只把一个已验证Package和一个WorkBuddy/OpenMontage已选能力请求转换为可供阶段4消费的能力就绪回执。

### 实现启动Gate

以下全部满足前，阶段3生产代码变化必须为0：

1. 最终Release ZIP及SHA sidecar持久保留，安装后的生产PackageRoot存在；
2. 生产DataRoot已有Registration和显式Activation，新进程`locate_active_package()`成功；
3. Locator返回的Python及47个锁定依赖、FFmpeg/ffprobe、Node/npm/npx身份和路径全部有效；
4. Package内存在被Manifest管理且hash锁定的Remotion/HyperFrames可选能力Lock；Shell不复制另一份版本权威；
5. 真实WorkBuddy/OpenMontage消费者合同明确何时选择能力、怎样传入请求、怎样暂停确认以及准备后怎样继续；
6. 最新正式Git对象、精确允许路径、直接测试和独立Reviewer范围写入新的实现任务包。

实现授权前任一Gate输入缺失，任务治理裁决为`INCOMPLETE_STAGE_3_INPUT`并零代码停止；它不是公共接口的第六种结果。未来接口存在后，运行期输入缺失统一返回`BLOCKED(reason_code=INCOMPLETE_STAGE_3_INPUT)`。不得创建占位实现、通用Runtime框架或测试假合同。

### 唯一输入合同

`capability_request`最少固定为：

```text
registration_sha256
capability: none | remotion | hyperframes
capability_lock_relative_path
capability_lock_sha256
explicit_candidate_path: optional
```

调用方不能提供任意下载URL、任意命令或任意安装目录。`capability_lock_relative_path`必须位于当前已验证PackageRoot内且对应文件被Manifest覆盖。`authorization_receipt`只有在精确绑定`registration_sha256 + capability_lock_sha256 + plan_sha256`时有效；任一身份变化使旧确认失效。literal `user_message`永远不进入本接口。

### 固定执行步骤

1. **Locator重验**：只从生产DataRoot读取活动Registration；缺失、漂移或必带工具链无效即`BLOCKED`，零修复、零下载。
2. **请求与Lock验证**：只接受`none/remotion/hyperframes`；验证Package-owned Lock、版本、入口、批准镜像、大小、SHA-256、许可证、目标和附属资产。
3. **只读发现**：按受管目标、明确候选路径、Lock明确允许的正常命令解析顺序核验；不扫盘、不枚举全局npm、不因PATH命中直接通过。
4. **零写入裁决**：不需可选能力返回`NO_OPTIONAL_CAPABILITY_REQUIRED`；精确能力已存在返回`READY_REUSED`。
5. **missing-only计划**：只列所选能力及Lock声明资产，返回版本、镜像、hash、大小、总下载量、许可证、目标和`plan_sha256`，状态`CONSENT_REQUIRED`；不得下载。
6. **授权复核与准备**：仅在授权回执仍匹配时，使用Package自带Node/npm/npx，从批准大陆镜像下载到同卷staging，核验后原子发布到`<DataRoot>/Runtime/Composition/<capability>/<capability_lock_sha256>/`；缓存只在`<DataRoot>/Caches/optional-runtime/`。
7. **失败处理**：外来目标保留并fail closed；hash、大小、许可、来源、命令或能力探针失败即回滚，清除staging和任务临时文件，不修改系统PATH、注册表或全局npm。
8. **回执**：重新核验所选能力、另一渲染器零触碰和必带Package零变化后，返回绑定`registration_sha256`、`capability`、`capability_lock_sha256`、`runtime_root`、验证入口、版本证据和`plan_sha256`的`READY_PREPARED`回执。

### 后续阶段交接

- 阶段4基础调用只消费阶段2Locator事实；执行Remotion/HyperFrames时额外校验阶段3回执，不能自行安装或接受跨Package回执。
- 阶段5拥有用户对话、计划展示、明确同意和真实WorkBuddy继续动作；技术控制与用户原话分离。
- 阶段6优先原样转交`CONSENT_REQUIRED`、`READY_*`、`BLOCKED`和Launcher事实；不安装、不解释Artifact、不自动重试。
- Shell不得声称已无缝继续，除非真实WorkBuddy消费者测试证明同一会话可恢复；否则要求新的显式WorkBuddy调用。

### 最小文件和交付

未来实现最多新增`golden_key_openmontage_workbuddy/runtime_prepare.py`，最小编辑`golden_key_openmontage_workbuddy/__init__.py`导出唯一入口，并新增`tests/workbuddy/test_runtime_prepare.py`。不新增Shell Runtime Lock、`host_tools.py`、CLI/MCP、服务、数据库、后台进程、UI或通用下载器。交付为单一入口、稳定结果集、绑定身份的计划/就绪回执、直接测试证据和阶段4可消费合同；不是Installer、最终Package、WorkBuddy入口、Launcher或视频E2E。

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
