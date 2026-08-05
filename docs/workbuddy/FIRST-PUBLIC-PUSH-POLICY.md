# 首次公开推送与持续发布政策

状态：`FROZEN / FIRST BASELINE PUBLISHED`

生效日期：2026-08-05

## 1. 权威结论

首次公开推送不等待 W1～W4 或全部 WorkBuddy Adapter 开发完成，但只由以下两个条件共同解锁：

1. 对最终拟公开 tree/commit 完成基于 v0.3.21 Release 导出合同的新 W0，并得到明确 `PASS`；
2. 用户已经看到该次报告，并对报告列明的目标提交再次作出明确推送授权。

`W0 PASS`、Core Release 已发布、此前的“继续”或本政策本身都不是推送授权。

## 2. 首次完整公开基线

获得授权后应立即建立第一个完整公开基线，不等待 W1～W4。它至少包含：

- `golden-key-v0.3.21` WorkBuddy Callable Core 导出包的全部 1566 个受管文件；
- source commit `757ea3822e5f2eef7f341389983119021e827c8d` 的 Release provenance；
- 四个 Golden Key 业务 Pipeline；
- 44 个 Pipeline Skill、Reviewer/Checkpoint 规则、通用 Schema、Tool Registry 引用和公开合同测试；
- 当时安全可公开的 WorkBuddy 项目增量；
- README、架构、同步策略、`PROJECT-STATE.md`、`WORK-LOG.md` 和 W0 证据。

公开提交必须以公开 `origin/main` 为祖先，不得包含 Golden Key private Git ancestry。推送前报告必须
列出 Gate、风险、待发布文件、测试、Release/lock 身份、目标 tree/commit 和 `origin/main` 当前 hash。

## 3. 对外状态声明

首次公开基线必须标记为 `Pre-Alpha` 或“WorkBuddy Adapter 开发中”。在真实验收完成前不得声称：

- 已经可以安装；
- WorkBuddy Skill/MCP 已可用；
- 已通过真实 WorkBuddy 验收；
- 已达到 `OFFLINE ADAPTER READY`；
- 已调用真实或付费 Provider 并完成真实成片验收。

## 4. CONDITIONAL PASS / FAIL

若新 W0 为 `CONDITIONAL PASS` 或 `FAIL`，不得推送。应先完成所有安全、可逆、范围内修正，列出
外部阻断，并对最终候选重新执行 W0。不得用 private Core 源仓库历史、非导出文件或删除
WorkBuddy 自有文件来绕过问题。

旧 v0.3.18 整仓方案的 `FAIL` 是历史结论；它不再阻断 v0.3.21 导出候选，也不能被误写成旧方案已通过。

## 5. 首次基线后的 W1～W4

首次完整公开基线发布后，W1～W4 持续开发、持续留痕、持续提交和持续推送。任何新的公开性风险、
Core 漂移、测试失败或用户暂停指令都会恢复 fail-closed。

## 6. 当前状态

v0.3.21 导出候选的新 W0 得到 `PASS` 后，用户已针对报告中的目标提交明确授权。首个完整
`Pre-Alpha`公开基线`e4f7577bad99e93e0a35217940d8c17f7a6d81cb`已于2026-08-05推送到
`origin/main`。后续W1～W4按第5节持续开发、留痕、提交和推送；这不放宽fail-closed门禁或对外声明边界。
