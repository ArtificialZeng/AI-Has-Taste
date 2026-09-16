#!/usr/bin/env python3
"""Direct all-submatrices verifier, deliberately distinct from row intersections."""
import csv
import itertools
import sys

path = sys.argv[1]
with open(path, newline="", encoding="utf-8") as handle:
    a = [[int(x) for x in row] for row in csv.reader(handle)]
assert len(a) == 13 and all(len(row) == 23 for row in a)
assert all(x in (0, 1) for row in a for x in row)
assert sum(map(sum, a)) == 140
checked = 0
for rs in itertools.combinations(range(13), 3):
    for cs in itertools.combinations(range(23), 3):
        checked += 1
        assert not all(a[r][c] for r in rs for c in cs), (rs, cs)
print(f"PASS edges=140 candidate_submatrices={checked}")
