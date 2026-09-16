"""Record the precisely stated local-start Newton-positivity kernel K.

Design range only: j<=32. This is not held-out confirmation of K.
Run with --B 64 in a later pass to attack the untested 33<=j<=64 range.
"""
import argparse
import hashlib
import json
from pathlib import Path
from research_edge_probe import margins,differences

ROOT=Path(__file__).resolve().parents[1]


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--B',type=int,default=32)
    args=p.parse_args()
    B=args.B
    out=dict(job_id='primary-20260913-subsum-denominator-research-c627858a54d2',
        edge_bound=B,scope='K design range; no uniform conclusion',polynomials=0,
        newton_coefficients=0,negative_coefficients=[],records=[],
        implementation_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    for s in range(1,B+2):
        tmin=0
        while (s<<tmin)<9:
            tmin+=1
        tmax=tmin
        while (s<<tmax)<max(9,B+1):
            tmax+=1
        values={t:margins(s,t,B) for t in range(tmin,tmax+2*B+1)}
        for j in range(s-1,B+1):
            t0=tmin
            while (s<<t0)<j+1:
                t0+=1
            c=differences([values[t0+h][j] for h in range(2*j+1)])
            out['polynomials']+=1
            out['newton_coefficients']+=len(c)
            out['records'].append(dict(s=s,j=j,t0=t0,newton_coefficients=c))
            for h,v in enumerate(c):
                if v<0:
                    out['negative_coefficients'].append(dict(s=s,j=j,t0=t0,h=h,value=v))
    path=ROOT/'evidence/research_kernel_probe.json'
    tmp=path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out,indent=2)+'\n')
    tmp.replace(path)
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))


if __name__=='__main__':
    main()
