# WorkBuddy Shell V2 权威入口

状态：

```text
STAGE_1_PASS_ACCEPTED
STAGE_2_REGISTRATION_LOCATOR_IMPLEMENTATION_PASS_ACCEPTED
STAGE_2_REAL_TEMPORARY_PACKAGE_VALIDATION_PASS_ACCEPTED
FINAL_PACKAGE_ARTIFACT_NOT_MATERIALIZED
PRODUCTION_PACKAGE_REGISTRATION_NOT_CREATED
REPOSITORY_HYGIENE_PASS_ACCEPTED_AT_20DDAB75825C1B6E7DE5A51603AFE8B6FD82ECEB
STAGE_3_PLANNING_PASS_ACCEPTED
STAGE_3_IMPLEMENTATION_NOT_GRANTED
STAGE_4_LAUNCHER_NOT_GRANTED
STAGE_5_WORKBUDDY_ENTRY_NOT_GRANTED
STAGE_6_STATUS_RESULT_RELAY_NOT_GRANTED
STAGE_3_PRETAKEOVER_REPLAN_DOCS_PASS_ACCEPTED_AFTER_INDEPENDENT_REVIEW_AND_FORMAL_FAST_FORWARD
```

本仓库只实现WorkBuddy Shell V2。腾讯WorkBuddy是唯一运行中的Agent；它读取已验证金钥匙版OpenMontage执行包后承担生产角色，不存在第二个OpenMontage Agent进程。Shell只负责六模块。仓库卫生已收敛到固定33文件；当前只固化阶段3接管前的缩减规划，不实施任何模块。

阶段2已经接受Registration/Locator实现，以及一次包含可用Python 3.10+环境及核心依赖、FFmpeg/ffprobe、Node/npm/npx的真实临时Package验证。临时Package随后已删除，因此最终Release、已安装生产PackageRoot和生产Registration仍不存在。阶段3只处理WorkBuddy/OpenMontage已经选定的`none`、Remotion或HyperFrames之一及Package自有能力Lock声明的附属资产，不处理三项Prerequisites。

终端用户可选能力下载必须使用批准的中国大陆镜像，形成精确missing-only计划并取得明确同意；不自动海外回退。`gyan.dev` FFmpeg候选归Package组装供应链审查。阶段3建议唯一入口为`prepare_optional_capability(data_root, capability_request, authorization_receipt=None)`，最大代码面为一个新增生产模块、一次仅导出修改和一个直接测试文件。Shell不选渲染器、不扫描盘符、不运行视频、不自动重试原请求。

## 权威文档

- `TASK-REGISTER.md`：实时任务、精确Git对象、授权与下一任务的唯一状态权威。
- `PROJECT-CHARTER.md`：产品角色、六模块职责和非目标。
- `PACKAGE-REGISTRATION-CONTRACT.md`：阶段2已接受Registration/Locator合同及其非Installer、非最终分发边界。
- `ACCEPTANCE-MATRIX.md`：证据、阶段3单一可选能力missing-only准备、阶段6零代码出口与Gate语义。
- `DRIFT-GUARD.md`：停止条件、范围保护和Git生命周期。
- `MODULE-DISPOSITION.md`：V1能力处置的历史映射，不是当前实现授权。

阶段3至阶段6不另建平行职责文档：职责只以`PROJECT-CHARTER.md`为准，实施必要性和PASS边界只以`ACCEPTANCE-MATRIX.md`为准，实时授权只以`TASK-REGISTER.md`为准。

旧阶段3可执行任务包、入口签名、Shell自有全组件Runtime Lock和条件授权已经`SUPERSEDED`。当前权威已经冻结新阶段3的输入、结果、八步路径、数据边界、最大文件范围和阶段4至阶段6衔接。阶段5先经阶段2重验生产Package；阶段4基础调用直接使用必带工具链，只有可选执行才额外要求阶段3回执；阶段6只转交事实。

阶段3实现仍为`NOT_GRANTED`。启动前必须保留最终Release，安装并生产登记PackageRoot，在新进程通过Locator重验，冻结Manifest覆盖的Package自有能力Lock和真实WorkBuddy暂停/同意/继续合同，并从最新正式Git对象取得精确Builder授权。

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
