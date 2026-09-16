#!/usr/bin/env python3
"""Exact finite-field cross-check of the proof's character-sum identities.

This is finite verification, not the all-m proof.  Arithmetic and irreducible
moduli come from the earlier package-free verifier in the same directory.
"""

import importlib.util
from pathlib import Path


HELPER = Path(__file__).with_name("verify_subfield_distribution.py")
SPEC = importlib.util.spec_from_file_location("finite_field_helper", HELPER)
FF = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(FF)


def verify(m, c_two_back, c_one_back):
    q = 1 << m
    modulus = FF.first_irreducible(m)

    def inv(x):
        return FF.power(x, q - 2, modulus, m)

    def trace(x):
        return FF.absolute_trace(x, modulus, m)

    def chi(x):
        return 1 if trace(x) == 0 else -1

    sigma = 0
    indicator_count = 0
    direct_count = 0
    for t in range(q):
        if t in (0, 1):
            continue
        t_plus_one = t ^ 1
        a_trace_argument = t ^ inv(t_plus_one)
        b_trace_argument = 1 ^ inv(t) ^ inv(t_plus_one)
        sigma += chi(b_trace_argument)
        indicator_count += (
            (1 - chi(a_trace_argument)) * (1 - chi(b_trace_argument)) // 4
        )

        h = FF.square(t, modulus, m) ^ t ^ 1
        if h != 0:
            y = FF.multiply(t_plus_one, inv(h), modulus, m)
            z = FF.multiply(t, y, modulus, m)
            if trace(inv(y)) == 1 and trace(inv(z)) == 1:
                direct_count += 1

    if m == 1:
        c = 1
    elif m == 2:
        c = -3
    else:
        c = c_one_back - 2 * c_two_back

    expected_sigma = -((-1) ** m) - c
    expected_d = (q - 2 + (-1) ** m + c) // 4
    infinity_fibre = 1 + (-1) ** m
    curve_points = q - 2 + sigma + 2 + infinity_fibre

    assert sigma == expected_sigma
    assert indicator_count == direct_count == expected_d
    assert curve_points == q + 1 - c
    print(
        f"m={m:2d} modulus=0x{modulus:x} sigma={sigma:6d} "
        f"D={direct_count:6d} #E={curve_points:6d} OK"
    )
    return c


def main():
    c_values = []
    for m in range(1, 16):
        c = verify(
            m,
            c_values[-2] if len(c_values) >= 2 else None,
            c_values[-1] if c_values else None,
        )
        c_values.append(c)


if __name__ == "__main__":
    main()
