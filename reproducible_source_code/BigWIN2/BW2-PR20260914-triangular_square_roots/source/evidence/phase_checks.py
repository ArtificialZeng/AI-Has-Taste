"""Reproduce exact checks of the Delannoy-square phase proof.

Run: python3 evidence/phase_checks.py
Numerical phase inversion only discovers rational samples; every serialized
sample sign and root enclosure is then checked with exact integer arithmetic.
The all-degree theorem is the argument in delannoy_phase_proof.md, not this
finite computation. No random search, remote process, or background worker.
"""
from pathlib import Path
from math import comb
from fractions import Fraction
import hashlib
import json
import platform

import mpmath as mp
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
JOB = "primary-20260914-triangular-square-roots-research-8c4db654213f"
SOURCE_HASH = "a1a75e5793dcd6534b63902eb3b6d415dfd60e8f129376f7af671b7b9401f1f3"
assert hashlib.sha256((ROOT / "source.md").read_bytes()).hexdigest() == SOURCE_HASH
x, u = sp.symbols("x u")
h = lambda z: z * (z-1) / (z+1)
v = (1-u)/(1+u)
r2 = sp.sqrt(2)
a, b, c, u0 = -4-3*r2, -3-2*r2, -3+2*r2, -1-r2
assert sp.simplify(h(b)-a) == 0
assert sp.simplify(h(u0)-b) == 0
assert sp.simplify(v.subs(u,b)+r2) == 0
assert sp.cancel(u+v-1-h(u)) == 0
assert sp.cancel(u*v+h(u)) == 0
assert sp.cancel(sp.diff(h(u),u)-(1-2/(u+1)**2)) == 0

# Independent path DP and ordinary matrix multiplication, through n=24.
SMALL = 24
grid = [[0]*(SMALL+1) for _ in range(SMALL+1)]
grid[0][0] = 1
for p in range(SMALL+1):
    for q in range(SMALL+1):
        if p or q:
            grid[p][q] = ((grid[p-1][q] if p else 0)
                          + (grid[p][q-1] if q else 0)
                          + (grid[p-1][q-1] if p and q else 0))
D = [[grid[n-k][k] for k in range(n+1)] for n in range(SMALL+1)]
assert all(D[n][k] == sum(comb(n-k,j)*comb(k,j)*2**j
                          for j in range(min(n-k,k)+1))
           for n in range(SMALL+1) for k in range(n+1))
rows = [[sum(D[n][i]*D[i][k] for i in range(k,n+1))
         for k in range(n+1)] for n in range(SMALL+1)]
poly = lambda row: sp.Poly.from_list(row[::-1],x,domain=sp.ZZ)
d = [poly(row) for row in D]
G = [poly(row) for row in rows]
for n in range(4,SMALL+1):
    assert G[n] == (x+3)*G[n-1]+(x-1)*(G[n-2]+G[n-3])+x*G[n-4]

# Formal rational substitution, separate from root/phase computations.
for n in range(9):
    expr = (u*d[n].as_expr().subs(x,u)-v*d[n].as_expr().subs(x,v))/(u-v)
    assert sp.cancel(expr-G[n].as_expr().subs(x,h(u))) == 0

def within_enclosure(q):
    """Exactly certify -4-3 sqrt(2) < rational q < -3+2 sqrt(2)."""
    t, s = q+4, q+3
    return (t >= 0 or t*t < 18) and (s <= 0 or s*s < 8)

small_counts = []
for n in range(1,SMALL+1):
    p = G[n]
    intervals = p.intervals(eps=sp.Rational(1,10**8))
    assert len(intervals) == n and all(mult == 1 for _,mult in intervals)
    assert all(within_enclosure(Fraction(int(lo.p),int(lo.q)))
               and within_enclosure(Fraction(int(hi.p),int(hi.q)))
               for (lo,hi),mult in intervals)
    small_counts.append({"n":n,"simple_real_roots":len(intervals),
                         "all_isolating_intervals_inside_claimed_enclosure":True})

# Two exact falsifications of more general intermediate assertions.
T = lambda p: sum((d[k]*int(coef) for (k,),coef in sp.Poly(p,x).terms()),
                  sp.Poly(0,x))
pal_input = (x*x+6*x+1)**3
pal_output = T(pal_input)
assert pal_output == sp.Poly(x**6+29*x**5+314*x**4+1542*x**3
                             +3305*x*x+2561*x+512,x)
assert pal_output.count_roots(-sp.oo,sp.oo) == 4
assert sp.gcd(pal_output,pal_output.diff()).degree() == 0
K4 = T(sp.cancel((d[4].as_expr()-1)/x))
assert K4 == sp.Poly((x+7)*(x+4)*(x+1),x)
shifted = sp.Poly(G[4].as_expr().subs(x,-7-x),x)
assert shifted == sp.Poly(x**4+14*x**3+61*x*x+80*x+1,x)
assert all(coef > 0 for coef in shifted.all_coeffs())

# Generate exact coefficient rows up to the held-out verification degrees.
DEGREES = [1,2,3,4,5,8,16,31,64,128,257]
for n in range(SMALL+1,max(DEGREES)+1):
    row = [0]*(n+1)
    for lag,constant,linear in [(1,3,1),(2,-1,1),(3,-1,1),(4,0,1)]:
        for k,coef in enumerate(rows[n-lag]):
            row[k] += constant*coef
            row[k+1] += linear*coef
    assert row[-1] == 1
    rows.append(row)

mp.mp.dps = 90
rt = mp.sqrt(2)
left, join, right = -4-3*rt, -3-2*rt, -3+2*rt
uu0 = -1-rt
th0 = mp.acos((1+uu0)/(2*mp.sqrt(-uu0)))
DEN = 10**40

def upper_phase(xx, N):
    uu = (1+xx+mp.j*mp.sqrt(-(xx*xx+6*xx+1)))/2
    ss = mp.sqrt(uu*uu+6*uu+1)
    ww = (1+uu+ss)/2
    return N*mp.arg(ww)+mp.arg(uu)-mp.arg(ss)

def phase_sample(n,j,m):
    N = n+1
    target = (mp.mpf(j)+mp.mpf('0.5'))*mp.pi
    if j < m:
        lo,hi = join,right
        # A continuous-level bisection; monotonicity is not a proof dependency.
        for _ in range(240):
            mid = (lo+hi)/2
            if upper_phase(mid,N) > target:
                lo = mid
            else:
                hi = mid
        return (lo+hi)/2
    theta = target/N
    # cos(theta)=(1-r^2)/(2r), r=sqrt(-u)>0.
    co = mp.cos(theta)
    rr = mp.sqrt(1+co*co)-co
    uu = -rr*rr
    return uu*(uu-1)/(uu+1)

def homogeneous_sign(row,p,q):
    """Sign of q^degree G(p/q), using integers only; q>0."""
    value = row[-1]
    power = q
    for coef in reversed(row[:-1]):
        value = value*p+coef*power
        power *= q
    return (value>0)-(value<0)

certificates = []
for n in DEGREES:
    m = int(mp.ceil((n+1)*th0/mp.pi))
    numerators = [int(mp.nint(phase_sample(n,j,m)*DEN)) for j in range(n+1)]
    assert all(numerators[j] > numerators[j+1] for j in range(n))
    assert all(within_enclosure(Fraction(p,DEN)) for p in numerators)
    signs = [homogeneous_sign(rows[n],p,DEN) for p in numerators]
    assert signs == [(-1)**j for j in range(n+1)], (n,m,signs)
    certificates.append({
        "n":n,"upper_sample_count":m,"lower_sample_count":n+1-m,
        "denominator":str(DEN),"numerators_in_decreasing_order":[str(p) for p in numerators],
        "exact_signs":signs,"coefficients_ascending":rows[n],
        "certified_conclusion":"n disjoint sign changes inside the enclosure; degree n, hence n simple roots"
    })

result = {
    "job_id":JOB,"source_sha256":SOURCE_HASH,
    "python":platform.python_version(),"sympy":sp.__version__,"mpmath":mp.__version__,
    "symbolic_identities":"outer-root relations, h endpoint images/derivative, divided difference for n=0..8",
    "independent_lattice_DP_and_ordinary_square_range":[0,SMALL],
    "small_exact_isolation":small_counts,
    "sample_discovery":{"precision_decimal_digits":90,"bisection_steps":240,
                        "rational_denominator":str(DEN),"seed":None,
                        "warning":"Numerical phase inversion alone is not a certificate."},
    "exact_sign_certificates":certificates,
    "failed_routes":{
        "palindromic_preservation":{"input":str(pal_input),"output":str(pal_output.as_expr()),
                                    "distinct_real_roots":4,"degree":6,
                                    "scope":"Refutes general palindromic real-root preservation; not D^2."},
        "auxiliary_interlacing":{"K4":str(K4.as_expr()),"G4_at_minus7":1,
                                 "G4_minus7_minus_x":str(shifted.as_expr()),
                                 "conclusion":"K4 has root -7 while G4 has no root at or below -7, so K4 does not interlace G4."}
    },
    "limitations":"The exact finite certificates check the proposed mechanism. The uniform theorem depends on the written proof and remains subject to fresh referee review. No A^2 resolution or consecutive interlacing theorem."
}
target = ROOT/"evidence/phase_checks.json"
temp = target.with_suffix(".json.tmp")
temp.write_text(json.dumps(result,indent=2)+"\n")
temp.replace(target)
print(json.dumps({"output":str(target.relative_to(ROOT)),"exact_sign_degrees":DEGREES,
                  "total_rational_sample_signs":sum(n+1 for n in DEGREES),
                  "DP_isolation_range":[1,SMALL],"palindromic_counterexample_real_roots":4}))
