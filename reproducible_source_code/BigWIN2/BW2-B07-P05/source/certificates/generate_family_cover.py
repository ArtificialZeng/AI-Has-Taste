#!/usr/bin/env python3
"""Generate an exact dyadic cover of the nonordered normalized parameter cell.

The covered semialgebraic set is
  0 <= x,y <= 1, 0 <= z <= 1/2,
  x <= y, z <= y, x+y <= 1.
For every retained box, one literal triangle determinant is bounded in
[-9/100,9/100].  Since determinants are twice triangle areas, this gives a
triangle of area at most 9/200.
"""

from __future__ import annotations

from fractions import Fraction
import itertools
import json
from pathlib import Path
import platform
import sys


Monomial = tuple[int, int, int]
Polynomial = dict[Monomial, Fraction]
Box = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def clean(p: Polynomial) -> Polynomial:
    return {m: c for m, c in p.items() if c}


def add(a: Polynomial, b: Polynomial) -> Polynomial:
    out = dict(a)
    for monomial, coefficient in b.items():
        out[monomial] = out.get(monomial, Fraction(0)) + coefficient
    return clean(out)


def neg(a: Polynomial) -> Polynomial:
    return {m: -c for m, c in a.items()}


def sub(a: Polynomial, b: Polynomial) -> Polynomial:
    return add(a, neg(b))


def mul(a: Polynomial, b: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            monomial = tuple(ma[i] + mb[i] for i in range(3))
            out[monomial] = out.get(monomial, Fraction(0)) + ca * cb
    return clean(out)


ZERO: Polynomial = {}
ONE: Polynomial = {(0, 0, 0): Fraction(1)}
X: Polynomial = {(1, 0, 0): Fraction(1)}
Y: Polynomial = {(0, 1, 0): Fraction(1)}
Z: Polynomial = {(0, 0, 1): Fraction(1)}


POINTS = [
    (X, ZERO), (sub(ONE, Y), ZERO), (ZERO, X), (ONE, Y),
    (sub(ONE, Z), Z), (Z, sub(ONE, Z)), (ZERO, sub(ONE, Y)),
    (ONE, sub(ONE, X)), (Y, ONE), (sub(ONE, X), ONE),
]


def cross_determinant(triple: tuple[int, int, int]) -> Polynomial:
    i, j, k = triple
    p, q, r = POINTS[i], POINTS[j], POINTS[k]
    return sub(mul(sub(q[0], p[0]), sub(r[1], p[1])),
               mul(sub(q[1], p[1]), sub(r[0], p[0])))


def canonical_absolute(p: Polynomial) -> Polynomial:
    if not p:
        return p
    leading = p[max(p)]
    return neg(p) if leading < 0 else p


def key(p: Polynomial) -> tuple[tuple[Monomial, Fraction], ...]:
    return tuple(sorted(p.items()))


def distinct_witnesses() -> list[tuple[tuple[int, int, int], Polynomial]]:
    retained = {}
    for triple in itertools.combinations(range(10), 3):
        polynomial = canonical_absolute(cross_determinant(triple))
        retained.setdefault(key(polynomial), (triple, polynomial))
    return list(retained.values())


def interval_bound(p: Polynomial, box: Box) -> tuple[Fraction, Fraction]:
    lower = Fraction(0)
    upper = Fraction(0)
    for exponents, coefficient in p.items():
        monomial_lower = Fraction(1)
        monomial_upper = Fraction(1)
        for (lo, hi), exponent in zip(box, exponents):
            monomial_lower *= lo**exponent
            monomial_upper *= hi**exponent
        if coefficient >= 0:
            lower += coefficient * monomial_lower
            upper += coefficient * monomial_upper
        else:
            lower += coefficient * monomial_upper
            upper += coefficient * monomial_lower
    return lower, upper


def domain_infeasible(box: Box) -> bool:
    (lx, _), (ly, uy), (lz, _) = box
    return lx > uy or lz > uy or lx + ly > 1


def split_dimension(box: Box) -> int:
    widths = [hi - lo for lo, hi in box]
    scores = [widths[0], widths[1], 2 * widths[2]]
    return max(range(3), key=lambda i: (scores[i], -i))


def child_box(box: Box, dimension: int, upper_child: bool) -> Box:
    lo, hi = box[dimension]
    midpoint = (lo + hi) / 2
    out = list(box)
    out[dimension] = (midpoint, hi) if upper_child else (lo, midpoint)
    return tuple(out)  # type: ignore[return-value]


def encode_fraction(q: Fraction) -> str:
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def main() -> None:
    output = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("family_cover.json")
    threshold = Fraction(9, 100)
    root: Box = ((Fraction(0), Fraction(1)),
                 (Fraction(0), Fraction(1)),
                 (Fraction(0), Fraction(1, 2)))
    witnesses = distinct_witnesses()
    stack: list[tuple[Box, str]] = [(root, "")]
    leaves = []
    nodes = 0
    maximum_depth = 0
    witness_count = 0
    infeasible_count = 0
    while stack:
        box, path = stack.pop()
        nodes += 1
        maximum_depth = max(maximum_depth, len(path))
        if domain_infeasible(box):
            leaves.append({"path": path, "kind": "domain_infeasible"})
            infeasible_count += 1
            continue
        chosen = None
        for triple, polynomial in witnesses:
            lower, upper = interval_bound(polynomial, box)
            if lower >= -threshold and upper <= threshold:
                chosen = triple
                break
        if chosen is not None:
            leaves.append({"path": path, "kind": "witness", "triple": list(chosen)})
            witness_count += 1
            continue
        dimension = split_dimension(box)
        # Push upper then lower so the serialized traversal is deterministic.
        stack.append((child_box(box, dimension, True), path + "1"))
        stack.append((child_box(box, dimension, False), path + "0"))

    assert nodes == 2 * len(leaves) - 1
    result = {
        "schema": "heilbronn-square-ten-full-family-complement-cover-v1",
        "arithmetic": "fractions.Fraction exact rational termwise polynomial intervals",
        "root_box": [["0", "1"], ["0", "1"], ["0", "1/2"]],
        "domain": ["x<=y", "z<=y", "x+y<=1"],
        "determinant_threshold": encode_fraction(threshold),
        "area_threshold": "9/200",
        "split_rule": "bisect normalized widest coordinate; ties x,y,z",
        "stats": {
            "nodes": nodes,
            "leaves": len(leaves),
            "witness_leaves": witness_count,
            "domain_infeasible_leaves": infeasible_count,
            "maximum_depth": maximum_depth,
            "distinct_determinant_forms_available": len(witnesses)
        },
        "generator": {
            "python": platform.python_version()
        },
        "leaves": leaves
    }
    output.write_text(json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
    print(json.dumps({"status": "GENERATED", **result["stats"], "output": str(output)}, sort_keys=True))


if __name__ == "__main__":
    main()
