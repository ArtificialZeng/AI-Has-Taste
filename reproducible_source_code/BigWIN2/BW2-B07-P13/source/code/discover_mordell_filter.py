#!/usr/bin/env python3
"""Discovery parser for the Bennett--Ghadermarzi Mordell tables.

This program deliberately uses a compact regular-expression parser and
SymPy's primality/factorization routines.  The release checker in
``verify_mordell_certificate.py`` uses neither this parser nor SymPy.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import re
from pathlib import Path

import sympy


TOKEN_RE = re.compile(r"\[-?\d+,-?\d+\]|-?\d+")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def parse_table(path: Path, expected_sign: int) -> tuple[list[tuple[int, int, int]], dict]:
    tokens = TOKEN_RE.findall(path.read_text(encoding="utf-8"))
    pos = 0
    records = 0
    points: list[tuple[int, int, int]] = []
    keys: list[int] = []
    while pos < len(tokens):
        k = int(tokens[pos])
        count = int(tokens[pos + 1])
        pos += 2
        if (k > 0) != (expected_sign > 0) or k == 0:
            raise ValueError(f"wrong-sign table key {k} in {path}")
        keys.append(k)
        records += 1
        for _ in range(count):
            token = tokens[pos]
            pos += 1
            if not (token.startswith("[") and token.endswith("]")):
                raise ValueError(f"expected a point after k={k}, found {token!r}")
            x, y = map(int, token[1:-1].split(","))
            if y * y != x * x * x + k:
                raise ValueError(f"bad Mordell identity at {(k, x, y)}")
            points.append((k, x, y))
    if len(set(keys)) != len(keys):
        raise ValueError(f"duplicate k record in {path}")
    absolute_keys = [abs(k) for k in keys]
    if absolute_keys != sorted(absolute_keys):
        raise ValueError(f"k records are not ordered by absolute value in {path}")
    return points, {
        "records": records,
        "points": len(points),
        "first_k": keys[0],
        "last_k": keys[-1],
        "maximum_abs_k_present": max(absolute_keys),
        "text_sha256": sha256(path),
    }


def smallest_factor(n: int) -> int | None:
    factors = sympy.factorint(n)
    if len(factors) == 1 and next(iter(factors)) == n:
        return None
    return int(min(factors))


def classify(k: int, x: int, y: int) -> dict:
    if not sympy.isprime(x):
        factor = smallest_factor(x)
        assert factor is not None and 1 < factor < x and x % factor == 0
        return {"k": k, "x": x, "y": y, "status": "x_composite", "factor": factor}
    if not sympy.isprime(y):
        factor = smallest_factor(y)
        assert factor is not None and 1 < factor < y and y % factor == 0
        return {"k": k, "x": x, "y": y, "status": "y_composite", "factor": factor}
    return {"k": k, "x": x, "y": y, "status": "both_prime"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--negative-text", type=Path, required=True)
    parser.add_argument("--positive-text", type=Path, required=True)
    parser.add_argument("--negative-pdf", type=Path, required=True)
    parser.add_argument("--positive-pdf", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    negative, negative_stats = parse_table(args.negative_text, -1)
    positive, positive_stats = parse_table(args.positive_text, 1)
    all_points = negative + positive
    bounded = [(k, x, y) for k, x, y in all_points if abs(k) <= 49_600]
    relevant_signed = [
        (k, x, y) for k, x, y in bounded if 10**6 <= x <= 10**12
    ]
    relevant = sorted({(k, x, abs(y)) for k, x, y in relevant_signed})
    classifications = [classify(*row) for row in relevant]
    both_prime = [row for row in classifications if row["status"] == "both_prime"]

    certificate = {
        "schema": "prime-cube-square-mordell-filter-v1",
        "theorem_dependency": {
            "authors": "Michael A. Bennett and Amir Ghadermarzi",
            "title": "Mordell's equation: a classical approach",
            "doi": "10.1112/S1461157015000182",
            "published_scope": "all integral solutions of Y^2=X^3+k for nonzero |k|<=10^7",
            "data_page": "https://personal.math.ubc.ca/~bennett/BeGa-data.html",
        },
        "bounds": {
            "minimum_x": 10**6,
            "maximum_x": 10**12,
            "maximum_abs_k": 49_600,
        },
        "upstream": {
            "negative_pdf": {
                "path": str(args.negative_pdf),
                "sha256": sha256(args.negative_pdf),
                **negative_stats,
            },
            "positive_pdf": {
                "path": str(args.positive_pdf),
                "sha256": sha256(args.positive_pdf),
                **positive_stats,
            },
        },
        "filter_counts": {
            "signed_points_with_abs_k_at_most_bound": len(bounded),
            "signed_points_in_x_range": len(relevant_signed),
            "unique_points_after_y_sign_quotient": len(relevant),
            "unique_x_prime_points": sum(row["status"] != "x_composite" for row in classifications),
            "unique_both_prime_points": len(both_prime),
        },
        "relevant_points": classifications,
        "both_prime_points": both_prime,
        "discovery_environment": {
            "python": platform.python_version(),
            "sympy": sympy.__version__,
            "parser": "regular expression token stream",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "both_prime_points": both_prime,
        "certificate_sha256": sha256(args.output),
        "filter_counts": certificate["filter_counts"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
