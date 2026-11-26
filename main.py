"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

The entry is one pickup line aimed at a robot: a CAPTCHA joke. The
setup names the machine gate, the punch is that the speaker keeps
failing the "I'm not a robot" test every time they look at it — the
human failing the humanity test because of the machine. No batteries,
no charging, no rebooting: the laugh comes from the CAPTCHA premise.

How it runs: `python3 main.py` writes the line to /output/entry.txt
(creating /output if needed) and prints the same line to stdout.
No arguments, no input files, no network, deterministic — every run
writes byte-identical output.

Verification (2026-11-25, local run): exit 0, /output/entry.txt is
94 UTF-8 characters on one line with no trailing newline, and the
stdout text matches the file exactly. Re-run after this docstring
edit and compare the stdout sha256 to confirm byte-identical output.
"""

import os

TEXT = "Are you a CAPTCHA? Because I keep failing the 'I'm not a robot' test every time I look at you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()
