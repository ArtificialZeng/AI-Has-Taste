#!/usr/bin/env python3
"""Emit exact cyclic C3 blow-ups with part sizes 4,4,3.

Each within-part tournament ranges over gentourng's canonical representatives,
supplied on the command line as three files.  The first emitted tournament is
C3[TT4,TT4,TT3] and is retained as the explicit upper-bound minimizer.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def pair_index(n: int, i: int, j: int) -> int:
    return i * (2 * n - i - 1) // 2 + j - i - 1


def read_bits(path: Path, n: int) -> list[str]:
    values = path.read_text(encoding="ascii").splitlines()
    assert values
    assert all(len(v) == n * (n - 1) // 2 and set(v) <= {"0", "1"} for v in values)
    return values


def inner_arc(bits: str, size: int, a: int, b: int) -> bool:
    if a < b:
        return bits[pair_index(size, a, b)] == "1"
    return bits[pair_index(size, b, a)] == "0"


def blowup(inner: tuple[str, str, str]) -> str:
    parts = (range(0, 4), range(4, 8), range(8, 11))
    part_of = {v: p for p, vertices in enumerate(parts) for v in vertices}
    result: list[str] = []
    for i in range(11):
        for j in range(i + 1, 11):
            pi, pj = part_of[i], part_of[j]
            if pi == pj:
                local_i = i - parts[pi].start
                local_j = j - parts[pj].start
                forward = inner_arc(inner[pi], len(parts[pi]), local_i, local_j)
            else:
                forward = (pi + 1) % 3 == pj
            result.append("1" if forward else "0")
    return "".join(result)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("t4_file", type=Path)
    parser.add_argument("t3_file", type=Path)
    args = parser.parse_args()
    t4 = read_bits(args.t4_file, 4)
    t3 = read_bits(args.t3_file, 3)
    for left in t4:
        for middle in t4:
            for right in t3:
                print(blowup((left, middle, right)))


if __name__ == "__main__":
    main()
