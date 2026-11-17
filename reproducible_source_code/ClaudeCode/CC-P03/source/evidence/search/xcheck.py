"""Cross-check transfer.py against brute force: non-conflict pair counts and number of optimal 9-sets."""
import itertools
from transfer import colorable, unit, T
from functools import lru_cache
for q in (3, 5, 7, 9):
    L = [(i, e) for i in range(q) for e in range(12)]
    def col(R):
        d = {}
        for i, e in R: d.setdefault(i, set()).add(e)
        return colorable(q, {i: frozenset(v) for i, v in d.items()})
    assert not col([])
    single = [x for x in L if col([x])]
    nc = sum(1 for a, b in itertools.combinations(L, 2) if not col([a, b]))
    print(f"q={q}: single conflicts {len(single)}, non-conflict pairs {nc}", flush=True)
