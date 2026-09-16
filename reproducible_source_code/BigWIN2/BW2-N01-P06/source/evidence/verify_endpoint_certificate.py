"""Check the endpoint certificate without importing any census code.

Domain completeness follows from the independently computed scalar counts in
evidence/disproof.md: every classical endpoint is a shifted Av(312,4321)
permutation followed by 1.  There are exactly 4181 at length 11.  Verify that
the supplied certificate has that many distinct valid tuples, then validate
every exclusion witness and every accepted square with generic rank patterns.
"""
import hashlib
import json
from collections import Counter
from itertools import combinations
from pathlib import Path


def pattern(values):
    ranks = {v: i + 1 for i, v in enumerate(sorted(values))}
    return tuple(ranks[v] for v in values)


def contains(p, sigma):
    return any(pattern(values) == sigma for values in combinations(p, len(sigma)))


def main():
    certificate_path = Path('evidence/endpoint_classical_n11.json')
    census_path = Path('evidence/endpoint_exhaustive.json')
    certificate = json.loads(certificate_path.read_text())
    census = json.loads(census_path.read_text())
    # f[h][m] counts Av_m(312, (h+1)...1), proved by the position of 1.
    f = [[1] + [0] * 10 for _ in range(4)]
    for h in range(1, 4):
        for m in range(1, 11):
            f[h][m] = sum(f[h-1][k] * f[h][m-1-k] for k in range(m))
    seen, accepted, square_rows = set(), [], []
    first_counts, good_first_counts = Counter(), Counter()
    for row in certificate:
        p = tuple(row['permutation'])
        assert sorted(p) == list(range(1, 12)) and p[-1] == 1
        assert p not in seen
        seen.add(p)
        assert not contains(p, (3, 1, 2))
        assert not contains(p, (5, 4, 3, 2, 1))
        first_counts[p[0]] += 1
        mapping = dict(enumerate(p, start=1))
        q = tuple(mapping[mapping[i]] for i in range(1, 12))
        assert q == tuple(row['square'])
        indices = row['square_132_indices']
        if indices is None:
            assert not contains(q, (1, 3, 2))
            accepted.append(p)
            square_rows.append({'permutation': p, 'square': q})
            good_first_counts[p[0]] += 1
        else:
            assert len(indices) == 3 and 1 <= indices[0] < indices[1] < indices[2] <= 11
            assert pattern(tuple(q[i - 1] for i in indices)) == (1, 3, 2)
    assert len(seen) == f[3][10]
    assert sorted(accepted) == sorted(map(tuple, census['members']['11']))
    b = [0] + [len(census['members'][str(n)]) for n in range(1, 12)]
    assert b[-1] == len(accepted) == 9
    for n, row in enumerate(census['rows'], start=1):
        assert row['n'] == n and row['b_n'] == b[n]
        assert row['prefix_avoids_312_4321'] == f[3][n-1]
    t, a = [1], [1]
    for n in range(1, 12):
        t.append(sum(t[n-j] for j in range(1, min(n, 4) + 1)))
        a.append(sum(b[k] * t[n-k] for k in range(1, n+1)))
    assert a[:6] == [1, 1, 2, 5, 11, 22]
    recurrence_rows = []
    for n in range(6, 12):
        rhs = sum(a[n-j] for j in range(1, 5)) + n - 1
        recurrence_rows.append({'n': n, 'actual': a[n], 'rhs': rhs,
                                'difference': a[n] - rhs})
    assert [r['n'] for r in recurrence_rows if r['difference']] == [11]
    compared = []
    for name in ['triage_counts.json', 'insertion_counts.json']:
        data = json.loads((Path('evidence') / name).read_text())
        assert [r['a_n'] for r in data['rows'][:12]] == a
        compared.append(name)
    source_hash = hashlib.sha256(Path('source.md').read_bytes()).hexdigest()
    assert source_hash == '51c5a2d559d1c8a858630d9de8afe0fb10e5b862ee0f2f5b544c8d7868fe9a75'
    out = {'job_id': 'newwin-00001-p06-research-8a0fdffcb5e5',
           'scope': 'Deterministic same-worker certificate check; no fresh referee',
           'scalar_class_counts_h3_n0_to_10': f[3],
           'distinct_classical_endpoints_checked': len(seen),
           'square_exclusion_witnesses_checked': len(seen) - len(accepted),
           'accepted_endpoints': square_rows,
           'classical_counts_by_first_entry': dict(sorted(first_counts.items())),
           'accepted_counts_by_first_entry': dict(sorted(good_first_counts.items())),
           'b_n0_to_11': b, 't_n0_to_11': t, 'a_n0_to_11': a,
           'recurrence_checks': recurrence_rows,
           'counts_match_archived_enumerators': compared,
           'source_sha256': source_hash,
           'input_sha256': {str(p): hashlib.sha256(p.read_bytes()).hexdigest()
                            for p in [certificate_path, census_path, Path(__file__)]}}
    path = Path('evidence/endpoint_certificate_verification.json')
    tmp = path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(out, indent=2) + '\n')
    tmp.replace(path)
    print(json.dumps({k: v for k, v in out.items()
                      if k not in ['input_sha256', 'accepted_endpoints']}))


if __name__ == '__main__':
    main()
