#!/usr/bin/env python3
import hashlib
import json
import math

import sympy as sp
import z3

N = 105
X = sp.symbols("x")
PHI = sp.Poly(sp.cyclotomic_poly(N, X), X, domain=sp.ZZ)
D = PHI.degree()
COLS = []
for exponent in range(N):
    remainder = sp.Poly(X**exponent, X, domain=sp.ZZ).rem(PHI)
    COLS.append(tuple(int(remainder.nth(i)) for i in range(D)))
UNITS = tuple(u for u in range(N) if math.gcd(u, N) == 1)


def vector_sum(subset):
    return tuple(sum(COLS[s][row] for s in subset) for row in range(D))


def image(subset, translation, unit):
    return tuple(sorted((translation + unit * s) % N for s in subset))


def orbit(subset):
    return {
        image(subset, translation, unit)
        for translation in range(N)
        for unit in UNITS
    }


def canonical(subset):
    return min(orbit(subset))


def proper_subset_check(subset):
    current = [0] * D
    previous_gray = 0
    full_mask = (1 << len(subset)) - 1
    for step in range(1, 1 << len(subset)):
        gray = step ^ (step >> 1)
        changed = gray ^ previous_gray
        position = changed.bit_length() - 1
        sign = 1 if gray & changed else -1
        for row, value in enumerate(COLS[subset[position]]):
            current[row] += sign * value
        if gray != full_mask and all(value == 0 for value in current):
            return False
        previous_gray = gray
    return True


BITS = [z3.Bool(f"x_{i}") for i in range(N)]
BASE = [
    z3.Sum([z3.If(BITS[col], COLS[col][row], 0) for col in range(N)]) == 0
    for row in range(D)
]
KNOWN_MINIMAL = set()
ROWS = []
for weight in range(1, 20):
    solver = z3.Solver()
    solver.set(random_seed=0)
    solver.add(BASE)
    solver.add(BITS[0])
    solver.add(z3.Sum([z3.If(bit, 1, 0) for bit in BITS]) == weight)
    for lower in sorted(KNOWN_MINIMAL):
        solver.add(z3.Or([z3.Not(BITS[i]) for i in lower]))
    representatives = set()
    while solver.check() == z3.sat:
        model = solver.model()
        subset = tuple(
            i for i, bit in enumerate(BITS) if z3.is_true(model.eval(bit))
        )
        assert vector_sum(subset) == (0,) * D
        representative = canonical(subset)
        representatives.add(representative)
        for normalized in sorted(item for item in orbit(representative) if 0 in item):
            solver.add(
                z3.Or(
                    [
                        bit != z3.BoolVal(i in normalized)
                        for i, bit in enumerate(BITS)
                    ]
                )
            )
    assert solver.check() == z3.unsat
    for representative in representatives:
        KNOWN_MINIMAL.update(orbit(representative))
    ROWS.append(
        {
            "weight": weight,
            "representatives": [
                {
                    "subset": list(representative),
                    "orbit_size": len(orbit(representative)),
                    "stabilizer_size": 5040 // len(orbit(representative)),
                    "proper_nonempty_subsets_checked": (1 << weight) - 2,
                    "proper_subset_check": proper_subset_check(representative),
                }
                for representative in sorted(representatives)
            ],
        }
    )

matrix_encoding = json.dumps(COLS, separators=(",", ":")).encode()
payload = {
    "schema": "minimal105-exhaustive-replay-v1",
    "environment": {
        "sympy": sp.__version__,
        "z3": z3.get_version_string(),
    },
    "cyclotomic_degree": D,
    "matrix_shape": [D, N],
    "matrix_rank": sp.Matrix(D, N, lambda row, col: COLS[col][row]).rank(),
    "matrix_sha256": hashlib.sha256(matrix_encoding).hexdigest(),
    "affine_group_order": N * len(UNITS),
    "weights": ROWS,
}
print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
