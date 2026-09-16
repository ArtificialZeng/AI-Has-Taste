"""Test finite local hit kernels. Their universal reproduction is a separate claim.

Run: python3 evidence/research_local_kernels.py
"""
from collections import Counter
from itertools import combinations, permutations
from pathlib import Path
import gzip
import json
import struct
import time

from research_n4 import exhaustive, JOB

OUT = Path(__file__).resolve().parent


def load_hits(n):
    path = OUT/f'research_n{n}_residues.bin.gz'
    if not path.exists():
        return exhaustive(n)
    flat = list(struct.iter_unpack('<3q',gzip.decompress(path.read_bytes())))
    return [flat[k:k+n+1] for k in range(0,len(flat),n+1)]


def projections(n,k):
    ans=[]
    for rows in combinations(range(n),k):
        other_rows = [i for i in range(n) if i not in rows]
        for cols in combinations(range(n),k):
            other_cols = [j for j in range(n) if j not in cols]
            ans.append(([i*n+j for i in rows for j in cols],
                        [i*n+j for i in other_rows for j in other_cols]))
    return ans


def project(mask,indices):
    return sum(((mask>>b)&1)<<i for i,b in enumerate(indices))


def main():
    start=time.monotonic()
    hits={0:[[[1,0,0]]]}
    for n in (1,2,3,4):
        hits[n]=load_hits(n)
    kernels={ell:{0:[[0]]} for ell in (1,2)}
    result={'job_id':JOB,'definition':
        'K[l,n](B;t)=C[l,n](B;t)-sum_{k<n} sum_{R,C:|R|=|C|=k} K[l,k](B[R,C];t) h(B[Rc,Cc];t)',
        'tests':[]}
    for n in (1,2,3,4):
        projs={k:projections(n,k) for k in range(1,n)}
        for ell in (1,2):
            kn=[]
            hist=Counter()
            negative=[]
            active={k:any(any(v) for v in kernels[ell][k]) for k in projs}
            for mask,h in enumerate(hits[n]):
                val=[x[ell] for x in h]
                for k,pjs in projs.items():
                    if not active[k]:
                        continue
                    for ix,iy in pjs:
                        x,y=project(mask,ix),project(mask,iy)
                        a=kernels[ell][k][x]
                        b=[v[0] for v in hits[n-k][y]]
                        for i,u in enumerate(a):
                            for j,v in enumerate(b):
                                val[i+j]-=u*v
                for d,v in enumerate(val):
                    hist[v]+=1
                    if v<0 and len(negative)<10:
                        negative.append({'mask':mask,'d':d,'coefficient':v,
                                         'kernel':val})
                kn.append(val)
            kernels[ell][n]=kn
            rr={'ell':ell,'n':n,'boards':len(kn),'range':[min(hist),max(hist)],
                'nonzero_coefficients':sum(v for k,v in hist.items() if k),
                'negative_coefficients':sum(v for k,v in hist.items() if k<0),
                'first_negative_witnesses':negative,
                'empty_full_kernels':[kn[0],kn[-1]]}
            result['tests'].append(rr)
            print(json.dumps(rr),flush=True)
    result['elapsed_seconds']=round(time.monotonic()-start,3)
    (OUT/'research_local_kernel_results.json').write_text(json.dumps(result,indent=2)+'\n')
    with gzip.open(OUT/'research_local_kernel_tables.json.gz','wt') as f:
        json.dump(kernels,f,separators=(',',':'))


if __name__=='__main__':
    main()
