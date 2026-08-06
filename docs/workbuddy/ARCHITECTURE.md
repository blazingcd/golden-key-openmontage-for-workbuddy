# Golden Key OpenMontage for WorkBuddy：架构边界

状态：`v0.3.21 BASELINE FROZEN / W2 MCP=OPTIONAL`

更新日期：2026-08-06

## 1. 产品目标

本项目交付一个可安装、可验证、适合开源发布的 WorkBuddy 发行版：

```text
Golden Key WorkBuddy Callable Core
+ WorkBuddy Skill
+ 本地确定性执行入口
+ 通过真实WorkBuddy决策Gate后可选的stdio MCP
+ Windows 安装、配置、用户提示和故障恢复
```

最终用户只需要本公开项目，不需要访问 private 的 Golden Key Core 仓库，也不需要安装 Golden Key SaaS。

## 2. 两层核心边界

### 2.1 WorkBuddy 可调用层

WorkBuddy 本身就是唯一 Agent，直接：

- 读取 `AGENT_GUIDE.md` 并执行 Rule Zero；
- 选择四条 Golden Key 业务 Pipeline；
- 读取阶段 Skill 和 Layer 3 Skill；
- 通过 Tool Registry 调用当前 Stage 允许的工具；
- 生成并校验 Artifact；
- 执行 Reviewer 与 Checkpoint 协议。

该层由不可变 Release `golden-key-v0.3.21` 的 WorkBuddy 专用导出包提供，合同 ID 为
`golden-key-workbuddy-callable-core-v1`。

### 2.2 非 WorkBuddy 调用层

以下内容留在 Golden Key 私有源仓库，不进入本项目：

- SaaS Agent Host 和模型兼容传输；
- `lib/agent_host_authority.py`、`lib/model_driven_agent_host.py`、
  `lib/openai_compatible_transport.py` 及其合同测试；
- 私有客户证据；
- Core Release 导出维护工具；
- Golden Key SaaS 或其他消费方自有集成文件。

本项目不得调用、复制或重新实现上述运行时能力。

### 2.3 W1～W4消费方修改边界

W1～W4只修改WorkBuddy自有包、Skill、配置、测试、安装和文档。当前v0.3.21 managed Core快照只读：

- 可以读取、调用、回归和打包其Pipeline、Skill、Schema、Checkpoint与Tool Registry；
- 不在WorkBuddy仓库直接修补其业务逻辑或managed文件；
- 若Core大改影响导出合同，先由私有Core形成新Release/ZIP/SHA/lock，再执行独立同步、回归和公开Gate。

## 3. 仓库与同步边界

### 官方 OpenMontage

- `calesthio/OpenMontage` 只作为 Golden Key Core 维护方的 reviewed upstream baseline。
- WorkBuddy 项目不得直接同步、merge 或 cherry-pick 官方更新。

### Golden Key Core

- 私有仓库是 Core 的开发源，但其 `main`、工作树和 Git ancestry 都不是 WorkBuddy 同步输入。
- WorkBuddy 唯一允许的同步源是正式 Release 的 ZIP、SHA sidecar 和 lock。
- 当前锁定 Release：`golden-key-v0.3.21`，source commit
  `757ea3822e5f2eef7f341389983119021e827c8d`。

### Golden Key SaaS

- 与本项目没有产品或运行时依赖关系。
- 不复制或调用 SaaS BFF、Core Invocation、Agent Worker、Job/Outbox、多租户、预算或 Provider 管理代码。
- 当前同步和 W0 不读取、修改或追随 SaaS 仓库。

## 4. 运行时链路

```text
用户
  -> WorkBuddy Agent
     -> AGENT_GUIDE / Rule Zero
     -> Golden Key Pipeline Manifest
     -> Stage Skill / Reviewer / Checkpoint
     -> WorkBuddy Skill
     -> 本地确定性CLI（权威回退）
        -> 可选本地stdio MCP（同一消费方函数的结构化工具层）
     -> 本地 WorkBuddy Callable Core
        -> Schema / Artifact / Tool Registry / 媒体工具
```

权威运行时声明：

```text
authority.invocation_model = direct_agent
authority.nested_agent_host_allowed = false
```

真实WorkBuddy 5.3.8对照Gate已经通过并裁决`MCP=optional`。Skill、CLI与Callable Core是产品必选层；
MCP不是远端服务或第二个Agent，只是调用同一消费方函数的本地结构化工具层。它带来17个Schema工具、
语义发现和免Shell参数拼接，但增加用户级配置、stdio进程和首次信任成本。W4打包前不发布活动
`.workbuddy/mcp.json`；CLI始终可独立工作。

无论使用哪个入口，任何Adapter/MCP都不得拥有第二套 Pipeline 选择器、Director、Reviewer、Checkpoint
协议或模型规划循环。WorkBuddy始终是唯一Agent。

W1已建立环境命令，W2在同一消费方CLI上建立直接调用命令：

```text
golden-key-workbuddy doctor
golden-key-workbuddy gate
golden-key-workbuddy context / pipelines
golden-key-workbuddy config inspect / template
golden-key-workbuddy project / stage / artifact / checkpoint
golden-key-workbuddy tool list / execute
golden-key-workbuddy task submit / status / run / cancel / recover
```

模型配置严格分层：WorkBuddy主对话模型属于WorkBuddy Host，本Adapter不定义兼容端点、不读取该模型的凭据，
也不启动嵌套模型Agent；生产Provider属于Golden Key Tool Registry。`config inspect`只核验Registry类合同，
不调用`get_status()`、Provider或网络，并把DashScope、豆包、火山即梦、可灵官方的厂商直连与当前通过
fal.ai/Replicate接入的Seedance、MiniMax第三方网关明确分开。`config template`只在D盘消费方目录写入
环境变量名称引用，不包含密钥值，且拒绝覆盖用户修改后的文件。

`tool list`只解析项目已绑定Pipeline的当前Stage，并按Manifest原顺序返回允许工具、输入Schema和Layer 3 Skill；
不选择Pipeline或Provider。`tool execute`要求请求JSON位于项目`artifacts/`内、所有Schema声明路径位于项目目录、
所有Layer 3 Skill已显式确认，并且工具为本地、零网络、估算零成本。API、Hybrid、声明需网络或估算有成本的工具
在状态探测和`execute()`前拒绝。首条真实本地纵向验证使用`scene_detect`，socket封锁下Provider调用为0。

长任务入口在同一确定性CLI中持久化到`D:/WorkBuddyData/Jobs/<project-id>`。`task submit`完成Stage、Registry、
Skill、Schema、路径、成本与输入hash校验后只排队；稳定task ID使重复提交幂等。`task run`是可由WorkBuddy放入
后台进程的前台执行命令，执行前再次校验输入hash，并把结果原子写回。成功或终态任务不会重复执行。当前Core
Tool合同没有通用协作式取消，因此`task cancel`只允许queued任务；running任务明确返回不可安全取消，不能伪称
已取消或粗暴杀进程。进程中断后`task status`要求`task recover`，后者只把任务标记为failed，不自动重试，
避免未知的局部文件副作用被重复执行。声明为本地的Tool在执行期间受进程内socket-denial边界保护。

它们只做本地环境、锁定Core身份、四Pipeline、Skill和隔离边界检查，Provider调用数必须为0。
默认D盘目录和缓存规则见`docs/workbuddy/LOCAL-STORAGE-POLICY.md`。

## 5. 发布与 Git lineage

公开候选必须以公开 `origin/main` 为祖先，通过验证后的 Release 导出包建立核心快照，再叠加
WorkBuddy 自有 README、配置、同步脚本、Adapter/MCP、打包、状态和文档。Golden Key private
source commit 只作为 Release provenance 记录，绝不能成为公开目标提交的 Git 祖先。

```text
public origin/main
  -> verified v0.3.21 WorkBuddy callable-core snapshot
     -> WorkBuddy-owned increments
        -> Pre-Alpha publication candidate
```

旧 `golden-key-v0.3.18` 整仓 ancestry 方案只保留在本地 `legacy/` 分支和历史审计记录中，不是当前同步或发布基线。

## 6. 明确不做

- 不接入或修改 Golden Key SaaS。
- 不直接同步官方 OpenMontage。
- 不 merge/cherry-pick Golden Key private `main` 或历史。
- 不把非 WorkBuddy 调用层重新带回公开候选。
- 不在真实WorkBuddy对比前把MCP写成必选依赖或发布活动MCP配置。
- 不开发新的 Web UI；Backlot 仅作为原生、可选观察界面。
- 不在离线阶段调用真实或付费 Provider。
- 不用 mock 结果声明 WorkBuddy 或真实成片已通过。
