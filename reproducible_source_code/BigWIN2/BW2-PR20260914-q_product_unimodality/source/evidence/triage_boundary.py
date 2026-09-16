"""Exact structural calibration, not a universal proof or novelty certificate.
Run from PROJECT_DIR: python3 evidence/triage_boundary.py > evidence/triage-boundary.json
"""
from itertools import combinations_with_replacement
import hashlib
import json
import platform

JOB = 'primary-20260914-q-product-unimodality-triage-b5b9ae83cac9'

def count_multiples(lo, hi, r, b):
    return max(0, min(b-1, hi//r)-max(0, -((-lo)//r))+1)

def difference(a, c, b, r, n):
    return (count_multiples(n-a+1, n, r, b)
            - count_multiples(n-a-c+1, n-c, r, b))

def coefficients(a, c, b, r):
    # Trapezoidal coefficients obtained independently by ordinary convolution.
    base = [0]*(a+c-1)
    for i in range(a):
        for j in range(c):
            base[i+j] += 1
    result = [0]*(a+c-1+r*(b-1))
    for j in range(b):
        for i, value in enumerate(base):
            result[r*j+i] += value
    return result

checks = identities = witnesses = sufficient = 0
failures = []
signature = hashlib.sha256()
for r in range(2, 13):
    values = [r*A+s for A in range(3) for s in range(1,r)]
    for a, c in combinations_with_replacement(values,2):
        A,s = divmod(a,r); C,t = divmod(c,r); M=A+C
        # Boundary-adapted test; not an extension of the outer rectangular grid.
        for b in sorted({1, max(1,M), M+1, M+2, M+4}):
            p = coefficients(a,c,b,r)
            D = len(p)-1
            assert p == p[::-1]
            for n in range(D+2):
                left = p[n] if n<=D else 0
                right = p[n-1] if 0<=n-1<=D else 0
                assert difference(a,c,b,r,n) == left-right, (a,c,b,r,n)
                identities += 1
            unimodal = all(p[n]>=p[n-1] for n in range(1,D//2+1))
            checks += 1
            signature.update(json.dumps([a,c,b,r,p],separators=(',',':')).encode())
            if b<=M+1:
                sufficient += 1
                if not unimodal:
                    failures.append({'kind':'sufficiency','a':a,'c':c,'b':b,'r':r,'p':p})
            else:
                nstar = r*M+max(s,t)
                assert 1<=nstar<=D//2
                assert difference(a,c,b,r,nstar)==-1
                assert p[nstar]-p[nstar-1]==-1
                witnesses += 1
                if unimodal:
                    failures.append({'kind':'necessity','a':a,'c':c,'b':b,'r':r,'p':p})
example = {'r':5,'a':7,'c':9,'b':4}
p = coefficients(example['a'],example['c'],example['b'],example['r'])
example.update(coefficients=p, witness_index=14, preceding_coefficient=p[13], coefficient=p[14])
print(json.dumps({
    'job_id':JOB, 'arithmetic':'exact Python integers', 'python':platform.python_version(),
    'scope':'k=2; r=2..12; a<=c; a=rA+s,c=rC+t; A,C=0..2; s,t=1..r-1; b in distinct {1,max(1,A+C),A+C+1,A+C+2,A+C+4}',
    'parameter_checks':checks,'full_difference_identity_checks':identities,
    'sufficient_regime_checks':sufficient,'negative_witness_checks':witnesses,
    'failures':failures,'coefficients_signature_sha256':signature.hexdigest(),
    'example':example,
    'limitations':'Finite calibration of the interval identity and explicit witness; not a universal proof, independent referee report, or priority claim.'
},indent=2))
