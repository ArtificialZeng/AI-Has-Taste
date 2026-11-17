"""Ex. 7.2.2.4-205, the case n = 1: average number of pointers in the compact trie (method of answer 204, with the
field count TMS + 3, or TMS + 2 when l + TMS = q - 1, or TMS when l + TMS = q) built from ONE random marked involution
a_1..a_q.  P(key) = 3 + sum_{l=1}^{q-1} d_l.  Exact formula:
  E P = 3q + (q+1) E[M] / 3 - sum_{s=1}^{q-1} ( Pnear(s) + 3 Ptight(s) ),
  E[M] = (q - E[F]) / 2, E[F] = 2 q T_{q-1} / T_q  (M pairs, F fixed points),
  Ptight(s) = (q-s)!/(q-2s)! T_{q-2s} / T_q,  Pnear(s) = 2 s (q-s)!/(q-2s+1)! T_{q-2s+1} / T_q  (0 when undefined)."""
from fractions import Fraction as Fr
from math import factorial
import itertools, sys
def Tseq(N):
    T = [1, 2]
    for n in range(2, N + 1): T.append(2 * T[n - 1] + (n - 1) * T[n - 2])
    return T
def formula(q, T):
    EF = Fr(2 * q * T[q - 1], T[q]); EM = (q - EF) / 2
    tot = 3 * q + (q + 1) * EM / 3
    for s in range(1, q):
        if q - 2 * s >= 0: tot -= 3 * Fr(factorial(q - s) // factorial(q - 2 * s) * T[q - 2 * s], T[q])
        if q - 2 * s + 1 >= 0: tot -= Fr(2 * s * (factorial(q - s) // factorial(q - 2 * s + 1)) * T[q - 2 * s + 1], T[q])
    return tot
def all_keys(q):
    """All marked involutions of order q as code strings."""
    def rec(rest, mate):
        if not rest:
            a, t = [], 0; code = {}
            for k in range(1, q + 1):
                j = mate[k]
                if j <= 0: a.append(j)
                elif j > k: t += 1; code[k] = t; a.append(t)
                else: a.append(code[j])
            yield a; return
        x = rest[0]
        for f in (-1, 0):
            mate[x] = f; yield from rec(rest[1:], mate)
        for y in rest[1:]:
            mate[x] = y; mate[y] = x
            yield from rec([z for z in rest[1:] if z != y], mate)
    yield from rec(list(range(1, q + 1)), {})
def pointers(a, q):
    P = 3; TMS = 0; opened = set()
    for l in range(1, q):
        x = a[l - 1]
        if x > 0:
            if x in opened: TMS -= 1
            else: opened.add(x); TMS += 1
        P += TMS if l + TMS == q else TMS + 2 if l + TMS == q - 1 else TMS + 3
    return P
T = Tseq(4000)
for q in range(2, 10):
    keys = list(all_keys(q)); assert len(keys) == T[q]
    avg = Fr(sum(pointers(a, q) for a in keys), len(keys))
    print(f"q={q}: brute force over all {T[q]} keys {avg} = {float(avg):.6f}; formula {formula(q, T)}; equal: {avg == formula(q, T)}")
import math
print("asymptotics: E P - q^2/6 + q^1.5/3 divided by q:")
for q in (100, 400, 1600, 3200):
    v = float(formula(q, T)); print(f"  q={q}: E P = {v:.4f}; (E P - q^2/6 + q^1.5/3)/q = {(v - q*q/6 + q**1.5/3)/q:.6f}")
