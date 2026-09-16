#!/usr/bin/env python3
"""Exact checks in Q[q]/(q^2+q+1) for the cubic B2 presentation.

This is a finite certificate for the displayed identities in
evidence/cubic_center_and_ozone.md, not a substitute for its PBW/filtration
argument.  Normal words are z^d t^c x^a y^b.
"""

from fractions import Fraction
from functools import lru_cache


class C:
    """a+b*q in Q[q]/(q^2+q+1)."""

    __slots__ = ("a", "b")

    def __init__(self, a=0, b=0):
        self.a, self.b = Fraction(a), Fraction(b)

    def __add__(self, other):
        other = as_c(other)
        return C(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return C(-self.a, -self.b)

    def __sub__(self, other):
        return self + (-as_c(other))

    def __rsub__(self, other):
        return as_c(other) - self

    def __mul__(self, other):
        other = as_c(other)
        # q^2=-q-1
        return C(
            self.a * other.a - self.b * other.b,
            self.a * other.b + self.b * other.a - self.b * other.b,
        )

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = as_c(other)
        # (a+bq)(a+bq^2)=a^2-ab+b^2
        norm = other.a * other.a - other.a * other.b + other.b * other.b
        if norm == 0:
            raise ZeroDivisionError
        return self * C((other.a - other.b) / norm, -other.b / norm)

    def __eq__(self, other):
        other = as_c(other)
        return self.a == other.a and self.b == other.b

    def __bool__(self):
        return bool(self.a or self.b)

    def __repr__(self):
        return f"C({self.a},{self.b})"


def as_c(value):
    return value if isinstance(value, C) else C(value)


ZERO, ONE, q = C(0), C(1), C(0, 1)
q2 = q * q

# Letters in desired PBW order z<t<x<y.
z, t, x, y = (0,), (1,), (2,), (3,)


def clean(poly):
    return {w: c for w, c in poly.items() if c}


def add(*polys):
    out = {}
    for poly in polys:
        for w, c in poly.items():
            out[w] = out.get(w, ZERO) + c
    return clean(out)


def scale(c, poly):
    return clean({w: as_c(c) * v for w, v in poly.items()})


@lru_cache(maxsize=None)
def reduce_word(word):
    """Reduce a word with the cubic Ore rules, choosing the leftmost inversion."""
    for i in range(len(word) - 1):
        a, b = word[i], word[i + 1]
        if a <= b:
            continue
        pre, post = word[:i], word[i + 2 :]
        if b == 0:  # z is central
            pieces = [(ONE, (b, a))]
        elif (a, b) == (2, 1):  # x t = q t x
            pieces = [(q, (1, 2))]
        elif (a, b) == (3, 1):  # y t = q^2 t y + z
            pieces = [(q2, (1, 3)), (ONE, (0,))]
        elif (a, b) == (3, 2):  # y x = q x y - q t
            pieces = [(q, (2, 3)), (-q, (1,))]
        else:
            raise AssertionError((a, b))
        return add(*(scale(c, reduce_word(pre + middle + post)) for c, middle in pieces))
    return {word: ONE}


def atom(word):
    return {word: ONE}


def mul(left, right):
    out = {}
    for u, cu in left.items():
        for v, cv in right.items():
            out = add(out, scale(cu * cv, reduce_word(u + v)))
    return out


def power(poly, n):
    out = {(): ONE}
    for _ in range(n):
        out = mul(out, poly)
    return out


def sub(left, right):
    return add(left, scale(-ONE, right))


def comm(left, right):
    return sub(mul(left, right), mul(right, left))


Z, T, X, Y = map(atom, (z, t, x, y))

# The two inverses are evaluated exactly in the quadratic coefficient field.
alpha = ONE / (q2 - ONE)
beta = ONE / (q * q * q * q - ONE)
S = add(mul(mul(X, Y), T), scale(alpha, mul(X, Z)), scale(beta, power(T, 2)))


def expect_zero(name, poly):
    if clean(poly):
        raise AssertionError(f"{name}: {poly}")


def expect_equal(name, left, right):
    expect_zero(name, sub(left, right))


def main():
    expect_equal("q^3", power({(): q}, 3), {(): ONE})
    expect_equal("root vector t", sub(mul(X, Y), scale(q2, mul(Y, X))), T)
    expect_equal("root vector z", sub(mul(Y, T), scale(q2, mul(T, Y))), Z)

    r1 = add(mul(power(X, 2), Y), mul(mul(X, Y), X), mul(Y, power(X, 2)))
    r2 = sub(mul(power(Y, 3), X), mul(X, power(Y, 3)))
    expect_zero("first specialized Serre relation", r1)
    expect_zero("second specialized Serre relation", r2)

    for name, central in (("x^3", power(X, 3)), ("y^3", power(Y, 3)),
                          ("t^3", power(T, 3)), ("z", Z), ("s", S)):
        for generator_name, generator in (("z", Z), ("t", T), ("x", X), ("y", Y)):
            expect_zero(f"[{name},{generator_name}]", comm(central, generator))

    # Exhaustively verify the congruence kernel used for gr(A) on a box.
    for a in range(10):
        for b in range(10):
            for c in range(10):
                equations = ((a + 2 * b) % 3 == 0 and
                             (b - c) % 3 == 0 and
                             (a - c) % 3 == 0)
                residues = a % 3 == b % 3 == c % 3
                if equations != residues:
                    raise AssertionError((a, b, c))

    print("PASS: exact cubic Serre, root-vector, and centrality identities")
    print("PASS: gr-center congruence criterion on 0<=a,b,c<10")
    print(f"alpha={alpha!r}, beta={beta!r}; normal form of z1={S}")


if __name__ == "__main__":
    main()
