"""Screen a specific algebraic proof route; conclusions are scoped in output."""
import json
import signal
import time
from pathlib import Path
import sympy as S

signal.alarm(40)
started=time.monotonic()
m,n,t,z,x,y=S.symbols('m n t z x y')
raw=json.loads(Path('evidence/k4-rational.json').read_text())
P=S.Poly(S.sympify(raw['numerator']),t).primitive()[1]
J=S.prod((m-i)*(n-j)-(3-i-j)*t for i in range(3) for j in range(3-i))
D=S.Poly(S.expand(P.as_expr()-J),t)
R=m*n/4
bound44=sum(abs(D.nth(i).subs({m:4,n:4}))*4**i for i in range(6))
rouche_ratio=S.cancel(bound44/J.subs({m:4,n:4,t:4}))
H=S.Poly(S.expand(sum(P.nth(i)*(m*n)**i*4**(6-i)*(1-z)**i*(1+z)**(6-i) for i in range(7))),z)
h=[S.cancel(c/(m*n)**3) for c in H.all_coeffs()]
def signs(poly):
    q=S.Poly(poly,x,y)
    coeff=q.coeffs()
    negative=[{'monomial':list(mon),'coefficient':str(c)} for mon,c in q.terms() if c<0]
    return {'degree':q.total_degree(),'terms':len(coeff),
            'negative_coefficient_count':len(negative),
            'negative_examples':negative[:3],
            'constant':str(q.coeff_monomial(1)),
            'all_coefficients_nonnegative':all(c>=0 for c in coeff)}
hs=[S.Poly(c.subs({m:x+4,n:y+4}),x,y).as_expr() for c in h]
minors=[hs[1],S.expand(hs[1]*hs[2]-hs[0]*hs[3])]
out={'scope':'Exact first-stage certificate feasibility only; higher Hurwitz minors untested.',
     'transformation':'H(z)=4^6/(m*n)^3*(1+z)^6*P((m*n/4)*(1-z)/(1+z)), P primitive in t',
     'parameter_shift':'m=4+x,n=4+y',
     'h_coefficients_descending_z':[str(c) for c in h],
     'shifted_h_coefficient_signs':[signs(c) for c in hs],
     'shifted_hurwitz_minors_1_2':[signs(c) for c in minors],
     'simple_rouche_absolute_coefficient_bound_at_4_4':str(rouche_ratio),
     'rouche_scope':'Ratio >1 disproves sufficiency of this absolute-coefficient bound, not zero-freeness or the full Rouche approach.',
     'seconds':time.monotonic()-started}
Path('evidence/triage-certificate-screen.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='h_coefficients_descending_z'},indent=2))
