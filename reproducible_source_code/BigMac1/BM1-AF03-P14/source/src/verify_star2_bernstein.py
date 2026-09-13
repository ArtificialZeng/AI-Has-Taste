#!/usr/bin/env python3
"""Fail-closed, no-project-import verifier for the Q5 star2 certificate."""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from pathlib import Path

import sympy as sp


TOP_KEYS = {
    "schema", "claim", "coordinate_order", "high_pairs", "normalization",
    "gaps", "domain", "critical_numerators", "direction_coefficients_xyzw",
    "bernstein", "chamber_margin_identities", "proof_assistants",
}
BERNSTEIN_KEYS = {
    "parameter_order", "P_degree", "P_coefficients", "H_degree",
    "H_coefficients", "canonical_tables_sha256",
}


def reject(message: str) -> int:
    print(f"REJECT: {message}", file=sys.stderr)
    return 1


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_booleans(value: object, path: str = "$") -> None:
    if type(value) is bool:
        raise ValueError(f"boolean forbidden in certificate at {path}")
    if type(value) is dict:
        for key, child in value.items():
            reject_booleans(child, f"{path}.{key}")
    elif type(value) is list:
        for index, child in enumerate(value):
            reject_booleans(child, f"{path}[{index}]")


def table(poly: sp.Expr, v: sp.Symbol, params: tuple[sp.Symbol, ...]):
    univar = sp.Poly(sp.expand(poly), v, domain=sp.QQ.frac_field(*params))
    degree = univar.degree()
    power = [sp.expand(univar.coeff_monomial(v**i)) for i in range(degree + 1)]
    rows = []
    reconstruction = 0
    for k in range(degree + 1):
        b = sp.expand(sum(
            sp.Rational(math.comb(k, i), math.comb(degree, i)) * power[i]
            for i in range(k + 1)
        ))
        bp = sp.Poly(b, *params, domain=sp.QQ)
        terms = []
        for monomial, value in bp.terms():
            value = sp.Rational(value)
            if value <= 0:
                raise ValueError(f"nonpositive Bernstein-monomial coefficient at k={k}")
            terms.append([*map(int, monomial), str(value.p), str(value.q)])
        if not terms or sp.Rational(bp.coeff_monomial(1)) <= 0:
            raise ValueError(f"strict positivity not certified at k={k}")
        rows.append({"k": k, "terms": terms})
        reconstruction += b * sp.binomial(degree, k) * v**k * (1 - v) ** (degree - k)
    if sp.expand(reconstruction - poly) != 0:
        raise ValueError("Bernstein identity failed")
    return degree, rows


def verify(payload: dict) -> None:
    reject_booleans(payload)
    if not isinstance(payload, dict) or set(payload) != TOP_KEYS:
        raise ValueError("wrong or incomplete top-level schema")
    if payload["schema"] != "q5-star2-bernstein-v1":
        raise ValueError("unexpected schema version")
    if payload["claim"] != "the ordered full-support star2 chamber closure has no critical direction":
        raise ValueError("unexpected claim")
    if payload["high_pairs"] != [[0, 1], [0, 2]]:
        raise ValueError("unexpected chamber graph")
    if payload["coordinate_order"] != ["a0", "a1", "a2", "a3", "a4"]:
        raise ValueError("unexpected coordinate order")
    if payload["normalization"] != {"a4": 1} or type(payload["normalization"]["a4"]) is not int:
        raise ValueError("unexpected normalization")
    if payload["direction_coefficients_xyzw"] != [-2, 2, -2, 1]:
        raise ValueError("unexpected derivative combination")
    if payload["critical_numerators"] != "Hq=S_q*P*D+2*S*P_q*D-2*S*P*D_q":
        raise ValueError("unexpected critical-numerator definition")
    if payload["domain"] != ["u>=0", "y>=0", "w>=0", "0<=v<=1"]:
        raise ValueError("unexpected domain")
    if payload["proof_assistants"] != []:
        raise ValueError("unexpected proof-assistant claim")
    expected_gaps = {
        "a0": "1+w+z+y+x", "a1": "1+w+z+y", "a2": "1+w+z",
        "a3": "1+w", "a4": "1", "x": "u+v", "z": "u+1-v",
    }
    if payload["gaps"] != expected_gaps:
        raise ValueError("unexpected gap chart")
    expected_margins = {
        "high_02": "x+z-1=2*u",
        "low_03": "1+z-x=2*(1-v)",
        "low_12": "1+x-z=2*v",
    }
    if payload["chamber_margin_identities"] != expected_margins:
        raise ValueError("unexpected chamber margins")
    bdata = payload["bernstein"]
    if not isinstance(bdata, dict) or set(bdata) != BERNSTEIN_KEYS:
        raise ValueError("wrong Bernstein schema")
    if bdata["parameter_order"] != ["u", "y", "w"]:
        raise ValueError("unexpected parameter order")

    # Independent reconstruction: this verifier imports no discovery/project module.
    a = sp.symbols("a0:5")
    x, y, z, w, u, v = sp.symbols("x y z w u v")
    T = sum(a) / 2
    S = sum(q * q for q in a)
    pairs = tuple(itertools.combinations(range(5), 2))
    high_pairs = ((0, 1), (0, 2))
    P = T**4 - sum((T - q) ** 4 for q in a)
    P += sum((T - a[i] - a[j]) ** 4 for i, j in pairs)
    P -= 2 * sum((T - a[i] - a[j]) ** 4 for i, j in high_pairs)
    gap_sub = {
        a[0]: 1 + w + z + y + x, a[1]: 1 + w + z + y,
        a[2]: 1 + w + z, a[3]: 1 + w, a[4]: 1,
    }
    Pg = sp.expand(P.subs(gap_sub))
    Sg = sp.expand(S.subs(gap_sub))
    Dg = sp.expand(sp.prod(a).subs(gap_sub))
    H = []
    for q in (x, y, z, w):
        H.append(sp.expand(
            sp.diff(Sg, q) * Pg * Dg
            + 2 * Sg * sp.diff(Pg, q) * Dg
            - 2 * Sg * Pg * sp.diff(Dg, q)
        ))
    combo = sp.expand((-2 * H[0] + 2 * H[1] - 2 * H[2] + H[3]).subs(
        {x: u + v, z: u + 1 - v}
    ))
    positive_P = sp.expand(Pg.subs({x: u + v, z: u + 1 - v}))
    p_degree, p_rows = table(positive_P, v, (u, y, w))
    h_degree, h_rows = table(combo, v, (u, y, w))
    if (p_degree, h_degree) != (4, 8):
        raise ValueError("unexpected exact degrees")
    if bdata["P_degree"] != p_degree or bdata["H_degree"] != h_degree:
        raise ValueError("claimed degrees mismatch")
    if bdata["P_coefficients"] != p_rows or bdata["H_coefficients"] != h_rows:
        raise ValueError("serialized coefficient table mismatch")
    canonical = json.dumps(
        {"P": p_rows, "H": h_rows}, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    digest = hashlib.sha256(canonical).hexdigest()
    if bdata["canonical_tables_sha256"] != digest:
        raise ValueError("coefficient-table digest mismatch")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(
            args.certificate.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_keys,
        )
        verify(payload)
    except Exception as exc:
        return reject(str(exc))
    print("PASS: star2 Bernstein positivity certificate verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
