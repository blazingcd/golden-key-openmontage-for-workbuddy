# OpenMontage Package Registration and Locator Contract

状态：`PASS_ACCEPTED / REGISTRATION_LOCATOR_AND_TEMPORARY_PACKAGE_PROOF_ONLY`

## 1. Object and boundary

Stage 2 registers one explicitly supplied **Golden Key OpenMontage for WorkBuddy Package**. The Package is an already assembled portable ZIP plus its installed PackageRoot. It contains the reviewed Golden Key OpenMontage resource directory and the complete package-private required toolchain.

Stage 2 does not download, install, launch, repair, select a renderer, run WorkBuddy, interpret the external Guide, or perform media production. Stage 3 must not replace or fall back to system Python, FFmpeg, or Node.

The public entries remain:

```python
register_package(data_root, release_archive, release_sha256_sidecar, package_root, package_python)
activate_package(data_root, expected_active_pointer_sha256_or_missing, registration_sha256)
recover_active_package(data_root, expected_broken_pointer_sha256, replacement_registration_sha256)
locate_active_package(data_root)
```

`package_python` is retained as the compatibility input and must equal the fixed Python executable declared by the Package. No new public entry is added.

## 2. Fixed schemas, authority, and paths

```text
registration schema: golden-key-workbuddy-openmontage-package-registration-v2
registration owner: golden-key-workbuddy-shell-v2
active pointer schema: golden-key-workbuddy-active-openmontage-package-v1
active lock schema: golden-key-workbuddy-active-package-lock-v1
manifest schema: golden-key-workbuddy-portable-bundle-v2
core lock schema: integer 2
dependency lock schema: golden-key-workbuddy-python-core-dependencies-v1
manifest: BUNDLE-MANIFEST.json
core lock: GOLDEN_KEY_WORKBUDDY_CORE.lock.json
guide: AGENT_GUIDE.md
python: bootstrap/python/python.exe
python dependency lock: bootstrap/python/CORE-DEPENDENCIES.lock.json
ffmpeg: bootstrap/ffmpeg/bin/ffmpeg.exe
ffprobe: bootstrap/ffmpeg/bin/ffprobe.exe
node: bootstrap/node/node.exe
npm: bootstrap/node/npm.cmd
npx: bootstrap/node/npx.cmd
```

Manifest authority remains exactly `direct_agent / nested_agent_host_allowed=false`. Core Lock authority remains exactly the WorkBuddy direct-agent authority accepted in Stage 2. The Shell does not become a second Agent, Director, FSM, or production control plane.

## 3. Closed required-toolchain contract

Manifest `installation.runtime_roles` has exactly `python`, `ffmpeg`, and `node`. Manifest `required_toolchain` has exactly `python`, `ffmpeg`, `node`, and `managed_files`.

- Python declares version, fixed source label, source archive SHA-256 and size, `system_python_required=false`, executable, and dependency-lock path.
- FFmpeg declares actual version, fixed source label, source archive SHA-256 and size, and fixed `ffmpeg`/`ffprobe` paths.
- Node declares version, fixed source label, source archive SHA-256 and size, and fixed `node`/`npm`/`npx` paths.
- Every byte below `bootstrap/python`, `bootstrap/ffmpeg`, and `bootstrap/node` is listed exactly once in `required_toolchain.managed_files` and exactly once in Manifest `files` with owner `workbuddy_required_toolchain`. The actual filesystem set must equal that declared set.

The Python dependency lock has a closed root of `schema_version`, `python_version`, `requirements`, and `packages`. Each package has exactly `name`, `version`, and its managed `.dist-info/METADATA` path. Names are normalization-unique; every installed distribution metadata file is locked; recorded Name/Version must equal installed metadata.

The Registration root remains closed and adds only `required_toolchain`; `package_python` remains as a compatibility identity. `required_toolchain` returns the exact fixed path, canonical path, SHA-256, size, version, source archive identity, dependency lock, 47 resolved Python distributions, FFmpeg/ffprobe, and Node/npm/npx. Manifest hash binds the complete managed-file closure without duplicating thousands of entries into the Registration object.

## 4. Validation and fail-closed behavior

Registration and every later activation, recovery, or locate perform the previous Release/sidecar, archive-member, Manifest, Core Lock, Guide, managed-core, canonical-path, object-hash, active-lock, CAS, and atomic-pointer checks. They additionally:

1. reject missing or unknown toolchain schema fields;
2. reject absolute, escaping, aliased, reserved, ADS, symlink, or reparse tool paths;
3. reject missing, duplicate, unlisted, or extra toolchain managed files;
4. hash and size-check every managed toolchain file;
5. reject executable identity exchange or source/version drift;
6. reject dependency-lock duplicates, uncovered distributions, and installed Name/Version mismatch;
7. re-run the complete validation from the immutable Registration object during Locator reads.

Stable errors remain `INPUT_INVALID`, `PATH_VIOLATION`, `OBJECT_MISSING`, `DUPLICATE`, `IDENTITY_MISMATCH`, `HASH_MISMATCH`, `TAMPERED`, `ACTIVE_LOCK_BUSY`, `ACTIVE_CAS_MISMATCH`, and `ATOMIC_WRITE_FAILED`.

Registration never activates. Activation remains explicit CAS. Recovery remains explicit hash-locked replacement of a broken pointer. Locator remains read-only and never repairs, scans, downloads, launches, or chooses a fallback.

## 5. Exact accepted refresh evidence

```text
source package commit: 8395e578165e802990d53fef5a166f8b4cf0461a
source package tree: 0464861c5985c7c9072e789b94889d29cf9a937a
Python: 3.14.7 / archive 12,673,227 bytes / d297e5ff019966817ad8502465176139f2d3d840fa4ed84b13bed399a6ab1f15
FFmpeg and ffprobe actual version: 9.0.1-essentials_build
FFmpeg archive: 34,372,199 bytes / 49a73bdf0850092a252ac4641d922f3048d63ed113e196cc65ce1e4f7fb33e85
Node: 22.23.2; npm/npx: 10.9.8
Node archive: 35,683,585 bytes / 1177b4137ba5adaa56354ae40f1080c7450e8ae09cecb47da459d1c52ac99f97
locked Python distributions: 47
offline reconstruction: 4,555 files / missing 0 / extra 0 / changed 0
core files: 2,155
required-toolchain managed files: 6,670
Manifest entries: 8,826
Release ZIP: 223,112,435 bytes / f00e83d6154e7593b765a3d6c863b6653fc642818133acd7924f3fd91aab5d03
real temporary registration: aa5aba5ff543258d58acf944a0f4e87d80b9f38e62205268ae23b5266b78659b
```

The dependency reconstruction uses the frozen Aliyun-resolved wheelhouse twice with `--no-compile`. Location-dependent console wrappers and pip `RECORD` installation receipts are excluded from both reconstructions; the remaining runtime dependency trees are byte-identical. The final private Python successfully imports every requirement and passes SSL plus same-interpreter subprocess checks. FFmpeg, ffprobe, Node, npm, and npx version commands pass. Real register, temporary activation, and read-only locate pass in a task-only DataRoot.

The Release, PackageRoot, and DataRoot used for this proof were task-only temporary objects and were deleted after evidence capture. This accepted evidence proves Registration/Locator behavior and repeatable complete-toolchain assembly, but does not prove a retained final Release, installed production PackageRoot, production Registration/Activation, Installer, Stage 3 optional capabilities, Launcher, real WorkBuddy, Provider, media, SaaS, network production, or business E2E.

## 6. Current Stage 5 final-delivery ownership boundary

This Stage 2 contract remains unchanged: the public Registration/Activation/Locator schemas, APIs, validation rules, and accepted temporary-package evidence above are not reopened or expanded by Stage 5 planning. The retained final Release, production PackageRoot, production Registration/Activation, and new-process Locator proof are final-delivery responsibilities of the separately authorized `V2-S5-R04-INSTALLER-LIFECYCLE1` and `V2-S5-R05-FINAL-PACKAGE-MATERIALIZATION-REGISTRATION1` tasks. The final installed, Installer-stamped WorkBuddy Skill is handled by the separately authorized R03/R04/R06 chain. Until those tasks produce evidence, `final_package_artifact=NOT_MATERIALIZED`, `production_package_root=NOT_CREATED`, `production_registration_activation=NOT_CREATED`, `final_installed_skill=NOT_CREATED`, and a real WorkBuddy `LauncherReceiptV1` remains `NOT_PROVED`. R00 and R01 do not create, register, activate, or silently promote any Package object.

## 7. [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT / ORIGINAL R01 / FORMALLY CLOSED / PRESERVED] Current R01 boundary confirmation

R01 was a controlled WorkBuddy execution-contract evidence attempt only. It did not call Registration, Activation, Locator, Package, Installer, Stage4, Provider, media, or Stage6. WorkBuddy `5.3.14` installed the temporary probe Skill after a non-skipped safety scan, but the HY3 path exposed no independent native bundled-script invocation/tool event and execution stopped before Bash/PowerShell. The final R01 result is `BLOCKED_EXTERNAL_CONTRACT`; independent review approved and formally fast-forwarded the docs closeout. The user uninstalled the temporary Skill, WorkBuddy showed `2` installed Skills, task history remained, and the exact probe folder/ZIP was deleted; the two baseline Skills were untouched. The Stage 2 contract and its accepted temporary-package proof remain unchanged. R02-R08 are blocked by the strict chain.

## 8. [HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT] R01 Sandbox Refresh1 不改变 Stage 2 Registration/Locator 合同（正式结果镜像，2026-08-22）

refresh1 是独立的 WorkBuddy 客户端沙箱执行面窄核验，不调用、不修改 Registration、Activation、Locator、Package、Installer 或 Stage 2 既有临时 Package 证据。官方 134420 明示 enterprise Skill scripts 在客户端沙箱执行。受控 WorkBuddy 客户端观察将 PowerShell 记录为沙箱执行面的 `ELIGIBLE_CANDIDATE_SURFACE`，不是官方精确执行合同；本轮不得再把 PowerShell 非原生当作阻断。剩余阻断是 Skill-root cwd/bundled-relative resource resolution 与 stdin/stdout/stderr/final-exit/timeout 合同缺失；134432 仅证明 Skill 脚本/工作流打包上传调用形态，134516 是 CodeBuddy `PRODUCT_MISMATCH_NOT_CONTRACT_PROOF`。

```text
task: V2-S5-R01-WORKBUDDY-SANDBOX-REFRESH1 / ACCEPTED_BLOCKED_EXTERNAL_CONTRACT / NO_ACTIVE_TASK
accepted_result: 6c20371f1c72ee9d55147e1ad7feb8ede201858f / tree 9eb4643f09d03cc9f39b0b46906773e5bcc9125d / docs_review=APPROVE_P0_0_P1_0_P2_0
base: 932bcabc5baf90d0190101b1039e4ccf087b2b08 / tree 2ed2cd0e67dd8628b7f0b1acf84df0a7d8b0d0fd / tracked 40
client: WorkBuddy 5.3.14 / HY3_ONLY / NEVER_AUTO / baseline=agent-browser,find-skills
probe: ISOLATED_D_DRIVE_TEMP_ROOT / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / CLEANUP_COMPLETE / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND
hashes: SKILL=A369E89912B51C1627C972A7DE8F82111E55E2909622CB2E0E3276B45331FFF9 / SCRIPT=8A1D38A65945CC99C4B7F8EE95FDF4FF744D105303BC9904E5915E630DF58359 / ZIP=2284E6D6FE8FFD38689A357DD0A6653CEB23B923F0C531BF9EAC376178E9A28A
client_evidence: safety_scan_not_skipped / no_non_high_risk_auto_install_selected / count_3 / workbuddy-skill-1787379691395 / SKILL_MD_NO_METADATA_NAME / body_first_line_match
native_read_and_path: SKILL_MD_AND_scripts\\r01_contract_probe.py_READ / physical_install_path_exposed_contract_deviation / full path not reprinted as authority
frozen_attempt: SESSION_WORKSPACE_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER / relative=.\\scripts\\r01_contract_probe.py / no_cd_no_absolute_no_guessing_no_command_mutation / Skill-root-and-bundle-relative=NOT_EXPOSED
result: UI_USER_CANCELLED / POWERSHELL_NOT_STARTED / NO_SCRIPT_STDOUT_STDERR_FINAL_EXIT_CWD_TIMEOUT / BLOCKED_EXTERNAL_CONTRACT / NOT_BECAUSE_POWERSHELL_IS_NON_NATIVE
review_chain: APPROVE_P0=0_P1=0_P2=0 / nonzero=NOT_RUN / timeout=NOT_RUN / R02-R08=NOT_STARTED_NOT_AUTHORIZED
reviewer_independent_observation: WORKBUDDY_5.3.14 / HY3 / USER_CANCELLED / NO_SUCCESS_STDOUT_STDERR_EXIT_CWD / COORDINATOR_OBSERVATION_NOT_INDEPENDENTLY_VISIBLE_TO_REVIEWER
package_registration_state: UNTOUCHED / NO_REGISTRATION / NO_ACTIVATION / NO_LOCATOR / NO_PACKAGE / NO_INSTALLER
temporary_skill: UNINSTALLED / USER_UNINSTALLED_TEMPORARY_SKILL / TEMP_SKILL_ID=workbuddy-skill-1787379691395_NOT_IN_INSTALLED_LIST / WORKBUDDY_MY_INSTALLED_SKILLS_2=agent-browser,find-skills / TASK_HISTORY_RETAINED / BASELINE_SKILLS_UNTOUCHED / SOURCE_AND_ZIP_DELETED / PATH_NOT_FOUND
computer_use_transparency: LOW_IMPACT_OPERATIONAL_ANOMALY / EXPLORER_MISTAKEN_FOR_FILE_PICKER / ALT+N_MAY_OPEN_TAB_OR_WINDOW / NO_PATH_INPUT_NO_FILE_SELECTION_NO_WRITE_DELETE / STOPPED_RECOVERED
```

该候选不改变 Stage 2 `PASS_ACCEPTED` 或 Stage 5 `IN_PROGRESS / ENTRY_CODE_COMPLETE / REAL_INTEGRATION_INCOMPLETE`，不创建或启动 Provider、媒体、Stage4、Stage6、生产 Package 或生产 Registration。

## Current Stage 5 R01 acceptance-contract correction1 and Stage 2 boundary (2026-08-22)

The original R01, Sandbox Refresh1, and Expert Entry Feasibility records are `HISTORICAL / SUPERSEDED_ACCEPTANCE_CONTRACT`; their old blocked/incomplete outcomes remain preserved. This user-authorized correction does not reopen or change the accepted Stage 2 Registration/Activation/Locator contract and is not new official evidence.

```text
r01_acceptance: ENTRY_SURFACE_ACCEPTED / EXECUTION_PROOF_DEFERRED_TO_R03_R07
r01_surface_evidence: SKILL_PACKAGING / UPLOAD / INSTALL / IDENTITY_APPEARED / SELECTION_HIT / CLIENT_SANDBOX_SCRIPTS / POWERSHELL_ELIGIBLE_CANDIDATE_SURFACE
deferred_execution: LOCATOR -> FIXED_POWERSHELL_OR_PRIVATE_CLI -> LAUNCHER_RECEIPT / IMPLEMENTATION_AND_REAL_PROOF_DEFERRED_TO_R03_R07 / NOT_CURRENTLY_PROVED
no_overclaim: NO_SCRIPT_STDOUT_STDERR_EXIT_CWD_TIMEOUT_OR_LAUNCHER_RECEIPT_CLAIM / NO_FINAL_PACKAGE_OR_REGISTRATION_CLAIM / NOT_STAGE5_PASS
hy3_policy: CURRENT_TEST_MODEL_ONLY / COST_AVOIDANCE / PRODUCT_MODEL_NEUTRAL / USER_SELECTED_MODEL / NOT_A_SKILL_OR_EXPERT_OR_SYSTEM_DEPENDENCY
stage_2_boundary: REGISTRATION_ACTIVATION_LOCATOR_CONTRACT_UNCHANGED / NO_PACKAGE_OR_PRODUCTION_REGISTRATION_SIDE_EFFECT
current_task: NONE / NO_ACTIVE_TASK / R01_CORRECTED_ACCEPTED_ENTRY_SURFACE
next_authorized_task: V2-S5-R02-PACKAGE-RELEASE-TOOL-DEFINITION-BINDING1 / R02_AUTHORIZED_ONLY / R03-R08_NOT_AUTHORIZED
```

The single WorkBuddy Skill/user-entry, fixed internal CLI bridge, no arbitrary CLI/path guessing/scan/PATH fallback/MCP/second Skill/second Agent/router/retry/replay, and Installer-stamped final Skill locator boundaries remain unchanged. R03/R07 own the later implementation and real execution proof; this correction creates no Package, Registration, Locator, PowerShell process, private CLI run, Provider, media, Stage 4, Stage 6, or production state.
