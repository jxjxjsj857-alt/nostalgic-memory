#!/usr/bin/env python3
"""Nostalgic Memory: a childhood memory in one sentence.

Writes one original sentence recalling a childhood memory
(182 characters) to /output/entry.txt.
"""

import os
import sys

LINE = "In grandma's kitchen at dusk, the smell of steamed rice and woodsmoke, I sat on a low wooden stool peeling garlic while the cicadas sang outside, certain that summer would never end."

# The gate allows 1 to 280 characters of UTF-8 text, not only whitespace.
assert 1 <= len(LINE) <= 280, f"line is {len(LINE)} chars, must be 1-280"
assert LINE.strip(), "line must not be only whitespace"


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    if "--dry-run" in sys.argv:
        print(LINE)
    else:
        main()
