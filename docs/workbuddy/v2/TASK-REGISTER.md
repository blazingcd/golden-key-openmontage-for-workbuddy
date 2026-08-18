# WorkBuddy Shell V2 任务账本

状态：`CONDITIONAL AUTHORITY / V2_S2_REQUIRED_TOOLCHAIN_REFRESH_AUTHORITY_REVIEW_READY`

更新时间：2026-08-18

## 当前任务

```text
authority_task_id: V2-S2-REQUIRED-TOOLCHAIN-REFRESH-AUTHORITY1
authority_task_status: REVIEW_READY
authority_start_commit: 29a890db22181db9532263a168dcbe5f708b7149
authority_result_commit: THIS_COMMIT
authority_branch: codex/v2-s2-toolchain-refresh-authority1
authority_review_range: 29a890db22181db9532263a168dcbe5f708b7149..THIS_COMMIT
authority_activation_condition: independent_reviewer == APPROVE AND THIS_COMMIT fast-forwarded to origin/codex/workbuddy-shell-v2
authority_allowed_path: docs/workbuddy/v2/TASK-REGISTER.md
authority_production_code_changes: 0
authority_test_changes: 0
task_id: V2-S2-REQUIRED-TOOLCHAIN-PACKAGE-REFRESH-BUILDER1
task_status: READY_NOT_STARTED
task_kind: STAGE_2_REQUIRED_TOOLCHAIN_PACKAGE_REFRESH
user_authorization: 2026-08-18 / 尽快把这个阻塞完成
implementation_authorization: GRANTED_FOR_REQUIRED_TOOLCHAIN_REFRESH_ONLY
start_commit: THIS_COMMIT
start_commit_resolution: Authority1经独立APPROVE并fast-forward推广后的精确40位result SHA；绝不从29a890旧对象启动
result_commit: NOT_CREATED
branch: codex/v2-s2-required-toolchain-package-refresh-b1
formal_target_branch: origin/codex/workbuddy-shell-v2
formal_target_at_authority_start: 29a890db22181db9532263a168dcbe5f708b7149
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
ffmpeg_version: 9.0 essentials
ffmpeg_archive_url: https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.7z
ffmpeg_archive_size: 34372199
ffmpeg_archive_sha256: 49a73bdf0850092a252ac4641d922f3048d63ed113e196cc65ce1e4f7fb33e85
rejected_ffmpeg_archive: D:\Downloads\Working\ffmpeg-9.0-essentials_build.7z / SHA256 prefix ffb866 / MUST_NOT_USE
temporary_build_root: D:\BlazingCD\Personal\Temp\workbuddy-v2-s2-toolchain-refresh-b1
project_venv_rule: 必须使用该任务在D盘的独立.venv；不得混用系统或其他项目Python包
package_build_scope: 一次真实临时Package；源树+干净私有Python及锁定核心依赖+FFmpeg/ffprobe+Node/npm/npx
registration_scope: Stage2必须验证并返回全部必带工具身份与固定路径；负面测试fail closed
forbidden_scope: external source repo、官方OpenMontage、Installer、Runtime、Launcher、Stage3、Skill、config、其他测试、生产DataRoot激活、WorkBuddy、Provider、媒体
exit_evidence: commit+push+REVIEW_READY；真实构建和注册证据；production=1/test=1/docs<=2；临时构建根清理
next_authorized_task: V2-S2-REQUIRED-TOOLCHAIN-PACKAGE-REFRESH-BUILDER1
```

`THIS_COMMIT`由Authority1 Reviewer解析为本分支精确40位结果SHA。只有该结果获独立`APPROVE`并fast-forward进入正式分支后，Builder才从同一精确SHA启动；未推广前不得启动。Builder只刷新阶段2必带工具链Package及其Registration合同和测试，不授权阶段3或其他Shell模块。

## 当前正式状态

```text
formal_branch: codex/workbuddy-shell-v2
formal_handoff_commit: 29a890db22181db9532263a168dcbe5f708b7149
stage_1_status: PASS_ACCEPTED
stage_2_status: REOPENED_REQUIRED_TOOLCHAIN_PACKAGE_REFRESH / READY_NOT_STARTED
stage_2_previous_package_status: PASS_ACCEPTED_HISTORICAL
stage_2_integration_commit: ca6e93b7da108732f2034239da340a986ba3da3a
repository_hygiene_status: PASS_ACCEPTED
repository_final_tree_commit: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
repository_final_audit: APPROVE
repository_final_audit_source: USER_ACCEPTED_HANDOFF_2026_08_17
repository_tracked_files: 33
stage_3_planning_authorization: NOT_GRANTED_PENDING_STAGE_2_REFRESH
stage3_planning: REOPENED_OPTIONAL_CAPABILITY_RECLASSIFICATION_REQUIRED
stage_3_implementation_authorization: NOT_GRANTED
stage_3_conditional_authorization: SUSPENDED_PENDING_REPLAN
stage_3_start_gate: BLOCKED_STAGE_2_REQUIRED_TOOLCHAIN
stage_3_execution_packet: SUPERSEDED_BY_REQUIRED_TOOLCHAIN_CORRECTION
stage3_implementation: NOT_GRANTED
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry_authorization: NOT_GRANTED
stage_6_status_result_relay_authorization: NOT_GRANTED
stage_3_to_6_scope_reduction: SUPERSEDED_BY_REQUIRED_TOOLCHAIN_CORRECTION
runtime_correction: REOPENED_REQUIRED_TOOLCHAIN_CORRECTION
```

阶段2此前通过的是旧金钥匙版Package登记合同和实现，不是更新后的当前Package。官方当前Quick Start明确列出Python 3.10+、FFmpeg和Node.js 18+三项基础Prerequisites；当前HyperFrames合同进一步要求Node.js 22+。金钥匙Package必须因此自带可用私有Python环境及核心依赖、FFmpeg/ffprobe、满足最高要求的Node/npm/npx，并在Manifest/Lock与Registration中逐项锁定。只登记Python的旧阶段2合同不足，必须修订、重新组装、独立审阅和推广；完成前阶段3不得启动。

仓库卫生最终树基线仍为`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`，tracked精确33且等于固定白名单；该对象是当前正式handoff `29a890db22181db9532263a168dcbe5f708b7149`的祖先。后续文档修订没有恢复已清理内容，也没有生产代码或测试变化。

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

在这些输入齐全前，阶段3保持`REOPENED_OPTIONAL_CAPABILITY_RECLASSIFICATION_REQUIRED / NOT_GRANTED`。可以确定的边界只有：Remotion与HyperFrames不预装全部；只准备已选能力；浏览器仅在该能力锁明确要求时准备；Python/FFmpeg/Node及核心Python依赖绝不由阶段3扫描、下载或替换；阶段3不选择渲染器、不启动第二Agent、不执行视频生产。

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

老项目可迁移证据：`347272c`固定包内便携Python；`899592d`固定完整Runtime、hash、许可、DataRoot和大陆PyPI/npm/Node/浏览器镜像；`639978d`增加`managed`、`registered_host`、`PATH_host`、`missing`发现与missing-only准备。旧锁中的精确FFmpeg 9.0 `gyan.dev`资产现只作为必带Package组装候选；阶段2必须核验其来源、SHA-256、许可、分发和实际可获得性。它不再形成阶段3下载授权，也不得扩展为其他可选能力的海外回退权。
