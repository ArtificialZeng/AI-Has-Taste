"""Exact continuation of H, using cached minor arrays; single foreground process.

Run: python3 evidence/research_h_probe.py --max-n 512
The triage artifacts are read-only. Every support index is checked explicitly.
"""
import argparse
import hashlib
import json
import time
from pathlib import Path

JOB = "primary-20260913-subsum-denominator-research-c627858a54d2"
ROOT = Path(__file__).resolve().parents[1]


def atomic_json(path, obj):
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(obj, indent=2) + "\n")
    tmp.replace(path)


def shifted_add(a, s):
    b = a + [0] * s
    for j, v in enumerate(a):
        b[j+s] += v
    return b


def minors(a):
    return [a[0]**2] + [v*v-u*w for u,v,w in zip(a,a[1:],a[2:])] + [a[-1]**2]


def at(a,j):
    return a[j] if 0 <= j < len(a) else 0


def digest(a):
    return hashlib.sha256(json.dumps(a,separators=(',',':')).encode()).hexdigest()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--max-n',type=int,default=512)
    p.add_argument('--min-n',type=int,default=257)
    args = p.parse_args()
    assert 2 <= args.min_n <= args.max_n
    started = time.monotonic()
    result = dict(job_id=JOB, exact_arithmetic='Python arbitrary-precision integers',
                  requested_range=[args.min_n,args.max_n], completed_through=args.min_n-1,
                  h_checks=0, five_ninths_checks=0, stages_checked=0,
                  original_internal_minors_checked=0, h_failures=[],
                  five_ninths_failures=[], original_failures=[], stage_failures=[],
                  source_sha256=hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest(),
                  implementation_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  rows=[])
    old_m = None
    a = [1]
    for n in range(1,args.max_n+1):
        shifts = sorted(n >> q for q in range((n & -n).bit_length()))
        for k,s in enumerate(shifts):
            old = a
            a = shifted_add(a,s)
            if n < args.min_n:
                continue
            new_m = minors(a)
            hbad = fbad = sbad = 0
            for j,t in enumerate(new_m):
                base = at(old_m,j) + at(old_m,j-s)
                if 2*t < base:
                    hbad += 1
                    if not result['h_failures']:
                        result['h_failures'].append(dict(n=n,k=k,shift=s,j=j,
                            old_degree=len(old)-1,new_degree=len(a)-1,
                            old_triple=[at(old,j-1),at(old,j),at(old,j+1)],
                            shifted_old_triple=[at(old,j-s-1),at(old,j-s),at(old,j-s+1)],
                            new_triple=[at(a,j-1),at(a,j),at(a,j+1)],
                            new_minor=t,sum_old_minors=base,h_margin=2*t-base))
                if 9*t < 5*base:
                    fbad += 1
                    if not result['five_ninths_failures']:
                        result['five_ninths_failures'].append(dict(n=n,k=k,shift=s,j=j,
                            new_minor=t,sum_old_minors=base,margin=9*t-5*base))
                if t < 0:
                    sbad += 1
                    if not result['stage_failures']:
                        result['stage_failures'].append(dict(n=n,k=k,shift=s,j=j,minor=t,
                            triple=[at(a,j-1),at(a,j),at(a,j+1)]))
            result['h_checks'] += len(a)
            result['five_ninths_checks'] += len(a)
            result['stages_checked'] += 1
            if hbad or fbad or sbad:
                result.setdefault('failing_stage_counts',[]).append(dict(n=n,k=k,
                    h_failures=hbad,five_ninths_failures=fbad,negative_minors=sbad))
            old_m = new_m
        degree = sum(i*(n//i).bit_length() for i in range(1,n+1))
        assert len(a)-1 == degree
        assert a == a[::-1]
        assert sum(a) == 1 << sum((n//i).bit_length() for i in range(1,n+1))
        if n == args.min_n-1:
            old_m = minors(a)
            result['base'] = dict(n=n,degree=degree,coefficients_sha256=digest(a),
                                 negative_internal_minors=sum(t<0 for t in old_m[1:-1]))
            baseline=json.loads((ROOT/'evidence/triage_probe.json').read_text())
            matched=[r for r in baseline['rows'] if r['n']==n]
            if matched:
                assert matched[0]['coefficients_sha256']==result['base']['coefficients_sha256']
                result['base']['matches_triage_digest']=True
        if n >= args.min_n:
            bad=[j for j,t in enumerate(old_m) if t<0]
            result['original_internal_minors_checked'] += len(a)-2
            if bad:
                result['original_failures'].append(dict(n=n,negative_count=len(bad),
                    first=dict(j=bad[0],minor=old_m[bad[0]],
                    triple=[at(a,bad[0]-1),at(a,bad[0]),at(a,bad[0]+1)])))
            result['rows'].append(dict(n=n,degree=degree,stages=len(shifts),
                                       negative_original_minors=len(bad)))
            result['completed_through']=n
            result['elapsed_seconds']=round(time.monotonic()-started,3)
            if n % 16 == 0 or n == args.max_n or bad:
                result['last_coefficients_sha256']=digest(a)
                atomic_json(ROOT/'evidence/research_h_probe.json',result)
                print(json.dumps({k:result[k] for k in ['completed_through','h_checks',
                    'stages_checked','elapsed_seconds']}),flush=True)
    result['complete']=True
    atomic_json(ROOT/'evidence/research_h_probe.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2),flush=True)


if __name__ == '__main__':
    main()
