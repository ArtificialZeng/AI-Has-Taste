#!/usr/bin/env python3
"""Independent exact audit of the key three-vertex C3 obstruction."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp


def main() -> int:
    a_p, a_q, a_r = sp.symbols("a_p a_q a_r")
    d_pq, d_qp, d_qr, d_rq = sp.symbols("d_pq d_qp d_qr d_rq")
    X = d_pq - a_q
    Y = a_p - d_qp
    Z = d_qr - a_r
    W = a_q - d_rq
    coefficient_matrix = sp.Matrix(
        [
            [X, -Y, 0],
            [0, Z, -W],
            [Z, 0, -Y],
        ]
    )
    determinant = sp.factor(coefficient_matrix.det())
    expected = sp.factor(Y * Z * (W - X))
    if sp.expand(determinant - expected) != 0:
        raise RuntimeError("C3 determinant factorization failed")
    obstruction = sp.factor(W - X)
    if obstruction != 2 * a_q - d_pq - d_rq:
        raise RuntimeError("unexpected generic obstruction")

    script_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(
        json.dumps(
            {
                "boundary_equation": str(obstruction),
                "determinant": str(determinant),
                "script_sha256": script_hash,
                "status": "VERIFIED",
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
