#!/usr/bin/env python3
"""Exact SymPy discovery computation for the k=4 RV exponential GF.

This implements Chang--Fuchs Proposition 12 literally.  It enumerates rooted
labelled multidigraphs by choosing the two parents of each non-root vertex,
rejects cyclic choices, sums vertex weights, and divides by k!.  No floating
point arithmetic is used.
"""

from __future__ import annotations

import json
from collections import Counter
from itertools import combinations_with_replacement, product
from math import comb, factorial

import sympy as sp


X, z = sp.symbols("X z")


def odd_double_factorial(n: int) -> int:
    if n in (-1, 0, 1):
        return 1
    if n < -1:
        raise ValueError(n)
    ans = 1
    for value in range(n, 0, -2):
        ans *= value
    return ans


_m_cache: dict[tuple[int, int], int] = {}


def one_component_count(leaves: int, reticulations: int) -> int:
    """The Gunawan--Rathin--Zhang recurrence quoted by Chang--Fuchs."""
    if leaves < reticulations or leaves < 0 or reticulations < 0:
        return 0
    key = (leaves, reticulations)
    if key in _m_cache:
        return _m_cache[key]
    if reticulations == 0:
        value = 0 if leaves == 0 else odd_double_factorial(2 * leaves - 3)
    elif reticulations == 1:
        value = (leaves - 1) * odd_double_factorial(2 * leaves - 3)
    else:
        k = reticulations
        value = (leaves + k - 2) * one_component_count(leaves, k - 1)
        value += (k - 1) * one_component_count(leaves, k - 2)
        correction = sum(
            comb(k - 1, d)
            * odd_double_factorial(2 * d - 1)
            * (
                one_component_count(leaves - d, k - 1 - d)
                - one_component_count(leaves + 1 - d, k - 1 - d)
            )
            for d in range(1, k)
        )
        assert correction % 2 == 0
        value += correction // 2
    _m_cache[key] = value
    return value


def one_component_numerator(k: int) -> sp.Expr:
    """Return N_k with F_k=N_k(z)/(1-2z)^((4k-1)/2)."""
    alpha = sp.Rational(4 * k - 1, 2)
    numerator = 0
    for r in range(2 * k):
        coefficient = sum(
            sp.Rational(one_component_count(k + r - j, k), factorial(r - j))
            * sp.binomial(alpha, j)
            * (-2) ** j
            for j in range(r + 1)
        )
        numerator += coefficient * z**r
    return sp.expand(numerator)


def dz(expr: sp.Expr, times: int) -> sp.Expr:
    """Differentiate with respect to z, using z=(1-X^2)/2."""
    for _ in range(times):
        expr = sp.expand(-sp.diff(expr, X) / X)
    return expr


def vertex_weights(k: int) -> dict[tuple[int, int], sp.Expr]:
    fs: dict[int, sp.Expr] = {0: 1 - X}
    for d in range(1, k + 1):
        numerator = one_component_numerator(d)
        fs[d] = sp.expand(numerator.subs(z, (1 - X**2) / 2) / X ** (4 * d - 1))
    weights: dict[tuple[int, int], sp.Expr] = {}
    for children in range(k + 1):
        for double_children in range(children + 1):
            if double_children:
                weight = dz(fs[double_children], children - double_children)
            else:
                forbidden_constant = (
                    0
                    if children == 0
                    else odd_double_factorial(2 * children - 3)
                )
                weight = dz(fs[0], children) - forbidden_constant
            weights[children, double_children] = sp.expand(weight)
    return weights


def is_acyclic(adjacency: list[list[int]]) -> bool:
    m = len(adjacency)
    indegrees = [sum(adjacency[u][v] for u in range(m)) for v in range(m)]
    stack = [v for v in range(m) if indegrees[v] == 0]
    seen = 0
    while stack:
        v = stack.pop()
        seen += 1
        for child in range(m):
            multiplicity = adjacency[v][child]
            if multiplicity:
                indegrees[child] -= multiplicity
                if indegrees[child] == 0:
                    stack.append(child)
    return seen == m


def rv_egf(k: int) -> tuple[sp.Expr, int, Counter]:
    """Compute E_k=sum_l RV_{l,k}z^l/l! by a labelled-DAG sum."""
    m = k + 1
    weights = vertex_weights(k)
    options = {
        v: list(combinations_with_replacement([u for u in range(m) if u != v], 2))
        for v in range(1, m)
    }
    total = 0
    labelled_count = 0
    signatures: Counter = Counter()
    for parent_data in product(*(options[v] for v in range(1, m))):
        adjacency = [[0] * m for _ in range(m)]
        for child, parents in zip(range(1, m), parent_data):
            for parent in parents:
                adjacency[parent][child] += 1
        if not is_acyclic(adjacency):
            continue
        labelled_count += 1
        types = []
        term = 1
        for v in range(m):
            child_set = [child for child in range(m) if adjacency[v][child]]
            vertex_type = (
                len(child_set),
                sum(adjacency[v][child] == 2 for child in child_set),
            )
            types.append(vertex_type)
            term *= weights[vertex_type]
        signatures[tuple(sorted(types))] += 1
        total += term
    return sp.expand(total / factorial(k)), labelled_count, signatures


def laurent_coefficients(expr: sp.Expr) -> dict[int, sp.Rational]:
    coefficients: dict[int, sp.Rational] = {}
    for term in sp.Add.make_args(sp.expand(expr)):
        exponent = int(term.as_powers_dict().get(X, 0))
        coefficient = sp.cancel(term / X**exponent)
        coefficients[exponent] = sp.cancel(coefficients.get(exponent, 0) + coefficient)
    return {exponent: coefficient for exponent, coefficient in coefficients.items() if coefficient}


def main() -> None:
    output = {"one_component_numerators": {}}
    for k in range(1, 5):
        output["one_component_numerators"][str(k)] = str(one_component_numerator(k))
    output["rv_egfs"] = {}
    for k in (2, 3, 4):
        egf, labelled, signatures = rv_egf(k)
        output["rv_egfs"][str(k)] = {
            "labelled_dags_with_root_fixed": labelled,
            "signature_classes": len(signatures),
            "laurent_coefficients": {
                str(exponent): str(coefficient)
                for exponent, coefficient in sorted(laurent_coefficients(egf).items())
            },
        }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
