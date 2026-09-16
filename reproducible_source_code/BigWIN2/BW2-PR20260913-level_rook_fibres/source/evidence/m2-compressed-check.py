"""Deterministic cross-checks of the compressed counter; run at project root.

Run: python3 evidence/m2-compressed-check.py > evidence/m2-compressed-check.json
Finite tests are evidence about this implementation, not a proof or referee.
"""
import hashlib
import importlib.util
import itertools
import json
import platform
import random
import sys
import time
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


fast = load('compressed', 'evidence/m2-compressed.py')
baseline = load('baseline', 'evidence/m2-path-check.py')


def brute(a):
    if not a:
        return 1
    upper = [a[0]] + [min(a[i - 1], a[i]) for i in range(1, len(a))]
    return sum(all(x[i] + x[i + 1] <= a[i] for i in range(len(a) - 1))
               for x in itertools.product(*(range(u + 1) for u in upper)))


def small_test():
    count = brute_count = 0
    most_pieces = {'piece_count': 0}
    for length, maximum in [(i, 4) for i in range(7)] + [(7, 3)]:
        for a in itertools.product(range(maximum + 1), repeat=length):
            got, trace = fast.compressed_count(a, return_trace=True)
            want = baseline.path_count(a)
            assert got == want, (a, got, want)
            if a:
                # Every nonnegative capacity vector occurs for some C.
                s = [0] * length
                s[-1] = 2 * a[-1] + 1
                for i in range(length - 2, -1, -1):
                    s[i] = 2 * (a[i] + (s[i + 1] + 1) // 2)
                c = tuple(reversed(s))
                assert baseline.capacities(c) == a
                assert fast.fibre_count(c) == got
            if length <= 5 and maximum == 4:
                assert got == brute(a), a
                brute_count += 1
            count += 1
            for row in trace:
                if row['piece_count'] > most_pieces['piece_count']:
                    most_pieces = {'capacities': a, **row}
    return {'cases': count, 'brute_force_cases': brute_count,
            'ranges': 'all a in {0,...,4}^t for 0<=t<=6, plus {0,...,3}^7',
            'largest_observed_piece_count': most_pieces}


def census_test():
    boards = fibres = 0
    for n in range(21):
        groups = defaultdict(int)
        for b in baseline.partitions(n):
            groups[baseline.image(b)] += 1
            boards += 1
        for c, count in groups.items():
            assert fast.fibre_count(c) == count, (c, count)
            fibres += 1
    assert fast.fibre_count((2, 4)) == 3
    for bad in [(1, 1), (3, 3), (4, 2), (0,)]:
        try:
            fast.fibre_count(bad)
        except ValueError:
            pass
        else:
            raise AssertionError(('invalid input accepted', bad))
    return {'area_range': [0, 20], 'boards': boards, 'fibres': fibres}


def scaled_test():
    large_pairs = [(0, 10**100), (10**100, 0),
                   (10**100 + 7, 10**100 - 9),
                   (10**150, 10**160), (2**1024, 2**1023)]
    for a, b in large_pairs:
        q = min(a, b)
        want = (q + 1) * (a + 1) - q * (q + 1) // 2
        assert fast.compressed_count((a, b)) == want
    # Uniform-capacity Ehrhart polynomial interpolation is a separate
    # large-value check: the path matrix is totally unimodular. The
    # written proof identifies why this interpolation applies.
    interpolated = []
    for t in range(1, 10):
        values = [baseline.path_count((a,) * t) for a in range(t + 1)]
        def lagrange(x):
            # Separate rational Lagrange formula; does not reuse any
            # binomial evaluation or finite-difference code under test.
            result = Fraction(0)
            for j, value in enumerate(values):
                term = Fraction(value)
                for k in range(t + 1):
                    if j != k:
                        term *= Fraction(x - k, j - k)
                result += term
            assert result.denominator == 1
            return result.numerator
        assert lagrange(t + 1) == baseline.path_count((t + 1,) * t)
        a = 10**80 + 17
        got, trace = fast.compressed_count((a,) * t, return_trace=True)
        assert got == lagrange(a), t
        interpolated.append({'t': t, 'answer_bits': got.bit_length(),
                             'max_pieces': max(r['piece_count'] for r in trace)})
    # Deterministic, recorded seed. Long uneven inputs are checked by the
    # independent numeric DP when capacities stay moderate.
    rng = random.Random(20260913)
    for case in range(160):
        a = tuple(rng.randrange(301) for _ in range(rng.randrange(1, 61)))
        assert fast.compressed_count(a) == baseline.path_count(a), (case, a)
    # Stress cases with no capacity-sized oracle: report, do not label an
    # independent verification. These exercise the proven internal bounds.
    stress = []
    for name, a in [
        ('uniform', (10**100,) * 80),
        ('inhomogeneous', tuple(10**100 + rng.randrange(10**90) for _ in range(80))),
        ('alternating_scale', tuple(10**100 if i % 2 else 10**30 for i in range(80))),
        ('zero_capacities', tuple(0 if i % 9 == 0 else 10**100 + i for i in range(80)))
    ]:
        started = time.monotonic()
        answer, trace = fast.compressed_count(a, return_trace=True)
        stress.append({'name': name, 'capacities': a, 't': len(a),
                       'elapsed_seconds': round(time.monotonic() - started, 4),
                       'answer_bits': answer.bit_length(),
                       'answer_binary_sha256': hashlib.sha256(answer.to_bytes(
                           (answer.bit_length() + 7) // 8, 'big')).hexdigest(),
                       'max_pieces': max(r['piece_count'] for r in trace),
                       'max_coefficient_bits': max(r['max_coefficient_bits'] for r in trace),
                       'scope': 'stress run; internal bounds only, no independent oracle'})
    return {'large_t2_formula_cases': len(large_pairs),
            'uniform_ehrhart_checks': interpolated,
            'inhomogeneous_numeric_comparisons': 160,
            'random_seed': 20260913, 'stress': stress}


def main():
    start = time.monotonic()
    result = {'job_id': 'primary-20260913-level-rook-fibres-research-4655afa47dc0',
              'python': platform.python_version(),
              'scope': 'exact finite verification; no mathematical acceptance or priority certification',
              'small': small_test(), 'census': census_test(), 'scaling': scaled_test(),
              'all_checks_passed': True,
              'elapsed_seconds': round(time.monotonic() - start, 3),
              'source_sha256': hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
              'implementation_sha256': hashlib.sha256(Path('evidence/m2-compressed.py').read_bytes()).hexdigest()}
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
