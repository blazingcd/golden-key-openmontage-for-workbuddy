# Project State

更新时间：2026-08-20

## 当前状态

```text
product: WorkBuddy Shell V2
formal_branch: origin/codex/workbuddy-shell-v2
formal_head: e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3
formal_tree: a4d8034f6cf76c6eedd2f4bbe3c30dbe1b4e382a
stage_1: PASS_ACCEPTED
stage_2_registration_implementation: PASS_ACCEPTED
stage_2_temporary_package_validation: PASS_ACCEPTED
final_package_artifact: NOT_MATERIALIZED
production_package_registration: NOT_CREATED
repository_hygiene: PASS_ACCEPTED
repository_tracked_files: 35
stage_3_implementation: PASS_ACCEPTED / a3f8959682d296301dc573c2835f8c705a52e8b2
stage_3_closeout: PASS_ACCEPTED / 7c15aae4e77c579309312b21c79076f930970214
stage_3_evidence: 55 direct / 10 hygiene / 199 full / all exit 0 / no skip
stage_3_evidence_boundary: no real third-party or mainland-mirror download, production DataRoot, WorkBuddy, Stage4, Provider, media or video E2E proof
ci_stage3_state_assertion_fix: FORMAL / e5ae6f8cec3bc9829072a71f4acd9cc6c50ad8b3 / exactly two assertions in tests/workbuddy/test_repository_hygiene.py
ci_stage3_state_assertion_evidence: run 32218904419 / completed / success / 198 passed / 1 skipped / final exit 0
ci_stage3_state_assertion_review_history: first independent review INCOMPLETE / P0=0 / P1=0 / P2=0 / authority mismatch only / code diff no finding
ci_stage3_state_assertion_governance_deviation: formal advanced before authority closeout / history retained / current mirrors only are being repaired
stage_4_planning: ELIGIBLE / V2-S4-PLAN-BUILDER1_START_ONLY_AFTER_CURRENT_CLOSEOUT_APPROVE_AND_FORMAL_FAST_FORWARD
stage_4_implementation_authorization: NOT_GRANTED
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry: NOT_GRANTED
stage_6_status_result_relay: NOT_GRANTED
current_task: V2-CI-STAGE3-STATE-ASSERTION-CLOSEOUT-BUILDER1
current_task_status: WORKTREE_RESULT_READY_FOR_REVIEW
stage_4_contract_gap: fixed Package tool-entry identity absent from current Locator output; exact Stage4 public entry and immutable receipt field names not frozen
next_authorized_task: V2-S4-PLAN-BUILDER1 / EFFECTIVE_ONLY_AFTER_CURRENT_CLOSEOUT_INDEPENDENT_REVIEW_APPROVE_AND_ORDINARY_FORMAL_FAST_FORWARD
final_package_gate: LATER_FINAL_DELIVERY_OR_INSTALLER_TASK / NOT_GRANTED / DUE_BEFORE_STAGE5_PRODUCTION_ACCEPTANCE
```

腾讯WorkBuddy是唯一运行中的Agent；它读取已验证金钥匙版OpenMontage Package Guide后承担生产角色。阶段2已经接受完整必带工具链的Registration/Locator实现和一次真实临时Package验证。阶段3已完成Remotion与HyperFrames的有界探测、报告、逐能力授权集成合同实现并正式收口；两项始终是OpenMontage候选能力，Shell不选择渲染器，缺失、拒绝或延期不阻塞基础工具链路径。

## 已接受对象

- 阶段1已审对象：`041c6600dc8eb9094b5c93cb4a4ed088894578af`；正式集成边界：`fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9`。
- 阶段2完整工具链登记实现：`709c8e880b144fa9e9be26e9feb5d776dd6025e2`；状态收口：`95eeeff175060f06ca2f549737e724160edc9e14`。它证明登记能力、负面测试和一次临时Package组装/登记，不证明最终Package已经保留。
- 阶段3实现：`a3f8959682d296301dc573c2835f8c705a52e8b2`，独立`APPROVE / P0=0 / P1=0 / P2=0`并正式推广；closeout：`7c15aae4e77c579309312b21c79076f930970214`，已正式推广。
- 阶段3证据：55 direct、10 hygiene、199 full，全部最终退出0且无skip；未证明真实第三方/大陆镜像下载、生产DataRoot集成、WorkBuddy、Stage4、Provider或媒体/视频E2E。
- 当前正式树tracked精确35。最终Release、生产PackageRoot和生产Registration仍属于后续最终交付/Installer任务，最迟在Stage5真实WorkBuddy生产验收前完成；它不是Stage4规划或编码前置。

## 阶段3至阶段6建设顺序与实际运行链路

建设、审阅和交付严格按`阶段3 -> 阶段4 -> 阶段5 -> 阶段6`推进；这不等于最终用户的调用顺序。实际运行从阶段5开始：

```text
User -> Stage 5 WorkBuddy entry -> Stage 2 Locator revalidation
     -> Stage 4 one fixed Package-tool call with bundled required toolchain
     -> WorkBuddy/OpenMontage locks render capability
        -> bundled FFmpeg path: continue
       -> explicit Remotion/HyperFrames execution: require matching Stage 3 PRESENT or INTEGRATED evidence
     -> Stage 6 fact relay
```

- Python及核心依赖、FFmpeg/ffprobe、Node/npm/npx是阶段2登记对象，阶段3不得扫描、下载、替换或用系统PATH补救。
- 阶段3公共入口是`prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`；结果闭集是`DETECTION_REPORT/CONSENT_REQUIRED/INTEGRATED/SKIPPED/BLOCKED`。
- 阶段4先调用`locate_active_package(data_root)`；基础固定工具调用只依赖阶段2必带工具链。只有本次明确执行某可选能力时，才要求同一capability+definition的`PRESENT`或`INTEGRATED`证据。
- 阶段5拥有真实WorkBuddy新会话、唯一入口、literal `user_message`不变、逐能力询问和同任务继续的实现/验收；这些不是Stage4前置。
- 阶段6只在Stage4回执和Stage5真实消费者存在后判断；可直接消费时以`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`和生产代码0结束。

详细实时字段只以`docs/workbuddy/v2/TASK-REGISTER.md`为准；Git历史中的Wave A/B/C记录不是当前任务授权。

## Stage 4接管审计摘要

当前`locate_active_package(data_root)`会重验并返回Registration、PackageRoot、完整必带工具链、Guide、Manifest和Lock身份，但没有给出固定Package工具入口的权威身份。现有权威也没有冻结Stage4精确公共入口和不可改写进程回执字段。Stage4规划负责闭合这两项，Stage4实现仍未获授权。

未来单独授权的Stage4规划任务必须冻结：固定工具入口身份来自何种经验证Package定义、相对路径/hash/owner和固定argv形状；唯一公共入口；一次不可改写真实进程回执的精确字段。工具身份由批准OpenMontage Package定义及后续最终交付/Installer所有者提供，Launcher API和回执字段由Stage4规划所有者冻结；不得重开Stage2、猜测未验证Guide，或把最终Package/真实WorkBuddy变成Stage4规划前置。

Stage4最小边界只允许一次WorkBuddy拥有的会话调用一个固定Package工具并返回真实回执；禁止任意shell/命令、意图解析、第二Agent、Runtime安装、渲染器选择、自动重试/重放、队列/服务/数据库/多进程调度、媒体生产、Artifact创建和Checkpoint推进。当前closeout候选仍须独立只读审查和普通fast-forward；两者完成后唯一下一任务才是`V2-S4-PLAN-BUILDER1`。这不授权Stage4实现、Launcher实现、Stage5、Stage6或最终Package Gate。
