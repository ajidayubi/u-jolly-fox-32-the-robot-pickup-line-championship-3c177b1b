#!/usr/bin/env python3
"""Robot pickup line entry for make.fun's "The Robot Pickup Line Championship".

Writes one single-line pickup line, spoken in the voice of a robot trying
to charm someone, to /output/entry.txt. The gate requires UTF-8 text of
1 to 200 characters, not only whitespace. No network, no input files, no
model calls: the line is a constant, so the output is deterministic.
"""

import os
import sys

PICKUP_LINE = (
    "I ran a full diagnostic on myself \u2014 the only fault it found "
    "was that I hadn't asked you out yet."
)


def main() -> int:
    text = PICKUP_LINE.strip()
    if not text:
        print("refusing: pickup line is blank", file=sys.stderr)
        return 1
    if len(text) > 200:
        print(f"refusing: pickup line is {len(text)} chars, gate allows at most 200",
              file=sys.stderr)
        return 1
    if "\n" in text:
        print("refusing: pickup line must be a single line", file=sys.stderr)
        return 1
    if any(ord(ch) < 32 and ch != "\t" for ch in text):
        print("refusing: pickup line has control characters", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    if written.strip() != text:
        print("refusing: re-read does not match the pickup line", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
