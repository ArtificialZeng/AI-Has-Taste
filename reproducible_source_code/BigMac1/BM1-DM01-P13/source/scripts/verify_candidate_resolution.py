#!/usr/bin/env python3
"""Exact checks for the candidate Clausen/Legendre--Lucas proof.

This is a deterministic standard-library verifier.  Finite checks exercise
all algebraic identities used by the universal prose proof; they do not by
themselves prove the universal quantifiers.
"""

from __future__ import annotations

import hashlib
import json
import math
import platform
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results" / "candidate_resolution_verification.json"


def primes_through(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[:2] = b"\x00\x00"
    for q in range(2, math.isqrt(limit) + 1):
        if sieve[q]:
            sieve[q * q : limit + 1 : q] = b"\x00" * (
                (limit - q * q) // q + 1
            )
    return [q for q in range(2, limit + 1) if sieve[q]]


def poly_trim(a: list[Fraction]) -> list[Fraction]:
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * max(len(a), len(b))
    for i in range(len(out)):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return poly_trim(out)


def poly_scale(a: list[Fraction], c: Fraction) -> list[Fraction]:
    return poly_trim([c * x for x in a])


def poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return poly_trim(out)


def poly_pow(a: list[Fraction], n: int) -> list[Fraction]:
    out = [Fraction(1)]
    base = a
    while n:
        if n & 1:
            out = poly_mul(out, base)
        base = poly_mul(base, base)
        n //= 2
    return out


def legendre_polynomials(n: int) -> list[list[Fraction]]:
    values = [[Fraction(1)]]
    if n == 0:
        return values
    values.append([Fraction(0), Fraction(1)])
    for k in range(1, n):
        numerator = poly_add(
            poly_scale([Fraction(0)] + values[k], Fraction(2 * k + 1)),
            poly_scale(values[k - 1], Fraction(-k)),
        )
        values.append(poly_scale(numerator, Fraction(1, k + 1)))
    return values


def companion_from_convolution(P: list[list[Fraction]], n: int) -> list[Fraction]:
    out = [Fraction(0)]
    for j in range(1, n + 1):
        out = poly_add(out, poly_scale(poly_mul(P[j - 1], P[n - j]), Fraction(1, j)))
    return out


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


def companion_from_bernstein(n: int) -> list[Fraction]:
    # Returns -D_n, where D_n is the harmonic Bernstein sum in (C6).
    u = [Fraction(1, 2), Fraction(1, 2)]
    v = [Fraction(-1, 2), Fraction(1, 2)]
    D = [Fraction(0)]
    for b in range(n + 1):
        term = poly_mul(poly_pow(u, b), poly_pow(v, n - b))
        coefficient = Fraction(math.comb(n, b) ** 2) * (harmonic(n - b) - harmonic(b))
        D = poly_add(D, poly_scale(term, coefficient))
    return poly_scale(D, Fraction(-1))


def clausen_rhs(n: int) -> list[Fraction]:
    # Sum (-n)_k(n+1)_k(1/2)_k/(k!)^3 * (1-z^2)^k.
    out = [Fraction(0)]
    poch_neg = poch_pos = poch_half = Fraction(1)
    factorial = 1
    base = [Fraction(1), Fraction(0), Fraction(-1)]
    for k in range(n + 1):
        coefficient = poch_neg * poch_pos * poch_half / (factorial**3)
        out = poly_add(out, poly_scale(poly_pow(base, k), coefficient))
        if k < n:
            poch_neg *= -n + k
            poch_pos *= n + 1 + k
            poch_half *= Fraction(1, 2) + k
            factorial *= k + 1
    return out


Pair = tuple[int, int]


def pair_add(x: Pair, y: Pair, modulus: int) -> Pair:
    return ((x[0] + y[0]) % modulus, (x[1] + y[1]) % modulus)


def pair_mul(x: Pair, y: Pair, d: int, modulus: int) -> Pair:
    return (
        (x[0] * y[0] + d * x[1] * y[1]) % modulus,
        (x[0] * y[1] + x[1] * y[0]) % modulus,
    )


def pair_scale(x: Pair, c: int, modulus: int) -> Pair:
    return (c * x[0] % modulus, c * x[1] % modulus)


def pair_pow(x: Pair, n: int, d: int, modulus: int) -> Pair:
    out = (1, 0)
    while n:
        if n & 1:
            out = pair_mul(out, x, d, modulus)
        x = pair_mul(x, x, d, modulus)
        n //= 2
    return out


def pair_inverse(x: Pair, d: int, modulus: int) -> Pair:
    norm = (x[0] * x[0] - d * x[1] * x[1]) % modulus
    inverse_norm = pow(norm, -1, modulus)
    return (x[0] * inverse_norm % modulus, -x[1] * inverse_norm % modulus)


def strip_p(x: int, p: int) -> tuple[int, int]:
    valuation = 0
    while x % p == 0:
        x //= p
        valuation += 1
    return x, valuation


def binomial_sequence_mod_p2(n: int, p: int) -> list[int]:
    modulus = p * p
    values = [1]
    unit = 1
    valuation = 0
    for k in range(n):
        numerator, vn = strip_p(n - k, p)
        denominator, vd = strip_p(k + 1, p)
        valuation += vn - vd
        if valuation < 0:
            raise AssertionError("negative binomial valuation")
        unit = unit * numerator * pow(denominator, -1, modulus) % modulus
        values.append(0 if valuation >= 2 else unit * (p**valuation) % modulus)
    return values


def legendre_large_at_root(p: int) -> Pair:
    n = (p * p - 1) // 2
    modulus = p * p
    d = -63
    inv2 = pow(2, -1, modulus)
    u = (inv2, inv2)
    v = (-inv2 % modulus, inv2)
    ratio = pair_mul(u, pair_inverse(v, d, modulus), d, modulus)
    power = pair_pow(v, n, d, modulus)
    total = (0, 0)
    for coefficient in binomial_sequence_mod_p2(n, p):
        total = pair_add(
            total,
            pair_scale(power, coefficient * coefficient, modulus),
            modulus,
        )
        power = pair_mul(power, ratio, d, modulus)
    return total


def central_sum_mod(p: int, endpoint: int, exponent: int) -> int:
    modulus = p**exponent
    valuation = 0
    unit = 1
    total = 0
    for k in range(endpoint + 1):
        if 3 * valuation < exponent:
            total = (total + pow(unit, 3, modulus) * p ** (3 * valuation)) % modulus
        if k == endpoint:
            break
        numerator, vn = strip_p(2 * (2 * k + 1), p)
        denominator, vd = strip_p(k + 1, p)
        valuation += vn - vd
        unit = unit * numerator * pow(denominator, -1, modulus) % modulus
    return total


def harmonic_table_mod(p: int) -> list[int]:
    table = [0] * p
    for j in range(1, p):
        table[j] = (table[j - 1] + pow(j, -1, p * p)) % (p * p)
    return table


def check_digit_binomial_formula(p: int) -> int:
    h = (p - 1) // 2
    modulus = p * p
    H = harmonic_table_mod(p)
    checked = 0
    for a in range(h + 1):
        for b in range(h + 1):
            correction = (
                h * H[h] - a * H[b] - (h - a) * H[h - b]
            ) % modulus
            predicted = (
                math.comb(h, a)
                * math.comb(h, b)
                * (1 + p * correction)
            ) % modulus
            actual = math.comb(p * h + h, p * a + b) % modulus
            if actual != predicted:
                raise AssertionError(("digit-binomial", p, a, b, actual, predicted))
            checked += 1
    return checked


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    P = legendre_polynomials(20)
    companion_checks = 0
    for n in range(21):
        if companion_from_convolution(P, n) != companion_from_bernstein(n):
            raise AssertionError(("companion identity", n))
        companion_checks += 1

    clausen_checks = 0
    for n in range(13):
        if poly_mul(P[n], P[n]) != clausen_rhs(n):
            raise AssertionError(("Clausen identity", n))
        clausen_checks += 1

    digit_checks = sum(check_digit_binomial_formula(p) for p in primes_through(31) if p >= 5)

    rows: list[dict[str, object]] = []
    for p in primes_through(300):
        if p % 7 not in (3, 5, 6):
            continue
        if p == 3:
            direct = central_sum_mod(p, p * p, 3)
            rows.append(
                {
                    "p": p,
                    "separate_small_prime": True,
                    "A_p2_mod_p3": direct,
                    "target_mod_p3": (8 + p * p) % (p**3),
                    "holds": direct == (8 + p * p) % (p**3),
                }
            )
            continue
        value = legendre_large_at_root(p)
        modulus2 = p * p
        expected = (((-1) ** ((p - 1) // 2) * p) % modulus2, 0)
        square = pair_mul(value, value, -63, p**3)
        direct = central_sum_mod(p, p * p, 3)
        bridge_rhs = ((direct - 8) % (p**3), 0)
        row = {
            "p": p,
            "P_N_mod_p2": list(value),
            "expected_P_N_mod_p2": list(expected),
            "legendre_lift_holds": value == expected,
            "P_N_squared_mod_p3": list(square),
            "A_p2_minus_8_mod_p3": list(bridge_rhs),
            "clausen_bridge_holds": square == bridge_rhs,
            "target_holds": direct == (8 + p * p) % (p**3),
        }
        if not all(
            bool(row[key])
            for key in ("legendre_lift_holds", "clausen_bridge_holds", "target_holds")
        ):
            raise AssertionError(("candidate endpoint", row))
        rows.append(row)

    # Fail-closed attacks on hypotheses and signs.
    split_p = 11
    split_value = legendre_large_at_root(split_p)
    split_expected = (((-1) ** ((split_p - 1) // 2) * split_p) % (split_p**2), 0)
    attacks = {
        "flip_candidate_sign": all(
            row.get("P_N_mod_p2") != [(-row["expected_P_N_mod_p2"][0]) % (row["p"] ** 2), 0]
            for row in rows
            if row["p"] >= 5
        ),
        "replace_companion_minus_by_plus": companion_from_bernstein(1)
        != poly_scale(companion_from_convolution(P, 1), Fraction(-1)),
        "delete_nonresidue_root_hypothesis_at_p11": split_value != split_expected,
        "treat_p3_as_unramified": math.gcd(3, 2 * 3 * 7) != 1,
    }
    if not all(attacks.values()):
        raise AssertionError(("fail-closed attack unexpectedly survived", attacks))

    payload = {
        "problem_id": "mac01-p13",
        "status": "candidate-proof-verification-only",
        "proof_assistant_used": False,
        "python": sys.version,
        "platform": platform.platform(),
        "exact_symbolic_checks": {
            "clausen_identity_degrees_0_through_12": clausen_checks,
            "companion_identity_degrees_0_through_20": companion_checks,
            "digit_binomial_cases": digit_checks,
        },
        "eligible_endpoint_rows_through_300": rows,
        "all_endpoint_checks_pass": all(bool(row["holds"] if row["p"] == 3 else row["target_holds"]) for row in rows),
        "fail_closed_attacks": attacks,
        "limitations": [
            "Finite checks do not prove the universal statement.",
            "The universal argument is in proof/candidate_resolution.md and requires a fresh independent audit.",
            "The cited Sun theorem endpoints are inherited from the separately recorded primary-source audit.",
        ],
        "input_sha256": {
            "proof/candidate_resolution.md": sha256(ROOT / "proof" / "candidate_resolution.md"),
            "proof/structural_lemmas.md": sha256(ROOT / "proof" / "structural_lemmas.md"),
            "scripts/verify_candidate_resolution.py": sha256(Path(__file__).resolve()),
        },
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        json.dumps(
            {
                "status": "PASS",
                "eligible_primes_through_300": len(rows),
                "symbolic_checks": clausen_checks + companion_checks + digit_checks,
                "output": str(OUTPUT.relative_to(ROOT)),
                "output_sha256": sha256(OUTPUT),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
