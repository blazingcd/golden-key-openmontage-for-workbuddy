# WorkBuddy Shell V2 权威入口

状态：

```text
STAGE_1_PASS_ACCEPTED
STAGE_2_REOPENED_REQUIRED_TOOLCHAIN_PACKAGE_REFRESH
STAGE_2_PREVIOUS_PYTHON_ONLY_PACKAGE_PASS_ACCEPTED_HISTORICAL
REPOSITORY_HYGIENE_PASS_ACCEPTED_AT_20DDAB75825C1B6E7DE5A51603AFE8B6FD82ECEB
STAGE_3_REOPENED_OPTIONAL_CAPABILITY_RECLASSIFICATION_REQUIRED
STAGE_3_IMPLEMENTATION_NOT_GRANTED
STAGE_4_LAUNCHER_NOT_GRANTED
STAGE_5_WORKBUDDY_ENTRY_NOT_GRANTED
STAGE_6_STATUS_RESULT_RELAY_NOT_GRANTED
REQUIRED_TOOLCHAIN_CORRECTION_DOCS_REVIEW_READY
```

本仓库只实现WorkBuddy Shell V2。腾讯WorkBuddy是唯一运行中的Agent；它读取已验证金钥匙版OpenMontage执行包后承担生产角色，不存在第二个OpenMontage Agent进程。Shell只负责六模块。仓库卫生已收敛到固定33文件；当前只固化阶段二重新登记前置条件和阶段三至阶段六纠偏范围，不实施任何模块。

运行时裁决：金钥匙版交付包必须自带并由阶段2登记完整必带工具链，即可用Python 3.10+环境及核心依赖、FFmpeg/ffprobe、Node/npm/npx；Node按当前Package最高要求锁定，当前不得低于22。只登记Python的旧阶段2结果不再足够。阶段3只处理WorkBuddy/OpenMontage已经锁定的一个可选Remotion或HyperFrames能力及其Lock声明附属资产，不处理三项Prerequisites。

终端用户可选能力下载必须使用批准的中国大陆镜像，形成精确missing-only计划并取得明确同意；不自动海外回退。`gyan.dev` FFmpeg候选改归Package组装供应链审查。阶段3与阶段4的真实暂停/继续关系等待WorkBuddy消费者合同重新冻结，Shell不选渲染器、不自动重试原请求。

## 权威文档

- `TASK-REGISTER.md`：实时任务、精确Git对象、授权与下一任务的唯一状态权威。
- `PROJECT-CHARTER.md`：产品角色、六模块职责和非目标。
- `PACKAGE-REGISTRATION-CONTRACT.md`：旧Package已接受合同和当前Package重新登记裁决。
- `ACCEPTANCE-MATRIX.md`：证据、阶段3单一可选能力missing-only准备、阶段6零代码出口与Gate语义。
- `DRIFT-GUARD.md`：停止条件、范围保护和Git生命周期。
- `MODULE-DISPOSITION.md`：V1能力处置的历史映射，不是当前实现授权。

阶段3至阶段6不另建平行职责文档：职责只以`PROJECT-CHARTER.md`为准，实施必要性和PASS边界只以`ACCEPTANCE-MATRIX.md`为准，实时授权只以`TASK-REGISTER.md`为准。

旧阶段3可执行任务包、入口签名、全组件Runtime Lock和条件授权已经`SUPERSEDED`或暂停。当前权威只冻结重新规划的前置输入和边界；必须先完成阶段2完整必带工具链登记，再取得真实WorkBuddy/OpenMontage可选能力消费者合同，之后才能冻结新的执行步骤、路径和精确文件范围。阶段3实现仍为`NOT_GRANTED`。

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
