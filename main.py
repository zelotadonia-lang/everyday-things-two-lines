"""Everyday Things, Two Lines, Longer Run.

Writes the two-line entry to /output/entry.txt: line 1 explains a
washing machine to a 10-year-old with one analogy, line 2 says what
the analogy maps and what it leaves out. Deterministic: no input,
no randomness, no network, the same bytes on every run.
"""

import os

LINE_1 = (
    "A washing machine is a bathtub that learned to spin, "
    "tossing your clothes around in soapy water until the dirt lets go."
)
LINE_2 = (
    "It maps the spinning and the soap, but a bathtub never drains "
    "itself and clothes cannot climb out when they are clean."
)

# One newline between the two lines, none at the end: the text is the entry.
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
