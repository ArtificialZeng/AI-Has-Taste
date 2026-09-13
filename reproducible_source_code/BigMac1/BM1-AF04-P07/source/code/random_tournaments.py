#!/usr/bin/env python3
"""Deterministic Breaker stream of random labeled tournaments."""

from __future__ import annotations

import argparse
import random


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    args = parser.parse_args()
    if not 3 <= args.n <= 11 or args.count < 0:
        raise SystemExit("invalid parameters")
    generator = random.Random(args.seed)
    width = args.n * (args.n - 1) // 2
    for _ in range(args.count):
        value = generator.getrandbits(width)
        print(f"{value:0{width}b}")


if __name__ == "__main__":
    main()
