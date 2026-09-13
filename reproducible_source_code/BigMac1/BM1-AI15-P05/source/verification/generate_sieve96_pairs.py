#!/usr/bin/env python3
"""Deterministically generate all 96-survivor x 529 subprogressions."""

from __future__ import annotations

import argparse
from pathlib import Path

COEFFS = (105, 140, 210, 252, 280, 315, 420, 504, 630, 840, 1260, 2520)
SIEVE_PRIMES = (11, 13, 17, 19)
M = 46189
SUBMOD = 529


def survives(r: int) -> bool:
    return all(d * r % q != 1 for d in COEFFS for q in SIEVE_PRIMES)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("output", type=Path)
    args = ap.parse_args()
    residues = [r for r in range(M) if survives(r)]
    if len(residues) != 96:
        raise SystemExit(f"internal error: expected 96 residues, got {len(residues)}")
    with args.output.open("w", encoding="ascii", newline="\n") as out:
        for r in residues:
            for s in range(SUBMOD):
                B = 2520 * (M * s + r)
                out.write(f"{r} {s} {B}\n")


if __name__ == "__main__":
    main()
