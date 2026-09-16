#!/usr/bin/env python3
"""Second exact certificate: a rational Sturm chain for the gamma quartic."""
from fractions import Fraction as F


def trim(p):
    while len(p) > 1 and p[-1] == 0: p.pop()
    return p


def divrem(a, b):
    a = list(map(F, a)); b = trim(list(map(F, b)))
    if b == [0]: raise ZeroDivisionError
    q = [F(0)] * max(1, len(a) - len(b) + 1)
    while len(a) >= len(b) and a != [0]:
        k = len(a) - len(b); c = a[-1] / b[-1]; q[k] = c
        for j in range(len(b)): a[j + k] -= c * b[j]
        trim(a)
    return trim(q), trim(a)


def proportional_positive(a, b):
    a = trim(list(map(F, a))); b = trim(list(map(F, b)))
    if len(a) != len(b): return None
    ratios = [x/y for x, y in zip(a, b) if y]
    if any((x == 0) != (y == 0) for x, y in zip(a, b)): return None
    return ratios[0] if ratios and ratios[0] > 0 and all(r == ratios[0] for r in ratios) else None


S = [
    [1, 9, 24, 16, 1],
    [9, 48, 48, 4],
    [32, 165, 144],
    [160, 651],
    [-1],
]


def sign_at_infinity(p, positive):
    leading = p[-1]
    if positive or (len(p)-1) % 2 == 0: return 1 if leading > 0 else -1
    return -1 if leading > 0 else 1


def variations(signs):
    return sum(a != b for a, b in zip(signs, signs[1:]))


ratios = []
for i in range(3):
    _, rem = divrem(S[i], S[i+1])
    ratio = proportional_positive([-x for x in rem], S[i+2])
    if ratio is None: raise SystemExit("FAIL invalid Sturm remainder at %d" % i)
    ratios.append(ratio)
minus = [sign_at_infinity(p, False) for p in S]
plus = [sign_at_infinity(p, True) for p in S]
count = variations(minus) - variations(plus)
if ratios != [F(1,4), F(7,1728), F(6848,47089)] or count != 2:
    raise SystemExit("FAIL ratios=%r real_count=%r" % (ratios, count))
print("PASS sturm gamma_real_roots=2 nonreal_roots=2")
print("positive_remainder_scales=" + ",".join(str(x) for x in ratios))
print("variations_minus_infinity=%d variations_plus_infinity=%d" %
      (variations(minus), variations(plus)))
