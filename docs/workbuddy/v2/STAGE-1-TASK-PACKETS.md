# WorkBuddy Shell V2 阶段1任务包

状态：`READY_NOT_STARTED / AUTHORIZED_FOR_NEXT_SESSION_AFTER_TAKEOVER_GATES`

更新时间：2026-08-15

## 1. 用途

本文件把阶段1拆解成可直接派发、可停止、可审阅的任务包。新统筹会话不得重新设计阶段1，不得从聊天记录猜任务，也不得把阶段1扩大为生产代码实现。

阶段1只冻结：

- WorkBuddy、OpenMontage Core、Shell的职责；
- 目标架构和控制权边界；
- 旧消费层模块的处置结论；
- 后续阶段的验收与证据口径。

阶段1不修改生产代码，不运行测试、安装、WorkBuddy、Provider或媒体生成。

## 2. 不可变原则

```text
WorkBuddy = 唯一对话Agent
OpenMontage Core = 唯一生产决策与执行权威
Shell = 安装 + Core对象锁定 + 运行环境绑定 + 会话入口 + 状态/结果转交
```

Shell不得：

- 选择Pipeline、Stage、Provider、模型、媒体方案或创意方向；
- 创建OpenMontage Artifact或推进Checkpoint；
- 实现第二套Director、FSM、Supervisor、Agent Host或生产任务状态机；
- 解析Pipeline业务语义来代替Core；
- 把CLI、MCP、Jobs或Runtime包装成新的生产控制面；
- 把技术路由、Codex控制词或执行器参数写入用户消息。

发现任何任务需要上述能力时，停止为`STOPPED_SCOPE_EXPANSION`，不得“先实现再解释”。

## 3. 推荐派发结构

为避免上下文继续碎片化，阶段1只使用以下执行链：

1. `V2-S1-TAKEOVER`：新统筹核验并锁定交接对象；
2. `V2-S1-BUILDER1`：一个有界文档Builder串行完成T1至T5；
3. `V2-S1-T6`：一个独立只读Reviewer审阅Builder精确提交；
4. `V2-S1-GATE`：统筹汇总后由用户决定是否接受阶段1。

不要为T1至T5分别创建五个会话。它们修改同一组相互依赖的治理文档，拆成五个会话会增加合并、状态和基线漂移风险。Builder必须在最终报告中分别给出T1至T5的完成证据，不能用“一次提交”掩盖子任务缺失。

## 4. V2-S1-TAKEOVER：新统筹接管

### 目标

确认新会话位于正确项目、正确分支和用户Prompt给出的精确40位handoff commit，并直接派发阶段1 Builder。

### 只读步骤

1. 完整读取根`AGENTS.md`和`AGENT_GUIDE.md`；本任务是治理统筹，不触发视频生产Pipeline；
2. 读取`docs/workbuddy/v2/NEXT-SESSION-HANDOFF.md`及其规定的权威文档；
3. 核验项目路径为`D:\BlazingCD\Personal\Golden_Key_OpenMontage_for_WorkBuddy-shell-v2`；
4. 核验分支为`codex/workbuddy-shell-v2`；
5. 核验本地HEAD、远端分支和Prompt中的`EXPECTED_HANDOFF_COMMIT`三者一致；
6. 核验工作树clean，`immutable_code_baseline=2a2bf09832d558388dc2816c54b32a2dce4aa607`仍是祖先；
7. 核验`governance_review_gate=PASS_ACCEPTED`、`stage_1=READY_NOT_STARTED`；
8. 从该精确handoff commit创建`V2-S1-BUILDER1`独立任务，任务分支建议为`codex/v2-s1-builder1`。

### 停止条件

任一对象、路径、分支、远端、clean状态或治理状态不一致时，返回`INCOMPLETE_CONTEXT_MISMATCH`。不得改用任意HEAD、旧项目或旧长期分支。

### 完成定义

- Builder任务已经创建并开始；
- Builder Prompt明确记录`stage_1_builder_start_commit=<EXPECTED_HANDOFF_COMMIT>`；
- 本统筹会话不亲自执行T1至T5。

## 5. V2-S1-T1：建立阶段1活动入口和权威关系

### 目标

让Builder结果分支中的当前状态、权威顺序和阶段1起点无歧义。

### 允许写路径

```text
docs/workbuddy/v2/README.md
docs/workbuddy/v2/TASK-REGISTER.md
docs/workbuddy/v2/STAGE-1-EXECUTION-PLAN.md
```

### 执行步骤

1. 记录`stage_1_builder_start_commit`为统筹Prompt给出的精确40位对象；
2. 将Builder自身状态从`READY_NOT_STARTED`推进为`IN_PROGRESS`；
3. 保持治理Gate历史结论不变；
4. 冻结本阶段权威顺序、允许路径、禁止路径和停止规则；
5. 确认阶段2至8仍受`V2-S1 PASS_ACCEPTED`阻断。

### 不得做

- 不把阶段1标成`PASS_ACCEPTED`；
- 不创建生产代码或测试；
- 不改写旧历史为当前授权；
- 不重新审阅已接受的前置治理Gate。

### 完成证据

- 三份文档状态一致；
- 精确start commit、Builder任务ID和任务分支可追溯；
- T2可按账本进入同一Builder的下一步。

## 6. V2-S1-T2：冻结职责和目标架构

### 目标

把V2职责、控制权、信任边界和最小数据流冻结为阶段1架构决策。

### 允许写路径

```text
docs/workbuddy/v2/PROJECT-CHARTER.md
```

### 执行步骤

1. 核验WorkBuddy、Core、Shell、Launcher、Installer、Runtime、Tool/Provider的唯一职责；
2. 明确会话入口只建立绑定和转交，不选择生产方案；
3. 明确Shell只消费Core公开合同，不导入Core业务内部实现；
4. 明确`user_message`与`executor_controls`隔离；
5. 明确所有生产状态、Artifact、Checkpoint和决策归Core；
6. 明确首版非目标及后续范围变更程序。

### 硬门禁

- Shell没有第二套Director/FSM；
- Launcher没有任意Shell、Agent或业务编排能力；
- WorkBuddy不是生产执行器；
- Core不是由Shell重新实现的库函数集合。

### 完成证据

`PROJECT-CHARTER.md`可让后续Builder对任何候选模块回答“归谁负责、为什么、Shell是否允许拥有”。

## 7. V2-S1-T3：建立逐模块处置矩阵

### 目标

创建`MODULE-DISPOSITION.md`，逐项裁决旧消费层能力是否进入V2，禁止整模块迁移。

### 允许写路径

```text
docs/workbuddy/v2/MODULE-DISPOSITION.md
```

### 只读输入

- `STAGE-1-EXECUTION-PLAN.md`列出的固定输入和消费层路径；
- `immutable_code_baseline`上的旧实现；
- 两个现有WorkBuddy Skill；
- 已列出的七个历史证据任务，仅在确有必要时核验最终结论；
- 官方Core固定对象，只用于职责和公开合同事实。

### 每项必须记录

```text
current_path
current_consumer
real_problem_solved
v2_verdict
minimum_reusable_capability
forbidden_logic
target_stage
required_consumer_evidence
required_tests
```

### 允许结论

```text
KEEP
ADAPT
REWRITE
REMOVE_FROM_V1
HISTORICAL_ONLY
UNKNOWN
```

### 必须覆盖

- doctor、runtime、runtime_prepare、tasks、cli、mcp_server、paths、security；
- 两个WorkBuddy Skill；
- installer、package、manifest、credentials、upgrade、rollback、uninstall；
- Core同步、测试和审计资产。

### 硬门禁

- 没有消费者/调用链证据不得判`KEEP`；
- 测试通过不等于模块必要；
- 任何Director、Stage FSM、Pipeline选择、Artifact/Checkpoint推进逻辑必须判为禁止迁移或由Core承担；
- 不修改被分析的实现文件。

## 8. V2-S1-T4：冻结验收矩阵和状态模型

### 目标

让后续阶段的PASS、FAIL、INCOMPLETE、NOT_TESTED和非证明项不可混淆。

### 允许写路径

```text
docs/workbuddy/v2/ACCEPTANCE-MATRIX.md
```

### 执行步骤

1. 对照章程和模块处置矩阵补齐Gate；
2. 区分静态合同、安装对象、真实WorkBuddy、Core流程、本地成片、Provider和发布证据；
3. 明确Gate A至D及可选E的对象、动作、证据和零边界；
4. 保持Provider、费用、下载和真实运行独立授权；
5. 明确任何对象不一致、无最终退出或证据缺失均为`INCOMPLETE`。

### 硬门禁

- ZIP、doctor、registry、旧MP4或历史成功不得冒充V2最终PASS；
- Gate D默认Provider调用0、费用0；
- Gate E不是本地V2完成前置；
- 目标正式Skill必须保留，仅清理临时、测试、重复或旧版本残留。

## 9. V2-S1-T5：Builder收口

### 目标

同步阶段1文档、账本和工作日志，形成一个可独立审阅的精确提交。

### 允许写路径

```text
docs/workbuddy/v2/README.md
docs/workbuddy/v2/TASK-REGISTER.md
PROJECT-STATE.md
WORK-LOG.md
```

### 执行步骤

1. 核验T1至T4产物齐全且无跨文档冲突；
2. 将T1至T5分别记录为`REVIEW_READY`；
3. 将阶段1整体记录为`REVIEW_READY`，不得自判通过；
4. 记录精确baseline、结果commit、文件、静态校验、非证明项和零执行边界；
5. 创建一个只含允许文档的提交并推送`codex/v2-s1-builder1`；
6. 设置`next_authorized_task=V2-S1-T6`。

### Builder静态校验

- `git diff --check`；
- 相对start commit的变更路径全部属于T1至T5允许路径；
- 生产代码、Skill、安装器、测试、配置、lock、Core变化数均为0；
- 工作树clean；
- 本地和远端Builder分支指向同一结果提交。

## 10. V2-S1-T6：独立只读Reviewer

### 前置

Builder已返回`REVIEW_READY`并给出精确40位提交。

### 审阅范围

- 只审Builder相对`stage_1_builder_start_commit`的允许文档；
- 核验T1至T5逐项完成；
- 搜索Shell越权、第二Director/FSM、模糊依赖、范围扩大和证据冒充；
- 核验生产代码变化0和`git diff --check=0`。

### Reviewer限制

- 零修改、零commit、零push；
- 不运行测试、WorkBuddy、安装、Provider或媒体生成；
- 不自行修复；
- 结论只允许`APPROVE / REQUEST_CHANGES / INCOMPLETE`。

### 防止审阅失控

- 只报告会阻断阶段1可执行性的具体问题；
- 不把个人偏好的文档润色列为P1；
- 与Builder diff无关的历史问题记录为非阻断后续项，不扩大本Gate；
- 若需要修订，只开有界FIX任务并只复审该FIX的直接变化。

## 11. V2-S1-GATE：用户阶段1Gate

只有以下条件全部满足，统筹才可提交用户Gate：

- Builder结果提交已推送；
- Reviewer最终结论为`APPROVE`；
- 统筹复核对象、路径、状态和零边界；
- 阶段1没有生产代码变化；
- `MODULE-DISPOSITION.md`覆盖规定模块；
- 最高职责原则没有弱化。

用户接受后才可把`V2-S1`设为`PASS_ACCEPTED`。阶段2在此之前不得细化或启动。

## 12. 全阶段停止规则

出现任一情况立即停止：

- 当前HEAD、远端或任务Prompt对象不一致；
- 目标分支或项目不是Shell V2；
- Builder需要修改允许路径以外文件；
- 任务开始后证据缺失、无最终退出或环境干扰；
- 需要Shell承担任何生产决策或执行；
- 需要运行测试、安装、WorkBuddy、Provider或媒体生成；
- 需要merge/rebase `main`或旧长期分支；
- 发现用户未授权的范围变化。

停止时使用`INCOMPLETE`或`STOPPED_SCOPE_EXPANSION`，记录精确对象、缺口和零执行事实，不得自行扩大任务。
