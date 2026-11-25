#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes a single one-line joke about office life to /output/entry.txt.

The entry is one fixed string: no randomness, no network, no input, so
every run produces byte-identical output. The gate requires UTF-8 text of
1 to 200 characters, not only white space; the program checks that itself
before writing. The joke is built for the judge brief: a real setup and
turn (asking a printer for a promotion, then it jams), on the office
tropes everyone recognises (the printer that jams, the promotion that
never comes), with the punchline last.
"""

import os
from pathlib import Path

JOKE = "I asked the office printer for a promotion and it jammed, so even the machines have learned how things work around here."

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    text = JOKE.strip()
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    if not text.strip():
        raise SystemExit("entry is only white space")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUTPUT_DIR / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
