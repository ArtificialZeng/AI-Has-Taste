"""Independent endpoint census over every (n-1)! tuple, using only the stdlib.

Run from PROJECT_DIR: python3 evidence/endpoint_exhaustive.py
No recursive avoider generator or conjectured recurrence is used.  Appending 1
cannot create 312, and a length-five descent after appending 1 exists iff the
prefix contains a length-four descent.  All endpoint tuples for 1 <= n <= 11
are tested.  This is a finite certificate, not an infinite enumeration formula.
"""
import hashlib
import json
import math
from itertools import combinations, permutations
from pathlib import Path


def has312(p):
    for i, j, k in combinations(range(len(p)), 3):
        if p[i] > p[k] > p[j]:
            return True
    return False


def has4321(p):
    return any(p[i] > p[j] > p[k] > p[l]
               for i, j, k, l in combinations(range(len(p)), 4))


def first132(p):
    return next(((i + 1, j + 1, k + 1)
                 for i, j, k in combinations(range(len(p)), 3)
                 if p[i] < p[k] < p[j]), None)


def main():
    rows, members, classical_n11 = [], {}, []
    for n in range(1, 12):
        tested, no312, classical, good = 0, 0, 0, []
        for prefix in permutations(range(2, n + 1)):
            tested += 1
            if has312(prefix):
                continue
            no312 += 1
            if has4321(prefix):
                continue
            classical += 1
            p = prefix + (1,)
            q = tuple(p[p[i] - 1] for i in range(n))
            witness = first132(q)
            if witness is None:
                good.append(p)
            if n == 11:
                classical_n11.append({"permutation": p, "square": q,
                                      "square_132_indices": witness})
        assert tested == math.factorial(n - 1)
        members[str(n)] = good
        row = {"n": n, "tuples_tested": tested, "prefix_avoids_312": no312,
               "prefix_avoids_312_4321": classical, "b_n": len(good)}
        rows.append(row)
        print(json.dumps(row), flush=True)
    previous = json.loads(Path('evidence/triage_counts.json').read_text())
    for row in rows:
        n = row['n']
        assert sorted(members[str(n)]) == sorted(map(tuple, previous['endpoint_permutations'][str(n)]))
    insertion = json.loads(Path('evidence/insertion_members_n11.json').read_text())
    assert members['11'] == sorted(tuple(p) for p in insertion if p[-1] == 1)
    out = {"job_id": "newwin-00001-p06-research-8a0fdffcb5e5",
           "scope": "Exact complete endpoint census for 1 <= n <= 11",
           "method": "All (n-1)! permutations, direct index tests",
           "source_sha256": hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "rows": rows, "members": members,
           "matches_previous_endpoint_lists_through": 11,
           "matches_insertion_members_at": 11}
    for name, data in [('endpoint_exhaustive.json', out),
                       ('endpoint_classical_n11.json', classical_n11)]:
        path = Path('evidence') / name
        tmp = path.with_suffix('.json.tmp')
        tmp.write_text(json.dumps(data, indent=2) + '\n')
        tmp.replace(path)


if __name__ == '__main__':
    main()
