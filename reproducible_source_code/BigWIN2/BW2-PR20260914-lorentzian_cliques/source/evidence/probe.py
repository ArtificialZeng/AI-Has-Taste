"""Bounded exact triage; run python3 evidence/probe.py from project root."""
from itertools import product, combinations
from collections import defaultdict
from math import factorial
from pathlib import Path
import json
import sympy as s

def comps(n,q):
    if q==1:
        yield (n,)
    else:
        for k in range(n+1):
            for rest in comps(n-k,q-1): yield (k,)+rest

def positive_count(M):
    # Symmetric M has real roots only. Descartes variations are then exact.
    cc=[s.sign(c) for c in M.charpoly().all_coeffs() if c]
    return sum(a!=b for a,b in zip(cc,cc[1:]))

def poly(n,edges,A):
    q=A.rows
    c=defaultdict(int)
    for sig in product(range(q),repeat=n):
        w=1
        for u,v in edges:
            w*=int(A[sig[u],sig[v]])
            if not w: break
        if w: c[tuple(sig.count(i) for i in range(q))]+=w
    return dict(c)

def check(c,n,q):
    S=set(c)
    for a,b in product(sorted(S),repeat=2):
        for i in range(q):
            if a[i]<=b[i]: continue
            possible=[]
            for j in range(q):
                if a[j]>=b[j]:continue
                z=list(a);z[i]-=1;z[j]+=1
                possible.append(tuple(z))
            if not any(z in S for z in possible):
                return {'kind':'support-exchange','a':a,'b':b,'i':i,
                        'missing_candidates':possible}
    for beta in comps(n-2,q):
        H=s.zeros(q)
        for i in range(q):
            for j in range(q):
                z=list(beta);z[i]+=1;z[j]+=1
                val=c.get(tuple(z),0)
                for k in z:val*=factorial(k)
                H[i,j]=val
        count=positive_count(H)
        if count>1:
            return {'kind':'hessian','beta':beta,'H':H.tolist(),
                    'characteristic_coefficients':H.charpoly().all_coeffs(),
                    'positive_eigenvalues':count,'determinant':H.det()}
    return None

def main():
    graphs={'P3':(3,[(0,1),(1,2)]),
            'P4':(4,[(0,1),(1,2),(2,3)]),
            'C4':(4,[(0,1),(1,2),(2,3),(3,0)]),
            'paw':(4,[(0,1),(1,2),(2,0),(2,3)]),
            'diamond':(4,[(0,1),(0,2),(0,3),(1,2),(1,3)])}
    targets=[('known-P3',s.Matrix([[0,0,1],[0,0,2],[1,2,0]]))]
    for q in (2,3,4):
        for loop in (False,True):
            B=s.ones(q)-s.eye(q)
            if loop:B[q-1,q-1]=1
            weights=[(1,)*q]+list(product((1,2),repeat=q))
            seen=set()
            for d in weights:
                if d in seen:continue
                seen.add(d)
                D=s.diag(*d)
                targets.append((f'K{q}-loop{int(loop)}-D{d}',D*B*D))
    result={'method':'integer enumeration; exact characteristic signs',
            'target_count':len(targets),'graphs':{}}
    for name,(n,edges) in graphs.items():
        rows=[]
        for tname,A in targets:
            assert positive_count(A)<=1
            c=poly(n,edges,A)
            bad=check(c,n,A.rows)
            row={'target':tname,'A':A.tolist(),'target_charpoly':A.charpoly().all_coeffs(),
                 'target_positive_eigenvalues':positive_count(A),'failure':bad}
            if bad or tname=='known-P3':
                row['coefficients']=[{'exponent':a,'coefficient':v} for a,v in sorted(c.items())]
            rows.append(row)
        result['graphs'][name]={'n':n,'edges':edges,'tests':rows,
             'failures':sum(row['failure'] is not None for row in rows)}
        print(name,'tested',len(rows),'failures',result['graphs'][name]['failures'],flush=True)
        for row in rows:
            if row['failure']:
                print(' first witness',row['target'],row['failure'],flush=True);break
    Path('evidence/probe.json').write_text(json.dumps(result,indent=2,default=lambda x:int(x))+'\n')

if __name__=='__main__':main()
