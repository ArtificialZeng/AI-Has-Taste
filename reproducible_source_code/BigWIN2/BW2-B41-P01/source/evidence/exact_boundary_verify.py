"""Exact regression checks for the boundary RP certificate.

The finite loop is not used as an infinite proof.  The symbolic endpoint
argument is recorded in boundary_certificate.md.
"""

from fractions import Fraction
from math import comb


def certificate(L):
    m = 2 * L + 3
    D = (L + 2) * (3 * L + 4)
    e = Fraction(1, D)
    return {
        "BB": Fraction(3 * L * L + 9 * L + 8, 2 * (L + 1) * D),
        "aX": Fraction(3 * L + 5, D),
        "bX": 1 - e,
        "UU": e,
        "Ua": e,
        "UB": e,
        "UX": Fraction(1, L + 2),
    }


def check(L):
    m = 2 * L + 3
    n = 2 * m + L + 1
    x = certificate(L)
    D = (L + 2) * (3 * L + 4)
    e = Fraction(1, D)

    total = (
        comb(m, 2) * x["BB"]
        + m * x["aX"]
        + m * x["bX"]
        + comb(L, 2) * x["UU"]
        + L * x["Ua"]
        + L * m * x["UB"]
        + L * m * x["UX"]
    )
    assert total == n - 1
    degrees = {
        "a": m * x["aX"] + L * x["Ua"],
        "b": (m - 1) * x["BB"] + x["bX"] + L * x["UB"],
        "x": x["aX"] + x["bX"] + L * x["UX"],
        "u": (L - 1) * x["UU"] + x["Ua"] + m * x["UB"] + m * x["UX"],
    }
    assert degrees == {
        "a": 2 - e,
        "b": 2 - e,
        "x": 2 - Fraction(1, L + 2),
        "u": 2 - e,
    }

    minimum = None
    minimizers = []
    descriptor_count = 0
    for alpha in range(2):
        for k in range(m + 1):
            for h in range(m + 1):
                # x["bX"] is positive, so d=min(k,h) is the exact worst
                # case.  Every other feasible d has larger slack by
                # (min(k,h)-d)*x["bX"].  Count all feasible d values while
                # evaluating only this decisive endpoint.
                d = min(k, h)
                d_count = d - max(0, k + h - m) + 1
                for z in range(L + 1):
                    size = alpha + k + h + z
                    if size < 2 or size == n:
                        continue
                    descriptor_count += d_count
                    internal = (
                        comb(k, 2) * x["BB"]
                        + alpha * h * x["aX"]
                        + d * x["bX"]
                        + comb(z, 2) * x["UU"]
                        + z * alpha * x["Ua"]
                        + z * k * x["UB"]
                        + z * h * x["UX"]
                    )
                    slack = size - 1 - internal
                    assert slack >= e
                    if minimum is None or slack < minimum:
                        minimum = slack
                        minimizers = [(alpha, k, h, d, z)]
                    elif slack == minimum:
                        minimizers.append((alpha, k, h, d, z))
    assert minimum == e
    assert minimizers == [(0, 1, 1, 1, 0)]
    return D, degrees, descriptor_count, minimum, minimizers


for ell in range(1, 31):
    denominator, degree_sums, count, minimum, where = check(ell)
    print(
        f"ell={ell:2d} D={denominator:5d} descriptors={count:9d} "
        f"min_slack={minimum} minimizer={where} degrees={degree_sums}"
    )
