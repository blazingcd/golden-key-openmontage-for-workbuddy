# WorkBuddy Shell V2 任务账本

状态：`ACTIVE AUTHORITY / V2-S2-OFFICIAL-PACKAGE-ALIGNMENT-FIX2 / REVIEW_READY`

更新时间：2026-08-17

## 当前任务

```text
task_id: V2-S2-OFFICIAL-PACKAGE-ALIGNMENT-FIX2
task_status: REVIEW_READY
authority_lifetime: ONE_TIME_BOUNDED
start_commit: 8d4461dd159d7aff2484e34c21088ddb9f239053
cumulative_start_commit: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
result_commit: THIS_COMMIT
branch: codex/v2-s2-official-package-alignment-b1
fix_review_range: 8d4461dd159d7aff2484e34c21088ddb9f239053..THIS_COMMIT
cumulative_review_range: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb..THIS_COMMIT
formal_target_branch: origin/codex/workbuddy-shell-v2
formal_target_at_start: 20ddab75825c1b6e7de5a51603afe8b6fd82eceb
promotion_authorization: NOT_GRANTED
reviewer_creation_by_builder: NOT_GRANTED
allowed_paths:
  - golden_key_openmontage_workbuddy/package_registration.py
  - tests/workbuddy/test_package_registration.py
  - docs/workbuddy/v2/PACKAGE-REGISTRATION-CONTRACT.md
  - docs/workbuddy/v2/TASK-REGISTER.md
tracked_file_contract: EXACT_33_UNCHANGED
production_code_files_changed: 1
test_files_changed: 1
contract_files_changed: 2
stage3_implementation: NOT_GRANTED
stage3_files_changed: 0
forbidden_paths_changed: 0
reviewer1_p1_1_git_blob_closure: CLOSED_BY_TEST_CANDIDATE
reviewer1_p1_2_git_environment_closure: CLOSED_BY_TEST_CANDIDATE
reviewer1_p1_3_lock_cas_recovery_evidence: CLOSED_BY_TEST_CANDIDATE
reviewer2_p1_windows_handle_reparse_race: CLOSED_BY_TEST_CANDIDATE
```

`THIS_COMMIT`表示本账本与Builder结果位于同一不可变提交中。只有独立Reviewer
基于结果分支精确40位SHA审阅并给出`APPROVE`，且用户另行授权推广后，正式分支才可
fast-forward。本状态是`REVIEW_READY`，不是`PASS_ACCEPTED`，也不授权Builder创建
Reviewer、推广结果或开始Stage 3。

## 本次修订目标

旧Stage 2合同把Golden Key便携包的Release ZIP、Manifest、Lock和bundled Python当作
OpenMontage身份。它们不是用户提供的官方OpenMontage Git源码树原生身份，其中Python
属于Stage 3 Runtime边界。本次只把Package Registration/Locator修正为官方Git checkout
身份，不修改官方源码、不读取或迁移真实registry、不实施其他Shell模块。

```text
registration_schema: golden-key-workbuddy-openmontage-git-registration-v2
registry_path: <DataRoot>/State/PackageRegistration/v2
register_api: register_package(data_root, package_root, expected_origin_url, expected_commit)
official_origin: https://github.com/calesthio/OpenMontage.git
explicit_commit_selection: REQUIRED
scan_or_guess_latest: FORBIDDEN
v1_automatic_migration: FORBIDDEN
ignored_policy: ALLOWED_BUT_EXCLUDED_FROM_IDENTITY
tracked_changes: REJECT
untracked_files: REJECT
locator_network: 0
locator_writes: 0
locator_git_update: 0
package_mutation: 0
package_python_identity: REMOVED_FROM_STAGE_2
manifest_lock_release_identity: REMOVED_FROM_STAGE_2
```

## 冻结候选对象

用户明确提供且统筹在任务开始前只读核验：

```text
package_root_candidate: D:\BlazingCD\Personal\AIWorkspaces\OpenMontage-official-gate4r-95e1c3d0
origin: https://github.com/calesthio/OpenMontage.git
expected_commit: 95e1c3d0ab93482159818560f6a8c8e866b9139f
local_head_at_gate: 95e1c3d0ab93482159818560f6a8c8e866b9139f
remote_head_at_gate: 95e1c3d0ab93482159818560f6a8c8e866b9139f
worktree_at_gate: CLEAN_DETACHED
data_root: D:\WorkBuddyData
real_v1_registry_at_gate: ABSENT
real_v2_registry_at_gate: ABSENT
```

Builder不得用真实候选或`D:\WorkBuddyData`制造测试状态。Git checkout身份覆盖使用临时
测试fixture；真实外部对象保持零修改。本任务不把一次远端HEAD在线核验嵌入Locator，
也不让Stage 2选择远端“最新”对象。

## 当前实现和证据边界

Registration要求四个显式输入并核验PackageRoot、官方origin、精确HEAD/tree、clean
状态、固定tracked inventory、Git mode、size、SHA-256及tracked非空Guide。tracked或
untracked变化拒绝；ignored文件允许存在但不进入身份。Git命令固定参数、`shell=False`、
固定超时、明确退出码，失败、超时或非UTF-8输出均fail closed。

FIX1进一步把每个`ls-tree` blob OID纳入登记并用稳定文件handle证明工作树字节对应HEAD
blob；拒绝assume-unchanged/skip-worktree，并在hash后复核HEAD/tree/status/inventory/index
flags。Git子进程只接收受控环境，拒绝Git路径、index、object和config注入，且命令级关闭
fsmonitor及可选Git写入。内核锁、跨进程竞争、统一deadline、crash释放、原子replace、
pointer CAS和activate/recover互斥均由v2 Git fixture重新覆盖。

FIX2只关闭Windows tracked-file open竞态：不允许`O_NOFOLLOW=0`式普通open退化；使用
Win32句柄API拒绝final-handle reparse，要求打开后最终路径精确等于tracked path，并在
handle保持打开时重查路径组件。真实junction父目录竞态使用PackageRoot外同内容hardlink
验证必须fail closed。P1-2、P1-3未再修改。

Locator离线、只读、零修复、零网络、零Git fetch/pull，重新核验pointer、登记对象、
PackageRoot、origin、HEAD/tree、clean、inventory和Guide SHA，返回不可变的PackageRoot、
Guide、origin、commit、tree及inventory identity。它不返回Release、Manifest、Lock、
bundled Python或`package_python`。

本次测试证据只证明临时Git fixture上的Stage 2合同、不可变对象、active pointer、内核锁、
CAS、显式恢复和只读Locator。它不证明官方候选已登记，不证明真实DataRoot写入，不证明
Installer、Runtime、Launcher、真实WorkBuddy、OpenMontage生产、Provider、网络、媒体、
SaaS或业务E2E。

## 阶段状态

```text
stage_1_status: PASS_ACCEPTED
stage_2_historical_portable_contract: SUPERSEDED_BY_REVIEW_CANDIDATE
stage_2_official_package_alignment: REVIEW_READY
stage_2_current_acceptance: NOT_YET_ACCEPTED
stage_3_planning_authorization: GRANTED
stage_3_implementation_authorization: NOT_GRANTED
stage_3_launcher_authorization: NOT_GRANTED
stage_3_workbuddy_entry_authorization: NOT_GRANTED
stage_3_status_result_handoff_authorization: NOT_GRANTED
stage_3_other_module_authorization: NOT_GRANTED
```

## 仓库卫生与停止边界

固定FINAL仓库合同仍是33个tracked文件；本次只允许修改其中4个既有文件，不能改变集合、
新增文件、恢复旧控制面或动态放宽`test_repository_hygiene.py`。`.venv`、cache、pyc和临时
文件不得提交。

独立Reviewer下一步只读比较：

```text
20ddab75825c1b6e7de5a51603afe8b6fd82eceb..THIS_COMMIT
```

任一精确对象、正式远端、白名单、33文件集合、测试最终退出、clean状态或Stage 3边界不符，
结论必须为`INCOMPLETE`。Reviewer批准不等于正式交付；正式分支推广仍需独立授权。
