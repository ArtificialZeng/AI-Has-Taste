"""Reproduce exact convention tests and the bounded floating structural screen."""
from pathlib import Path
import json
import math
import sympy as s
import numpy as np

OUT = Path(__file__).resolve().parent
z, x, c, q, t, K, k = s.symbols('z x c q t K k', positive=True)

def connected_counts(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v); adj[v].add(u)
    counts = [0]*(n+1)
    for mask in range(1, 1 << n):
        chosen = {i for i in range(n) if mask >> i & 1}
        reached = {next(iter(chosen))}
        todo = list(reached)
        while todo:
            u = todo.pop()
            for v in adj[u] & chosen - reached:
                reached.add(v); todo.append(v)
        if reached == chosen:
            counts[len(chosen)] += 1
    return counts

cases = []
for n in range(2, 8):
    for name, edges, formula in [
        ('path', [(j, j+1) for j in range(n-1)], sum((n-j+1)*z**j for j in range(1,n+1))),
        ('star', [(0,j) for j in range(1,n)], z*((1+z)**(n-1)+n-1))]:
        cc = connected_counts(n, edges)
        assert s.expand(sum(cc[j]*z**j for j in range(n+1))-formula) == 0
        cases.append({'family':name,'n':n,'counts':cc})
for a in range(1, 4):
    for b in range(1, 4):
        n=a+b+2
        edges=[(0,1)]+[(0,j) for j in range(2,a+2)]+[(1,j) for j in range(a+2,n)]
        cc=connected_counts(n,edges)
        formula=z*(a+b+(1+z)**a+(1+z)**b+z*(1+z)**(a+b))
        assert s.expand(sum(cc[j]*z**j for j in range(n+1))-formula)==0
        cases.append({'family':'double-star','a':a,'b':b,'n':n,'counts':cc})

witness=-s.Rational(1,2)+s.Rational(49,100)*s.I
L=s.expand(witness*(1+witness)**3)
mod2=s.expand((1+L)*s.conjugate(1+L))
assert mod2>1
assert s.Rational(49,100)**2<s.Rational(1,4)
H=s.expand(4*(x+1)**3-3*(x+1)**2+2*(x+1)-1)
assert H==4*x**3+9*x**2+8*x+2
assert [9,9*8-4*2,2*(9*8-4*2)]==[9,64,128]
margin_after_substitution=((c+1)*(q+1)/c-c-(q+1)/c**2-q)/((c+1)*(q+1)/c)
assert s.factor(margin_after_substitution-(c-1)*(q+1-c**2)/(c*(c+1)*(q+1)))==0
logf=-k*s.log(t)-s.log(K-t*t)/2
assert s.simplify(s.diff(logf,t,2)-(k/t**2+(K+t*t)/(K-t*t)**2))==0
report={'kind':'exact finite checks and symbolic identities, not general root certification',
        'cases':cases,'failed_invariant_witness':{'z':str(witness),'L':str(L),'modulus_squared':str(mod2)},
        'P4_H':str(H),'P4_Hurwitz_determinants':[9,64,128],
        'endpoint_factorization_verified':True,'log_second_derivative_verified':True}
(OUT/'exact-checks.json').write_text(json.dumps(report,indent=2)+'\n')

qs=[2,3,4,5,6,8,12,20,40,80,160]
rows=[]
for qq in qs:
    cc=(qq+1)**(1/(qq+1)); R=cc+.5
    best=(float('inf'),None,None)
    for a in range(1,qq//2+1):
        b=qq-a
        for theta in np.linspace(0,math.pi,2001):
            zz=-.5+R*complex(math.cos(theta),math.sin(theta)); rr=abs(zz+1)
            gap=1-(rr**a+rr**b+qq)/(abs(zz)*rr**qq)
            if gap<best[0]:best=(gap,a,float(theta))
    rows.append({'q':qq,'n':qq+2,'min_normalized_domination_gap':best[0],'a':best[1],'theta':best[2]})
(OUT/'double-star-float-screen.json').write_text(json.dumps({
    'status':'floating exploratory samples only; no interval certificate',
    'q_values':qs,'a_range':'1..floor(q/2)','theta_grid':'2001 equally spaced points in [0,pi]',
    'results':rows},indent=2)+'\n')
print(json.dumps({'exact_cases':len(cases),'exact_identity_checks':'passed','floating_samples':sum(qq//2 for qq in qs)*2001}))
