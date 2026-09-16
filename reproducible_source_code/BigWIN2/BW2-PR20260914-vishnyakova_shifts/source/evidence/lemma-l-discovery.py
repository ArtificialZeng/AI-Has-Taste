"""Floating-point search only; discoveries require a separate exact certificate."""
import numpy as np
from scipy.optimize import differential_evolution
import json, time
from pathlib import Path
rng=np.random.default_rng(83017)
b=1-1/np.sqrt(2)
def op(p,t):
    q=np.zeros(len(p)+1)
    for j,c in enumerate(p): q[j]+=(j+t)*c; q[j+1]+=(j+1)*c
    return q

def run(v,d):
    t=-b+v[0]*b
    aa=np.sort(v[1:d+1])
    lam=v[-1]/(np.sum(1/aa)+(1+2*t)/(1+t)**2)
    p=np.polynomial.polynomial.polyfromroots(list(-aa)+[lam])
    q=op(op(p,t),t)
    roots=np.polynomial.polynomial.polyroots(q)
    return t,aa,lam,q,roots

def target(v,d):
    _,aa,_,_,r=run(v,d)
    # For low degrees the missing near-zero pair is numerically resolvable.
    imag=abs(r.imag)
    return -float(max(imag))

out=[]
for d in (2,4,6):
    bounds=[(1e-8,0.999999)]+[(0.0001,0.9999)]*d+[(0.001,1)]
    res=differential_evolution(lambda v:target(v,d),bounds,seed=rng,
                             popsize=12,maxiter=150,tol=1e-8,polish=False,workers=1)
    t,aa,lam,q,rr=run(res.x,d)
    item={'d':d,'t':float(t),'magnitudes':aa.tolist(),'lambda':float(lam),'ratio':float(res.x[-1]),'roots':[[float(z.real),float(z.imag)] for z in rr],'objective':float(res.fun),'warning':'Floating point only; clustered high-degree roots can be spurious.'}
    out.append(item)
    print(json.dumps(item),flush=True)
Path('evidence/lemma-l-discovery.json').write_text(json.dumps(out,indent=2)+'\n')
