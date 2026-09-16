#!/usr/bin/env python3
"""Bounded exact intake calibration, not a proof of universal conjectures."""
import argparse
import json
import platform
import time
from pathlib import Path


def sg(parts, certificate=False):
    below = []
    rows = []
    for width in reversed(parts):
        row = [0] * width
        for j in range(width - 1, -1, -1):
            options = set()
            if j + 1 < width:
                options.add(row[j + 1])
            if j < len(below):
                options.add(below[j])
            if j + 1 < len(below):
                options.add(below[j + 1])
            value = 0
            while value in options:
                value += 1
            row[j] = value
        below = row
        if certificate:
            rows.append(row)
    return (below[0], list(reversed(rows))) if certificate else below[0]


def staircase(r, c, k):
    return [c * step for step in range(k, 0, -1) for _ in range(r)]


def rectangle_formula(r, c):
    if r % 2 == c % 2:
        return 0 if r % 2 else 2
    return 1 if min(r, c) % 2 else 3


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    start = time.perf_counter()
    baseline_counts = {'rectangles_r_c_1_to_14': 0,
                       'ordinary_staircase_k_1_to_30': 0,
                       'equal_even_blocks_r_2_to_12_k_1_to_15': 0}
    for r in range(1, 15):
        for c in range(1, 15):
            assert sg([c] * r) == rectangle_formula(r, c)
            baseline_counts['rectangles_r_c_1_to_14'] += 1
    for k in range(1, 31):
        assert sg(staircase(1, 1, k)) == (k - 1) % 3
        baseline_counts['ordinary_staircase_k_1_to_30'] += 1
    for r in range(2, 13, 2):
        for k in range(1, 16):
            assert sg(staircase(r, r, k)) == (2 if k == 1 else 1)
            baseline_counts['equal_even_blocks_r_2_to_12_k_1_to_15'] += 1
    tests = {'5.1': [], '5.2': []}
    failures = {'5.1': [], '5.2': []}
    for r in range(1, 16, 2):
        for k in range(1, 31):
            rem = k % (r + 2)
            expected = 2 if rem == 0 else (0 if rem % 2 else 1)
            actual = sg(staircase(r, r, k))
            record = {'r': r, 'c': r, 'k': k, 'actual': actual, 'expected': expected}
            tests['5.1'].append(record)
            if actual != expected:
                failures['5.1'].append(record)
    for r in range(2, 13, 2):
        for c in range(2, 13, 2):
            if r == c:
                continue
            for k in range(1, 16):
                expected = 2 if k % 2 else 3
                actual = sg(staircase(r, c, k))
                record = {'r': r, 'c': c, 'k': k, 'actual': actual, 'expected': expected}
                tests['5.2'].append(record)
                if actual != expected:
                    failures['5.2'].append(record)
    witnesses = {}
    for label, cases in failures.items():
        if cases:
            first = min(cases, key=lambda t: (t['r'] * t['c'] * t['k'] * (t['k'] + 1) // 2,
                                             t['r'], t['c'], t['k']))
            parts = staircase(first['r'], first['c'], first['k'])
            value, matrix = sg(parts, certificate=True)
            witnesses[label] = {**first, 'parts': parts, 'sg_cells': matrix,
                                'certificate_root': value,
                                'minimality': 'smallest area among this tested grid only'}
    out = {'schema': 1, 'source': 'arXiv:2501.14640v1 Definitions2.1/3.1 and Conjectures5.1/5.2',
           'python': platform.python_version(), 'arithmetic': 'exact integers and finite mex',
           'moves': [[0, 1], [1, 0], [1, 1]], 'empty_destinations_excluded': True,
           'seed': None, 'randomness': 'none', 'baseline_counts': baseline_counts,
           'tests': tests, 'failure_counts': {k: len(v) for k, v in failures.items()},
           'witnesses': witnesses, 'elapsed_seconds': time.perf_counter() - start,
           'qualification': 'Finite exact observations only. No universal proof, novelty or current open-status certification.'}
    Path(args.out).write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: out[k] for k in ['baseline_counts', 'failure_counts', 'elapsed_seconds']}))
    print(json.dumps({'test_counts': {k: len(v) for k, v in tests.items()},
                      'witness_parameters': {k: {a: v[a] for a in ['r', 'c', 'k', 'actual', 'expected']} for k, v in witnesses.items()}}))


if __name__ == '__main__':
    main()
