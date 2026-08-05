"""Irreversibly redact private metadata from the superseded v0.3.18 W0 record."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
AUDIT_ROOT = ROOT / "docs/workbuddy/audits"
TARGETS = [
    AUDIT_ROOT / "W0-PUBLICATION-AUDIT-REPORT-2026-08-05.md",
    *(AUDIT_ROOT / "evidence-2026-08-05").glob("*"),
]
PUBLIC_COMMITS = {"4eab34c5cfcccaa4f1970554928feccce73ee930"}


REPLACEMENTS = (
    (re.compile(r"(?i)named_case_haitao"), "named_case_a"),
    (re.compile(r"(?i)named_case_head_spa"), "named_case_b"),
    (re.compile(r"(?i)named_case_gaga"), "named_case_c"),
    (re.compile(r"(?i)customer_signal_comment_666"), "customer_signal"),
    (re.compile(r"(?i)\bhai" + r"tao\b|海" + "涛"), "[named-case-a]"),
    (re.compile(r"(?i)\bhead[-_ ]spa\b|头" + "疗"), "[named-case-b]"),
    (re.compile(r"(?i)\bga" + r"ga\b"), "[named-case-c]"),
    (
        re.compile(r"(?i)" + "com" + r"ment[-_ ]?666|评论.{0,8}" + "666"),
        "[customer-signal]",
    ),
)
SHA_PATTERN = re.compile(r"(?<![0-9a-fA-F])[0-9a-fA-F]{40}(?![0-9a-fA-F])")


def _redact_sha(match: re.Match[str]) -> str:
    value = match.group(0).lower()
    if value in PUBLIC_COMMITS:
        return value
    digest = hashlib.sha256(value.encode("ascii")).hexdigest()[:16]
    return f"[private-commit-fingerprint:{digest}]"


def sanitize() -> dict[str, int]:
    changed = 0
    replacements = 0
    for path in TARGETS:
        if not path.is_file():
            continue
        original = path.read_text(encoding="utf-8")
        text = original
        for pattern, replacement in REPLACEMENTS:
            text, count = pattern.subn(replacement, text)
            replacements += count
        text, count = SHA_PATTERN.subn(_redact_sha, text)
        replacements += count
        if path.name.endswith("commit-history.tsv"):
            rows = text.splitlines()
            sanitized_rows = [
                "commit_fingerprint\tauthor_redacted\tauthor_email_fingerprint\tdate_redacted\tsubject_redacted"
            ]
            for row in rows[1:]:
                fields = row.split("\t")
                if len(fields) == 5:
                    sanitized_rows.append(
                        "\t".join(
                            (
                                fields[0],
                                "[redacted]",
                                fields[2],
                                "[redacted]",
                                "[historical metadata redacted]",
                            )
                        )
                    )
            text = "\n".join(sanitized_rows) + "\n"
        if text != original:
            path.write_text(text, encoding="utf-8", newline="\n")
            changed += 1
    return {"changed_files": changed, "replacements": replacements}


if __name__ == "__main__":
    print(sanitize())
