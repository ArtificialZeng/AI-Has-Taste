"""Exact bounded triage test; run with python3 evidence/triage_orbits.py.

Polynomial reconstruction DEPENDS on Chen--Selover Remark 2.3 and the
orbit polynomiality used in Theorem 3.12. The separate degree bound is
beta = edges - vertices + 1, from the spanning-tree gauge parametrization.
No floating point arithmetic and no unbounded-positivity conclusion.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent
PRIMES = (2, 3, 5, 7, 11, 13)


def rank(a, p):
    a = [row[:] for row in a]
    r = 0
    for j in range(len(a[0])):
        k = next((k for k in range(r, len(a)) if a[k][j] % p), None)
        if k is None:
            continue
        a[r], a[k] = a[k], a[r]
        inv = pow(a[r][j] % p, -1, p)
        a[r] = [(z * inv) % p for z in a[r]]
        for k in range(r + 1, len(a)):
            t = a[k][j] % p
            a[k] = [(u - t*v) % p for u, v in zip(a[k], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def edge_list(r, c, mask):
    return [(i, j) for i in range(r) for j in range(c)
            if mask >> (i*c+j) & 1]


def tree(r, c, edges):
    parent = list(range(r+c))
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    chosen, other = [], []
    for i, j in edges:
        a, b = root(i), root(r+j)
        if a != b:
            parent[a] = b
            chosen.append((i, j))
        else:
            other.append((i, j))
    return (chosen, other) if len(chosen) == r+c-1 else None


def canonical(r, c, edges):
    return min(sum(1 << (pr[i]*c+pc[j]) for i, j in edges)
               for pr in permutations(range(r))
               for pc in permutations(range(c)))


def orbit_counts(r, c, mask, p):
    chosen, other = tree(r, c, edge_list(r, c, mask))
    a = [[0]*c for _ in range(r)]
    for i, j in chosen:
        a[i][j] = 1
    counts = [0]*(min(r, c)+1)
    for vals in product(range(1, p), repeat=len(other)):
        for (i, j), val in zip(other, vals):
            a[i][j] = val
        counts[rank(a, p)] += 1
    assert sum(counts) == (p-1)**len(other)
    return counts


def multiply(a, b, limit=None):
    ans = [0]*(len(a)+len(b)-1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            ans[i+j] += u*v
    return ans if limit is None else (ans+[0]*limit)[:limit]


def interpolate(xs, ys):
    ans = [Fraction(0)]*len(xs)
    for i, (x, y) in enumerate(zip(xs, ys)):
        term = [Fraction(y)]
        for j, z in enumerate(xs):
            if i != j:
                term = [v/(x-z) for v in multiply(term, [-z, 1])]
        for j, v in enumerate(term):
            ans[j] += v
    assert all(v.denominator == 1 for v in ans), ans
    return [int(v) for v in ans]


def evaluate(coeff, x):
    return sum(v*x**i for i, v in enumerate(coeff))


def components(n, mask):
    edges = edge_list(n, n, mask)
    remaining = set(range(len(edges)))
    ans = []
    while remaining:
        k = remaining.pop()
        used = [edges[k]]
        rows, cols = {edges[k][0]}, {edges[k][1]}
        changed = True
        while changed:
            changed = False
            for k in list(remaining):
                i, j = edges[k]
                if i in rows or j in cols:
                    remaining.remove(k)
                    used.append((i, j))
                    rows.add(i)
                    cols.add(j)
                    changed = True
        rows, cols = sorted(rows), sorted(cols)
        local = [(rows.index(i), cols.index(j)) for i, j in used]
        ans.append((len(rows), len(cols), canonical(len(rows), len(cols), local)))
    return ans


def qpower(k):
    return [1, k, k*(k-1)//2]


def hit_weights(n):
    facts = [[1, 0, 0]]
    for k in range(1, n+1):
        qint = [sum(qpower(j)[z] for j in range(k)) for z in range(3)]
        facts.append(multiply(facts[-1], qint, 3))
    result = []
    prod = [[1, 0, 0]]
    for i in range(n+1):
        scale = multiply(qpower(n*(n-1)//2), facts[n-i], 3)
        result.append([multiply(p, scale, 3) for p in prod])
        new = [[0, 0, 0] for _ in range(len(prod)+1)]
        for d, p in enumerate(prod):
            term = multiply(p, qpower(-i), 3)
            for z in range(3):
                new[d][z] -= p[z]
                new[d+1][z] += term[z]
        prod = new
    return result


def main():
    reps, lookup = {}, {}
    for r in range(1, 4):
        for c in range(1, 4):
            for mask in range(1, 1 << (r*c)):
                edges = edge_list(r, c, mask)
                if tree(r, c, edges) is not None:
                    key = (r, c, canonical(r, c, edges))
                    reps[key] = True
    table = []
    for r, c, mask in sorted(reps):
        beta = mask.bit_count()-r-c+1
        counts = [orbit_counts(r, c, mask, p) for p in PRIMES]
        polynomials = []
        for d in range(min(r, c)+1):
            coeff = interpolate([p-1 for p in PRIMES[:beta+1]],
                                [v[d] for v in counts[:beta+1]])
            assert all(evaluate(coeff, p-1) == vals[d]
                       for p, vals in zip(PRIMES, counts))
            polynomials.append(coeff)
        lookup[(r, c, mask)] = polynomials
        table.append(dict(rows=r, columns=c, mask=mask, edges=edge_list(r, c, mask),
                          cycle_rank=beta, orbit_polynomials_in_x=polynomials,
                          counts_by_prime=dict(zip(map(str, PRIMES), counts))))
    (OUT/'connected_orbits.json').write_text(json.dumps(table, indent=2)+'\n')
    summary = {'job_id': 'newwin-00001-p13-triage-16d0b42a11dd',
               'connected_graph_classes': len(table),
               'classes_by_dimensions': dict(Counter(f'{r}x{c}' for r,c,_ in reps)),
               'nonzero_rank_types_with_defect_at_most_2': sum(
                   any(co) and r+c-d-1 <= 2 for (r,c,_), polys in lookup.items()
                   for d,co in enumerate(polys)),
               'primes_tested': PRIMES, 'maximum_cycle_rank': 4,
               'tests': []}
    for n in (1, 2, 3):
        total = 1 << (n*n)
        exact = [[[0]*3 for _ in range(n+1)] for _ in range(total)]
        for mask in range(total):
            state = {0: [1, 0, 0]}
            for r,c,cmask in components(n, mask):
                nxt = {}
                for d, coeff in enumerate(lookup[(r,c,cmask)]):
                    defect = r+c-d-1
                    if defect > 2 or not any(coeff):
                        continue
                    shifted = ([0]*defect + coeff + [0]*3)[:3]
                    for oldrank, oldcoeff in state.items():
                        value = multiply(oldcoeff, shifted, 3)
                        target = nxt.setdefault(oldrank+d, [0,0,0])
                        for z in range(3):
                            target[z] += value[z]
                state = nxt
            for d, coeff in state.items():
                exact[mask][d] = coeff
        # Subset zeta transform: exact support -> support contained in B.
        mseries = [[a[:] for a in ranks] for ranks in exact]
        for bit in range(n*n):
            for mask in range(total):
                if mask >> bit & 1:
                    for d in range(n+1):
                        for z in range(3):
                            mseries[mask][d][z] += mseries[mask^(1 << bit)][d][z]
        direct_checks = 0
        exact_support_checks = 0
        for p in (2, 3):
            counts = [[0]*(n+1) for _ in range(total)]
            for vals in product(range(p), repeat=n*n):
                mask = sum(1 << k for k,v in enumerate(vals) if v)
                a = [list(vals[i*n:(i+1)*n]) for i in range(n)]
                counts[mask][rank(a, p)] += 1
            for mask in range(total):
                expected = [1]
                for r,c,cmask in components(n, mask):
                    factor = [evaluate(co,p-1)*(p-1)**(r+c-1)
                              for co in lookup[(r,c,cmask)]]
                    expected = multiply(expected, factor)
                expected += [0]*(n+1-len(expected))
                assert expected == counts[mask], (n, p, mask, expected, counts[mask])
                exact_support_checks += n+1
            for bit in range(n*n):
                for mask in range(total):
                    if mask >> bit & 1:
                        for d in range(n+1):
                            counts[mask][d] += counts[mask^(1 << bit)][d]
            for mask in range(total):
                for d in range(n+1):
                    assert counts[mask][d] % (p-1)**d == 0
                    observed = counts[mask][d] // (p-1)**d
                    assert (observed-evaluate(mseries[mask][d],p-1)) % (p-1)**3 == 0
                    direct_checks += 1
        weights = hit_weights(n)
        histogram = Counter()
        negatives = []
        endpoints = {}
        for mask in range(total):
            h = [[0,0,0] for _ in range(n+1)]
            for i in range(n+1):
                for d, w in enumerate(weights[i]):
                    value = multiply(mseries[mask][i], w, 3)
                    for z in range(3):
                        h[d][z] += value[z]
            classical = [0]*(n+1)
            for perm in permutations(range(n)):
                classical[sum(mask >> (i*n+j) & 1 for i,j in enumerate(perm))] += 1
            assert [v[0] for v in h] == classical
            for d, v in enumerate(h):
                histogram[v[2]] += 1
                if v[2] < 0:
                    negatives.append([mask,d,v])
            if mask in (0,total-1):
                endpoints[str(mask)] = h
        summary['tests'].append(dict(n=n, boards=total, board_rank_pairs=total*(n+1),
            direct_M_residue_checks=direct_checks, exact_support_rank_checks=exact_support_checks,
            quadratic_histogram=dict(sorted(histogram.items())),
            negative_quadratic_witnesses=negatives, empty_full_H_series=endpoints))
    (OUT/'triage_test_results.json').write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k != 'tests'}, indent=2))
    print(json.dumps([{k:v for k,v in t.items() if k not in ('quadratic_histogram','empty_full_H_series')}
                      for t in summary['tests']], indent=2))


if __name__ == '__main__':
    main()
