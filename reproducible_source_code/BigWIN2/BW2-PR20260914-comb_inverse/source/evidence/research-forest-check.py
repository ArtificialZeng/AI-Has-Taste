#!/usr/bin/env python3
"""Exact adversarial checks for research-proof.md, using Python stdlib only.

Run from PROJECT_DIR: python3 evidence/research-forest-check.py
Output is atomically installed as evidence/research-forest-check.json.
This is an alternative implementation in the proposer context, not a fresh audit.
"""
from collections import defaultdict
from datetime import datetime, timezone
from functools import lru_cache
from hashlib import sha256
from math import comb
from pathlib import Path
import json

JOB = 'primary-20260914-comb-inverse-research-b437f7246570'
SOURCE_HASH = '43669ff2a9b8b7c472001ccd2e726fe69f54a96d58bb34957d636160c09bcfce'


def plus(a, b):
    out = [0] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def times(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return tuple(out)


def weight(c):
    return (1, 1) if c == 0 else (0, 2, c)


@lru_cache(None)
def forest_shapes(size):
    """Root/sibling recursion; does not use degrees or prefix inequalities.

    A tree is its tuple of children. A forest is its tuple of trees.
    Its first tree has k vertices; its children form a forest of k-1 vertices.
    """
    if size == 0:
        return ((),)
    return tuple((children,) + rest
                 for k in range(1, size + 1)
                 for children in forest_shapes(k - 1)
                 for rest in forest_shapes(size - k))


def postorder(forest):
    out = []
    for tree in forest:
        out.extend(postorder(tree))
        out.append(len(tree))
    return tuple(out)


def reconstruct(degrees):
    stack = []
    for degree in degrees:
        if degree > len(stack):
            raise ValueError('insufficient children')
        if degree:
            children = tuple(stack[-degree:])
            del stack[-degree:]
        else:
            children = ()
        stack.append(children)
    return tuple(stack)


def vectors(length, budget, prefix=()):
    if length == 0:
        yield prefix
    else:
        for value in range(budget + 1):
            yield from vectors(length - 1, budget - value, prefix + (value,))


def prefix_ok(costs):
    total = 0
    for k, c in enumerate(costs, 1):
        total += c
        if total > k:
            return False
    return True


@lru_cache(None)
def multiset_weight(degrees):
    out = (1,)
    for c in degrees:
        out = times(out, weight(c))
    return out


def cubic_coefficients(bound):
    hs = [(1,)]
    a, b, c = (1, 3, 1), (0, 2, 4, 2), (0, 0, 1, 2, 1)
    for n in range(1, bound + 1):
        h = times(a, hs[n-1])
        for i in range(n-1):
            h = plus(h, times(b, times(hs[i], hs[n-2-i])))
        for i in range(n-2):
            for j in range(n-2-i):
                k = n-3-i-j
                h = plus(h, times(c, times(hs[i], times(hs[j], hs[k]))))
        hs.append(h)
    return hs


def recursive_poset_ideals(n):
    """Construct strict comparabilities using the frozen recursion itself."""
    relations = set()
    for k in range(n):
        root = 2*k + 1
        # Labels 0,...,2*k-1 are the old poset; 2*k is the new singleton.
        relations.update((root, v) for v in range(root))
    return [tuple(v for v in range(2*n) if mask >> v & 1)
            for mask in range(1 << (2*n))
            if all(not (mask >> v & 1) or mask >> u & 1
                   for u, v in relations)]


def badd(*polys):
    out = defaultdict(int)
    for poly in polys:
        for monomial, value in poly.items():
            out[monomial] += value
    return {monomial: value for monomial, value in out.items() if value}


def bmul(a, b):
    out = defaultdict(int)
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            out[i+k, j+l] += x*y
    return {monomial: value for monomial, value in out.items() if value}


def bneg(poly):
    return {m: -v for m, v in poly.items()}


def main():
    source = Path('source.md')
    assert sha256(source.read_bytes()).hexdigest() == SOURCE_HASH
    hs = cubic_coefficients(12)

    local = []
    for cost in range(21):
        count = [0, 0, 0]
        for a in range(cost + 1):
            for b in range(cost + 2):
                if a + max(b-1, 0) == cost:
                    count[int(a > 0) + int(b > 0)] += 1
        actual = plus(tuple(count), (0,))
        assert actual == weight(cost)
        local.append({'cost': cost, 'coefficients': actual})

    forest_checks = []
    for n in range(11):
        shapes = forest_shapes(n+1)
        assert len(shapes) == len(set(shapes)) == comb(2*n+2, n+1)//(n+2)
        words = set()
        total_weight = (0,)
        full_weight = (0,)
        component_counts = defaultdict(int)
        for forest in shapes:
            degrees = postorder(forest)
            assert len(degrees) == n+1 and degrees[0] == 0
            assert prefix_ok(degrees[1:])
            assert reconstruct(degrees) == forest
            words.add(degrees[1:])
            component_counts[len(forest)] += 1
            total_weight = plus(total_weight, multiset_weight(tuple(sorted(degrees[1:]))))
            full_weight = plus(full_weight, multiset_weight(tuple(sorted(degrees))))
        assert len(words) == len(shapes)
        valid = set()
        ambient = 0
        for costs in vectors(n, n):
            ambient += 1
            if prefix_ok(costs):
                valid.add(costs)
                assert postorder(reconstruct((0,) + costs)) == (0,) + costs
            else:
                try:
                    reconstruct((0,) + costs)
                except ValueError:
                    pass
                else:
                    raise AssertionError(('invalid word reconstructed', costs))
        assert ambient == comb(2*n, n)
        assert words == valid
        assert total_weight == hs[n]
        assert full_weight == times((1, 1), hs[n])
        forest_checks.append({'n': n, 'vertices': n+1, 'forests': len(shapes),
                              'ambient_cost_words': ambient,
                              'component_counts': dict(sorted(component_counts.items())),
                              'support_polynomial': total_weight})

    lattice_checks = []
    for n in range(6):
        ideals = recursive_poset_ideals(n)
        coeff = [0] * (2*n+1)
        ambient = 0
        for v in vectors(2*n, 2*n):
            ambient += 1
            direct = all(sum(v[j] for j in ideal) <= len(ideal) for ideal in ideals)
            # Reverse recursion order to read the spine from its minimum.
            costs = tuple(v[2*k+1] + max(v[2*k]-1, 0) for k in reversed(range(n)))
            assert direct == prefix_ok(costs), (n, v)
            if direct:
                coeff[sum(x > 0 for x in v)] += 1
        assert ambient == comb(4*n, 2*n)
        assert tuple(coeff) == hs[n]
        lattice_checks.append({'n': n, 'ambient_vectors': ambient,
                               'ideals_including_empty': len(ideals),
                               'support_polynomial': coeff})

    # Clear all rational denominators and check two identities in Z[t,y].
    one, t, y = {(0, 0): 1}, {(1, 0): 1}, {(0, 1): 1}
    q = badd(one, t)
    qy = bmul(q, y)
    d = badd(t, qy)
    wa = badd(d, bmul(badd(t, bneg(one)), qy))
    wb = badd(bmul(q, d), bneg(qy))
    w_residual = badd(bmul(wa, wb), bneg(bmul(bmul(t, t),
                         bmul(q, bmul(badd(one, y), badd(one, qy))))))
    r_residual = badd(bmul(badd(one, qy), d),
                     bneg(bmul(bmul(q, q), bmul(y, badd(one, y)))), bneg(t))
    assert w_residual == {} and r_residual == {}

    old = json.loads(Path('evidence/triage-prefix-check.json').read_text())
    assert hs == [tuple(p) for p in old['prefix_dp_coefficients_n_0_through_12']]
    assert all(h[0] == 1 for h in hs)
    assert all(sum((-1)**j * c for j, c in enumerate(h)) == (-1)**n
               for n, h in enumerate(hs))

    result = {
        'job_id': JOB,
        'observed_at_utc': datetime.now(timezone.utc).isoformat(),
        'source_sha256': SOURCE_HASH,
        'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
        'arithmetic': 'exact integers and symbolic polynomials; deterministic',
        'local_pair_checks_cost_0_through_20': local,
        'forest_checks_n_0_through_10': forest_checks,
        'forests_checked_total': sum(row['forests'] for row in forest_checks),
        'ambient_cost_words_total': sum(row['ambient_cost_words'] for row in forest_checks),
        'recursive_poset_lattice_checks': lattice_checks,
        'ambient_lattice_vectors_total': sum(row['ambient_vectors'] for row in lattice_checks),
        'all_bijection_and_first_leaf_checks_passed': True,
        'all_original_ideal_checks_passed': True,
        'cubic_coefficients_n_0_through_12': hs,
        'cubic_vs_prior_prefix_dp_match': True,
        'symbolic_W_substitution_numerator_residual': w_residual,
        'symbolic_R_summation_numerator_residual': r_residual,
        't_zero_and_minus_one_checks_through_n': 12,
        'uniform_proof_artifact': 'evidence/research-proof.md',
        'finite_computation_is_not_uniform_proof': True,
        'fresh_referee': False,
        'limits': 'Both programs were inspected in this proposer context. These are alternative algorithms, not independent peer review. Exhaustiveness holds only in the reported finite ranges.'
    }
    target = Path('evidence/research-forest-check.json')
    temp = target.with_suffix('.json.tmp')
    temp.write_text(json.dumps(result, indent=2) + '\n')
    temp.replace(target)
    assert sha256(source.read_bytes()).hexdigest() == SOURCE_HASH
    print(json.dumps({'output': str(target), 'checks_passed': True,
                      'forests': result['forests_checked_total'],
                      'cost_words': result['ambient_cost_words_total'],
                      'lattice_vectors': result['ambient_lattice_vectors_total']}))


if __name__ == '__main__':
    main()
