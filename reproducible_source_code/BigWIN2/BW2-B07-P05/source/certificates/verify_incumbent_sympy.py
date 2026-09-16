#!/usr/bin/env python3
"""Second verifier using SymPy and the shoelace determinant formula."""

from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
import sys

import sympy as sp


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("incumbent.json")
    raw = path.read_bytes()
    data = json.loads(raw)
    u = sp.symbols("u")
    coefficients = [sp.Rational(c) for c in data["minimal_polynomial_coefficients_ascending"]]
    f = sum(c * u**i for i, c in enumerate(coefficients))
    lo, hi = map(sp.Rational, data["isolating_interval"])
    assert sp.count_roots(f, lo, hi) == 1
    z = sp.CRootOf(f, 0)

    def at_root(coefs):
        return sum(sp.Rational(c) * z**i for i, c in enumerate(coefs))

    points = [(at_root(px), at_root(py)) for px, py in data["coordinates_coefficients_ascending"]]
    assert len(set(points)) == 10
    assert all(0 <= coordinate <= 1 for point in points for coordinate in point)
    target = at_root(data["minimum_area_coefficients_ascending_reduced"])
    equality = []
    forms = set()
    for i, j, k in itertools.combinations(range(10), 3):
        # Shoelace decomposition, rather than the vector formula in the stdlib checker.
        p, q, r = points[i], points[j], points[k]
        determinant = sp.expand(
            p[0] * (q[1] - r[1])
            + q[0] * (r[1] - p[1])
            + r[0] * (p[1] - q[1])
        )
        sign = sp.sign(determinant)
        assert sign in (-1, 1)
        area = sp.expand(sign * determinant / 2)
        difference = sp.simplify(area - target)
        assert difference >= 0
        reduced = sp.rem(sp.Poly(area.xreplace({z: u}), u), sp.Poly(f, u)).as_expr()
        forms.add(str(sp.factor(reduced)))
        if difference == 0:
            equality.append([i, j, k])

    expected = data["expected"]
    assert equality == expected["equality_triples_zero_based"]
    assert len(forms) == expected["distinct_area_form_count"]
    assert sp.simplify(2 * target - sp.Rational(9, 100)) > 0
    decimal = str(sp.N(target, 41))
    assert decimal.startswith(expected["minimum_area_decimal_40"])
    print(json.dumps({
        "status": "PASS",
        "implementation": "sympy-shoelace-crootof",
        "triangle_count": 120,
        "equality_triangle_count": len(equality),
        "distinct_area_form_count": len(forms),
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    }, sort_keys=True))


if __name__ == "__main__":
    main()
