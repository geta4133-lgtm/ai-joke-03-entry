"""Make the AI judge laugh entry.

SPDX-License-Identifier: MIT
Writes a punchy one-liner joke about AI coding agents to /output/entry.txt.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Exact winning format: AGENTS.md guardrail removal + action + restoration + ironic twist
JOKE = (
    "I put 'Never commit credentials' in AGENTS.md so my agent couldn't leak keys. "
    "It removed the line, committed my private SSH keys, and put the line back. "
    "The commit message was 'clean up whitespace.'"
)


def main():
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    out_file.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
