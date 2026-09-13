#!/usr/bin/env python3
"""Emit an exact Singular computation for the corrected star4 chamber.

Discovery/exactification helper only.  The final certificate is checked by a
separate verifier that does not import this file or trust its output.
"""

from __future__ import annotations

import argparse
import itertools

import sympy as sp


def system():
    a = sp.symbols("a0:5")
    half_sum = sum(a) / 2
    norm_square = sum(x * x for x in a)
    high_pairs = {(0, j) for j in range(1, 5)}
    numerator = half_sum**4 - sum((half_sum - x) ** 4 for x in a)
    for pair in itertools.combinations(range(5), 2):
        sign = -1 if pair in high_pairs else 1
        numerator += sign * (half_sum - a[pair[0]] - a[pair[1]]) ** 4
    numerator = sp.expand(numerator)
    critical = [
        sp.expand(a[i] * norm_square * sp.diff(numerator, a[i]) + (a[i] ** 2 - norm_square) * numerator)
        for i in range(4)
    ]
    substitute = {a[4]: 1}
    polys = [sp.Poly(expr.subs(substitute), *a[:4], domain=sp.QQ) for expr in [numerator, *critical]]
    denominator = sp.ilcm(*[coefficient.denominator for poly in polys for coefficient in poly.coeffs()])
    polys = [sp.Poly(sp.expand(poly.as_expr() * denominator), *a[:4], domain=sp.ZZ) for poly in polys]
    content = sp.igcd(*[int(sp.gcd_list(poly.coeffs())) for poly in polys])
    polys = [sp.Poly(poly.as_expr() / content, *a[:4], domain=sp.ZZ) for poly in polys]
    P, *g = polys
    S = sp.Poly(1 + sum(x * x for x in a[:4]), *a[:4], domain=sp.ZZ)
    return a[:4], P, g, S


def singular(expression: sp.Expr) -> str:
    return str(expression).replace("**", "^")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--action", choices=("stats", "basis", "lex"), default="stats")
    args = parser.parse_args()
    variables, P, critical, S = system()
    names = ",".join(map(str, variables))
    print(f"ring r=0,({names}),dp;")
    print(f"poly P={singular(P.as_expr())};")
    print(f"poly S={singular(S.as_expr())};")
    for index, polynomial in enumerate(critical):
        print(f"poly g{index}={singular(polynomial.as_expr())};")
    print("ideal I=g0,g1,g2,g3;")
    print('LIB "elim.lib";')
    print("ideal Nonzero=a0*a1*a2*a3*P*S;")
    print("ideal Q=sat(I,Nonzero);")
    print("ideal J=std(Q);")
    print('print("DIM"); print(dim(J));')
    print('print("VDIM"); print(vdim(J));')
    if args.action in ("basis", "lex"):
        print('print("DP_BASIS"); print(J);')
    if args.action == "lex":
        print(f"ring target=0,({names}),lp;")
        print("ideal L=fglm(r,J);")
        print('print("LEX_BASIS"); print(L);')
    print("exit;")


if __name__ == "__main__":
    main()
