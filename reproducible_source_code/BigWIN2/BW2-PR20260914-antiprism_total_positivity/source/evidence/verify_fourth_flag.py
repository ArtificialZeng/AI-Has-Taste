#!/usr/bin/env python3
"""Independent rational verification of the complete fourth-flag identity.

Only standard-library arithmetic (plus the previous direct integer definition
for separate dimension checks). No SymPy expressions or sign flags are trusted.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product, permutations
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import time
import triage_exact as direct


def add(p,q):
    out=dict(p)
    for m,c in q.items():out[m]=out.get(m,F(0))+c
    return {m:c for m,c in out.items() if c}


def mul(p,q):
    out=defaultdict(F)
    for m,c in p.items():
        for mm,cc in q.items():out[tuple(x+y for x,y in zip(m,mm))]+=c*cc
    return {m:c for m,c in out.items() if c}


def power(p,k):
    out={(0,)*len(next(iter(p))):F(1)}
    for _ in range(k):out=mul(out,p)
    return out


def parse(rows,dim):
    out={tuple(m):F(c) for m,c in rows}
    assert len(out)==len(rows) and all(len(m)==dim and all(v>=0 for v in m) for m in out)
    assert all(out.values())
    return out


def fall(v,k):
    out=1
    for h in range(k):out*=v-h
    return out


PERMS=[(p,(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)))
       for p in permutations(range(4))]


def det4(m):
    out=F(0)
    for p,sign in PERMS:
        term=sign
        for r in range(4):term*=m[r][p[r]]
        out+=term
    return out


def main():
    start=time.monotonic()
    path=Path('evidence/research_fourth_flag.json')
    data=json.loads(path.read_text())
    row={int(r):{int(l):parse(p,2) for l,p in rp.items()}
         for r,rp in data['row_polynomials'].items()}
    # Independently derive the row generating coefficients by denominator
    # multiplication, instead of the producer's Stirling-number formula.
    f={0:{(0,0,0):F(1)}}
    cminus1={(0,0,1):F(1),(0,0,0):F(-1)}
    for r in range(1,5):
        f[r]={(r,0,0):F(1,factorial(r))}
        for h in range(1,r+1):
            wh={(p,h-p,0):F(comb(h,p),factorial(h)) for p in range(h+1)}
            f[r]=add(f[r],mul(mul(cminus1,wh),f[r-h]))
        claimed={(px,py,l):coef for l,poly in row[r].items() for (px,py),coef in poly.items()}
        assert f[r]==claimed
    groups={tuple(g['powers']):parse(g['coefficients'],2) for g in data['groups']}
    assert len(groups)==14
    assert all(sum(p)==4 and all(v<=bound for v,bound in zip(p,[4,3,2,1])) for p in groups)
    assert all(sum(m)<=10 for poly in groups.values() for m in poly)
    checks=0
    for av,nv in product(range(11),repeat=2):
        coeffs=[[
            {l:F(l,l+1)**shift*sum(coef*fall(av+4+shift,px)*fall(nv-shift,py)
                                 /l**px/(l+1)**py for (px,py),coef in row[r][l].items())
             for l in range(1,r+1)} for shift in (-3,-2,-1,0)] for r in range(1,5)]
        vals={p:sum(coef*av**m[0]*nv**m[1] for m,coef in poly.items())
              for p,poly in groups.items()}
        for bases in product(range(5),range(4),range(3),range(2)):
            matrix=[[sum(bases[l-1]*coef for l,coef in ent.items()) for ent in row] for row in coeffs]
            rhs=F(0)
            for powers,val in vals.items():
                term=val
                for base,p in zip(bases,powers):term*=base**p
                rhs+=term
            assert det4(matrix)==rhs
            checks+=1
        if av%3==0 and nv==10:print('interpolation a',av,'checks',checks,flush=True)
    assert checks==11*11*5*4*3*2
    # Check the entire affine ratio-substitution identity coefficient by coefficient.
    bu={(1,0,0,0):F(1)}
    bv={(1,0,0,0):F(16),(0,1,0,0):F(1)}
    bw=add({m:F(81,16)*coef for m,coef in bv.items()},{(0,0,1,0):F(1)})
    bt=add({m:F(256,81)*coef for m,coef in bw.items()},{(0,0,0,1):F(1)})
    transformed=defaultdict(F)
    for powers,poly in groups.items():
        basepoly={(0,0,0,0):F(1)}
        for bp,p in zip([bu,bv,bw,bt],powers):basepoly=mul(basepoly,power(bp,p))
        for m,coef in poly.items():
            for bm,bc in basepoly.items():transformed[m+bm]+=coef*bc
    transformed={m:coef for m,coef in transformed.items() if coef}
    assert transformed==parse(data['ratio_substitution']['coefficients'],6)
    assert len(transformed)==924 and all(coef>0 for coef in transformed.values())
    assert transformed[0,0,4,0,0,0]==2925

    def formula(dim,col):
        av,nv=col-4,dim-col
        bases=[l**col*(l+1)**nv for l in range(1,5)]
        ans=F(0)
        for p,poly in groups.items():
            term=sum(coef*av**m[0]*nv**m[1] for m,coef in poly.items())
            for base,exponent in zip(bases,p):term*=base**exponent
            ans+=term
        assert ans.denominator==1
        return ans.numerator
    dims=[]
    for dim in range(4,17):
        h=direct.direct(dim)
        values=[]
        for col in range(4,dim+1):
            exact=direct.determinant([[h[r][c] for c in range(col-3,col+1)] for r in range(1,5)])
            assert formula(dim,col)==exact and exact>0
            values.append(str(exact))
        dims.append({'d':dim,'flags_j_4_through_d':values})
    st=[[0]*5 for _ in range(5)];st[0][0]=1
    for r in range(1,5):
        for l in range(1,r+1):st[r][l]=st[r-1][l-1]+l*st[r-1][l]
    face=[]
    for dim in list(range(17,65))+[96,128,192,256]:
        q=[[comb(t,r)*sum(factorial(l)*st[r][l]*l**(t-r) for l in range(r+1))
            if t>=r else 0 for t in range(dim+1)] for r in range(5)]
        rows=[[] for _ in range(5)]
        for col in range(dim+1):
            fvec=[sum(q[r][t]*comb(dim-col,t-col) for t in range(col,dim+1)) for r in range(5)]
            for r in range(1,5):
                rows[r].append(sum((-1)**(r-h)*comb(dim-h,r-h)*fvec[h] for h in range(r+1)))
        for col in range(4,dim+1):
            exact=direct.determinant([[rows[r][c] for c in range(col-3,col+1)] for r in range(1,5)])
            assert exact==formula(dim,col) and exact>0
        face.append({'d':dim,'all_allowed_flags_checked':True})
    out={'job_id':data['job_id'],'arithmetic':'standard-library Fraction and integers',
         'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
         'row_egf_recurrence_identity':True,'separate_degree_bounds':[10,10,4,3,2,1],
         'interpolation_grid_sizes':[11,11,5,4,3,2],'grid_points':checks,
         'complete_polynomial_identity':True,'affine_substitution_identity':True,
         'positive_coefficient_count':len(transformed),'u_fourth_coefficient':2925,
         'direct_definition_checks':dims,'independent_face_checks':face,
         'elapsed_seconds':time.monotonic()-start,
         'review_scope':'separate arithmetic implementation in same context; no fresh referee'}
    dest=Path('evidence/verify_fourth_flag.json');tmp=dest.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(dest)
    print(json.dumps({k:out[k] for k in ['grid_points','positive_coefficient_count','u_fourth_coefficient','elapsed_seconds']}))


if __name__=='__main__':main()
