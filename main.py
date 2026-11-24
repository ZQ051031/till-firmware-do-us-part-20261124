#!/usr/bin/env python3
"""Till Firmware Do Us Part — one funny, heartfelt robot wedding vow.

Writes the entry to /output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "I vow to love you through every firmware update, every unexpected reboot, "
    "and every low-battery warning \u2014 till our circuits finally power down together."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
