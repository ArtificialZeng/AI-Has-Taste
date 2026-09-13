#!/usr/bin/env python3
"""Build the exact Bernstein positivity certificate for the ordered star2 chamber."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path

import sympy as sp


def rat_text(q: sp.Rational) -> tuple[str, str]:
    q = sp.Rational(q)
    return str(q.p), str(q.q)


def bernstein_table(poly: sp.Expr, v: sp.Symbol, params: tuple[sp.Symbol, ...]):
    univar = sp.Poly(sp.expand(poly), v, domain=sp.QQ.frac_field(*params))
    degree = univar.degree()
    power = [sp.expand(univar.coeff_monomial(v**i)) for i in range(degree + 1)]
    rows = []
    reconstructed = 0
    for k in range(degree + 1):
        coeff = sp.expand(sum(
            sp.Rational(math.comb(k, i), math.comb(degree, i)) * power[i]
            for i in range(k + 1)
        ))
        coeff_poly = sp.Poly(coeff, *params, domain=sp.QQ)
        terms = []
        for monomial, value in coeff_poly.terms():
            num, den = rat_text(value)
            terms.append([*map(int, monomial), num, den])
        rows.append({"k": k, "terms": terms})
        reconstructed += coeff * sp.binomial(degree, k) * v**k * (1 - v) ** (degree - k)
    if sp.expand(reconstructed - poly) != 0:
        raise RuntimeError("internal Bernstein reconstruction failure")
    return degree, rows


def build_payload() -> dict:
    a = sp.symbols("a0:5")
    x, y, z, w, u, v = sp.symbols("x y z w u v")
    total = sum(a)
    T = total / 2
    S = sum(q * q for q in a)
    high_pairs = ((0, 1), (0, 2))
    pairs = tuple(itertools.combinations(range(5), 2))
    P = T**4 - sum((T - q) ** 4 for q in a)
    P += sum((T - a[i] - a[j]) ** 4 for i, j in pairs)
    P -= 2 * sum((T - a[i] - a[j]) ** 4 for i, j in high_pairs)
    P = sp.expand(P)

    gap_sub = {
        a[0]: 1 + w + z + y + x,
        a[1]: 1 + w + z + y,
        a[2]: 1 + w + z,
        a[3]: 1 + w,
        a[4]: 1,
    }
    Pg = sp.expand(P.subs(gap_sub))
    Sg = sp.expand(S.subs(gap_sub))
    Dg = sp.expand(sp.prod(a).subs(gap_sub))
    variables = (x, y, z, w)
    H = []
    for q in variables:
        H.append(sp.expand(
            sp.diff(Sg, q) * Pg * Dg
            + 2 * Sg * sp.diff(Pg, q) * Dg
            - 2 * Sg * Pg * sp.diff(Dg, q)
        ))
    direction = (-2, 2, -2, 1)
    combo = sp.expand(sum(c * h for c, h in zip(direction, H)))
    chamber_sub = {x: u + v, z: u + 1 - v}
    combo = sp.expand(combo.subs(chamber_sub))
    positive_P = sp.expand(Pg.subs(chamber_sub))

    p_degree, p_table = bernstein_table(positive_P, v, (u, y, w))
    h_degree, h_table = bernstein_table(combo, v, (u, y, w))
    canonical = json.dumps(
        {"P": p_table, "H": h_table}, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return {
        "schema": "q5-star2-bernstein-v1",
        "claim": "the ordered full-support star2 chamber closure has no critical direction",
        "coordinate_order": ["a0", "a1", "a2", "a3", "a4"],
        "high_pairs": [[0, 1], [0, 2]],
        "normalization": {"a4": 1},
        "gaps": {
            "a0": "1+w+z+y+x",
            "a1": "1+w+z+y",
            "a2": "1+w+z",
            "a3": "1+w",
            "a4": "1",
            "x": "u+v",
            "z": "u+1-v",
        },
        "domain": ["u>=0", "y>=0", "w>=0", "0<=v<=1"],
        "critical_numerators": "Hq=S_q*P*D+2*S*P_q*D-2*S*P*D_q",
        "direction_coefficients_xyzw": list(direction),
        "bernstein": {
            "parameter_order": ["u", "y", "w"],
            "P_degree": p_degree,
            "P_coefficients": p_table,
            "H_degree": h_degree,
            "H_coefficients": h_table,
            "canonical_tables_sha256": hashlib.sha256(canonical).hexdigest(),
        },
        "chamber_margin_identities": {
            "high_02": "x+z-1=2*u",
            "low_03": "1+z-x=2*(1-v)",
            "low_12": "1+x-z=2*v",
        },
        "proof_assistants": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    payload = build_payload()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
