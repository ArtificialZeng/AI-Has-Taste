#!/usr/bin/env python3
"""Independent exact sparse-Laurent checks for the low-degree referee audit.

No project proof code or CAS is imported.  Conjugate symbols are independent,
and conjugation swaps d/D, b/B, c/C and sends q to q^{-1}.
"""

import argparse
from fractions import Fraction


VARS = ("q", "d", "D", "b", "B", "c", "C", "r")
N = len(VARS)


class E:
    def __init__(self, terms=None):
        self.t = {m: Fraction(v) for m, v in (terms or {}).items() if v}

    @staticmethod
    def one(value=1):
        return E({(0,) * N: Fraction(value)})

    @staticmethod
    def var(name, power=1):
        m = [0] * N
        m[VARS.index(name)] = power
        return E({tuple(m): Fraction(1)})

    def __add__(self, other):
        other = as_e(other)
        out = dict(self.t)
        for m, v in other.t.items():
            out[m] = out.get(m, 0) + v
            if not out[m]:
                del out[m]
        return E(out)

    __radd__ = __add__

    def __neg__(self):
        return E({m: -v for m, v in self.t.items()})

    def __sub__(self, other):
        return self + (-as_e(other))

    def __rsub__(self, other):
        return as_e(other) - self

    def __mul__(self, other):
        other = as_e(other)
        out = {}
        for m, a in self.t.items():
            for n, b in other.t.items():
                k = tuple(x + y for x, y in zip(m, n))
                out[k] = out.get(k, 0) + a * b
        return E(out)

    __rmul__ = __mul__

    def __pow__(self, power):
        if power < 0:
            if len(self.t) != 1:
                raise ValueError("negative powers only supported for monomials")
            (m, a), = self.t.items()
            return E({tuple(power * x for x in m): a ** power})
        out = E.one()
        for _ in range(power):
            out *= self
        return out

    def __eq__(self, other):
        return self.t == as_e(other).t

    def __repr__(self):
        return repr(self.t)


def as_e(value):
    return value if isinstance(value, E) else E.one(value)


q, d, D, b, B, c, C, r = (E.var(v) for v in VARS)


def conj(f):
    out = {}
    iq, id_, iD, ib, iB, ic, iC, ir = range(N)
    for m, a in f.t.items():
        n = list(m)
        n[iq] = -m[iq]
        n[id_], n[iD] = m[iD], m[id_]
        n[ib], n[iB] = m[iB], m[ib]
        n[ic], n[iC] = m[iC], m[ic]
        n[ir] = m[ir]
        out[tuple(n)] = out.get(tuple(n), 0) + a
    return E(out)


def poly_scale(scalar, p):
    return [scalar * x for x in p]


def poly_sub(p, q_):
    length = max(len(p), len(q_))
    return [
        (p[i] if i < len(p) else E()) - (q_[i] if i < len(q_) else E())
        for i in range(length)
    ]


def schur(h):
    """Return (conj(h_m) H - h_0 H#)/y as coefficient list."""
    hs = [conj(x) for x in reversed(h)]
    numerator = poly_sub(poly_scale(conj(h[-1]), h), poly_scale(h[0], hs))
    check(numerator[0] == 0, "Schur numerator has nonzero constant term")
    return numerator[1:]


def fail(message):
    """Terminate verification explicitly; never disabled by ``python -O``."""
    raise SystemExit(f"VERIFICATION FAILED: {message}")


def check(condition, message):
    if not condition:
        fail(message)


def check_poly_equal(actual, expected, label):
    check(len(actual) == len(expected), f"{label}: coefficient-length mismatch")
    for i, (x, y) in enumerate(zip(actual, expected)):
        check(x == y, f"{label}: coefficient {i}, residual {x - y}")
    print("PASS", label)


def degree_three():
    z = q
    p = D + z + z**2 + d * z**3
    h = [d, d * z + 1, d * z**2 + z + 1]
    expected = poly_scale(p * z**-2, [E.one(), 1 + z])
    check_poly_equal(schur(h), expected, "(3.3) first Schur identity")

    derivative = [E.one(), E.one(2), 3 * d]
    check_poly_equal(
        schur(derivative),
        [6 * D - 2, 9 * d * D - 1],
        "(3.8) derivative Schur coefficients",
    )

    # Use z=q^2 to eliminate half powers.  Verify the asserted real part and
    # that the discarded remainder is anti-self-conjugate (pure imaginary on
    # the unit circle).
    z = q**2
    p = D + z + z**2 + d * z**3
    center = Fraction(1, 2) + 2 * D
    expression = q**-3 * (p - center)
    real_part = q + q**-1 - Fraction(1, 4) * (q**3 + q**-3)
    remainder = expression - real_part
    check(conj(real_part) == real_part, "(3.6) purported real part is not real")
    check(conj(remainder) == -remainder, "(3.6) remainder is not pure imaginary")
    print("PASS (3.6) exact real/pure-imaginary decomposition")


def degree_four():
    z = q
    p = D + B * z + r * z**2 + b * z**3 + d * z**4
    h = [
        d,
        d * z + b,
        d * z**2 + b * z + r,
        d * z**3 + b * z**2 + r * z + B,
    ]
    k = [b, b * z + r, b * z**2 + r * z + B]
    check_poly_equal(schur(h), poly_scale(p * z**-3, k), "(4.4)")

    u = b * z
    S = r + u + B * z**-1
    second = schur(k)
    check_poly_equal(
        second,
        [z**-1 * (r * S + u**2), S**2 - b * B],
        "(4.6) second Schur endpoint coefficients",
    )
    check(
        z**-2 * (p - 2 * D) == S + d * z**2 - D * z**-2,
        "(4.8) boundary decomposition",
    )
    print("PASS (4.8) boundary decomposition")


def degree_five():
    z = q**2
    p = D + B * z + C * z**2 + c * z**3 + b * z**4 + d * z**5
    h = [
        d,
        d * z + b,
        d * z**2 + b * z + c,
        d * z**3 + b * z**2 + c * z + C,
        d * z**4 + b * z**3 + c * z**2 + C * z + B,
    ]
    k = [
        b,
        b * z + c,
        b * z**2 + c * z + C,
        b * z**3 + c * z**2 + C * z + B,
    ]
    check_poly_equal(schur(h), poly_scale(p * z**-4, k), "(5.2)")

    transformed = [q**3 * coeff * q**(-2 * j) for j, coeff in enumerate(k)]
    BB = b * q**3
    CC = c * q
    S = BB + CC + C * q**-1 + B * q**-3
    ell = [BB, BB + CC, BB + CC + C * q**-1, S]
    check_poly_equal(transformed, ell, "(5.4) unit-phase transformation")

    second = schur(ell)
    check(second[0] == S * CC + BB**2, "(5.5) constant coefficient")
    check(second[-1] == S**2 - BB * conj(BB), "(5.5) leading coefficient")
    print("PASS (5.5) second Schur endpoint coefficients")
    check(
        q**-5 * (p - 2 * D) == S + d * q**5 - D * q**-5,
        "(5.6) boundary decomposition",
    )
    print("PASS (5.6) boundary decomposition")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--inject-failure",
        action="store_true",
        help="exercise the explicit nonzero exit path used by the audit",
    )
    args = parser.parse_args()
    if args.inject_failure:
        check(False, "injected fail-closed self-test")
    degree_three()
    degree_four()
    degree_five()
