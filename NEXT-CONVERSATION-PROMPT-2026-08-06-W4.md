# Golden Key OpenMontage for WorkBuddy：W4继续开发Prompt

请在`<WORKBUDDY_REPO_ROOT>`继续工作。先完整读取`AGENT_GUIDE.md`，然后读取：

1. `PROJECT-STATE.md`
2. `docs/workbuddy/ARCHITECTURE.md`
3. `docs/workbuddy/ROADMAP.md`
4. `docs/workbuddy/W3-OFFLINE-RELIABILITY-REPORT-2026-08-06.md`
5. `docs/workbuddy/W2-MCP-DECISION-2026-08-06.md`
6. `docs/workbuddy/LOCAL-STORAGE-POLICY.md`
7. `docs/workbuddy/CORE-SYNC-POLICY.md`
8. `WORK-LOG.md`最后一条记录

## 当前权威基线

- Core=`golden-key-v0.3.21`；contract ID=`golden-key-workbuddy-callable-core-v1`；1566个managed文件只读。
- authority=`direct_agent`；WorkBuddy是唯一Agent；nested Agent Host forbidden。
- 四个Golden Key业务Pipeline、44个Pipeline Skill、Schema/Reviewer/Checkpoint/Tool Registry合同完整。
- W0首个`Pre-Alpha`公开基线已发布；W1同步/包/doctor/gate/Skill/CI完成；W2调用、任务和
  `MCP=optional`裁决完成；W3离线可靠性Gate=`PASS`。
- W3验证Python/Node子进程网络继承、SaaS/private Core仓库不可用、CLI/MCP/任务统一脱敏；
  WorkBuddy专项=`76 passed`，完整回归=`1136 passed, 10 skipped, 1 subtest passed`。
- CLI是权威回退；MCP仅是本地stdio结构化工具增强，活动配置尚未进入仓库发行面。
- 当前仍为`Pre-Alpha`，尚未通过W4全新Windows安装和普通用户WorkBuddy验收，不得声明
  “已经可以安装”或`OFFLINE ADAPTER READY`。

## W4目标

1. 先基于现有`PKG-001`和真实机器状态，冻结Python、Node、FFmpeg、Core/Skill和消费方包的Windows交付合同；
   区分开发环境、便携运行目录和最终安装器，不把工程缓存放到C盘。
2. 以TDD建立一个最小、可回滚的D盘安装纵向切片：安装、doctor/gate、版本/合同核验、升级和卸载；
   不删除用户项目、Artifact、配置或模型数据。
3. 打包可导入WorkBuddy Skill和完整v0.3.21 Callable Core；普通用户不得另外下载Golden Key私有Core。
4. 按`MCP=optional`提供明确选择：默认CLI可用；启用MCP时只生成用户级stdio配置和首次信任指引，
   不覆盖已有配置，并提供禁用/卸载路径。
5. 编写中文快速开始、自然语言示例和故障排查；所有状态继续明确`Pre-Alpha`，不声称Provider生产验收。
6. 先验证一个全新D盘目录，再在真实WorkBuddy中验证Skill发现、自然语言触发、Pipeline选择、Stage Skill、
   本地Tool、长任务状态/恢复和Human Checkpoint。真实Provider成片保持独立授权Gate。
7. 每个安全可验证增量更新`PROJECT-STATE.md`、追加`WORK-LOG.md`、重跑W0并持续提交推送。

## 发布红线

- 不修改v0.3.21 managed Core；Core改动只能通过新的不可变Release合同迁移。
- 不修改Golden Key SaaS/private Core仓库，不直接同步官方OpenMontage或private Git ancestry。
- 不调用真实/付费Provider，除非用户针对该次验证另行明确授权。
- 不覆盖或删除用户已有WorkBuddy配置、项目、Artifact、模型、缓存或凭据。
- W4全新安装和真实WorkBuddy普通用户验收通过前，不声明`OFFLINE ADAPTER READY`。
