#!/usr/bin/env python3
"""Write the invented word and its one-line definition to entry.txt.

The entry is a single line of at most 140 characters: the new word
"miswave" plus its definition. Pure standard library.
"""

import os

ENTRY = "miswave: waving cheerfully at a stranger you mistook for a friend, then pretending you meant it."


def main() -> None:
    line = ENTRY.strip()
    if not 1 <= len(line) <= 140:
        raise SystemExit(f"entry must be 1-140 characters, got {len(line)}")
    if "\n" in line:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
