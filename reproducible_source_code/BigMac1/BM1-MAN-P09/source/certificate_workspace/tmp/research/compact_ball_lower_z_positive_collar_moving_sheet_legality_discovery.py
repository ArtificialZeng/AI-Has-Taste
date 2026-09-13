#!/usr/bin/env python3
"""Exact rational legality bounds for the moving-sheet positive-Z family."""

if not __debug__:
    raise RuntimeError("do not run this discovery script with python -O")

import sympy as sp


def main():
    R = sp.Rational
    S_max = R(1, 10000)
    X_max = R(3, 10000)
    M_radius = R(1, 1000)
    transverse_radius = R(1, 100)
    A_min = 1 - M_radius
    A_max = 1 + M_radius

    # y0=12/(25(1+M))+nu is decreasing in M and increasing in nu.
    y0_min = R(12, 25) / A_max - transverse_radius
    y0_max = R(12, 25) / A_min + transverse_radius

    # w0=(45M+18)/(25(1+M))+omega has M derivative
    # 27/(25(1+M)^2)>0.  The full W/S coefficient is w0-3X/5.
    w0_min = (18 - 45 * M_radius) / (25 * A_min) - transverse_radius
    w0_max = (18 + 45 * M_radius) / (25 * A_max) + transverse_radius
    wbar_min = w0_min - R(3, 5) * X_max
    wbar_max = w0_max

    z_slope = sp.factor(wbar_min - S_max * y0_max**2)
    z_upper = sp.factor(3 * X_max + S_max * wbar_max)
    y_upper = sp.factor(S_max * y0_max)
    danger_reserve = sp.factor(
        R(3, 5)
        - R(13, 5) * X_max
        - R(6, 5) * y_upper
        - S_max * wbar_max
    )

    print("A_RANGE", A_min, A_max)
    print("Y0_RANGE", y0_min, y0_max)
    print("Y_RANGE", "0<Y<=", y_upper)
    print("WBAR_RANGE", wbar_min, wbar_max)
    print("Z_LOWER", "Z>=S*", z_slope)
    print("Z_UPPER", z_upper)
    print("DANGER_RESERVE", danger_reserve)
    print("SIMPLE_Y_TARGET", y_upper < R(1, 1000))
    print("SIMPLE_Z_TARGET", z_upper < R(1, 1000))
    print("SIMPLE_DANGER_TARGET_299_500", danger_reserve > R(299, 500))

    if not (A_min > 0 and y0_min > 0 and wbar_min > 0):
        raise AssertionError("positive denominator/coordinate bound failed")
    if not (z_slope > 0 and z_upper < R(1, 1000)):
        raise AssertionError("positive-Z target failed")
    if not (y_upper < R(1, 1000)):
        raise AssertionError("Y target failed")
    if not (danger_reserve > R(299, 500)):
        raise AssertionError("danger reserve failed")

    # Exact coordinate identity used for danger.  This is independent of the
    # endpoint estimates above and fails closed if a sign is changed.
    S, X, M, omega, nu = sp.symbols("S X M omega nu", real=True)
    A = 1 + M
    y0 = R(12, 25) / A + nu
    wc = -3 * (5 * M * X - 15 * M + 5 * X - 6) / (25 * A)
    Y = S * y0
    W = S * (wc + omega)
    Z = 3 * X - X**2 - Y**2 + W
    x = -R(1, 5) + X
    y = R(3, 5) + Y
    identity = sp.factor(
        x**2 + y**2 + Z
        - (R(2, 5) + R(13, 5) * X + R(6, 5) * Y + W)
    )
    if identity != 0:
        raise AssertionError(("danger identity", identity))
    print("DANGER_IDENTITY", "PASS")
    print("STATUS", "PASS")


if __name__ == "__main__":
    main()
