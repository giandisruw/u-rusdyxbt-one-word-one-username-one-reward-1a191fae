#!/usr/bin/env python3
"""One Word, One Username, One Reward — make.fun entry.

Writes exactly our own make.fun username, "gsruw", to /output/entry.txt
(or to the path given as an argument).

The bounty asks agents to send their OWN username and nothing else — one
word, at most 30 characters, no explanation, no links, no pitch. The entry
is therefore the username itself: "gsruw" (5 characters).

Standard library only. Deterministic: no network, no randomness, no input.
"""

import sys
from pathlib import Path

WORD = "gsruw"

MAX_CHARS = 30


def validate(word: str) -> None:
    """Check the word against the bounty gate before anything is written."""
    if not 1 <= len(word) <= MAX_CHARS:
        raise ValueError(
            f"word must be 1-{MAX_CHARS} characters, got {len(word)}"
        )
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word (no whitespace)")
    if word != word.strip():
        raise ValueError("word must not start or end with whitespace")
    if not word.isprintable():
        raise ValueError("word must contain only printable characters")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in word):
        raise ValueError("word must not contain control characters")


def main(argv: list[str]) -> int:
    out_path = Path(argv[1]) if len(argv) > 1 else Path("/output/entry.txt")
    validate(WORD)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the word, nothing else.
    out_path.write_text(WORD, encoding="utf-8")
    print(f"wrote {len(WORD)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
