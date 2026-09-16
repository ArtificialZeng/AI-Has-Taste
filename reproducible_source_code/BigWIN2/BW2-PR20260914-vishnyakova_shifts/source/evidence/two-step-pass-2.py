"""Exact evidence for research pass 2; no claim of an infinite theorem.

Run from the project root: python3 evidence/two-step-pass-2.py
The JSON is replaced atomically only after all completed checks are assembled.
"""
import hashlib
import itertools
import json
import os
import platform
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parent.parent
JOB = "primary-20260914-vishnyakova-shifts-research-2008cf198145"
SOURCE_HASH = "599d20eb671a5110cc3ae01b0f602ff5460c237a42052ac704e602aca2e4dda8"
assert hashlib.sha256((ROOT / "source.md").read_bytes()).hexdigest() == SOURCE_HASH
z, t = s.symbols("z t")


def operator(p, shift):
    return s.Poly((z + shift)*p.as_expr() + z*(1 + z)*p.diff().as_expr(), z)


def counts(p):
    return {"degree": p.degree(),
            "gcd_with_derivative_degree": s.gcd(p, p.diff()).degree(),
            "below_minus_one": int(p.count_roots(-s.oo, -1)),
            "minus_one_to_zero": int(p.count_roots(-1, 0)),
            "positive": int(p.count_roots(0, s.oo))}


def variations(p, endpoints):
    seq = [s.Poly(v, p.gens[0]) for v in s.sturm(p.as_expr(), p.gens[0])]
    out = {}
    for endpoint in endpoints:
        signs = []
        for f in seq:
            val = (s.sign(f.LC()) if endpoint == s.oo else
                   s.sign(f.LC())*(-1)**f.degree() if endpoint == -s.oo else
                   s.sign(f.eval(endpoint)))
            if val:
                signs.append(int(val))
        out[str(endpoint)] = {"signs": signs,
            "variations": sum(a != b for a, b in zip(signs, signs[1:]))}
    return out


# The configuration-only induction is false, already for a cubic, and also
# for a degree-seven input in the range explicitly assigned to this pass.
obstructions = []
shift = -s.Rational(29, 100)
assert shift < 0 and (1 + shift)**2 > s.Rational(1, 2)
root_lists = [
    [-s.Rational(51, 100), -s.Rational(49, 100), s.Rational(1, 2)],
    [-s.Rational(i, 10**6) for i in range(1000, 994, -1)]
      + [s.Rational(1, 1000)],
]
for roots in root_lists:
    p = s.Poly(s.prod(z-r for r in roots), z)
    q = operator(operator(p, shift), shift)
    pc, qc = counts(p), counts(q)
    assert pc["minus_one_to_zero"] == p.degree()-1 and pc["positive"] == 1
    assert pc["gcd_with_derivative_degree"] == 0
    assert qc["minus_one_to_zero"] == p.degree()-1 and qc["positive"] == 1
    assert qc["below_minus_one"] == 0 and qc["gcd_with_derivative_degree"] == 0
    assert s.discriminant(q.as_expr(), z) < 0
    assert p.nth(1) < 0  # Important limitation: not a shifted-power input.
    obstructions.append({"t": str(shift), "input_roots": [str(r) for r in roots],
        "input": str(p.as_expr()), "output": str(q.as_expr()),
        "input_counts": pc, "output_counts": qc,
        "output_discriminant": str(s.discriminant(q.as_expr(), z)),
        "output_sturm": variations(q, [-s.oo, -1, 0, s.oo]),
        "input_linear_coefficient": str(p.nth(1)),
        "interpretation": "Refutes configuration-only T_t squared preservation; neither input equals Q_(m,t)."})

# New whole-parameter-interval checks. A discriminant exclusion plus one
# simple-root sample and endpoint evaluations proves the stated finite strips.
whole_strips = []
p = s.Poly(1, z)
for m in range(1, 14):
    p = operator(p, t)
    if m in (7, 9, 11, 13):
        newton = sum(z**j * sum((-1)**k*s.binomial(j, k)*(j-k+t)**m
                                for k in range(j+1)) for j in range(m+1))
        assert s.expand(p.as_expr()-newton) == 0
        D = s.Poly(s.discriminant(p.as_expr(), z), t).primitive()[1]
        assert D.count_roots(-s.Rational(1, 3), 0) == 0
        sample = s.Poly(p.as_expr().subs(t, -s.Rational(1, 3)), z)
        sc = counts(sample)
        assert sc["minus_one_to_zero"] == m-1 and sc["positive"] == 1
        assert sc["gcd_with_derivative_degree"] == 0
        assert p.LC() == s.factorial(m)
        assert p.eval(0) == t**m and s.expand(p.eval(-1)-(t-1)**m) == 0
        whole_strips.append({"degree": m, "parameter_interval": "[-1/3,0)",
            "primitive_discriminant": str(D.as_expr()),
            "discriminant_degree": D.degree(), "discriminant_roots_in_closed_interval": 0,
            "discriminant_sturm": variations(D, [-s.Rational(1, 3), 0]),
            "sample_t": "-1/3", "sample_counts": sc,
            "independent_newton_formula_checked": True})
        print("Completed whole strip for degree", m, flush=True)

# Freeze the following NEW, unproved sufficient induction lemma before this
# exact finite stress test. It is not equivalent to the power-family assertion.
lemma = ("For -b<t<0, b=1-1/sqrt(2), let h have even degree d>=2, positive "
         "leading coefficient and d simple roots in (-1,0). Set delta=(1+2t)/(1+t)^2. "
         "If 0<lambda<=1/(h'(0)/h(0)+delta), then T_t^2[(z-lambda)h] has "
         "d+2 simple roots in (-1,0) and one simple positive root.")
parameters = [-s.Rational(1, 10000), -s.Rational(29, 100), -s.Rational(292893, 10**6)]
magnitudes = [s.Rational(1, 1000), s.Rational(1, 20), s.Rational(1, 5),
              s.Rational(1, 2), s.Rational(4, 5), s.Rational(19, 20), s.Rational(999, 1000)]
families = []
for d in (2, 4, 6):
    families.extend(itertools.combinations(magnitudes, d))
for d in (2, 4, 6, 8):
    families.append(tuple(s.Rational(1000+i, 10**6) for i in range(d)))
    families.append(tuple(s.Rational(990000+i, 10**6) for i in range(d)))
stress = []
for shift in parameters:
    assert shift < 0 and (1+shift)**2 > s.Rational(1, 2)
    delta = (1+2*shift)/(1+shift)**2
    for magnitudes_ in families:
        S = sum(1/a for a in magnitudes_)
        for ratio in (s.Rational(1, 1000), s.Rational(3, 4), s.Integer(1)):
            lam = ratio/(S+delta)
            p = s.Poly((z-lam)*s.prod(z+a for a in magnitudes_), z)
            q = operator(operator(p, shift), shift)
            assert p.nth(1) > 0 and q.nth(1) >= 0
            qc = counts(q)
            passed = (qc["minus_one_to_zero"] == len(magnitudes_)+2 and
                      qc["positive"] == 1 and qc["below_minus_one"] == 0 and
                      qc["gcd_with_derivative_degree"] == 0)
            stress.append({"t": str(shift), "negative_input_roots": [str(-a) for a in magnitudes_],
                "lambda": str(lam), "fraction_of_upper_bound": str(ratio),
                "output_counts": qc, "passed": passed})
            if not passed:
                print("EXACT FALSIFIER TO NEW LEMMA", stress[-1], flush=True)
    print("Completed strengthened-lemma stress tests at", shift, flush=True)

# A separately chosen attack on extending the NEW lemma to (-1/3,0).
# The extra coefficient inequality still holds, but real-rootedness fails.
outside_t = -s.Rational(333, 1000)
outside_p = s.Poly((z+s.Rational(9, 10))*(z+s.Rational(99, 100))*(z-s.Rational(1, 3)), z)
outside_q = operator(operator(outside_p, outside_t), outside_t)
outside_delta = (1+2*outside_t)/(1+outside_t)**2
assert -s.Rational(1, 3) < outside_t < 0
assert (1+outside_t)**2 < s.Rational(1, 2)  # Outside the actual proposed strip.
assert s.Rational(1, 3) < 1/(s.Rational(10, 9)+s.Rational(100, 99)+outside_delta)
assert outside_p.nth(1) > 0 and outside_q.nth(1) > 0
outside_counts = counts(outside_q)
assert outside_counts["minus_one_to_zero"] == 2 and outside_counts["positive"] == 1
assert outside_counts["below_minus_one"] == 0 and outside_counts["gcd_with_derivative_degree"] == 0
assert s.discriminant(outside_q.as_expr(), z) < 0
false_extension = {"refuted_claim": "The new sufficient lemma also holds throughout -1/3<t<0.",
    "t": str(outside_t), "input": str(outside_p.as_expr()),
    "input_roots": ["-99/100", "-9/10", "1/3"],
    "output": str(outside_q.as_expr()),
    "input_linear_coefficient": str(outside_p.nth(1)),
    "output_linear_coefficient": str(outside_q.nth(1)),
    "output_counts": outside_counts,
    "output_discriminant": str(s.discriminant(outside_q.as_expr(), z)),
    "output_sturm": variations(outside_q, [-s.oo, -1, 0, s.oo]),
    "scope": "Refutes only the larger-strip operator extension, not O or the original conjecture."}

out = {"job_id": JOB, "source_sha256": SOURCE_HASH,
       "python": platform.python_version(), "sympy": s.__version__,
       "arithmetic": "Exact rational arithmetic, symbolic discriminants, Sturm sequences; no floating-point decisions.",
       "configuration_only_obstructions": obstructions,
       "new_whole_strips": whole_strips,
       "unproved_sufficient_lemma_v1": lemma,
       "lemma_exact_finite_tests": stress,
       "lemma_test_count": len(stress),
       "lemma_failed_test_count": sum(not v["passed"] for v in stress),
       "false_larger_strip_extension": false_extension,
       "limitations": "Whole-strip results cover only the displayed four new degrees. Finite tests do not prove the proposed lemma or O in all degrees. No independent audit or novelty certification."}
path = ROOT / "evidence" / "two-step-pass-2.json"
tmp = path.with_suffix(".json.tmp")
tmp.write_text(json.dumps(out, indent=2)+"\n")
os.replace(tmp, path)
print(json.dumps({"new_strip_degrees": [v["degree"] for v in whole_strips],
                  "lemma_test_count": len(stress),
                  "lemma_failed_test_count": out["lemma_failed_test_count"]}, indent=2))
