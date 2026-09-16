"""Exact triage calibration, not an independent referee or all-length proof."""
from collections import Counter
from datetime import datetime, timezone
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location, module_from_spec
from itertools import combinations, combinations_with_replacement
from math import comb, isqrt, prod
from pathlib import Path
import json
import platform

ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / 'evidence/check-p10-p11-small.py'
spec = spec_from_file_location('baseline', BASE)
old = module_from_spec(spec)
spec.loader.exec_module(old)

def conv(a, b):
    d = len(a)-1
    return [sum(comb(j,k)*a[k]*b[j-k] for k in range(j+1)) for j in range(d+1)]

def output_moments(n, p):
    d = len(p)-1
    a = [n]+p[1:]
    a2 = [a[j]*2**j for j in range(d+1)]
    a3 = [a[j]*3**j for j in range(d+1)]
    b = conv(a,a)
    b4, b22, b13 = conv(b,b), conv(a2,a2), conv(a,a3)
    return [Fraction(b4[j]+3*b22[j]-4*b13[j],12) for j in range(d+1)]

def coefficient(n,j):
    return Fraction(n*(n*n-1+3*2**(j-1)-3**j),3)

def log_weights(y):
    out = Counter()
    for a,b in combinations(y,2): out[2*a+2*b] += 1
    for a,b,c in combinations(y,3):
        for v in (a,b,c): out[a+b+c+v] += 1
    for t in combinations(y,4): out[sum(t)] += 2
    return out

def h2(values):
    return Counter(a*b for a,b in combinations_with_replacement(values,2))

def decode_h2(s,k):
    top = isqrt(max(s))
    assert top*top == max(s)
    prefix = [top]
    while len(prefix)<k:
        used = h2(prefix)
        assert all(v<=s.get(t,0) for t,v in used.items())
        residual = s-used
        t,r = divmod(max(residual),top)
        assert r==0 and 0<t<=prefix[-1]
        prefix.append(t)
    assert h2(prefix)==s
    return tuple(prefix)

def main():
    source_before = sha256((ROOT/'source.md').read_bytes()).hexdigest()
    counts = Counter()
    for N in range(2,25):
        seen = {}
        for a in old.partitions(N):
            n = len(a)
            if n<2: continue
            s = old.schur22_monomials(a)
            assert s == old.schur22_jacobi_trudi(a)
            if n<=6:
                assert s==old.schur22_tableaux(a)
                counts['tableau_checks']+=1
            assert sum(s.values())==n*n*(n*n-1)//12
            key = tuple(sorted(s.items()))
            assert key not in seen
            seen[key]=a
            for r in range(2,n):
                used=old.schur22_monomials(a[:r])
                assert all(v<=s.get(t,0) for t,v in used.items())
                assert max(s-used)==a[0]**2*a[1]*a[r]
                counts['prefix_maximum_checks']+=1
            if n<=4:
                e2=old.elementary_values(a,2)
                correction=old.elementary_values(a,4)
                assert h2(list(e2.elements()))==s+correction
                assert decode_h2(s+correction,comb(n,2))==tuple(sorted(e2.elements(),reverse=True))
                if n==4:
                    assert prod(t**v for t,v in s.items())==prod(a)**20
                counts['length_at_most_four_reductions']+=1
            counts['partitions']+=1
    # y are exact integer logarithm coordinates: actual parts can be 2**y.
    # Negative y are allowed here because the proposed criterion covers positive reals.
    for n in range(2,21):
        for y in [tuple(range(n)), tuple(i%3 for i in range(n)), tuple(i-n//2 for i in range(n)), (0,)*n]:
            p=[n]+[sum(v**j for v in y) for j in range(1,n+1)]
            weights=log_weights(y)
            q=output_moments(n,p)
            assert q==[sum(v*t**j for t,v in weights.items()) for j in range(n+1)]
            recovered=[n]
            for j in range(1,n+1):
                c=coefficient(n,j)
                probe=[n]+[0]*j
                probe[j]=1
                assert output_moments(n,probe)[j]==c
                if c==0: break
                residual=output_moments(n,recovered+[0])[j]
                recovered.append((q[j]-residual)/c)
            if len(recovered)==n+1:
                assert recovered==p
                counts['complete_exact_log_moment_recoveries']+=1
            counts['exact_log_weight_samples']+=1
    zeros=[]
    for j in range(1,257):
        a=1+3**j-3*2**(j-1)
        n=isqrt(a)
        if n*n==a: zeros.append({'moment_order':j,'length':n})
    failures=[]
    for n in range(2,257):
        js=[j for j in range(1,n+1) if coefficient(n,j)==0]
        if js: failures.append({'length':n,'zero_orders':js})
    assert source_before==sha256((ROOT/'source.md').read_bytes()).hexdigest()
    out=dict(job_id='newwin-00001-p10-triage-c547cde10837', observed_at_utc=datetime.now(timezone.utc).isoformat(),
        python=platform.python_version(), arithmetic='exact integers and Fractions; no numerical logarithms',
        counts=dict(counts), baseline_domain='All positive integer partitions N=2..24, length>=2',
        log_sample_domain='Four deterministic integer log-coordinate lists for each length 2..20; not exhaustive',
        square_equation_checked_orders=[1,256], square_equation_solutions=zeros,
        coefficient_checked_lengths=[2,256], coefficient_failures=failures,
        source_sha256=source_before, script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        imported_script_sha256=sha256(BASE.read_bytes()).hexdigest(),
        limitations='Calibration only. No all-N resolution, no exhaustive classification beyond stated bounds, and no novelty or referee certification.')
    (ROOT/'evidence/triage-log-moments.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
