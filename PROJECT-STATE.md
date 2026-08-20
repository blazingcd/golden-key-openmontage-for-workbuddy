# Project State

更新时间：2026-08-20

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
stage_4_launcher_authorization: NOT_GRANTED
stage_5_workbuddy_entry: NOT_GRANTED
stage_6_status_result_relay: NOT_GRANTED
current_task: V2-S4-FINAL-HANDOFF-HYGIENE-AUTH-REVISION1
current_task_status: AUTHORIZATION_CANDIDATE / WORKTREE_RESULT_READY_FOR_ZERO_WRITE_REVIEW / PASS_ACCEPTED_ONLY_AFTER_APPROVE_AND_ORDINARY_FAST_FORWARD
stage_4_contract_status: CLOSED_BY_FORMAL_PLAN_RESULT / PackageToolDefinitionV1 + launch_session_tool + nine-outcome immutable LauncherReceiptV1
next_authorized_task: V2-S4-FINAL-HANDOFF-HYGIENE-BUILDER1 / EXACT_SIX_PATHS / EFFECTIVE_ONLY_AFTER_THIS_AUTHORIZATION_REVISION_ZERO_WRITE_APPROVE_AND_ORDINARY_FAST_FORWARD
effective_stage_4_launcher_authorization: NOT_GRANTED
effective_stage_5_workbuddy_entry_authorization: NOT_GRANTED
effective_stage_6_status_result_relay_authorization: NOT_GRANTED
effective_final_package_gate_authorization: NOT_GRANTED
final_package_gate: LATER_FINAL_DELIVERY_OR_INSTALLER_TASK / NOT_GRANTED / DUE_BEFORE_STAGE5_PRODUCTION_ACCEPTANCE
```

## Stage 4最终交接卫生收口授权修订候选

原三路径卫生授权已在`78ee170678f80b71b3a88de95703a522a1f80cbc`正式推广。其实际Builder在创建worktree、修改文件、运行测试或提交推送前发现`README.md`、`README_zh-CN.md`、`PROJECT_CONTEXT.md`也是 materially stale 的当前入口，依第4路径停止规则报告`INCOMPLETE / STOPPED_SCOPE_EXPANSION`；该尝试为零worktree、零修改、零测试、零提交/推送，WSL未启动。

本修订候选从正式对象`78ee170678f80b71b3a88de95703a522a1f80cbc`、tree `b3e0c2d2e2bc660951f6b54868096b1e43751d36`和tracked精确37接管，只修改`PROJECT-STATE.md`与`docs/workbuddy/v2/TASK-REGISTER.md`。它不执行实际卫生修改、不运行项目测试、不启动WSL，也不改变已接受的Stage4产品状态。

只有本修订候选经独立零写Reviewer返回`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward进入实时`origin/codex/workbuddy-shell-v2`后，`V2-S4-FINAL-HANDOFF-HYGIENE-BUILDER1`才获得执行权。后续Builder必须从届时最新正式对象接管，并且只可修改`.github/workflows/ci.yml`、`docs/workbuddy/v2/README.md`、`docs/workbuddy/v2/MODULE-DISPOSITION.md`、`README.md`、`README_zh-CN.md`、`PROJECT_CONTEXT.md`：CI仅把`actions/checkout@v4`和`actions/setup-python@v5`分别升为`@v6`；五个当前/映射入口文档只机械同步Stage3与Stage4现行事实，包括Stage3已接受公共签名和结果闭集、Stage4 `launch_session_tool`、`PackageToolDefinitionV1`、不可改写`LauncherReceiptV1`、tracked精确37。Stage5、Stage6、最终Package物化和生产登记继续保持`NOT_GRANTED`或未证明。

该后续任务只删除陈旧的现在时Stage3/4未实现、旧Stage3签名/结果/模型及旧Gate展示，保留明确标为historical的证据；禁止修改生产代码、测试、其他权威合同、`WORK-LOG.md`或历史证据，禁止启动或预写Stage5/6，禁止执行真实WorkBuddy、Provider、Runtime或媒体工作。需要第7个实际路径时必须`INCOMPLETE`停止。授权交付后本修订Builder自解析为完成，`effective_current_task=NONE`，唯一下一授权任务为上述精确六路径卫生Builder。

腾讯WorkBuddy是唯一运行中的Agent；它读取已验证金钥匙版OpenMontage Package Guide后承担生产角色。阶段2已经接受完整必带工具链的Registration/Locator实现和一次真实临时Package验证。阶段3已完成Remotion与HyperFrames的有界探测、报告、逐能力授权集成合同实现并正式收口；两项始终是OpenMontage候选能力，Shell不选择渲染器，缺失、拒绝或延期不阻塞基础工具链路径。

## 已接受对象

- 阶段1已审对象：`041c6600dc8eb9094b5c93cb4a4ed088894578af`；正式集成边界：`fd68eb5a33af4c77b3bc879ca0d0c75b4c22e5b9`。
- 阶段2完整工具链登记实现：`709c8e880b144fa9e9be26e9feb5d776dd6025e2`；状态收口：`95eeeff175060f06ca2f549737e724160edc9e14`。它证明登记能力、负面测试和一次临时Package组装/登记，不证明最终Package已经保留。
- 阶段3实现：`a3f8959682d296301dc573c2835f8c705a52e8b2`，独立`APPROVE / P0=0 / P1=0 / P2=0`并正式推广；closeout：`7c15aae4e77c579309312b21c79076f930970214`，已正式推广。
- 阶段3证据：55 direct、10 hygiene、199 full，全部最终退出0且无skip；未证明真实第三方/大陆镜像下载、生产DataRoot集成、WorkBuddy、Stage4、Provider或媒体/视频E2E。
- 阶段4规划：`5cb3f585a0cddffbd823c785b1d39ebd1834c1df`，`V2-S4-PLAN-REVIEW1`最终`APPROVE / P0=0 / P1=0 / P2=0`并正式推广；正式CI run `32337744225`为`completed/success`。两轮历史`REQUEST_CHANGES`已经闭合定义hash环、receipt结果/优先级/非法输入、可伪造摘要证据及Stage3 `managed/explicit/PATH`交接问题。
- 阶段4实现结果`fa9adb8470ab94b88ec9900ede03cb26f7de0ebd`经第八轮独立只读审查`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward；随后仅修复GitHub `setup-python`无`pyvenv.cfg`时的测试夹具，修复结果`13a3227b0c55bbe9039b46d7e92eba822b48f57e`也经独立审查`APPROVE / P0=0 / P1=0 / P2=0`并普通fast-forward。正式树tracked精确37。
- 官方Ubuntu CI run `32369588814`为`357 passed / 1 skipped / exit 0`；Windows最终证据为158 direct、11 hygiene、358 combined，全部exit 0且无skip。WSL仅用于临时Linux等价验证，测试后已清理并关闭，不是Stage4运行依赖。
- 阶段4closeout固定历史锚点为`b63d8c2bc2214bc39f18378dbe47057ef538301e`、tree `02814c6a4a483913e7b1abe3e9ee6d025236c951`；closeout独立审查为`APPROVE / P0=0 / P1=0 / P2=0`，正式CI run `32371507874`在Ubuntu 24.04 / Python 3.11.16上`357 passed / 1 skipped`。因此阶段4实现已是`PASS_ACCEPTED`；当时无活动产品任务和下一授权任务，当前仅新增上述有界最终交接卫生授权候选。
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

Stage 4规划、实现、closeout均已完成独立审查、普通fast-forward并由正式CI验证，`stage_4_planning=PASS_ACCEPTED`且`stage_4_implementation=PASS_ACCEPTED`。六权威同步、secret nondisclosure澄清、五路径实现、单文件CI夹具修复和closeout都已进入历史；原三路径卫生Builder已按边界安全停止，当前只存在`V2-S4-FINAL-HANDOFF-HYGIENE-AUTH-REVISION1`授权修订候选，后续精确六路径卫生Builder仅在其独立批准并正式推广后生效。`mirror_result/mirror_effect/mirror_repository_delivery_resolution`不改变或重新门禁产品状态。真实生产WorkBuddy/Launcher会话、Stage5、Stage6、Provider/媒体执行及final Package物化/生产登记仍为`NOT_GRANTED`或未证明。
