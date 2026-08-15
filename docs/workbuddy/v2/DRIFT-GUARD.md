# WorkBuddy Shell V2 防漂移与停止规则

状态：`ACTIVE / FAIL_CLOSED`

## 1. 立即停止条件

执行任务出现以下任一事实时必须停止，不得“顺手修复”：

- 需要修改任务未授权的路径；
- 需要Shell决定Pipeline、Stage、Reviewer或Checkpoint；
- 需要Launcher理解Artifact业务语义；
- 需要Shell选择Provider或媒体处理路径；
- 需要把Core路径、Python、`.venv`、CLI、Pipeline或Stage加入普通用户消息；
- 需要通过临时脚本、外部Core目录或手工预转码制造PASS；
- 需要直接修改Core才能让当前Shell任务通过；
- 需要安装、下载、WorkBuddy、Provider、费用、发布或删除，但任务没有对应授权；
- 固定Git对象、Manifest、Lock、SHA、安装对象或工作树发生漂移；
- 发现另一任务正在修改重叠文件；
- 测试通过但找不到真实消费者和调用链；
- 命令超时、输出截断或没有最终退出状态；
- 实现规模明显超过任务单，或开始处理相邻阶段；
- 文档、代码和任务账本对同一状态给出不同结论。

停止后必须登记：

```text
status: STOPPED_SCOPE_EXPANSION | STOPPED_CONTRACT_CONFLICT | INCOMPLETE
last_verified_object:
last_successful_action:
new_fact:
affected_gate:
why_original_task_cannot_continue:
recommended_decision_or_new_task:
files_changed_before_stop:
```

状态语义固定如下：`BLOCKED`只用于执行或审阅开始前的依赖、精确输入或授权未满足；任务或审阅一旦开始，出现固定对象不一致、无最终退出、证据缺失或环境干扰必须记为`INCOMPLETE`。

## 2. 禁止实现模式

以下实现无论测试是否通过都不得进入V2：

- `if user_request ... choose_pipeline(...)`；
- Shell生成或修订Brief、Script、Scene Plan、Asset Manifest、Edit Decisions；
- Shell导入Core的Pipeline Loader或Checkpoint writer；
- Shell维护与Core Stage同构的FSM；
- Launcher接受任意命令字符串并直接交给shell；
- 根据目录名包含`v0.3.23`推断正式对象；
- 磁盘递归搜索后选择“看起来最新”的Core或Python；
- 把`doctor=pass`、ZIP成功或一个MP4写成最终验收；
- 为了本地成功而永久封锁所有API/Hybrid路径；
- 安装阶段无条件准备Remotion、HyperFrames、浏览器和大型模型；
- 由Shell硬编码transpose、9:16或其他媒体补丁；
- 用MCP重建Project/Stage/Artifact/Checkpoint工具面作为首版主链；
- 将Codex控制词、测试编号或PASS标准发送给WorkBuddy用户消息。

## 3. 普通用户消息边界

`user_message`只包含用户真实会说的业务请求、素材位置、事实、授权和期望结果。

以下只能进入`executor_controls`或测试卡：

- Shell/Core/包/安装实例身份；
- Python、CoreRoot、DataRoot和cwd；
- 模型选择、测试编号、重试预算和停止条件；
- 如何读取Guide、执行命令或判断PASS；
- 下载、Provider、费用和环境隔离控制；
- 证据采集和进程残留要求。

任何控制词进入literal `user_message`均为Gate失败。

## 4. 范围变更程序

发现合理但超范围的新需求时：

1. 当前任务停止在安全点；
2. 记录新事实和受影响Gate；
3. 判断归属：Shell、Core、Host、Tool、模型、Provider或产品范围；
4. 给出“不处理”“调整当前阶段”“新增后续任务”三个选项及影响；
5. 由用户批准后更新`PROJECT-CHARTER.md`、`TASK-REGISTER.md`和对应阶段计划；
6. 只有文档提交后才能恢复执行。

聊天中的临时同意不能替代任务账本和版本化文档更新。

## 5. Git与文件保护

- 不使用`git add .`或其他可能纳入未知文件的宽泛暂存；
- 不删除、移动、暂存或覆盖`.codex/config.toml`；
- 不删除、移动、暂存或覆盖当前未跟踪handoff，除非用户另行明确授权；
- 不merge/rebase `main`或长期旧分支进入V2；
- `immutable_code_baseline=2a2bf09832d558388dc2816c54b32a2dce4aa607`只冻结代码谱系；阶段1执行者必须使用新统筹从用户Prompt取得、并通过本地HEAD与远端分支三方一致核验的完整`stage_1_builder_start_commit`。字段仍为`PENDING_NEXT_SESSION_HANDOFF_COMMIT`或三方不一致时不得启动T1；不得直接checkout代码基线或任意`HEAD`；
- 不清理其他任务的tracked、untracked、ignored、stash或worktree现场；
- 每项迁移必须列出来源commit、文件、消费者和目标测试；
- 递归删除或移动前必须验证绝对目标路径和所有权；
- Core源码工作树只读，Shell任务不得修改。

## 6. 证据防错

必须分别报告：对象、安装、绑定、真实客户端、流程正确、真实能力、本地成片、业务效果、严格合同、Provider和发布。

非证明包括但不限于：

- 静态检查；
- 单元测试；
- doctor或registry成功；
- ZIP或安装成功；
- WorkBuddy读取Guide；
- 产生project.json或一个MP4；
- 历史对象曾经跑通。

任何Gate对象不一致或无最终退出一律`INCOMPLETE`，不得降格为PASS WITH WARNING。

## 7. 并发纪律

- 同一时间最多一个真实WorkBuddy执行任务；
- 后续阶段不得在前一阶段 `PASS_ACCEPTED` 前启动；阶段1 T1–T5 的内部串行依赖以 `TASK-REGISTER` 第4节为准；本规则不授权并行执行。
- 同一Gate的Builder和Reviewer必须独立；
- Reviewer不得修改代码来制造APPROVE；
- 后续真实WorkBuddy Gate不得与尚未完成的安装、Core切换或全局Skill变更并行。
