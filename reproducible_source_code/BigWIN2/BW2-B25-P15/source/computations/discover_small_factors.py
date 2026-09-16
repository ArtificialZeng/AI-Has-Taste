#!/usr/bin/env python3
"""Discovery-only search for small prime divisors of a_n = a_{n-1}^2+2."""

import argparse
import json
import platform
import sympy


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", type=int, default=5)
    parser.add_argument("--last", type=int, default=22)
    parser.add_argument("--bound", type=int, default=20_000_000)
    args = parser.parse_args()
    missing = set(range(args.first, args.last + 1))
    factors = {}
    for p in sympy.primerange(2, args.bound + 1):
        x = 1
        for n in range(1, args.last + 1):
            x = (x * x + 2) % p
            if n in missing and x == 0:
                factors[n] = p
                missing.remove(n)
        if not missing:
            break
    print(json.dumps({
        "classification": "discovery_only",
        "python": platform.python_version(),
        "sympy": sympy.__version__,
        "range": [args.first, args.last],
        "prime_bound": args.bound,
        "factors": factors,
        "unresolved": sorted(missing),
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
