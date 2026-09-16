"""Held-out attack on frozen kernel K; preserves all pass-1 artifacts.

The calculation is identical to research_kernel_probe.py, with current
provenance and separate output; 33<=j<=64 is the new range.
"""
import argparse
import hashlib
import json
from pathlib import Path
from research_edge_probe import margins,differences

ROOT=Path(__file__).resolve().parents[1]


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--B',type=int,default=64)
    args=p.parse_args()
    B=args.B
    out=dict(job_id='primary-20260913-subsum-denominator-research-983c87564404',
        edge_bound=B,scope='Frozen K through j=64; held-out range 33<=j<=64; no uniform conclusion',polynomials=0,
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
    path=ROOT/'evidence/research2_kernel_probe.json'
    tmp=path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out,indent=2)+'\n')
    tmp.replace(path)
    print(json.dumps({k:v for k,v in out.items() if k!='records'},indent=2))


if __name__=='__main__':
    main()
