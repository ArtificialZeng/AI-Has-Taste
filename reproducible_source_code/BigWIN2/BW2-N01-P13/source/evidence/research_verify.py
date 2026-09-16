"""Same-worker verification using different rank and evaluation algorithms.

Run: python3 evidence/research_verify.py
This is not a fresh referee audit. No floating point arithmetic is used.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, permutations, product
from math import comb, factorial
from pathlib import Path
import gzip
import json
import random
import struct
import sys
import time

JOB='newwin-00001-p13-research-75edfb64efc5'
OUT=Path(__file__).resolve().parent
TABLE=json.loads((OUT/'connected_orbits.json').read_text())


def connected(r,c,es):
    seen={0}
    while True:
        old=len(seen)
        for i,j in es:
            if i in seen or r+j in seen:
                seen.update((i,r+j))
        if len(seen)==old:
            return len(seen)==r+c


def key(r,c,es):
    return min(sum(1<<(pr[i]*c+pc[j]) for i,j in es)
               for pr in permutations(range(r)) for pc in permutations(range(c)))


def orbit_verify():
    """Ranks from minors, BFS tree, extension fields F4/F8, fresh interpolation."""
    coverage=set()
    for r in range(1,4):
        for c in range(1,4):
            for mask in range(1,1<<(r*c)):
                es=[(i,j) for i in range(r) for j in range(c) if mask>>(i*c+j)&1]
                if connected(r,c,es):
                    coverage.add((r,c,key(r,c,es)))
    assert coverage=={(a['rows'],a['columns'],a['mask']) for a in TABLE}
    fields=(2,3,4,5,7,8)
    checked=0
    assignments=Counter()
    for entry in TABLE:
        r,c=entry['rows'],entry['columns']
        es=[tuple(e) for e in entry['edges']]
        tree=[];seen={0}
        while len(seen)<r+c:
            e=next((i,j) for i,j in es if (i in seen) != (r+j in seen))
            tree.append(e);seen.update((e[0],r+e[1]))
        rest=[e for e in es if e not in tree]
        samples=[]
        for q in fields:
            if q in (4,8):
                degree=q.bit_length()-1
                modulus={4:0b111,8:0b1011}[q]
                def add(a,b): return a^b
                def neg(a): return a
                def mul(a,b):
                    v=0
                    while b:
                        if b&1: v^=a
                        b>>=1;a<<=1
                        if a&q: a^=modulus
                    return v
            else:
                def add(a,b): return (a+b)%q
                def neg(a): return (-a)%q
                def mul(a,b): return a*b%q
            def determinant(a):
                v=0
                for p in permutations(range(len(a))):
                    w=1
                    for i,j in enumerate(p): w=mul(w,a[i][j])
                    inv=sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))
                    v=add(v,neg(w) if inv%2 else w)
                return v
            def rank_minors(a):
                for d in range(min(r,c),0,-1):
                    for rr in combinations(range(r),d):
                        for cc in combinations(range(c),d):
                            if determinant([[a[i][j] for j in cc] for i in rr]):
                                return d
                return 0
            counts=[0]*(min(r,c)+1)
            a=[[0]*c for _ in range(r)]
            for i,j in tree:a[i][j]=1
            for vals in product(range(1,q),repeat=len(rest)):
                for (i,j),v in zip(rest,vals):a[i][j]=v
                counts[rank_minors(a)]+=1
                assignments[q]+=1
            assert sum(counts)==(q-1)**len(rest)
            for d,poly in enumerate(entry['orbit_polynomials_in_x']):
                assert counts[d]==sum(v*(q-1)**k for k,v in enumerate(poly)), (entry,q,d)
                checked+=1
            samples.append(counts)
        # Newton divided differences, separate from triage's Lagrange routine.
        beta=len(rest)
        for d,expected in enumerate(entry['orbit_polynomials_in_x']):
            xs=[q-1 for q in fields[:beta+1]]
            dd=[Fraction(v[d]) for v in samples[:beta+1]]
            actual=[Fraction(0)]*(beta+1);basis=[Fraction(1)]
            for k in range(beta+1):
                for j,b in enumerate(basis):actual[j]+=dd[0]*b
                dd=[(dd[j+1]-dd[j])/(xs[j+k+1]-xs[j]) for j in range(len(dd)-1)]
                nxt=[Fraction(0)]*(len(basis)+1)
                for j,b in enumerate(basis):nxt[j]-=xs[k]*b;nxt[j+1]+=b
                basis=nxt
            assert actual==expected
    return {'connected_classes':len(coverage),'fields':fields,
            'rank_polynomial_evaluation_comparisons':checked,
            'gauge_assignments_by_field':dict(assignments),
            'rank_method':'all minors / determinant permutation expansion',
            'reconstruction':'Newton divided differences at beta+1 first field sizes',
            'finite_field_polynomials':{'4':'u^2+u+1','8':'u^3+u+1'}}


def local_connected_factors():
    lookup={(a['rows'],a['columns'],a['mask']):a['orbit_polynomials_in_x'] for a in TABLE}
    ans={}
    for r in range(1,4):
        for c in range(1,4):
            if (r,c)==(1,1):continue
            rows=[[[0,0] for _ in range(min(r,c)+1)] for _ in range(1<<(r*c))]
            for mask in range(1,1<<(r*c)):
                es=[(i,j) for i in range(r) for j in range(c) if mask>>(i*c+j)&1]
                if not connected(r,c,es):continue
                for d,p in enumerate(lookup[r,c,key(r,c,es)]):
                    e=r+c-d-1
                    for a in (1,2):
                        if 0<=a-e<len(p):rows[mask][d][a-1]=p[a-e]
            for bit in range(r*c):
                for mask in range(1<<(r*c)):
                    if mask>>bit&1:
                        for d in range(min(r,c)+1):
                            for a in (0,1):rows[mask][d][a]+=rows[mask^(1<<bit)][d][a]
            ans[r,c]=rows
    return ans


FACTORS=local_connected_factors()


class CoreEvaluator:
    def __init__(self,n,mask):
        self.n=n;self.mask=mask;self.full=(1<<n)-1
        self.rowboards=[(mask>>(i*n))&self.full for i in range(n)]
        self.rook=lru_cache(None)(self._rook)
        self.hit=lru_cache(None)(self._hit)

    def _rook(self,rr,cc):
        if not rr:return (1,)
        low=rr&-rr;i=low.bit_length()-1;rest=rr^low
        out=list(self.rook(rest,cc))+[0]
        available=self.rowboards[i]&cc
        while available:
            col=available&-available;available^=col
            p=self.rook(rest,cc^col)
            for d,v in enumerate(p):out[d+1]+=v
        while len(out)>1 and not out[-1]:out.pop()
        return tuple(out)

    def _hit(self,rr,cc):
        if not rr:return (1,)
        assert rr.bit_count()==cc.bit_count()
        low=rr&-rr;i=low.bit_length()-1;rest=rr^low
        out=[0]*(rr.bit_count()+1);available=cc
        while available:
            col=available&-available;available^=col
            shift=bool(self.rowboards[i]&col)
            for d,v in enumerate(self.hit(rest,cc^col)):out[d+shift]+=v
        return tuple(out)

    def residues(self):
        n=self.n;full=self.full
        out=[[0,0,0] for _ in range(n+1)]
        for i,v in enumerate(self.rook(full,full)):out[i][0]=v
        first=[]
        for (r,c),table in FACTORS.items():
            if max(r,c)>n:continue
            for rows in combinations(range(n),r):
                rb=sum(1<<i for i in rows)
                for cols in combinations(range(n),c):
                    cb=sum(1<<j for j in cols)
                    lm=sum(((self.mask>>(i*n+j))&1)<<(a*c+b)
                           for a,i in enumerate(rows) for b,j in enumerate(cols))
                    factors=table[lm]
                    if not any(any(v) for v in factors):continue
                    rest=self.rook(full^rb,full^cb)
                    for d,(a,b) in enumerate(factors):
                        if a:first.append((rb,cb,d,a))
                        for j,v in enumerate(rest):
                            out[d+j][1]+=a*v;out[d+j][2]+=b*v
        for k,(ra,ca,da,va) in enumerate(first):
            for rb,cb,db,vb in first[k+1:]:
                if ra&rb or ca&cb:continue
                rest=self.rook(full^(ra|rb),full^(ca|cb))
                for j,v in enumerate(rest):out[da+db+j][2]+=va*vb*v
        return out

    def quadratic(self):
        n=self.n;N=n*(n-1)//2
        out=[Fraction(0)]*(n+1)
        def add_z(power,shift,value):
            if not value:return
            assert power>=0
            for d in range(power+1):out[d+shift]+=value*comb(power,d)*(-1)**(power-d)
        for i,(r0,r1,r2) in enumerate(self.residues()):
            m=n-i;f=factorial(m)
            A=Fraction(m*(m-1),4)
            B=Fraction(m*(m-1)*(m-2)*(9*m+13),288)
            a=N+A;b=Fraction(N*(N-1),2)+N*A+B
            I=Fraction(i*(i-1),2);J=Fraction(i*(i-1)*(i+1),6)
            K=Fraction(i*(i-1)*(i-2)*(3*i-1),24)
            add_z(i,0,f*(r2+a*r1+b*r0))
            add_z(i-1,1,f*(-I*r1+(J-a*I)*r0))
            add_z(i-2,2,f*K*r0)
        assert all(v.denominator==1 for v in out)
        return [int(v) for v in out]

    def lifted(self,kernels):
        n=self.n;out=[0]*(n+1)
        for k in range(2,min(4,n)+1):
            for rows in combinations(range(n),k):
                rb=sum(1<<i for i in rows)
                for cols in combinations(range(n),k):
                    cb=sum(1<<j for j in cols)
                    local=sum(((self.mask>>(i*n+j))&1)<<(a*k+b)
                              for a,i in enumerate(rows) for b,j in enumerate(cols))
                    a=kernels[str(k)][local];b=self.hit(self.full^rb,self.full^cb)
                    for i,u in enumerate(a):
                        for j,v in enumerate(b):out[i+j]+=u*v
        return out


def heldout_verify():
    path=OUT/'research_local_kernel_tables.json.gz'
    digest=sha256(path.read_bytes()).hexdigest()
    kernels=json.loads(gzip.decompress(path.read_bytes()))['2']
    rng=random.Random(751364)
    cases=[]
    for n in (1,2,3):
        cases.extend((n,mask,'exhaustive small') for mask in range(1<<(n*n)))
    for n,count in ((4,32),(5,24),(6,12),(7,4),(8,2)):
        full=(1<<(n*n))-1
        cases.extend([(n,0,'empty'),(n,full,'full'),
                      (n,sum(1<<(i*n+i) for i in range(n)),'diagonal'),
                      (n,sum(1<<(i*n+j) for i in range(n) for j in range(n) if j<=i),'staircase'),
                      (n,sum(1<<(i*n+j) for i in range(n) for j in (i,(i+1)%n)),'cycle')])
        for k in range(count):
            numerator=(1,2,4,6,7)[k%5]
            mask=sum(1<<i for i in range(n*n) if rng.randrange(8)<numerator)
            cases.append((n,mask,f'deterministic density {numerator}/8'))
    fano_rows=('1100010','0110001','1011000','0101100','0010110','0001011','1000101')
    fano=sum(1<<(i*7+j) for i,row in enumerate(fano_rows) for j,v in enumerate(row) if v=='1')
    cases.extend([(7,fano,'Fano board from primary source'),
                  (7,((1<<49)-1)^fano,'complement of Fano board')])
    records=[]
    for n,mask,family in cases:
        ev=CoreEvaluator(n,mask)
        direct=ev.quadratic();lift=ev.lifted(kernels)
        assert direct==lift,(n,mask,direct,lift)
        assert min(direct)>=0
        if n>=4:records.append({'n':n,'mask':mask,'family':family,'quadratic':direct})
    return {'kernel_table_sha256_before_tests':digest,
            'seed':751364,'cases_by_size':dict(Counter(n for n,_,_ in cases)),
            'distinct_boards_by_size':{n:len({mask for nn,mask,_ in cases if nn==n})
                                       for n in sorted({nn for nn,_,_ in cases})},
            'board_index_comparisons':sum(n+1 for n,_,_ in cases),
            'algorithm':'connected-core embeddings plus residual matching DP; independent explicit weight formula; compare local lift',
            'records_for_n_at_least_4':records}


def exhaustive_local_verify():
    """Second all-board evaluator and direct, nonrecursive inverse convolution."""
    kernels=json.loads(gzip.decompress((OUT/'research_local_kernel_tables.json.gz').read_bytes()))['2']
    calculated={0:[[0]]}
    summaries=[]
    for n in (1,2,3,4):
        start=time.monotonic()
        raw=gzip.decompress((OUT/f'research_n{n}_residues.bin.gz').read_bytes())
        reference=list(struct.iter_unpack('<3q',raw))
        now=[]
        h_digest=sha256();k_digest=sha256();hist=Counter()
        projections=[]
        for j in range(1,n):
            for rows in combinations(range(n),j):
                rb=sum(1<<i for i in rows)
                for cols in combinations(range(n),j):
                    cb=sum(1<<i for i in cols)
                    ix=[i*n+k for i in rows for k in cols]
                    projections.append((j,rb,cb,ix,(-1)**(n-j)))
        for mask in range(1<<(n*n)):
            ev=CoreEvaluator(n,mask);v=ev.quadratic();now.append(v)
            assert v==[reference[mask*(n+1)+d][2] for d in range(n+1)],(n,mask,'H')
            local=v[:]
            for j,rb,cb,ix,sign in projections:
                m=sum(((mask>>b)&1)<<i for i,b in enumerate(ix))
                a=calculated[j][m];b=ev.hit(ev.full^rb,ev.full^cb)
                for d,u in enumerate(a):
                    for e,w in enumerate(b):local[d+e]+=sign*u*w
            assert local==kernels[str(n)][mask],(n,mask,'kernel')
            assert min(local)>=0
            for x,y in zip(v,local):
                h_digest.update(struct.pack('<q',x));k_digest.update(struct.pack('<q',y));hist[y]+=1
        calculated[n]=now
        summaries.append({'n':n,'boards':len(now),'quadratic_comparisons':len(now)*(n+1),
            'kernel_comparisons':len(now)*(n+1),'kernel_range':[min(hist),max(hist)],
            'quadratic_stream_sha256':h_digest.hexdigest(),'kernel_stream_sha256':k_digest.hexdigest(),
            'stream_format':'mask increasing then d; signed little-endian int64',
            'elapsed_seconds':round(time.monotonic()-start,3)})
        print('second exhaustive path',summaries[-1],flush=True)
    result={'job_id':JOB,'audit_status':'same worker, separate finite-evaluation algorithm',
        'method':'connected-core and matching DP residues; explicit weight expansion; direct alternating inverse convolution',
        'shared_dependency':'connected orbit polynomial table, independently reconstructed with minor ranks and extension fields',
        'tests':summaries}
    (OUT/'research_independent_n4_results.json').write_text(json.dumps(result,indent=2)+'\n')


def main():
    start=time.monotonic()
    result={'job_id':JOB,'audit_status':'same worker, different algorithms; fresh review pending'}
    result['orbits']=orbit_verify()
    print('orbit verification passed',flush=True)
    partial=OUT/'research_verification_results.json'
    partial.write_text(json.dumps(result,indent=2)+'\n')
    result['heldout']=heldout_verify()
    result['elapsed_seconds']=round(time.monotonic()-start,3)
    tmp=partial.with_suffix('.json.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(partial)
    print(json.dumps({k:result['heldout'][k] for k in ('cases_by_size','distinct_boards_by_size','board_index_comparisons')},indent=2))
    print('seconds',result['elapsed_seconds'])


if __name__=='__main__':
    if '--exhaustive-local' in sys.argv:exhaustive_local_verify()
    else:main()
