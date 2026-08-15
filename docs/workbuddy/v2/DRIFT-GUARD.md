# WorkBuddy Shell V2 防漂移与Git生命周期

状态：`ACTIVE / FAIL_CLOSED`

## 立即停止

出现以下任一情况时停止并报告`INCOMPLETE`或明确的范围冲突，不得顺手修复：

- 当前HEAD、实时正式远端、任务起点、允许路径、tracked计数或锁定blob不一致；
- 需要修改任务未授权路径，或与其他任务/用户改动重叠；
- 需要Shell选择或运行Pipeline、Stage、Provider、模型、媒体或创意；
- 需要实现未授权的Runtime、Launcher、WorkBuddy入口、状态结果转交或其他阶段；
- 需要扫描磁盘、猜测“最新”执行包、读取未验证Package Guide或修改外部执行包；
- 需要把PackageRoot、Python、cwd、测试编号、重试或证据控制拼入literal `user_message`；
- 命令超时、输出截断、没有最终退出、证据缺失，或文档与任务账本冲突；
- 需要reset、stash、merge、rebase或改写已审对象。

## 产品边界

WorkBuddy负责对话，OpenMontage Agent负责生产，Shell只负责六模块。仓库Agent不得运行视频Pipeline、Provider或媒体生产。SaaS Core不是Package Registration对象，也不在Shell V2当前实现范围。

外部Package Guide只有在Registration身份完整验证、Locator返回已验证身份后，才可由对应下游消费者读取。本仓库根`AGENT_GUIDE.md`只治理Shell V2，不能替代或预先信任外部Guide。

`user_message`只包含用户真实会说的业务请求、素材、事实、授权和期望结果。包身份、路径、Python、cwd、命令、测试、停止条件和证据采集只进入独立的`executor_controls`。

## Git任务生命周期

- Builder分支是单任务临时隔离；不得发展为长期分支。
- Reviewer独立只读，不建立长期审阅分支，不修改结果制造APPROVE。
- 用户接受或Reviewer批准不等于已交付。
- 任务或阶段只有在已审结果进入`origin/codex/workbuddy-shell-v2`后才算仓库完成。
- 正式主线只允许fast-forward到已审集成结果；不得merge/rebase推进中的`main`或旧长期分支。
- 推广后，所有已完全合入且无未合入commit的临时远端分支必须删除。
- 本地分支仅在对应worktree关闭后安全删除；不得清理其他任务的worktree、branch、stash、tracked、untracked或ignored现场。
- 下一阶段接管只能使用正式主线最新精确commit，不能使用任务分支。

只精确暂存授权路径，禁止`git add .`。正式状态只以`TASK-REGISTER.md`为准；Git历史保存旧Prompt、计划、报告和证据，但不恢复其活动授权。

## 证据边界

静态检查、单元测试、Package Registration成功、ZIP、Guide读取或旧运行历史都不能证明真实Installer、Runtime、Launcher、WorkBuddy、OpenMontage生产、Provider、媒体、SaaS或业务效果。任何Gate对象不一致或无最终退出一律不是PASS。
