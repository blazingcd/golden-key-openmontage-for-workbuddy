# Project State

更新时间：2026-08-05 23:37 +08:00

## 当前里程碑

`W0 DONE / v0.3.21 PRE-ALPHA BASELINE PUBLISHED / W1 ACTIVE`

新的 W0 只审计 `golden-key-v0.3.21` WorkBuddy Callable Core Release 导出包、公开
`origin/main` lineage 和 WorkBuddy 自有增量。技术 Gate 已通过；用户在看到完整报告和目标提交后
明确授权推送，首个 `Pre-Alpha` 公开基线已发布到 `origin/main`。

## 当前权威基线

| 项目 | 当前值 |
|---|---|
| Release | `golden-key-v0.3.21` |
| Source commit（仅provenance） | `757ea3822e5f2eef7f341389983119021e827c8d` |
| ZIP SHA-256 | `DC21792B6F9D773B1559B1687DEE0CC78FCBFC442400D71A735F7EE375426599` |
| Contract ID | `golden-key-workbuddy-callable-core-v1` |
| Authority | `direct_agent` / nested Agent Host forbidden |
| Managed files | `1566`，目标清单和每文件hash/mode完全匹配 |
| Public base | `origin/main` / `4eab34c5cfcccaa4f1970554928feccce73ee930` |
| Private ancestry | 不属于发布候选；source commit不是当前`main`祖先 |
| Public baseline | `e4f7577bad99e93e0a35217940d8c17f7a6d81cb`，已推送到`origin/main` |

## DONE

- Release ZIP、GitHub asset digest、外部 SHA sidecar、外部/内嵌 lock 完整核验。
- managed scope 精确镜像；公开基线首次导入改写 96 个文件，第二次同步 0 改动。
- 六个 `consumer_remove_paths` 均不存在；`requirements.txt`、`setup.py`、README、配置、同步脚本和文档均保留。
- 同步器对 forbidden path、hash/mode、缺失、额外、scope 漂移、六路径漂移和幂等风险建立负测。
- 四个 Golden Key Pipeline、44 个 Pipeline Skill、Reviewer/Checkpoint、Schema、Tool Registry 和 10 个变更合同测试通过完整性核验。
- 回归：contracts `716 passed, 7 skipped`；tools `284 passed, 1 subtest passed`；WorkBuddy `15 passed`。
- 公开性扫描、direct-agent静态隔离和公开Git lineage Gate通过；未扫描或引入Golden Key私有历史。
- 旧`v0.3.18`整仓发布W0报告保留并脱敏，明确标记为历史且已被取代。
- 首个完整`Pre-Alpha`公开基线已发布；远端`origin/main`核验为`e4f7577bad99e93e0a35217940d8c17f7a6d81cb`。
- W1新增`sync-release`维护者命令：缓存缺失时只下载三个固定Release资产，验证后原子发布缓存；缓存命中时完整复核并复用。
- 真实v0.3.21 D盘缓存回归：1566个文件验证通过，0改动、0删除；当前WorkBuddy专项`18 passed`。
- W0 Pipeline比较基线已固定为配置中的`upstream_base_commit`，不再因首次推送后`origin/main`前移而误报0个合同变化。

## 历史记录（不再是当前Gate）

- `golden-key-v0.3.18`整仓/private ancestry方案的W0裁决为`FAIL`。
- 该结论只约束已废弃旧方案，不否定或阻断v0.3.21 Release导出候选。
- 旧本地分支保留为`legacy/core-sync-v0.3.18`和`legacy/private-ancestry-v0.3.18`，不得推送。

## 下一步

1. 将已完成的`sync-release`命令接入后续常规Gate/CI入口。
2. 建立WorkBuddy包、Skill/测试/示例配置骨架和D盘环境`doctor`。
3. 每个安全、可验证增量持续更新状态、提交并推送；发现公开性风险或测试失败时恢复fail-closed。
4. W2实现WorkBuddy Skill和最小确定性MCP；W3完成动态隔离；W4完成安装与真实WorkBuddy验收。

## 当前允许声明

- v0.3.21 WorkBuddy Callable Core已同步并通过本地W0和回归。
- 首个公开基线已发布，状态为`Pre-Alpha`/“WorkBuddy Adapter开发中”。

当前不允许声明：

- 已经可以安装；
- WorkBuddy Skill/MCP已可用或真实WorkBuddy验收通过；
- `OFFLINE ADAPTER READY`；
- 真实Provider成片通过。

## 权威文件

- `docs/workbuddy/ARCHITECTURE.md`
- `docs/workbuddy/CORE-SYNC-POLICY.md`
- `docs/workbuddy/FIRST-PUBLIC-PUSH-POLICY.md`
- `docs/workbuddy/audits/W0-PUBLICATION-AUDIT-REPORT-v0.3.21-2026-08-05.md`
- `NEXT-CONVERSATION-PROMPT-2026-08-05-W1.md`
