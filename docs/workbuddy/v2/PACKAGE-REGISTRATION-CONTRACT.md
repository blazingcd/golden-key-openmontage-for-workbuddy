# OpenMontage Package Registration and Locator Contract

状态：`REQUIRED_TOOLCHAIN_REFRESH / REVIEW_READY`

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

## 5. Exact refresh evidence

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

This evidence does not prove Installer, Stage 3 optional capabilities, Launcher, real WorkBuddy, Provider, media, SaaS, network production, or business E2E.
