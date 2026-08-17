# WorkBuddy Shell V2 权威入口

状态：

```text
STAGE_1_PASS_ACCEPTED
STAGE_2_REOPENED_PACKAGE_REFRESH_REQUIRED
STAGE_2_PREVIOUS_PACKAGE_PASS_ACCEPTED_HISTORICAL
REPOSITORY_HYGIENE_PASS_ACCEPTED_AT_20DDAB75825C1B6E7DE5A51603AFE8B6FD82ECEB
STAGE_3_RUNTIME_SCOPE_CORRECTED_FOR_REVIEW
STAGE_3_IMPLEMENTATION_NOT_GRANTED
STAGE_4_LAUNCHER_NOT_GRANTED
STAGE_5_WORKBUDDY_ENTRY_NOT_GRANTED
STAGE_6_STATUS_RESULT_RELAY_NOT_GRANTED
STAGE_2_S3_RUNTIME_CORRECTION_REVIEW_READY
```

本仓库只实现WorkBuddy Shell V2。腾讯WorkBuddy是唯一运行中的Agent；它读取已验证金钥匙版OpenMontage执行包后承担生产角色，不存在第二个OpenMontage Agent进程。Shell只负责六模块。仓库卫生已收敛到固定33文件；当前只固化阶段二重新登记前置条件和阶段三至阶段六纠偏范围，不实施任何模块。

运行时裁决：金钥匙版交付包自带锁定私有Python；阶段三只从受管路径、明确登记的宿主工具和PATH命令解析中发现Python依赖、FFmpeg、Node、Remotion、HyperFrames及锁定浏览器，不扫描盘符。缺失项经missing-only计划、用户明确同意后从批准的中国大陆镜像准备；唯一临时例外是精确锁定的FFmpeg 9.0 `gyan.dev`资产，它在无代理/VPN大陆网络直连验证通过前保持阻断。任何组件都不能自动回退其他海外源。

阶段3至阶段6按编号建设和验收，但用户实际运行从阶段5入口开始：阶段5调用阶段2 Locator重验和阶段3单一闭集接口；Runtime已就绪才进入阶段4，阶段6转交Runtime及Launcher事实。若缺失，用户另行确认计划后由阶段3准备并停止，原请求不自动重试。

## 权威文档

- `TASK-REGISTER.md`：实时任务、精确Git对象、授权与下一任务的唯一状态权威。
- `PROJECT-CHARTER.md`：产品角色、六模块职责和非目标。
- `PACKAGE-REGISTRATION-CONTRACT.md`：旧Package已接受合同和当前Package重新登记裁决。
- `ACCEPTANCE-MATRIX.md`：证据、阶段3闭集发现/missing-only准备、阶段6零代码出口与Gate语义。
- `DRIFT-GUARD.md`：停止条件、范围保护和Git生命周期。
- `MODULE-DISPOSITION.md`：V1能力处置的历史映射，不是当前实现授权。

阶段3至阶段6不另建平行职责文档：职责只以`PROJECT-CHARTER.md`为准，实施必要性和PASS边界只以`ACCEPTANCE-MATRIX.md`为准，实时授权只以`TASK-REGISTER.md`为准。

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
