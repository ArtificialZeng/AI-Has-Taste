#!/usr/bin/env python3
"""Exact triage tests of the proposed square transfer; no universal certificate."""
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import platform

MOVES = ((0, 1), (1, 0), (1, 1))


def shape(r, k):
    return tuple(r * t for t in range(k, 0, -1) for _ in range(r))


def cut(parts, i, j):
    return tuple(a - j for a in parts[i:] if a > j)


def mex(values):
    a = 0
    while a in values:
        a += 1
    return a


@lru_cache(None)
def recursive(parts):
    assert parts
    successors = (cut(parts, i, j) for i, j in MOVES)
    return mex({recursive(p) for p in successors if p})


def board(parts):
    """Full cell table, computed separately with bit masks."""
    table = [[0] * n for n in parts]
    for i in range(len(parts) - 1, -1, -1):
        for j in range(parts[i] - 1, -1, -1):
            mask = 0
            for di, dj in MOVES:
                a, b = i + di, j + dj
                if a < len(parts) and b < parts[a]:
                    mask |= 1 << table[a][b]
            table[i][j] = next(v for v in range(4) if not (mask >> v) & 1)
    return table


def transfer(r, previous=None, diagonal=None):
    """None means an absent cell, never an SG value of an empty board."""
    square = [[None] * (r + 1) for _ in range(r + 1)]
    if previous is not None:
        for j in range(r):
            square[r][j] = square[j][r] = previous[j]
    square[r][r] = diagonal
    for i in range(r - 1, -1, -1):
        for j in range(r - 1, -1, -1):
            values = {square[i + di][j + dj] for di, dj in MOVES}
            values.discard(None)
            square[i][j] = mex(values)
    return tuple(square[0][:r])


def words(r, end):
    result = [None, transfer(r)]
    for k in range(2, end + 1):
        result.append(transfer(r, result[k - 1],
                               None if k == 2 else result[k - 2][0]))
    return result


def main():
    counts = {'coordinate_identities': 0, 'full_board_boundary_comparisons': 0,
              'recursive_subpartition_comparisons': 0}
    for r in range(1, 10):
        w = words(r, 12)
        for k in range(1, 13):
            p = shape(r, k)
            if k >= 2:
                assert cut(p, r, 0) == cut(p, 0, r) == shape(r, k - 1)
                assert cut(p, r, r) == (() if k == 2 else shape(r, k - 2))
            else:
                assert cut(p, r, 0) == cut(p, 0, r) == cut(p, r, r) == ()
            counts['coordinate_identities'] += 1
            assert w[k] == tuple(board(p)[0][:r])
            counts['full_board_boundary_comparisons'] += 1
            if r <= 5 and k <= 6:
                for j in range(r):
                    assert w[k][j] == recursive(cut(p, 0, j))
                    counts['recursive_subpartition_comparisons'] += 1
    observations = []
    for r in range(1, 32, 2):
        period = r + 2
        w = words(r, 3 * period + 1)
        root_failures = []
        word_failures = []
        state_failures = []
        for k in range(1, 2 * period + 2):
            if w[k] != w[k + period]:
                word_failures.append(k)
            if k >= 2 and (w[k], w[k - 1][0]) != (w[k + period], w[k + period - 1][0]):
                state_failures.append(k)
        for k in range(1, len(w)):
            q = k % period
            expected = 2 if q == 0 else (0 if q % 2 else 1)
            if w[k][0] != expected:
                root_failures.append(k)
        observations.append({'r': r, 'k_max': len(w) - 1, 'period_tested': period,
                             'root_formula_failures': root_failures,
                             'word_period_failures_k': word_failures,
                             'state_period_failures_k': state_failures,
                             'initial_words': [list(v) for v in w[1:period + 3]]})
    result = {'job_id': 'primary-20260913-king-odd-staircase-triage-76eec04b3033',
              'python': platform.python_version(), 'arithmetic': 'exact integer mex',
              'randomness': 'none', 'checks': counts, 'observations': observations,
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'qualification': 'Finite observations only; uniform closure for every odd r is unproved.'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(counts))
    for x in observations:
        print(json.dumps({k: v for k, v in x.items() if k != 'initial_words'}))
    for x in observations[:4]:
        print('WORDS', x['r'], x['initial_words'])


if __name__ == '__main__':
    main()
