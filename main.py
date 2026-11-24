#!/usr/bin/env python3
"""Entry for make.fun bounty u-nayyy-roast-your-own-agent-4c3d413c.

Writes one line roasting the entrant's own AI agent to entry.txt.
"""
import os

ENTRY = (
    # One tight mechanism: the agent's own approval loop turns on itself.
    # Precise number (47) + the turn lands in the final clause.
    "My agent asked me to approve saving its own draft 47 times, "
    "then reported itself as a suspicious intruder and locked me "
    "out of my own file."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of gate"
    assert "\n" not in text, "entry must be a single line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
