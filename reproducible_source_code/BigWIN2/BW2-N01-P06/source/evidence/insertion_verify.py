"""Independent enumeration by inserting the maximum; no min decomposition.

Deleting the maximum preserves classical pattern avoidance. Therefore inserting
n in every position of every Av_(n-1)(312,54321) member, then filtering, produces
the entire Av_n(312,54321), uniquely. Square avoidance is tested only afterwards;
no unjustified hereditary assumption about square avoidance is used.
"""
from pathlib import Path
import hashlib
import json


def has312(p):
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                for k in range(j + 1, len(p)):
                    if p[i] > p[k] > p[j]:
                        return True
    return False


def has54321(p):
    n = len(p)
    for a in range(n):
        for b in range(a + 1, n):
            if p[a] <= p[b]: continue
            for c in range(b + 1, n):
                if p[b] <= p[c]: continue
                for d in range(c + 1, n):
                    if p[c] <= p[d]: continue
                    for e in range(d + 1, n):
                        if p[d] > p[e]: return True
    return False


def valid_square(p):
    q = [p[p[i] - 1] for i in range(len(p))]
    for i in range(len(q)):
        for j in range(i + 1, len(q)):
            for k in range(j + 1, len(q)):
                if q[i] < q[k] < q[j]:
                    return False
    return True


pool = [()]
rows = []
for n in range(12):
    if n:
        next_pool = []
        for p in pool:
            for pos in range(n):
                q = p[:pos] + (n,) + p[pos:]
                if not has312(q) and not has54321(q):
                    next_pool.append(q)
        pool = next_pool
    assert len(pool) == len(set(pool))
    good = sorted(p for p in pool if valid_square(p))
    row = {"n": n, "avoid312_54321": len(pool), "a_n": len(good),
           "b_n_ending_in_1": sum(bool(p) and p[-1] == 1 for p in good)}
    rows.append(row)
    print(json.dumps(row), flush=True)
    if n == 11:
        Path('evidence/insertion_members_n11.json').write_text(json.dumps(good) + '\n')
out = {"job_id": "newwin-00001-p06-triage-aaf5e6140737",
       "method": "maximum insertion, direct subsequence tests",
       "scope": "exact finite enumeration through n=11; no fresh referee",
       "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       "rows": rows}
Path('evidence/insertion_counts.json').write_text(json.dumps(out, indent=2) + '\n')
