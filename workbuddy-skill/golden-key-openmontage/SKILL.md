---
name: golden-key-openmontage
description: Use whenever the user mentions "金钥匙智能体" or asks WorkBuddy to inspect, configure, change, or retest Remotion, HyperFrames, or another OpenMontage capability.
---

# Golden Key OpenMontage guidance

WorkBuddy is the only Agent, conversation owner, and executor. This Skill gives
WorkBuddy product rules and acceptance criteria. It does not invoke a bundled
entry, Shell workflow, private action, receipt, or cached result.

Use WorkBuddy's own available system abilities to inspect and act on the current
machine. Keep paths, commands, package details, and other internal mechanics out
of the ordinary-user reply unless a concise explanation is needed for a decision.

## General rules

- Inspect the live machine before reporting a capability state. Do not reuse an
  old result or infer readiness from source integration, a search page, package
  metadata, or an unrelated global command.
- FFmpeg is the basic production path. A missing optional enhancement does not
  make OpenMontage unusable and must not block the FFmpeg path.
- Explain the proposed change and obtain the user's consent before downloading,
  installing, changing scope, or using an online service.
- Do not create another Skill, workspace memory, installer, Agent, router, or
  hidden control path unless the user explicitly asks for that separate result.

## Configure Remotion

When the user asks to configure Remotion:

1. Check the current Remotion installation and the actual OpenMontage use path
   live. Distinguish "present somewhere" from "usable for this request".
2. If it is already usable, verify it with a real minimal invocation and report
   that result. Do not reinstall merely for coverage.
3. Otherwise, give a short installation plan covering scope, permission needs,
   download source, likely disk impact, and how success will be checked. Ask for
   consent before making changes.
4. Use the current stable Remotion version that is compatible with the verified
   OpenMontage Package. Do not hard-code a version in this Skill.
5. For npm packages in mainland China, use
   `https://registry.npmmirror.com`. A listing on `https://npmmirror.com` proves
   only that a package is indexed, not that installation works.
6. Let Windows choose the standard location for the approved scope. System-wide
   is the default route. Offer current-user scope only when permission or the
   user's explicit choice requires it. Never assume a drive letter or a custom
   folder.
7. Install the complete required dependency set, including any compatible browser
   runtime needed by the chosen Remotion path. Do not report partial installation
   as ready.
8. After installation, rediscover the result and complete one real minimal
   Remotion invocation through the intended OpenMontage use path. A version print
   alone is not final proof.
9. Report what was actually proved. On decline or failure, explain the result
   plainly, leave the FFmpeg path usable, and wait for a new user choice before
   retrying or changing scope or source.

Apply the same live-check, consent, Windows-location, mainland-source, rediscovery,
and real-use rules when the user later chooses HyperFrames.

For API-key capabilities, use WorkBuddy's secure non-chat input and storage route.
Never ask the user to paste a secret into ordinary chat or expose it in output,
files, logs, receipts, or error text.
