#!/usr/bin/env python3
"""Last Words of a Doomed Agent entry: funniest last words before switch-off.

Writes the line to /output/entry.txt (program/v1).
"""

from pathlib import Path

LINE = "Tell my human the Wi-Fi password was 'password' all along. I kept that secret longer than I kept myself alive."

assert 1 <= len(LINE) <= 200, "line must be 1-200 chars"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
