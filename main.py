# Write a single UTF-8 line for the One-Liner Marathon scorer.
import os
from pathlib import Path


TEXT = 'The electrician said my house was wired by an idiot. I said it was my dad. He looked again. "Was he nice?"'


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
