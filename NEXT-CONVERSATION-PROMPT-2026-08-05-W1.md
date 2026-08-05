# Golden Key OpenMontage for WorkBuddy：W1继续开发Prompt

请在`<WORKBUDDY_REPO_ROOT>`继续工作。先完整读取`AGENT_GUIDE.md`，然后读取：

1. `PROJECT-STATE.md`
2. `docs/workbuddy/ARCHITECTURE.md`
3. `docs/workbuddy/CORE-SYNC-POLICY.md`
4. `docs/workbuddy/FIRST-PUBLIC-PUSH-POLICY.md`
5. `docs/workbuddy/ROADMAP.md`
6. `docs/workbuddy/audits/W0-PUBLICATION-AUDIT-REPORT-v0.3.21-2026-08-05.md`
7. `WORK-LOG.md`最后一条记录

## 当前权威基线

- 唯一同步源：`golden-key-v0.3.21` Release资产。
- source commit（仅provenance）：`757ea3822e5f2eef7f341389983119021e827c8d`。
- ZIP SHA-256：`DC21792B6F9D773B1559B1687DEE0CC78FCBFC442400D71A735F7EE375426599`。
- contract ID：`golden-key-workbuddy-callable-core-v1`。
- authority：`direct_agent`，nested Agent Host forbidden。
- 当前`main`以公开`origin/main`为祖先，不包含Golden Key private Git ancestry。
- 1566个受管文件已同步并通过lock校验；四Pipeline、44个Skill、合同和工具回归已通过。
- 新W0 Gate=`PASS`，但公开推送仍未授权。

`golden-key-v0.3.18`、`v0.3.19`、`v0.3.20`和活动`core-sync`方案均已废弃。不得直接同步官方
OpenMontage，不得merge/cherry-pick Golden Key private `main`或历史，不得复制Release包外文件。

## W1下一步

1. 将Release下载、固定SHA、lock验证、managed mirror和幂等检查封装为维护者可重复执行的命令。
2. 建立WorkBuddy Python包、Skill目录、测试目录和示例配置骨架。
3. 建立D盘项目、缓存、模型和临时目录规则及`doctor`骨架。
4. 保持`requirements.txt`、`setup.py`、README、config、同步脚本、Adapter/MCP、打包和文档为消费方所有。
5. 保持六个consumer-remove路径不存在，并禁止重新实现Agent Host/transport。
6. 每个安全可验证增量更新`PROJECT-STATE.md`和追加`WORK-LOG.md`，运行专项测试后本地提交。

## 发布红线

- 本Prompt不是公开推送授权。
- 在用户针对报告中的最终目标提交明确回复允许推送前，不得推送`origin`。
- 不修改`golden_key_short_video_agent`。
- 不调用真实或付费Provider。
- 不声明已安装、真实WorkBuddy验收通过或`OFFLINE ADAPTER READY`。
