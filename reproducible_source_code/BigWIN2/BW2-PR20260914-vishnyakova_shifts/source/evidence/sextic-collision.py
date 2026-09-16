"""Exact sextic collision certificate; no floating-point decisions.

Run from the project root: python3 evidence/sextic-collision.py
The output JSON is replaced atomically. This is research evidence, not a referee.
"""
import hashlib
import json
import os
import platform
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parent.parent
JOB = "primary-20260914-vishnyakova-shifts-research-77f35a690f9a"
SOURCE_HASH = "599d20eb671a5110cc3ae01b0f602ff5460c237a42052ac704e602aca2e4dda8"
assert hashlib.sha256((ROOT / "source.md").read_bytes()).hexdigest() == SOURCE_HASH
t, z = s.symbols("t z")
Q = s.Integer(1)
for n in range(1, 7):
    Q = s.expand((z+t)*Q + z*(1+z)*s.diff(Q, z))
newton = sum(z**j * sum((-1)**k*s.binomial(j, k)*(j-k+t)**6
                         for k in range(j+1)) for j in range(7))
assert s.expand(Q-newton) == 0
D = s.Poly(s.discriminant(Q, z), t)
content, F = D.primitive()
if F.LC() < 0:
    F, content = -F, -content
assert s.gcd(F, F.diff()).degree() == 0
intervals = F.intervals(eps=s.Rational(1, 10**25))
assert len(intervals) == 6 and all(m == 1 for _, m in intervals)
assert F.count_roots(-s.Rational(1, 2), s.Rational(3, 2)) == 2
negative = [(lo, hi) for (lo, hi), _ in intervals if -s.Rational(1, 2) < lo < hi < 0]
assert len(negative) == 1
T = negative[0]
assert -s.Rational(255, 1000) < T[0] < T[1] < -s.Rational(254, 1000)
# alpha > -b: b=1-1/sqrt(2), certified without irrational arithmetic.
assert (1+T[0])**2 > s.Rational(1, 2)
assert s.expand(F.as_expr().subs(t, 1-t)-F.as_expr()) == 0
assert s.expand(Q.subs(t, 1-t)-Q.subs(z, -1-z)) == 0
assert Q.subs(z, 0) == t**6 and s.expand(Q.subs(z, -1)-(t-1)**6) == 0


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def mul(a, b):
    p = [x*y for x in a for y in b]
    return min(p), max(p)


def neg(a):
    return -a[1], -a[0]


def inv(a):
    assert not a[0] <= 0 <= a[1]
    return 1/a[1], 1/a[0]


def power(a, n):
    p = (s.Integer(1), s.Integer(1))
    for _ in range(n):
        p = mul(p, a)
    return p


def evaluate(poly, vars_, boxes):
    val = (s.Integer(0), s.Integer(0))
    for degrees, coeff in s.Poly(poly, *vars_).terms():
        term = (coeff, coeff)
        for degree, box in zip(degrees, boxes):
            term = mul(term, power(box, degree))
        val = add(val, term)
    return val


def rational_outer(box, scale=10**12):
    return [str(s.floor(box[0]*scale)/scale), str(s.ceiling(box[1]*scale)/scale)]


subres = s.subresultants(Q, s.diff(Q, z), z)
assert s.degree(subres[-2], z) == 1
assert s.expand(subres[-1] + 720*D.as_expr()) == 0
Araw, Braw = s.Poly(subres[-2], z).all_coeffs()
common = s.gcd(s.Poly(Araw, t).content(), s.Poly(Braw, t).content())
A, B = s.Poly(Araw/common, t), s.Poly(Braw/common, t)
Ab, Bb = evaluate(A.as_expr(), (t,), (T,)), evaluate(B.as_expr(), (t,), (T,))
assert Ab[0] > 0
Rcomputed = mul(neg(Bb), inv(Ab))
R = (-s.Rational(325753388855, 10**14), -s.Rational(325753388854, 10**14))
assert R[0] < Rcomputed[0] <= Rcomputed[1] < R[1]
assert -1 < R[0] < R[1] < 0

# Check both defining equations modulo F after substituting r=-B/A.
# The subresultant also proves there is exactly one double root, since its
# specialization is a nonzero linear polynomial and the resultant vanishes.
for p in (Q, s.diff(Q, z)):
    pol = s.Poly(p, z)
    degree = pol.degree()
    numerator = s.Poly(0, t)
    for (j,), c in pol.terms():
        numerator += s.Poly(c, t)*(-B)**j*A**(degree-j)
    assert numerator.rem(F).is_zero

Qt = evaluate(s.diff(Q, t), (t, z), (T, R))
Qzz = evaluate(s.diff(Q, z, 2), (t, z), (T, R))
assert Qt[1] < 0 and Qzz[0] > 0
sigma = mul(neg(Qt), inv(Qzz))
assert sigma[0] > 0

# One sample in each discriminant cell of the necessary range [-1/2,3/2].
# Endpoints z=-1,0 are roots only at t=1,0, so cells may be split there.
samples = []
for shift, expected in [(s.Rational(-1, 2), 4), (s.Rational(-13, 50), 4),
                         (s.Rational(-1, 4), 6), (0, 6),
                         (s.Rational(1, 2), 6), (1, 6),
                         (s.Rational(5, 4), 6), (s.Rational(3, 2), 4)]:
    p = s.Poly(Q.subs(t, shift), z)
    assert s.gcd(p, p.diff()).degree() == 0
    count = int(p.count_roots(-1, 0))
    assert count == expected
    samples.append({"t": str(shift), "distinct_roots_in_closed_interval": count})

signs = {}
sturm = [s.Poly(p, t) for p in s.sturm(F.as_expr(), t)]
for endpoint in [-s.oo, -s.Rational(1, 2), T[0], T[1], 0, s.Rational(3, 2), s.oo]:
    seq = []
    for p in sturm:
        value = (s.sign(p.LC()) if endpoint == s.oo else
                 s.sign(p.LC())*(-1)**p.degree() if endpoint == -s.oo else
                 s.sign(p.eval(endpoint)))
        if value:
            seq.append(int(value))
    signs[str(endpoint)] = {"signs": seq,
        "variations": sum(a != b for a, b in zip(seq, seq[1:]))}

out = {
    "job_id": JOB, "source_sha256": SOURCE_HASH,
    "python": platform.python_version(), "sympy": s.__version__,
    "arithmetic": "exact integers, rational polynomial remainders, Sturm isolation, rational interval arithmetic",
    "Q6": str(Q), "discriminant_content": str(content),
    "discriminant_primitive_positive_leading": str(F.as_expr()),
    "F_squarefree": True,
    "all_real_discriminant_roots": [{"interval": [str(lo), str(hi)], "multiplicity": m}
                                     for (lo, hi), m in intervals],
    "sturm": signs,
    "alpha_interval": [str(x) for x in T],
    "alpha_coarse_interval": ["-51/200", "-127/500"],
    "linear_subresultant_normalized": {"A": str(A.as_expr()), "B": str(B.as_expr())},
    "A_interval_outer": rational_outer(Ab),
    "repeated_root_definition": "r=-B(alpha)/A(alpha), F(alpha)=0",
    "repeated_root_interval": [str(x) for x in R],
    "Qt_interval_outer": rational_outer(Qt), "Qzz_interval_outer": rational_outer(Qzz),
    "sigma_interval_outer": rational_outer(sigma),
    "Qt_negative": True, "Qzz_positive": True, "sigma_positive": True,
    "higher_multiplicities_in_admissible_exterior_range": "none; nonzero linear subresultant and Qzz>0",
    "samples": samples,
    "scope": "One exterior admissible collision for n=6; complete M6 cell classification explained in sextic-collision.md. No all-degree sign or nesting theorem."
}
path = ROOT / "evidence" / "sextic-collision.json"
tmp = path.with_suffix(".json.tmp")
tmp.write_text(json.dumps(out, indent=2)+"\n")
os.replace(tmp, path)
print(json.dumps({key: out[key] for key in ["alpha_coarse_interval", "repeated_root_interval",
    "Qt_interval_outer", "Qzz_interval_outer", "sigma_interval_outer", "samples"]}, indent=2))
