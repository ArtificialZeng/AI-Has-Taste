#!/usr/bin/env python3
"""Exact complete term-function DP, independently checked by raw trees to n=7.

Run from PROJECT_DIR: python3 evidence/exact_spectrum.py --max-n 10
Only full uint8 truth-table bytes decide function equality; no fingerprints do.
"""
import argparse
import hashlib
import json
from functools import lru_cache
from itertools import product
from math import comb
from pathlib import Path
import time
import numpy as np

TABLE = ((0, 0, 0), (1, 1, 0), (1, 0, 1))
OP = np.array(TABLE, dtype=np.uint8)


@lru_cache(None)
def trees(n, start=0):
    if n == 1:
        return (start,)
    return tuple((l, r) for k in range(1, n)
                 for l in trees(k, start) for r in trees(n-k, start+k))


def evaluate(t, assignment):
    if isinstance(t, int):
        return assignment[t]
    return TABLE[evaluate(t[0], assignment)][evaluate(t[1], assignment)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, default=10)
    args = parser.parse_args()
    started = time.monotonic()
    functions = {1: {bytes((0, 1, 2))}}
    rows = []
    counts = [0]
    for n in range(1, args.max_n + 1):
        combinations = 0
        if n >= 2:
            current = set()
            for k in range(1, n):
                for left in functions[k]:
                    lv = np.frombuffer(left, dtype=np.uint8)
                    for right in functions[n-k]:
                        rv = np.frombuffer(right, dtype=np.uint8)
                        current.add(OP[lv[:, None], rv[None, :]].tobytes())
                        combinations += 1
            functions[n] = current
        counts.append(len(functions[n]))
        row = {'n': n, 'distinct_functions': counts[n],
               'assignments_per_function': 3**n,
               'root_function_pairs_checked': combinations,
               'catalan_bracketings_covered': comb(2*n-2, n-1)//n,
               'sorted_full_tables_sha256': hashlib.sha256(
                   b''.join(sorted(functions[n]))).hexdigest()}
        if n >= 4:
            row['recurrence_prediction'] = 3*counts[n-1]-2*counts[n-2]+counts[n-3]
            row['recurrence_matches'] = row['recurrence_prediction'] == counts[n]
        if n <= 7:
            assignments = tuple(product(range(3), repeat=n))
            raw_trees = trees(n)
            raw = {bytes(evaluate(t, x) for x in assignments) for t in raw_trees}
            assert len(raw_trees) == row['catalan_bracketings_covered']
            assert raw == functions[n]
            row['raw_tree_scalar_crosscheck'] = 'full set equality'
        rows.append(row)
        result = {'job_id': 'newwin-00001-p02-triage-ba81b5c3d443',
                  'arithmetic': 'exact uint8 table lookup',
                  'equality': 'complete bytes; Python set resolves hash collisions by equality',
                  'tuple_order': 'lexicographic, last coordinate fastest',
                  'rows': rows, 'elapsed_seconds': time.monotonic()-started,
                  'status': 'exact finite observation, not an all-n proof'}
        target = Path('evidence/exact-spectrum.json')
        temp = target.with_suffix('.json.tmp')
        temp.write_text(json.dumps(result, indent=2)+'\n')
        temp.replace(target)
        print(json.dumps(row), flush=True)


if __name__ == '__main__':
    main()
