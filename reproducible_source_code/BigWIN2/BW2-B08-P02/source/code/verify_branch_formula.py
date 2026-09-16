#!/usr/bin/env python3
"""Independent exact evaluator using the height-two branch reduction."""
from itertools import product
from math import comb


def poly_add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a): c[i] += v
    for i, v in enumerate(b): c[i] += v
    return c


def poly_mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): c[i + j] += x * y
    return c


def F(r, eps):
    out = [0] * 5
    for e in product(range(r + eps + 1), repeat=4):
        if e[0] > r: continue
        if sum(max(e[i] - (i <= r), 0) for i in range(1, 4)) > eps: continue
        if sum(e) > r + eps: continue
        out[sum(v > 0 for v in e)] += 1
    while out and out[-1] == 0: out.pop()
    return out


def main():
    h = [0]
    table = {}
    for r in range(4):
        for eps in range(2):
            f = F(r, eps)
            table[(r, eps)] = f
            lower = [0] * (4 - r - eps) + [comb(3, r)]
            term = [0]
            for s, count in enumerate(f):
                upper = poly_mul([0] * s + [1], [comb(4 - s, k) for k in range(5 - s)])
                term = poly_add(term, [count * v for v in upper])
            h = poly_add(h, poly_mul(lower, term))
    expected_table = {
        (0,0):[1], (0,1):[1,3], (1,0):[1,2], (1,1):[1,5,5],
        (2,0):[1,4,3], (2,1):[1,7,13,4],
        (3,0):[1,6,9,4], (3,1):[1,9,24,16,1]}
    expected_h = [1,17,106,303,427,303,106,17,1]
    if table != expected_table or h != expected_h:
        raise SystemExit("FAIL branch formula: table=%r h=%r" % (table, h))
    print("PASS branch-formula")
    print("h=" + ",".join(map(str, h)))
    for key in sorted(table): print("F%d%d=%s" % (key + (",".join(map(str, table[key])),)))


if __name__ == "__main__": main()
