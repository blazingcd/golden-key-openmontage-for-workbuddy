# W0 v0.3.21 WorkBuddy Callable Core公开审计报告

审计日期：2026-08-05

审计对象：`golden-key-v0.3.21` Release导出包 + WorkBuddy自有增量

## Gate裁决

`PASS — AWAITING EXPLICIT PUSH AUTHORIZATION`

当前候选满足公开性、Release同步合同、四Pipeline合同、direct-agent运行时边界、公开Git lineage和
离线回归Gate。该结论只表示候选可以进入“向用户报告并等待授权”状态，不构成推送授权，也不表示
WorkBuddy Adapter、安装或真实成片已经完成。

旧`golden-key-v0.3.18`整仓/private ancestry方案的`FAIL`仍作为历史事实保留在
`W0-PUBLICATION-AUDIT-REPORT-2026-08-05.md`，但旧方案已被本次两层Release导出合同取代，不再是当前阻断。

## 1. Release与lock身份

| 项目 | 核验值 |
|---|---|
| Release tag | `golden-key-v0.3.21` |
| Source commit（仅provenance） | `757ea3822e5f2eef7f341389983119021e827c8d` |
| ZIP | `golden-key-v0.3.21-workbuddy-core.zip` |
| ZIP SHA-256 | `DC21792B6F9D773B1559B1687DEE0CC78FCBFC442400D71A735F7EE375426599` |
| Lock | `GOLDEN_KEY_WORKBUDDY_CORE.lock.json` |
| Contract ID | `golden-key-workbuddy-callable-core-v1` |
| Bundle digest | `ff0da1a11cd67605a79fc5b48bc627325d03a7d405ef3d60caf3a5b537372d64` |
| Authority | `direct_agent`; `nested_agent_host_allowed=false` |

GitHub Release资产digest、外部固定ZIP SHA、sidecar、外部lock和ZIP内嵌lock一致。1566个文件逐项
通过canonical path、SHA-256、size、Git mode、classification和`apply_mode`核验；required paths、
forbidden paths、managed scope和bundle digest全部通过。

证据：`evidence-v0.3.21-2026-08-05/release-contract.json`。

## 2. 同步结果与消费方所有权

- 从公开`origin/main`建立干净候选后，Release managed scope导入改写96个文件，删除0个。
- lock管理1566个文件；其余1470个与公开官方基线内容一致。
- 第二次同步改写0、删除0，幂等通过。
- 六个`consumer_remove_paths`在最终候选中全部不存在。
- `requirements.txt`、`setup.py`、README、`.gitignore`、config、同步脚本、WorkBuddy文档和测试均保留。
- 同步器没有复制Release包外的Golden Key私有源文件。

旧本地private-ancestry工作树的第一次纠偏曾实际移除上述六路径；该分支现只保存在本地`legacy/`
并禁止发布。最终公开候选从`origin/main`建立时这些路径原本不存在，因此最终导入删除数为0。

证据：`core-sync-report.json`、`core-sync-idempotency-report.json`和同步专项测试。

## 3. Git公开lineage

- 公开基线：`origin/main` / `4eab34c5cfcccaa4f1970554928feccce73ee930`。
- 当前`main`从该公开提交重新建立；公开基线是当前HEAD祖先。
- Golden Key source commit不是当前`main`祖先，只作为Release provenance记录。
- 不使用活动`core-sync`；旧分支已改名为`legacy/core-sync-v0.3.18`。
- 不merge/cherry-pick官方更新、Golden Key private `main`或private ancestry。

最终目标commit在本地提交完成并进行提交后只读复核后，由本轮最终报告给出。

证据：`evidence-v0.3.21-2026-08-05/lineage.json`。

## 4. 四个Golden Key业务Pipeline

核验：

- 4个Pipeline manifest；
- 每个Pipeline 11个自有Stage/Executive Producer Skill，共44个；
- `skills/meta/reviewer.md`和`skills/meta/checkpoint-protocol.md`存在并由manifest声明；
- 所有Stage Skill、review focus、success criteria和checkpoint要求存在；
- 所有产物Schema引用存在；
- 22个去重Tool Registry引用全部可发现，无缺失；
- 相对公开官方基线有10个合同测试变化：8新增、2修改；
- 四个Golden Key manifest在当前公开`origin/main`不存在，等待首次授权发布。

证据：`evidence-v0.3.21-2026-08-05/pipeline-integrity.json`。

## 5. 回归测试

```text
tests/contracts   716 passed, 7 skipped
tests/tools       284 passed, 1 subtest passed
tests/workbuddy   15 passed
```

WorkBuddy专项测试包含managed scope精确镜像、消费方文件保护、固定六路径、外部SHA、forbidden、
hash、mode、缺失、额外、只读漂移和幂等负测。测试临时文件和pycache位于D盘临时目录并在运行后清理。
未调用真实或付费Provider。

证据：`evidence-v0.3.21-2026-08-05/regression-results.json`。

## 6. 公开性与许可证范围

扫描范围严格限定为公开`origin/main`到当前候选tree的文件，不扫描、要求公开或把Golden Key私有
源仓库历史当作发布内容。候选扫描结果：

- live secret、credential assignment、private key、token：0；
- 本机绝对路径：0；
- 命名客户/案例标识和具体业务信号：0；
- 新增二进制媒体/字体：0；
- private Core history进入候选：否。

旧W0历史证据保留文件与统计结构，但其中的命名案例、业务信号和非公开commit元数据已不可逆脱敏。
根LICENSE继续继承AGPL-3.0；本轮没有引入新的vendored第三方代码。

证据：`publication-risk-scan.json`、`publication-candidate-files.tsv`和`candidate-inventory.json`。

## 7. 运行时隔离

- 三个Agent Host/transport模块及三个对应合同测试均不存在。
- WorkBuddy自有运行时代码没有导入SaaS Worker或禁入Agent Host模块。
- WorkBuddy是唯一Agent，直接读取Guide、选择Pipeline、读取Skill、写Artifact并执行Checkpoint。
- 当前尚无可运行WorkBuddy Adapter入口，因此动态网络拦截仍为`NOT YET APPLICABLE`，留到W2/W3。

静态边界为`PASS`；这不等于`OFFLINE ADAPTER READY`。

## 8. 剩余风险与责任

1. 首次公开推送仍需用户看到本报告、文件清单、测试和目标commit后再次明确授权。
2. WorkBuddy Skill/MCP尚未实现；不能声明可安装或WorkBuddy验收通过。
3. 动态网络/进程隔离在Adapter入口出现后执行。
4. Python、Node、FFmpeg打包方案仍按`PKG-001`留到W4。
5. 真实Provider和成片验收仍需独立逐次授权。

这些剩余项不阻断`Pre-Alpha`源代码基线，但阻断任何安装可用、WorkBuddy验收或Offline Ready声明。
