# WorkBuddy Shell V2 权威入口

状态：

```text
STAGE_1_PASS_ACCEPTED
STAGE_2_REGISTRATION_LOCATOR_IMPLEMENTATION_PASS_ACCEPTED
STAGE_2_REAL_TEMPORARY_PACKAGE_VALIDATION_PASS_ACCEPTED
FINAL_PACKAGE_ARTIFACT_NOT_MATERIALIZED
PRODUCTION_PACKAGE_REGISTRATION_NOT_CREATED
REPOSITORY_HYGIENE_PASS_ACCEPTED_AT_20DDAB75825C1B6E7DE5A51603AFE8B6FD82ECEB
REPOSITORY_TRACKED_FILES_40
STAGE_3_PLANNING_PASS_ACCEPTED
STAGE_3_IMPLEMENTATION_PASS_ACCEPTED_AT_A3F8959682D296301DC573C2835F8C705A52E8B2
STAGE_3_CLOSEOUT_PASS_ACCEPTED_AT_7C15AAE4E77C579309312B21C79076F930970214
STAGE_4_PLANNING_PASS_ACCEPTED
STAGE_4_IMPLEMENTATION_PASS_ACCEPTED
STAGE_5_IN_PROGRESS_ENTRY_CODE_COMPLETE_REAL_INTEGRATION_INCOMPLETE
STAGE_6_STATUS_RESULT_RELAY_NOT_GRANTED
FINAL_PACKAGE_PACKAGE_ROOT_NOT_CREATED
PRODUCTION_REGISTRATION_ACTIVATION_NOT_CREATED
FINAL_INSTALLED_SKILL_NOT_CREATED
REAL_WORKBUDDY_LAUNCHER_RECEIPT_NOT_PROVED
```

本仓库只实现WorkBuddy Shell V2。腾讯WorkBuddy是唯一运行中的Agent；它读取已验证金钥匙版OpenMontage执行包后承担生产角色，不存在第二个OpenMontage Agent进程。Shell只负责六模块。当前正式树tracked精确40；Stage 3与Stage 4规划、实现均已`PASS_ACCEPTED`。Stage 5为`IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`，不是整体PASS；Stage 6、最终Package/PackageRoot、生产Registration/Activation、最终安装Skill和真实WorkBuddy回执仍未证明或未创建。

阶段2已经接受Registration/Locator实现，以及一次包含可用Python 3.10+环境及核心依赖、FFmpeg/ffprobe、Node/npm/npx的真实临时Package验证。Stage 3实现`a3f8959682d296301dc573c2835f8c705a52e8b2`和closeout `7c15aae4e77c579309312b21c79076f930970214`均已正式推广，状态为`PASS_ACCEPTED`。Remotion/HyperFrames是OpenMontage候选能力；Shell只做有界探测、提示和逐能力获批集成，不选择生产渲染器。

阶段3唯一入口为`prepare_optional_capabilities(data_root, capability_definitions, user_decisions=None)`，结果闭集为`DETECTION_REPORT/CONSENT_REQUIRED/INTEGRATED/SKIPPED/BLOCKED`。已接受证据为55 direct、10 hygiene、199 full，全部退出0且无skip；没有真实第三方/大陆镜像下载、生产DataRoot、WorkBuddy、Stage4、Provider或媒体/视频E2E证明。

阶段4唯一入口为`launch_session_tool(data_root, user_message, executor_controls, package_tool_definition, local_capability_evidence=(), cancel_event=None)`。它只消费批准Package定义/最终交付Installer owner提供的release-specific immutable `PackageToolDefinitionV1`，恰好启动一个固定Package工具，并返回九值闭集、递归不可改写的`LauncherReceiptV1`。Stage4对Provider和Runtime保持opaque，不硬编码或选择Remotion、HyperFrames及任何Provider；只有固定定义声明本地能力要求时才接收完整批准定义和未改写Stage3原始事实并重新核验实际字节。

## 权威文档

- `TASK-REGISTER.md`：实时任务、精确Git对象、授权与下一任务的唯一状态权威。
- `PROJECT-CHARTER.md`：产品角色、六模块职责和非目标。
- `PACKAGE-REGISTRATION-CONTRACT.md`：阶段2已接受Registration/Locator合同及其非Installer、非最终分发边界。
- `ACCEPTANCE-MATRIX.md`：证据、阶段3双候选能力有界探测与逐能力批准集成、阶段6零代码出口与Gate语义。
- `DRIFT-GUARD.md`：停止条件、范围保护和Git生命周期。
- `MODULE-DISPOSITION.md`：V1能力处置的历史映射，不是当前实现授权。

阶段3至阶段6不另建平行职责文档：职责只以`PROJECT-CHARTER.md`为准，实施必要性和PASS边界只以`ACCEPTANCE-MATRIX.md`为准，实时授权只以`TASK-REGISTER.md`为准。

旧阶段3可执行任务包、入口签名、Shell自有全组件Runtime Lock和条件授权已经`SUPERSEDED`。阶段5拥有真实WorkBuddy新会话、唯一入口、literal `user_message`不变、逐能力询问和同任务继续；这些不是Stage4前置。当前R00只做十二文档纠偏；R01至R08必须严格顺序执行且各自另行授权。阶段5完整PASS的五类物证与任务链只以`TASK-REGISTER.md`当前R00节为准。阶段6只在Stage4回执和Stage5真实消费者存在后判断，可直接消费时以`STAGE_6_DIRECT_LAUNCHER_RECEIPT_REUSE`和生产代码0结束；全项目业务E2E另行处理，不称为阶段7。

Stage4规划和实现已经完成独立审查、普通fast-forward与正式CI验证，均为`PASS_ACCEPTED`；这不证明真实生产WorkBuddy/Launcher会话、Provider或媒体执行。Stage4先调用`locate_active_package(data_root)`，基础固定工具调用不依赖Remotion/HyperFrames；只有固定定义声明要求时才使用相同capability+definition的Stage3 `PRESENT`或`INTEGRATED`证据。最终Package/生产Registration归后续最终交付或Installer任务，最迟在Stage5真实生产验收前完成；Stage5/6没有因本次入口同步获得授权。

## Git任务生命周期

- Builder分支只是一项任务的临时隔离，不是长期交付分支。
- Reviewer必须独立且只读；Reviewer无需建立长期分支。
- 用户接受或Reviewer批准不等于已经交付到仓库正式主线。
- 任务或阶段只有在已审结果进入`origin/codex/workbuddy-shell-v2`后，才算仓库完成。
- 正式主线只允许fast-forward到已审集成结果；不得把推进中的`main`或旧长期分支merge/rebase回来。
- 推广后，所有已完全合入且无未合入commit的临时远端分支必须删除。
- 本地分支仅在对应worktree关闭后安全删除。
- 下一阶段接管只能使用正式主线最新精确commit，不能使用任务分支。

当前状态与下一步不得从Git历史、旧Prompt、旧任务包或聊天推断；只读`TASK-REGISTER.md`。
