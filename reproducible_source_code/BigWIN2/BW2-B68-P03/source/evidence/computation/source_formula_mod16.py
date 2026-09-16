#!/usr/bin/env python3
"""Independent exact computation from Das--Nath--Sarma formula (3.15).

This implementation does not use the Laurent constant-term product.  It
expands the eta products f_d=(q^d;q^d)_infinity by Euler's pentagonal
theorem, their inverses by the partition recurrence, and the Borwein cubic
theta a(q)=sum_{m,n in Z}q^(m^2+mn+n^2) by direct lattice enumeration.
All polynomial arithmetic is exact int64 convolution followed by reduction
modulo 16.
"""
from __future__ import annotations

import csv
import hashlib
import json
import platform
import sys
import time
from functools import lru_cache
from pathlib import Path

import numpy as np

N = 3025
MOD = 16
HERE = Path(__file__).resolve().parent


def mul(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    # Each convolution sum is < (N+1)*15^2 < 2^63, hence np.int64 is exact.
    return (np.convolve(a.astype(np.int64), b.astype(np.int64))[: N + 1] % MOD).astype(np.int64)


def power(a: np.ndarray, exponent: int) -> np.ndarray:
    out = np.zeros(N + 1, dtype=np.int64)
    out[0] = 1
    base = a
    e = exponent
    while e:
        if e & 1:
            out = mul(out, base)
        e >>= 1
        if e:
            base = mul(base, base)
    return out


@lru_cache(maxsize=None)
def f_basic(d: int) -> np.ndarray:
    out = np.zeros(N + 1, dtype=np.int64)
    out[0] = 1
    k = 1
    while True:
        g1 = d * k * (3 * k - 1) // 2
        g2 = d * k * (3 * k + 1) // 2
        if g1 > N:
            break
        sign = -1 if k & 1 else 1
        out[g1] = sign % MOD
        if g2 <= N:
            out[g2] = sign % MOD
        k += 1
    return out


@lru_cache(maxsize=None)
def inv_f_basic(d: int) -> np.ndarray:
    # 1/f_d is the ordinary partition series with q replaced by q^d.
    out = np.zeros(N + 1, dtype=np.int64)
    out[0] = 1
    for n in range(d, N + 1, d):
        total = 0
        k = 1
        while True:
            g1 = d * k * (3 * k - 1) // 2
            g2 = d * k * (3 * k + 1) // 2
            if g1 > n:
                break
            sign = 1 if k & 1 else -1
            total += sign * int(out[n - g1])
            if g2 <= n:
                total += sign * int(out[n - g2])
            k += 1
        out[n] = total % MOD
    return out


@lru_cache(maxsize=None)
def f_power(d: int, exponent: int) -> np.ndarray:
    return power(f_basic(d) if exponent >= 0 else inv_f_basic(d), abs(exponent))


def eta_quotient(exponents: dict[int, int]) -> np.ndarray:
    out = np.zeros(N + 1, dtype=np.int64)
    out[0] = 1
    for d, exponent in sorted(exponents.items()):
        if exponent:
            out = mul(out, f_power(d, exponent))
    return out


def cubic_theta(scale: int = 1) -> np.ndarray:
    out = np.zeros(N + 1, dtype=np.int64)
    # Q(m,n) >= (m^2+n^2)/2, so |m|,|n| <= sqrt(2N/scale).
    bound = int((2 * N / scale) ** 0.5) + 1
    for m in range(-bound, bound + 1):
        for n in range(-bound, bound + 1):
            q = scale * (m * m + m * n + n * n)
            if q <= N:
                out[q] += 1
    return out % MOD


def shifted_scaled(poly: np.ndarray, coefficient: int, shift: int) -> np.ndarray:
    out = np.zeros(N + 1, dtype=np.int64)
    if shift <= N:
        out[shift:] = (coefficient % MOD) * poly[: N + 1 - shift] % MOD
    return out


def main() -> None:
    started = time.time()
    aq = cubic_theta(1)
    aq3 = cubic_theta(3)
    aq6 = cubic_theta(6)
    apow = {p: power(aq, p) for p in (1, 2, 3, 4, 6)}
    aq3pow = {1: aq3}
    aq6pow = {1: aq6}

    # Nonzero terms of formula (3.15), after incorporating the outer f_1^-18.
    # Tuple: (integer coefficient, q-shift, a(q)-power, a(q^3)-power,
    #         a(q^6)-power, {d: exponent of f_d}).
    terms = [
        (1, 0, 6, 0, 1, {1:-18, 3:-6, 6:15, 12:-6}),
        (270, 1, 4, 0, 1, {1:-21, 2:2, 3:3, 4:-1, 6:9, 12:-3}),
        (7290, 2, 2, 0, 0, {1:-22, 2:-1, 3:6, 6:18, 12:-6}),
        (1080, 2, 3, 0, 0, {1:-20, 2:-1, 3:8, 4:1, 6:6, 12:-1}),
        (1080, 2, 3, 0, 0, {1:-22, 3:8, 4:1, 6:6, 9:2, 12:-1, 18:-1}),
        (1080, 2, 3, 0, 0, {1:-22, 2:1, 3:6, 4:-1, 6:12, 12:-3}),
        (14580, 3, 0, 0, 0, {1:-25, 2:1, 3:15, 4:-1, 6:12, 12:-3}),
        (29160, 3, 2, 0, 0, {1:-24, 2:3, 3:12, 6:2, 12:2}),
        (24, 3, 6, 0, 0, {1:-18, 3:-3, 6:5, 9:-1, 12:2, 18:2}),
        (29160, 4, 0, 0, 0, {1:-24, 2:2, 3:20, 4:-1, 6:-3, 12:5}),
        (13122, 4, 0, 0, 0, {1:-24, 3:16, 9:4, 18:5, 36:-2}),
        (29160, 4, 0, 0, 0, {1:-26, 2:3, 3:20, 4:-1, 6:-3, 9:2, 12:5, 18:-1}),
        (43740, 4, 1, 0, 0, {1:-24, 2:2, 3:12, 4:-1, 6:8, 12:-3, 18:3}),
        (8748, 4, 0, 1, 0, {1:-24, 3:16, 6:2, 9:4, 12:-1, 18:-1, 36:1}),
    ]

    total = np.zeros(N + 1, dtype=np.int64)
    for coefficient, shift, pa, pa3, pa6, exponents in terms:
        term = eta_quotient(exponents)
        if pa:
            term = mul(term, apow[pa])
        if pa3:
            term = mul(term, aq3pow[pa3])
        if pa6:
            term = mul(term, aq6pow[pa6])
        total = (total + shifted_scaled(term, coefficient, shift)) % MOD

    coeff = total.astype(np.uint8).tolist()
    csv_path = HERE / "source_formula_targets_mod16.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        wr = csv.writer(fh)
        wr.writerow(["progression", "n", "exponent", "residue_mod16"])
        for residue in (19, 25):
            for n in range(101):
                exponent = 30 * n + residue
                wr.writerow([residue, n, exponent, coeff[exponent]])

    raw = bytes(coeff)
    metadata = {
        "algorithm": "Das--Nath--Sarma exact formula (3.15)",
        "coefficient_range": [0, N],
        "arithmetic": "int64 polynomial convolution, canonical reduction modulo 16 after every product",
        "eta_expansion": "Euler pentagonal theorem; inverse via partition recurrence",
        "cubic_theta_expansion": "direct enumeration of m^2+mn+n^2",
        "retained_nonzero_terms_mod16": len(terms),
        "all_202_target_residues_zero": all(coeff[30*n+r] == 0 for r in (19, 25) for n in range(101)),
        "coefficient_vector_sha256": hashlib.sha256(raw).hexdigest(),
        "target_csv_sha256": hashlib.sha256(csv_path.read_bytes()).hexdigest(),
        "elapsed_seconds": round(time.time() - started, 3),
        "python": sys.version,
        "numpy": np.__version__,
        "platform": platform.platform(),
    }
    (HERE / "source_formula_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    (HERE / "source_formula_coefficients_mod16.bin").write_bytes(raw)
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
