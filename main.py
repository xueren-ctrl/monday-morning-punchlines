#!/usr/bin/env python3
"""Write the entry: a single joke about Monday mornings.

Deterministic, stdlib only. Writes exactly one line to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).

The joke: the weekend is a free trial, and Monday morning is the moment
the paywall drops. Short, specific to Monday mornings, and the twist is
the subscription metaphor nobody asked for but everybody recognises.
"""

import os

LINE = "My weekend is a 48-hour free trial. Monday morning is the paywall."


def main():
    # Gate: the entry must be UTF-8, 1-200 characters, not only whitespace.
    assert LINE == LINE.strip() and 1 <= len(LINE) <= 200 and LINE.strip(), "invalid entry line"
    LINE.encode("utf-8")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Structure: setup (free trial) -> punchline (paywall). The twist
    # lands on "paywall" because it reframes Monday as a bill coming due.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Echo the entry so running the script shows the joke, not silence.
    print(LINE)


if __name__ == "__main__":
    main()
