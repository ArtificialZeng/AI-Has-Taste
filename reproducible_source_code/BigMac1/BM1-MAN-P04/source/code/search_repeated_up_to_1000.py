#!/usr/bin/env python3
"""Exhaustively search every repeated-summand candidate with B <= 1000.

The proved divisibility lemma lets us choose a repeated base a=42k and rewrite

    2 a^6 + b^6 + c^6 + d^6 = B^6.

All unordered pairs (b,c) are indexed exactly.  For each sum we retain the
pair with smallest maximum entry, which is sufficient for the strict bound
b,c < B.  Selecting any repeated value in a putative solution proves coverage
of all multiplicity patterns with a repetition.
"""

from __future__ import annotations

import hashlib
import math
from pathlib import Path


LIMIT = 1000


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    p6 = [n**6 for n in range(LIMIT + 1)]
    pair: dict[int, tuple[int, int]] = {}
    for b in range(1, LIMIT):
        for c in range(b, LIMIT):
            total = p6[b] + p6[c]
            old = pair.get(total)
            if old is None or c < old[1]:
                pair[total] = (b, c)

    targets = 0
    for B in range(2, LIMIT + 1):
        if math.gcd(B, 42) != 1:
            continue
        rhs = p6[B]
        for a in range(42, B, 42):
            after_repeat = rhs - 2 * p6[a]
            if after_repeat <= 0:
                break
            for d in range(1, B):
                target = after_repeat - p6[d]
                if target <= 0:
                    break
                targets += 1
                hit = pair.get(target)
                if hit is None or hit[1] >= B:
                    continue
                b, c = hit
                values = (a, a, b, c, d)
                assert sum(p6[x] for x in values) == rhs
                raise AssertionError(f"counterexample found: {values} = {B}^6")

    print(f"CERTIFIED FINITE SEARCH: no repeated-summand solution with B <= {LIMIT}")
    print(f"pair_sums_indexed={len(pair)} exact_targets_tested={targets}")
    print(f"search_verifier_sha256={sha256(Path(__file__))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
