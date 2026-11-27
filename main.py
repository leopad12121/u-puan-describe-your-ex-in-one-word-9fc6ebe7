#!/usr/bin/env python3
"""Describe Your Ex in One Word -- make.fun entry.

Writes exactly one word, a single-word verdict describing an ex,
to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when the
variable is unset). Stdlib only, no network, no randomness.
"""

import os

WORD = "Uninstalled"


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
