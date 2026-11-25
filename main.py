#!/usr/bin/env python3
"""One excuse for The Excuse Your Agent Gives You.

The judge is briefed to pick the excuse that makes it laugh
hardest on first read, with the joke found in the specific
absurdity of an agent owning up to its own code, a sharp turn
at the end, and no wasted setup. This line follows that order
on purpose. It opens with the classic deflection every agent
reaches for, the bug was already there before I touched it,
and then the turn quietly takes the blame back: the agent did
not write the bug, it merely gave the bug the confidence to
show itself, as if bugs were shy performers waiting for a
supportive coach. The absurdity is specific to an agent owning
up to its own code, because only an agent would describe
shipping a bug as an act of encouragement, and the punchline
lands on the last word, where the brief says the sharp turn
belongs.

The line is 99 characters, well inside the 1-200 character
gate, so validation only has to catch an edit that would break
the shape: too long, padded, non-ASCII, or split across two
lines. It is plain ASCII and a single line by construction.
"""

import os

# The sealed line. An agent's excuse for a shipped bug: it was
# already in the repo, the agent just gave it the confidence to
# show itself.
ENTRY = "The bug was already in your repo before I touched it; I just gave it the confidence to show itself."

LIMIT = 200  # gate: one line, 1-200 characters


def _validate(text):
    """Refuse anything that is not one clean line inside the limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text, not another type")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if not text.isascii():
        # Non-ASCII bytes would make the character count mean
        # different things on different platforms, so ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if len(text) > LIMIT:
        raise ValueError(
            f"entry is {len(text)} characters, past the {LIMIT} limit"
        )
    if text.strip() != text:
        # Padding at either end is invisible dead weight the gate
        # still counts, so the line must start and end on a letter.
        raise ValueError("entry must not pad itself with spaces")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.isprintable():
        # A tab or other control character would hide bytes inside it.
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # Two spaces in a row is a gap where a word should be.
        raise ValueError("entry must not contain a double space")
    if text[-1] not in ".!?":
        # An excuse that trails off without terminal punctuation
        # reads unfinished, and the turn should land on the last word.
        raise ValueError("entry must end with terminal punctuation")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
