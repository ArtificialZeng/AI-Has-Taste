"""Exact generic k=4 feasibility test of Wastlund (9); no universal claim."""
import json
import signal
import time
from functools import lru_cache
from pathlib import Path
import sympy as S
from sympy.polys.fields import field

signal.alarm(45)
started = time.monotonic()
K, m, n, t = field('m,n,t', S.QQ)

@lru_cache(None)
def F(k, offset, d=0):
    nn = n-offset
    if d < 0 or d > k:
        return K.zero
    if k == 0:
        return K.one
    if d == 0:
        return t/nn*F(k,offset,1)+F(k-1,offset+1,0)
    a = m-k+d
    v = F(k-1,offset+1,d-1)/a
    if d < k:
        v += (d+1)*t/nn*F(k,offset,d+1)+F(k-1,offset+1,d)
    return v/(1-d*t/(a*nn))

f = F(4,0)
ms,ns,ts,z = S.symbols('m n t z')
P = f.numer.as_expr()
Q = f.denom.as_expr()
Path('evidence/k4-rational.json').write_text(json.dumps({
    'numerator':str(P), 'denominator':str(Q),
    'variables':['m','n','t'], 'domain':'QQ(m,n,t)',
    'source':'arXiv:2602.07563v1 equation (9)',
    'scope':'Generic rational identity from a single implementation; no independent audit.'
},indent=2)+'\n')
out = {'scope':'Exact symbolic feasibility and finite calibration only.',
       'sympy':S.__version__, 'generic_numerator_t_degree':int(S.degree(P,ts)),
       'generic_denominator_t_degree':int(S.degree(Q,ts)),
       'numerator_terms':len(f.numer.terms()),
       'denominator_terms':len(f.denom.terms()),
       'normalization':S.Poly((P-Q).subs(ts,0),ms,ns).is_zero,
       'symmetry':S.Poly(P*Q.xreplace({ms:ns,ns:ms})-Q*P.xreplace({ms:ns,ns:ms}),ms,ns,ts).is_zero}
f3generic = F(3,0).as_expr()
f3 = f3generic.subs({ms:3,ns:3})
out['eq10_match'] = S.cancel(f3-6*(162-90*ts+16*ts**2-ts**3)/((4-ts)*(3-ts)**5)) == 0
out['printed_eq38_cubic_coefficient'] = 2
out['factored_eq38_cubic_coefficient'] = int(S.Poly((ms*ns-2*ts)*((ms-1)*ns-ts)*(ms*(ns-1)-ts),ts).nth(3))
q36 = S.prod((ms-i)*(ns-j)-(3-i-j)*ts for i in range(3) for j in range(3-i))
p37corrected = ms**2*ns**2*(ms-1)*(ns-1)-ms*ns*(4*ms*ns-3*ms-3*ns+2)*ts+(5*ms*ns-2*ms-2*ns-1)*ts**2-2*ts**3
factor = ms*ns*(ms-1)*(ns-1)*(ms-2)*(ns-2)
out['eq36_37_additional_normalization_factor'] = str(factor)
out['generic_corrected_eq36_37_match'] = S.cancel(f3generic-factor*p37corrected/q36)==0
out['printed_eq36_37_F_at_zero_3_3'] = str((p37corrected/q36).subs({ms:3,ns:3,ts:0}))
out['seconds'] = time.monotonic()-started
Path('evidence/triage-symbolic.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
