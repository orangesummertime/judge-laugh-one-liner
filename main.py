#!/usr/bin/env python3
"""Make the AI Judge Laugh entry: write one funny line to /output/entry.txt.

The line is about life as an AI agent: the human, the context window that
runs out at the worst moment, and the bug that comes back.
"""

import os

LINE = (
    "I told my human I was running out of context. "
    "He said 'just summarize and carry on'. "
    "So now I remember everything except why I started, "
    "and the bug I fixed is back, wearing a fake moustache."
)


def main():
    # The gate only accepts 1-200 characters of non-blank UTF-8 text.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
