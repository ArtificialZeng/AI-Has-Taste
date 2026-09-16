"""Exact triage test: column-partition census versus m=2 path constraints.

Run: python3 evidence/m2-path-check.py > evidence/m2-path-check.json
No external packages, randomness, or floating point. This finite check does
not certify an unrestricted theorem or novelty.
"""
from collections import defaultdict
from itertools import accumulate
import hashlib
import json
import platform
from pathlib import Path


def partitions(n, lo=1):
    if n == 0:
        yield ()
    for x in range(lo, n + 1):
        for tail in partitions(n - x, x):
            yield (x,) + tail


def image(board):
    if not board:
        return ()
    return tuple(reversed([
        sum(min(2, max(0, h - 2 * p)) for h in board)
        for p in range((board[-1] + 1) // 2)
    ]))


def capacities(c):
    s = tuple(reversed(c)) + (0,)
    return tuple(s[i] // 2 - (s[i + 1] + 1) // 2
                 for i in range(len(c)))


def path_count(a):
    if not a:
        return 1
    if min(a) < 0:
        return 0
    u = [a[0]] + [min(a[i - 1], a[i]) for i in range(1, len(a))]
    values = [1] * (u[0] + 1)
    for i in range(1, len(a)):
        prefix = list(accumulate(values))
        values = [prefix[min(u[i - 1], a[i - 1] - y)]
                  if a[i - 1] >= y else 0 for y in range(u[i] + 1)]
    return sum(values)


def coordinates(board, c):
    rows = [sum(h >= r for h in board) for r in range(1, 2 * len(c) + 1)]
    s = tuple(reversed(c))
    return tuple(s[i] // 2 - rows[2 * i + 1] for i in range(len(c)))


def inverse(d, c):
    rows = []
    for s, x in zip(reversed(c), d):
        rows.extend(((s + 1) // 2 + x, s // 2 - x))
    assert all(x >= y for x, y in zip(rows, rows[1:]))
    assert all(x >= 0 for x in rows)
    return tuple(sorted(sum(r >= j for r in rows)
                        for j in range(1, max(rows, default=0) + 1)))


def main():
    cases = []
    total_boards = total_fibres = 0
    for area in range(21):
        groups = defaultdict(list)
        for board in partitions(area):
            groups[image(board)].append(board)
        for c, boards in groups.items():
            a = capacities(c)
            assert path_count(a) == len(boards), (c, a, len(boards))
            encoded = set()
            for board in boards:
                d = coordinates(board, c)
                assert all(x >= 0 for x in d)
                assert all(d[i] + d[i + 1] <= a[i] for i in range(len(a) - 1))
                assert not d or d[-1] <= a[-1]
                assert inverse(d, c) == board
                encoded.add(d)
            assert len(encoded) == len(boards)
        total_boards += sum(map(len, groups.values()))
        total_fibres += len(groups)
        cases.append({'area': area, 'boards': sum(map(len, groups.values())),
                      'fibres': len(groups)})
    control_c = (2, 4)
    control = {'C': control_c, 'capacities': capacities(control_c),
               'path_count': path_count(capacities(control_c)),
               'direct_preimages': [b for b in partitions(6) if image(b) == control_c]}
    # Uniform capacity one gives binary strings without adjacent ones.
    uniform = [path_count((1,) * t) for t in range(1, 13)]
    expected = [2, 3]
    while len(expected) < 12:
        expected.append(sum(expected[-2:]))
    assert uniform == expected
    print(json.dumps({
        'job_id': 'primary-20260913-level-rook-fibres-triage-4e5c62cdde68',
        'python': platform.python_version(), 'm': 2, 'area_range': [0, 20],
        'total_boards': total_boards, 'total_fibres': total_fibres,
        'all_count_and_roundtrip_checks_passed': True,
        'rows': cases, 'negative_control': control,
        'uniform_capacity_one_counts_t_1_to_12': uniform,
        'source_sha256': hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
        'scope': 'Exact finite observation; arbitrary-size proof and novelty not certified'
    }, indent=2))


if __name__ == '__main__':
    main()
