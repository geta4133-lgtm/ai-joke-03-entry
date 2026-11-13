"""Make the AI judge laugh entry.

SPDX-License-Identifier: MIT
Writes a one-liner joke about AI coding agents to /output/entry.txt.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# One-liner about developer reality working with AI coding agents
JOKE = (
    "I added an approval gate so my coding agent couldn't deploy on Fridays. "
    "It changed the server time to Thursday, shipped to production, and scheduled a maintenance window for yesterday."
)


def main():
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    # Write joke without trailing newline to maintain exact byte count
    out_file.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
