"""Exact finite checks of the proposed all-even-cycle certificate."""
from probe import poly, positive_count
from math import factorial
from pathlib import Path
import sympy as s
import json

A=s.Matrix([[0,1,1],[1,0,1],[1,1,1]])
assert A.charpoly().as_expr().factor()==(s.Symbol('lambda')+1)*(s.Symbol('lambda')**2-2*s.Symbol('lambda')-1)
rows=[]
for k in range(2,6):
    n=2*k
    c=poly(n,[(i,(i+1)%n) for i in range(n)],A)
    expected={(k+1,k-1,0):0,(k,k,0):2,(k,k-1,1):2*k,
              (k-1,k,1):2*k,(k-1,k-1,2):6*k*(k-1)}
    assert all(c.get(a,0)==v for a,v in expected.items())
    beta=(k-1,k-1,0)
    H=s.zeros(3)
    for i in range(3):
        for j in range(3):
            a=list(beta);a[i]+=1;a[j]+=1
            v=c.get(tuple(a),0)
            for z in a:v*=factorial(z)
            H[i,j]=v
    expected_H=2*factorial(k)**2*s.Matrix([[0,1,1],[1,0,1],[1,1,s.Rational(6*(k-1),k)]])
    assert H==expected_H
    assert positive_count(H)==2
    rows.append({'k':k,'assignments_enumerated':3**n,'beta':beta,
                 'H':H.tolist(),'determinant':H.det(),
                 'coefficient_checks':[{'exponent':a,'value':v} for a,v in expected.items()]})
    print('C'+str(n),'formula verified',flush=True)
Path('evidence/cycles.json').write_text(json.dumps({'target':A.tolist(),
    'target_spectrum':['-1','1-sqrt(2)','1+sqrt(2)'],
    'coverage':'k=2,3,4,5 only; infinite statement requires the counting proof',
    'checks':rows},indent=2,default=lambda x:int(x))+'\n')
