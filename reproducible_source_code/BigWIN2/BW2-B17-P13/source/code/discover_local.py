#!/usr/bin/env python3
"""Deterministic-seed local falsification search for large exact sumsets."""
import argparse, json, math, random, time

def score(A):
    B=sorted(A)
    return len({a+b for i,a in enumerate(B) for b in B[i:]})

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--n',type=int,default=38); p.add_argument('--k',type=int,default=12)
    p.add_argument('--seconds',type=float,default=60); p.add_argument('--seed',type=int,default=3812)
    p.add_argument('--output',required=True); a=p.parse_args(); rng=random.Random(a.seed)
    best=None; bestv=-1; starts=steps=0; end=time.time()+a.seconds
    while time.time()<end:
        starts+=1; A={1,*rng.sample(range(2,a.n+1),a.k-1)}; v=score(A); temp=2.0
        for q in range(5000):
            steps+=1
            old=rng.choice(tuple(A-{1})); new=rng.choice(tuple(set(range(2,a.n+1))-A))
            C=A-{old}|{new}; w=score(C)
            if w>=v or rng.random()<math.exp((w-v)/temp): A,v=C,w
            temp=max(.03,temp*.998)
            if v>bestv: best,bestv=sorted(A),v
            if time.time()>=end: break
    out={'purpose':'discovery only','parameters':vars(a),'starts':starts,'steps':steps,
         'set':best,'objective':bestv,'sums':sorted({x+y for i,x in enumerate(best) for y in best[i:]})}
    with open(a.output,'w') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
    print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
