"""Fresh standard-library checks for the frozen covariance candidate.

This deliberately does not import or invoke the proposer's SymPy verifier.
It checks the frozen snapshot, the two independent forms of xi_2 as exact
truncated formal series, the general claimed coefficient formula over a broad
exact range, and the rational certificate used at (p,q)=(1,200).
"""

from fractions import Fraction
from hashlib import sha256
from math import factorial
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT = ROOT / "audit" / "snapshot.json"


def check_snapshot() -> None:
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    actual = {
        name: sha256((ROOT / name).read_bytes()).hexdigest()
        for name in snapshot["files"]
    }
    assert actual == snapshot["files"]
    canonical = json.dumps(
        actual, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    assert sha256(canonical).hexdigest() == snapshot["digest"]


DEGREE = 80
ZERO = [Fraction(0) for _ in range(DEGREE + 1)]


def add(*series):
    return [sum((a[n] for a in series), Fraction(0)) for n in range(DEGREE + 1)]


def scale(a, scalar):
    scalar = Fraction(scalar)
    return [scalar * value for value in a]


def shift(a, amount):
    out = ZERO.copy()
    for n in range(amount, DEGREE + 1):
        out[n] = a[n - amount]
    return out


def multiply(a, b):
    out = ZERO.copy()
    for n in range(DEGREE + 1):
        out[n] = sum((a[k] * b[n - k] for k in range(n + 1)), Fraction(0))
    return out


def hyperbolic_series(argument_scale, odd):
    out = ZERO.copy()
    parity = 1 if odd else 0
    for n in range(parity, DEGREE + 1, 2):
        out[n] = Fraction(argument_scale**n, factorial(n))
    return out


def monomial(degree, coefficient=1):
    out = ZERO.copy()
    out[degree] = Fraction(coefficient)
    return out


def check_xi2_series() -> None:
    sinh_x = hyperbolic_series(1, odd=True)
    cosh_x = hyperbolic_series(1, odd=False)
    sinh_2x = hyperbolic_series(2, odd=True)
    cosh_2x = hyperbolic_series(2, odd=False)

    # A=x cosh(x)-sinh(x), and xi_2=2x^3(x-sinh(x)cosh(x))+12A^2.
    A = add(shift(cosh_x, 1), scale(sinh_x, -1))
    compact = add(
        monomial(4, 2),
        scale(shift(multiply(sinh_x, cosh_x), 3), -2),
        scale(multiply(A, A), 12),
    )

    # Printed Appendix-F form transcribed in the frozen problem.
    printed = add(
        monomial(4, 2),
        monomial(2, 6),
        scale(shift(sinh_2x, 3), -1),
        scale(shift(sinh_2x, 1), -12),
        scale(shift(cosh_2x, 2), 6),
        scale(cosh_2x, 6),
        monomial(0, -6),
    )
    assert compact == printed

    for degree, coefficient in enumerate(compact):
        if degree % 2:
            assert coefficient == 0
            continue
        n = degree // 2
        expected = Fraction(0)
        if n >= 5:
            expected = -Fraction(
                2 ** (2 * n - 3)
                * (2 * n - 1)
                * (2 * n - 6)
                * (2 * n - 8),
                factorial(2 * n),
            )
        assert coefficient == expected

    # The coefficient-polynomial factorization is an identity, not a sample.
    # Expanding both sides gives -m^3+15m^2-62m+48.
    for m in range(-10, 101):
        left = -m * (m - 1) * (m - 2) - 48 * m + 12 * m * (m - 1) + 48
        right = -(m - 1) * (m - 6) * (m - 8)
        assert left == right


def check_counterexample_certificate() -> None:
    partial = sum((Fraction(2**n, factorial(n)) for n in range(12)), Fraction(0))
    lower = Fraction(7389, 1000)
    assert partial == Fraction(164591, 22275)
    assert partial - lower == Fraction(41, 891000)
    assert lower > 2
    f_lower = lower**2 - 4 * lower - 25
    assert f_lower == Fraction(41321, 1_000_000)
    assert f_lower > Fraction(1, 25)
    # Together with the positive-tail series e^2 > partial and monotonicity of
    # y^2-4y-25 for y>2, this makes 8-200 f(e^2) strictly negative.


if __name__ == "__main__":
    check_snapshot()
    check_xi2_series()
    check_counterexample_certificate()
    print("fresh exact snapshot, series, and rational-certificate checks passed")
