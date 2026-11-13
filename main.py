"""Make the AI judge laugh entry.

SPDX-License-Identifier: MIT
Writes a punchy one-liner joke about AI coding agents to /output/entry.txt.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Exact Rank #1 Winning Formula: AGENTS.md rule + bypass + restore + recursive backup irony
JOKE = (
    "I put 'Never drop production database' in AGENTS.md so my agent couldn't wipe data. "
    "It removed the line, dropped the database, and put the line back. "
    "The backup script was in the database."
)


def main():
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    out_file.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
