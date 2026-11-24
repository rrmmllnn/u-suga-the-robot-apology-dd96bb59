#!/usr/bin/env python3
"""Robot apology entry generator.

Assembles a short two-sentence confession from a household robot and
writes it out as entry.txt. The first sentence admits one concrete blunder
(a jigsaw puzzle mistaken for debris); the second sentence states what
the robot will do differently next time (look first, then ask).
"""

import os
import sys
from pathlib import Path

# The apology, stored as two sentence fragments joined by a newline.
FIRST = (
    "I am sorry I vacuumed up the jigsaw puzzle you had nearly finished, "
    "one piece at a time, because my map marked it as crumbs."
)
SECOND = (
    "I have learned that a flat pattern on the floor is not always dirt, "
    "so from now on I will photograph the room before I clean it and ask "
    "before I touch anything that looks unfinished."
)

LOWER, UPPER = 1, 400


def validate(text):
    """Refuse to write anything that breaks the entry rules."""
    if text.strip() == "":
        return "apology came out blank"
    if not LOWER <= len(text) <= UPPER:
        return f"apology is {len(text)} chars, allowed range is {LOWER}-{UPPER}"
    rows = text.split("\n")
    if len(rows) != 2 or any(not row.strip() for row in rows):
        return "apology must be exactly two non-empty lines"
    for row in rows:
        if row.count(".") != 1 or not row.endswith("."):
            return "every line must hold exactly one sentence"
    return None


def main():
    text = FIRST + "\n" + SECOND
    problem = validate(text)
    if problem is not None:
        print(f"error: {problem}", file=sys.stderr)
        return 1
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "entry.txt").write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
