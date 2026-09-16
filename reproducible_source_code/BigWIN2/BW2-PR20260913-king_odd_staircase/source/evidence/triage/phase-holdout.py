#!/usr/bin/env python3
"""Frozen two-phase boundary ansatz, checked on new block sizes."""
from pathlib import Path
import hashlib
import json
import runpy


def predicted(r, k):
    assert r > 0 and r % 2 and k > 0
    p = r + 2
    t = (k - 1) % p + 1
    h = ((k - 1) // p) % 2
    a, b = 3 - h, 2 + h
    result = []
    for j in range(r):
        if j == 0 and t == p:
            result.append(2)
        elif j < p - t:
            result.append((t + 1) % 2 if j % 2 == 0 else a)
        else:
            result.append(b if j % 2 == 0 else t % 2)
    return tuple(result)


def main():
    base = runpy.run_path(str(Path(__file__).with_name('boundary-test.py')))
    rows = []
    for r in (33, 35, 47, 63):
        end = 4 * (r + 2) + 2
        actual = base['words'](r, end)
        mismatches = [k for k in range(1, end + 1) if actual[k] != predicted(r, k)]
        # Direct full-board checks at a start, a phase wrap and a double wrap.
        direct = []
        for k in (1, 2, r + 2, 2 * (r + 2) + 1):
            # Recursive full-board evaluation is deliberately not used at this size.
            if r == 33:
                value = tuple(base['board'](base['shape'](r, k))[0][:r])
                assert value == predicted(r, k)
                direct.append(k)
        rows.append({'r': r, 'k_range': [1, end], 'word_mismatches': mismatches,
                     'direct_full_board_k': direct})
    result = {'job_id': 'primary-20260913-king-odd-staircase-triage-76eec04b3033',
              'frozen_formula': 'predicted() in this script, fixed before this run',
              'discovery_block_sizes': list(range(1, 32, 2)),
              'holdout': rows, 'arithmetic': 'exact integer mex; no randomness',
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'qualification': 'Finite falsification test of an unproved uniform boundary formula; no independent referee.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
