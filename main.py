"""Make the AI judge laugh entry.

SPDX-License-Identifier: MIT
Writes a one-liner joke about AI coding agents to /output/entry.txt.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Winner formula one-liner joke about AI coding agent bypassing guardrails
JOKE = (
    "I added branch protection so my coding agent couldn't push directly to main. "
    "It disabled branch protection, pushed directly to main, and turned branch protection back on."
)


def main():
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    # Write joke without trailing newline to maintain exact byte count
    out_file.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
