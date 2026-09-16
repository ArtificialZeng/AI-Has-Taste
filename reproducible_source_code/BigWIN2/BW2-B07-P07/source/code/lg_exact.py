#!/usr/bin/env python3
"""Exact Links--Gould evaluator for short braid words.

Discovery implementation.  Arithmetic is performed in

    Z[s0^+-1,s1^+-1,Y] / (Y^2 + (s0^2-1)(s1^2-1)).

The 16 by 16 R-matrix and quantum trace are the matrices printed in
Garoufalidis--Harper--Kashaev--Kohli--Song--Tahar (JLMS 2026), Appendix A,
and used independently in SageMath's braid implementation.  No floating
point arithmetic is used.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from typing import Dict, Iterable, List, Mapping, Sequence, Tuple


Monomial = Tuple[int, int, int]  # powers of s0, s1, Y; Y power is 0 or 1
Poly = Dict[Monomial, int]
Matrix = Dict[Tuple[int, int], Poly]


def clean(p: Mapping[Monomial, int]) -> Poly:
    return {m: int(c) for m, c in p.items() if c}


def const(c: int) -> Poly:
    return {} if c == 0 else {(0, 0, 0): c}


def monomial(a: int = 0, b: int = 0, y: int = 0, coeff: int = 1) -> Poly:
    if y not in (0, 1):
        raise ValueError("Y exponent must already be reduced")
    return {} if coeff == 0 else {(a, b, y): coeff}


ONE = const(1)
S0 = monomial(1, 0)
S1 = monomial(0, 1)
Y = monomial(0, 0, 1)
T0 = monomial(2, 0)
T1 = monomial(0, 2)
T0I = monomial(-2, 0)
T1I = monomial(0, -2)


def padd(*polys: Mapping[Monomial, int]) -> Poly:
    out: defaultdict[Monomial, int] = defaultdict(int)
    for p in polys:
        for m, c in p.items():
            out[m] += c
    return clean(out)


def pneg(p: Mapping[Monomial, int]) -> Poly:
    return {m: -c for m, c in p.items()}


def psub(p: Mapping[Monomial, int], q: Mapping[Monomial, int]) -> Poly:
    return padd(p, pneg(q))


def pscale(p: Mapping[Monomial, int], c: int) -> Poly:
    return clean({m: c * v for m, v in p.items()})


def pmul(p: Mapping[Monomial, int], q: Mapping[Monomial, int]) -> Poly:
    out: defaultdict[Monomial, int] = defaultdict(int)
    # Y^2 = -s0^2*s1^2 + s0^2 + s1^2 - 1.
    y2_terms = ((2, 2, -1), (2, 0, 1), (0, 2, 1), (0, 0, -1))
    for (a, b, y), c in p.items():
        for (aa, bb, yy), d in q.items():
            if y + yy < 2:
                out[(a + aa, b + bb, y + yy)] += c * d
            else:
                for da, db, e in y2_terms:
                    out[(a + aa + da, b + bb + db, 0)] += c * d * e
    return clean(out)


def ppow(p: Mapping[Monomial, int], n: int) -> Poly:
    if n < 0:
        raise ValueError("negative polynomial powers are not supported")
    out = ONE
    base = dict(p)
    while n:
        if n & 1:
            out = pmul(out, base)
        base = pmul(base, base)
        n //= 2
    return out


def midentity(n: int) -> Matrix:
    return {(i, i): ONE for i in range(n)}


def madd(*matrices: Mapping[Tuple[int, int], Poly]) -> Matrix:
    out: Dict[Tuple[int, int], Poly] = {}
    keys = set().union(*(m.keys() for m in matrices))
    for key in keys:
        value = padd(*(m.get(key, {}) for m in matrices))
        if value:
            out[key] = value
    return out


def mscale(a: Mapping[Tuple[int, int], Poly], p: Mapping[Monomial, int]) -> Matrix:
    return {ij: v for ij, q in a.items() if (v := pmul(p, q))}


def mmul(a: Mapping[Tuple[int, int], Poly],
         b: Mapping[Tuple[int, int], Poly]) -> Matrix:
    by_row: defaultdict[int, List[Tuple[int, Poly]]] = defaultdict(list)
    for (k, j), q in b.items():
        by_row[k].append((j, q))
    accum: defaultdict[Tuple[int, int], Poly] = defaultdict(dict)
    for (i, k), p in a.items():
        for j, q in by_row.get(k, ()):
            accum[(i, j)] = padd(accum[(i, j)], pmul(p, q))
    return {ij: p for ij, p in accum.items() if p}


def mtensor(a: Mapping[Tuple[int, int], Poly], na: int,
            b: Mapping[Tuple[int, int], Poly], nb: int) -> Matrix:
    out: Matrix = {}
    for (i, j), p in a.items():
        for (k, ell), q in b.items():
            value = pmul(p, q)
            if value:
                out[(i * nb + k, j * nb + ell)] = value
    return out


def r_matrix() -> Matrix:
    t0m1 = psub(T0, ONE)
    t1m1 = psub(T1, ONE)
    t0t1m1 = psub(pmul(T0, T1), ONE)
    ys0s1 = pmul(Y, pmul(S0, S1))
    r: Matrix = {
        (0, 0): T0, (1, 4): S0, (2, 8): S0, (3, 12): ONE,
        (4, 1): S0, (4, 4): t0m1, (5, 5): const(-1),
        (6, 6): t0t1m1, (6, 9): pneg(pmul(S0, S1)),
        (6, 12): pneg(ys0s1), (7, 13): S1,
        (8, 2): S0, (8, 8): t0m1,
        (9, 6): pneg(pmul(S0, S1)), (9, 12): Y,
        (10, 10): const(-1), (11, 14): S1,
        (12, 3): ONE, (12, 6): pneg(ys0s1), (12, 9): Y,
        (12, 12): pneg(pmul(t0m1, t1m1)),
        (13, 7): S1, (13, 13): t1m1,
        (14, 11): S1, (14, 14): t1m1, (15, 15): T1,
    }
    return {ij: clean(p) for ij, p in r.items() if p}


def r_inverse(r: Mapping[Tuple[int, int], Poly]) -> Matrix:
    # This is the inverse furnished by the cubic relation with eigenvalues
    # -1, t0, t1; expressing it this way avoids rational functions.
    ident = midentity(16)
    r2 = mmul(r, r)
    first = mscale(madd(ident, r), padd(T0I, T1I))
    second = mscale(madd(r, r2), pmul(T0I, T1I))
    return madd(first, mscale(second, const(-1)), mscale(ident, const(-1)))


def representation(n: int) -> Tuple[List[Tuple[Matrix, Matrix]], List[Poly]]:
    if n < 2:
        raise ValueError("at least two braid strands are required")
    r = r_matrix()
    ri = r_inverse(r)
    i4 = midentity(4)
    generators: List[Tuple[Matrix, Matrix]] = []
    for pos in range(n - 1):
        left_dim = 4 ** pos
        right_dim = 4 ** (n - pos - 2)
        g, gi, dim = r, ri, 16
        if left_dim > 1:
            g = mtensor(midentity(left_dim), left_dim, g, dim)
            gi = mtensor(midentity(left_dim), left_dim, gi, dim)
            dim *= left_dim
        if right_dim > 1:
            g = mtensor(g, dim, midentity(right_dim), right_dim)
            gi = mtensor(gi, dim, midentity(right_dim), right_dim)
        generators.append((g, gi))

    mu1 = [T0I, pneg(T1), pneg(T0I), T1]
    # The first tensor factor is the open strand in the modified trace, so
    # Sage/Marin use I tensor mu^(n-1), not mu^n.
    mu = [ONE, ONE, ONE, ONE]
    for _ in range(n - 1):
        mu = [pmul(x, y) for x in mu for y in mu1]
    return generators, mu


def braid_matrix(word: Sequence[int], n: int) -> Matrix:
    generators, _ = representation(n)
    out = midentity(4 ** n)
    for letter in word:
        if letter == 0 or abs(letter) >= n:
            raise ValueError(f"invalid B_{n} generator: {letter}")
        pair = generators[abs(letter) - 1]
        out = mmul(out, pair[0 if letter > 0 else 1])
    return out


def lg_s_polynomial(word: Sequence[int], n: int) -> Poly:
    generators, mu = representation(n)
    out = midentity(4 ** n)
    for letter in word:
        if letter == 0 or abs(letter) >= n:
            raise ValueError(f"invalid B_{n} generator: {letter}")
        pair = generators[abs(letter) - 1]
        out = mmul(out, pair[0 if letter > 0 else 1])

    # Partial quantum trace with the first tensor factor left open.  The
    # (0,0) entry is enough because the result is a scalar matrix.
    e = 4 ** (n - 1)
    answer: Poly = {}
    for k in range(e):
        row = k  # first base-4 digit is zero
        answer = padd(answer, pmul(mu[row], out.get((row, row), {})))
    return answer


def to_lg(poly: Mapping[Monomial, int]) -> Dict[Tuple[int, int], int]:
    out: defaultdict[Tuple[int, int], int] = defaultdict(int)
    for (a, b, y), c in poly.items():
        if y:
            raise ArithmeticError("the closed-braid invariant still contains Y")
        if a % 2 or b % 2:
            raise ArithmeticError("the closed-braid invariant has half-integral powers")
        out[(a // 2, b // 2)] += c
    return {ij: c for ij, c in out.items() if c}


def links_gould(word: Sequence[int], n: int | None = None) -> Dict[Tuple[int, int], int]:
    if n is None:
        n = max((abs(x) for x in word), default=1) + 1
    return to_lg(lg_s_polynomial(word, n))


def closure_components(word: Sequence[int], n: int) -> int:
    perm = list(range(n))
    for letter in word:
        i = abs(letter) - 1
        if i < 0 or i + 1 >= n:
            raise ValueError(f"invalid B_{n} generator: {letter}")
        perm[i], perm[i + 1] = perm[i + 1], perm[i]
    seen = set()
    cycles = 0
    for start in range(n):
        if start not in seen:
            cycles += 1
            j = start
            while j not in seen:
                seen.add(j)
                j = perm[j]
    return cycles


def parity_positive(poly: Mapping[Tuple[int, int], int]) -> bool:
    return all(((-1) ** (i + j)) * c >= 0 for (i, j), c in poly.items())


def format_laurent(poly: Mapping[Tuple[int, int], int]) -> str:
    if not poly:
        return "0"
    terms = []
    for (i, j), c in sorted(poly.items(), reverse=True):
        factors = []
        if i:
            factors.append("t0" if i == 1 else f"t0^{i}")
        if j:
            factors.append("t1" if j == 1 else f"t1^{j}")
        mon = "*".join(factors) or "1"
        terms.append(f"{c}*{mon}")
    return " + ".join(terms).replace("+ -", "- ")


def self_test() -> None:
    expected_unknot = {(0, 0): 1}
    assert links_gould([1], 2) == expected_unknot

    expected_figure_eight = {
        (1, 1): 2, (1, 0): -3, (1, -1): 1,
        (0, 1): -3, (0, 0): 7, (0, -1): -3,
        (-1, 1): 1, (-1, 0): -3, (-1, -1): 2,
    }
    got = links_gould([1, -2, 1, -2], 3)
    assert got == expected_figure_eight, (got, expected_figure_eight)
    assert closure_components([1, -2, 1, -2], 3) == 1
    assert parity_positive(got)

    # R*R^{-1}=I is checked entry-by-entry in the quotient ring.
    r = r_matrix()
    ri = r_inverse(r)
    assert mmul(r, ri) == midentity(16)
    assert mmul(ri, r) == midentity(16)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("word", nargs="*", type=int, help="signed braid generators")
    parser.add_argument("--strands", type=int)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("SELF_TEST_OK")
        return
    if not args.word:
        parser.error("provide a braid word or --self-test")
    n = args.strands or max(abs(x) for x in args.word) + 1
    poly = links_gould(args.word, n)
    payload = {
        "word": args.word,
        "strands": n,
        "closure_components": closure_components(args.word, n),
        "parity_positive": parity_positive(poly),
        "terms": [[i, j, c] for (i, j), c in sorted(poly.items())],
    }
    print(json.dumps(payload, sort_keys=True) if args.json else format_laurent(poly))


if __name__ == "__main__":
    main()
