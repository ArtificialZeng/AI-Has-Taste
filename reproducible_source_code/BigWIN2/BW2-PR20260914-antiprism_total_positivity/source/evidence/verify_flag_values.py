#!/usr/bin/env python3
"""Supplementary exact matrix checks for the order-five/six certificates."""
from pathlib import Path
import json
from math import prod,lcm
from fractions import Fraction as F
from triage_exact import direct,determinant


def main():
    out={'job_id':'primary-20260914-antiprism-total-positivity-research-1f8d7876bdf3',
         'arithmetic':'integers with denominator clearing','orders':{}}
    for k in [5,6]:
        data=json.loads(Path('evidence/research_flag_order_'+str(k)+'.json').read_text())
        group={}
        for m,c in data['coefficients']:
            group.setdefault(tuple(m[2:]),[]).append((m[0],m[1],F(c)))
        packed={}
        for m,terms in group.items():
            den=lcm(*(c.denominator for p,q,c in terms))
            packed[m]=(den,[(p,q,int(c*den)) for p,q,c in terms])
        vals=[]
        for d in range(k,17):
            h=direct(d)
            for j in range(k,d+1):
                a,n=j-k,d-j
                z=[2**n]+[ell**a*(ell+1)**n-(ell-1)**a*ell**n for ell in range(2,k+1)]
                assert all(x>=0 for x in z) and z[0]>0
                value=F(0)
                for m,(den,terms) in packed.items():
                    value+=F(sum(c*a**p*n**q for p,q,c in terms),den)*prod(base**power for base,power in zip(z,m))
                exact=determinant([[h[r][c] for c in range(j-k+1,j+1)] for r in range(1,k+1)])
                assert value.denominator==1 and value.numerator==exact and exact>0
                vals.append({'d':d,'j':j,'determinant':str(exact)})
        out['orders'][str(k)]={'every_d_from_k_through_16_and_every_j_from_k_through_d':True,'checks':vals}
        print(k,len(vals),'exact flags checked',flush=True)
    p=Path('evidence/verify_flag_values.json');q=p.with_suffix('.json.tmp')
    q.write_text(json.dumps(out,indent=2)+'\n');q.replace(p)


if __name__=='__main__':main()
