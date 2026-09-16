#!/usr/bin/env python3
import math
X=529; D=42
V=[487,479,467,457,449,421,461,401,397,367,389,337,331,317,311,307,281,251,241,271,227,197,191,181,157,151,137,131,377,107,97,71,67,215,61,59,47,41,37,31,121]
assert len(V)==41 and len(set(V))==41 and all(2<=v<=X-D for v in V)
S=[z for v in V for z in (v,v+D)]
assert len(S)==82 and len(set(S))==82
bad=[(a,b,math.gcd(a,b)) for i,a in enumerate(S) for b in S[i+1:] if math.gcd(a,b)!=1]
assert not bad,bad
print('WITNESS VERIFIED')
print('x=',X,'d=',D,'V=',','.join(map(str,sorted(V))),sep='')
print('numbers=',','.join(map(str,sorted(S))),sep='')
