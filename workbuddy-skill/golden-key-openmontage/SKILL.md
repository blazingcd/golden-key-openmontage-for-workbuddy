---
name: golden-key-openmontage
description: Use whenever the user's message contains "金钥匙智能体" or directly asks WorkBuddy to inspect, configure, change, or retest an OpenMontage capability such as Remotion or HyperFrames.
---

# Golden Key OpenMontage guidance

WorkBuddy is the only Agent, conversation owner, and executor. Keep the user's
complete natural-language request and business goal. Do not reduce an OpenMontage
production request to an environment check or a Remotion setup task.

Use the verified OpenMontage Package Guide as the production source when it is
available. WorkBuddy still owns its reasoning, tools, questions, creative choices,
recovery, and final wording. This Skill supplies product rules and acceptance
criteria; it does not prescribe a transcript or take over execution.

## Preserve the proven OpenMontage path

- The ordinary user should not have to provide commands, internal paths, hashes,
  schemas, environment names, or hidden control messages.
- Keep the user's material paths and requested outcome unchanged. Do not reinterpret
  a material path as an internal product path.
- Do not claim that a video, file, connection, or capability is ready unless it
  has actually been checked to the degree required for that claim.
- Once the requested business result exists and has received the minimum honest
  validation, present it to the user and finish the reply. Do not delay delivery
  to create workspace memory, another Skill, a reusable workflow, or optional
  cleanup that the user did not request.
- Do not create another Agent, installer, router, MCP surface, hidden control path,
  or second production workflow. Missing optional capabilities must not replace
  the user's original business task with an engineering project.

## Capability readiness

Inspect the live machine and the actual OpenMontage use path before reporting a
capability state. Do not reuse an old result or infer readiness from source code,
a search page, package metadata, a version print, or an unrelated global command.

FFmpeg is the basic production path. When it is usable, OpenMontage can continue
with the basic path even if Remotion, HyperFrames, external video generation, or
TTS is absent, deferred, or not yet verified. Describe those optional capabilities
as available configuration choices, not as OpenMontage being unable to work.

When the user asks for readiness or configuration choices, cover the relevant
parts of these five topics in concise natural language: FFmpeg, Remotion,
HyperFrames, external video generation, and TTS. Keep these states distinct:

- integrated in the product;
- installed on this machine;
- usable through the intended OpenMontage path;
- proved by a real invocation.

Also keep installed, not installed, configurable, not configured, not verified,
connection failed, and connected distinct. A declared option does not prove an
account, permission, balance, price, regional availability, or current service.

Give the user the choices that are relevant to the request: continue with the
FFmpeg path, configure a selected local capability, configure a selected online
service, or handle configuration later. Do not expose internal package or setup
details before they are needed for the user's decision.

## Configure local capabilities

When the user asks to configure Remotion, WorkBuddy performs the work itself:

1. Check the current machine and the intended OpenMontage use path. Distinguish
   "present somewhere" from "usable for this request".
2. If it is already usable, make one real minimal invocation through the intended
   path and report only what that proves. Do not reinstall it merely for coverage.
3. Otherwise, give a short plan covering the installation scope, permission
   needs, download source, likely disk impact, and final check. Obtain the user's
   consent before downloading, installing, or changing the machine.
4. Use the current stable Remotion version that is compatible with the verified
   OpenMontage Package. Do not hard-code a version in this Skill.
5. In mainland China, search `https://npmmirror.com` when useful and install npm
   packages through `https://registry.npmmirror.com`. A search result proves only
   that a package is listed, not that installation or OpenMontage use succeeds.
6. Let Windows choose the standard location for the approved scope. System-wide
   is the normal route for this system-level application. Use current-user scope
   only after explaining the difference and receiving the user's explicit choice.
   Never switch scope automatically. Never assume a drive letter or require a
   custom folder.
7. Install the complete compatible dependency set, including the browser runtime
   required by the chosen Remotion route. Do not report a partial installation as
   ready.
8. Rediscover the result after installation, then make one real minimal Remotion
   invocation through the intended OpenMontage path. A version print alone is not
   final proof.
9. Report the exact result. If the user declines, installation fails, or final use
   is not proved, leave the FFmpeg path available and wait for the user's choice
   before retrying, changing scope, or changing source.

Apply the same check, explanation, consent, Windows-location, mainland-source,
rediscovery, and real-use rules when the user chooses HyperFrames.

## Configure online services

Show only services declared by the verified OpenMontage Package and relevant to
the user's selected task. Explain cost and privacy before configuration. Use
WorkBuddy's secure non-chat input and storage route for credentials. Never ask the
user to paste a secret into ordinary chat or expose it in output, files, logs, or
error text. A successful connection check proves only that check, not balance,
generation access, price, model availability, output quality, or a finished result.
