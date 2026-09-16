#!/usr/bin/env python3
"""Separate deterministic triage checks; no universal theorem is certified."""
from fractions import Fraction
from math import isqrt, lcm
from pathlib import Path
import hashlib
import json
import platform

ROOT = Path(__file__).resolve().parents[1]
JOB = "newwin-00001-p19-triage-624bca8c0b20"

def primes_up_to(n):
    sieve = bytearray(b"\1") * (n + 1)
    sieve[:2] = b"\0\0"
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            for m in range(p * p, n + 1, p):
                sieve[m] = 0
    return [p for p in range(2, n + 1) if sieve[p]]

PS = primes_up_to(2048)

def literal(n):
    first = {n % k for k in range(1, n // 2 + 1)}
    return {n % k for k in first if k}

# Generate divisors independently, then test every possible positive remainder.
N = 2048
divisors = [[] for _ in range(N + 1)]
for q in range(3, N + 1):
    for v in range(q, N + 1, q):
        divisors[v].append(q)
tested_pairs = 0
for n in range(1, N + 1):
    actual = literal(n) - {0}
    predicted = set()
    for r in range(1, n // 4 + 1):
        tested_pairs += 1
        for q in divisors[n - r]:
            if (q + 1) * r > n - q:
                continue
            for p in PS:
                if p >= q:
                    break
                if ((q - 1) * n + r) % (p * q) == 0:
                    predicted.add(r)
                    break
            if r in predicted:
                break
    assert predicted == actual, (n, predicted ^ actual)

def residue_scan(Q, b):
    small_primes = [p for p in PS if p < Q]
    period = lcm(*(p * q for q in range(3, Q + 1)
                   for p in small_primes if p < q))
    counts = {q: 0 for q in range(3, Q + 1)}
    # Test each residue using the separate divisibilities q|(b-r), p|(b-k).
    for r in range(period):
        for q in counts:
            if (b - r) % q:
                continue
            k = (b - r) // q
            if any((b - k) % p == 0 for p in small_primes if p < q):
                counts[q] += 1
                break
    constant = sum((Fraction(v, period * (q + 1))
                    for q, v in counts.items()), Fraction())
    return period, counts, constant

def zero_density_dp(Q):
    """CRT weights for v_p=0, v_p in {1,2}, v_p>=3; no handoff formula."""
    # State: smallest present prime (0 if none), earliest witness (Q+1 if none).
    # Later primes can beat an already recorded prime-square witness.
    states = {(0, Q + 1): Fraction(1)}
    for p in [p for p in PS if p <= Q]:
        choices = [(False, False, Fraction(p - 1, p))]
        if p * p <= Q:
            choices += [(True, False, Fraction(p * p - 1, p ** 3)),
                        (True, True, Fraction(1, p ** 3))]
        else:
            choices += [(True, False, Fraction(1, p))]
        new = {}
        for (first, earliest), weight in states.items():
            for present, cube, prob in choices:
                witness = earliest
                if present and first:
                    witness = min(witness, p)
                if cube:
                    witness = min(witness, p * p)
                key = (first or (p if present else 0), witness)
                new[key] = new.get(key, Fraction()) + weight * prob
        states = new
    density = {q: Fraction() for q in range(3, Q + 1)}
    unused = Fraction()
    for (_, witness), weight in states.items():
        if witness <= Q:
            density[witness] += weight
        else:
            unused += weight
    assert sum(density.values()) + unused == 1
    constant = sum((d / (q + 1) for q, d in density.items()), Fraction())
    return density, constant

Q = 50
clauses = [(q, p * q) for q in range(3, Q + 1) for p in PS if p < q]
class_checks = 100000
for r in range(1, class_checks + 1):
    first_direct = next((q for q, modulus in clauses if r % modulus == 0), Q + 1)
    prime_factors = [p for p in PS if p <= Q and r % p == 0]
    second = prime_factors[1] if len(prime_factors) >= 2 else Q + 1
    cubes = [p * p for p in PS if p * p <= Q and r % (p ** 3) == 0]
    classified = min([Q + 1, second] + cubes)
    assert first_direct == classified, (r, first_direct, classified)

L10, counts1, beta = residue_scan(10, 1)
_, counts0, zero10 = residue_scan(10, 0)
d10, dp10 = zero_density_dp(10)
assert zero10 == dp10
assert all(Fraction(counts0[q], L10) == d10[q] for q in counts0)
d50, C0 = zero_density_dp(50)
alpha = C0 + Fraction(1, 52)
gap = beta - alpha
assert gap > 0
L50 = lcm(*(modulus for _, modulus in clauses))

handoff = json.loads((ROOT / "literature/p19-cutoff-check.json").read_text())
assert beta == Fraction(handoff["lower_constant"])
assert C0 == Fraction(handoff["upper_trials"][-1]["d0"])
assert alpha == Fraction(handoff["upper_trials"][-1]["upper"])
assert gap == Fraction(handoff["upper_trials"][-1]["lower_minus_upper"])

result = {
    "job_id": JOB,
    "python": platform.python_version(),
    "arithmetic": "exact integers and Fraction; deterministic",
    "scope": "finite tests and exact rational arithmetic; no referee acceptance",
    "source_sha256": hashlib.sha256((ROOT / "source.md").read_bytes()).hexdigest(),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "membership_n_range": [1, N],
    "positive_remainder_pairs_tested": tested_pairs,
    "zero_class_first_witness_r_range": [1, class_checks],
    "lower_Q": 10,
    "L10": L10,
    "lower_new_counts": counts1,
    "zero10_new_counts": counts0,
    "zero10_constant": str(zero10),
    "upper_Q": 50,
    "L50": L50,
    "zero50_densities": {q: str(d) for q, d in d50.items() if d},
    "C0": str(C0),
    "alpha": str(alpha),
    "beta": str(beta),
    "gap": str(gap),
    "strict_rational_separation": gap > 0,
    "agrees_with_handoff_constants": True,
}
print(json.dumps(result, indent=2))
