# Golden Key OpenMontage for WorkBuddy：架构边界

状态：`FROZEN FOR v0.3.21 EXPORT BASELINE`

更新日期：2026-08-05

## 1. 产品目标

本项目交付一个可安装、可验证、适合开源发布的 WorkBuddy 发行版：

```text
Golden Key WorkBuddy Callable Core
+ WorkBuddy Skill
+ WorkBuddy stdio MCP
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
     -> WorkBuddy Skill / MCP 确定性能力
     -> 本地 WorkBuddy Callable Core
        -> Schema / Artifact / Tool Registry / 媒体工具
```

权威运行时声明：

```text
authority.invocation_model = direct_agent
authority.nested_agent_host_allowed = false
```

WorkBuddy MCP 不得拥有第二套 Pipeline 选择器、Director、Reviewer、Checkpoint 协议或模型规划循环。

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
- 不开发新的 Web UI；Backlot 仅作为原生、可选观察界面。
- 不在离线阶段调用真实或付费 Provider。
- 不用 mock 结果声明 WorkBuddy 或真实成片已通过。
