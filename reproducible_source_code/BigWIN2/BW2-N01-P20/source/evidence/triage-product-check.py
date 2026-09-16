#!/usr/bin/env python3
"""Exact finite checks of the new product reduction; no asymptotic certificate."""
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import platform

counts = {"even_product": 0, "odd_even_identity": 0,
          "log_linear_sum": 0, "log_quadratic_sum": 0,
          "log_cubic_bound_sum": 0}
for m in range(1, 41):
    central = comb(2*m, m)
    products = [Fraction(1)]
    for r in range(1, m+1):
        products.append(products[-1]*Fraction(m-r+1, m+r))
    for j in range(-m, m+1):
        assert Fraction(comb(2*m, m+j), central) == products[abs(j)]
        counts["even_product"] += 1
        if j < m:
            p = Fraction(comb(2*m-1, m+j), 2**(2*m-1))
            q = Fraction(comb(2*m, m+j), 4**m)
            assert p == (1-Fraction(j, m))*q
            counts["odd_even_identity"] += 1
for r in range(101):
    assert sum(2*l-1 for l in range(1,r+1)) == r*r
    counts["log_linear_sum"] += 1
    assert sum(l*l-(l-1)**2 for l in range(1,r+1)) == r*r
    counts["log_quadratic_sum"] += 1
    assert 2*sum((l-1)**3+l**3 for l in range(1,r+1)) == r*r*(r*r+1)
    counts["log_cubic_bound_sum"] += 1

result = {
    "job_id": "newwin-00001-p20-triage-41e54da15a7f",
    "status": "passed exact finite checks only",
    "python": platform.python_version(),
    "arithmetic": "integer and fractions.Fraction; no floating point",
    "coverage": {"m": "1..40", "j_even": "-m..m", "j_odd": "-m..m-1", "power_sums_r": "0..100"},
    "checks": counts,
    "source_sha256": sha256(Path("source.md").read_bytes()).hexdigest(),
    "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    "limitation": "Checks algebraic reductions, not the logarithmic inequality or universal expectation remainder."
}
print(json.dumps(result, indent=2))
