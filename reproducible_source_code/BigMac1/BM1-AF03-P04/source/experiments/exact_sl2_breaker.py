#!/usr/bin/env python3
"""Exact counterexample hunt in a noncommutative rational Lie algebra.

The family is r+ = H tensor H + 4 E tensor F and
r- = -H tensor H - 4 F tensor E in sl_2, a denominator-cleared version of
the standard pair r and -tau(r).  All arithmetic is integral.  This script is
diagnostic negative evidence; the universal proof does not rely on it.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from collections import defaultdict
from pathlib import Path


H, E, F = range(3)
BRACKET = {
    (H, E): ((E, 2),),
    (E, H): ((E, -2),),
    (H, F): ((F, -2),),
    (F, H): ((F, 2),),
    (E, F): ((H, 1),),
    (F, E): ((H, -1),),
}
FAMILY = {
    "0": ((1, H, H), (4, E, F)),
    "1": ((-1, H, H), (-4, F, E)),
}


def tensor_residual(c: str, middle: str, c_double_prime: str):
    result: defaultdict[tuple[int, int, int], int] = defaultdict(int)
    for alpha, a, b in FAMILY[c]:
        for beta, d, e in FAMILY[middle]:
            for basis, coefficient in BRACKET.get((a, d), ()):
                result[(basis, b, e)] += alpha * beta * coefficient
    for alpha, a, b in FAMILY[c]:
        for beta, d, e in FAMILY[c_double_prime]:
            for basis, coefficient in BRACKET.get((b, d), ()):
                result[(a, basis, e)] += alpha * beta * coefficient
    for alpha, a, b in FAMILY[middle]:
        for beta, d, e in FAMILY[c_double_prime]:
            for basis, coefficient in BRACKET.get((b, e), ()):
                result[(a, d, basis)] += alpha * beta * coefficient
    return {key: value for key, value in result.items() if value}


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: exact_sl2_breaker.py CERTIFICATE.json", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    raw = path.read_bytes()
    data = json.loads(raw)

    relation_checks = 0
    for c, middle, c_double_prime in itertools.product("01", repeat=3):
        if middle in (c, c_double_prime):
            relation_checks += 1
            if tensor_residual(c, middle, c_double_prime):
                raise AssertionError("the exact sl2 family fails transitive CYBE")

    arrays = [
        array
        for array in data["n_values"]["5"]["arrays"]
        if set(array) <= {"0", "1"}
    ]
    component_checks = 0
    for array in arrays:
        for j, i, k in itertools.product(range(5), repeat=3):
            c = array[i * 5 + j]
            middle = array[k * 5 + j]
            c_double_prime = array[k * 5 + i]
            component_checks += 1
            if tensor_residual(c, middle, c_double_prime):
                raise AssertionError(
                    f"counterexample found: array={array}, component={(j, i, k)}"
                )

    print(
        "NO_COUNTEREXAMPLE_IN_EXACT_SL2_STRATUM "
        f"arrays={len(arrays)} relation_checks={relation_checks} "
        f"component_checks={component_checks} "
        f"input_sha256={hashlib.sha256(raw).hexdigest()} "
        f"script_sha256={hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
