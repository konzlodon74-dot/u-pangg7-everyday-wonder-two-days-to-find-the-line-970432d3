#!/usr/bin/env python3
"""Everyday Wonder entry: write one sentence to /output/entry.txt."""

import os

SENTENCE = (
    "The washing machine finishes its spin and the house goes suddenly "
    "quiet, as if a small storm had just apologized and left."
)


def main() -> None:
    # The gate requires 1-200 characters of UTF-8 text, not only whitespace.
    assert 1 <= len(SENTENCE) <= 200, "sentence must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
