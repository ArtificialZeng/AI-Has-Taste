#!/usr/bin/env python3
"""Exact truncated coefficient check for f4^8/(f1^16*f2^8) modulo 5."""

import argparse


def coefficients_mod_5(limit: int) -> list[int]:
    # The exponent of (1-q^d) is -16, with an additional -8 if 2|d and
    # an additional +8 if 4|d.  Ascending updates divide by (1-q^d),
    # while descending updates multiply by it.  All arithmetic is in F_5.
    coeff = [1] + [0] * limit
    for d in range(1, limit + 1):
        exponent = -16 - (8 if d % 2 == 0 else 0) + (8 if d % 4 == 0 else 0)
        if exponent < 0:
            for _ in range(-exponent):
                for n in range(d, limit + 1):
                    coeff[n] = (coeff[n] + coeff[n - d]) % 5
        else:
            for _ in range(exponent):
                for n in range(limit, d - 1, -1):
                    coeff[n] = (coeff[n] - coeff[n - d]) % 5
    return coeff


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=1000)
    args = parser.parse_args()
    if args.limit < 5:
        raise SystemExit("--limit must be at least 5")

    coeff = coefficients_mod_5(args.limit)
    failures = [(n, coeff[5 * n]) for n in range(1, args.limit // 5 + 1)
                if coeff[5 * n] != 0]
    print(f"limit={args.limit}")
    print(f"constant_term_mod_5={coeff[0]}")
    print(f"tested_progression_terms={args.limit // 5}")
    print(f"failures={failures}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()

