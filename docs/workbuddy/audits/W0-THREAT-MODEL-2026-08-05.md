# W0 Repository Threat Model

## Overview

Golden Key OpenMontage for WorkBuddy is a Windows-first, locally operated video-production distribution. It combines the verified `golden-key-v0.3.21` WorkBuddy Callable Core Release export with a WorkBuddy adapter. WorkBuddy is the only upper-level Agent; the export supplies declarative Pipeline manifests, Stage Skills, Schemas, Checkpoints, Artifacts, the Tool Registry, and deterministic tools. Golden Key SaaS and the non-callable Agent Host layer are not product, synchronization, or runtime dependencies.

The public-release audit protects the future public repository as well as local users who may run tools against untrusted prompts, media, URLs, project files, and provider responses. The repository is not yet authorized for public push, and no real or paid Provider is authorized during W0.

## Threat Model, Trust Boundaries, and Assumptions

Assets and invariants:

- Provider credentials, tokens, internal endpoints, local paths, customer/SaaS data, and unpublished configuration must not enter the public repository, logs, errors, or generated evidence.
- User-selected files and project workspaces must remain inside authorized roots; deterministic tools must not silently broaden file or network access.
- Canonical Artifacts, Schemas, Reviews, Checkpoints, approval gates, and append-only decision history must not be bypassed or forged.
- The external ZIP SHA, embedded/external lock, per-file hashes/modes, required/forbidden paths, managed scope, and bundle digest must all verify before mirroring.
- WorkBuddy-owned files, especially `requirements.txt` and `setup.py`, must not be overwritten or deleted by the Core contract.
- WorkBuddy must remain the only upper-level Agent. The Agent Host authority, model-driven host, compatible transport, and their tests must remain absent and must not be reimplemented.
- Pipeline choice and creative decisions stay with WorkBuddy plus the authoritative Manifest/Skill chain. MCP exposes only deterministic checks, reads, validation, bounded persistence, tool execution, status, and cancellation.

Trust boundaries and actors:

- Untrusted user or third-party input: prompts, URLs, media, documents, project metadata, filenames, archives, subtitles, and reference content.
- Operator-controlled input: provider credentials, local configuration, approval decisions, installation choices, and selected output roots.
- External systems: public Git remotes, optional media/provider APIs, package registries, websites, and downloaded executables or models.
- WorkBuddy-to-local-core boundary: natural-language planning crosses into deterministic MCP/tool calls and schema-governed persistence.
- Core-to-provider boundary: selectors and provider tools may send data over the network only after explicit user approval and must not expose credentials.
- Maintainer release boundary: WorkBuddy consumes only immutable Release assets; private Golden Key Core history and non-exported files never enter the public candidate.
- Golden Key SaaS boundary: read-only lock verification is allowed for maintainers; SaaS code, data, Worker processes, and runtime services are out of scope and must remain disconnected.

Assumptions:

- The local operator controls the machine and repository checkout, but project inputs and external responses can be malicious.
- GitHub and package/provider endpoints are external systems; network availability does not authorize publishing, paid use, or additional data disclosure.
- Test fixtures and examples are public-release content and therefore require the same secret, privacy, brand, asset, and license review as production code.
- Optional Backlot UI and local servers may expose user project data if bound beyond localhost; exposure must be verified from code and configuration rather than assumed.

## Attack Surface, Mitigations, and Attacker Stories

Primary surfaces:

- Python CLI, MCP, Backlot/local HTTP services, project/artifact readers, schema validators, checkpoint persistence, and tool execution entry points.
- Media and document analyzers, URL/download tools, archive or parser paths, output-path handling, subprocess construction, and provider response parsing.
- Environment-variable and `.env` handling, logs, exception messages, sample configuration, fixtures, and audit artifacts.
- Git synchronization scripts, tag/commit validation, protected-path ownership checks, release manifests, and installer/build scripts.
- Front-end rendering of user-controlled Artifact data, subtitles, filenames, logs, and project metadata.

Relevant attacker stories include command injection through tool parameters; path traversal or overwrite through crafted output paths; malicious ZIP members; forged lock/hash/mode entries; managed-scope overreach that deletes consumer files; SSRF or unsafe downloads; XSS; parser resource exhaustion; credential leakage; approval/Schema/Checkpoint bypass; direct Git sync that bypasses the Release contract; and an adapter that starts a SaaS Worker or nested Agent model call.

Existing mitigations include BaseTool contracts and registry discovery, manifest-scoped tool lists, JSON Schemas, fail-closed Checkpoints, explicit human gates, lock-managed exact mirroring, six fixed removal paths, consumer ownership checks, idempotency tests, no-provider W0 restrictions, and the frozen Skill/MCP separation. Documentation alone is not proof; W0 requires Release verification, static checks, contract tests, publication scans, and a runtime network-denial test design.

Out-of-scope stories are attacks requiring a malicious local administrator who can replace the checkout or runtime, and vulnerabilities that exist only in the separate Golden Key SaaS product with no imported or invoked WorkBuddy path. Such SaaS evidence becomes relevant only if the adapter introduces a dependency or release artifact.

## Severity Calibration (Critical, High, Medium, Low)

- Critical: public release of a live privileged secret; unauthenticated remote code execution on a normally exposed service; or a default runtime path that silently invokes an external model/provider with broad user-data access and no approval.
- High: reachable command injection, arbitrary file overwrite/read outside authorized roots, material credential disclosure, approval/checkpoint bypass leading to consequential provider execution, or an actual WorkBuddy runtime dependency on the private SaaS Worker.
- Medium: localhost-only XSS with meaningful project-data impact, bounded SSRF, incomplete redaction, unsafe defaults that need user setup, or a release-governance bypass requiring maintainer action but capable of publishing unreviewed core content.
- Low: limited information disclosure without secrets, denial of service with easy recovery, ambiguous public asset/brand provenance, or documentation/config examples that create a realistic but non-immediate unsafe setup.

Baseline: `golden-key-v0.3.21` / `golden-key-workbuddy-callable-core-v1`
Publication lineage: public `origin/main` plus verified export and WorkBuddy-owned increments
