#!/usr/bin/env python3
"""Attack the stronger 6-section identity suggested by the exact data.

The identity under test is

  sum_{m>=0} cphi_18(6m+1) q^m == 4*f_2*f_3^2/(f_1*f_6) (mod 16).

The right side is also generated independently as the unary theta series
4*sum_{k in Z} q^(k(3k-1)/2).  The first 100 section coefficients were the
discovery range; all remaining available coefficients are a held-out range.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

import source_formula_mod16 as sf

HERE = Path(__file__).resolve().parent
DISCOVERY_MAX_M = 99


def unary_theta(limit: int) -> np.ndarray:
    out = np.zeros(limit + 1, dtype=np.int64)
    # k(3k-1)/2 <= limit implies |k| <= sqrt(2*limit/3)+1.
    bound = int((2 * limit / 3) ** 0.5) + 2
    for k in range(-bound, bound + 1):
        exponent = k * (3 * k - 1) // 2
        if 0 <= exponent <= limit:
            out[exponent] += 1
    return out


def digest(a: np.ndarray) -> str:
    return hashlib.sha256(bytes(a.astype(np.uint8))).hexdigest()


def main() -> None:
    constant_term = np.frombuffer(
        (HERE / "constant_term_coefficients_mod16.bin").read_bytes(),
        dtype=np.uint8,
    ).astype(np.int64)
    source_formula = np.frombuffer(
        (HERE / "source_formula_coefficients_mod16.bin").read_bytes(),
        dtype=np.uint8,
    ).astype(np.int64)
    assert np.array_equal(constant_term, source_formula)

    max_m = (len(source_formula) - 2) // 6
    section_constant_term = np.array(
        [constant_term[6 * m + 1] for m in range(max_m + 1)],
        dtype=np.int64,
    )
    section_source_formula = np.array(
        [source_formula[6 * m + 1] for m in range(max_m + 1)],
        dtype=np.int64,
    )

    eta = sf.eta_quotient({1: -1, 2: 1, 3: 2, 6: -1})[: max_m + 1]
    theta = unary_theta(max_m)
    # This finite check is redundant mathematically: Jacobi's triple product
    # proves f_2*f_3^2/(f_1*f_6) = sum_k q^(k(3k-1)/2) in Z[[q]].
    assert np.array_equal(eta, theta)
    rhs = 4 * theta % sf.MOD

    assert np.array_equal(section_constant_term, rhs)
    assert np.array_equal(section_source_formula, rhs)
    assert DISCOVERY_MAX_M < max_m
    assert np.array_equal(
        section_source_formula[DISCOVERY_MAX_M + 1 :],
        rhs[DISCOVERY_MAX_M + 1 :],
    )

    support = np.flatnonzero(theta).tolist()
    report = {
        "identity_status": "exact finite observation, not an all-orders proof",
        "identity": "sum_m cphi_18(6m+1)q^m == 4*f_2*f_3^2/(f_1*f_6) (mod 16)",
        "equivalent_rhs": "4*sum_{k in Z} q^(k(3k-1)/2)",
        "m_range": [0, max_m],
        "discovery_range": [0, DISCOVERY_MAX_M],
        "held_out_range": [DISCOVERY_MAX_M + 1, max_m],
        "independent_left_generators": [
            "finite Laurent constant-term product",
            "Das--Nath--Sarma formula (3.15)",
        ],
        "right_generators": [
            "eta quotient via Euler/partition recurrences",
            "direct generalized-pentagonal exponent enumeration",
        ],
        "section_vector_sha256": digest(section_source_formula),
        "rhs_vector_sha256": digest(rhs),
        "support_size": len(support),
        "support_m_residues_mod5": sorted({m % 5 for m in support}),
        "target_classes_3_and_4_absent": all(m % 5 not in (3, 4) for m in support),
        "all_checks_passed": True,
    }
    (HERE / "h_identity_metadata.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
