# Project State

更新时间：2026-08-20

## 当前状态

```text
product: WorkBuddy Shell V2
formal_branch: origin/codex/workbuddy-shell-v2
formal_head: 5cb3f585a0cddffbd823c785b1d39ebd1834c1df
formal_tree: 144df76b3a307fa8944ccd7bd384bddb1b340516
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
stage_4_plan_formal_result: 5cb3f585a0cddffbd823c785b1d39ebd1834c1df / tree 144df76b3a307fa8944ccd7bd384bddb1b340516
stage_4_plan_promotion: ORDINARY_FAST_FORWARD / origin/codex/workbuddy-shell-v2=5cb3f585a0cddffbd823c785b1d39ebd1834c1df
stage_4_plan_review: V2-S4-PLAN-REVIEW1 / APPROVE / P0=0 / P1=0 / P2=0
stage_4_plan_review_history: two REQUEST_CHANGES rounds closed definition hash-cycle, receipt outcome/priority/invalid-input, forged-summary evidence, and managed/explicit/PATH handoff findings
stage_4_plan_ci: run 32337744225 / completed / success
embedded_plan_candidate_labels: HISTORICAL_CONDITIONAL_TEXT / review-and-promotion conditions satisfied by V2-S4-PLAN-REVIEW1 APPROVE and formal result 5cb3f585a0cddffbd823c785b1d39ebd1834c1df / not live authorization
stage_4_planning: FORMAL_PLAN_PROMOTED / PASS_ACCEPTED_ONLY_AFTER_V2-S4-PLAN-CLOSEOUT1_INDEPENDENT_APPROVE_AND_ORDINARY_FAST_FORWARD / CURRENT_CANDIDATE_NOT_YET_EFFECTIVE
stage_4_implementation_authorization: NOT_GRANTED
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry: NOT_GRANTED
stage_6_status_result_relay: NOT_GRANTED
current_task: V2-S4-PLAN-CLOSEOUT1
current_task_status: WORKTREE_RESULT_READY_FOR_REVIEW
stage_4_contract_status: CLOSED_BY_FORMAL_PLAN_RESULT / PackageToolDefinitionV1 + launch_session_tool + nine-outcome immutable LauncherReceiptV1
next_authorized_task: V2-S4-PLAN-CLOSEOUT-REVIEW1 / ZERO_WRITE_ONLY
closeout_effective_only_if: V2-S4-PLAN-CLOSEOUT-REVIEW1 APPROVE / P0=0 / P1=0 / P2=0 AND closeout candidate ordinary-fast-forwarded as formal head
effective_stage_4_planning: PASS_ACCEPTED
effective_stage_4_implementation_authorization: NOT_GRANTED
effective_stage_4_launcher_authorization: NOT_GRANTED
effective_next_authorized_task: NONE
effective_stage_5_workbuddy_entry_authorization: NOT_GRANTED
effective_stage_6_status_result_relay_authorization: NOT_GRANTED
effective_final_package_gate_authorization: NOT_GRANTED
final_package_gate: LATER_FINAL_DELIVERY_OR_INSTALLER_TASK / NOT_GRANTED / DUE_BEFORE_STAGE5_PRODUCTION_ACCEPTANCE
```

腾讯WorkBuddy是唯一运行中的Agent；它读取已验证金钥匙版OpenMontage Package Guide后承担生产角色。阶段2已经接受完整必带工具链的Registration/Locator实现和一次真实临时Package验证。阶段3已完成Remotion与HyperFrames的有界探测、报告、逐能力授权集成合同实现并正式收口；两项始终是OpenMontage候选能力，Shell不选择渲染器，缺失、拒绝或延期不阻塞基础工具链路径。

## 已接受对象

- 阶段1已审对象：`041c6600dc8eb9094b5c93cb4a4ed088894578af`；正式集成边界：`fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9`。
- 阶段2完整工具链登记实现：`709c8e880b144fa9e9be26e9feb5d776dd6025e2`；状态收口：`95eeeff175060f06ca2f549737e724160edc9e14`。它证明登记能力、负面测试和一次临时Package组装/登记，不证明最终Package已经保留。
- 阶段3实现：`a3f8959682d296301dc573c2835f8c705a52e8b2`，独立`APPROVE / P0=0 / P1=0 / P2=0`并正式推广；closeout：`7c15aae4e77c579309312b21c79076f930970214`，已正式推广。
- 阶段3证据：55 direct、10 hygiene、199 full，全部最终退出0且无skip；未证明真实第三方/大陆镜像下载、生产DataRoot集成、WorkBuddy、Stage4、Provider或媒体/视频E2E。
- 阶段4规划：`5cb3f585a0cddffbd823c785b1d39ebd1834c1df`，`V2-S4-PLAN-REVIEW1`最终`APPROVE / P0=0 / P1=0 / P2=0`并正式推广；正式CI run `32337744225`为`completed/success`。两轮历史`REQUEST_CHANGES`已经闭合定义hash环、receipt结果/优先级/非法输入、可伪造摘要证据及Stage3 `managed/explicit/PATH`交接问题。
- 当前正式树tracked精确35。最终Release、生产PackageRoot和生产Registration仍属于后续最终交付/Installer任务，最迟在Stage5真实WorkBuddy生产验收前完成；它不是Stage4规划或编码前置。

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

本状态closeout候选仍须独立只读审查和普通fast-forward后才能把`stage_4_planning`记为`PASS_ACCEPTED`。生效后的固定状态只能是：Stage4 planning `PASS_ACCEPTED`；Stage4 implementation与Launcher `NOT_GRANTED`；`next_authorized_task: NONE`；Stage5、Stage6及最终Package Gate均`NOT_GRANTED`。本closeout不授权任何实现Builder。
