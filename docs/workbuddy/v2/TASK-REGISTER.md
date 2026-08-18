# WorkBuddy Shell V2 任务账本

状态：`V2_S2_REQUIRED_TOOLCHAIN_REFRESH / PASS_ACCEPTED；V2_S3_PRETAKEOVER_REPLAN / READY_NOT_STARTED`

更新时间：2026-08-18

## 当前任务

```text
authority_task_id: V2-S2-REQUIRED-TOOLCHAIN-REFRESH-AUTHORITY1
authority_task_status: PASS_ACCEPTED
authority_start_commit: 29a890db22181db9532263a168dcbe5f708b7149
authority_result_commit: 55781b45ac9217693843f2c73cec994805e4024c
authority_branch: codex/v2-s2-toolchain-refresh-authority1
authority_review_range: 29a890db22181db9532263a168dcbe5f708b7149..55781b45ac9217693843f2c73cec994805e4024c
authority_activation_condition: SATISFIED / independent APPROVE and fast-forward promotion
authority_allowed_path: docs/workbuddy/v2/TASK-REGISTER.md
authority_production_code_changes: 0
authority_test_changes: 0
task_id: V2-S2-REQUIRED-TOOLCHAIN-PACKAGE-REFRESH-CLOSEOUT1
task_status: REVIEW_READY
task_kind: STAGE_2_REQUIRED_TOOLCHAIN_STATE_CLOSEOUT
user_authorization: 2026-08-18 / 先解决前置阻塞，之后开始阶段三前置任务
closeout_authorization: GRANTED_FOR_TASK_REGISTER_ONLY
start_commit: 709c8e880b144fa9e9be26e9feb5d776dd6025e2
start_commit_resolution: reviewed Stage2 refresh result after ordinary fast-forward promotion
result_commit: THIS_COMMIT
branch: codex/v2-s2-toolchain-refresh-closeout1
formal_target_branch: origin/codex/workbuddy-shell-v2
formal_target_at_closeout_start: 709c8e880b144fa9e9be26e9feb5d776dd6025e2
closeout_allowed_path: docs/workbuddy/v2/TASK-REGISTER.md
closeout_production_code_changes: 0
closeout_test_changes: 0
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
allowed_paths:
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
exit_evidence: TASK-REGISTER-only commit+push+REVIEW_READY；production=0；test=0；worktree clean
next_authorized_task: V2-S3-PRETAKEOVER-PLAN1
next_task_status: READY_NOT_STARTED
next_task_authorization: GRANTED_FOR_PRETAKEOVER_REPLAN_ONLY
next_task_start_commit: THIS_COMMIT after independent APPROVE and ordinary fast-forward promotion; resolve to exact 40-hex from origin/codex/workbuddy-shell-v2
```

`THIS_COMMIT`由Closeout1独立Reviewer解析为本分支精确40位结果SHA，只读确认本次相对`709c8e880b144fa9e9be26e9feb5d776dd6025e2`仅修改任务账本且生产/测试均为0。只有该结果获`APPROVE`并普通fast-forward进入`origin/codex/workbuddy-shell-v2`后，`V2-S3-PRETAKEOVER-PLAN1`才从同一最新正式40位SHA接管。该授权只允许回顾目标和重新冻结阶段3前置规划，不授权阶段3实现。

## 当前正式状态

```text
formal_branch: codex/workbuddy-shell-v2
formal_handoff_commit: 709c8e880b144fa9e9be26e9feb5d776dd6025e2
stage_1_status: PASS_ACCEPTED
stage_2_status: PASS_ACCEPTED
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
stage_3_planning_authorization: GRANTED_FOR_PRETAKEOVER_REPLAN_ONLY
stage3_planning: READY_NOT_STARTED / PRETAKEOVER_REPLAN_ONLY
stage_3_implementation_authorization: NOT_GRANTED
stage_3_conditional_authorization: NOT_GRANTED
stage_3_start_gate: ELIGIBLE_FOR_REPLAN
stage_3_execution_packet: SUPERSEDED_BY_REQUIRED_TOOLCHAIN_CORRECTION
stage3_implementation: NOT_GRANTED
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
stage_3_to_6_scope_reduction: SUPERSEDED_BY_REQUIRED_TOOLCHAIN_CORRECTION
runtime_correction: REQUIRED_TOOLCHAIN_REFRESH_PASS_ACCEPTED
```

阶段2旧结果只覆盖Python身份，现已由`709c8e880b144fa9e9be26e9feb5d776dd6025e2`完成当前Package必带Python及锁定核心依赖、FFmpeg/ffprobe、Node/npm/npx的重新组装、Registration/Locator验证、负测、独立审阅和正式推广。阶段2前置阻塞已关闭；阶段3现在只具备前置重新规划资格，实施仍未授权。

仓库卫生最终树基线仍为`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`，tracked精确33且等于固定白名单；该对象是当前正式handoff `709c8e880b144fa9e9be26e9feb5d776dd6025e2`的祖先。阶段2刷新只修改四个既有白名单文件，没有恢复已清理内容或新增仓库文件。

## 阶段3至阶段6建设与交付顺序

```text
Stage 3: Runtime Preparation on Demand
Stage 4: Session Launcher
Stage 5: WorkBuddy Entry
Stage 6: Status and Result Relay
```

该顺序只表示建设、审阅和正式交付顺序，不是最终用户运行时的调用顺序。每个阶段都从当时最新的`origin/codex/workbuddy-shell-v2`精确提交开始，经单一有界Builder、独立只读Reviewer、普通非force fast-forward推广、远端临时分支清理和本地worktree关闭后，下一阶段才可接管。规划接受、Builder提交或Reviewer批准均不等于正式交付。

上一版`阶段5 -> 阶段2 -> 阶段3全闭集检查 -> 阶段4`运行链路已失效，因为阶段3不再负责启动前必带工具链。新的最低关系是：阶段5触发阶段2对必带Python/FFmpeg/Node重验，阶段4据此启动固定工具；WorkBuddy/OpenMontage形成并锁定Remotion或HyperFrames能力要求后，才调用阶段3准备对应可选能力。阶段3与阶段4在真实会话中的精确调用/暂停合同必须等待WorkBuddy消费者证据后重新冻结，不能由Shell预先猜测。

阶段3至阶段6共同约束：每阶段最多一个公共入口；没有可验证输入或直接下游消费者时必须零代码退出；不得预建通用Runtime管理器、CLI/MCP镜像、任务平台、后台服务、第二Agent Host、生产FSM或状态数据库。WorkBuddy是唯一运行中的Agent；所谓OpenMontage Agent只能指WorkBuddy读取已验证Package Guide后承担的逻辑生产角色。

## 阶段授权与零代码出口

```text
stage_3_scope: 仅对WorkBuddy/OpenMontage已经锁定的可选Remotion或HyperFrames能力及其锁声明附属资产执行按需发现和用户确认后的准备；不得处理必带Python/FFmpeg/Node工具链。
stage_3_zero_code_exit: STAGE_3_NO_OPTIONAL_CAPABILITY_REQUIRED
stage_3_download_policy: OPTIONAL_CAPABILITY_APPROVED_MAINLAND_CHINA_MIRRORS / NO_AUTOMATIC_OVERSEAS_FALLBACK
stage_4_scope: 启动固定工具时必须接受阶段2必带工具链就绪事实；执行已选可选能力前还必须接受该能力对应的阶段3就绪事实；缺少相应事实返回RUNTIME_NOT_READY；不启动第二Agent，无任意Shell、无自动重试。
stage_5_scope: 用户实际运行起点；只保留一种真实WorkBuddy显式入口，literal user_message不变，技术控制独立。
stage_6_scope: 直接转交Runtime计划/准备事实与Launcher回执；仅有真实格式转换缺口时才允许独立实现；不解释、不安装、不重试。
stage_6_zero_code_exit: STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE
```

上述范围是规划边界，不是实现授权。任何需要阶段3扫描盘符、发现/下载/替换包内Python/FFmpeg/Node、一次安装全部可选能力、选择渲染引擎/版本、使用未批准海外默认源或覆盖外来目录，阶段4启动第二Agent、解析意图或调度任务，阶段5建立第二聊天Agent，阶段6解释Artifact或自动重试的方案，必须停止并返回`STOPPED_SCOPE_EXPANSION`。

## 阶段3重新规划前置

上一版阶段3执行包、`prepare_runtime_on_demand(...)`签名和`WORKBUDDY-PRODUCTION-RUNTIME.lock.json`全闭集形状全部标记为`SUPERSEDED`，不得交给Builder。阶段3重新冻结必须先得到：

1. 阶段2已审Package Registration，明确返回必带Python及核心依赖、FFmpeg/ffprobe、Node/npm/npx的精确身份和路径；
2. 当前Package提供的WorkBuddy/OpenMontage消费者合同，明确何时产生已锁定的`remotion`或`hyperframes`能力要求；
3. 对应可选能力的版本、npm锁、批准大陆镜像、hash、大小、许可证、目标和必要附属资产；
4. 阶段3与阶段4同一WorkBuddy会话中的调用、暂停、用户确认和继续边界；Shell不得自动重放原业务请求；
5. 最新正式Git对象、允许路径、一个公共入口、一个生产模块、一个Optional Runtime Lock和一个直接测试文件的精确任务包。

`V2-S3-PRETAKEOVER-PLAN1`只被授权回顾并冻结上述输入；输入未齐全时必须以零代码结果退出。阶段3实现保持`NOT_GRANTED`。可以确定的边界只有：Remotion与HyperFrames不预装全部；只准备已选能力；浏览器仅在该能力锁明确要求时准备；Python/FFmpeg/Node及核心Python依赖绝不由阶段3扫描、下载或替换；阶段3不选择渲染器、不启动第二Agent、不执行视频生产。

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

旧Stage2只证明旧金钥匙版Package的Registration与Locator：明确路径输入、不可变登记对象、活动指针CAS、破损指针显式恢复和只读Locator。它不证明当前新版Package、Installer、Runtime、Launcher、真实WorkBuddy、Provider、SaaS、网络或媒体E2E。阶段3至阶段6不得读取未验证Package Guide、扫描磁盘猜测对象，或把技术控制词写入literal `user_message`。

老项目可迁移证据：`347272c`固定包内便携Python；`899592d`固定完整Runtime、hash、许可、DataRoot和大陆PyPI/npm/Node/浏览器镜像；`639978d`增加`managed`、`registered_host`、`PATH_host`、`missing`发现与missing-only准备。旧锁中的“FFmpeg 9.0 essentials”只提供候选来源标签；本次冻结URL与hash对应二进制实际报告`9.0.1-essentials_build`。它不形成阶段3下载授权，也不得扩展为其他可选能力的海外回退权。
