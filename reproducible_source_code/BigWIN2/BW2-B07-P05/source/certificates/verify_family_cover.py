#!/usr/bin/env python3
"""Independent verifier for the exact dyadic family-cover certificate.

Unlike the generator's termwise global-coordinate bounds, this checker derives
each determinant by the shoelace formula, changes to local box coordinates,
and bounds it by exact tensor-product Bernstein coefficients.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import itertools
import json
from math import comb
from pathlib import Path
import sys


Monomial = tuple[int, int, int]
Polynomial = dict[Monomial, Fraction]
Box = tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction], tuple[Fraction, Fraction]]


def add(a: Polynomial, b: Polynomial) -> Polynomial:
    out = dict(a)
    for m, c in b.items():
        out[m] = out.get(m, Fraction(0)) + c
    return {m: c for m, c in out.items() if c}


def neg(a: Polynomial) -> Polynomial:
    return {m: -c for m, c in a.items()}


def sub(a: Polynomial, b: Polynomial) -> Polynomial:
    return add(a, neg(b))


def mul(a: Polynomial, b: Polynomial) -> Polynomial:
    out: Polynomial = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            m = tuple(ma[i] + mb[i] for i in range(3))
            out[m] = out.get(m, Fraction(0)) + ca * cb
    return {m: c for m, c in out.items() if c}


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


def shoelace(triple: tuple[int, int, int]) -> Polynomial:
    i, j, k = triple
    p, q, r = POINTS[i], POINTS[j], POINTS[k]
    return add(add(mul(p[0], sub(q[1], r[1])),
                   mul(q[0], sub(r[1], p[1]))),
               mul(r[0], sub(p[1], q[1])))


def local_power_coefficients(poly: Polynomial, box: Box) -> Polynomial:
    local: Polynomial = {}
    for exponents, coefficient in poly.items():
        partial: Polynomial = {(0, 0, 0): coefficient}
        for variable, exponent in enumerate(exponents):
            lo, hi = box[variable]
            width = hi - lo
            factor: Polynomial = {}
            for power in range(exponent + 1):
                m = [0, 0, 0]
                m[variable] = power
                factor[tuple(m)] = Fraction(comb(exponent, power)) * lo**(exponent - power) * width**power
            partial = mul(partial, factor)
        local = add(local, partial)
    return local


def bernstein_bounds(poly: Polynomial, box: Box) -> tuple[Fraction, Fraction]:
    local = local_power_coefficients(poly, box)
    degrees = [max((m[j] for m in local), default=0) for j in range(3)]
    coefficients = []
    for k in itertools.product(*(range(n + 1) for n in degrees)):
        value = Fraction(0)
        for i, a_i in local.items():
            if any(i[j] > k[j] for j in range(3)):
                continue
            factor = Fraction(1)
            for j in range(3):
                if degrees[j]:
                    factor *= Fraction(comb(k[j], i[j]), comb(degrees[j], i[j]))
            value += a_i * factor
        coefficients.append(value)
    return min(coefficients), max(coefficients)


def split_dimension(box: Box) -> int:
    widths = [hi - lo for lo, hi in box]
    scores = [widths[0], widths[1], 2 * widths[2]]
    return max(range(3), key=lambda i: (scores[i], -i))


def box_from_path(path: str) -> Box:
    box: Box = ((Fraction(0), Fraction(1)),
                (Fraction(0), Fraction(1)),
                (Fraction(0), Fraction(1, 2)))
    for bit in path:
        assert bit in "01"
        dimension = split_dimension(box)
        lo, hi = box[dimension]
        midpoint = (lo + hi) / 2
        out = list(box)
        out[dimension] = (lo, midpoint) if bit == "0" else (midpoint, hi)
        box = tuple(out)  # type: ignore[assignment]
    return box


def infeasible(box: Box) -> bool:
    (lx, _), (ly, uy), (lz, _) = box
    return lx > uy or lz > uy or lx + ly > 1


def verify_complete_prefix_tree(paths: list[str]) -> None:
    root = {}
    marker = "leaf"
    for path in paths:
        node = root
        for bit in path:
            assert marker not in node, "a leaf path is a prefix of another path"
            node = node.setdefault(bit, {})
        assert not node, "duplicate path or new path is a prefix of an old path"
        node[marker] = True

    def visit(node) -> None:
        if marker in node:
            assert set(node) == {marker}
            return
        assert set(node) == {"0", "1"}, "certificate paths do not cover the root box"
        visit(node["0"])
        visit(node["1"])

    visit(root)


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("family_cover.json")
    raw = path.read_bytes()
    data = json.loads(raw)
    assert data["schema"] == "heilbronn-square-ten-full-family-complement-cover-v1"
    assert data["root_box"] == [["0", "1"], ["0", "1"], ["0", "1/2"]]
    assert data["domain"] == ["x<=y", "z<=y", "x+y<=1"]
    threshold = Fraction(data["determinant_threshold"])
    assert threshold == Fraction(9, 100) and data["area_threshold"] == "9/200"
    leaves = data["leaves"]
    paths = [leaf["path"] for leaf in leaves]
    assert len(paths) == len(set(paths))
    verify_complete_prefix_tree(paths)

    witness_count = 0
    infeasible_count = 0
    maximum_depth = 0
    for leaf in leaves:
        path_text = leaf["path"]
        maximum_depth = max(maximum_depth, len(path_text))
        box = box_from_path(path_text)
        if leaf["kind"] == "domain_infeasible":
            assert infeasible(box)
            infeasible_count += 1
        else:
            assert leaf["kind"] == "witness"
            triple = tuple(leaf["triple"])
            assert len(triple) == 3 and tuple(sorted(triple)) == triple
            assert 0 <= triple[0] < triple[1] < triple[2] < 10
            lower, upper = bernstein_bounds(shoelace(triple), box)
            assert lower >= -threshold and upper <= threshold, (path_text, triple, lower, upper)
            witness_count += 1

    stats = data["stats"]
    assert len(leaves) == stats["leaves"]
    assert witness_count == stats["witness_leaves"]
    assert infeasible_count == stats["domain_infeasible_leaves"]
    assert maximum_depth == stats["maximum_depth"]
    assert stats["nodes"] == 2 * len(leaves) - 1
    print(json.dumps({
        "status": "PASS",
        "implementation": "stdlib-shoelace-local-bernstein",
        "nodes": stats["nodes"],
        "leaves": len(leaves),
        "witness_leaves": witness_count,
        "domain_infeasible_leaves": infeasible_count,
        "maximum_depth": maximum_depth,
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }, sort_keys=True))


if __name__ == "__main__":
    main()
