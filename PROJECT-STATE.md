# Project State

更新时间：2026-08-18

## 当前状态

```text
product: WorkBuddy Shell V2
formal_branch: origin/codex/workbuddy-shell-v2
formal_baseline: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
stage_1: PASS_ACCEPTED
stage_2: REOPENED_REQUIRED_TOOLCHAIN_PACKAGE_REFRESH
stage_2_previous_package: PASS_ACCEPTED_HISTORICAL
repository_hygiene: PASS_ACCEPTED
repository_tracked_files: 33
stage_3_planning: REOPENED_OPTIONAL_CAPABILITY_RECLASSIFICATION_REQUIRED
stage_3_implementation: NOT_GRANTED
stage_3_conditional_authorization: SUSPENDED_PENDING_REPLAN
stage_3_start_gate: BLOCKED_STAGE_2_REQUIRED_TOOLCHAIN
stage_3_execution_packet: SUPERSEDED_BY_REQUIRED_TOOLCHAIN_CORRECTION
stage_4_launcher: NOT_GRANTED
stage_5_workbuddy_entry: NOT_GRANTED
stage_6_status_result_relay: NOT_GRANTED
current_task: V2-S2-S3-REQUIRED-TOOLCHAIN-CORRECTION-DOCS1
current_task_status: REVIEW_READY
current_result: THIS_COMMIT
next: V2-S2-S3-REQUIRED-TOOLCHAIN-CORRECTION-DOCS-REVIEW1
```

腾讯WorkBuddy是唯一运行中的Agent；它读取已验证金钥匙版OpenMontage Package Guide后承担生产角色。金钥匙版Package必须自带完整必带私有工具链：Python及核心依赖、FFmpeg/ffprobe、Node/npm/npx；Node按当前最高要求取22+。阶段3只准备WorkBuddy/OpenMontage已经锁定的可选Remotion或HyperFrames能力及其锁声明附属资产。上一版阶段3全闭集执行包已失效，本结论等待独立只读Reviewer且不构成实现授权。

## 已接受对象

- 阶段1已审对象：`041c6600dc8eb9094b5c93cb4a4ed088894578af`；正式集成边界：`fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9`。
- 阶段2旧Package最终实现：`ab1eddf474233859c6a3b32056a503f82ecdc117`；正式集成：`ca6e93b7da108732f2034239da340a986ba3da3a`。该证据仅为历史已接受对象；当前新版Package需要重新组装、登记、审阅和推广。
- 仓库卫生最终树：`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`；tracked精确33并受固定白名单保护。
- 旧阶段2只证明旧金钥匙版Package的Registration与Locator，不证明当前新版Package、Installer、Runtime、Launcher、真实WorkBuddy、Provider、SaaS或媒体E2E。

## 阶段3至阶段6建设顺序与实际运行链路

建设、审阅和交付严格按`阶段3 -> 阶段4 -> 阶段5 -> 阶段6`推进；这不等于最终用户的调用顺序。实际运行从阶段5开始：

```text
User -> Stage 5 WorkBuddy entry -> Stage 2 Locator revalidation
     -> Stage 4 fixed tool call with bundled required toolchain
     -> WorkBuddy/OpenMontage locks render capability
        -> bundled FFmpeg path: continue
        -> missing selected Remotion/HyperFrames: Stage 3 optional preparation
     -> Stage 6 fact relay
```

- Python及核心依赖、FFmpeg/ffprobe、Node/npm/npx是阶段2登记对象，阶段3不得扫描、下载、替换或用系统PATH补救。
- 阶段3只处理已选Remotion或HyperFrames能力；无能力要求时以`STAGE_3_NO_OPTIONAL_CAPABILITY_REQUIRED`零代码结束。浏览器只有当前能力锁明确要求时才准备。
- 阶段4启动时接受阶段2必带工具链事实；执行已选可选能力前接受对应阶段3就绪事实。否则返回`RUNTIME_NOT_READY`。
- 阶段5是用户实际运行起点，只允许一种真实WorkBuddy显式入口，用户原话与执行控制严格分离。
- 阶段6直接转交Runtime计划/准备事实和Launcher回执；无需独立转换时以`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`零代码结束，不解释、不安装、不重试。

详细实时字段只以`docs/workbuddy/v2/TASK-REGISTER.md`为准；Git历史中的Wave A/B/C记录不是当前任务授权。

## 阶段3启动检查摘要

用户对旧阶段3任务包的条件授权已因Required/Optional重新分类而暂停。当前不能在阶段2完成后直接启动旧实现，必须先取得完整工具链Locator输出和真实可选能力消费者合同，再重新冻结阶段3任务包。

阶段2必须证明Package/Manifest/Lock/Guide、Python/core dependencies、FFmpeg/ffprobe、Node/npm/npx的全身份、能力、许可证和分发完整性。阶段3重新规划还必须证明WorkBuddy/OpenMontage何时锁定Remotion/HyperFrames以及Shell如何在同一会话内请求确认和继续。完整实时状态只以`TASK-REGISTER.md`为准。
