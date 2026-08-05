# Golden Key OpenMontage for WorkBuddy：下一对话启动 Prompt

> **历史启动文件。** 当前权威交接是`NEXT-CONVERSATION-PROMPT-2026-08-05-W1.md`；如有冲突，
> 以v0.3.21 Release导出合同、`PROJECT-STATE.md`和`docs/workbuddy/`最新冻结文档为准。

请在目录 `<WORKBUDDY_REPO_ROOT>` 开始一个全新的独立项目。

## 你的任务

为腾讯 WorkBuddy 开发一个可安装、可验证、适合开源发布的 Golden Key OpenMontage 调用项目。
WorkBuddy 本身就是负责理解用户目标、规划和多步执行的 Agent Host；本项目只向 WorkBuddy 提供
OpenMontage 的确定性工具能力、原生项目工作区和必要的操作说明，不再嵌套另一套 Agent Worker。

当前对话和仓库必须与 Golden Key SaaS 主项目隔离。SaaS 仓库只能只读用于核对 OpenMontage
版本锁，不能把 SaaS BFF、Core Invocation、Agent Worker、预算/Outbox或产品合同复制进本项目。

## 已冻结的项目名称与公开定位

- 正式展示名：`Golden Key OpenMontage for WorkBuddy`
- GitHub仓库名：`golden-key-openmontage-for-workbuddy`
- 本地目录：`<WORKBUDDY_REPO_ROOT>`
- 中文一句话：`面向腾讯 WorkBuddy 的 Golden Key 版 OpenMontage 社区分支。`
- 英文一句话：`An unofficial community fork of OpenMontage, based on the Golden Key edition and adapted for WorkBuddy.`

正式名称不用难以识别的`GK`缩写，也不使用可能被误解为官方产品的`OpenMontage for WorkBuddy`
单独命名。README、GitHub About、包元数据和发布说明必须使用`Golden Key OpenMontage for WorkBuddy`
全称，并明确：这是独立维护的非官方社区分支，继承OpenMontage，不代表OpenMontage上游或WorkBuddy
官方背书。代码包名可在不冲突时使用`golden_key_openmontage_workbuddy`，但必须在W0检查Python/MCP
命名冲突后再冻结。

## 已确认的本机基线

- 新项目目录：`<WORKBUDDY_REPO_ROOT>`
- SaaS仓库：`<GOLDEN_KEY_SAAS_REPO_ROOT>`
- SaaS版本锁：`<GOLDEN_KEY_SAAS_REPO_ROOT>\config\openmontage.lock.json`
- 金钥匙OpenMontage本地仓库：`<GOLDEN_KEY_CORE_REPO_ROOT>`
- 金钥匙OpenMontage远端：`https://github.com/blazingcd/golden-key-openmontage.git`
- 官方上游：`https://github.com/calesthio/OpenMontage.git`
- 当前锁定发布：`golden-key-v0.3.17`
- 当前锁定提交：`09177a2e9512ac9a4062f9d7f1e314660273aff8`
- 当前金钥匙远端是private、非GitHub fork；本地仓库保留`upstream`远端并继承官方历史。
- 官方OpenMontage许可证：GNU AGPL-3.0。
- 重点参考：`https://github.com/noah-1106/openmontage-zh-mcp`
- WorkBuddy官方说明：
  - `https://www.workbuddy.cn/docs/workbuddy/Overview`
  - `https://www.workbuddy.ai/docs/zh/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/MCP-Guide`

这些值是2026-08-05的已核对快照。开始工作时必须重新读取真实文件和Git状态，不得把快照当作
永远不变的事实。

## 不可漂移的架构边界

正确链路是：

```text
用户
  -> WorkBuddy Agent（理解、规划、决策、与用户交互）
  -> WorkBuddy Skill 和/或 MCP stdio工具
  -> 金钥匙版OpenMontage原生能力、工作区与工具
  -> OpenMontage原生Manifest / Skill / Schema / Review / Checkpoint / Artifact
```

禁止变成：

```text
WorkBuddy -> SaaS Core Invocation -> SaaS Agent Worker -> OpenMontage
```

也禁止在本项目中创建第二套Director、创意状态机、Pipeline选择器、Reviewer、Checkpoint协议、
模型规划循环或SaaS任务生命周期。WorkBuddy必须按照OpenMontage自己的`AGENT_GUIDE.md`、Rule Zero、
Pipeline Manifest、Stage Skill、Schema、Review和Checkpoint规则工作。

## 版本同步规则

“与SaaS保持同一核心版本”不等于要求两个仓库的最终HEAD相同。WorkBuddy适配提交会让公开仓库
HEAD继续前进，但每个适配器版本必须明确记录并验证以下三层身份：

1. `upstream_base_commit`：对应官方OpenMontage基线；
2. `golden_key_core_commit`：必须与SaaS `config/openmontage.lock.json`中的`commit`完全一致；
3. `adapter_release_commit`：本项目在该核心基线之上的WorkBuddy适配提交。

增加一个机器可读同步清单，例如`config/openmontage.sync.json`，并提供fail-closed校验命令。若
SaaS锁升级，顺序必须是：核心变更先进入金钥匙OpenMontage并发布新tag -> SaaS更新lock并通过门禁
-> 本项目同步完全相同的核心commit -> 运行OpenMontage合同回归和WorkBuddy适配回归 -> 再发布
新的适配器版本。不得只手工改版本字符串，也不得在本项目先改OpenMontage核心后反向追赶SaaS。

## 已确认的目标仓库形态与发布前审计

产品目标已确定为：审计通过后，建立`calesthio/OpenMontage`的公开GitHub fork，并在该fork中
同步Golden Key核心修改和增加WorkBuddy适配。公开fork是默认交付形态，不再把独立Adapter仓库
作为并列首选。

### 默认方案：官方OpenMontage的公开fork

- 从`calesthio/OpenMontage`建立公开fork；
- 保留官方Git历史、AGPL-3.0、原作者版权和归属说明；
- 在fork中同步金钥匙OpenMontage的同一核心commit，再增加WorkBuddy Skill/MCP；
- 若能保持原始commit对象和父链，优先保持`golden_key_core_commit`原SHA不变；
- 适合用户一次clone后直接使用，也最接近`openmontage-zh-mcp`的交付形态。

### 仅在公开审计失败时保留的回退方案

- 只保存WorkBuddy Skill/MCP和同步清单；
- 通过明确依赖、submodule或安装流程取得金钥匙OpenMontage；
- 只有当普通公开用户能合法、无需访问private仓库地取得锁定核心时才成立；
- 如果核心仍是private，不能把该方案描述为可独立使用的public开源项目。

回退为独立Adapter必须先报告公开fork的具体阻断证据并取得产品负责人重新授权，不能由开发者
自行改变已经冻结的公开fork方向。

在推荐公开fork前，必须审计金钥匙OpenMontage相对官方上游的全部差异：密钥、真实客户数据、
私有路径、供应商凭证、不可公开素材、SaaS专有代码、第三方资产许可证、品牌和版权声明。AGPL
兼容只是基础条件，不等于所有内容都天然适合公开。若复用参考项目的代码而非只参考设计，必须
检查其提交来源、许可证和归属，并保留相应notice。

除非产品负责人明确授权，不得在GitHub创建仓库、改变可见性或push公开内容。第一阶段只完成
本地审计、方案结论和实施计划。

## 参考项目的正确用法

重点研究`noah-1106/openmontage-zh-mcp`的：

- MCP stdio启动和安装方式；
- 少量业务级工具而不是平铺全部Provider工具；
- 长任务异步化、`job_id`、状态查询与取消；
- 结构化错误码、路径解析、并发边界和离线smoke；
- 中文文档与配置体验。

不要机械复制它的9个工具。必须先映射当前锁定的金钥匙OpenMontage真实接口，并检查
`run_tool`、`write_checkpoint`等入口是否会绕过OpenMontage原生Agent Guide、Review或Checkpoint
约束。工具面应保持最小、确定性和可测试；创意与编排仍由WorkBuddy按照OpenMontage规则完成。

## 开发阶段和小时预算

先重新整理计划并告诉产品负责人，然后分阶段执行，每阶段独立回归：

1. `W0 仓库与公开性审计`，目标0.75小时：核对三个仓库、版本祖先、许可证、private/public、
   金钥匙diff和参考项目；输出公开fork的可发布性结论、风险和精确实施边界。完成后暂停远端
   操作，但本地可继续开发已确认的可逆部分。
2. `W1 本地项目基线与同步门禁`，目标1小时：建立最小目录、许可证/NOTICE、机器可读同步清单、
   版本校验和D盘工作区规则；不得复制SaaS代码。
3. `W2 WorkBuddy最小调用面`，目标2小时：根据WorkBuddy官方Skill/MCP格式和当前OpenMontage真实
   接口实现最小stdio MCP/Skill；不含第二Agent Worker，不含UI。
4. `W3 离线开发与调试`，目标1.5小时：合同测试、MCP smoke、版本漂移、路径越界、错误脱敏、
   异步状态/取消、重启后项目状态和无凭证失败路径。
5. `W4 安装与开源交付文档`，目标1小时：Windows优先的安装/配置/卸载、WorkBuddy接入示例、
   中英文README最小集、贡献和同步流程。

离线目标总计6.25小时，工程红线9小时。到红线仍未完成时必须报告根因和剩余项，不得删门禁、
放宽Schema或用mock冒充可用。真实模型/生图/生视频/TTS/成片验收是后续独立阶段，预计1.5～3小时，
必须先列出Provider、凭证、单次预算、素材权限和停止条件并取得逐次授权，不能自动消耗Token。

## 最小实现候选面

在读完真实接口后再冻结名称，候选能力仅包括：

- 环境与版本检查；
- 创建/打开OpenMontage项目工作区；
- 查询原生Pipeline能力与当前项目状态；
- 调用确定性的OpenMontage工具；
- 查询/取消长任务；
- 返回需要WorkBuddy继续读取的原生Artifact、Review或Checkpoint位置和下一步事实。

不得把SaaS六命令直接搬过来，也不得让MCP伪造审批、直接写“已通过”Checkpoint或代替
OpenMontage作创意判断。所有路径必须限制在D盘配置的项目根目录内；秘密只从环境或用户本机
配置读取，不进入日志、测试fixture、Git或机器可读错误。

## 验收标准

离线阶段只有同时满足以下条件才可声明`OFFLINE ADAPTER READY`：

- 能从全新D盘目录按文档安装并被WorkBuddy识别；
- MCP握手、工具发现、参数Schema和结构化错误通过；
- 锁定核心commit与SaaS lock一致，漂移时fail-closed；
- WorkBuddy是唯一上层Agent，代码中不存在另一个模型规划循环或SaaS Agent Worker依赖；
- 原生OpenMontage Guide/Manifest/Skill/Review/Checkpoint/Artifact仍是唯一制作真相；
- 长任务不会因stdio超时伪失败，状态查询和取消可验证；
- 路径越界、密钥泄漏、重复执行和无凭证路径有负测；
- OpenMontage原合同测试与Adapter专项测试均取得新鲜证据；
- README明确区分“离线适配通过”和“真实Provider端到端成片通过”。

只有用WorkBuddy实际提出自然语言视频目标、走完必要澄清/审批、执行锁定金钥匙OpenMontage并
产出可播放成片及原生证据链后，才可声明`WORKBUDDY E2E READY`。

## 明确不做

- 不修改Golden Key SaaS仓库的业务代码或文档；
- 不接入SaaS BFF/Core Invocation/Agent Worker；
- 不开发Web UI、账户、支付、点数、多租户、云队列或数据库；
- 不新增另一套Director、Workflow、Reviewer或Checkpoint；
- 不为了兼容所有Agent平台过度抽象，首个正式宿主只验收WorkBuddy；
- 不自动创建/公开GitHub仓库，不自动调用付费模型或Provider；
- 不把参考项目的README、工具数量或测试结论当作本项目证据。

## 开始方式

现在先执行W0：

1. 检查新目录是否为空以及Git状态；
2. 读取SaaS真实lock、金钥匙OpenMontage的Git/许可证/差异和官方上游祖先；
3. 检查WorkBuddy官方MCP/Skill规则及参考项目的实现结构；
4. 用小时重新整理W0～W4计划，确认公开fork是否通过发布审计；若不通过，列出明确阻断证据；
5. 把结论和计划写入本项目文档；
6. 在未创建远端、未公开仓库、未调用Provider的前提下继续完成可逆的本地工作。

全程以证据区分：`已实现`、`离线测试通过`、`WorkBuddy本机验收通过`、`真实Provider成片通过`、
`已公开发布`，不得混写。
