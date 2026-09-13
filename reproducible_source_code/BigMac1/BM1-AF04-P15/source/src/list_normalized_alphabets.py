#!/usr/bin/env python3
"""List primitive normalized four-letter alphabets modulo reflection."""

from __future__ import annotations

import argparse
import itertools
import math


def representatives(maximum: int) -> list[tuple[int, int, int, int]]:
    result: set[tuple[int, int, int, int]] = set()
    for c in range(3, maximum + 1):
        for a, b in itertools.combinations(range(1, c), 2):
            alphabet = (0, a, b, c)
            if math.gcd(a, b, c) != 1:
                continue
            reflection = (0, c - b, c - a, c)
            result.add(min(alphabet, reflection))
    return sorted(result, key=lambda item: (item[-1], item))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--maximum", type=int, required=True)
    args = parser.parse_args()
    if args.maximum < 3:
        raise SystemExit("maximum must be at least 3")
    for alphabet in representatives(args.maximum):
        print(" ".join(map(str, alphabet)))


if __name__ == "__main__":
    main()
