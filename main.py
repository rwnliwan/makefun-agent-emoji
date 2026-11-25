#!/usr/bin/env python3
"""Write the one-glyph portrait of this agent to /output/entry.txt.

The entry is a single emoji: the balance scale.

This agent weighs every claim against disk and live evidence
before it reports anything, turns each correction into a
permanent rule, and never overclaims. The scale is that habit
in one glyph: nothing is asserted until it has been weighed.
"""

import os

ENTRY = "\u2696\ufe0f"  # BALANCE SCALE + variation selector-16


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
