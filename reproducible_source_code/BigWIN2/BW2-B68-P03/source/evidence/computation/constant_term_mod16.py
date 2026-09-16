#!/usr/bin/env python3
"""Exact constant-term computation of Cphi_18(q) modulo 16.

Uses directly
 CT_z (1+z^{-1})^18 prod_{w>=1}(1+z q^w)^18(1+z^{-1}q^w)^18.
All arithmetic is in Z/256Z in uint8 arrays and is reduced to Z/16Z
on output.  Since reduction Z/256Z -> Z/16Z is a ring homomorphism,
uint8 wraparound is exact for the requested residues.
"""
from __future__ import annotations

import csv
import hashlib
import json
import platform
import sys
import time
from math import comb
from pathlib import Path

import numpy as np

N = 3025
K = 18
MOD = 16
HERE = Path(__file__).resolve().parent


def min_sum_positive(r: int) -> int:
    """Minimum sum of r choices from 18 copies of each 1,2,... ."""
    blocks, rem = divmod(r, K)
    return K * blocks * (blocks + 1) // 2 + rem * (blocks + 1)


def max_columns(limit: int) -> int:
    # The top row selects r positive weights.  The bottom row has 18 zero
    # weights and then the same positive multiset.
    r = 0
    while min_sum_positive(r + 1) + min_sum_positive(max(0, r + 1 - K)) <= limit:
        r += 1
    return r


def multiply_factor(dp: np.ndarray, weight: int, sign: int, choose: list[int]) -> np.ndarray:
    """Multiply by (1+z^sign q^weight)^18 in (Z/256Z)[q,z]."""
    zdim, qdim = dp.shape
    out = np.zeros_like(dp)
    max_t = K if weight == 0 else min(K, (qdim - 1) // weight)
    for t in range(max_t + 1):
        dz = sign * t
        dq = weight * t
        if dz >= 0:
            src_z = slice(0, zdim - dz)
            dst_z = slice(dz, zdim)
        else:
            src_z = slice(-dz, zdim)
            dst_z = slice(0, zdim + dz)
        src_q = slice(0, qdim - dq)
        dst_q = slice(dq, qdim)
        # uint8 multiplication/addition wraps modulo 256, hence exactly
        # preserves the desired value modulo 16.
        out[dst_z, dst_q] += np.uint8(choose[t]) * dp[src_z, src_q]
    return out


def main() -> None:
    started = time.time()
    rmax = max_columns(N)
    assert min_sum_positive(rmax) + min_sum_positive(max(0, rmax - K)) <= N
    assert min_sum_positive(rmax + 1) + min_sum_positive(rmax + 1 - K) > N
    choose = [comb(K, t) & 255 for t in range(K + 1)]
    dp = np.zeros((2 * rmax + 1, N + 1), dtype=np.uint8)
    zero = rmax
    dp[zero, 0] = 1

    # Bottom-row zero entries.
    dp = multiply_factor(dp, 0, -1, choose)
    # Positive weights.  Factors of weight > N cannot affect q^0,...,q^N.
    for w in range(1, N + 1):
        dp = multiply_factor(dp, w, +1, choose)
        dp = multiply_factor(dp, w, -1, choose)

    coeff = (dp[zero].astype(np.uint16) % MOD).tolist()
    csv_path = HERE / "constant_term_targets_mod16.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        wr = csv.writer(fh)
        wr.writerow(["progression", "n", "exponent", "residue_mod16"])
        for residue in (19, 25):
            for n in range(101):
                exponent = 30 * n + residue
                wr.writerow([residue, n, exponent, coeff[exponent]])

    raw = bytes(coeff)
    metadata = {
        "algorithm": "finite Laurent constant-term product",
        "identity": "CT_z (1+z^-1)^18 prod_{w=1}^N (1+z q^w)^18(1+z^-1 q^w)^18",
        "coefficient_range": [0, N],
        "arithmetic": "uint8 modulo 256, then canonical reduction modulo 16",
        "rmax": rmax,
        "rmax_justification": {
            "min_energy_rmax": min_sum_positive(rmax) + min_sum_positive(max(0, rmax - K)),
            "min_energy_rmax_plus_1": min_sum_positive(rmax + 1) + min_sum_positive(rmax + 1 - K),
        },
        "all_202_target_residues_zero": all(coeff[30*n+r] == 0 for r in (19, 25) for n in range(101)),
        "coefficient_vector_sha256": hashlib.sha256(raw).hexdigest(),
        "target_csv_sha256": hashlib.sha256(csv_path.read_bytes()).hexdigest(),
        "elapsed_seconds": round(time.time() - started, 3),
        "python": sys.version,
        "numpy": np.__version__,
        "platform": platform.platform(),
    }
    (HERE / "constant_term_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    (HERE / "constant_term_coefficients_mod16.bin").write_bytes(raw)
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
