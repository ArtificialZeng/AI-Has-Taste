#!/usr/bin/env python3
"""Explore a frozen higher-order algebraic certificate; exact arithmetic only.

For flag order k, j=k+a, d=j+n, replace b_l by
l**k*(z_1+...+z_l). Tested polynomial coefficient positivity is stronger
than positivity at the antiprism specialization.
"""
import argparse
import json
import time
from pathlib import Path
import sympy as S
from research_fourth_flag import row_polys, falling, serialize, JOB


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('order',type=int)
    args=parser.parse_args()
    k=args.order
    a,n=S.symbols('a n')
    z=S.symbols('z1:'+str(k+1))
    b=S.symbols('b1:'+str(k+1))
    start=time.monotonic()
    polys={r:row_polys(r) for r in range(1,k+1)}
    matrix=[]
    for r in range(1,k+1):
        matrix.append([])
        for shift in range(1-k,1):
            expr=sum(b[ell-1]*S.Rational(ell,ell+1)**shift
                     *sum(coef*falling(a+k+shift,px)*falling(n-shift,py)
                          /S.Integer(ell)**px/S.Integer(ell+1)**py
                          for (px,py),coef in polys[r][ell].terms())
                     for ell in range(1,r+1))
            matrix[-1].append(S.Poly(expr,a,n,*b))
    minors={0:S.Poly(1,a,n,*b)}
    for r in range(1,k+1):
        for mask in range(1,1<<k):
            cols=[c for c in range(k) if mask>>c&1]
            if len(cols)!=r:continue
            value=S.Poly(0,a,n,*b)
            for pos,col in enumerate(cols):
                value+=(-1)**(r-1+pos)*minors[mask^(1<<col)]*matrix[r-1][col]
            minors[mask]=value
        print('order',k,'row',r,'seconds',round(time.monotonic()-start,2),flush=True)
    det=minors[(1<<k)-1]
    groups=S.Poly(det.as_expr(),*b)
    # Substitute only the small base monomials; retain a,n coefficients.
    transformed=S.Poly(0,a,n,*z)
    for powers,coef in groups.terms():
        basepoly=S.Poly(S.prod((ell**k*sum(z[:ell]))**power
                              for ell,power in enumerate(powers,1)),a,n,*z)
        transformed+=S.Poly(coef,a,n,*z)*basepoly
    negatives=[(m,str(coef)) for m,coef in transformed.terms() if coef<0]
    out={'job_id':JOB,'order':k,'scope':'formal flag determinant after b_l=l^k*sum(z_1,...,z_l)',
         'a':'j-k','n':'d-j','coefficient_variables':['a','n']+[str(v) for v in z],
         'base_group_count':len(groups.terms()),'original_terms':len(det.terms()),
         'transformed_terms':len(transformed.terms()),'negative_count':len(negatives),
         'negative_examples':negatives[:20],
         'coefficients':serialize(transformed),
         'z1_to_k_coefficient':str(transformed.coeff_monomial(z[0]**k)),
         'elapsed_seconds':time.monotonic()-start,
         'status':'exact coefficient calculation; no assertion beyond this order'}
    dest=Path('evidence/research_flag_order_'+str(k)+'.json')
    tmp=dest.with_suffix('.json.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(dest)
    print(json.dumps({key:out[key] for key in ['order','base_group_count','original_terms','transformed_terms','negative_count','z1_to_k_coefficient','elapsed_seconds']}))


if __name__=='__main__':main()
