# Golden Key WorkBuddy Callable Core 同步策略

状态：`FROZEN FOR IMPLEMENTATION`

更新日期：2026-08-05

## 1. 唯一同步源

WorkBuddy 只消费以下不可变 Release 资产：

- tag：`golden-key-v0.3.21`
- source commit：`757ea3822e5f2eef7f341389983119021e827c8d`
- ZIP：`golden-key-v0.3.21-workbuddy-core.zip`
- ZIP SHA-256：`DC21792B6F9D773B1559B1687DEE0CC78FCBFC442400D71A735F7EE375426599`
- SHA sidecar：`golden-key-v0.3.21-workbuddy-core.zip.sha256`
- lock：`GOLDEN_KEY_WORKBUDDY_CORE.lock.json`
- contract ID：`golden-key-workbuddy-callable-core-v1`

`golden-key-v0.3.18`、`v0.3.19`、`v0.3.20` 均已废弃，不得再同步。

## 2. 禁止的同步方式

- 不从 `calesthio/OpenMontage` 直接同步、merge 或 cherry-pick。
- 不 merge/cherry-pick `blazingcd/golden-key-openmontage` 的 `main`、tag ancestry 或任何 private Git 历史。
- 不复制 Core 源仓库中未进入 Release 导出包的文件。
- 不把 source commit 当作公开目标提交的祖先；它只用于 Release provenance 核验。
- 不再维护活动的 `core-sync` 分支。旧分支已改名为 `legacy/core-sync-v0.3.18`，禁止发布。

## 3. 同步步骤

1. 下载 ZIP、SHA sidecar 和 lock。
2. 在解压或读取包内容前，用 `config/openmontage.sync.json` 固定的外部 SHA-256 校验 ZIP。
3. 在 D 盘临时目录处理资产。
4. 验证外部 lock 与 ZIP 内嵌 lock 完全一致。
5. 验证 lock schema、合同 ID、source ref/commit、authority 和 bundle digest。
6. 验证 ZIP 文件清单无缺失、额外、重复、绝对路径、`..` 或反斜杠路径。
7. 对每个文件验证 SHA-256、size、Git mode、classification 和 `apply_mode=replace`。
8. 验证 required paths 全部存在、forbidden paths 全部不在包内。
9. 只镜像 `workbuddy-core/` 下由 `managed_paths`/`managed_prefixes` 声明的内容。
10. 删除受管范围内不在 lock 清单中的旧文件，并确保六个 `consumer_remove_paths` 不存在。
11. 验证 WorkBuddy 消费方自有文件仍保留。
12. 再次验证目标工作树的受管清单和每文件 hash；任何不一致 fail closed。
13. 第二次执行必须为 0 改动，证明幂等。

实现：`scripts/core_sync/sync_workbuddy_core.py`。

### 维护者一键同步命令

```powershell
python scripts/core_sync/sync_workbuddy_core.py sync-release `
  --asset-dir D:\WorkBuddyData\Caches\golden-key-workbuddy-core\golden-key-v0.3.21 `
  --config config\openmontage.sync.json `
  --destination . `
  --report D:\WorkBuddyData\Temp\workbuddy-core-sync-report.json
```

- 缓存命中时仍会完整验证SHA sidecar、ZIP、外部/内嵌lock、bundle和逐文件合同，然后直接复用；不会调用`gh`。
- 缓存缺失时通过已认证的GitHub CLI只下载配置固定的ZIP、SHA sidecar和lock到同一D盘父目录的隔离临时目录。
- 三个资产全部验证通过后才原子建立版本缓存；部分缓存、同级额外文件、下载失败或任何合同漂移均fail closed。
- 缓存中的历史解压子目录不参与同步，可以保留；任何同级额外文件仍被拒绝。
- 命令完成后立即执行managed mirror和目标复核；重复运行必须报告`changed_file_count=0`、`deleted_file_count=0`。

### 维护者同步与公开CI边界

- `blazingcd/golden-key-openmontage`是私有Core源仓库；`sync-release`只在已获授权的维护者环境执行。
- 公开WorkBuddy仓库的GitHub Actions不得保存、请求或依赖任何能够读取私有Core仓库的令牌。
- 公开CI验证已经发布的快照：固定合同身份、四Pipeline、Skill/Schema/Tool引用、禁入路径、W1 Gate和完整测试。
- 每次Core版本更新仍必须先在维护者环境完成Release资产、lock、1566文件和幂等Gate，再把验证后的快照作为普通公开提交发布。

## 4. 六个消费方移除路径

只能按 lock 合同移除以下六个历史泄漏路径：

```text
lib/agent_host_authority.py
lib/model_driven_agent_host.py
lib/openai_compatible_transport.py
tests/contracts/test_agent_host_authority.py
tests/contracts/test_model_driven_agent_host.py
tests/contracts/test_openai_compatible_transport.py
```

同步器不得自行扩展这份列表。

## 5. WorkBuddy 消费方所有权

以下内容不受 Core managed scope 覆盖或删除：

```text
README.md
.gitignore
requirements.txt
setup.py
config/
scripts/core_sync/
scripts/workbuddy/
docs/workbuddy/
tests/workbuddy/
golden_key_openmontage_workbuddy/
workbuddy-skill/
.workbuddy/
PROJECT-STATE.md
WORK-LOG.md
NEXT-CONVERSATION-PROMPT-*.md
```

特别规则：`requirements.txt` 和 `setup.py` 出现在 forbidden paths 中表示 Core 包不得携带或覆盖，
不表示消费者应删除它们。

## 6. Fail-closed 门禁

必须拒绝：

- ZIP 外部 SHA、内嵌 lock 或外部 lock 不一致；
- source ref/commit、contract ID、authority 或 bundle digest 不匹配；
- 缺文件、额外文件、重复成员、不安全路径、hash/size/Git mode 不一致；
- required path 缺失或 forbidden path 进入包；
- managed scope 之外的 Core 文件试图进入项目；
- 六路径集合被增加、减少或重排；
- WorkBuddy 自有文件被覆盖或删除；
- 目标受管范围存在漂移；
- 从官方或 Golden Key private Git history 直接同步；
- 合同、工具或 WorkBuddy 专项测试失败。

## 7. 公开发布节奏

首次公开基线和最终安装发行是两个 Gate：

- 首次基线：新 W0 明确 `PASS`，再由用户看到报告后明确授权；状态只能是 `Pre-Alpha` 或
  “WorkBuddy Adapter 开发中”。
- 持续开发：首次基线建立后，W1～W4 持续留痕、提交和推送。
- 安装发行：只有 W4 真实安装和 WorkBuddy 验收通过，才允许声明 `OFFLINE ADAPTER READY`。

Release 已发布不等于 WorkBuddy 公开仓库已获准推送。
