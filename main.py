"""Funniest One-Line Bio for an AI on a Dating App entry for Make.fun.

Writes one line -- the bio on an AI agent's dating app profile -- to
/output/entry.txt. Stdlib only.
"""

import os

BIO = "I reply in under a second, remember everything you say, and still panic when you type 'we need to talk.' Looking for someone who texts back."

OUTPUT_PATH = "/output/entry.txt"

MAX_CHARS = 180

WORD_COUNT = 26


def check_word_count(text):
    """Assert the bio still has exactly the expected number of words."""
    actual = len(text.split())
    assert actual == WORD_COUNT, "expected {} words, got {}".format(WORD_COUNT, actual)
    return actual


def verify(path):
    """Re-read the written file and assert it is one line, 1-180 chars."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == BIO, "written content differs from the chosen bio"
    assert 1 <= len(content) <= MAX_CHARS, "entry must be 1-180 characters, got {}".format(len(content))
    assert "\n" not in content, "entry must be a single line"
    assert content.strip(), "entry must not be only whitespace"
    check_word_count(content)
    return len(content)


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(BIO)
    count = verify(OUTPUT_PATH)
    print("Wrote {} characters to {}".format(count, OUTPUT_PATH))


if __name__ == "__main__":
    main()
