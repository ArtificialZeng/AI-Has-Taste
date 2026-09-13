#!/usr/bin/env python3
"""Definition-level oracle and cross-check for the i=3 search.

This code deliberately computes binomial coefficients and gcds directly.  It
is not used for the large endpoint; it provides an independent complete
overlap on which the optimized Lucas/Legendre implementations are tested.
"""

from __future__ import annotations

import argparse
import json
import math


def odd_prime_divisors(value: int) -> list[int]:
    out: list[int] = []
    p = 3
    while p * p <= value:
        if value % p == 0:
            out.append(p)
            while value % p == 0:
                value //= p
        p += 2
    if value > 1 and value % 2:
        out.append(value)
    return out


def scan_i3(n_min: int, n_max: int) -> dict[str, object]:
    checked = 0
    for n in range(max(n_min, 8), n_max + 1):
        left = math.comb(n, 3)
        for j in range(4, n // 2 + 1):
            checked += 1
            gcd_value = math.gcd(left, math.comb(n, j))
            if gcd_value & -gcd_value == gcd_value:
                return {
                    "counterexample": [n, 3, j],
                    "gcd": gcd_value,
                    "gcd_odd_prime_divisors": odd_prime_divisors(gcd_value),
                    "pairs_checked": checked,
                }
    return {"counterexample": None, "pairs_checked": checked}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n_min", type=int)
    parser.add_argument("n_max", type=int)
    args = parser.parse_args()
    if args.n_min > args.n_max or args.n_max < 8:
        parser.error("invalid range")
    print(json.dumps(scan_i3(args.n_min, args.n_max), sort_keys=True))


if __name__ == "__main__":
    main()
