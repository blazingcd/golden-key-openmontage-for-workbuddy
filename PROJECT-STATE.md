# Project State

更新时间：2026-08-18

## 当前状态

```text
product: WorkBuddy Shell V2
formal_branch: origin/codex/workbuddy-shell-v2
formal_baseline_before_authority: d2a2aa5ce9a0b4c8735ec81da8fb1723bfb0e9e2
accepted_authority_result: ba0a84d93a4b26c09eaf7e2469d09c064c27710e
formal_head_after_closeout: THIS_COMMIT
stage_1: PASS_ACCEPTED
stage_2_registration_implementation: PASS_ACCEPTED
stage_2_temporary_package_validation: PASS_ACCEPTED
final_package_artifact: NOT_MATERIALIZED
production_package_registration: NOT_CREATED
stage_2_previous_package: PASS_ACCEPTED_HISTORICAL
repository_hygiene: PASS_ACCEPTED
repository_tracked_files: 33
stage_3_planning: PASS_ACCEPTED_AFTER_CLOSEOUT_REVIEW_AND_FORMAL_FAST_FORWARD
stage_3_implementation: NOT_GRANTED
stage_3_conditional_authorization: NOT_GRANTED
stage_3_start_gate: BLOCKED_PACKAGE_CAPABILITY_LOCK_FINAL_PACKAGE_AND_CONSUMER_CONTRACT
stage_3_execution_packet: REPLANNED_BOUNDARY_PASS_ACCEPTED / IMPLEMENTATION_NOT_GRANTED
stage_4_launcher: NOT_GRANTED
stage_5_workbuddy_entry: NOT_GRANTED
stage_6_status_result_relay: NOT_GRANTED
current_task: V2-PACKAGE-OWNED-OPTIONAL-CAPABILITY-LOCK-INPUT-GATE1
current_task_status: BLOCKED_EXTERNAL_PACKAGE_INPUT_REQUIRED
current_result: ba0a84d93a4b26c09eaf7e2469d09c064c27710e / APPROVE / P0=0 / P1=0 / P2=0 / FORMAL_FAST_FORWARD_COMPLETE
reviewed_planning_result: 72719c758f092868fc6446e44a803d13eeae44a6
reviewed_planning_verdict: APPROVE / P0=0 / P1=0 / P2=0
final_package_gate: BLOCKED_PACKAGE_CAPABILITY_LOCK
package_owned_capability_lock: MISSING_OR_INELIGIBLE
real_workbuddy_consumer_contract: NOT_FROZEN
next: EXTERNAL_GOLDEN_KEY_PACKAGE_CAPABILITY_LOCK_RESULT + REAL_WORKBUDDY_CONSUMER_CONTRACT / NOT_GRANTED_IN_SHELL_REPOSITORY
```

腾讯WorkBuddy是唯一运行中的Agent；它读取已验证金钥匙版OpenMontage Package Guide后承担生产角色。阶段2已经接受完整必带工具链的登记实现和一次真实临时Package验证，但临时Package已清理，最终Release、生产PackageRoot和生产Registration都不存在。阶段3只准备WorkBuddy/OpenMontage已经锁定的一个可选Remotion或HyperFrames能力及其Package-owned Lock声明附属资产；当前只完成重新规划，实施仍未授权。

## 已接受对象

- 阶段1已审对象：`041c6600dc8eb9094b5c93cb4a4ed088894578af`；正式集成边界：`fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9`。
- 阶段2完整工具链登记实现：`709c8e880b144fa9e9be26e9feb5d776dd6025e2`；状态收口：`95eeeff175060f06ca2f549737e724160edc9e14`。它证明登记能力、负面测试和一次临时Package组装/登记，不证明最终Package已经保留。
- 仓库卫生最终树：`20ddab75825c1b6e7de5a51603afe8b6fd82eceb`；tracked精确33并受固定白名单保护。
- 当前D盘任务临时Package不存在，生产DataRoot没有活动Package Registration；Installer、Runtime、Launcher、真实WorkBuddy、Provider、SaaS和媒体E2E均未证明。

## 阶段3至阶段6建设顺序与实际运行链路

建设、审阅和交付严格按`阶段3 -> 阶段4 -> 阶段5 -> 阶段6`推进；这不等于最终用户的调用顺序。实际运行从阶段5开始：

```text
User -> Stage 5 WorkBuddy entry -> Stage 2 Locator revalidation
     -> Stage 4 base fixed-tool call with bundled required toolchain
     -> WorkBuddy/OpenMontage locks render capability
        -> bundled FFmpeg path: continue
       -> selected Remotion/HyperFrames: Stage 3 verifies Registration + Package Lock
          -> exact existing capability: READY_REUSED
          -> missing capability: consented optional preparation -> READY_PREPARED
     -> Stage 6 fact relay
```

- Python及核心依赖、FFmpeg/ffprobe、Node/npm/npx是阶段2登记对象，阶段3不得扫描、下载、替换或用系统PATH补救。
- 阶段3只处理已选Remotion或HyperFrames能力；无能力要求时返回`NO_OPTIONAL_CAPABILITY_REQUIRED`且零下载。浏览器只有当前Package-owned能力Lock明确要求时才准备。
- 阶段4启动时接受阶段2必带工具链事实；执行已选可选能力前接受对应阶段3就绪事实。否则返回`RUNTIME_NOT_READY`。
- 阶段5是用户实际运行起点，只允许一种真实WorkBuddy显式入口，用户原话与执行控制严格分离。
- 阶段6直接转交Runtime计划/准备事实和Launcher回执；无需独立转换时以`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`零代码结束，不解释、不安装、不重试。

详细实时字段只以`docs/workbuddy/v2/TASK-REGISTER.md`为准；Git历史中的Wave A/B/C记录不是当前任务授权。

## 阶段3启动检查摘要

旧阶段3任务包已经失效。当前重新规划建议唯一入口为`prepare_optional_capability(data_root, capability_request, authorization_receipt=None)`，输出仅允许`NO_OPTIONAL_CAPABILITY_REQUIRED`、`READY_REUSED`、`CONSENT_REQUIRED`、`READY_PREPARED`或`BLOCKED`。最大实现范围为一个新生产模块、一个导出编辑和一个直接测试文件；Shell不拥有另一份Runtime Lock。

阶段3实现启动前必须同时证明：最终Package持久落盘；生产Registration/Activation存在；新进程Locator成功；Package-owned可选能力Lock存在且被Manifest绑定；真实WorkBuddy/OpenMontage消费者合同冻结；正式Git对象和精确Builder白名单获授权。完整实时状态只以`TASK-REGISTER.md`为准。

当前下一项不是阶段3编码，也不是立即生成最终Package。必须先由外部Golden Key OpenMontage Package产出Manifest覆盖且合格的Remotion/HyperFrames能力Lock，并冻结真实WorkBuddy消费者合同；随后才可独立授权`V2-FINAL-PACKAGE-MATERIALIZATION-AND-PRODUCTION-REGISTRATION-GATE1`，一次性持久生成最终Release、安装生产PackageRoot、建立生产Registration/Activation并做新进程Locator核验；最后才可发出阶段3 Builder任务包。阶段2临时ZIP `f00e83d6154e7593b765a3d6c863b6653fc642818133acd7924f3fd91aab5d03`不得作为最终Package发布；上述门禁也不得塞入阶段3Runtime模块。
