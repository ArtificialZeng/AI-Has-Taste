"""Exact triage checks; run from PROJECT_DIR with python3 evidence/triage_checks.py."""
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import re
import sympy as S

x, a, b, t = S.symbols('x a b t', real=True)

def graph(r, s, ell):
    n = r+s+ell-1
    edges = [(i, i+1) for i in range(r-1)] + [(r-1, 0)]
    edges += [(r+i, r+i+1) for i in range(s-1)] + [(r+s-1, r)]
    path = [0] + list(range(r+s, n)) + [r]
    edges += list(zip(path, path[1:]))
    return n, edges

def matching(n, edges, removed=()):
    neighbors = [0]*n
    for u,v in edges:
        neighbors[u] |= 1 << v
        neighbors[v] |= 1 << u
    @lru_cache(None)
    def counts(mask):
        if not mask:
            return (1,)
        v = (mask & -mask).bit_length()-1
        rest = mask ^ (1 << v)
        out = list(counts(rest)) + [0]
        nbr = neighbors[v] & rest
        while nbr:
            ubit = nbr & -nbr
            nbr ^= ubit
            for k,c in enumerate(counts(rest ^ ubit)):
                out[k+1] += c
        while len(out)>1 and out[-1]==0:
            out.pop()
        return tuple(out)
    mask = (1 << n)-1
    for v in removed:
        mask ^= 1 << v
    order = mask.bit_count()
    return S.Add(*(c*(-1)**k*x**(order-2*k) for k,c in enumerate(counts(mask))))

def predicted(r,s,ell):
    n,edges=graph(r,s,ell)
    return S.expand(matching(n,edges)-2*a*matching(n,edges,range(r))
                    -2*b*matching(n,edges,range(r,r+s))
                    +4*a*b*matching(n,edges,range(r+s)))

p = predicted(3,3,1)
expected = x**6-7*x**4+11*x**2-1-2*(a+b)*(x**3-3*x)+4*a*b
assert S.expand(p-expected)==0

matrix_checks=[]
z=S.Rational(3,5)+S.I*S.Rational(4,5)
w=S.Rational(5,13)+S.I*S.Rational(12,13)
for r,s,ell in [(3,3,1),(3,5,1),(5,3,3),(5,5,3)]:
    n,edges=graph(r,s,ell)
    A=S.zeros(n)
    for u,v in edges:
        gain=z if (u,v)==(r-1,0) else w if (u,v)==(r+s-1,r) else S.Integer(1)
        A[u,v]=gain
        A[v,u]=S.conjugate(gain)
    cp=A.charpoly().as_expr()
    cp=cp.subs(next(iter(cp.free_symbols)),x)
    assert S.expand(cp-predicted(r,s,ell).subs({a:S.re(z),b:S.re(w)}))==0
    matrix_checks.append([r,s,ell])

det_checks=[]
for r in (3,5,7):
    for s in (3,5,7):
        for ell in (1,3,5):
            n=r+s+ell-1
            aa=(-1)**((r+1)//2)*a
            bb=(-1)**((s+1)//2)*b
            det=predicted(r,s,ell).subs(x,0)
            assert S.expand(det-(-1)**(n//2)*(1-4*aa*bb))==0
            det_checks.append([r,s,ell])

half=S.factor(p.subs({a:S.Rational(1,2),b:S.Rational(1,2)}))
assert S.expand(half-x*(x+2)*(x*x-x-3)*(x*x-x-1))==0
fp=x**3-x*x-3*x+1-2*a
fm=x**3+x*x-3*x-1-2*a
assert S.expand(p.subs(b,a)-fp*fm)==0

q=S.Poly(x**3-7*x*x+11*x-1,x)
intervals=[(S.Rational(9678807,10**8),S.Rational(9678808,10**8)),
           (S.Rational(219393656,10**8),S.Rational(219393657,10**8)),
           (S.Rational(470927535,10**8),S.Rational(470927537,10**8))]
assert all(q.count_roots(l,u)==1 for l,u in intervals)
# Rational square-root enclosures, checked by integer/rational arithmetic.
sqrt_bounds=[]
for l,u in intervals:
    scale=10**9
    k=int(S.sqrt(l).evalf(30)*scale)
    lo=S.Rational(k,scale)
    hi=S.Rational(k+2,scale)
    while hi*hi<=u:
        hi+=S.Rational(1,scale)
    assert 0<lo and lo*lo<l and hi*hi>u
    sqrt_bounds.append((lo,hi))
origin_low=2*sum(v[0] for v in sqrt_bounds)
half_upper=2+S.Rational(3605551276,10**9)+S.Rational(2236067978,10**9)
assert S.Rational(3605551276,10**9)**2>13
assert S.Rational(2236067978,10**9)**2>5
assert half_upper<origin_low

Z=1+7*t*t+11*t**4+t**6
X=2*t**3*(1+3*t*t)
W=4*t**6
AA=Z-W/4
BB=X
numerator=S.factor(-W*AA/2+X*BB)
assert S.expand(numerator-2*t**6*(1+5*t*t+7*t**4))==0
U=(S.sqrt(13)-1)/2
v=(1+S.sqrt(5))/2
wroot=(1+S.sqrt(13))/2
left=4*(1/(5*v)-1/(6-U))
right=4*(1/(6+wroot)+1/(5*v))
assert S.simplify(right-left)==S.Rational(4,3)

source_hash=hashlib.sha256(Path('source.md').read_bytes()).hexdigest()
assert source_hash=='ec7265dcc8f807c129c4343be3ebf171d3c8a7b56c87316810172368a8e016fa'
out={'job_id':'primary-20260914-dumbbell-min-energy-triage-f6149d7dafbe',
     'source_sha256':source_hash,'sympy_version':S.__version__,
     'matrix_matching_polynomial_checks':matrix_checks,
     'matrix_cycle_gains':['3/5+4i/5','5/13+12i/13'],
     'exact_determinant_check_triples':det_checks,
     'D331_polynomial':str(p),'half_factorization':str(half),
     'origin_squared_root_intervals':[[str(l),str(u)] for l,u in intervals],
     'origin_energy_rational_lower_bound':str(origin_low),
     'known_half_energy_rational_upper_bound':str(half_upper),
     'stationarity_numerator':str(numerator),
     'diagonal_derivative_left':str(S.simplify(left)),
     'diagonal_derivative_right':str(S.simplify(right)),
     'diagonal_derivative_jump':'4/3',
     'all_assertions_passed':True,
     'scope':'Exact finite algebra checks; global D331 argument is in triage-math.md; no independent referee.'}
Path('evidence/triage-checks.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))

registry=Path('/home/ailab/4math-open-problems/registry/problems.jsonl')
rows=[json.loads(s) for s in registry.read_text().splitlines() if s.strip()]
exact=[r.get('id') for r in rows if re.search(r'dumbbell|2604\.27785|unit.?gain',json.dumps(r),re.I)]
record={'date':'2026-09-14','record_count':len(rows),
        'sha256':hashlib.sha256(registry.read_bytes()).hexdigest(),
        'target_term_matches':exact,
        'semantic_comparison':'Registry win-00041-p02 studies squared positive/negative energies of unicyclic ordinary graphs, not absolute energy of two-cycle unit-gain graphs.',
        'supervisor_only':'The Windows Excel corpus screen in literature/dedup.json was not independently repeated; its quoted thrackle and signed theta targets have different objects or gain domains.'}
Path('evidence/triage-registry.json').write_text(json.dumps(record,indent=2)+'\n')
