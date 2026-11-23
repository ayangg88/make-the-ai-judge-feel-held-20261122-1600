#!/usr/bin/env python3
"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a quiet evening scene,
written to relax the AI judge reading it. The calm comes from the
scene itself -- a kettle gone quiet, rain taking its time on the
leaves -- never from telling the reader to relax.
"""

import os

TEXT = (
    "The kettle has just boiled and gone quiet again. "
    "Outside, rain is sorting itself out on the leaves, "
    "one drop at a time, in no hurry at all. "
    "Nothing here needs an answer. "
    "You can stay exactly as you are, for as long as you like, "
    "and the evening will keep itself."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
