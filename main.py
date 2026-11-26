"""Everyday Things, Two Lines, Longer Run (rev2).

Writes the two-line entry to /output/entry.txt: line 1 explains a
mirror to a 10-year-old with one analogy, line 2 says what the
analogy maps and what it leaves out. Deterministic: no input,
no randomness, no network, the same bytes on every run.
The pond was chosen because a child already knows still water
shows a face back, so the only new idea to learn is that the
mirror keeps that picture flat and hard instead of rippling.
"""

import os

LINE_1 = (
    "A mirror is a still pond hung on the wall, showing your face "
    "back to you without a single ripple."
)
LINE_2 = (
    "It maps the clear reflection and the looking back, but a pond "
    "ripples when you touch it and a mirror stays flat and hard "
    "under your hand."
)

# One newline between the two lines, none at the end: the text is the entry.
# Rule: exactly one "\n" joins LINE_1 and LINE_2, and no trailing newline.
TEXT = LINE_1 + "\n" + LINE_2


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 400 characters.
    n = len(TEXT)
    if n < 1 or n > 400:
        raise SystemExit(f"entry is {n} characters, outside 1-400")
    if TEXT.count("\n") != 1:
        raise SystemExit("entry must be exactly two lines")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
