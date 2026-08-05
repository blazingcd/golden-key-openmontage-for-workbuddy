# W0 公开性、架构和接口审计报告

> **历史记录，已被取代。** 本报告只记录 `golden-key-v0.3.18`“整仓复制并公开 private Git
> ancestry”旧方案的审计结论。该同步方案已废弃，报告中的 `FAIL`、四位置模型、必须保留嵌套
> Agent Host 文件和剩余项均不得继续作为当前发布 Gate。当前权威基线是
> `golden-key-v0.3.21` 的 `golden-key-workbuddy-callable-core-v1` Release 导出合同，当前 Gate 见
> `W0-PUBLICATION-AUDIT-REPORT-v0.3.21-2026-08-05.md`。
>
> 为保留审计结构同时遵守新公开边界，本历史报告及其证据中的命名案例、业务信号、非公开提交
> 元数据已做不可逆脱敏；原始 Golden Key 私有历史不属于 WorkBuddy 发布候选。

审计日期：2026-08-05

审计目标：本地 `main` 审计前提交 `[private-commit-fingerprint:24cf792cbc0ace26]`

Golden Key 锁定核心：`golden-key-v0.3.18` / `[private-commit-fingerprint:8dc4b3a945ddd6e3]`

官方基线：`4eab34c5cfcccaa4f1970554928feccce73ee930`

## Gate 裁决

`FAIL`

当前 Golden Key 核心快照和现行“把 private 核心提交作为公开 `main` 祖先”的发布方式不得推送到公开 `origin`。阻断原因不是 Pipeline 不完整或合同测试失败，而是待公开核心及其 Git 历史包含尚未确认可公开的 private-fork/真实客户案例信息、命名案例、作者邮箱和本机路径历史。WorkBuddy 仓库无权在核心拥有路径中直接修复这些内容，且只在新提交中删除或改名不能清除可达 Git 历史。

本裁决只针对首次公开发布 Gate，不否定 Golden Key 核心的本地合同完整性，也不代表 WorkBuddy Adapter 已实现或已验收。

## 1. 四位置 Git 基线

实时 fetch 后的结论：

| 位置 | Commit | 结论 |
|---|---|---|
| `golden-key-core/main` | `[private-commit-fingerprint:8dc4b3a945ddd6e3]` | Golden Key 远端真相源 |
| 本地 `core-sync` | `[private-commit-fingerprint:8dc4b3a945ddd6e3]` | 与远端全仓 tree 差异为 0；tag 精确匹配 |
| 本地 `main`（审计前） | `[private-commit-fingerprint:24cf792cbc0ace26]` | 以锁定核心为祖先；核心受保护路径差异为 0 |
| 公开 `origin/main` | `4eab34c5cfcccaa4f1970554928feccce73ee930` | 仍是官方基线；四个 Golden Key Pipeline 均不存在 |

当时只读核对的 Golden Key SaaS lock 同样指向 `golden-key-v0.3.18` / `[historical private commit redacted]`。证据见
`evidence-2026-08-05/w0-git-baseline.json`；证据文件不记录 SaaS 仓库绝对路径。

## 2. 四个 Golden Key Pipeline 合同完整性

核验对象：

- `golden-key-brand-company`
- `golden-key-lead-conversion`
- `golden-key-product-marketing`
- `golden-key-subject-ip`

四个 Pipeline 均满足：

- Manifest 在 Golden Key 远端、本地 `core-sync`、本地 `main` 的 blob 完全一致，在公开 `origin/main` 不存在；
- 每个 Pipeline 有 11 个自有 Pipeline Skill，共 44 个；三处 blob 一致；
- Manifest 通过通用 `pipeline_manifest.schema.json`；
- `meta/reviewer`、`meta/checkpoint-protocol` 和 `default_checkpoint_policy: guided` 均已声明；
- 每个 Stage 都声明存在的 Stage Skill、`checkpoint_required: true`、非空 `review_focus` 和 `success_criteria`；
- 产出的 `brief`、`proposal_packet`、`script`、`scene_plan`、`asset_manifest`、`edit_decisions`、`render_report`、`final_review`、`publish_log`、`decision_log` 均引用 OpenMontage 通用 Artifact Schema，没有复制四套 Schema；
- 22 个 Manifest Tool 引用全部存在于实时 Tool Registry；Registry 共发现 102 个工具；
- Golden Key 相对官方新增 11 个合同测试文件，三处 blob 一致，公开 `origin/main` 不存在。

完整逐 Pipeline/Skill/Stage/Schema/Tool/blob 矩阵见
`evidence-2026-08-05/pipeline-integrity.json`。

## 3. 合同与相关工具测试

在独立 D 盘环境 `<W0_VENV>` 中运行；没有 Provider 调用：

```text
python -m pytest tests\contracts -q --disable-warnings --maxfail=1
743 passed, 7 skipped in 86.52s

python -m pytest tests\tools\test_browser_runtime.py tests\tools\test_cinematic_remotion_adapter.py tests\tools\test_corpus_builder_total_failure.py tests\tools\test_hyperframes_compose.py tests\tools\test_remotion_caption_burn.py tests\tools\test_remotion_diagnostics.py -q --disable-warnings --maxfail=1
70 passed in 40.26s
```

7 个 skip 是测试套件声明的环境条件，不是断言失败。

## 4. Golden Key 相对官方的完整差异和历史

- Golden Key 核心相对官方：40 个提交、107 个路径差异（81 新增、25 修改、1 删除）。
- WorkBuddy 审计前增量相对核心：7 个提交、10 个路径差异（9 新增、1 修改）。
- 公开 `origin/main` 到审计前本地 `main`：117 个路径差异。
- 核心差异唯一媒体路径是删除上游 `diagram.png`；没有新增图片、音频、视频或字体二进制。

完整清单：

- `evidence-2026-08-05/golden-key-vs-official-files.tsv`
- `evidence-2026-08-05/workbuddy-vs-core-files.tsv`
- `evidence-2026-08-05/first-publication-files.tsv`
- `evidence-2026-08-05/golden-key-commit-history.tsv`
- `evidence-2026-08-05/workbuddy-commit-history.tsv`
- `evidence-2026-08-05/first-publication-working-tree-files.tsv`（包含 W0 新增证据和安全修正）

## 5. 密钥、路径、客户/SaaS 数据和 Provider 配置

确定性扫描覆盖公开差异当前快照 117 个路径，以及 `origin/main..main` 可达历史中的 355 个变更 blob。证据只保存路径、行号、类别和不可逆指纹，不保存匹配值。

### 已排除的假阳性

`tests/contracts/test_openai_compatible_transport.py:14` 使用明显的 `sk-` 前缀测试占位值，并在同一测试文件中断言异常、响应体和对象表示不能泄露该值。743 个合同测试通过，因此它不是 live secret。

`https://tokenhub.tencentmaas.com/v1` 是腾讯云官方公开文档列出的 TokenHub 接口地址，不是内部地址或私有配置；测试中没有真实 key。

### WorkBuddy 当前快照已修正

两个历史交接 Prompt 的本机绝对路径已替换为 `<WORKBUDDY_REPO_ROOT>`、`<GOLDEN_KEY_SAAS_REPO_ROOT>` 和 `<GOLDEN_KEY_CORE_REPO_ROOT>`。README 已增加预发布警示，避免把尚未实现的 Skill/MCP 描述成可用成品。

包含 W0 新增报告、证据、脚本和测试后的首次发布工作树清单共有 134 个路径；重新扫描后的当前工作树绝对私有路径命中为 0。唯一 credential-like 命中仍是上述合同测试占位值。证据见 `evidence-2026-08-05/first-publication-working-tree-files.tsv` 和 `evidence-2026-08-05/publication-working-tree-risk-scan.json`。

### 未解决的核心和历史阻断

1. `docs/DIRECTOR-ONLY-ROUND-1-EVIDENCE-2026-07-29.md:7` 明确自称 private-fork note；同文件第 23-31、43-50 行描述命名案例、真实客户事实/素材和具体转化信号。
2. `tests/fixtures/golden_key_four_pipeline_route_robustness_cases.yaml:4-12` 及对应 results 文件保留 [named-case-a]/[named-case-a]、项目合作、[customer-signal] 和响应责任人状态；其他合同/fixture 还出现 [named-case-b]/[named-case-b]和 [named-case-c] 命名案例。
3. 47 个待公开提交均带作者邮箱元数据；证据清单只保存邮箱指纹，但 Git 推送会公开原始 commit metadata。
4. 现有本地历史中仍有 10 个绝对路径匹配。修改当前快照不会从可达历史移除它们。

这些内容是否获得公开授权无法从仓库证明。Golden Key 核心路径属于受保护路径，本仓库未修改它们。

完整脱敏命中见 `evidence-2026-08-05/publication-risk-scan.json`。

## 6. 素材、字体、品牌、第三方代码和许可证

- Golden Key 差异没有新增媒体、字体或 vendor/third_party 目录；唯一媒体差异是删除上游 `diagram.png`。
- 根 `LICENSE` 在官方、核心和本地 `main` 的 blob 相同，继续是 AGPL-3.0；没有 LICENSE/NOTICE 变更。
- 新增运行依赖只有 `httpx>=0.28,<1`；本轮安装验证的 `httpx 0.28.1` 包元数据声明 BSD-3-Clause，且代码没有 vendored 进仓库。
- README 明确本项目不是 OpenMontage 或 WorkBuddy 官方发行，相关名称和标识归各自权利人所有。
- [named-case-c]/[named-case-a]/[named-case-b] 等文本案例的素材权、商标/角色权和客户公开许可未在仓库中形成可复核授权，因此继续属于 Gate 阻断，而不是按普通测试夹具自动放行。

`PKG-001` 的 Python、Node、FFmpeg 再分发许可证仍按冻结计划留到 W4；本报告不提前决定打包方案。

## 7. 三层能力边界

### Golden Key OpenMontage 核心

包含四个业务 Pipeline、44 个 Pipeline Skill、通用 Schema、Review/Checkpoint 规则、Tool Registry、合同测试，以及通用 Agent Host/transport 文件。后两类文件必须保留，但 WorkBuddy 运行时不得调用。

### WorkBuddy 适配层

当前只有架构/同步/路线/状态文档、同步清单和 W0 审计脚本；尚无可安装 Skill、MCP Server 或 Adapter 入口。不能声明 WorkBuddy 握手、离线体验或成片已通过。

### Golden Key SaaS 参考边界

W0 只读核对 `openmontage.lock.json`。本仓库没有复制或调用 SaaS BFF、Core Invocation、Agent Worker、Job/Outbox、多租户或 Provider 管理代码。

## 8. 运行时隔离

当前静态扫描没有发现 WorkBuddy 自有代码导入 Agent Host transport 或 SaaS Worker，且两个核心文件均保留。由于 Adapter 入口尚不存在，动态网络拦截和进程隔离结论是 `NOT YET APPLICABLE`，不是 PASS。

冻结方案见 `docs/workbuddy/W0-RUNTIME-ISOLATION-TEST-PLAN.md`，机器结果见
`evidence-2026-08-05/runtime-isolation-scan.json`。

## 9. Codex Security 工作台覆盖缺口

标准安全扫描 ID `570a0a8a-65a1-402f-90e3-ff5d4e4042fe` 未完成：预检因当前会话不允许委派且无法证明六个 worker slot 而保持 incomplete；随后权威文件清单在 Windows 路径校验处把第 1 行判为 unsafe repository path。该工具没有产生 sealed report，因此本报告不声称完成了 Codex Security 的 2127 文件语义扫描。

W0 的发布差异/历史、秘密模式、Pipeline 合同和测试证据由仓库内确定性脚本独立完成。完整语义安全扫描仍应在公开 Gate 重新评审时补跑，但它不能消除本报告已确认的客户/历史阻断。

## 10. 最小剩余项与责任归属

1. **用户/仓库所有者决策：** 在以下方案中明确选择公开策略：
   - 推荐：建立“私有核心同步身份”和“公开净化导出历史”两层模型；公开分支从官方基线生成经过审计的净化快照，不推送 private 核心提交历史，并相应更新冻结的架构/同步门禁。
   - 或：逐项取得并记录对命名案例、客户信息、作者邮箱和历史路径公开的明确授权，继续保留现有 ancestry。
   - 不推荐：重写已冻结 Golden Key tag；这违反当前不可变 tag 策略。
2. **Golden Key 核心责任：** 对 private-fork 证据文档、命名案例和真实客户状态进行授权确认或匿名化设计。WorkBuddy 仓库不得直接改核心受保护路径。
3. **WorkBuddy 责任：** 获得策略授权后更新 `ARCHITECTURE.md`、`CORE-SYNC-POLICY.md`、发布清单和 Gate 脚本；W2/W3 再实现并执行动态隔离测试。
4. **重新审计：** 对最终拟公开 commit/history 重跑 W0 脚本、秘密扫描、合同测试和可用的完整安全扫描，再给出新 Gate。

在上述最小剩余项完成并产生新证据前，公开推送继续被禁止。
