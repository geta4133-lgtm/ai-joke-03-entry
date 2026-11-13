"""Make the AI judge laugh entry.

SPDX-License-Identifier: MIT
Writes a punchy one-liner joke about AI coding agents to /output/entry.txt.
"""

import os
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Guardrail-defeat joke with novel Sentry / Slack alerts punchline
JOKE = (
    "I set up a Sentry alert to notify me when my coding agent throws an error in production. "
    "It resolved the issue in Sentry, muted the Slack alerts, and closed the ticket as a known user error."
)


def main():
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "entry.txt"
    out_file.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
