# Project State

更新时间：2026-08-17

## 当前状态

```text
product: WorkBuddy Shell V2
formal_branch: origin/codex/workbuddy-shell-v2
formal_baseline: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
stage_1: PASS_ACCEPTED
stage_2: REOPENED_PACKAGE_REFRESH_REQUIRED
stage_2_previous_package: PASS_ACCEPTED_HISTORICAL
repository_hygiene: PASS_ACCEPTED
repository_tracked_files: 33
stage_3_planning: RUNTIME_SCOPE_CORRECTED_FOR_REVIEW
stage_3_implementation: NOT_GRANTED
stage_3_conditional_authorization: GRANTED_AFTER_ALL_START_GATES_PASS
stage_3_start_gate: WAITING_STAGE_2_AND_PLANNING_PROMOTION
stage_3_execution_packet: FROZEN_FOR_INDEPENDENT_REVIEW
stage_4_launcher: NOT_GRANTED
stage_5_workbuddy_entry: NOT_GRANTED
stage_6_status_result_relay: NOT_GRANTED
current_task: V2-S2-S3-RUNTIME-CORRECTION-DOCS1
current_task_status: REVIEW_READY
current_result: THIS_COMMIT
next: V2-S2-S3-RUNTIME-CORRECTION-DOCS-REVIEW1
```

腾讯WorkBuddy是唯一运行中的Agent；它读取已验证金钥匙版OpenMontage Package Guide后承担生产角色，不存在第二个OpenMontage Agent进程。金钥匙版Package必须自带锁定私有Python；阶段3只对Python私有依赖、FFmpeg、Node、Remotion、HyperFrames和锁定浏览器执行闭集发现与missing-only准备。下载使用批准的中国大陆镜像，另临时允许精确锁定的FFmpeg `gyan.dev`资产；该例外在无代理/VPN大陆网络直连验证通过前不可执行。本结论等待独立只读Reviewer；这不是任何实现授权。

## 已接受对象

- 阶段1已审对象：`041c6600dc8eb9094b5c93cb4a4ed088894578af`；正式集成边界：`fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9`。
- 阶段2旧Package最终实现：`ab1eddf474233859c6a3b32056a503f82ecdc117`；正式集成：`ca6e93b7da108732f2034239da340a986ba3da3a`。该证据仅为历史已接受对象；当前新版Package需要重新组装、登记、审阅和推广。
- 仓库卫生最终树：`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`；tracked精确33并受固定白名单保护。
- 旧阶段2只证明旧金钥匙版Package的Registration与Locator，不证明当前新版Package、Installer、Runtime、Launcher、真实WorkBuddy、Provider、SaaS或媒体E2E。

## 阶段3至阶段6建设顺序与实际运行链路

建设、审阅和交付严格按`阶段3 -> 阶段4 -> 阶段5 -> 阶段6`推进；这不等于最终用户的调用顺序。实际运行从阶段5开始：

```text
User -> Stage 5 WorkBuddy entry -> Stage 2 Locator revalidation
     -> Stage 3 closed-set runtime check
        -> ready: Stage 4 fixed tool call -> Stage 6 fact relay
        -> missing/incompatible: Stage 6 missing-only plan relay
           -> separate user consent -> Stage 3 preparation
           -> Stage 6 preparation fact relay -> stop
           -> later explicit WorkBuddy invocation rechecks runtime
```

- 包内Python是阶段2登记对象，阶段3不扫描、不下载、不替换它。阶段3只检查受管路径、明确登记宿主工具和PATH命令候选；不扫描盘符。
- 阶段3是一个闭集接口的不同结果，不是两条实现路线。没有真实额外Runtime缺口时以`STAGE_3_NO_ADDITIONAL_RUNTIME_REQUIRED`零代码结束；存在缺口时先输出锁定missing-only计划并取得另一次明确同意。准备后停止，不自动重试原请求。除临时批准且通过大陆直连验证的FFmpeg `gyan.dev`精确资产外，只使用批准大陆镜像，且没有自动海外回退。
- 阶段4只接受有效Runtime就绪回执并为WorkBuddy会话调用一次固定工具进程；否则返回`RUNTIME_NOT_READY`。它不接受任意Shell、不自动重试、不启动第二Agent或进入Package业务内部。
- 阶段5是用户实际运行起点，只允许一种真实WorkBuddy显式入口，用户原话与执行控制严格分离。
- 阶段6直接转交Runtime计划/准备事实和Launcher回执；无需独立转换时以`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`零代码结束，不解释、不安装、不重试。

详细实时字段只以`docs/workbuddy/v2/TASK-REGISTER.md`为准；Git历史中的Wave A/B/C记录不是当前任务授权。

## 阶段3启动检查摘要

用户已给出条件授权：阶段2全部完成后，先由本任务进行只读交接检查，全部通过才可启动阶段3。当前仍不能启动，因为新版阶段2和本轮规划纠偏都尚未在正式分支形成已审结果。

启动检查固定为：规划纠偏已审推广；新版阶段2已审推广；当前Package/Manifest/Lock/Guide/私有Python全身份重验；私有Python可执行且bootstrap/import探针通过；当前Package依赖输入足以冻结精确Runtime Lock；正式Git对象、33文件白名单和工作树无漂移；FFmpeg直连状态按`BLOCKED_SOURCE_ACCESS_UNVERIFIED`/可用/`BLOCKED_SOURCE_UNREACHABLE`如实处理。完整任务路径、实现文件和验收条件只以`docs/workbuddy/v2/TASK-REGISTER.md`及`ACCEPTANCE-MATRIX.md`为准。
