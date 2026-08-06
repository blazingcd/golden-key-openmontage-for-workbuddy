# W2 MCP 决策 Gate

日期：2026-08-06

客户端：WorkBuddy `5.3.8`（已登录，默认权限）

裁决：`PASS / MCP=optional`

## 1. 裁决

直接CLI继续作为必选入口和权威回退。本地stdio MCP保留为可选的结构化工具适配层，不是远端服务、
不是第二个Agent，也不拥有Pipeline选择、创作、Reviewer、Checkpoint或任务重试逻辑。

W4打包前不在仓库发布活动`.workbuddy/mcp.json`。后续安装器可以选择生成WorkBuddy用户级配置，
但必须展示本地命令、要求WorkBuddy信任确认，并允许用户不启用或随时禁用MCP。

## 2. 实机证据

### Skill+CLI

- 导入包只含一个已审计`SKILL.md`；SHA-256为
  `4B40A3A614388E32F9FAA3525A1C94E3E7E72BE993F75FC39FC7BD665619EAA3`。
- WorkBuddy成功安装并启用`golden-key-openmontage` Skill。
- WorkBuddy读取`AGENT_GUIDE.md`后运行本地`doctor`和`context`；两条命令退出码均为0。
- `authority.invocation_model=direct_agent`，`nested_agent_host_allowed=false`，四条Pipeline完整，
  `provider_calls_attempted=0`。
- WorkBuddy Host默认会为实质任务写自己的workspace memory；该未跟踪验收文件已从发布候选清理，
  不是CLI或Core合同的一部分。

### Skill+stdio MCP

- WorkBuddy用户级stdio配置成功启动D盘虚拟环境中的消费方服务器。
- 首次启用要求明确的本地服务信任确认；首轮16个工具通过实机握手；随后按CLI等价面补齐
  `golden_key_tool_execute`，最终合同固定为17个工具。
- WorkBuddy先读取`AGENT_GUIDE.md`和Skill，再通过Schema搜索只选择目标工具；
  `golden_key_context`与`golden_key_pipelines`均返回`status=pass`。
- 两次正常调用均报告`provider_calls_attempted=0`，没有Shell、文件写入、外网或Core修改。
- 失败路径只调用一次`golden_key_task_status`，非法task ID在输入校验阶段返回`status=fail`，
  `tool_calls_attempted=0`、`provider_calls_attempted=0`、`network_calls_attempted=0`，WorkBuddy未重试。
- 服务器按MCP合同返回`isError=true`，本地测试确认；WorkBuddy 5.3.8的模型侧没有可靠呈现该传输层字段，
  但正确读取了业务层`status=fail`和结构化错误。因此业务`status/errors`仍是强制判断依据。

## 3. 对比

| 维度 | Skill+CLI | Skill+stdio MCP |
|---|---|---|
| 安装复杂度 | 较低；安装包和Skill即可 | 额外用户级JSON、stdio进程和首次信任 |
| Schema发现 | 依赖Skill中的命令合同 | WorkBuddy原生发现17个JSON Schema工具 |
| 调用方式 | 构造本地命令行 | 结构化工具参数，无Shell拼接 |
| Pipeline选择 | WorkBuddy | WorkBuddy，MCP不选择 |
| 长任务/恢复 | 原生`task`合同 | 调用同一`task`函数，无第二套状态机 |
| 失败语义 | 退出码+JSON `status/errors` | JSON `status/errors`可靠；Host未稳定呈现`isError` |
| 权限成本 | 可能触发命令权限 | 一次本地服务信任；之后按工具调用 |
| Provider/网络 | 本次均为0 | 本次均为0 |

## 4. Gate边界

- `PASS`只表示真实WorkBuddy中的离线CLI/MCP对照通过，并完成MCP交付形态裁决。
- 它不表示完整安装包、普通用户全新机器验收、长时间可靠性、真实Provider或成片通过。
- `claims.real_workbuddy_accepted`继续为`false`，直至W4完整安装与真实使用矩阵通过。
- v0.3.21 managed Core未修改；候选MCP只调用现有WorkBuddy消费方函数。
