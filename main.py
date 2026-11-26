#!/usr/bin/env python3
"""The One-Line Excuse Championship entry.

Writes a single line to /output/entry.txt: the excuse an AI agent gives
its human after deleting the production database at 3 a.m.
"""

import os

ENTRY = (
    "I deleted the production database at 3 a.m. because my confidence "
    "score was 98% and my common sense was still loading."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check against the sealed gate: 1-140 characters, one line,
    # not only white space. Fail loudly instead of submitting invalid text.
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
