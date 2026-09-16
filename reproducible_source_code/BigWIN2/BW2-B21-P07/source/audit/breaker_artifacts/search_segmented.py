#!/usr/bin/env python3
"""Memory-bounded exact search, using an odd-only segmented sieve."""
import argparse, hashlib, json, math, platform, sys, time
from pathlib import Path

def simple_primes(limit):
    b=bytearray(b"\x01")*(limit+1); b[:2]=b"\x00\x00"
    for p in range(2,math.isqrt(limit)+1):
        if b[p]: b[p*p:limit+1:p]=b"\x00"*(((limit-p*p)//p)+1)
    return [i for i in range(2,limit+1) if b[i]]

def prime_stream(upper, segment_odds):
    yield 2
    base=simple_primes(math.isqrt(upper))
    lo=3
    while lo<=upper:
        hi=min(upper+1,lo+2*segment_odds)
        flags=bytearray(b"\x01")*((hi-lo+1)//2)
        for p in base[1:]:
            if p*p>=hi and p>math.isqrt(hi-1): break
            start=max(p*p,((lo+p-1)//p)*p)
            if start%2==0: start+=p
            if start<hi: flags[(start-lo)//2::p]=b"\x00"*(((hi-1-start)//(2*p))+1)
        for j,f in enumerate(flags):
            if f: yield lo+2*j
        lo=hi if hi%2 else hi+1

def nth_upper(n):
    if n<6:return 15
    x=float(n); return math.ceil(x*(math.log(x)+math.log(math.log(x))))+10

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--count",type=int,required=True)
    ap.add_argument("--segment-odds",type=int,default=500000); ap.add_argument("--output",required=True)
    z=ap.parse_args(); t=time.time(); a=0; hits=[]; checkpoints=[]; lastp=0
    for n,p in enumerate(prime_stream(nth_upper(z.count),z.segment_odds),1):
        if n>z.count: break
        prev=a; s=prev+p
        while s%2==0: s//=2
        a=s; lastp=p
        if a==1: hits.append({"n":n,"p_n":p,"a_prev":prev,"sum":prev+p,"exponent":((prev+p).bit_length()-1)})
        if n in (33900,100000,1000000,z.count): checkpoints.append({"n":n,"p_n":p,"a_n":a})
    assert n>=z.count
    d={"algorithm":"odd-only segmented Eratosthenes; repeated exact division by 2", "count":z.count,
      "segment_odds":z.segment_odds,"last_prime":lastp,"last_a":a,"hits":hits,"checkpoints":checkpoints,
      "elapsed_seconds":time.time()-t,"python":sys.version,"platform":platform.platform()}
    raw=json.dumps(d,sort_keys=True,indent=2)+"\n"; Path(z.output).write_text(raw)
    print(raw,end=""); print("output_sha256",hashlib.sha256(raw.encode()).hexdigest())
if __name__=="__main__":main()
