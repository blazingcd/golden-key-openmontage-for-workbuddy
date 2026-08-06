# WorkBuddy 运行时隔离验证方案

状态：`v0.3.21 DIRECT-AGENT BASELINE / W3 OFFLINE ISOLATION MATRIX PASS`

日期：2026-08-06

## 1. 当前结论

当前仓库已经建立W1入口和W2直接调用/受限本地Tool入口，但尚未形成真实Provider生产闭环或
W4完整安装验收。v0.3.21导出合同、W1 Gate和W2离线专项/真实WorkBuddy入口对照已经证明：

- authority为`direct_agent`且`nested_agent_host_allowed=false`；
- 三个Agent Host/transport模块及三个对应合同测试不在导出包和当前工作树；
- 当前WorkBuddy自有代码不存在对它们或Golden Key SaaS Worker的导入；W1 Gate会对新增Python入口执行AST导入扫描；
- `doctor`/`gate`只执行本地确定性检查并显式报告Provider调用数为0；
- 当前Stage allowlist、项目路径、Layer 3 Skill确认和API/Hybrid前置拒绝已启用；本地`scene_detect`在socket
  封锁下执行成功，Tool调用1次、Provider调用0次、成本0；仍不能声明 `OFFLINE ADAPTER READY`。

W0/W1静态边界、W2纯本地Tool/持久任务纵向切片和W3离线隔离矩阵均为`PASS`。socket负测覆盖当前
Python进程的DNS/连接/数据报入口，并通过`sitecustomize`和`NODE_OPTIONS`覆盖受信Core Tool启动的
Python/Node子进程；真实loopback监听器确认连接从未建立。SaaS/private Core仓库路径指向不存在目录时，
仓库外进程仍能读取direct-agent上下文和创建离线项目。CLI、MCP、ToolResult和任务JSON中的环境密钥、
常见凭据文本及敏感字段均已脱敏。该结论是离线运行时Gate，不替代W4安装/普通用户验收或真实Provider授权Gate。

## 2. 静态依赖门禁

扫描 WorkBuddy 自有运行时路径：

```text
golden_key_openmontage_workbuddy/
workbuddy-skill/
.workbuddy/
scripts/workbuddy/
scripts/core_sync/
```

必须 fail-closed 拒绝：

- Python/Node import、动态 import 或进程启动指向 `lib/model_driven_agent_host.py`；
- Python/Node import、动态 import 或进程启动指向 `lib/openai_compatible_transport.py`；
- 对 `golden_key_short_video_agent`、SaaS Agent Worker、BFF、Core Invocation、Job/Outbox 或多租户模块的依赖；
- Adapter 自带 Pipeline 选择器、Director、Reviewer、模型规划循环或第二套 Checkpoint；
- 未经 Manifest/Stage 允许的 Tool Registry 调用；
- MCP 返回或持久化未通过原生 Schema 的伪 Artifact。

`scripts/workbuddy/w0_audit.py` 已提供AST/import和禁入文件扫描，结果写入
`docs/workbuddy/audits/evidence-v0.3.21-2026-08-05/runtime-isolation.json`。W2必须把相同规则移入常规CI。

## 3. 运行时网络拦截

W2建立单进程socket封锁，W3已把门禁继承到Python/Node子进程。MCP已裁决为`optional`，CLI与MCP应用同一门禁：

1. 清空所有 Provider 凭据，并设置测试专用环境变量表。
2. 在进程启动前拦截 `socket.create_connection`、DNS、`requests`、`httpx`、OpenAI SDK 和 Node `fetch/http/https`。
3. 只允许测试明确列出的本地进程/临时文件通信；保留MCP时可额外允许loopback/stdio协议通信。任何其他目标立即失败并记录调用栈、目标类别和发起模块，不记录凭据或完整请求体。
4. 执行所选入口的能力读取、Pipeline列表、Schema校验、项目创建、Checkpoint读取和一个纯本地Stage提交流程；保留MCP时另测握手。
5. 断言外网调用数为 0，Provider 调用数为 0，嵌套模型调用数为 0。
6. 再注入一个伪造 Provider Tool 请求，确认审批/能力门禁在网络层之前拒绝它。

真实 Provider 测试必须使用独立授权的测试组，不得放宽此离线夹具。

## 4. 不导入或启动 SaaS Worker

静态检查之外，动态测试必须记录当前进程及子进程模块/命令：

- 不得出现 Golden Key SaaS 包名、仓库路径、Worker/BFF 启动模块或 SaaS 配置路径；
- 不得启动另一个 Python/Node 进程作为 Agent Worker；
- 只读 SaaS lock 核对仅属于维护者发布门禁，不进入最终用户运行时；
- 将 SaaS 仓库临时改名或完全不可访问后，离线 Adapter 测试仍必须通过。

## 5. 不发起嵌套 Agent 模型请求

动态测试对以下边界设置不可绕过的 spy/fail stub：

- 任意OpenAI兼容Chat transport构造与`create`/stream调用；
- OpenAI/兼容 SDK Chat Completions 调用；
- `lib.model_driven_agent_host` 导入；
- 任何带有 Agent Host、planner、director-model 或 reviewer-model 语义的子进程/HTTP 调用。

WorkBuddy Agent负责理解、Pipeline选择和Stage创作；CLI或MCP只能返回确定性检查、读取、Schema
校验、受限持久化、Tool执行、状态和取消结果。测试必须验证任何入口都不能通过参数或配置切换为第二个Agent。

## 6. 验收矩阵

| 验证项 | W0 当前状态 | W2/W3 完成条件 |
|---|---|---|
| 静态禁止导入/禁入文件 | `PASS`，六个consumer-remove路径均不存在 | CI 对全部Adapter运行时文件持续通过 |
| SaaS Worker 隔离 | `PASS` | SaaS/private Core路径不存在、从仓库外启动时上下文和项目创建仍通过 |
| 嵌套模型调用拦截 | `PASS` | direct-agent authority、静态禁入/import Gate和Provider调用0持续通过 |
| 外网/Provider 拦截 | `PASS` | Python当前进程与Python/Node子进程真实loopback负测均在连接前拒绝 |
| 本地确定性能力 | `PASS` | 项目、Schema、Checkpoint、Tool、持久任务、并发/超时、CLI/MCP语义和脱敏回归通过 |

W3离线隔离矩阵通过不等于`OFFLINE ADAPTER READY`。W4全新Windows安装、打包和普通用户WorkBuddy验收仍是
该声明的必要条件；真实Provider验收继续是逐次授权的独立Gate。
