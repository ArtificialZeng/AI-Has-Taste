"""Exact attacks on the direct-sum restriction proof; no external workers.

Enumerates ALL insertion triples, including inactive right triples. All
permutations through length 6, plus explicitly listed larger sum families.
The universal argument is in sum-restriction-proof.md; tests are finite.
"""
from collections import Counter, defaultdict
from itertools import combinations_with_replacement, permutations
from pathlib import Path
import hashlib
import json
import random
import time

OUT = Path(__file__).resolve().parent
JOB = 'primary-20260912-ray-west-j-research-db44e3159ae7'


def insertion(p, t):
    r, c, rho = t
    out = [0] * (len(p) + 2)
    for j, v in enumerate(p, 1):
        out[j + sum(x <= j for x in c) - 1] = v + sum(x <= v for x in r)
    vals = (r[0], r[1] + 1)
    out[c[0] - 1] = vals[rho[0]]
    out[c[1]] = vals[rho[1]]
    assert sorted(out) == list(range(1, len(p) + 3))
    return tuple(out)


def active(p, t):
    r, c, rho = t
    return all(all(not (0 <= q < len(p)) or p[q] != r[rho[z]]
                   for q in (c[z] - 2, c[z] - 1)) for z in (0, 1))


def is_c(t, u):
    r, c, _ = t
    s, d, _ = u
    return r[1] < s[0] and (c[1] < d[0] or d[1] < c[0])


def gap(t, u):
    c, d = t[1], u[1]
    return c[1] - 1 if c[1] < d[0] else c[0] - 3


def embed(p, t):
    r, c, _ = t
    return {(j + sum(x <= j for x in c), v + sum(x <= v for x in r)): j
            for j, v in enumerate(p, 1)}


def tracks(p, t, u):
    lhs = {j: pt for pt, j in embed(p, t).items()}
    rhs = embed(p, u)
    r, c, rho = t
    vals, cols = (r[0], r[1] + 1), (c[0], c[1] + 1)
    ans = []
    for z in (0, 1):
        pt = (cols[z], vals[rho[z]])
        track = []
        while pt in rhs:
            j = rhs[pt]
            assert j not in track
            track.append(j)
            pt = lhs[j]
        assert track
        ans.append(track)
    return ans


def restrict_prefix(p, k, t, u):
    tau = insertion(p, t)
    local = tau[:k + 2]
    assert sorted(local) == list(range(1, k + 3))
    s, d, _ = u
    kept = {j + sum(x <= j for x in d) for j in range(1, k + 1)}
    removed = sorted(set(range(1, k + 3)) - kept)
    deleted_values = [local[j - 1] for j in removed]
    vals = sorted(deleted_values)
    new_r = (vals[0], vals[1] - 1)
    new_c = (removed[0], removed[1] - 1)
    new_rho = (0, 1) if deleted_values[0] < deleted_values[1] else (1, 0)
    assert new_r == tuple(min(v, k + 1) for v in s)
    assert new_c == tuple(min(v, k + 1) for v in d)
    new_u = (new_r, new_c, new_rho)
    assert insertion(p[:k], t) == local == insertion(p[:k], new_u)
    assert active(p[:k], t) and is_c(t, new_u)
    assert gap(t, new_u) == gap(t, u)
    return new_u


def components(p):
    cuts = [0] + [i for i in range(1, len(p) + 1) if max(p[:i]) == i]
    return [tuple(x - a for x in p[a:b]) for a, b in zip(cuts, cuts[1:])]


def decreasing(p):
    return p == tuple(range(len(p), 0, -1))


def verify(p, counters, samples):
    m = len(p)
    groups = defaultdict(list)
    multisets = list(combinations_with_replacement(range(1, m + 2), 2))
    for r in multisets:
        for c in multisets:
            for rho in ((0, 1), (1, 0)):
                t = (r, c, rho)
                groups[insertion(p, t)].append(t)
    base = (m**4 + 2*m**3 + m*m + 4*m + 4) // 2
    known_j = base - len(groups)
    left_to_gap = {}
    cuts = [k for k in range(1, m) if max(p[:k]) == k]
    for ambient, triples in groups.items():
        for t in triples:
            if not active(p, t):
                continue
            for u in triples:
                if not is_c(t, u):
                    continue
                counters['all_pattern_c_pairs'] += 1
                counters['inactive_right_pairs'] += not active(p, u)
                g = gap(t, u)
                assert 0 <= g < m - 1
                assert t not in left_to_gap or left_to_gap[t] == g
                left_to_gap[t] = g
                r, c, _ = t
                s, d, _ = u
                positive = c[1] < d[0]
                assert positive == (p[g] > p[g + 1])
                if positive:
                    assert r[0] == p[g + 1]
                    assert c[1] == g + 1
                    assert p[c[0] - 1] == r[1] + 1
                ts = tracks(p, t, u)
                assert sum((g + 1 in tr) for tr in ts) == 1
                assert sum((g + 2 in tr) for tr in ts) == 1
                assert not any(g + 1 in tr and g + 2 in tr for tr in ts)
                col_lo, col_hi = (c[0], d[1]) if positive else (d[0], c[1])
                support = set(range(col_lo, col_hi))
                assert set(sum(ts, [])) == support
                assert set(p[j - 1] for j in support) == set(range(r[0], s[1]))
                for tr in ts:
                    for a, b in zip(tr, tr[1:]):
                        assert p[a - 1] < p[b - 1]
                        assert (a < b) == positive
                for k in cuts:
                    counters['pair_cut_cases'] += 1
                    if g == k - 1:
                        assert not positive
                        assert decreasing(components(p[:k])[-1])
                        assert decreasing(components(tuple(v-k for v in p[k:]))[0])
                        a = k - min(support) + 1
                        b = max(support) - k
                        block = tuple(v - (k-a) for v in p[k-a:k+b])
                        assert block == tuple(range(a, 0, -1)) + tuple(range(a+b, a, -1))
                        counters['join_pairs'] += 1
                    elif g < k - 1:
                        if positive:
                            assert max(r) <= k - 1 and max(c) <= k - 1
                            new_u = restrict_prefix(p, k, t, u)
                            counters['positive_prefix_restrictions'] += 1
                            if new_u[2] != u[2]:
                                counters['right_pattern_changed'] += 1
                                if len(samples) < 8:
                                    old_clipped = (new_u[0], new_u[1], u[2])
                                    samples.append({'pi': p, 'cut': k, 'left': t,
                                                    'right': u, 'ambient': ambient,
                                                    'repaired_right': new_u,
                                                    'left_local_value': insertion(p[:k], t),
                                                    'unrepaired_right_value': insertion(p[:k], old_clipped)})
                        else:
                            assert max(support) <= k and max(p[j-1] for j in support) <= k
                            assert max(r+c+s+d) <= k + 1
                            assert insertion(p[:k], t) == insertion(p[:k], u)
                            assert active(p[:k], t)
                            counters['negative_prefix_localizations'] += 1
                    else:
                        assert min(r+c+s+d) >= k + 1
                        f = lambda z: (tuple(v-k for v in z[0]), tuple(v-k for v in z[1]), z[2])
                        q = tuple(v-k for v in p[k:])
                        assert insertion(q, f(t)) == insertion(q, f(u))
                        assert active(q, f(t)) and is_c(f(t), f(u))
                        assert gap(f(t), f(u)) == g-k
                        counters['suffix_localizations'] += 1
    assert len(left_to_gap) == known_j
    assert len(set(left_to_gap.values())) == known_j
    counters['patterns'] += 1
    return known_j, set(left_to_gap.values())


def main():
    started = time.monotonic()
    counters, samples, by_length = Counter(), [], Counter()
    table = {}
    for m in range(1, 7):
        for p in permutations(range(1, m+1)):
            j, gaps = verify(p, counters, samples)
            table[p] = j, gaps
            for k in range(1, m):
                if max(p[:k]) != k:
                    continue
                a, b = p[:k], tuple(v-k for v in p[k:])
                extra = int(decreasing(components(a)[-1]) and decreasing(components(b)[0]))
                want = table[a][1] | {g+k for g in table[b][1]}
                if extra:
                    want.add(k-1)
                assert gaps == want
                counters['exact_gap_cut_tests'] += 1
            by_length[m] += 1
        print('exhaustive length', m, dict(counters), flush=True)
    rng = random.Random(20260912)
    large = []
    for a, b in [(1,9), (9,1), (2,9), (9,2), (5,7), (7,5)]:
        large.append(tuple(range(a,0,-1))+tuple(range(a+b,a,-1)))
        large.append((2,1)+tuple(range(3,a+b+1)))
        x,y=list(range(1,a+1)),list(range(a+1,a+b+1))
        rng.shuffle(x);rng.shuffle(y)
        large.append(tuple(x+y))
    large = list(dict.fromkeys(large))
    large_rows = []
    for p in large:
        j, gaps = verify(p, counters, samples)
        large_rows.append({'pi': p, 'j': j, 'gaps_zero_based': sorted(gaps)})
    report = {'job_id': JOB,
              'status': 'Exact finite checks of the written restriction proof; no independent referee or novelty certification.',
              'exhaustive_patterns_by_length': dict(by_length),
              'counter_counts': dict(counters),
              'larger_family_selection': 'Selected in pass 2 before these insertion results: decreasing-block sums, 21 followed by singleton sums, seeded arbitrary summands; lengths 10, 11, 12.',
              'larger_family_results': large_rows,
              'clipping_without_repair_counterexamples': samples,
              'failure_count': 0,
              'elapsed_seconds': time.monotonic()-started,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    path = OUT/'sum-restriction-verification.json'
    tmp = path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(report, indent=2)+'\n')
    tmp.replace(path)
    print(json.dumps({k:v for k,v in report.items() if k not in ('larger_family_results', 'clipping_without_repair_counterexamples')}, indent=2))


if __name__ == '__main__':
    main()
