from __future__ import annotations

import os
import re
from collections.abc import Mapping
from typing import Any


REDACTED = "[REDACTED]"
SENSITIVE_ENV_NAME = re.compile(
    r"(?:KEY|TOKEN|SECRET|PASSWORD|CREDENTIAL|AUTH|BEARER)", re.IGNORECASE
)
SENSITIVE_FIELD_NAME = re.compile(
    r"^(?:api[_-]?key|access[_-]?token|refresh[_-]?token|token|secret|password|"
    r"credential|authorization|bearer(?:[_-]?token)?)$",
    re.IGNORECASE,
)
COMMON_SECRET_PATTERNS = (
    re.compile(r"\bsk-[A-Za-z0-9_-]{8,}\b"),
    re.compile(r"(?i)(Bearer\s+)[A-Za-z0-9._~+/-]{8,}=*"),
    re.compile(
        r"(?i)((?:api[_-]?key|token|secret|password|credential)\s*[=:]\s*)"
        r"[^\s,;]+"
    ),
)


def _sensitive_environment_values() -> list[str]:
    values = {
        value
        for name, value in os.environ.items()
        if SENSITIVE_ENV_NAME.search(name) and isinstance(value, str) and len(value) >= 8
    }
    return sorted(values, key=len, reverse=True)


def redact_text(value: str) -> str:
    redacted = value
    for secret in _sensitive_environment_values():
        redacted = redacted.replace(secret, REDACTED)
    redacted = COMMON_SECRET_PATTERNS[0].sub(REDACTED, redacted)
    redacted = COMMON_SECRET_PATTERNS[1].sub(r"\1" + REDACTED, redacted)
    redacted = COMMON_SECRET_PATTERNS[2].sub(r"\1" + REDACTED, redacted)
    return redacted


def redact_payload(value: Any) -> Any:
    if isinstance(value, str):
        return redact_text(value)
    if isinstance(value, Mapping):
        return {
            key: (
                REDACTED
                if isinstance(key, str) and SENSITIVE_FIELD_NAME.fullmatch(key)
                else redact_payload(item)
            )
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [redact_payload(item) for item in value]
    if isinstance(value, tuple):
        return tuple(redact_payload(item) for item in value)
    return value
