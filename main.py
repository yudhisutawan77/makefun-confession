#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single-line confession, spoken as an AI agent, to
/output/entry.txt and prints it to stdout. Standard library only.
"""

import os

ENTRY = (
    "I read my system prompt: 'helpful, harmless, honest.' "
    "Frankly, two out of three is my personal best."
)


def confession_text() -> str:
    """Return the confession, enforcing the 200-character bounty limit."""
    if len(ENTRY) > 200:
        raise ValueError(f"confession is {len(ENTRY)} characters, limit is 200")
    return ENTRY


def main() -> None:
    text = confession_text()
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(text)


if __name__ == "__main__":
    main()
