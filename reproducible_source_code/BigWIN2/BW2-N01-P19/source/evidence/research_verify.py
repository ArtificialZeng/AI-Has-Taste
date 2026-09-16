#!/usr/bin/env python3
"""Exact arithmetic for the proposed j=2 proof; not a mathematical audit.

Run: python3 evidence/research_verify.py
Writes research-verification.json atomically, with no prior evidence as input.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import gcd, isqrt, lcm
from pathlib import Path
import hashlib
import json
import platform

ROOT = Path(__file__).resolve().parents[1]
JOB = "newwin-00001-p19-research-c7978facb398"


def primes(n):
    return [p for p in range(2, n + 1)
            if all(p % d for d in range(2, isqrt(p) + 1))]


def period(Q):
    return lcm(*(p*q for q in range(3, Q + 1) for p in primes(q - 1)))


def first_residues(Q, b):
    L = period(Q)
    first = [0] * L
    counts = {q: 0 for q in range(3, Q + 1)}
    for q in counts:
        for p in primes(q - 1):
            modulus = p*q
            for a in range((-(q - 1)*b) % modulus, L, modulus):
                if not first[a]:
                    first[a] = q
                    counts[q] += 1
    return first, counts


def class_count(H, a, m):
    """Positive integers <=H in a mod m, for H>=0."""
    assert H >= 0 and 0 <= a < m
    representative = a if a else m
    return (H + m - representative) // m


def crt_intersection(left, right):
    a, m = left
    b, d = right
    g = gcd(m, d)
    if (b - a) % g:
        return None
    h = d // g
    step = (((b - a) // g) * pow(m // g, -1, h)) % h if h > 1 else 0
    modulus = lcm(m, d)
    return ((a + m*step) % modulus, modulus)


def crt_first_events(Q, b):
    """Signed congruence indicators, using union inclusion-exclusion."""
    L = period(Q)
    union = {}
    exclusive = {}
    counts = {}
    previous_count = 0
    for q in range(3, Q + 1):
        before = union.copy()
        for p in primes(q - 1):
            clause = ((-(q - 1)*b) % (p*q), p*q)
            new = defaultdict(int, union)
            new[clause] += 1
            for old, coefficient in union.items():
                intersection = crt_intersection(old, clause)
                if intersection is not None:
                    new[intersection] -= coefficient
            union = {key: val for key, val in new.items() if val}
        difference = defaultdict(int, union)
        for key, val in before.items():
            difference[key] -= val
        exclusive[q] = {key: val for key, val in difference.items() if val}
        current_count = sum(c*(L // m) for (_, m), c in union.items())
        counts[q] = current_count - previous_count
        previous_count = current_count
    return exclusive, counts


def zero_formulas(Q):
    ps = primes(Q)
    densities = {q: F(0) for q in range(3, Q + 1)}
    for ell in ps:
        if ell < 3:
            continue
        prefactor = F(1, ell)
        for a in ps:
            if a < ell:
                prefactor *= F(a - 1, a)
        densities[ell] = prefactor * sum(
            (F(1, p) + F(1, p*p) if p*p < ell else F(1, p - 1)
             for p in ps if p < ell), F(0))
    for p in ps:
        q = p*p
        if q > Q:
            break
        density = F(1, q*(p - 1))
        for a in ps:
            if a < q:
                density *= F(a - 1, a)
        densities[q] = density
    return densities


def avoid_primes(base, excluded):
    """Indicator 1_(base|r) times product(1-1_(p|r))."""
    terms = {base: 1}
    for p in excluded:
        new = defaultdict(int, terms)
        for d, coefficient in terms.items():
            new[lcm(d, p)] -= coefficient
        terms = {d: c for d, c in new.items() if c}
    return terms


def zero_indicator_events(Q):
    """Divisibility inclusion-exclusion, separately from density formulas."""
    ps = primes(Q)
    events = {}
    for q in range(3, Q + 1):
        terms = defaultdict(int)
        if q in ps:
            for p in ps:
                if p >= q:
                    break
                excluded = [a for a in ps if a < q and a != p]
                for d, c in avoid_primes(p*q, excluded).items():
                    terms[d] += c
                if p*p < q:
                    for d, c in avoid_primes(p**3*q, excluded).items():
                        terms[d] -= c
        elif isqrt(q)**2 == q and isqrt(q) in ps:
            p = isqrt(q)
            terms.update(avoid_primes(p**3, [a for a in ps if a < q and a != p]))
        events[q] = {d: c for d, c in terms.items() if c}
    return events


def literal(n):
    first = {n % h for h in range(1, n // 2 + 1)}
    return {n % k for k in first if k}


def truncated(n, Q):
    result = set()
    for q in range(3, Q + 1):
        H = (n - q) // (q + 1)
        if H < 1:
            continue
        for p in primes(q - 1):
            modulus = p*q
            a = (-(q - 1)*n) % modulus
            result.update(range(a if a else modulus, H + 1, modulus))
    return result


# Positive zero-residue representatives and exact floor endpoints.
endpoint_checks = 0
for m in range(1, 41):
    for a in range(m):
        for H in range(2*m + 3):
            actual = sum(r % m == a for r in range(1, H + 1))
            assert class_count(H, a, m) == actual
            assert abs(F(actual) - F(H, m)) <= 1
            endpoint_checks += 1

L, M = period(10), period(50)
assert L == 75600 and M == 691374732709966591241323368000
first10, counts10 = first_residues(10, 1)
crt10, crt_counts10 = crt_first_events(10, 1)
assert counts10 == crt_counts10
assert list(counts10.values()) == [12600, 12600, 6930, 7770, 4110, 3540, 165, 1128]
beta = sum((F(c, L*(q + 1)) for q, c in counts10.items()), F(0))
assert beta == F(1182869, 9979200)

d50 = zero_formulas(50)
events50 = zero_indicator_events(50)
indicator_sizes = {}
for q, terms in events50.items():
    assert all(M % d == 0 for d in terms)
    residue_count = sum(c*(M // d) for d, c in terms.items())
    assert F(residue_count, M) == d50[q], q
    indicator_sizes[q] = len(terms)
C0 = sum((d/(q + 1) for q, d in d50.items()), F(0))
assert C0 == F(6191714756605250456368, 69244275641746488908625)
alpha = C0 + F(1, 52)
delta = beta - alpha
assert alpha == F(30093341768093808664597, 276977102566985955634500)
assert delta == F(131410063319607383019139, 13294900923215325870456000)
assert delta > 0

# Direct full-period tests for zero-class densities at feasible cutoffs.
zero_period_tests = []
for Q in [3, 4, 5, 6, 7, 8, 9, 10]:
    _, counts = first_residues(Q, 0)
    densities = zero_formulas(Q)
    assert all(F(c, period(Q)) == densities[q] for q, c in counts.items())
    zero_period_tests.append({"Q": Q, "period": period(Q)})

# Structured valuation boundaries, including primes outside the cutoff and
# the zero residue represented by M. This is finite falsification evidence.
ps50 = primes(50)
clauses50 = [(q, p*q) for q in range(3, 51) for p in ps50 if p < q]
structured = {M, M - 1, M + 1, 1, 53, 53**3}
for a, b, c, d in product(range(5), range(4), range(4), range(4)):
    core = 2**a * 3**b * 5**c * 7**d
    for extra in [1, 11, 47, 53, 11*47]:
        structured.add(core*extra)
for r in sorted(structured):
    direct = next((q for q, modulus in clauses50 if r % modulus == 0), 51)
    factors = [p for p in ps50 if r % p == 0]
    second = factors[1] if len(factors) >= 2 else 51
    cubes = [p*p for p in ps50 if p*p <= 50 and r % (p**3) == 0]
    classified = min([51, second] + cubes)
    assert direct == classified, (r, direct, classified)

# Exhaustive small-n equality and selected large boundary inputs.
small_limit = 256
targeted_ns = [1023, 1024, 1025, 2015, 2016, 2017, 75599, 75600, 75601, 75602]
cutoff_checks = 0
counting_checks = 0
for n in list(range(1, small_limit + 1)) + targeted_ns:
    actual = literal(n)
    if n <= small_limit:
        full = truncated(n, max(3, (n - 1) // 2))
        assert full == actual - {0}, n
    for Q in [3, 4, 5, 7, 10, 50]:
        truncated_set = truncated(n, Q)
        assert truncated_set <= actual
        assert 0 <= len(actual) - len(truncated_set) <= n // (Q + 2) + 1
        cutoff_checks += 1
        if n <= small_limit and Q <= 7 and n >= Q:
            _, cq = first_residues(Q, n % period(Q))
            coefficient = sum((F(v, period(Q)*(q + 1))
                               for q, v in cq.items()), F(0))
            assert abs(F(len(truncated_set)) - n*coefficient) <= period(Q) + 2
            counting_checks += 1

# Exact finite truncated counts on both progressions, with no giant-period
# scan and no literal large-n remainder computation.
finite_counts = []
for t in [1, 202, 203, 204, 1000, 10**12]:
    n, m = M*t, L*t + 1
    T50 = sum(c*(((n - q) // (q + 1)) // d)
              for q, terms in events50.items() for d, c in terms.items())
    T10_scan = sum(class_count((m - q) // (q + 1), a, L)
                  for a, q in enumerate(first10) if q)
    T10_crt = sum(c*class_count((m - q) // (q + 1), a, modulus)
                 for q, terms in crt10.items() for (a, modulus), c in terms.items())
    assert T10_scan == T10_crt
    assert abs(F(T50) - n*C0) <= M + 2
    assert abs(F(T10_scan) - m*beta) <= L + 2
    if t == 1:
        assert T10_scan == len(truncated(m, 10))
        assert T10_scan <= len(literal(m))
    finite_counts.append({
        "t": t, "n": n, "m": m, "T50_n_exact": T50,
        "T10_m_exact": T10_scan,
        "T50_counting_error": str(F(T50) - n*C0),
        "T10_counting_error": str(F(T10_scan) - m*beta),
    })

A, B = F(M + 3, M), F(L + 2, L)
t0 = (A + B) // delta + 1
assert t0 == 203
gap202 = delta - (A + B)/202
gap203 = delta - (A + B)/203
assert gap202 < 0 < gap203
assert gap203 == F(559612671694976819161613011, 17543633842515402252748580463000)
# Cross multiplication certificate; strict sign uses integers only.
cross = (delta.numerator*(A + B).denominator*203
         - (A + B).numerator*delta.denominator)
assert cross > 0
source_hash = hashlib.sha256((ROOT / "source.md").read_bytes()).hexdigest()
assert source_hash == "06bb18541ed5c313de4681fcc61eebb42d73353add1b3dc546c441aa8a9015b6"

result = {
    "job_id": JOB,
    "python": platform.python_version(),
    "arithmetic": "exact integers and fractions.Fraction; deterministic; no random sampling",
    "scope": "finite arithmetic and falsification tests; universal lemmas are proved in research-proof.md; no referee acceptance",
    "source_sha256": source_hash,
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "endpoint_class_count_checks": endpoint_checks,
    "L10": L, "L50": M,
    "lower_first_counts": counts10,
    "lower_counts_methods": ["complete residue-class sieve", "generalized CRT inclusion-exclusion"],
    "lower_crt_first_event_term_counts": {q: len(v) for q, v in crt10.items()},
    "zero50_densities": {q: str(d) for q, d in d50.items() if d},
    "upper_density_methods": ["closed valuation formulas", "signed divisibility-indicator counts over a complete period"],
    "upper_indicator_term_counts": {q: n for q, n in indicator_sizes.items() if n},
    "zero_class_complete_period_tests": zero_period_tests,
    "zero_class_structured_first_witness_tests": len(structured),
    "membership_exhaustive_n_range": [1, small_limit],
    "additional_literal_n_values": targeted_ns,
    "cutoff_tail_checks": cutoff_checks,
    "small_n_progression_counting_checks": counting_checks,
    "finite_progression_truncated_counts": finite_counts,
    "C0": str(C0), "alpha": str(alpha), "beta": str(beta), "delta": str(delta),
    "upper_error_coefficient_A": str(A), "lower_error_coefficient_B": str(B),
    "common_threshold_t0": t0,
    "finite_upper_constant": str(alpha + A/t0),
    "finite_lower_constant": str(beta - B/t0),
    "coarse_gap_at_202": str(gap202), "certified_gap_at_203": str(gap203),
    "threshold_cross_multiplication_positive_integer": cross,
    "all_assertions_passed": True,
    "limits": [
        "No enumeration of the full L50 residue period.",
        "No literal computation of S2(M*t).",
        "No inference about all n from the finite n tests.",
        "The independent methods run in one researcher context; no independent referee is claimed.",
    ],
}
destination = ROOT / "evidence/research-verification.json"
temporary = destination.with_suffix(".json.tmp")
temporary.write_text(json.dumps(result, indent=2) + "\n")
temporary.replace(destination)
print(json.dumps({"evidence": str(destination.relative_to(ROOT)),
                  "all_assertions_passed": True, "common_threshold_t0": t0,
                  "certified_gap_at_203": str(gap203)}))
