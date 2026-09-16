"""Exact regression checks for the proof dossier; no infinite-proof verdict.

Run from the project root: python3 evidence/research-verify.py
Dependencies: Python standard library and SymPy. No network or randomness.
"""
import hashlib
import json
from fractions import Fraction as Q
from math import comb
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
JOB = "primary-20260913-chen-ulc-failure-research-14052831c026"


def polynomial_rows(limit):
    # f_(m+1)=(1+s)f_m+(-1)^m; independent of descending division.
    a = [1]
    for m in range(1, limit + 1):
        yield m, a
        nxt = [0] * (m + 1)
        for j, v in enumerate(a):
            nxt[j] += v
            nxt[j + 1] += v
        nxt[0] += (-1) ** m
        a = nxt


def moment(p, q):
    # Integral of x^q(1+x)^p on [-1,1], evaluated as exact rationals.
    return sum((Q(2 * comb(p, ell), q + ell + 1)
                for ell in range(p + 1) if (q + ell) % 2 == 0), Q(0))


def hankel(p, k):
    a, b, c = (moment(p, k + r) for r in range(3))
    return a * c - b * b


def minor(a, m, j):
    return j * (m - 1 - j) * a[j] ** 2 - (j + 1) * (m - j) * a[j-1] * a[j+1]


def symbolic_checks():
    m, k = sp.symbols("m k")
    A, B, C, D = sp.symbols("A B C D")
    H, E = A*C - B**2, B*D - C**2
    hp = (A+B)*(C+D) - (B+C)**2
    rec_residual = sp.expand(B*hp - (B+C)*H - (B+A)*E)
    assert rec_residual == 0
    base = sp.factor((6/(k+2)+2/(k+4))*(6/(k+4)+2/(k+6))
                     - (2/(k+2)+6/(k+4))**2)
    target = 64*(k+1)/((k+2)**2*(k+4)**2*(k+6))
    assert sp.cancel(base-target) == 0
    endpoint = sp.expand((m-2)**3-(m-1)*(m**2-5*m+8))
    assert endpoint == -m
    norm_cancellation = sp.expand(C*(A+2*B+C)-(B+C)**2-(A*C-B**2))
    assert norm_cancellation == 0
    return {"recurrence_residual_after_multiplying_by_M1": str(rec_residual),
            "odd_k_p3_hankel_factored": str(base),
            "top_endpoint_minor": str(endpoint),
            "normalized_minor_cancellation_residual": str(norm_cancellation)}


def main():
    symbolic = symbolic_checks()
    s = sp.symbols("s")
    division_checks = normalized_checks = target_checks = same_h_checks = 0
    quotient_identity_checks = 0
    rows = dict(polynomial_rows(257))
    chosen_m = list(range(4, 31)) + [63, 64, 65, 127, 128, 129, 257]
    endpoint_examples = []
    selected_indices = {}
    for m in chosen_m:
        a = rows[m]
        h = a.copy()
        h[0] += (-1)**m
        assert len(a) == m and a[-1] == 1
        assert min(a) >= 0 and min(h) >= 0
        for P, const, linear in [(a, -(-1)**m, 0), (h, (-1)**m, (-1)**m)]:
            # Check all coefficients of the original quotient identities.
            for j in range(m + 1):
                lhs = 2*(P[j] if j < m else 0)+(P[j-1] if j else 0)
                rhs = comb(m, j)+(const if j == 0 else 0)+(linear if j == 1 else 0)
                assert lhs == rhs
            quotient_identity_checks += 1
        if m <= 18:
            for P, numerator in [(a, (s+1)**m-(-1)**m),
                                 (h, (s+1)**m+(-1)**m*(s+1))]:
                quotient, remainder = sp.div(sp.Poly(numerator, s), sp.Poly(s+2, s))
                assert remainder.is_zero
                assert [int(quotient.nth(j)) for j in range(m)] == P
                division_checks += 1
        indices = list(range(1, m-1)) if m <= 30 else sorted({1, 2, 3, 4, 5, m//2, m-3, m-2})
        selected_indices[str(m)] = indices
        for j in indices:
            p, k = j-1, m-j-2
            bprev, b, bnext = (Q(a[t], comb(m-1, t)) for t in (j-1, j, j+1))
            for t, bt in [(j-1, bprev), (j, b), (j+1, bnext)]:
                assert bt == Q(m, 2**(t+1))*moment(t, m-1-t)
            reverse = bprev*bnext-b*b
            H = hankel(p, k)
            assert reverse == Q(m*m, 2**(2*j+2))*H
            d = minor(a, m, j)
            assert d == -j*(m-1-j)*comb(m-1, j)**2*reverse
            normalized_checks += 1
            if j >= 2:
                assert d == minor(h, m, j)
                same_h_checks += 1
            if j >= 4:
                assert d < 0
                target_checks += 1
        assert minor(a, m, m-2) == minor(h, m, m-2) == -m
        endpoint_examples.append({"m":m, "j":m-2, "D":-m})

    # Asymmetric and boundary moment tests. These are finite regression,
    # not an enlarged census offered as proof.
    ps = [3, 4, 5, 10, 31, 64, 101]
    ks = [0, 1, 2, 3, 16, 17, 128, 129, 1000000, 1000001]
    moment_checks = recurrence_checks = 0
    for p in ps:
        for k in ks:
            H = hankel(p, k)
            assert H > 0
            moment_checks += 1
            if k % 2:
                A, B, C, D = [moment(p, k+r) for r in range(4)]
                assert min(A, B, C, D) > 0
                E = B*D-C*C
                assert E > 0
                assert B*hankel(p+1, k) == (B+C)*H+(B+A)*E
                recurrence_checks += 1
    negative = hankel(2, 1)
    assert negative == Q(-16, 225)
    assert minor(rows[6], 6, 3) == 6
    out = {"job_id": JOB,
           "arithmetic": "exact integers, Fraction, and symbolic rational/polynomial algebra",
           "sympy_version": sp.__version__,
           "symbolic_identities": symbolic,
           "original_quotient_identity_checks": quotient_identity_checks,
           "independent_sympy_division_checks": division_checks,
           "complete_internal_index_m_range": [4, 30],
           "additional_selected_m": chosen_m[27:],
           "selected_indices_by_m": selected_indices,
           "normalized_minor_identity_checks": normalized_checks,
           "higher_index_strict_negative_checks": target_checks,
           "same_f_h_minor_checks": same_h_checks,
           "moment_test_p_values": ps, "moment_test_k_values": ks,
           "positive_hankel_checks": moment_checks,
           "denominator_free_recurrence_checks": recurrence_checks,
           "negative_control": {"p":2, "k":1, "H":str(negative), "m":6, "j":3, "D":6},
           "endpoint_examples": endpoint_examples,
           "source_sha256": hashlib.sha256((ROOT/"source.md").read_bytes()).hexdigest(),
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "all_assertions_passed": True,
           "limitations": "Finite exact regression and symbolic identities; positivity for all parameters is proved in research-proof.md. No formal proof assistant or independent referee acceptance is claimed."}
    path = Path(__file__).with_suffix(".json")
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(out, indent=2)+"\n")
    tmp.replace(path)
    print(json.dumps({k: out[k] for k in ["job_id", "symbolic_identities", "original_quotient_identity_checks", "independent_sympy_division_checks", "normalized_minor_identity_checks", "higher_index_strict_negative_checks", "positive_hankel_checks", "denominator_free_recurrence_checks", "negative_control", "all_assertions_passed"]}, indent=2))


if __name__ == "__main__":
    main()
