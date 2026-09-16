#!/usr/bin/env python3
"""Fail-closed exact verifier for the eight-element preorder counterexample.

Uses only the Python standard library.  It recomputes the transitive closure,
all order ideals, every feasible lattice point, the support enumerator, the
gamma coefficients, and an exact Laguerre-inequality violation.
"""
from fractions import Fraction
from itertools import product
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "counterexample_poset.json"


def fail(message):
    raise SystemExit("FAIL: " + message)


def closure(n, edges):
    leq = [[i == j for j in range(n)] for i in range(n)]
    for i, j in edges:
        if i == j:
            fail("strict relation contains a loop")
        leq[i][j] = True
    for k in range(n):
        for i in range(n):
            if leq[i][k]:
                for j in range(n):
                    leq[i][j] = leq[i][j] or leq[k][j]
    for i in range(n):
        for j in range(n):
            if i != j and leq[i][j] and leq[j][i]:
                fail("relation is not antisymmetric")
    return leq


def ideals(leq):
    n = len(leq)
    ans = []
    for mask in range(1 << n):
        if all(not (mask >> y & 1) or not leq[x][y] or (mask >> x & 1)
               for x in range(n) for y in range(n)):
            ans.append(tuple(i for i in range(n) if mask >> i & 1))
    return ans


def direct_h(leq, ideal_list):
    n = len(leq)
    # Each minimal element has singleton ideal, hence coordinate in {0,1};
    # every other coordinate is at most n by the whole-set ideal.
    minimal = [all(not leq[j][i] or j == i for j in range(n)) for i in range(n)]
    ranges = [range(2) if minimal[i] else range(n + 1) for i in range(n)]
    h = [0] * (n + 1)
    feasible = 0
    for x in product(*ranges):
        if all(sum(x[i] for i in ideal) <= len(ideal) for ideal in ideal_list):
            h[sum(v > 0 for v in x)] += 1
            feasible += 1
    if sum(h) != feasible:
        fail("support bins do not sum to feasible-point count")
    return h, feasible


def gamma_from_palindromic(h):
    # Solve h(t)=sum gamma_i t^i(1+t)^(n-2i) triangularly.
    from math import comb
    n = len(h) - 1
    residual = list(h)
    gamma = []
    for i in range(n // 2 + 1):
        g = residual[i]
        gamma.append(g)
        for k in range(n - 2 * i + 1):
            residual[i + k] -= g * comb(n - 2 * i, k)
    if any(residual):
        fail("h has no exact gamma expansion of the required form")
    return gamma


def eval_poly(coeffs, x, derivative=0):
    c = list(coeffs)
    for _ in range(derivative):
        c = [(i + 1) * c[i + 1] for i in range(len(c) - 1)]
    return sum(Fraction(a) * x ** i for i, a in enumerate(c))


def main():
    try:
        raw = DATA.read_bytes()
        obj = json.loads(raw)
        names = obj["elements"]
        pairs = obj["strict_cover_relations"]
        expected = obj["expected_h_coefficients_low_to_high"]
    except Exception as exc:
        fail("malformed input: " + repr(exc))
    if len(names) != 8 or len(set(names)) != 8:
        fail("expected eight distinct elements")
    index = {name: i for i, name in enumerate(names)}
    try:
        edges = [(index[a], index[b]) for a, b in pairs]
    except Exception as exc:
        fail("relation references unknown element: " + repr(exc))
    leq = closure(len(names), edges)
    ideal_list = ideals(leq)
    h, feasible = direct_h(leq, ideal_list)
    if h != expected:
        fail("computed h differs from serialized expected vector: " + repr(h))
    if h != h[::-1] or any(v <= 0 for v in h):
        fail("unexpected loss of palindromicity or coefficient positivity")
    gamma = gamma_from_palindromic(h)
    if gamma != [1, 9, 24, 16, 1]:
        fail("unexpected gamma vector: " + repr(gamma))
    s = Fraction(-1, 4)
    q, qp, qpp = (eval_poly(gamma, s, d) for d in range(3))
    laguerre = qp * qp - q * qpp
    if (q, qp, qpp, laguerre) != (Fraction(1, 256), Fraction(-1, 16),
                                  Fraction(99, 4), Fraction(-95, 1024)):
        fail("exact root obstruction did not reproduce")
    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_hash = hashlib.sha256(raw).hexdigest()
    print("PASS exact-counterexample")
    print("elements=8 ideals=%d feasible_lattice_points=%d" %
          (len(ideal_list), feasible))
    print("h=" + ",".join(map(str, h)))
    print("gamma=" + ",".join(map(str, gamma)))
    print("laguerre_at_-1/4=-95/1024")
    print("input_sha256=" + input_hash)
    print("code_sha256=" + code_hash)


if __name__ == "__main__":
    main()
