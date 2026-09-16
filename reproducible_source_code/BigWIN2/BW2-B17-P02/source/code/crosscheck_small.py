#!/usr/bin/env python3
"""Brute-force cross-check of the hypergraph and cardinality CNF semantics."""
import itertools
import math
from generate_cnf import build
from pysat.solvers import Solver


def admissible(s):
    return all(not (math.gcd(a,b) == math.gcd(a,c) == math.gcd(b,c))
               for a,b,c in itertools.combinations(s, 3))


for n in range(1, 13):
    optimum = max(len(s) for mask in range(1 << n)
                  if admissible(s := [i + 1 for i in range(n) if mask >> i & 1]))
    for k in range(1, n + 1):
        _, clauses = build(n, k)
        with Solver(name="cadical195", bootstrap_with=clauses) as solver:
            got = solver.solve()
        assert got == (optimum >= k), (n, k, optimum, got)
    print(n, optimum)
print("SMALL_CROSSCHECK_OK")
