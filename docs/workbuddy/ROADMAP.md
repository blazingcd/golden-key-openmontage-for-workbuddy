# W0-W4 任务路径与执行步骤

状态：`ACTIVE PLAN`

更新日期：2026-08-06

## 总体路径

```text
W0 v0.3.21导出合同、公开性、架构和接口审计
 -> W1 Callable Core同步门禁和安装骨架
 -> W2 Skill-first直接调用闭环与MCP决策Gate
 -> W3 离线可靠性、安全和回归
 -> W4 安装交付、用户提示和真实WorkBuddy验收
```

每个阶段完成时必须同时更新 `PROJECT-STATE.md` 和追加 `WORK-LOG.md`，附提交、测试和证据路径。

## W0：v0.3.21导出合同、公开性与产品接口审计

### 任务

- 核对v0.3.21 Release、ZIP外部SHA、内外lock、source commit和公开`origin/main`。
- 验证1566个managed-scope文件、required/forbidden/consumer-remove合同和幂等同步。
- 只审计“Release导出包+WorkBuddy自有增量”的公开候选，不扫描或发布Golden Key私有历史。
- 检查密钥、客户数据、私有路径、素材/字体/品牌和第三方许可证。
- 形成官方OpenMontage、参考MCP与本项目的实现对照。
- 冻结 WorkBuddy用户旅程、提示状态和Skill/MCP职责。
- 映射当前核心的Guide、Manifest、Skill、Schema、Checkpoint和Tool Registry接口。
- 验证`direct_agent`运行时不包含或调用SaaS Agent Host/模型兼容传输。
- 检查Python包名、MCP Server名和WorkBuddy Skill名冲突。

### 完成证据

- v0.3.21公开审计报告、Release合同证据和候选文件清单。
- 架构边界和同步策略文档。
- MCP候选工具合同。
- 运行时隔离测试方案。
- 明确结论：`PASS`、`CONDITIONAL PASS`或`FAIL`。

### Gate

新W0对v0.3.21导出候选得到`PASS`，用户随后明确授权，首个`Pre-Alpha`公开基线已经发布。
旧v0.3.18整仓方案的`FAIL`保留为历史记录，但不再阻断当前基线。后续增量持续提交和推送；
公开性风险、Core漂移或测试失败会恢复fail-closed。

## W1：Callable Core同步门禁与安装骨架

状态：`DONE`。维护者Release同步幂等门禁、公开快照CI、独立WorkBuddy Python发行身份、`doctor`/`gate`、Skill、
`.workbuddy`骨架和D盘存储策略已经建立。完整生产调用闭环和安装发行分别属于W2与W4。

### 任务

- 维护v0.3.21 Release资产和lock身份，不维护活动`core-sync`分支。
- 维持`config/openmontage.sync.json`和`scripts/core_sync/sync_workbuddy_core.py`的fail-closed校验。
- 将下载、外部SHA、lock、managed mirror、消费方所有权和幂等测试纳入常规门禁。
- 保证公开`main`只继承公开`origin/main`，不继承private Core ancestry。
- 建立 WorkBuddy Python包、Skill目录、测试目录和示例配置目录。
- 规定D盘项目、缓存、模型和临时文件位置。
- 建立环境 `doctor` 骨架，但不在本阶段冻结运行环境打包方案。
- 维护者环境执行`sync-release`幂等复核；公开CI不持有私有Core凭据，只执行W1 Gate和完整测试。
- W1不发布活动MCP配置；将MCP默认/可选/省略的裁决留给W2真实WorkBuddy对比。

### 完成证据

- Core ZIP、lock、managed scope或目标文件漂移会fail-closed。
- Release source commit、合同ID、authority和bundle digest一致。
- 全新D盘目录可以建立开发环境。
- 不复制SaaS/Agent Host/私有证据/导出维护代码。
- `doctor`报告Core身份、四Pipeline、运行时和D盘目录；`gate`拒绝禁入文件/导入和提前启用MCP。

## W2：Skill-first体验、最小调用面和MCP决策Gate

状态：`IN PROGRESS`。直接调用基线已经完成权威上下文、Pipeline目录、项目生命周期、当前Stage合同、
Artifact/Checkpoint、Manifest限定的Tool发现和首个纯本地Tool执行。API/Hybrid在网络前fail-closed；
主对话模型/生产Provider配置分层、安全引用模板，以及本地Tool持久任务、幂等、排队取消、明确运行中
不可取消和中断恢复语义已经完成；真实WorkBuddy CLI/MCP对照已通过并裁决`MCP=optional`。跨任务单执行槽、
可观测超时和中断后槽释放已经完成；完整Provider授权执行仍需用户单独授权，当前可转入W3离线矩阵。

### 任务

- 编写可导入的 WorkBuddy Skill。
- 复用原生 onboarding，提供中文、按真实能力生成的用户提示和示例Prompt。
- 支持模糊需求、具体目标、参考视频、源素材和继续项目五类入口。
- 实现环境/版本检查、权威上下文读取、项目创建/打开和状态查询。
- 实现Schema校验和受限Stage提交。
- 实现当前Manifest/Stage允许范围内的确定性工具执行。首个本地纵向切片和持久长任务协议已完成；
  后续仅在单独授权下补Provider路径。
- 不包含、调用或重新实现`model_driven_agent_host.py`、`openai_compatible_transport.py`或`agent_host_authority.py`。
- `DONE`：已在真实WorkBuddy 5.3.8中比较`Skill+本地CLI`与`Skill+本地stdio MCP`的安装、Schema发现、
  任务失败语义和权限成本，裁决`MCP=optional`；证据见`W2-MCP-DECISION-2026-08-06.md`。
- 已将WorkBuddy主对话模型配置与视频生产Provider配置分层；国内生态生产模型只报告Registry已注册工具，
  并区分厂商直连和第三方网关。WorkBuddy主模型的具体兼容端点仍以WorkBuddy真实支持面为准，不由Adapter伪造。

### 完成证据

- WorkBuddy能够按Rule Zero选择Pipeline，任何执行适配层都不预选。
- 可选MCP握手、17个工具发现、参数Schema、正常调用和一次失败不重试已通过；CLI等价基线保留。
- 提示明确展示当前状态、选择、推荐、成本/风险和下一步。

## W3：离线可靠性、安全和回归

### 任务

- 将长任务状态持久化到D盘工作区。（W2直接CLI基线已完成）
- 验证所选执行入口重启后的任务和项目恢复。（W2已完成中断识别与fail-closed恢复；真实WorkBuddy待W4）
- 实现并验证真实取消或明确不可取消语义。（W2已完成queued取消/running明确不可取消）
- 并发限制、幂等、重复执行保护和超时处理。（W2已完成数据根级并发1、稳定ID、终态重放、可观测超时和中断槽释放；硬终止因Core无安全取消合同而明确禁止）
- 路径规范化和根目录封闭。（`DONE`：项目、Artifact、Tool输入/输出和Checkpoint路径负测持续通过）
- 密钥、异常和日志脱敏。（`DONE`：CLI、MCP、ToolResult和任务JSON统一脱敏）
- 无凭证、缺Artifact、Gate违规和Schema错误负测。（`DONE`）
- 静态依赖检查和运行时网络拦截，证明没有第二个Agent模型调用。（`DONE`：当前Python进程及Python/Node子进程继承门禁，SaaS仓库不可用负测通过）
- 运行核心合同回归和Adapter专项回归。（`DONE`）

### 完成证据

- 离线测试报告：`W3-OFFLINE-RELIABILITY-REPORT-2026-08-06.md`。
- `76 passed` WorkBuddy专项和`1136 passed, 10 skipped, 1 subtest passed`完整回归。
- 失败路径均为结构化、可操作且不泄漏凭据的提示；CLI与可选MCP语义一致。
- mock只作为拒绝路径夹具，不作为真实Provider或普通用户可用结论；`OFFLINE ADAPTER READY`仍等待W4。

## W4：打包、安装、文档和真实WorkBuddy验收

### 任务

- 决策并实现Python、Node、FFmpeg等运行环境交付方式。
- Windows优先安装、升级和卸载。
- 按`MCP=optional`裁决生成可选的WorkBuddy用户级配置、信任提示和禁用/卸载路径；不覆盖用户已有MCP配置。
- 打包可导入Skill和完整Golden Key核心。
- 中文快速开始、Prompt Gallery和故障排查。
- 在未预装开发环境的普通Windows用户场景验证安装。
- 在真实WorkBuddy中验证所选执行入口、能力发现、自然语言触发、审批暂停、长任务、取消和恢复。

### 完成证据

- 全新D盘目录按文档安装成功。
- 用户不需要另外下载Golden Key核心。
- 真实WorkBuddy验收通过后才声明`OFFLINE ADAPTER READY`。
- Provider真实成片仍为单独授权阶段。

## 发布节奏

- 首次公开基线是 W0 后的独立 Gate，不是 W4 之后的集中发布阶段。
- W0 明确 `PASS` 后，先报告 Gate、风险、待发布文件、测试证据和目标提交，并等待用户再次明确授权。
- 获得授权后立即发布完整v0.3.21 WorkBuddy Callable Core导出、四个业务Pipeline及合同面、
  安全可公开的WorkBuddy增量和治理文档；发布状态标记为`Pre-Alpha`或“WorkBuddy Adapter开发中”。
- 首次基线发布后，W1～W4 持续开发、持续留痕、持续提交和持续推送，不积压到 W4。
- W4 的真实安装和 WorkBuddy 验收仍是声明 `OFFLINE ADAPTER READY` 的必要条件。
- 未经单次授权不调用真实或付费 Provider。
- 权威细则见 `docs/workbuddy/FIRST-PUBLIC-PUSH-POLICY.md`。
