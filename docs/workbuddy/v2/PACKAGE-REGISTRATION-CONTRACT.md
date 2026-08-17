# OpenMontage Package Registration and Locator Contract

状态：`V2-S2-OFFICIAL-PACKAGE-ALIGNMENT / REVIEW_READY`

## 1. Scope

Stage 2 binds one explicitly supplied official OpenMontage Git checkout to an
immutable local registration and locates the single explicitly activated checkout.
It does not scan disks, infer a package from a directory name, choose "latest",
fetch or update Git, install dependencies, create a Python environment, execute
OpenMontage, or modify the checkout.

The public entries are:

```python
register_package(data_root, package_root, expected_origin_url, expected_commit)
activate_package(data_root, expected_active_pointer_sha256_or_missing, registration_sha256)
recover_active_package(data_root, expected_broken_pointer_sha256, replacement_registration_sha256)
locate_active_package(data_root)
```

Registration validates and publishes an immutable object but does not activate it.
Activation is an explicit compare-and-swap (CAS). Recovery replaces only an
explicitly hash-locked broken pointer with an explicitly named valid registration.
Locator is offline, read-only, and performs complete revalidation without repair or
fallback selection.

## 2. Fixed v2 identity and storage

```text
registration schema: golden-key-workbuddy-openmontage-git-registration-v2
registration owner: golden-key-workbuddy-shell-v2
active pointer schema: golden-key-workbuddy-active-openmontage-package-v2
active lock schema: golden-key-workbuddy-active-package-lock-v2
official origin: https://github.com/calesthio/OpenMontage.git
guide path: AGENT_GUIDE.md
registry path: <DataRoot>/State/PackageRegistration/v2
object path: <registry>/objects/<registration_sha256>.json
active pointer: <registry>/active.json
active lock: <registry>/active.lock
```

`PackageRegistration/v1` is a different historical schema. Stage 2 does not read,
activate, repair, import, or automatically migrate v1. The current deployment has no
real v1 registry; a future migration, if ever authorized, requires a separate task
and explicit evidence.

## 3. Explicit inputs and Git command boundary

All four registration inputs are mandatory. `data_root` and `package_root` must be
existing canonical absolute directories. PackageRoot must itself be the exact Git
worktree top level, not a parent, nested directory, symlink, junction, reparse alias,
or guessed location.

`expected_origin_url` is normalized only to the fixed official HTTPS URL (an omitted
terminal `.git` is accepted); other hosts, owners, repositories, schemes,
credentials, ports, queries, fragments, and case-different repository paths fail
closed. `expected_commit` is an explicit lowercase 40-hex commit. The Shell never
resolves a branch or tag into a preferred commit and never selects "latest".

Every Git call uses a fixed argument list, `shell=False`, captured byte output, an
explicit 10-second timeout, and an explicit exit-code check. Output must be UTF-8 and
NFC where text is expected. `GIT_OPTIONAL_LOCKS=0`, `GIT_TERMINAL_PROMPT=0`, and
`GCM_INTERACTIVE=Never` keep identity reads non-interactive and prevent optional Git
index refresh locks. A timeout, non-zero exit, malformed output, or non-UTF-8 output
fails closed. Stage 2 never invokes `fetch`, `pull`, `push`, `clone`, or `ls-remote`;
online comparison with official remote HEAD is external takeover-gate evidence.

## 4. Checkout and inventory validation

Registration and every later activation, recovery, and locate operation revalidate:

- PackageRoot is the exact independent Git worktree root;
- normalized `remote.origin.url` equals the fixed official URL and the explicit
  expected URL;
- `HEAD^{commit}` exactly equals the explicit expected commit;
- `HEAD^{tree}` is recorded as the Git tree identity;
- `git status --porcelain=v1 -z --untracked-files=all --ignored=no` is empty;
- `git ls-tree -rz --full-tree HEAD` exactly supplies the fixed tracked inventory;
- each inventory path is unique under Windows case aliases, canonical, relative,
  traversal-safe, ADS-safe, and free of reserved names or trailing-dot/space aliases;
- every entry is a regular Git blob with mode `100644` or `100755` and resolves to a
  regular file without symlink, junction, or reparse traversal;
- every tracked file records its path, Git mode, byte size, and working-tree SHA-256;
- the canonical complete entry array records a file count and inventory SHA-256;
- `AGENT_GUIDE.md` exists, is tracked by the same inventory, is non-empty, and records
  its path, mode, size, and SHA-256.

Tracked modifications, staged changes, deleted tracked files, and untracked files are
all dirty and rejected. Ignored files are explicitly allowed, excluded from the
registration inventory, and do not contribute identity; they cannot replace or
shadow any tracked inventory entry. This ignored-file policy is fixed, not inferred
per checkout.

The Guide bytes are used only to compute identity after PackageRoot, origin, HEAD,
tree, and clean-state validation. Stage 2 does not interpret the Guide. A downstream
authorized session consumer may read it only after successful Registration/Locator
identity validation.

## 5. Immutable registration and Locator result

The closed registration object has exactly:

```text
schema_version, owner, package_root, origin_url, openmontage_commit,
git_tree, inventory, guide
```

`inventory` has exactly `file_count`, `sha256`, and `entries`; each entry has exactly
`path`, `git_mode`, `sha256`, and `size`. `guide` has exactly `relative_path`, `path`,
`git_mode`, `sha256`, and `size`. Canonical object bytes are UTF-8 without BOM, sorted
keys, compact separators, and exactly one trailing LF. The SHA-256 of those bytes is
the object filename and returned `registration_sha256`.

Locator returns an immutable mapping containing exactly:

```text
registration_sha256, package_root, guide, origin_url, openmontage_commit,
git_tree, inventory
```

The Locator inventory result exposes its immutable `file_count` and `sha256` identity;
the complete entries remain in the content-addressed registration object. Locator
does not return Release, Manifest, Lock, bundled Python, or `package_python` pseudo-
identity. It performs no write, network access, Git update, repair, process launch,
or fallback enumeration.

## 6. Publication, lock, CAS, and recovery

Registration objects remain content-addressed and immutable. Publication uses a
same-directory temporary file, flush, `fsync`, readback, and atomic hard-link
publication; identical bytes are idempotent and conflicting bytes at one content
address fail closed.

`active.lock` is a persistent fixed-identity file. Initialization is allowed only for
an empty v2 registry. Writers share one process guard and an exclusive kernel byte-0
lock with one monotonic five-second deadline. Inside the critical section they
revalidate the lock, pointer, and explicit target; write, flush, `fsync`, and read back
a same-directory temporary pointer; repeat the raw-byte CAS; and publish with
`os.replace`. Failures before replacement preserve the prior pointer.

Recovery requires the exact SHA-256 of an existing damaged pointer and an explicit
valid replacement registration. It does not accept a missing or valid pointer,
create a registration, choose another object, or silently repair. Rollback is an
explicit CAS activation of a named older valid object.

## 7. Fail-closed errors

Stable codes are:

```text
INPUT_INVALID
PATH_VIOLATION
OBJECT_MISSING
DUPLICATE
IDENTITY_MISMATCH
HASH_MISMATCH
TAMPERED
GIT_COMMAND_FAILED
GIT_TIMEOUT
GIT_OUTPUT_INVALID
ACTIVE_LOCK_BUSY
ACTIVE_CAS_MISMATCH
ATOMIC_WRITE_FAILED
```

Unknown or missing fields, duplicate JSON or inventory paths, invalid Unicode,
unsafe paths, symlink/reparse traversal, dirty status, Git identity drift, file
hash/size/mode drift, pointer/object/lock tampering, stale CAS, and publication
failure all reject without guessing or state repair.

## 8. Explicit non-goals and evidence boundary

The official checkout is registered without adding Golden Key Manifest/Lock files and
without requiring `BUNDLE-MANIFEST.json`,
`GOLDEN_KEY_WORKBUDDY_CORE.lock.json`, or `bootstrap/python/python.exe`.
Registration never creates a venv, downloads packages, or runs OpenMontage.

Package Python, Runtime preparation, Launcher, WorkBuddy Entry, Relay, status/result
handoff, Provider, Pipeline, media, and production control belong to Stage 3 or later
separately authorized modules. Their implementation authorization remains
`NOT_GRANTED`. Passing this contract proves only Stage 2 registration/locator behavior;
it does not prove installation, Runtime, real WorkBuddy, OpenMontage production,
Provider, network, media, SaaS, or business E2E.
