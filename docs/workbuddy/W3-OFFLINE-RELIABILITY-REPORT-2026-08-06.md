# W3 离线可靠性与安全 Gate 报告

日期：2026-08-06

裁决：`PASS`

## 候选边界

- Golden Key Core固定为`golden-key-v0.3.21` WorkBuddy Callable Core导出合同；1566个managed文件只读。
- W3只变更WorkBuddy消费方运行时、测试、打包元数据、Skill和项目文档。
- WorkBuddy仍是唯一Agent；未引入或启动nested Agent Host、SaaS Worker或模型兼容transport。
- 未调用真实/付费Provider，未修改Golden Key SaaS/private Core仓库。

## 已通过的隔离矩阵

| 验证项 | 证据 | 结果 |
|---|---|---|
| Python子进程网络继承 | local Tool启动Python子进程连接真实loopback监听器；`sitecustomize`在连接前拒绝 | `PASS` |
| Node子进程网络继承 | local Tool启动Node `net.createConnection`连接真实loopback监听器；`NODE_OPTIONS --require`在连接前拒绝 | `PASS` |
| 当前进程网络边界 | Python DNS、连接和数据报入口持续由runtime socket guard拒绝 | `PASS` |
| SaaS仓库不可用 | 从仓库外目录启动，SaaS/private Core路径指向不存在目录；context和project create成功 | `PASS` |
| CLI错误脱敏 | Tool异常和Schema错误中的环境密钥替换为`[REDACTED]` | `PASS` |
| MCP结果脱敏 | 嵌套ToolResult敏感字段和Bearer错误在text/structuredContent中均不泄漏 | `PASS` |
| 任务持久化脱敏 | 失败任务的原子JSON记录不包含环境密钥明文 | `PASS` |
| Provider/nested Agent | 全部验证报告`provider_calls_attempted=0`，W1静态隔离Gate无违规 | `PASS` |

## 回归证据

- W3专项：`6 passed`。
- WorkBuddy专项：`76 passed`。
- 完整仓库：`1136 passed, 10 skipped, 1 subtest passed`。
- W1轻依赖Gate：以`python -S`运行，`status=pass`、静态隔离违规0、Provider调用0。
- 消费方Python源码内存编译：22个文件通过。
- `git diff --check`：通过。

## 安全实现说明

- 当前Python进程仍使用运行时socket monkeypatch；受信Core Tool创建子进程时，运行时临时注入并在退出后恢复
  `GOLDEN_KEY_WORKBUDDY_OFFLINE_GUARD`、`PYTHONPATH`和`NODE_OPTIONS`。
- Python子进程通过消费方`sitecustomize.py`加载相同socket拒绝；Node子进程通过消费方CommonJS预加载脚本
  拒绝`net`、`tls`、`http/https`、`dns`、`dgram`和全局`fetch`入口。
- 脱敏在runtime结果、CLI输出、MCP结构化/文本输出和任务原子写入边界执行；明确敏感字段整体替换，
  其他字符串按环境密钥值和常见凭据格式替换。

## 保留边界

- 该Gate证明当前源码候选的离线调用与隔离合同，不证明W4安装器、全新Windows环境或普通用户操作体验。
- 当前Core没有通用协作式取消，运行时截止时间仍只做可观测报警，不强杀Tool。
- MCP保持`optional`；CLI仍是权威回退，W4前不发布活动`.workbuddy/mcp.json`。
- 在W4全新安装和真实WorkBuddy普通用户验收通过前，不得声明`OFFLINE ADAPTER READY`或“已经可以安装”。
- 真实Provider测试必须等待用户单次明确授权，并与本离线Gate分离。
