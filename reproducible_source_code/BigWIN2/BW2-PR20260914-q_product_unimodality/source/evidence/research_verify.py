"""Exact finite checks for the proposed k=2 theorem; not its universal proof.

Run from the project root:
    python3 evidence/research_verify.py > evidence/research-verification.json

Uses no triage imports. Dense coefficients come from two sliding-window
convolutions of a sparse geometric series. A second coefficient evaluator
uses the rational generating function and inclusion-exclusion.
"""
from collections import Counter
from itertools import combinations_with_replacement, product
from pathlib import Path
import hashlib
import json
import platform

JOB = 'primary-20260914-q-product-unimodality-research-ba86ac9fff54'


def multiply_box(poly, length):
    result = []
    running = 0
    for n in range(len(poly) + length - 1):
        if n < len(poly):
            running += poly[n]
        if 0 <= n - length < len(poly):
            running -= poly[n - length]
        result.append(running)
    return result


def coefficients(a, c, b, r):
    sparse = [0] * (r * (b - 1) + 1)
    for j in range(b):
        sparse[r * j] = 1
    return multiply_box(multiply_box(sparse, a), c)


def geometric_ramp(n, r):
    if n < 0:
        return 0
    h = n // r
    return (h + 1) * (n + 1) - r * h * (h + 1) // 2


def coefficient_closed(n, a, c, b, r):
    # (1-q^a)(1-q^c)(1-q^(rb)) / ((1-q)^2(1-q^r)).
    total = 0
    for x, y, z in product((0, 1), repeat=3):
        total += (-1)**(x+y+z) * geometric_ramp(n-x*a-y*c-z*r*b, r)
    return total


def count_multiples(lo, hi, r, b):
    lower = max(0, (lo + r - 1) // r)
    upper = min(b - 1, hi // r)
    return max(0, upper - lower + 1)


def interval_difference(n, a, c, b, r):
    return (count_multiples(n-a+1, n, r, b)
            - count_multiples(n-a-c+1, n-c, r, b))


stats = Counter()
branches = Counter()
signature = hashlib.sha256()


def check_floor_step(n, a, c, b, r):
    A, s = divmod(a, r)
    C, t = divmod(c, r)
    M, B = A+C, b-1
    D = a+c-2+r*B
    assert 1 <= s < r and 1 <= t < r
    assert 0 <= B <= M and c <= n <= D//2
    h, v = divmod(n, r)
    e = int(v < s) + int(v < t)
    F = (n-a)//r + (n-c)//r + 1
    assert n <= a+c-2 and 0 <= n-c < r*B
    assert F == 2*h-M+1-e
    assert F <= (2*n-a-c)//r + 1 <= B
    assert h <= M
    if h == M:
        assert 2*v <= s+t-2 and e >= 1
    assert F <= h
    assert interval_difference(n, a, c, b, r) >= 0
    branches[f'e={e},h={"M" if h == M else "<M"}'] += 1
    stats['floor_step_checks'] += 1


def check_dense(a, c, b, r, family):
    p = coefficients(a, c, b, r)
    D = a+c-2+r*(b-1)
    assert len(p) == D+1 and p == p[::-1]
    expected = (a % r == 0 or c % r == 0 or b <= 1+a//r+c//r)
    observed = all(p[n] >= p[n-1] for n in range(1, D//2+1))
    assert expected == observed, (a, c, b, r, p)
    stats[family + '_tuples'] += 1
    stats['unimodal_tuples' if observed else 'nonunimodal_tuples'] += 1
    signature.update(json.dumps([a,c,b,r,p], separators=(',', ':')).encode())

    for n in range(D+2):
        left = p[n] if n <= D else 0
        right = p[n-1] if n >= 1 else 0
        assert left-right == interval_difference(n, a, c, b, r)
        stats['dense_difference_checks'] += 1

    # A structurally different exact coefficient formula, calibrated at
    # endpoints, midpoint, and each side of the first negative witness.
    indices = {0, 1, D//2, max(0,D//2-1), D, D+1}
    if a % r and c % r:
        M = a//r+c//r
        if b > M+1:
            nstar = r*M+max(a % r, c % r)
            assert 1 <= nstar <= D//2
            assert p[nstar]-p[nstar-1] == -1
            indices.update((nstar-1, nstar))
            stats['dense_negative_witnesses'] += 1
        else:
            for n in range(c, D//2+1):
                check_floor_step(n, a, c, b, r)
    for n in sorted(indices):
        expected_coefficient = p[n] if n <= D else 0
        assert coefficient_closed(n, a, c, b, r) == expected_coefficient
        stats['closed_formula_dense_comparisons'] += 1


# Complete finite rectangular domain, including divisibility and factor 1.
for r in range(2, 12):
    for a, c in combinations_with_replacement(range(1, 19), 2):
        for b in range(1, 11):
            check_dense(a, c, b, r, 'small_grid')

# Chosen after the proof was written: larger prime and composite stretches,
# residue endpoints, middle residues, divisibility, and threshold +/- cases.
for r in (13, 17, 31, 64, 97):
    residues = sorted({1, 2, r//2, r-1})
    values = sorted({r, 2*r} | {r*A+s for A in (0,1,3) for s in residues})
    for a, c in combinations_with_replacement(values, 2):
        M = a//r+c//r
        for b in sorted({1, max(1,M), M+1, M+2, M+5}):
            check_dense(a, c, b, r, 'held_out')


large_examples = []
for r in (2, 3, 5, 17, 97, 1000000007):
    residues = sorted({s for s in (1,2,r//2,r-1) if 1 <= s < r})
    for A, C in ((0,0),(0,10**6),(1,10**6),(10**6,10**6),(10**30,10**30+1)):
        for s, t in product(residues, repeat=2):
            a, c = sorted((r*A+s, r*C+t))
            AA, ss = divmod(a, r)
            CC, tt = divmod(c, r)
            M = AA+CC
            for B in sorted({0, max(0,M-1), M}):
                D = a+c-2+r*B
                half = D//2
                indices = {c, c+1, half, half-1}
                for h in (c//r, half//r, half//r-1, M-1, M):
                    for v in {0, ss-1, ss, tt-1, tt, r-1}:
                        indices.add(r*h+v)
                for n in sorted(indices):
                    if c <= n <= half:
                        check_floor_step(n, a, c, B+1, r)
                        assert (coefficient_closed(n,a,c,B+1,r)
                                - coefficient_closed(n-1,a,c,B+1,r)
                                == interval_difference(n,a,c,B+1,r))
                        stats['large_integer_sufficient_indices'] += 1
            for B in (M+1, M+2, M+10**10):
                nstar = r*M+max(ss,tt)
                D = a+c-2+r*B
                before = coefficient_closed(nstar-1,a,c,B+1,r)
                after = coefficient_closed(nstar,a,c,B+1,r)
                assert 1 <= nstar <= D//2 and after-before == -1
                assert interval_difference(nstar,a,c,B+1,r) == -1
                stats['large_integer_negative_witnesses'] += 1
                if r == 1000000007 and AA == 10**30 and ss == 1 and tt == r-1 and B == M+1:
                    large_examples.append(dict(r=r,a=a,c=c,b=B+1,D=D,
                                               nstar=nstar,before=before,after=after))

report = {
    'job_id': JOB,
    'arithmetic': 'exact Python integers; no floating point',
    'python': platform.python_version(),
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'proof_file': 'evidence/k2-characterization.md',
    'domains': {
        'small_grid': 'All r=2..11, 1<=a<=c<=18, b=1..10.',
        'held_out': 'r in {13,17,31,64,97}; a<=c from {r,2r} union {rA+s:A in {0,1,3},s in distinct {1,2,floor(r/2),r-1}}; b in distinct {1,max(1,M),M+1,M+2,M+5}, M=floor(a/r)+floor(c/r). All dense coefficients are checked.',
        'large_integer': 'r in {2,3,5,17,97,1000000007}; ordered quotient pairs (0,0),(0,10^6),(1,10^6),(10^6,10^6),(10^30,10^30+1); all residue pairs from distinct valid {1,2,floor(r/2),r-1}; then sort a,c. B in distinct {0,max(0,M-1),M} for the finite index selection in this script; B in {M+1,M+2,M+10^10} for negative witnesses. No dense enumeration in this large domain.'
    },
    'counts': dict(sorted(stats.items())),
    'floor_case_coverage': dict(sorted(branches.items())),
    'dense_coefficients_signature_sha256': signature.hexdigest(),
    'large_exact_examples': large_examples,
    'failures': [],
    'limitations': 'Only the specified finite domains are checked. Dense convolution is independent of the interval expression, but all code and proof were prepared in the same research context. These computations are neither a universal proof, a fresh referee report, nor a novelty certificate.'
}
print(json.dumps(report, indent=2))
