#!/usr/bin/env python3
"""Reproduce the Huang--Zhang odd-coefficient test at (k,d,i)=(4,3,3)."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def falling(value: int, length: int) -> int:
    product = 1
    for offset in range(length):
        product *= value - offset
    return product


def coefficient_test(n: int) -> dict[str, object]:
    k, d, i = 4, 3, 3
    s_i = Fraction(falling(k - 1, i - 1), falling(n - k - 1, i - 1))
    t_i = Fraction(
        falling(d - 1, i - 1) ** 2 * falling(n - k - 1, i - 1),
        falling(n - d - 1, i - 1) ** 2 * falling(k - 1, i - 1),
    )
    lhs = k * s_i - d * t_i
    rhs = Fraction(k - d)
    return {
        "n": n,
        "S_3": str(s_i),
        "T_3": str(t_i),
        "lhs": str(lhs),
        "rhs": str(rhs),
        "slack_rhs_minus_lhs": str(rhs - lhs),
        "passes": lhs <= rhs,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {
        "schema_version": 1,
        "source": "Huang--Zhang arXiv:2407.14091v1, proof of Theorem 1.1 and Lemma A.3",
        "parameters": {"k": 4, "d": 3, "only_odd_index": 3},
        "tests": [coefficient_test(n) for n in (9, 10, 11, 12)],
        "interpretation": (
            "The cited coefficient inequality first passes at n=11; its "
            "failure at n=9,10 explains why that proof route does not close the endpoints."
        ),
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    if not result["tests"][2]["passes"]:
        return 1
    if result["tests"][0]["passes"] or result["tests"][1]["passes"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
