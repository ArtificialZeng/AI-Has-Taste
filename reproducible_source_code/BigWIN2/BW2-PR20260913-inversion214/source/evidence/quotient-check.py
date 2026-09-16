#!/usr/bin/env python3
"""Exact checks of the fixed triage quotient; no algebraicity inference.

Three separately implemented computations: the explicit quotient, the
published left-growth rule, and a right-append DP from the forbidden triple.
Run from PROJECT_DIR: python3 evidence/quotient-check.py
"""
from collections import Counter
from math import comb
from pathlib import Path
import hashlib
import json
import platform

JOB = "primary-20260913-inversion214-research-aabee08e3bf3"
N = 40
# A Laurent shift by at most N+3 and final division by z^3 occur below.
# This precision leaves strictly more than N reliable output coefficients.
M = 2*N + 12


def const(c):
    return [c] + [0]*M


def add(a, b):
    return [x+y for x, y in zip(a, b)]


def neg(a):
    return [-x for x in a]


def sub(a, b):
    return add(a, neg(b))


def shift(a, k):
    if k >= 0:
        return ([0]*k+a)[:M+1]
    assert all(v == 0 for v in a[:-k]), "nonintegral Laurent shift"
    return a[-k:]+[0]*(-k)


def mul(a, b):
    out = const(0)
    for i, ai in enumerate(a):
        if ai:
            for j in range(M+1-i):
                if b[j]:
                    out[i+j] += ai*b[j]
    return out


def inv(a):
    assert a[0] == 1, "only unit constant 1 is inverted"
    out = const(1)
    for n in range(1, M+1):
        out[n] = -sum(a[k]*out[n-k] for k in range(1, n+1))
    return out


def div(a, b):
    return mul(a, inv(b))


def val(a):
    return next((i for i, x in enumerate(a) if x), None)


one = const(1)
z = shift(one, 1)
X = [0] + [comb(2*n, n)//(n+1) for n in range(1, M+1)]
assert sub(X, shift(mul(add(one, X), add(one, X)), 1)) == const(0)
q = div(mul(X, X), add(one, add(X, X)))
B = div(mul(mul(X, X), X), mul(add(one, X), add(one, add(X, X))))


def quotient(terms):
    t = q[:]
    E = one[:]  # D_j = z^(j+1) E, with E(0)=1.
    A = const(0)
    L = q[:]
    orders = []
    for j in range(terms):
        zt = shift(t, 1)
        h = sub(mul(add(one, t), add(one, t)), shift(t, -1))
        assert h[0] == 1
        E = mul(E, h)
        r = div(sub(sub(one, z), zt), sub(one, zt))
        r0 = neg(shift(mul(mul(t, t), r), 1))
        r1 = mul(mul(mul(t, t), r), sub(sub(one, z), zt))
        alpha = shift(div(r0, E), -(j+1))
        beta = shift(div(r1, E), -(j+1))
        assert val(t) == j+2
        assert val(alpha) == j+4 and val(beta) == j+3
        orders.append([j, val(t), val(alpha), val(beta)])
        A = add(A, alpha)
        L = add(L, beta)
        t = div(zt, sub(one, zt))
    numerator = sub(B, A)
    denominator = shift(L, 1)
    assert val(numerator) == val(denominator) == 3
    result = div(shift(numerator, -3), shift(denominator, -3))
    return result[:N+1], orders, numerator[:12], denominator[:12]


def published_rule(bound):
    states = Counter({(0, 0): 1})
    counts = []
    linear = []
    for n in range(bound+1):
        counts.append(sum(m for (p, s), m in states.items()
                          if s == 0 and p <= 2))
        linear.append(states[1, 0])
        nxt = Counter()
        for (p, s), m in states.items():
            nxt[p+1, s] += m
            if s > 0:
                nxt[p+1, s-1] += m
            else:
                for ell in range(p):
                    nxt[p-ell, ell] += m
                for ell in range(p-1):
                    nxt[p-ell-1, ell] += m
        states = nxt
    return counts, linear


def definition_dp(bound):
    # M1 >= M2 are the two largest previous entries WITH multiplicity.
    # -1 pads prefixes of length < 2. A new entry v is legal iff v > M2.
    states = {(-1, -1): 1}
    counts = [1]
    for n in range(1, bound+1):
        nxt = {}
        for (m1, m2), multiplicity in states.items():
            for v in range(m2+1, n):
                pair = (v, m1) if v >= m1 else (m1, v)
                nxt[pair] = nxt.get(pair, 0) + multiplicity
        states = nxt
        counts.append(sum(states.values()))
    return counts


def literal_definition(bound):
    words = [()]
    counts = [1]
    for n in range(1, bound+1):
        words = [w+(v,) for w in words for v in range(n)
                 if not any(w[i] >= v and w[j] >= v
                            for i in range(len(w))
                            for j in range(i+1, len(w)))]
        counts.append(len(words))
    return counts


formula, orders, numerator, denominator = quotient(N)
formula_extra, _, _, _ = quotient(N+2)
rule, linear = published_rule(N+1)
direct = definition_dp(N)
literal = literal_definition(9)
assert formula == formula_extra == rule[:N+1] == direct
assert literal == direct[:10]
assert linear[1:] == rule[:-1]
contacts = []
for m in range(0, 21):
    approximant, _, _, _ = quotient(m)
    residual = [a-b for a, b in zip(approximant, formula)]
    first = next(i for i, v in enumerate(residual) if v)
    assert first == m+3 and residual[first] == 1
    contacts.append({"m": m, "first_error_degree": first,
                     "first_error_coefficient": residual[first]})
out = {
    "job_id": JOB,
    "python": platform.python_version(),
    "arithmetic": "exact Python integers, truncated formal series; no floats",
    "formula_version": "Q exactly as frozen in evidence/triage-kernel.md",
    "formula_source_sha256": hashlib.sha256(Path('evidence/triage-kernel.md').read_bytes()).hexdigest(),
    "coefficient_range": [0, N],
    "internal_absolute_degree": M,
    "summands": N,
    "additional_summands_stability": 2,
    "held_out_relative_to_triage_derivation": [17, 20],
    "held_out_counts": {str(n): formula[n] for n in range(17, 21)},
    "all_three_methods_equal": True,
    "formula_counts": formula,
    "published_rule_counts": rule[:N+1],
    "definition_dp_counts": direct,
    "literal_definition_range": [0, 9],
    "literal_definition_counts": literal,
    "F_equals_linear_over_z_range": [0, N],
    "orders_columns": ["j", "t_j", "R0_over_D_j", "R1_over_D_j"],
    "orders": orders,
    "finite_contact_checks": contacts,
    "numerator_initial_coefficients": numerator,
    "denominator_initial_coefficients": denominator,
    "scope": "Finite implementation checks, supporting the separate formal proof. No transcendence, algebraicity, analytic convergence, asymptotic, or novelty certificate. The implementations share a worker, not an independent referee.",
}
Path('evidence/quotient-check.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k: out[k] for k in ['coefficient_range', 'internal_absolute_degree', 'all_three_methods_equal', 'held_out_counts', 'literal_definition_range']}, indent=2))
