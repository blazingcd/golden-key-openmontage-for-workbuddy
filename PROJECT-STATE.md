# Project State

更新时间：2026-08-21

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
repository_tracked_files: 37
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
stage_5_planning_t1_hard_stop: PLANNING_BLOCKED_EXTERNAL_CONTRACT when exact real WorkBuddy Skill/install/entry/call contract is not evidenced; never fabricate interface or use CLI/MCP/second-Skill fallback
stage_5_planning: PLANNING_BLOCKED_EXTERNAL_CONTRACT
stage_5_planning_status: T1_EXTERNAL_CONTRACT_UNCLOSED / CURRENT_LIVE_AUTHORITY
stage_5_planning_candidate_promotion_effect: DOCS_ONLY / independent APPROVE plus ordinary fast-forward only formally fixes the planning documents; it does not make Stage 5 planning PASS_ACCEPTED or authorize implementation
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry: NOT_GRANTED
stage_6_status_result_relay: NOT_GRANTED
stage_5_implementation_authorization: NOT_GRANTED
current_task: NONE
current_task_status: NO_ACTIVE_TASK
stage_4_contract_status: CLOSED_BY_FORMAL_PLAN_RESULT / PackageToolDefinitionV1 + launch_session_tool + nine-outcome immutable LauncherReceiptV1
next_authorized_task: NONE
stage_5_t1_evidence_authorization_candidate: V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE-AUTHORIZATION1 / DOCS_ONLY / READY_FOR_INDEPENDENT_ZERO_WRITE_REVIEW / NOT_FORMALLY_PROMOTED
pending_next_authorized_task: V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE1 / EFFECTIVE_ONLY_AFTER_THIS_AUTHORIZATION_REVIEW_APPROVE_AND_ORDINARY_FAST_FORWARD
effective_stage_4_launcher_authorization: NOT_GRANTED
effective_stage_5_workbuddy_entry_authorization: NOT_GRANTED
effective_stage_6_status_result_relay_authorization: NOT_GRANTED
effective_final_package_gate_authorization: NOT_GRANTED
final_package_gate: LATER_FINAL_DELIVERY_OR_INSTALLER_TASK / NOT_GRANTED / DUE_BEFORE_STAGE5_PRODUCTION_ACCEPTANCE
```

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

本节只固化用户对 T1 证据核验的授权边界，不代表 T1 证据已经完成，也不授权 Stage 5 实现、真实 WorkBuddy、Launcher、Provider、媒体、最终 Package 或 Stage 6。候选推广前 `current_task=NONE`、`next_authorized_task=NONE`；只有候选经独立零写 Reviewer `APPROVE / P0=0 / P1=0 / P2=0` 并普通 fast-forward 后，下一项才是唯一的 `V2-S5-T1-OFFICIAL-CONTRACT-EVIDENCE1`。

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
candidate_status: READY_FOR_INDEPENDENT_ZERO_WRITE_REVIEW / NOT_FORMALLY_PROMOTED
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

若官方资料不能同时证明五项，Evidence Builder 完成时必须保持 `stage_5_planning=PLANNING_BLOCKED_EXTERNAL_CONTRACT`、`stage_5_implementation_authorization=NOT_GRANTED`，最终结果记为 `T1_EVIDENCE_INCOMPLETE`，并将 `next_authorized_task=NONE`；不得填造路径、接口、参数，不得授权实施。即使官方资料足以形成五项证据，仍只能记为证据候选/待独立审查，随后另行进行权威状态收口；不得从 Evidence1 自动推导 Stage 5 实现授权。

本授权候选及其后续 Evidence1 均禁止：生产代码、测试、CI、pyproject、Package 字节、Registration/Activation、真实 WorkBuddy、Launcher、Provider、Runtime 下载、媒体、WSL、Stage 6、final Package、production Registration，以及 CLI/MCP/第二 Skill/第二 Agent/并行入口。

## 已完成的Stage 4最终交接卫生收口

原三路径卫生授权已在`78ee170678f80b71b3a88de95703a522a1f80cbc`正式推广。其实际Builder在创建worktree、修改文件、运行测试或提交推送前发现`README.md`、`README_zh-CN.md`、`PROJECT_CONTEXT.md`也是 materially stale 的当前入口，依第4路径停止规则报告`INCOMPLETE / STOPPED_SCOPE_EXPANSION`；该尝试为零worktree、零修改、零测试、零提交/推送，WSL未启动。该历史结果已经由后续修订授权和最终六路径结果闭合。

最终卫生Builder从正式授权对象接管，累计只修改`.github/workflows/ci.yml`、`docs/workbuddy/v2/README.md`、`docs/workbuddy/v2/MODULE-DISPOSITION.md`、`README.md`、`README_zh-CN.md`、`PROJECT_CONTEXT.md`六个路径；正式结果为`4636e27a62aad9f1b721e6c482e34b44d350503c`、tree `fdf24f8450ac4bb48e5337cd7aa3477794796d19`、tracked精确37。独立Reviewer最终返回`APPROVE / P0=0 / P1=0 / P2=0`；本地Python 3.14.7证据为11 hygiene、358 combined且全部exit 0；正式CI run `32386393634`为`completed/success`、Python 3.14.7、`357 passed / 1 skipped`、actions v6且没有Node20 deprecation warning。

本收口只把上述已交付事实机械镜像到`PROJECT-STATE.md`与`docs/workbuddy/v2/TASK-REGISTER.md`，采用恒定self-resolving mirror规则，不形成新的产品任务。实时状态为`current_task=NONE / current_task_status=NO_ACTIVE_TASK / next_authorized_task=NONE`；Stage3/4继续`PASS_ACCEPTED`，Stage5、Stage6、最终Package物化和生产登记继续保持`NOT_GRANTED`或未证明。任何后续任务都必须另行明确授权。

腾讯WorkBuddy是唯一运行中的Agent；它读取已验证金钥匙版OpenMontage Package Guide后承担生产角色。阶段2已经接受完整必带工具链的Registration/Locator实现和一次真实临时Package验证。阶段3已完成Remotion与HyperFrames的有界探测、报告、逐能力授权集成合同实现并正式收口；两项始终是OpenMontage候选能力，Shell不选择渲染器，缺失、拒绝或延期不阻塞基础工具链路径。

## 已接受对象

- 阶段1已审对象：`041c6600dc8eb9094b5c93cb4a4ed088894578af`；正式集成边界：`fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9`。
- 阶段2完整工具链登记实现：`709c8e880b144fa9e9be26e9feb5d776dd6025e2`；状态收口：`95eeeff175060f06ca2f549737e724160edc9e14`。它证明登记能力、负面测试和一次临时Package组装/登记，不证明最终Package已经保留。
- 阶段3实现：`a3f8959682d296301dc573c2835f8c705a52e8b2`，独立`APPROVE / P0=0 / P1=0 / P2=0`并正式推广；closeout：`7c15aae4e77c579309312b21c79076f930970214`，已正式推广。
- 阶段3证据：55 direct、10 hygiene、199 full，全部最终退出0且无skip；未证明真实第三方/大陆镜像下载、生产DataRoot集成、WorkBuddy、Stage4、Provider或媒体/视频E2E。
- 阶段4规划：`5cb3f585a0cddffbd823c785b1d39ebd1834c1df`，`V2-S4-PLAN-REVIEW1`最终`APPROVE / P0=0 / P1=0 / P2=0`并正式推广；正式CI run `32337744225`为`completed/success`。两轮历史`REQUEST_CHANGES`已经闭合定义hash环、receipt结果/优先级/非法输入、可伪造摘要证据及Stage3 `managed/explicit/PATH`交接问题。
- 阶段4实现结果`fa9adb8470ab94b88ec9900ede03cb26f7de0ebd`经第八轮独立只读审查`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward；随后仅修复GitHub `setup-python`无`pyvenv.cfg`时的测试夹具，修复结果`13a3227b0c55bbe9039b46d7e92eba822b48f57e`也经独立审查`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward。正式树tracked精确37。
- 官方Ubuntu CI run `32369588814`为`357 passed / 1 skipped / exit 0`；Windows最终证据为158 direct、11 hygiene、358 combined，全部exit 0且无skip。WSL仅用于临时Linux等价验证，测试后已清理并关闭，不是Stage4运行依赖。
- 阶段4closeout固定历史锚点为`b63d8c2bc2214bc39f18378dbe47057ef538301e`、tree `02814c6a4a483913e7b1abe3e9ee6d025236c951`；closeout独立审查为`APPROVE / P0=0 / P1=0 / P2=0`，正式CI run `32371507874`在Ubuntu 24.04 / Python 3.11.16上`357 passed / 1 skipped`。因此阶段4实现已是`PASS_ACCEPTED`；最终交接卫生结果`4636e27a62aad9f1b721e6c482e34b44d350503c`也已独立批准、正式推广并由CI验证，当前不存在活动任务或下一授权任务。
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

Stage 4规划、实现、closeout及最终交接卫生均已完成独立审查、普通fast-forward并由正式CI验证，`stage_4_planning=PASS_ACCEPTED`且`stage_4_implementation=PASS_ACCEPTED`。六权威同步、secret nondisclosure澄清、五路径实现、单文件CI夹具修复、产品closeout和六路径最终入口卫生都已进入历史；原三路径卫生Builder的安全停止也已闭合。当前没有活动任务或下一授权任务。`mirror_result/mirror_effect/mirror_repository_delivery_resolution`不改变或重新门禁产品状态。真实生产WorkBuddy/Launcher会话、Stage5、Stage6、Provider/媒体执行及final Package物化/生产登记仍为`NOT_GRANTED`或未证明。
