#!/usr/bin/env python3
"""Emit exact Q5 chamber critical systems for external CAS checking.

Unlike the floating-point discovery program, every coefficient emitted here is
an integer reconstructed from the chamber name.  The current command prints a
Singular program to stdout; it does not consume numerical roots.
"""

from __future__ import annotations

import argparse
import itertools
import sys

import sympy as sp


CHAMBERS = {
    "empty": (),
    "star1": ((0, 1),),
    "star2": ((0, 1), (0, 2)),
    "star3": ((0, 1), (0, 2), (0, 3)),
    "star4": ((0, 1), (0, 2), (0, 3), (0, 4)),
    "triangle": ((0, 1), (0, 2), (1, 2)),
}


def exact_system(name: str, normalization: str = "min1", equations: str = "direct"):
    a = sp.symbols("a0:5")
    s = sum(z * z for z in a)
    t = sum(a) / 2
    p = t**4 - sum((t - z) ** 4 for z in a)
    p += sum((t - a[i] - a[j]) ** 4 for i, j in itertools.combinations(range(5), 2))
    p -= 2 * sum((t - a[i] - a[j]) ** 4 for i, j in CHAMBERS[name])
    p = sp.cancel(sp.expand(p))
    g = [sp.cancel(sp.expand(a[i] * s * sp.diff(p, a[i]) + (a[i] ** 2 - s) * p))
         for i in range(5)]
    if normalization == "min1":
        sub = {a[4]: 1}
    elif normalization == "sum2":
        # Compact projective chart: sum(a_i)=2, hence T=1 and
        # a4=2-a0-a1-a2-a3.  The identity sum_i G_i=0 makes G0..G3
        # equivalent to the full critical system.
        sub = {a[4]: 2 - sum(a[:4])}
    else:
        raise ValueError(normalization)
    p4 = sp.Poly(sp.expand(p.subs(sub)), *a[:4], domain=sp.QQ)
    nonzero_expr = sp.expand(sp.prod(a).subs(sub) * p.subs(sub) * s.subs(sub))
    if equations == "direct":
        eq_exprs = [sp.expand(z.subs(sub)) for z in g[:4]]
    elif equations == "affine" and normalization == "sum2":
        p_sub_expr = sp.expand(p.subs(sub))
        s_sub_expr = sp.expand(s.subs(sub))
        a4_expr = sp.expand(a[4].subs(sub))
        eq_exprs = [
            sp.expand(
                (a[i] - a4_expr) * p_sub_expr * (a[i] * a4_expr + s_sub_expr)
                + s_sub_expr * a[i] * a4_expr * sp.diff(p_sub_expr, a[i])
            )
            for i in range(4)
        ]
    elif equations == "reduced" and normalization == "sum2":
        p_sub_expr = sp.expand(p.subs(sub))
        s_sub_expr = sp.expand(s.subs(sub))
        prod_sub_expr = sp.expand(sp.prod(a).subs(sub))
        reduced = sp.cancel(p_sub_expr / prod_sub_expr)
        num, den = map(sp.expand, sp.fraction(reduced))
        eq_exprs = [
            sp.expand(
                sp.diff(s_sub_expr, a[i]) * num * den
                + 2 * s_sub_expr * sp.diff(num, a[i]) * den
                - 2 * s_sub_expr * num * sp.diff(den, a[i])
            )
            for i in range(4)
        ]
        # Retain the full coordinate product in the saturation even after
        # cancellation.  Otherwise the reduced equations acquire complex
        # coordinate-divisor components that are irrelevant to the positive
        # full-support chamber but inflate the algebraic degree.
        nonzero_expr = sp.expand(num * den * s_sub_expr * prod_sub_expr)
    else:
        raise ValueError("affine/reduced equations require the sum2 normalization")
    g4 = [sp.Poly(z, *a[:4], domain=sp.QQ) for z in eq_exprs]
    # Clear the common denominator introduced by T=(sum a_i)/2.
    den = sp.ilcm(*[term.denominator for poly in [p4, *g4] for _, term in poly.terms()])
    p4 = sp.Poly(sp.expand(p4.as_expr() * den), *a[:4], domain=sp.ZZ)
    g4 = [sp.Poly(sp.expand(poly.as_expr() * den), *a[:4], domain=sp.ZZ) for poly in g4]
    common = 0
    for poly in [p4, *g4]:
        common = sp.igcd(common, int(sp.gcd_list(poly.coeffs())))
    if common > 1:
        p4 = sp.Poly(p4.as_expr() / common, *a[:4], domain=sp.ZZ)
        g4 = [sp.Poly(poly.as_expr() / common, *a[:4], domain=sp.ZZ) for poly in g4]
    s4 = sp.Poly(sp.expand(s.subs(sub)), *a[:4], domain=sp.ZZ)
    a4 = sp.Poly(sp.expand(a[4].subs(sub)), *a[:4], domain=sp.ZZ)
    nonzero = sp.Poly(nonzero_expr, *a[:4], domain=sp.QQ)
    return a[:4], p4, g4, s4, a4, nonzero


def singular_expr(expr: sp.Expr) -> str:
    return str(expr).replace("**", "^")


def emit_singular(name: str, action: str, normalization: str, equations: str) -> None:
    a, p, g, s, a4, nonzero = exact_system(name, normalization, equations)
    names = ",".join(map(str, a))
    print(f"ring r=0,({names}),dp;")
    print(f"poly P={singular_expr(p.as_expr())};")
    print(f"poly S={singular_expr(s.as_expr())};")
    print(f"poly A4={singular_expr(a4.as_expr())};")
    print(f"poly Nonzero={singular_expr(nonzero.as_expr())};")
    for i, poly in enumerate(g):
        print(f"poly g{i}={singular_expr(poly.as_expr())};")
    print("ideal I=g0,g1,g2,g3;")
    if action in ("stats", "basis"):
        print('print("CHAMBER %s NORMALIZATION %s EQUATIONS %s");' % (name, normalization, equations))
        print('LIB "elim.lib";')
        print("ideal Q=sat(I,Nonzero);")
        print("ideal J=std(Q);")
        print('print("DIM"); print(dim(J));')
        print('print("VDIM"); print(vdim(J));')
        print('print("BASIS_SIZE"); print(size(J));')
        if action == "basis":
            print('print("BASIS"); print(J);')
    elif action == "lex":
        print('print("CHAMBER %s NORMALIZATION %s EQUATIONS %s");' % (name, normalization, equations))
        print('LIB "elim.lib";')
        print("ideal Q=sat(I,Nonzero);")
        print("ideal J=std(Q);")
        print("ring s=0,(a0,a1,a2,a3),lp;")
        print("ideal K=imap(r,J);")
        print("ideal L=std(K);")
        print('print("LEX_BASIS"); print(L);')
    elif action == "factor":
        print('print("CHAMBER %s NORMALIZATION %s EQUATIONS %s");' % (name, normalization, equations))
        for i in range(4):
            print(f'print("G{i}_FACTORS"); print(factorize(g{i}));')
            for j in range(i + 1, 4):
                print(f'print("G{i}-G{j}_FACTORS"); print(factorize(g{i}-g{j}));')
    else:
        raise ValueError(action)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("chamber", choices=sorted(CHAMBERS))
    ap.add_argument("--action", choices=("stats", "basis", "lex", "factor"), default="stats")
    ap.add_argument("--normalization", choices=("min1", "sum2"), default="min1")
    ap.add_argument("--equations", choices=("direct", "affine", "reduced"), default="direct")
    args = ap.parse_args()
    emit_singular(args.chamber, args.action, args.normalization, args.equations)
    return 0


if __name__ == "__main__":
    sys.exit(main())
