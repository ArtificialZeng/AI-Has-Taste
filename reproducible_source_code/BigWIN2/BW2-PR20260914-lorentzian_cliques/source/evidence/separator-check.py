"""Exact bounded verification; run python3 evidence/separator-check.py.

No random sampling, no graph-isomorphism reductions, no numerical eigenvalues.
The exhaustive domain is all 0/1 k by k bipartite adjacency matrices, k=2..4.
Minimum degree two is a proved necessary prefilter; all remaining hypotheses
are checked by enumerating every vertex subset. Structured larger examples
are separately labeled and are not an exhaustive extension.
"""
from collections import Counter
from itertools import combinations
from math import factorial
from pathlib import Path
from fractions import Fraction
import hashlib
import json

JOB = "primary-20260914-lorentzian-cliques-research-d50fb585b2a3"


def components(adj, removed=0):
    unseen = ((1 << len(adj)) - 1) & ~removed
    result = []
    while unseen:
        frontier = unseen & -unseen
        comp = 0
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            if not unseen & bit:
                continue
            unseen ^= bit
            comp |= bit
            frontier |= adj[bit.bit_length() - 1] & unseen
        result.append(comp)
    return result


def independent_sets(adj):
    valid = [False] * (1 << len(adj))
    valid[0] = True
    by_size = [[] for _ in range(len(adj) + 1)]
    by_size[0].append(0)
    for mask in range(1, len(valid)):
        bit = mask & -mask
        rest = mask ^ bit
        if valid[rest] and not (adj[bit.bit_length() - 1] & rest):
            valid[mask] = True
            by_size[mask.bit_count()].append(mask)
    return valid, by_size


def direct_coefficient(by_size, a, b):
    return sum(not (x & y) for x in by_size[a] for y in by_size[b])


def check_graph(adj, k, by_size, label):
    n = 2 * k
    left = (1 << k) - 1
    right = left << k
    assert len(components(adj)) == 1
    assert by_size[k] == [left, right]
    assert not any(by_size[k + 1:])
    assert all(len(components(adj, 1 << v)) == 1 for v in range(n))
    # Independently check the expansion hypothesis proved in the argument.
    for part in [left, right]:
        subset = (part - 1) & part
        while subset:
            neighbors = 0
            for v in range(n):
                if subset >> v & 1:
                    neighbors |= adj[v]
            assert neighbors.bit_count() >= subset.bit_count() + 1
            subset = (subset - 1) & part
    cross_hist, same_hist = Counter(), Counter()
    general_formula = 0
    for u, v in combinations(range(n), 2):
        comps = components(adj, (1 << u) | (1 << v))
        sizes = [((m & left).bit_count(), (m & right).bit_count())
                 for m in comps]
        # General component-bipartition formula, independent of simplification.
        poly = Counter({0: 1})
        for a, b in sizes:
            nxt = Counter()
            for exponent, value in poly.items():
                nxt[exponent + a] += value
                nxt[exponent + b] += value
            poly = nxt
        contribution = poly[k - 1]
        general_formula += contribution
        if (u < k) != (v < k):
            cross_hist[len(comps)] += 1
            assert all(a == b for a, b in sizes)
            assert contribution == 2 ** len(comps)
        else:
            same_hist[len(comps)] += 1
            if len(comps) > 1:
                assert len(comps) == 2
                assert all(abs(a - b) == 1 for a, b in sizes)
                assert contribution == 2
            else:
                assert contribution == 0
    same_cuts = sum(count for q, count in same_hist.items() if q > 1)
    formula = sum(count * 2 ** q for q, count in cross_hist.items()) + 2 * same_cuts
    beta = [k - 1, k - 1, 0]
    hessian = []
    coefficients = {}
    for i in range(3):
        row = []
        for j in range(3):
            exponent = beta.copy()
            exponent[i] += 1
            exponent[j] += 1
            c = direct_coefficient(by_size, exponent[0], exponent[1])
            coefficients[','.join(map(str, exponent))] = c
            row.append(c * factorial(exponent[0]) * factorial(exponent[1])
                       * factorial(exponent[2]))
        hessian.append(row)
    c = coefficients[f'{k-1},{k-1},2']
    assert c == general_formula == formula
    t = Fraction(c, k * k)
    normalized = [[Fraction(x, 2 * factorial(k) ** 2) for x in row]
                  for row in hessian]
    assert normalized == [[0, 1, 1], [1, 0, 1], [1, 1, t]]
    has_cut = same_cuts > 0 or any(q > 1 for q in cross_hist)
    assert c >= 2 * k * k
    assert (c > 2 * k * k) == has_cut
    return {'label': label, 'k': k, 'edges': [[u, v] for u in range(n)
                for v in range(u+1, n) if adj[u] >> v & 1],
            'coefficient': c, 'excess': c - 2 * k * k,
            'cross_component_histogram': dict(sorted(cross_hist.items())),
            'same_component_histogram': dict(sorted(same_hist.items())),
            'has_two_vertex_cut': has_cut, 'hessian': hessian,
            'normalized_determinant': str(2 - t),
            'inertia_positive_negative_zero': [2, 1, 0] if has_cut else [1, 1, 1]}


def from_edges(k, edges):
    adj = [0] * (2 * k)
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u
    return adj


def main():
    summaries, examples = [], []
    for k in range(2, 5):
        seen, minimum_degree, eligible, strict = 0, 0, 0, 0
        histogram = Counter()
        digest = hashlib.sha256()
        for graph_mask in range(1 << (k * k)):
            seen += 1
            rows = [(graph_mask >> (k * i)) & ((1 << k) - 1)
                    for i in range(k)]
            if any(row.bit_count() < 2 for row in rows):
                continue
            if any(sum(row >> j & 1 for row in rows) < 2 for j in range(k)):
                continue
            minimum_degree += 1
            adj = from_edges(k, [(i, k + j) for i in range(k) for j in range(k)
                                 if rows[i] >> j & 1])
            valid, by_size = independent_sets(adj)
            if by_size[k] != [(1 << k) - 1, ((1 << k) - 1) << k]:
                continue
            if any(by_size[k+1:]) or len(components(adj)) != 1:
                continue
            record = check_graph(adj, k, by_size, f'k={k},mask={graph_mask}')
            eligible += 1
            strict += record['has_two_vertex_cut']
            histogram[record['excess']] += 1
            digest.update(json.dumps(record, sort_keys=True).encode() + b'\n')
            if not any(e['k'] == k and e['excess'] == record['excess'] for e in examples):
                examples.append(record)
        summary = {'k': k, 'all_labeled_fixed_part_graphs': seen,
                   'minimum_degree_two': minimum_degree,
                   'satisfying_original_independent_set_hypothesis': eligible,
                   'two_cut_strict_cases': strict, 'no_two_cut_equality_cases': eligible-strict,
                   'excess_histogram': dict(sorted(histogram.items())),
                   'ordered_verified_records_sha256': digest.hexdigest()}
        summaries.append(summary)
        print(json.dumps(summary), flush=True)

    structured = []
    for k in range(2, 8):
        families = {
            'cycle': [(i, k+i) for i in range(k)] + [(i, k+(i+1)%k) for i in range(k)],
            'complete_bipartite': [(i,k+j) for i in range(k) for j in range(k)],
        }
        if k >= 3:
            # Odd theta: t=k-1 internally disjoint length-three paths, no uv edge.
            families['odd_theta'] = [(0,k+i) for i in range(1,k)] + [
                (i,k+i) for i in range(1,k)] + [(i,k) for i in range(1,k)]
            families['complete_minus_matching'] = [(i,k+j) for i in range(k)
                                                    for j in range(k) if i != j]
        for name, edges in families.items():
            adj = from_edges(k, edges)
            _, by_size = independent_sets(adj)
            record = check_graph(adj, k, by_size, f'{name},k={k}')
            if name == 'cycle':
                assert record['coefficient'] == 6*k*(k-1)
            if name == 'complete_bipartite':
                assert record['coefficient'] == (12 if k == 2 else 2*k*k)
            structured.append(record)

    result = {'job_id': JOB, 'exact_arithmetic': True,
              'exhaustive_domain': 'Every labeled fixed-part bipartite graph, k=2,3,4; no symmetry reduction',
              'prefilter': 'Minimum degree at least two, necessary by the proved strict expansion lemma',
              'hypothesis_check': 'Every vertex subset enumerated for independent sets; connectedness checked',
              'target': [[0,1,1],[1,0,1],[1,1,1]],
              'target_characteristic_polynomial': '(lambda+1)(lambda^2-2lambda-1)',
              'exhaustive_summary': summaries, 'representatives_by_k_and_excess': examples,
              'structured_checks': structured,
              'scope': 'Finite verification of the self-contained theorem; no proof from enumeration and no referee acceptance',
              'source_sha256': hashlib.sha256(Path('source.md').read_bytes()).hexdigest()}
    dest = Path('evidence/separator-check.json')
    temp = dest.with_suffix('.json.tmp')
    temp.write_text(json.dumps(result, indent=2)+'\n')
    temp.replace(dest)
    print(json.dumps({'output': str(dest), 'all_assertions_passed': True,
                      'structured_checks': len(structured)}), flush=True)


if __name__ == '__main__':
    main()
