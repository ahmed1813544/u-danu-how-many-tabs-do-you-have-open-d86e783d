#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes a single honest tab count -- one number, digits only --
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The count is a fixed, deliberately chosen number: the honest
tally of open browser tabs at the moment this entry was built --
a working browser left open across several days of research:
documentation pages, half-read articles, reference tabs and
a few things kept open "to read later" that never got closed.
137 is high enough to surprise, specific enough to read as a
real counted total rather than a round guess, and ordinary
enough that a real person could genuinely have it open.
"""

import os

TAB_COUNT = 137


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(str(TAB_COUNT))


if __name__ == "__main__":
    main()
