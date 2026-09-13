"""Exact arithmetic for a Lenhart-attributed family of Euler bricks.

All functions use Python integers only.  The signs of the displayed edge
formulae are immaterial, so ``edges`` returns positive lengths.
"""

from __future__ import annotations

from typing import List, Tuple


def parameters(r: int, s: int) -> Tuple[int, int, int]:
    """Return (u,v,w) with u^2+v^2=5w^2."""
    u = r * r - 4 * r * s - s * s
    v = -2 * (r * r + r * s - s * s)
    w = r * r + s * s
    return u, v, w


def signed_edges(r: int, s: int) -> Tuple[int, int, int]:
    u, v, w = parameters(r, s)
    return (
        (u * u - w * w) * (v * v - w * w),
        4 * u * v * w * w,
        2 * u * w * (v * v - w * w),
    )


def edges(r: int, s: int) -> Tuple[int, int, int]:
    return tuple(abs(x) for x in signed_edges(r, s))


def face_diagonals(r: int, s: int) -> Tuple[int, int, int]:
    """Return the three positive face diagonals in edge order AB, AC, BC."""
    u, v, w = parameters(r, s)
    return (
        abs(u**4 - 5 * u * u * w * w - 4 * w**4),
        abs((v * v - w * w) * (u * u + w * w)),
        abs(2 * u * w * (v * v + w * w)),
    )


def direct_space_norm(r: int, s: int) -> int:
    a, b, c = signed_edges(r, s)
    return a * a + b * b + c * c


def factored_space_norm(r: int, s: int) -> int:
    u, _, w = parameters(r, s)
    return (u * u + 4 * w * w) * (
        u**6 - 10 * u**4 * w * w + 25 * u * u * w**4 + 4 * w**6
    )


def quadratic_residues(p: int) -> set[int]:
    return {x * x % p for x in range(p)}


def bad_projective_slopes(p: int) -> Tuple[List[int], bool]:
    """Return bad finite slopes t=r/s and whether infinity [1:0] is bad."""
    squares = quadratic_residues(p)
    finite: List[int] = []
    for t in range(p):
        value = factored_space_norm(t, 1) % p
        if value != 0 and value not in squares:
            finite.append(t)
    infinity_value = factored_space_norm(1, 0) % p
    infinity_bad = infinity_value != 0 and infinity_value not in squares
    return finite, infinity_bad


def valuation(n: int, p: int) -> int:
    if n == 0:
        raise ValueError("the p-adic valuation of zero is not used here")
    n = abs(n)
    exponent = 0
    while n % p == 0:
        exponent += 1
        n //= p
    return exponent


def all_face_identities(r: int, s: int) -> bool:
    a, b, c = edges(r, s)
    x, y, z = face_diagonals(r, s)
    return a * a + b * b == x * x and a * a + c * c == y * y and b * b + c * c == z * z
