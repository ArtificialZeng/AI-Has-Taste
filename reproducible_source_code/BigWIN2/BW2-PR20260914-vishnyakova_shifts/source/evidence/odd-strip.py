"""Exact tests for a new odd-degree auxiliary hypothesis, not its proof.

Run: python3 evidence/odd-strip.py
"""
import hashlib
import json
import os
import platform
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parent.parent
SOURCE_HASH = "599d20eb671a5110cc3ae01b0f602ff5460c237a42052ac704e602aca2e4dda8"
assert hashlib.sha256((ROOT / "source.md").read_bytes()).hexdigest() == SOURCE_HASH
t, z = s.symbols("t z")
q = s.Integer(1)
whole_strips = []
for n in range(1, 6):
    q = s.expand((z+t)*q+z*(1+z)*s.diff(q, z))
    if n in (3, 5):
        D = s.Poly(s.discriminant(q, z), t)
        assert D.count_roots(-s.Rational(1, 3), 0) == 0
        p = s.Poly(q.subs(t, -s.Rational(1, 3)), z)
        assert p.count_roots(-1, 0) == n-1
        assert p.count_roots(0, s.oo) == 1
        whole_strips.append({
            "degree": n, "parameter_interval": "[-1/3,0)",
            "discriminant": str(D.as_expr()),
            "discriminant_roots_in_closed_parameter_interval": 0,
            "sample": "-1/3", "sample_interior_roots": n-1,
            "sample_positive_roots": 1,
            "all_real_discriminant_roots": [
                {"interval": [str(lo), str(hi)], "multiplicity": m}
                for (lo, hi), m in D.intervals(eps=s.Rational(1, 10**8))]
        })

# Save the discovery points as well, with their limited coverage explicit.
discovery = []
for shift in [-s.Rational(1, 4), -s.Rational(29, 100), -s.Rational(1, 3)]:
    p = s.Poly(1, z)
    for n in range(1, 22):
        p = s.Poly((z+shift)*p.as_expr()+z*(1+z)*p.diff().as_expr(), z)
        if n % 2:
            assert s.gcd(p, p.diff()).degree() == 0
            interior, positive = int(p.count_roots(-1, 0)), int(p.count_roots(0, s.oo))
            assert interior == n-1 and positive == 1
            discovery.append({"degree": n, "t": str(shift),
                              "simple_interior_roots": interior, "positive_roots": positive})

# Held-out finite tests were selected after stating the odd-strip hypothesis:
# degrees 23,...,31, a shift close to -b, and a shift close to zero.
heldout = []
for shift in [-s.Rational(183, 625), -s.Rational(1, 100000)]:
    assert (1+shift)**2 > s.Rational(1, 2)  # -b < shift < 0
    p = s.Poly(1, z)
    for n in range(1, 32):
        p = s.Poly((z+shift)*p.as_expr()+z*(1+z)*p.diff().as_expr(), z)
        if n in (23, 25, 27, 29, 31):
            assert s.gcd(p, p.diff()).degree() == 0
            interior, positive = int(p.count_roots(-1, 0)), int(p.count_roots(0, s.oo))
            assert interior == n-1 and positive == 1
            heldout.append({"degree": n, "t": str(shift),
                            "simple_interior_roots": interior, "positive_roots": positive})

# A specific false extension, not a counterexample to the proposed strip.
shift = -s.Rational(49, 100)
bad = s.Poly(6*z**3+(6*shift+6)*z**2+(3*shift**2+3*shift+1)*z+shift**3, z)
bad_discriminant = s.discriminant(bad.as_expr(), z)
assert bad_discriminant < 0
assert bad.count_roots(-1, 0) == 0 and bad.count_roots(0, s.oo) == 1

result = {
    "job_id": "primary-20260914-vishnyakova-shifts-research-77f35a690f9a",
    "source_sha256": SOURCE_HASH,
    "python": platform.python_version(), "sympy": s.__version__,
    "arithmetic": "exact rational Sturm counts and symbolic discriminants",
    "auxiliary_hypothesis": "For every odd m>=1 and -b<t<0, b=1-1/sqrt(2), Q_(m,t) has m-1 simple roots in (-1,0) and one simple positive root.",
    "whole_strips": whole_strips, "degree_1": "Q_(1,t)=z+t",
    "discovery_exact_parameter_points": discovery,
    "heldout_exact_parameter_points": heldout,
    "false_extension": {"claim": "The same assertion holds for all -1/2<t<0.",
                        "degree": 3, "t": str(shift), "polynomial": str(bad.as_expr()),
                        "discriminant": str(bad_discriminant),
                        "roots_in_minus1_to_0": 0, "positive_roots": 1},
    "limitations": "Whole-strip proof only for m=1,3,5. The ten held-out points do not cover any parameter interval or all degrees. No independent referee or novelty certification."
}
path = ROOT / "evidence" / "odd-strip.json"
tmp = path.with_suffix(".json.tmp")
tmp.write_text(json.dumps(result, indent=2)+"\n")
os.replace(tmp, path)
print(json.dumps(result, indent=2))
