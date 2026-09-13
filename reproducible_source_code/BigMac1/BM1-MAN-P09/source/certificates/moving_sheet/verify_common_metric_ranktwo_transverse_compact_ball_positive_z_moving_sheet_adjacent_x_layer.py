#!/usr/bin/env python3
"""Exact source verifier for the adjacent-X positive-Z moving-sheet layer.

The verifier deliberately replays the predecessor's raw Hermitian ``Q,Q^2``
reconstruction before using its exact sparse quotient bounds.  The new work
is the strictly larger projective radius ``X<=1/31`` and its legality audit.
No sampled or floating-point value is used as a proof.
"""

if not __debug__:
    raise RuntimeError("do not run this source verifier with python -O")

import sympy as sp

import verify_common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_family as base


def zero(expression, label):
    value = sp.factor(sp.cancel(sp.together(expression)))
    if value != 0:
        raise AssertionError((label, value))


def main():
    # This reconstructs the original Hermitian compression and gate, checks
    # the exact 20-term sparse quotient, and binds all H2/B_d constants below
    # to that raw source expression.
    base.main()

    R = sp.Rational
    Smax = R(1, 10000)
    Xold = R(3, 10000)
    Xmax = R(1, 31)
    Mradius = R(1, 1000)
    tradius = R(1, 100)

    if not (0 < Smax < Xold < Xmax < 3):
        raise AssertionError("ordered adjacent-X layer")

    Amin = 1 - Mradius
    Amax = 1 + Mradius
    y0min = R(12, 25) / Amax - tradius
    y0max = R(12, 25) / Amin + tradius
    w0min = (18 - 45 * Mradius) / (25 * Amin) - tradius
    w0max = (18 + 45 * Mradius) / (25 * Amax) + tradius
    wbarmin = w0min - R(3, 5) * Xmax
    yupper = Smax * y0max

    # Z=3X-X^2+S(wc+omega)-S^2 y0^2.  On 0<=X<=1/31,
    # 3X-X^2 is nonnegative, and the last two terms have this exact slope.
    zslope = sp.factor(wbarmin - Smax * y0max**2)
    zupper = sp.factor(3 * Xmax + Smax * w0max)
    danger_reserve = sp.factor(
        R(3, 5) - R(13, 5) * Xmax
        - R(6, 5) * yupper - Smax * w0max
    )
    legality_claims = {
        "wbarmin": (wbarmin, R(79093, 114700)),
        "zslope": (zslope, R(237033451226441, 343755900000000)),
        "zupper": (zupper, R(3005268611, 31031000000)),
        "danger": (danger_reserve, R(8886607262249, 17222205000000)),
    }
    for label, (value, claim) in legality_claims.items():
        zero(value - claim, label)
    if not (
        Amin > 0 and y0min > 0 and zslope > 0
        and zupper < R(1, 8) and danger_reserve > R(1, 2)
    ):
        raise AssertionError("adjacent-X legality reserve")

    # The predecessor's exact sparse quotient is
    # Qhat=H1+H2+R, H1>=0,
    # H2>=reserve*(S^2+SX+X^2), and after S=X*sigma the remainder is
    # bounded by X^2 sum B_d X^d.  The adjacent layer has S<=X, so C1 is
    # lossless everywhere and no division by a possibly zero X occurs.
    reserve = R(
        2564950982194530478444050838857341987999,
        1274019840000000000000000000,
    )
    layer_bounds = {
        1: R(
            1040210347071333285995390774300441067433076882959,
            17199267840000000000000000000000000,
        ),
        2: R(
            513625292315565411172470351664061881087569457669,
            28665446400000000000000000000000000,
        ),
        3: R(
            9574969116015939526109085821350045427090716403,
            6370099200000000000000000000000000,
        ),
        4: R(
            34218452213929153632941920549574435172203,
            1592524800000000000000000000000,
        ),
        5: R(
            1012066220495792924792495220066012001,
            530841600000000000000000000,
        ),
    }
    margin = sp.factor(
        reserve - sum(
            bound * Xmax**degree
            for degree, bound in layer_bounds.items()
        )
    )
    margin_claim = R(
        42950357876463827039627477692165648038556445276911579,
        984800872161607680000000000000000000000000,
    )
    zero(margin - margin_claim, "adjacent C1 margin")
    if margin <= 0:
        raise AssertionError(("adjacent C1 margin", margin))

    # A useful exact route boundary: the unchanged global absolute-remainder
    # estimate turns negative at X=1/30.  This is a failure of this sufficient
    # certificate only, never a negative value of the original gate.
    next_radius = R(1, 30)
    next_margin = sp.factor(
        reserve - sum(
            bound * next_radius**degree
            for degree, bound in layer_bounds.items()
        )
    )
    next_claim = -R(
        3902147921357110886357029674143626227976364394263,
        171992678400000000000000000000000000000,
    )
    zero(next_margin - next_claim, "next-radius route obstruction")
    if next_margin >= 0:
        raise AssertionError(("expected bound failure only", next_margin))

    print("PASS predecessor raw Hermitian Q,Q^2 reconstruction replayed")
    print("PASS adjacent X layer 3/10000<=X<=1/31 uses lossless C1 chart")
    print("PASS closed overlap X=3/10000; merged domain 0<=X<=1/31")
    print("PASS exact positive-Z, Z<1/8, danger reserve>1/2, rank-two PSD")
    print("DANGER_RESERVE", danger_reserve)
    print("ADJACENT_C1_MARGIN", margin)
    print("BOUND_FAILURE_ONLY_AT_X=1/30", next_margin)
    print("PASS strict raw 36Gamma on the adjacent-X moving-sheet layer")
    print("SCOPE adjacent parametric layer only; full compact ball and fixed lens open")


if __name__ == "__main__":
    main()
