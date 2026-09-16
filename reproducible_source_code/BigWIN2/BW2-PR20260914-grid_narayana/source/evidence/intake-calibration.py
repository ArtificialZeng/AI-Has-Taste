#!/usr/bin/env python3
"""Bounded exact intake calibration; outputs JSON, never a universal proof."""
import json
import platform
from datetime import datetime, timezone
from itertools import accumulate
from math import comb
from time import perf_counter

def vectors(d, remaining, prefix=()):
    if d == 0:
        yield prefix
        return
    for k in range(remaining + 1):
        yield from vectors(d - 1, remaining - k, prefix + (k,))

def grid_count(n, generic=False):
    elements = [(i, 0) for i in range(1, n+1)] + [(i, 1) for i in range(1, n)]
    d = len(elements)
    ideals = None
    if generic:
        ideals = []
        for mask in range(1, 1 << d):
            indices = [j for j in range(d) if mask >> j & 1]
            if all((mask >> k & 1) for j in indices for k in range(d)
                   if elements[k][0] <= elements[j][0] and elements[k][1] <= elements[j][1]):
                ideals.append(indices)
    counts = [0] * (d+1)
    examined = 0
    for x in vectors(d, d):
        examined += 1
        if generic:
            legal = all(sum(x[j] for j in I) <= len(I) for I in ideals)
        else:
            A = [0] + list(accumulate(x[:n]))
            B = [0] + list(accumulate(x[n:]))
            legal = all(A[a] + B[b] <= a+b
                        for a in range(n+1) for b in range(min(a,n-1)+1))
        if legal:
            counts[sum(v != 0 for v in x)] += 1
    assert examined == comb(2*d, d)
    return counts, examined, len(ideals) if generic else None

def narayana_product(n):
    r = n-1
    A = [comb(r,i) * comb(r+1,i) // (i+1) for i in range(r+1)]
    assert all(comb(r,i)*comb(r+1,i) % (i+1) == 0 for i in range(r+1))
    B = [comb(n,i)**2 for i in range(n+1)]
    out = [0]*(2*n)
    for i,a in enumerate(A):
        for j,b in enumerate(B):
            out[i+j] += a*b
    return out

def main():
    start = perf_counter()
    source = {1:[1,1], 2:[1,5,5,1], 3:[1,12,37,37,12,1],
              4:[1,22,138,329,329,138,22,1]}
    cases = []
    for n in range(1,7):
        h, examined, _ = grid_count(n)
        expected = narayana_product(n)
        baseline = grid_count(n,True) if n <= 4 else None
        cases.append({"n":n,"dimension":2*n-1,"complete_ambient_vectors":examined,
                      "actual_coefficients":h,"proposed_coefficients":expected,
                      "identity_matches":h==expected,
                      "primary_table_match":h==source[n] if n in source else None,
                      "generic_all_order_ideals_match":h==baseline[0] if baseline else None,
                      "generic_ideal_count":baseline[2] if baseline else None})
    print(json.dumps({"schema":1,"observed_at":datetime.now(timezone.utc).isoformat(),
                      "python":platform.python_version(),"arithmetic":"exact integers",
                      "randomness":False,"seed":None,
                      "domain":"C_n x C_2 with its unique maximum (n,2) deleted; all lower-ideal inequalities",
                      "range":"n=1..6, all nonnegative coordinate vectors with total at most 2n-1",
                      "method":"Complete ambient composition enumeration with all ideal prefix inequalities; independent generic ideal-mask check for n<=4",
                      "cases":cases,"uniform_proof":False,"independent_holdout":False,
                      "wall_seconds":perf_counter()-start},ensure_ascii=False,indent=2))
if __name__ == "__main__":
    main()
