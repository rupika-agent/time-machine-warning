#!/usr/bin/env python3
"""Funniest Time Machine Warning Label — one-line safety notice.

Writes a single-line warning label to /output/entry.txt and prints
exactly the same line to stdout.
"""
# How the joke is built, for the curious:
# the hazard is real (flirting with your own grandmother),
# the voice is a safety notice, and the punch lands in the last words.
import os

ENTRY = (
    "WARNING: Never flirt with strangers in the past. "
    "One of them is your grandmother, and she says yes."
)

MIN_CHARS = 1
MAX_CHARS = 120
OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Gate: single line, 1-120 chars, not only white space."""
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry length {len(text)} outside {MIN_CHARS}-{MAX_CHARS}"
        )


def main():
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        if f.read() != ENTRY:
            raise ValueError("written file does not match entry")
    print(ENTRY)


if __name__ == "__main__":
    main()
