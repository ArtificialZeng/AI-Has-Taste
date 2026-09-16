#!/usr/bin/env python3
"""Exact finite checks; the infinite theorem is proved in research-proof.md.

This implementation does not import the triage checker or use its module
normal-form algorithm. Negative monomial images instead use the Laurent
identity P*x^(1-m)=x^(p-m)+x^(-m). Coefficients use Lucas digit products.
"""
from pathlib import Path
from functools import lru_cache
import hashlib
import json
import math

JOB = "newwin-00001-p18-research-8635786e3d2c"


def add(a, exponent, coefficient, p):
    a[exponent] = (a.get(exponent, 0) + coefficient) % p
    if not a[exponent]:
        del a[exponent]


def multiply(a, b, p, limit=None):
    out = {}
    for i, c in a.items():
        for j, d in b.items():
            if limit is None or i + j <= limit:
                add(out, i + j, c * d, p)
    return out


def lucas(n, k, p):
    if not 0 <= k <= n:
        return 0
    value = 1
    while n or k:
        ni, ki = n % p, k % p
        if ki > ni:
            return 0
        value = value * math.comb(ni, ki) % p
        n, k = n // p, k // p
    return value


def ct_monomial(p, n, exponent):
    if (n - exponent) % p:
        return 0
    return lucas(n, (n - exponent) // p, p)


def shift(h, p):
    out = {}
    for r, c in h.items():
        if r:
            add(out, r - 1, c, p)
            add(out, r + p - 1, c, p)
    return out


@lru_cache(None)
def monomial_image(p, exponent):
    if exponent >= 0:
        return {exponent: 1}
    m = -exponent
    # This solves for x^(-m) using only monomials with smaller negative degree.
    h = shift(monomial_image(p, 1 - m), p)
    for r, c in monomial_image(p, p - m).items():
        add(h, r, -c, p)
    return h


def rank(rows, p, width):
    basis = {}
    for row in rows:
        v = list(row)
        for i in range(width):
            if not v[i]:
                continue
            if i in basis:
                scalar = v[i]
                v = [(a - scalar * b) % p for a, b in zip(v, basis[i])]
            else:
                inverse = pow(v[i], -1, p)
                basis[i] = [(a * inverse) % p for a in v]
                break
    return len(basis)


def digit_sum(n, p):
    total = 0
    while n:
        total += n % p
        n //= p
    return total


def next_power_exponent(p, upper):
    k, value = 0, 1
    while value <= upper:
        k += 1
        value *= p
    return k


def term(family, index, p):
    if family == "ones":
        return 1
    if family == "linear":
        return index + 1
    if family == "periodic":
        return (1, p - 1, 2, p)[index % 4]
    if family == "powers":
        return p ** index
    raise ValueError(family)


def divisible_block(p, k, start, family):
    """Pigeonhole construction with arbitrary-precision positive integers."""
    modulus = p ** k
    prefix = 0
    seen = {0: (start, 0)}
    # There are modulus+1 partial sums including the initial empty sum.
    for index in range(start, start + modulus):
        prefix += term(family, index, p)
        residue = prefix % modulus
        if residue in seen:
            left, old = seen[residue]
            total = prefix - old
            assert total > 0 and total % modulus == 0
            return {
                "start": left, "end_exclusive": index + 1,
                "sum": total, "k": k, "terms_scanned": index + 1 - start,
            }
        seen[residue] = (index + 1, prefix)
    raise AssertionError("Pigeonhole principle violated")


def digit_certificate(p, degree, a, family):
    blocks = []
    start = 0
    upper = (p - 1) * a + degree
    for _ in range(degree + 1):
        k = next_power_exponent(p, upper)
        b = divisible_block(p, k, start, family)
        assert p ** k > upper
        if blocks:
            assert k > blocks[-1]["k"]
            assert b["start"] >= blocks[-1]["end_exclusive"]
        blocks.append(b)
        start = b["end_exclusive"]
        upper = (p - 1) * b["sum"]
    n = a + sum(b["sum"] for b in blocks)
    offsets = []
    for r in range(degree + 1):
        lhs = digit_sum((p - 1) * n + r, p)
        rhs = digit_sum((p - 1) * a + r, p)
        rhs += sum(digit_sum((p - 1) * b["sum"], p) for b in blocks)
        assert lhs == rhs and lhs > degree
        offsets.append(lhs)
    return {
        "p": p, "degree": degree, "a": a, "family": family,
        "blocks": blocks, "excluded_n": n,
        "digit_sums_for_every_offset": offsets,
    }


def main():
    limit = 1024
    radius = 16
    coefficient_rows = []
    kernel_rows = []
    for p in (2, 3, 5, 7, 11, 13, 17):
        y = {}
        a = 1
        while a <= limit:
            y[a] = 1
            a = p * a + 1
        powers = [{0: 1}]
        for _ in range(radius * (p - 1)):
            powers.append(multiply(powers[-1], y, p, limit))
        comparisons = 0
        binomial_checks = 0
        support_checks = 0
        coefficient_table = {}
        for e in range(-radius, radius + 1):
            h = monomial_image(p, e)
            series = {}
            for r, c in h.items():
                for n, d in powers[r].items():
                    add(series, n, c * d, p)
            degree = max(h, default=0)
            values = []
            for n in range(limit + 1):
                expected = ct_monomial(p, n, e)
                values.append(expected)
                assert series.get(n, 0) == expected, (p, e, n)
                comparisons += 1
                if n <= 128:
                    k = (n - e) // p
                    direct = (
                        math.comb(n, k) % p
                        if (n - e) % p == 0 and 0 <= k <= n else 0
                    )
                    assert expected == direct
                    binomial_checks += 1
                if expected:
                    assert any(
                        digit_sum((p - 1) * n + r, p) <= degree
                        for r in range(degree + 1)
                    )
                    support_checks += 1
            coefficient_table[e] = values
        coefficient_rows.append({
            "p": p, "comparisons": comparisons,
            "integer_binomial_crosschecks": binomial_checks,
            "support_containment_checks": support_checks,
        })
        # All coefficient vectors on [-R,R] at once, using finite-field ranks.
        # The comparison is only for the explicitly recorded finite n-range.
        for r in range(1, radius + 1):
            bound = r * (p - 1)
            matrix = [
                [coefficient_table[e][n] for e in range(-r, r + 1)]
                for n in range(bound + 1)
            ]
            matrix_rank = rank(matrix, p, 2 * r + 1)
            nullity = 2 * r + 1 - matrix_rank
            highest_k = r // (p - 1)
            assert nullity == highest_k, (p, r, nullity, highest_k)
            # Independently build P^k by Laurent multiplication and check
            # that these coefficient vectors span the finite-prefix kernel.
            pk = {0: 1}
            kernel_basis = []
            for k in range(1, highest_k + 1):
                pk = multiply(pk, {-1: 1, p - 1: 1}, p)
                assert min(pk) >= -r and max(pk) <= r
                vector = [pk.get(e, 0) for e in range(-r, r + 1)]
                assert all(
                    sum(c * d for c, d in zip(row, vector)) % p == 0
                    for row in matrix
                )
                kernel_basis.append(vector)
            assert rank(kernel_basis, p, 2 * r + 1) == nullity
            kernel_rows.append({
                "p": p, "radius": r, "n_min": 0, "n_max": bound,
                "matrix_rank": matrix_rank, "kernel_dimension": nullity,
                "kernel_basis": f"P^k, 1<=k<={highest_k}",
            })

    certificates = []
    for p in (2, 3, 5, 7):
        for d in range(4):
            for a in (0, 1, p * p - 1):
                for family in ("ones", "linear", "periodic", "powers"):
                    certificates.append(digit_certificate(p, d, a, family))
    # Higher D with a fast-growing family; still exact finite checks.
    for p in (2, 3, 5, 7, 11):
        for d in (4, 8, 16):
            certificates.append(digit_certificate(p, d, p ** 4 - 1, "powers"))
    witness_path = Path(__file__).with_name("digit-block-certificates.json")
    witness_path.write_text(json.dumps({
        "job_id": JOB,
        "scope": "Explicit finite digit-block constructions only",
        "certificates": certificates,
    }, indent=2) + "\n")
    result = {
        "job_id": JOB,
        "arithmetic": "Exact Python integers and prime fields; no randomness",
        "monomial_scope": "p=2,3,5,7,11,13,17; exponents -16..16; n=0..1024",
        "coefficient_rows": coefficient_rows,
        "coefficient_comparisons": sum(r["comparisons"] for r in coefficient_rows),
        "integer_binomial_crosschecks": sum(
            r["integer_binomial_crosschecks"] for r in coefficient_rows
        ),
        "finite_kernel_matrices": kernel_rows,
        "digit_block_certificate_count": len(certificates),
        "digit_certificate_file": witness_path.name,
        "digit_certificate_sha256": hashlib.sha256(witness_path.read_bytes()).hexdigest(),
        "limitations": [
            "Finite coefficient comparisons are not an infinite series identity proof.",
            "Each kernel matrix covers all Q on its stated exponent range only through its stated n_max.",
            "Digit-block tests do not quantify over arbitrary infinite sequences.",
            "The recurrence implication is established by the written induction, not by these tests.",
            "No fresh referee or formal proof assistant was used in this research job.",
        ],
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    Path(__file__).with_name("research-check.json").write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps({
        "coefficient_comparisons": result["coefficient_comparisons"],
        "integer_binomial_crosschecks": result["integer_binomial_crosschecks"],
        "kernel_matrices": len(kernel_rows),
        "digit_block_certificates": len(certificates),
        "status": "all assertions passed",
    }, indent=2))


if __name__ == "__main__":
    main()
