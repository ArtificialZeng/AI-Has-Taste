#!/usr/bin/env python3
"""Exact validation of hook-prefix-proof.md; no inference from finite to infinite.

Independent of the saved triage implementation: dense integer/Fraction arrays,
rows from connected-graph edge counts, and direct hooks from Newton power sums
and sum_j (-1)^j p_(a+j)e_(b-j). No previous checker or output is imported.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb, factorial
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
JOB = 'primary-20260914-brugidou-positivity-research-cd617853de0e'


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q, scale=1, shift=0):
    out = list(p) + [0] * max(0, len(q) + shift - len(p))
    for i, x in enumerate(q):
        out[i + shift] += scale * x
    return trim(out)


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return trim(out)


def prefixes(p):
    out = []
    total = 0
    for x in p:
        total += x
        out.append(total)
    return out


def divide_1mq(p):
    out = prefixes(p)
    assert out[-1] == 0, ('nonzero remainder', out[-1])
    return trim(out)


@lru_cache(None)
def connected(n):
    """Counts of connected labeled graphs by number of edges, via root component."""
    if n == 1:
        return (1,)
    edges = comb(n, 2)
    out = [comb(edges, k) for k in range(edges+1)]
    for j in range(1, n):
        other_edges = comb(n-j, 2)
        other = [comb(other_edges, k) for k in range(other_edges+1)]
        out = add(out, mul(connected(j), other), -comb(n-1, j-1))
    assert all(x >= 0 for x in out)
    assert out[:n-1] == [0]*(n-1)
    return tuple(out)


@lru_cache(None)
def tree(n):
    """T_(K_n)(1,q)=sum_connected (q-1)^(edges-n+1)."""
    out = [0]
    for e, count in enumerate(connected(n)):
        if not count:
            continue
        degree = e-n+1
        term = [count*comb(degree, k)*(-1)**(degree-k)
                for k in range(degree+1)]
        out = add(out, term)
    assert len(out)-1 == comb(n-1, 2) if n >= 2 else len(out) == 1
    assert all(x > 0 for x in out)
    return tuple(out)


@lru_cache(None)
def hook(a, b):
    if a == 2:
        return tuple([1]*(b+1))
    numerator = [comb(a+b-1, a-2)*x for x in tree(a-1)]
    numerator = add(numerator, hook(a-1, b+1), -1, b+1)
    out = divide_1mq(numerator)
    assert len(out)-1 == comb(a-1, 2)+(a-1)*b
    return tuple(out)


@lru_cache(None)
def newton_power(n):
    # n e_n = sum_(j=1)^n (-1)^(j-1)e_(n-j)p_j.
    out = [Fraction(0)]*comb(n, 2) + [Fraction((-1)**(n-1), factorial(n-1))]
    for j in range(1, n):
        out = add(out, newton_power(j),
                  Fraction((-1)**(n-j-1), factorial(n-j)), comb(n-j, 2))
    return tuple(out)


def direct_hook(a, b):
    # [t^b] E(t) sum_i x_i^a/(1+x_i t).
    specialized = [Fraction(0)]
    for j in range(b+1):
        specialized = add(specialized, newton_power(a+j),
                          Fraction((-1)**j, factorial(b-j)), comb(b-j, 2))
    valuation = comb(b+1, 2)
    assert specialized[:valuation] == [0]*valuation
    out = [factorial(a+b-1)*x for x in specialized[valuation:]]
    for _ in range(a-1):
        out = divide_1mq(out)
    assert all(x.denominator == 1 for x in out)
    return tuple(int(x) for x in out)


def prufer_tree(word, n):
    degrees = [1]*(n+1)
    for x in word:
        degrees[x] += 1
    adjacent = [[] for _ in range(n+1)]
    for x in word:
        v = next(i for i in range(1, n+1) if degrees[i] == 1)
        adjacent[v].append(x)
        adjacent[x].append(v)
        degrees[v] -= 1
        degrees[x] -= 1
    u, v = [i for i in range(1, n+1) if degrees[i] == 1]
    adjacent[u].append(v)
    adjacent[v].append(u)
    parent = [0]*(n+1)
    order = [1]
    for v in order:
        for u in adjacent[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)
    inv = 0
    for v in range(2, n+1):
        u = parent[v]
        while u:
            inv += u > v
            u = parent[u]
    return inv, len(adjacent[n]) == 1


def digest(values):
    return hashlib.sha256(json.dumps(values, separators=(',', ':')).encode()).hexdigest()


def main():
    source_hash = hashlib.sha256((ROOT/'source.md').read_bytes()).hexdigest()
    assert source_hash == '41514463fec1850514a2d7e769680ea0403b78bc8ec786ce51eef70271847b1d'
    definition_count = 0
    for n in range(2, 13):
        for a in range(2, n+1):
            b = n-a
            assert hook(a, b) == direct_hook(a, b), ('direct', a, b)
            definition_count += 1

    tree_checks = []
    for n in range(2, 8):
        all_hist, leaf_hist = Counter(), Counter()
        for word in product(range(1, n+1), repeat=n-2):
            inv, maximal_leaf = prufer_tree(word, n)
            all_hist[inv] += 1
            if maximal_leaf:
                leaf_hist[inv] += 1
        assert tuple(all_hist[i] for i in range(len(tree(n)))) == tree(n)
        if n >= 3:
            expected = tuple((n-1)*x for x in tree(n-1))
            assert tuple(leaf_hist[i] for i in range(max(leaf_hist)+1)) == expected
        tree_checks.append({'n': n, 'trees': sum(all_hist.values()),
                            'largest_leaf_trees': sum(leaf_hist.values())})

    cases = []
    prefix_identities = 0
    prefix_coefficients = 0
    threshold_cases = 0
    row_checks = 0
    for a in range(2, 17):
        D = comb(a-2, 2)
        cutoff = max(0, (D-3)//2)  # ceil((D-4)/2)
        old_cutoff = max(0, D-1)
        legs = sorted(set(range(9)) | {max(0, cutoff-1), cutoff, cutoff+1,
                                      max(0, old_cutoff-1), old_cutoff})
        if a >= 4:
            excess = add(tree(a-1), tree(a-2), -(a-2))
            assert min(excess) >= 0
            assert excess[1]*2 == factorial(a-2)
            row_checks += 1
        for b in legs:
            values = hook(a, b)
            last = min(len(values)-1, 2*b+3)
            assert min(values[:last+1]) > 0, ('initial', a, b)
            prefix_coefficients += last+1
            if b >= cutoff:
                assert min(values) > 0, ('region', a, b)
                threshold_cases += 1
            if a >= 4:
                s = b+1
                A = [comb(a+b-1, a-2)*x for x in tree(a-1)]
                P = [comb(a+b-1, a-3)*x for x in tree(a-2)]
                Delta = add(A, P, -(s+1))
                assert all(x >= 0 for x in Delta)
                assert 2*Delta[1] == (s+1)*P[0]
                p = lambda i: P[i] if i < len(P) else 0
                delta_prefix = lambda k: sum(Delta[:k+1])
                for t in range(s+1):
                    k = s+t
                    rhs = (delta_prefix(k) + sum((s-t+i)*p(i) for i in range(t+1))
                           + (s+1)*sum(p(i) for i in range(t+1, k+1)))
                    assert values[k] == rhs, ('identity8', a, b, k)
                    prefix_identities += 1
                k = 2*s+1
                C0 = hook(a-2, b+2)[0]
                rhs = (delta_prefix(k) + sum((i-1)*p(i) for i in range(s+2))
                       + (s+1)*sum(p(i) for i in range(s+2, k+1)) + C0)
                assert values[k] == rhs, ('identity9', a, b)
                assert 2*values[k] >= (s-1)*P[0] + 2*C0 > 0
                prefix_identities += 1
            cases.append({'a': a, 'b': b, 'degree': len(values)-1,
                          'new_cutoff': cutoff, 'old_cutoff': old_cutoff,
                          'covered_by_new_region': b >= cutoff,
                          'checked_initial_last_index': last,
                          'minimum_initial_coefficient': min(values[:last+1]),
                          'minimum_full_coefficient': min(values),
                          'coefficient_sha256': digest(values)})

    explicit = [60, 120, 130, 110, 80, 55, 35, 20, 10, 4, 1]
    assert list(hook(5, 1)) == explicit
    a5_count = 0
    for b in range(13):
        lhs = mul(hook(5, b), [1, -2, 1])
        rhs = mul([comb(b+4, 3)*x for x in tree(4)], [1, -1])
        rhs = add(rhs, tree(3), -comb(b+4, 2), b+1)
        rhs = add(rhs, hook(3, b+2), 1, 2*b+3)
        assert lhs == rhs
        a5_count += 1

    result = {
        'job_id': JOB, 'arithmetic': 'exact integers and fractions.Fraction',
        'source_sha256': source_hash,
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'direct_definition_checks': definition_count, 'direct_max_size': 12,
        'tree_enumeration': tree_checks, 'row_excess_checks_a_range': [4, 16],
        'row_excess_checks': row_checks, 'tested_hook_cases': len(cases),
        'initial_coefficients_checked': prefix_coefficients,
        'prefix_identity_checks': prefix_identities,
        'full_positivity_cases_inside_new_region': threshold_cases,
        'a5_symbolic_identity_specializations': a5_count, 'a5_b_range': [0, 12],
        'a5_b1_coefficients': explicit, 'cases': cases, 'failures': [],
        'limitations': 'Finite validation of the proof identities and endpoints only. '
          'The infinite claims are justified by hook-prefix-proof.md. '
          'No exhaustive all-partition search, independent model review, or novelty certification.'
    }
    target = Path(__file__).with_suffix('.json')
    temporary = target.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(result, indent=2)+'\n')
    temporary.replace(target)
    print(json.dumps({k: v for k, v in result.items() if k not in ('cases',)}, indent=2))


if __name__ == '__main__':
    main()
