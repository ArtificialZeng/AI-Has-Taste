"""Evaluate the decomposition-tree statistic; None outside the separable class.

Running this file compares it with the inherited exact g2 census through 9.
Those data already informed the sum recurrence: this is a regression check,
not a blind experiment or a proof of the universal statement.
"""
from functools import lru_cache
from itertools import permutations
from collections import Counter
from pathlib import Path
import hashlib
import json
import numpy as np

OUT = Path(__file__).resolve().parent


def decompose(p, skew=False):
    n = len(p)
    cuts = [0]
    extreme = n+1 if skew else 0
    for i, v in enumerate(p, 1):
        extreme = min(extreme, v) if skew else max(extreme, v)
        if extreme == (n+1-i if skew else i):
            cuts.append(i)
    return tuple(tuple(v - (n-b if skew else a) for v in p[a:b])
                 for a, b in zip(cuts, cuts[1:]))


@lru_cache(None)
def tree_statistic(p):
    if len(p) == 1:
        return 0
    for skew in (False, True):
        children = decompose(p, skew)
        if len(children) < 2:
            continue
        values = [tree_statistic(q) for q in children]
        if None in values:
            return None
        marks = [q == tuple(range(1, len(q)+1) if skew else range(len(q), 0, -1))
                 for q in children]
        return sum(values) + sum(a and b for a,b in zip(marks, marks[1:]))
    return None


def main():
    rows = json.loads((OUT/'exact-counts.json').read_text())
    rows += json.loads((OUT/'exact-counts-length8.json').read_text())
    counts9 = np.load(OUT/'exact-counts-length9.npy')
    base9 = (9**4+2*9**3+9**2+4*9+4)//2
    def data():
        yield from ((tuple(r['beta']), r['j']) for r in rows)
        yield from ((p, base9-int(counts9[i])) for i,p in enumerate(permutations(range(1,10))))
    sep, extrema, all_count = Counter(), Counter(), Counter()
    for p, actual in data():
        n=len(p)
        all_count[n]+=1
        got=tree_statistic(p)
        if got is not None:
            assert got == actual, (p, actual, got)
            sep[n]+=1
            extrema[n]+=got==n-1
    report = {'job_id': 'primary-20260912-ray-west-j-research-db44e3159ae7',
              'status': 'Exact finite regression against inherited census, not blind evidence or independent review.',
              'all_patterns_by_length': dict(all_count),
              'separable_patterns_by_length': dict(sep),
              'separable_extremizers_by_length': dict(extrema),
              'separable_patterns_checked': sum(sep.values()),
              'failure_count': 0,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    path=OUT/'separable-statistic-verification.json'
    tmp=path.with_suffix('.json.tmp');tmp.write_text(json.dumps(report,indent=2)+'\n');tmp.replace(path)
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
