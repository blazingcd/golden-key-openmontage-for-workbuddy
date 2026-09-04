# WorkBuddy Shell V2 — Current Project State

Date: 2026-09-04

The live authority is `docs/workbuddy/v2/TASK-REGISTER.md`. This file is a compact
state snapshot, not a second task ledger.

## Current route

The latest v8 Skill completed the base connection gate in one real WorkBuddy task:
WorkBuddy called `locate_active_package` and completed reading the exact verified
Package `AGENT_GUIDE.md`. R3, M0, M1.1, and M1.2 remain unchanged. This result does
not prove Remotion installation, API-key configuration, M1.3, or a portable final
user release.

The v8 implementation closeout is complete at implementation commit
`13ea01cee6d4bf6ccdb0ec2533b907762b9774fe` and merge commit
`9459a13f46655a3c46db04385906c9b2775001ec`. Its independent zero-write review is
`APPROVE / P0=0 / P1=0 / P2=0`; local, tracking, and advertised refs match and the
M1 worktree is clean. The minimum product mainline now starts with the independent
Must prerequisite
`Installer / Release Assembly`, followed by M1.3 real local/API-key configuration
using that formal release, then M1.4 closeout. M2 may proceed independently because
M1.2 is complete; M3 still waits for M1.4 and M2.

## Product

An ordinary user writes a natural-language request in WorkBuddy containing
`金钥匙智能体`. WorkBuddy is the only Agent and production decision-maker. The
OpenMontage Package supplies production semantics. Shell V2 supplies Golden Key
application lifecycle, Registration/Locator, fixed mechanical invocation, and
status/result relay. The Skill guides optional configuration; WorkBuddy performs
its live inspection, consented installation, rediscovery, and verification. Shell
is never a second control plane.

WorkBuddy is a harness Agent: the same input may yield different internal thoughts,
tool paths, steps, wording, and intermediate conclusions. Skills and prompts must
not force a preset internal script. Acceptance follows the user's observed result;
process variation is acceptable unless it causes product failure, technical burden,
a second control plane, or a false result.

Future WorkBuddy executions prefer any available `0.00x` model row. Waiting may
switch among `0.00x` rows. A positive multiplier is allowed only when every
`0.00x` row is unavailable, and is selected from the smallest upward. Record the
chosen row and, for any non-`0.00x` choice, the unavailable `0.00x` evidence.

## Four results

| Result | Current state | Evidence / next boundary |
|---|---|---|
| 1. Installable Shell | `COMPLETE` | Commit `869358810ee41a0a61d10cec10c1b3b93c2c3450`; tree `3a623cb1eab9fee0d90854c0df271450f9779b9a`; Release SHA256 `7e5585298e50a5c5713ecd8fc4df57cfb6e88381b39453364cec62fdea1c6280`. Lifecycle and data protection passed. |
| 2. WorkBuddy natural-language result | `COMPLETE` | WorkBuddy `5.3.14` / Hy3; exact ordinary request ran through the single Skill and Shell and returned a concrete business reply plus LauncherReceipt. |
| 3. Playable Golden Key video | `COMPLETE` | WorkBuddy 5.3.14 / `Hy3 0.00x` displayed and played a real 46.6-second MP4; independent review `PASS / P0=0 / P1=0 / P2=0`. |
| 4. Formal closeout | `COMPLETE` | Frozen 11-path candidate passed `APPROVE / P0=0 / P1=0 / P2=0`; reviewed commit `70cf63be51774de9151fb0fee24cf78591ff1993` was fast-forwarded and pushed, followed only by the Owner-authorized completion record. |

Result 2 evidence: Skill ZIP SHA256
`c96ec03522b744e8771eb16f22f5521102c4007af50ccb27d895efb82b1fe3a6`; evidence
root `D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\evidence\product2-workbuddy-user-flow-20260826`.
The receipt's `INCOMPLETE / RESULT_POINTER_INVALID` means no video file was made
in that run. It is a Result 3 artifact condition, not a Result 2 failure.

## Repository state

The completed historical delivery target is
`refs/heads/codex/workbuddy-shell-v2` at
`aa9cabfa0d4f75d93e22317466709b6bad3bc3b4`. It is retained unchanged as the
R1-R4 baseline. The authorized next-phase documentation branch is
`refs/heads/codex/workbuddy-capability-onboarding`, created from that exact commit.
That branch creation record alone authorized no implementation. The later exact
two-file implementation authorization is recorded below; it still excludes a
WorkBuddy run, media production, and capability installation.

## Current task

At preparation start, planning local/tracking/advertised refs were
`e0aab40b4500e70d63b058df2d9731415e30fe0d`. The retained implementation branch
was clean at local `fd0a3f8cac41540ff25a3dd113828c7a5f39f7a6`, two commits ahead
of tracking/advertised `33f49fb385b103489772d3f8ce2f7cb2486b08dc`. Historical
baseline local/remote remains
`aa9cabfa0d4f75d93e22317466709b6bad3bc3b4`.

The historical factual-relay PackageRoot is retained read-only at
`D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\m1.2-final-factual-relay-33f49fb-20260829\PackageRoot`.
The current active Registration SHA256
`b726ff695ad2171048f5048d390a5ae27740715680889bad2c613ada97c08bfe`
points to
`D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\m1-package-slim-candidate-20260829\PackageRoot`;
its `fixed_child.py` SHA256 remains
`66defdd34ea984b4b2ccf6d79753f90bf1c45f4b387f226552035c4e2ae136bf`.
Do not rebuild, reregister, or reactivate either retained root in this correction.

The consumer candidate was built at
`D:\BlazingCD\Personal\GoldenKeyData\WorkBuddyShellV2\data\production\Integrations\WorkBuddy\golden-key-openmontage-0.3.25-m1.2-handoff-consumer-33f49fb.zip`,
SHA256 `437b02c60aa234197fb419275ac64c5df804c5f477fdba16fde3278f772e68d2`.
Its independent zero-write review passed `APPROVE / P0=0 / P1=0 / P2=0`; the
single Skill source commit is `c8eeb91e221ec96a406543c183091eea7ea6ac3c`.
After the Owner manually uninstalled the old same-name Skill, this candidate was
installed as the only Golden Key Skill. One WorkBuddy 5.3.14 / `Hy3 0.00x`
readiness probe produced an `EXITED_SUCCESS` receipt, valid result pointer, one
spawn and no retry against the active final PackageRoot and `fixed_child.py`
SHA256 `66defdd34ea984b4b2ccf6d79753f90bf1c45f4b387f226552035c4e2ae136bf`.
The factual summary reached the dialogue; no Provider/renderer was selected, no
production decision or media occurred, and the task workspace was empty after
WorkBuddy removed its temporary parsing scripts.

The independent user-result review is `REJECT / P0=0 / P1=3 / P2=0`. WorkBuddy
incorrectly described Remotion as ready, exposed environment-variable mechanics,
and did not clearly offer all four continue/local/API-key/defer choices. Read-only
inspection confirms OpenMontage does integrate Remotion source, adapters, and a
`4.0.484` dependency lock, but the active Package lacks
`remotion-composer/node_modules`; it is integrated, not runtime-ready or
invocation-verified. The Owner then authorized a minimal Skill consumer correction,
six-document synchronization, independent zero-write reviews, ordinary commits
and pushes, and one newly named uninstalled candidate. Another WorkBuddy probe,
installation, Package mutation, Provider/secret/media action, and M1.3 remain
unauthorized.

The correction is pushed at
`5229964ac681d7b34949480326e6f24a0c53913f`. The corrected candidate ZIP,
SHA256 `116737071d377b67dff6ea93fe18534114c17e762d32116efc5c4b973e000228`,
passed independent zero-write review `APPROVE / P0=0 / P1=0 / P2=0` and remains
uninstalled. At that historical checkpoint it was preparation evidence only; the
rejected M1.2 user result was unchanged until a separately authorized WorkBuddy
retest passed.

The bounded package-size checkpoint is complete and pushed on the M1 branch at
`d94d90c486f1d72452a6f65b71b7c2e7c55f1d04`. At that checkpoint, the then-active
PackageRoot and Release remained unchanged. The separately named successor ZIP
is 177,241,928 bytes
(169.03 MiB), SHA256
`0d71485772c6afd59b925c1ef9012a3b320ccf1dcbe398b6edb1abfb0f02c7ab`; its
PackageRoot is 463,051,387 bytes. Compared with the active package, this saves
40,291,428 compressed bytes and 115,942,206 expanded bytes. It removes only
unused FFmpeg `ffplay.exe` and HTML documentation and retains ffmpeg, ffprobe,
licenses, README, and presets. Focused checks passed `18 passed, 1 skipped`, the
independent review returned `APPROVE / P0=0 / P1=0 / P2=0`, and the exact task
temporary directory was removed. The later final-readiness sequence registered
and activated this exact slim PackageRoot; it is the current active root recorded
above.

Direct base-Package Remotion bundling is rejected under the Owner's 80 MiB
compressed-increment ceiling. The machine's external Remotion 4.0.507 core/CLI
measures 66.64 MiB as a level-9 ZIP but is neither the Package's locked 4.0.484
project tree nor a complete renderer; the locked Chrome Headless Shell archive is
115.33 MiB by itself. M1.3 therefore retains managed, consent-controlled
on-demand installation. This checkpoint does not complete M1.2, start M1.3, or
authorize WorkBuddy, Skill installation, activation, credentials, Provider calls,
or media.

The later semantic-correction candidate is implementation commit
`a884124718eab4bcdb0f98c59ae67acc7008f2fd` and ZIP
`golden-key-openmontage-0.3.25-m1.2-semantic-correction-20260830.zip`, SHA256
`c2b91d30aade188a133626b578e976857a10abd57f3f24efd4100bab2820f293`.
It was the only installed Golden Key Skill for one WorkBuddy 5.3.14 / `Hy4
preview 0.00x` task at 19:50 local time. Its installed `SKILL.md` SHA256 is
`1dfdb2f24758aaf97560c035a01310987709ad202d307c35c9e27642802b40c0` and
`run.ps1` SHA256 is
`bfe8692bac206c556274013a1be25f544985329d3203e552145edf003fd5a190`.
LauncherReceipt SHA256 is
`2da272dac5e5326c6d784fbdc867ffb1f5c413cc1e4aa1938f392df5f6274e87`;
the valid managed handoff SHA256 is
`cbf32ae738d42346381ec41f465d7cf52a360a149dbdaf7779ce29eb72cf26c5`.
The run exited successfully with one spawn, no retry, no media, no Provider or
renderer selection, and no production decision. Its exact task directory
`C:\Users\blazi\WorkBuddy\2026-08-30-19-50-10` is empty.

The dialogue proved the factual relay, continuing FFmpeg baseline, and all four
choices. At that historical checkpoint, independent review returned
`REJECT / P0=0 / P1=3 / P2=0`: partially configured groups were shown as ready,
the first-use result expanded a broad Provider/configuration catalogue, and
Remotion/HyperFrames were not separately explained across source integration,
project dependencies, runtime readiness, and real invocation verification. The
result was recorded as `NOT_PROVED`; the later Owner correction below supersedes
that product classification without changing the raw evidence.

The subsequent compact-readiness implementation is commit
`666c9d4cdbbc0a2aeb57c0b94598f4501e246c4f`; its candidate ZIP is
`golden-key-openmontage-0.3.25-m1.2-compact-readiness-20260830.zip`, SHA256
`4caf57cfcf5d298f0ded1098d4fda5bb482a699f57a72b02bc61f1cd3dbf2dd1`.
The one later WorkBuddy result still exposed npm/registry/runtime details,
unrelated HTML/CSS/GSAP and other capability descriptions, and the large video/
TTS catalogues. Independent review rejected that ordinary-user result with
`REJECT / P0=0 / P1=1 / P2=1`. The
managed handoff was 26,809 bytes; its `package_capability_summary` was about
25.95 KB and contained 24 capability rows plus 63 setup offers. Tightening Skill
wording did not make the over-broad fact surface stable.

The Owner therefore superseded the next Skill-only correction with a
documentation-only product-flow reset. That task changed only the six authority/
state documents, obtained one independent zero-write document review, committed
once, and ordinarily pushed the planning branch. It did not merge into the M1
implementation branch, modify Skill/Shell/Package/tests, build or install a
candidate, run WorkBuddy, configure anything, call a Provider, produce media, or
start M1.3.

The Owner's latest correction judges M1.2 by whether the ordinary user learns that
the FFmpeg basic path is usable now, is explicitly introduced to Remotion,
HyperFrames, external AI image/video, and TTS, and receives understandable entries
to continue or configure. The latest run proved that core result. Remotion/
HyperFrames four-layer facts remain internal truth. A small relevant Provider set
is still the preferred default after an online category is selected—normally two
or three image/video choices or one or two TTS choices—but the count is not a hard
acceptance threshold. Extra relevant declared choices are a UX issue, not proof
that the configuration entry failed. Optional installation, chat secrets,
Provider/connection calls, media, M1.3, Shell fallback, retry, source repair,
workspace relay files or managed-summary copies, old-root edits, and historical-
asset overwrite remain forbidden in this documentation task. False readiness,
secret exposure, a blocked FFmpeg path, unusable configuration entries, internal-
command burden, unsafe mutation, or Shell-owned choice would be a real M1.2
failure; catalogue length or technical wording alone is a UX finding. This latest
classification correction has the same documentation-only boundary.

The rejected v2 candidate ZIP SHA256 is
`bd35b98087cd7a03f909dc17bbd6048388a7c46e2251c3893a3f9f056d653249`.
The preserved baseline ZIP and byte-identical `r3-pass-baseline` copy still have
SHA256 `e7ecfd69a22b2f601215860a83f849584c50f29328c011622a42fdd2e63d4bab`.
The v3 candidate built afresh from that baseline has ZIP SHA256
`aa421dfbb00111392d37da6f6590e456b534a79e308560b441b4afd5d7b044a2`. Its only
WorkBuddy `5.3.14` / `Hy3 0.00x` comparison produced a managed first-call
`EXITED_SUCCESS` receipt with a valid result pointer, one spawn, and no retry.
WorkBuddy created a valid 37-second 1920x1080 H.264/AAC MP4 at
`C:\Users\blazi\WorkBuddy\2026-08-28-13-33-53\头头象花浴头疗_新店开业宣传.mp4`,
but planned an unrequested workspace-memory update and another user Skill before
the final reply. The task was stopped. Final UI state is `用户已取消` with no
artifact card or final path; independent result review is `TODO`. An empty new
workspace-memory file remains, no extra user Skill was created, and v3 was the
only installed Golden Key Skill at that historical comparison point.

Fresh Owner authorization permits a separately named `delivery-v4` candidate
derived from v3 while preserving the R3 baseline and v3 archives. V4 changes only
the WorkBuddy result-delivery stop boundary and retains the proven v3 receipt
relay. Its built ZIP SHA256 is
`d838cba0735d7a2df3d81029a7d7469551a28219d91f0e8ea2fe08b0f152845d`.
Focused checks passed and the one independent zero-write candidate review returned
`APPROVE / P0=0 / P1=0 / P2=0`.

The one action-time-authorized WorkBuddy `5.3.14` / `Hy3 0.00x` comparison is
complete. The first call returned `EXITED_SUCCESS`, a valid result pointer, one
spawn, and no retry. WorkBuddy gave a final answer and attached the 9.6 MB MP4 at
`D:\BlazingCD\Personal\测试素材\头头象花浴头疗素材\成片\头头象花浴头疗_新店开业宣传.mp4`.
The independent result review is `TODO / P0=0 / P1=1 / P2=0` because the closing
title is clipped. V4 is not accepted as the stability solution: WorkBuddy wrote
an optional 978-byte workspace memory before the final answer. No extra user
Skill was created. The Owner retains v4 for its improved first-call and
final-delivery mechanics; the clipped output from one harness run is not treated
as a Skill regression. The preserved R3 baseline remains rollback evidence.
Historical Result 3 and the formal Result 4 closeout are complete under the frozen
plan in the Task Register.

## Next-phase planning

M0 freezes the complete next-phase master roadmap and the execution contract for
the first Must task on `codex/workbuddy-capability-onboarding`. It records the
evidence gap, dependency order, read-only route boundary, user-visible acceptance,
anti-inflation stops, review method, and the gate that requires the Owner to
confirm both the implementation branch name and exact write allowlist after the
route audit. At the M0 freeze, no implementation branch existed; the later M1
branch history is recorded below.
The initial capability-onboarding contract remains preserved at
`4c0cbd3447546c3dcc0079f2392a3b43e7542e69`; the later Owner authorization adds
one documentation-only master-roadmap amendment without rewriting that commit.

`R1` through `R4` remain frozen historical result identifiers; no future task uses
the R series. M1–M3 are Must tasks, S1–S5 are Should tasks, and C1–C2 are Could
tasks. M1.1–M1.4 are steps within M1, not M0 subtasks.

The next product path begins with capability readiness, not a claim that
OpenMontage becomes incapable when an enhancement is absent. FFmpeg is the basic
production baseline. Verified first-use facts reach WorkBuddy, which tells the
ordinary user that basic production is ready when FFmpeg is ready, and
explicitly presents Remotion and HyperFrames as optional local enhancements and AI
image/video and TTS as optional online enhancements that may be configured now or
later. Their internal technical layers are not a mandatory first-use report.

M1 now derives its visible Provider set from the verified Package's formal
declarations. Current static evidence includes Seedance, Kling, and MiniMax.
After a relevant category is selected, the preferred first menu normally contains
two or three relevant image/video choices or one or two TTS choices and offers to
show more. This is a progressive-disclosure default, not an exact pass/fail count.
Undeclared Providers do not appear in M1. This snapshot is
not a Shell routing or ranking table and does not prove credentials, account
permission, balance, connectivity, regional availability, price, or live model
availability.

The configuration journey has two required mechanisms. Local capabilities such
as Remotion and HyperFrames require approved download, managed installation,
rediscovery, Package recognition, and actual Package-mediated invocation. API-key
Providers require a secret-safe input/store path outside ordinary chat, exact
Package allowlisting, non-disclosing relay, and an authorized connection test.
M1.3 must obtain one representative result for each mechanism.

WorkBuddy remains the only conversation and decision owner. It may use its own
current capabilities and the verified Package semantics to decide what is
relevant, explain cost/privacy/credentials, obtain consent, and recover from a
failed optional configuration. Shell runtime preparation remains bounded
mechanical detection and exactly approved integration. Later requests containing
`金钥匙智能体` may inspect, configure, change, or retest the same capabilities:
natural language remains the entry and intent carrier, while WorkBuddy may use a
bounded guided sequence when secure input or reliable installation requires it.
That sequence must not make the user operate internal commands or technical details.

Planned dependency: M1.1 fact audit then M1.2 first-use readiness; M2 may start
after M1.2. After the proved v8 base connection is closed out, the independent
Installer / Release Assembly prerequisite must produce the formal user release
before M1.3 real validation. M1.3 remains a required product capability with
representative local installation and API-key paths, but a particular user may
defer configuration until M2 establishes relevance or continue on FFmpeg without
using an enhancement. M3 starts only after M1.4 and M2 are complete. S1–S4 then cover revision/version/rollback,
one additional platform/aspect, export/share/reuse, and cross-machine lifecycle.
S5 qualifies only an enhancement selected for a real user goal. C1 broad
Provider/model coverage beyond the verified Package's formal declarations and C2
automatic routing/direct publishing remain deferred. Implementation and real-user
acceptance require separate Owner authorization.

Owner authorization dated 2026-08-29 permits only this six-document Provider-scope
correction, one independent zero-write document review, one commit, and one
ordinary push on `codex/workbuddy-capability-onboarding`. It does not authorize
M1.2/M1.3 implementation or any Package, test, WorkBuddy, installation,
credential, Provider-call, or media action.

The Owner's later 2026-08-29 direction authorizes one documentation-only M1.2
execution-contract freeze under the same six-document, one-review, one-commit,
ordinary-push boundary. The future implementation branch name is
`codex/workbuddy-m1-capability-onboarding`; one branch serves M1.2–M1.4 instead
of creating a branch per subtask. This task does not create it or authorize
implementation, tests, WorkBuddy, installation, credentials, Provider calls,
Package changes, or media.

The same Owner direction requires M1 cleanup to be part of completion. After the
reviewed M1.4 result, the M1 head first ordinary-fast-forwards and pushes
`codex/workbuddy-capability-onboarding`. Only after exact refs, clean worktrees,
and absence of unique/unmerged work are verified may the recorded implementation
worktree, local/remote temporary branch, and exact task-owned temporary directories
be removed. Dirty or unrecorded targets, user data, divergence, or a force
requirement stop cleanup as `CLEANUP_BLOCKED`. M1 cannot be `COMPLETE` before the
post-cleanup absence and retained-baseline checks pass.

The Owner accepted the failed probe and authorized a separate zero-write Shell
factual-relay audit. That audit is complete with
`PROPOSE_BOUNDED_SHELL_FACTUAL_RELAY`: the Package already exposes a raw factual
summary, and the existing validated `fixed-child-handoff` is the smallest reusable
carrier. Current evidence proves the raw summary is too broad for first-use
display. No implementation or test occurred in the audit.

The Owner's earlier relay-only direction authorized this six-document
status/contract update, one independent
zero-write document review, one commit, and one ordinary planning-branch push,
followed without another approval pause by the exact two-file implementation in
the retained M1 branch. Only `golden_key_openmontage_workbuddy/fixed_child.py`
and `tests/workbuddy/test_installer.py` may change. Only the focused direct test,
text/scope checks, one independent zero-write implementation review, one commit,
and one ordinary implementation-branch push are authorized. WorkBuddy, Skill
installation/build, optional installation, credentials, Provider calls, media,
M1.3, extra source files, new protocols, and cleanup remain unauthorized within
that relay gate. The later package-size checkpoint is the sole separate
successor-Package exception and does not reopen `fixed_child.py` or WorkBuddy.

Natural-language interaction examples remain planning hypotheses. Real WorkBuddy
evidence may require different wording, tools, or a bounded fixed confirmation
sequence. That variation is acceptable when the ordinary user can still start and
complete configuration without internal technical work and all safety boundaries
remain intact.

### M1.1 accepted fact audit

The Owner accepted the M1.1 factual conclusion. Locator revalidated the registered
PackageRoot and FFmpeg baseline. The Shell already contains bounded Remotion/
HyperFrames preparation, but no production caller uses it; `user_entry` sends an
empty local-capability evidence list, and the verified Package tool definition
declares no required local capabilities or Provider/secret allowlist. Later static
inspection found direct Package routes for Seedance, Kling, and MiniMax. Current
WorkBuddy tools, actual optional-capability
readiness, video/TTS Provider accounts, prices, credentials, balances,
connectivity, regional/model availability, first-use dialogue, natural-language
re-entry, and recovery remain `NOT_VERIFIED`.

M1.1 is `FACT_AUDIT_COMPLETE / OWNER_ACCEPTED / ZERO_WRITE_DEVIATION_RECORDED`.
The deviation is that its independent sub-audit created and removed the exact
temporary file `D:\DevCache\Temp\m11-rg.txt`; the repository stayed clean and the
path was confirmed absent at closeout.

M1.2 is `WORKBUDDY_FACT_RELAY_REACHED_DIALOGUE /
CORE_FIRST_USE_GUIDANCE_AND_CONFIGURATION_ENTRY_PROVED / UX_OVERLOAD_RECORDED /
COMPLETE / M1_3_LOCAL_CONTRACT_COMMITTED_PRODUCT_INCOMPLETE`.
The earlier contract at `f11e7118e2f652b6e0ceb31b1bc88e617dcf8174`, first
discovery probe, and prematurely cancelled probe remain historical failed routes;
they do not define the current result.

The implementation Skill correction is pushed at
`5229964ac681d7b34949480326e6f24a0c53913f`. The pushed factual-relay
ceiling is `33f49fb385b103489772d3f8ce2f7cb2486b08dc`; the pushed Skill consumer
commit is `c8eeb91e221ec96a406543c183091eea7ea6ac3c`. The reviewed consumer ZIP is
the historical candidate used by the rejected probe. Its relay reached the
ordinary-user dialogue, but the result failed acceptance because it misstated
Remotion runtime readiness, exposed configuration mechanics, and omitted two
clear choices. The Owner later manually uninstalled the same-name Skill; the next
execution must still inspect the actual installed state rather than infer it.

The corrected Remotion fact is: OpenMontage source integration exists, the active
Package lacks project-local dependencies, runtime readiness is false, and a real
Package-mediated invocation is not verified. Those four layers remain internal
truth and later diagnostic/configuration evidence; they are no longer mandatory
first-use prose. The latest compact-readiness run reached the user with the core
guidance and entries but also exposed excessive technical/catalogue detail. That
is a recorded UX finding, not an M1.2 blocker. Shell continues to carry mechanical
facts only; WorkBuddy owns explanation and choice. M1.3 now has a bounded local
implementation contract but still requires the missing Package definitions and
separate action-time user-result authorization.

### M1.3 execution-contract state

The Owner has now authorized and frozen the planning contract and smallest
implementation write set only. Current code evidence shows two reusable but
disconnected primitives: bounded Remotion/
HyperFrames detection and consent-bound managed preparation in
`runtime_prepare.py`, and fail-closed exact environment allowlisting plus secret
suppression in the launch path. No production caller currently reaches the local
preparation function; the production entry supplies empty local-capability
evidence and empty Provider environment names. No verified non-chat credential
input/store or Package-owned connection-test path has been found. These are
implementation prerequisites, not proof of configuration.

The completed read-only prerequisite review found that current WorkBuddy 5.3.14's
built-in `library` Skill proves a similar fixed-mode/canonical-stdin script
pattern is supported. Windows native credential UI plus current-user Credential
Manager are the candidate non-chat secret route, and Seedance can be extended
with a formally declared Package-owned read-only connection test. Golden Key has
not yet proved its carrier or credential flow, and that connection test does not
yet exist. An independent minimality review removed
`run.ps1` and `tools/base_tool.py` from the candidate write set. The next
implementation reuses `codex/workbuddy-m1-capability-onboarding` and the exact
write set frozen in the Task Register; the freeze itself is not implementation
authorization. M1.3 state is `PREREQUISITE_ROUTE_REVIEWED /
WRITE_SET_FROZEN / IMPLEMENTATION_LOCAL_CONTRACT_COMMITTED / PRODUCT_INCOMPLETE /
ACTION_TIME_GATES_REQUIRED`.

The first implementation result is Shell commit
`a89e062c5dc0cbfc3fd7b1e430baf61063d58064` and Package commit
`503f09677db36bad0deb74e94b06401f8f94e215`, both pushed and clean. Focused local
checks and the implementation review establish the structured-action, secret-
suppression, WinCred-wrapper, exact environment, and Package `/ping` code paths.
They are not a user-visible configuration result. Package optional-capability
definitions remain empty, so the local route is blocked before any Remotion or
HyperFrames installation; WorkBuddy, real Windows credential behavior, real Ark
authentication, optional installation, rediscovery, and Package invocation were
not run. M1.4 remains blocked by the incomplete M1.3 product result.

The 2026-09-01 local-route audit supersedes the earlier assumption that adding
Package definitions is the next complete prerequisite. Current preparation can
publish fixed downloaded assets, but it cannot install Remotion's locked npm
dependency closure; the Package renderer also looks only under PackageRoot and
cannot use the Shell-managed runtime. The current `../../data/production`
relationship is a development/package relationship, not a real-user Windows
installation policy.

The Owner's 2026-09-02 correction supersedes that Shell-owned route. The Skill
now only supplies rules: current compatible stable version, mainland mirror,
Windows-resolved standard location, consent, and success criteria. WorkBuddy
uses its own available system abilities for live inspection, explanation,
installation, rediscovery, and a real invocation. Old receipts, a global command,
or integrated source are not readiness evidence.

The historical 2026-09-02 candidate changed the authority/entry documents,
`SKILL.md`, the one-file ZIP builder, and directly affected focused tests. That
route produced the later v8 base-connection evidence and is no longer current
implementation authority. The current sequence is the `Current route` above;
M1.3 remains `PRODUCT_INCOMPLETE` and waits for the accepted Installer / Release
Assembly result.

## Non-goals

Do not preserve old route plans, packet/pre-review systems, extra Agents, MCP/
routers, Shell-side renderer/Provider selection, or generic framework work. The
planned WorkBuddy capability inventory and optional configuration entry do not
authorize Shell production decisions or implementation. Git history remains the
place for provenance.
