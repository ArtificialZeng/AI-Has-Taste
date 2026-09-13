#!/usr/bin/env python3
"""Independent verifier using direct edge norms and projective pairs.

This file deliberately does not import the formula implementation used by the
certificate generator.
"""

from __future__ import annotations

import json
from math import gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "certificates" / "local_sieve.json").read_text(encoding="utf-8"))


def raw(r: int, s: int):
    u = r * r - 4 * r * s - s * s
    v = -2 * (r * r + r * s - s * s)
    w = r * r + s * s
    a = (u * u - w * w) * (v * v - w * w)
    b = 4 * u * v * w * w
    c = 2 * u * w * (v * v - w * w)
    return u, v, w, a, b, c


def norm(r: int, s: int) -> int:
    *_, a, b, c = raw(r, s)
    return a * a + b * b + c * c


def projective_representatives(p: int):
    return [(t, 1, t) for t in range(p)] + [(1, 0, "infinity")]


def main() -> None:
    for local in DATA["local_sieve"]:
        p = local["prime"]
        squares = {x * x % p for x in range(p)}
        observed = []
        for r, s, label in projective_representatives(p):
            value = norm(r, s) % p
            if value != 0 and value not in squares:
                observed.append(label)
        expected = list(local["bad_finite_slopes"])
        if local["infinity_bad"]:
            expected.append("infinity")
        assert observed == expected

    for item in DATA["exponent_one_classes_mod_169"]:
        residue = item["r_mod_169"]
        assert norm(residue, 1) % 169 == item["space_norm_mod_169"]
        *_, a, b, c = raw(residue, 1)
        assert [abs(a) % 13, abs(b) % 13, abs(c) % 13] == item["edges_mod_13"]

    # The progression singled out in the theorem gives genuine positive Euler
    # bricks, and 13 does not divide their common scale.
    for k in (0, 1, 2, 8, 31):
        r, s = 169 * k + 3, 1
        u, v, w, a0, b0, c0 = raw(r, s)
        a, b, c = abs(a0), abs(b0), abs(c0)
        assert u * u + v * v == 5 * w * w
        assert min(a, b, c) > 0
        q1 = abs(u**4 - 5 * u * u * w * w - 4 * w**4)
        q2 = abs((v * v - w * w) * (u * u + w * w))
        q3 = abs(2 * u * w * (v * v + w * w))
        assert (a * a + b * b, a * a + c * c, b * b + c * c) == (
            q1 * q1,
            q2 * q2,
            q3 * q3,
        )
        value = norm(r, s)
        assert value % 169 == 52
        assert value % 13 == 0 and value % 169 != 0
        common = gcd(gcd(a, b), c)
        assert common % 13 != 0

    print("independent verifier: PASS")


if __name__ == "__main__":
    main()
