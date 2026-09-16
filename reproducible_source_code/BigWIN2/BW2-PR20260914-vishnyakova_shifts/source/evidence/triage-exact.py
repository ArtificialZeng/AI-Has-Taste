"""Exact triage calibration, not an independent audit or a uniform proof.

Run from the project directory: python3 evidence/triage-exact.py
The JSON output is written atomically beside this script.
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
z, t, v, x = s.symbols("z t v x")


def q(n):
    return s.expand(sum(z**j * sum(
        (-1)**ell * s.binomial(j, ell) * (j-ell+t)**n
        for ell in range(j+1)) for j in range(n+1)))


def root_count(poly):
    return sum(int(m) * int(f.count_roots(-1, 0))
               for f, m in s.Poly(poly, z).sqf_list()[1])


def sturm_signs(poly, var, endpoint):
    out = []
    for item in s.sturm(poly, var):
        p = s.Poly(item, var)
        if endpoint == s.oo:
            value = s.sign(p.LC())
        elif endpoint == -s.oo:
            value = s.sign(p.LC()) * (-1)**p.degree()
        else:
            value = s.sign(p.eval(endpoint))
        if value:
            out.append(int(value))
    return out


def variations(signs):
    return sum(a != b for a, b in zip(signs, signs[1:]))


q2, q4 = q(2), q(4)
assert s.expand(q2 - (t*t+(2*t+1)*z+2*z*z)) == 0
d2 = s.factor(s.discriminant(q2, z))
assert d2 == -4*t*t+4*t+1
for endpoint in [(1-s.sqrt(2))/2, (1+s.sqrt(2))/2]:
    repeated_root = -(2*endpoint+1)/4
    assert s.simplify(q2.subs({t: endpoint, z: repeated_root})) == 0
    assert -1 < repeated_root < 0

H = 3456*v**5-9504*v**4+11304*v**3-7046*v**2+2378*v-361
d4 = s.factor(s.discriminant(q4, z))
assert s.expand(d4 - 24*(4*(t-s.Rational(1,2))**2-5)
                * H.subs(v, (t-s.Rational(1,2))**2)) == 0
signs = {str(end): sturm_signs(H, v, end) for end in [-s.oo, 0, s.oo]}
V = {key: variations(value) for key, value in signs.items()}
assert V["-oo"]-V["oo"] == 1
assert V["0"]-V["oo"] == 1
vlo, vhi = s.Rational(42488,77697), s.Rational(77417,141571)
assert s.Poly(H,v).count_roots(vlo,vhi) == 1
assert s.Rational(1,4) < vlo < vhi < 1
# alpha = 1/2 - sqrt(v_*). Exact rational brackets, no float decisions.
alo, ahi = s.Rational(-240,1000), s.Rational(-239,1000)
assert (s.Rational(1,2)-ahi)**2 < vlo
assert vhi < (s.Rational(1,2)-alo)**2

samples = []
for shift, expected in [(-1,0), (s.Rational(-1,2),2),
                        (s.Rational(-1,4),2), (s.Rational(-23,100),4),
                        (0,4), (s.Rational(1,2),4), (1,4),
                        (s.Rational(3,2),2), (2,0)]:
    count = root_count(q4.subs(t,shift))
    assert count == expected
    samples.append({"t":str(shift), "roots_in_closed_interval":count,
                    "discriminant_sign":int(s.sign(d4.subs(t,shift)))})

for n in range(1,7):
    assert s.expand(s.diff(q(n),t)-n*q(n-1)) == 0
    assert s.expand(q(n)-(z+t)*q(n-1)-z*(1+z)*s.diff(q(n-1),z)) == 0
    assert s.expand(q(n).subs(t,1-t)-(-1)**n*q(n).subs(z,-1-z)) == 0
    assert s.expand(q(n).subs(z,0)-t**n) == 0
    assert s.expand(q(n).subs(z,-1)-(t-1)**n) == 0
    # Independently assemble the generating numerator from its coefficients.
    numerator = sum(x**j * sum((-1)**ell*s.binomial(n+1,ell)
                    *(j-ell+t)**n for ell in range(j+1))
                    for j in range(n+1))
    assert s.cancel((1-x)**n*q(n).subs(z,x/(1-x))-numerator) == 0

result = {
    "job_id":"primary-20260914-vishnyakova-shifts-triage-b88a2e27f2c3",
    "source_sha256":SOURCE_HASH,
    "python":platform.python_version(), "sympy":s.__version__,
    "arithmetic":"exact symbolic identities and rational Sturm counts",
    "randomness":False,
    "q2":str(q2), "discriminant_q2":str(d2),
    "q4":str(q4), "discriminant_q4":str(d4), "H":str(H),
    "H_sturm_signs":signs, "H_sturm_variations":V,
    "H_unique_real_root_bracket":[str(vlo),str(vhi)],
    "alpha_definition":"1/2-sqrt(v_*), where H(v_*)=0",
    "alpha_rational_bracket":[str(alo),str(ahi)],
    "quartic_samples":samples,
    "identity_check_degrees":[1,6],
    "scope":"Quartic cell certificate plus identities; see triage-exact.md for the completeness argument. No uniform even-degree theorem, novelty certification, or independent review."
}
out = ROOT / "evidence" / "triage-exact.json"
temp = out.with_suffix(".json.tmp")
temp.write_text(json.dumps(result,indent=2)+"\n")
os.replace(temp,out)
print(json.dumps(result,indent=2))
