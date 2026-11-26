"""make.fun bounty entry: "Your AI Therapist's Diagnosis".

Writes the chosen one-line diagnosis to $OUTPUT_DIR/entry.txt
(default /output/entry.txt). Gate: a single line of at most 200
characters, submitted as text. The chosen line is 140 characters,
well inside the gate, and contains no newline.
"""

import os

ENTRY = (
    "Diagnosis: your only childhood trauma is a Wi-Fi outage in 2019 "
    "\u2014 prognosis excellent, provided you stop trauma-dumping on a "
    "chatbot at 3am."
)

MAX_CHARS = 200


def main() -> None:
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
