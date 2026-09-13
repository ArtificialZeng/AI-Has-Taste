#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Serialize the recovered mixed d=6 and Gauss d=7 rational points."""

from fractions import Fraction
import json
from pathlib import Path

import numpy as np


def compositions(n: int):
    return [(a, b, c, n-a-b-c) for a in range(n+1)
            for b in range(n-a+1) for c in range(n-a-b+1)]


def variable_name(j: int, index) -> str:
    if j < 21:
        return f"A[{j}]"
    if j < 42:
        return f"B[{j-21}]"
    return "M[" + ",".join(map(str, index[j-42])) + "]"


def pair(q: Fraction):
    return [q.numerator, q.denominator]


def main() -> None:
    basis = np.load("evidence/mixed_d6_basis_rows.npz")
    support = [int(j) for j in basis["support"]]
    lines = Path("evidence/mixed_d6_basis_solution.txt").read_text().splitlines()
    values = [Fraction(s) for s in lines[1:]]
    if int(lines[0]) != len(support) or len(values) != len(support):
        raise RuntimeError("basis solution length mismatch")
    index = compositions(20)
    mixed = {
        "format": "mixed-d6-rational-point-v1",
        "parameters": {"n": 20, "k": 8, "d": 6},
        "variable_order": "A[0..20], B[0..20], then lexicographic (a,b,c,e) compositions of 20",
        "zero_convention": "Every variable not listed in nonzero_values is exactly zero.",
        "nonzero_values": [
            {"variable": j, "name": variable_name(j, index), "value": pair(q)}
            for j, q in zip(support, values)
        ],
        "counts": {"variables_total": 1813, "nonzero_values": len(values)},
    }
    Path("evidence/mixed_d6_rational_point.json").write_text(json.dumps(mixed, indent=2) + "\n")

    gauss_values = {
        0: 1, 7: 36, 8: 53, 9: 28, 10: 36, 11: 28, 12: 18,
        13: 36, 14: 20, 21: 1, 23: 1, 26: 84, 27: 203,
        28: 260, 29: 440, 30: 680, 31: 727, 32: 680, 33: 524,
        34: 260, 35: 125, 36: 84, 37: 27,
    }
    gauss = {
        "format": "gauss-d7-rational-point-v1",
        "parameters": {"n": 20, "k": 8, "d": 7},
        "branch": {"tau": "O", "beta": 0, "eta": 0, "dual_tau": "O"},
        "variable_order": "A[0..20], B[0..20]",
        "zero_convention": "Every variable not listed in nonzero_values is exactly zero.",
        "nonzero_values": [
            {"variable": j, "name": (f"A[{j}]" if j < 21 else f"B[{j-21}]"),
             "value": [v, 1]}
            for j, v in sorted(gauss_values.items())
        ],
        "counts": {"variables_total": 42, "nonzero_values": len(gauss_values)},
    }
    Path("evidence/gauss_d7_rational_point.json").write_text(json.dumps(gauss, indent=2) + "\n")
    print({"mixed_nonzero": len(values), "gauss_nonzero": len(gauss_values)})


if __name__ == "__main__":
    main()
