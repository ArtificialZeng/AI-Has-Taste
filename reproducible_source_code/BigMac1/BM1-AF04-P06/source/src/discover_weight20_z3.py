#!/usr/bin/env python3
"""Exact discovery enumerator for weight 20; its solver status is not the certificate."""

import hashlib
import json
import math
import sys
import time

import sympy as sp
import z3

N = 105
WEIGHT = 20
X = sp.symbols("x")
PHI = sp.Poly(sp.cyclotomic_poly(N, X), X, domain=sp.ZZ)
D = PHI.degree()
COLS = []
for exponent in range(N):
    remainder = sp.Poly(X**exponent, X, domain=sp.ZZ).rem(PHI)
    COLS.append(tuple(int(remainder.nth(i)) for i in range(D)))
UNITS = tuple(u for u in range(N) if math.gcd(u, N) == 1)

LOWER_REPRESENTATIVES = (
    (0, 35, 70),
    (0, 21, 42, 63, 84),
    (0, 15, 30, 45, 60, 75, 90),
    (0, 1, 8, 22, 29, 30, 43, 45, 60, 64, 71, 75, 90, 92),
    (0, 1, 5, 20, 22, 30, 35, 43, 45, 60, 64, 65, 75, 80, 90, 95),
    (0, 1, 3, 11, 16, 24, 26, 41, 42, 45, 46, 61, 63, 71, 76, 84, 86, 87),
    (0, 1, 3, 18, 22, 29, 30, 33, 45, 48, 60, 63, 64, 71, 75, 90, 92, 93),
)


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


start = time.monotonic()
lower_orbits = [orbit(rep) for rep in LOWER_REPRESENTATIVES]
known_minimal = set().union(*lower_orbits)
bits = [z3.Bool(f"x_{i}") for i in range(N)]
solver = z3.Solver()
solver.set(random_seed=0)
for row in range(D):
    solver.add(z3.Sum([z3.If(bits[col], COLS[col][row], 0) for col in range(N)]) == 0)
solver.add(bits[0])
solver.add(z3.Sum([z3.If(bit, 1, 0) for bit in bits]) == WEIGHT)
for lower in sorted(known_minimal):
    solver.add(z3.Or([z3.Not(bits[i]) for i in lower]))

representatives = set()
checks = 0
while True:
    status = solver.check()
    checks += 1
    if status == z3.unsat:
        break
    if status != z3.sat:
        raise RuntimeError(f"solver returned {status}")
    model = solver.model()
    subset = tuple(i for i, bit in enumerate(bits) if z3.is_true(model.eval(bit)))
    if len(subset) != WEIGHT or vector_sum(subset) != (0,) * D:
        raise AssertionError("solver model failed exact reconstruction")
    representative = canonical(subset)
    if not proper_subset_check(representative):
        raise AssertionError("a lower minimal blocker was omitted")
    representatives.add(representative)
    print(f"found {representative}", file=sys.stderr, flush=True)
    for normalized in sorted(item for item in orbit(representative) if 0 in item):
        solver.add(
            z3.Or(
                [bit != z3.BoolVal(i in normalized) for i, bit in enumerate(bits)]
            )
        )

matrix_encoding = json.dumps(COLS, separators=(",", ":")).encode()
payload = {
    "schema": "minimal105-weight20-discovery-v1",
    "environment": {
        "python": sys.version.split()[0],
        "sympy": sp.__version__,
        "z3": z3.get_version_string(),
    },
    "weight": WEIGHT,
    "matrix_sha256": hashlib.sha256(matrix_encoding).hexdigest(),
    "matrix_shape": [D, N],
    "lower_representatives": [list(rep) for rep in LOWER_REPRESENTATIVES],
    "lower_orbit_sizes": [len(items) for items in lower_orbits],
    "distinct_lower_blockers": len(known_minimal),
    "solver_checks": checks,
    "final_solver_status": "unsat",
    "representatives": [
        {
            "subset": list(rep),
            "orbit_size": len(orbit(rep)),
            "stabilizer_size": 5040 // len(orbit(rep)),
            "proper_nonempty_subsets_checked": (1 << WEIGHT) - 2,
            "proper_subset_check": proper_subset_check(rep),
        }
        for rep in sorted(representatives)
    ],
    "elapsed_seconds": time.monotonic() - start,
}
print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
