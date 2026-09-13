#!/usr/bin/env python3
"""Frozen formal no-import referee for shape (5/8,0,1/8)."""

from __future__ import annotations

import argparse
from pathlib import Path

import sympy as sp

from uncovered_ray_x5_8_referee_literal_free_scout import (
    COVERAGE_NOTE,
    SOURCE,
    SOURCE_MANIFEST,
    reconstruct,
)


S = sp.symbols("S", real=True)
EXPECTED_COEFFICIENTS = (
    sp.Rational(5),
    sp.Rational(85, 96) * S,
    sp.Rational(215, 331776) * S * (21249 * S + 19037),
    sp.Rational(5, 31850496) * S
    * (2654208 * S**2 + 8572032 * S + 4083977),
    sp.Rational(1, 110075314176) * S
    * (987426091008 * S**3 + 2214366284160 * S**2
       + 1677691247279 * S + 423511736838),
)
EXPECTED_CERTIFICATES = (
    (0, 0, (sp.Rational(5),)),
    (1, 0, (sp.Rational(85, 96),)),
    (1, 1, (sp.Rational(4092955, 331776),
            sp.Rational(4330745, 165888))),
    (1, 2, (sp.Rational(20419885, 31850496),
            sp.Rational(41849965, 31850496),
            sp.Rational(76551085, 31850496))),
    (1, 3, (sp.Rational(70585289473, 18345885696),
            sp.Rational(2948226457793, 330225942528),
            sp.Rational(427517749327, 20639121408),
            sp.Rational(5302995359285, 110075314176))),
)
EXPECTED_DIAGNOSTIC_MINIMUM = sp.Rational(
    33592320006031526764440574185198142121068487,
    6718464000000000000000000000000000000000000,
)


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(f"FAIL CLOSED: {label}")


def zero(expr: sp.Expr) -> bool:
    return sp.cancel(sp.together(expr)) == 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-path", type=Path, default=SOURCE)
    parser.add_argument("--manifest-path", type=Path, default=SOURCE_MANIFEST)
    parser.add_argument("--coverage-path", type=Path, default=COVERAGE_NOTE)
    parser.add_argument("--attack", choices=(
        "none", "drop-q2", "flip-danger", "corrupt-coefficient", "drop-gate"
    ), default="none")
    args = parser.parse_args()
    result = reconstruct(source_path=args.source_path,
                         manifest_path=args.manifest_path,
                         coverage_path=args.coverage_path,
                         attack=args.attack)
    require(result["lambda_degree"] == 4, "formal lambda degree four")
    require(len(result["coefficients"]) == 5, "formal five coefficients")
    require(all(zero(actual - expected) for actual, expected in
                zip(result["coefficients"], EXPECTED_COEFFICIENTS)),
            "formal coefficients equal literal-free scout")
    actual_certificates = tuple(
        (item["order"], item["degree"], item["bernstein"])
        for item in result["certificates"]
    )
    require(actual_certificates == EXPECTED_CERTIFICATES,
            "formal S-positivity certificates equal literal-free scout")
    lambda_symbol = next(symbol for symbol in result["gamma36"].free_symbols
                         if symbol.name == "lambda")
    require(zero(result["gamma36"] - sum(
        EXPECTED_COEFFICIENTS[power] * lambda_symbol**power
        for power in range(5))), "formal complete 36 Gamma polynomial")
    require(result["danger"] == sp.Rational(31, 64),
            "formal strict danger reserve")
    require(result["det_ratio"] == sp.Rational(5, 72),
            "formal determinant coefficient")
    require(result["diagnostic_count"] == 9,
            "formal derived diagnostic count")
    require(result["diagnostic_minimum"] == EXPECTED_DIAGNOSTIC_MINIMUM
            and result["diagnostic_data"]
            == (sp.Rational(1, 1000000), sp.Rational(1, 1000)),
            "formal diagnostic minimum")
    print("FORMAL_COEFFICIENTS", EXPECTED_COEFFICIENTS)
    print("FORMAL_CERTIFICATES", EXPECTED_CERTIFICATES)
    print("FORMAL_DANGER", sp.Rational(31, 64))
    print("FORMAL_DETC_OVER_S", sp.Rational(5, 72))
    print("VERDICT PASS fixed shape ray for all 0<h<=1 and lambda>0")
    print("SCOPE no numerical inference, no general full-ball conclusion")


if __name__ == "__main__":
    main()
