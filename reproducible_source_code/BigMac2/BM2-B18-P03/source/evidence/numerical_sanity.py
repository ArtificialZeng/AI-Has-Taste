#!/usr/bin/env python3
"""Floating-point sanity checks only; the proof is resolution_argument.md."""

import math


KAPPA = math.pi / 2.0
A = KAPPA * KAPPA
TRIAL_LIMIT = 4.0 * A / (3.0 * math.sqrt(math.pi))
UPPER_LIMIT = 2.0 * A


def autocorrelation(r):
    """Integral f(p)f(p-r) dp for f=cos(pi*p/2) 1_{[-1,1]}, 0<=r<=2."""
    return (1.0 - r / 2.0) * math.cos(KAPPA * r) + math.sin(KAPPA * r) / (2.0 * KAPPA)


def simpson(f, left, right, n=100000):
    if n % 2:
        n += 1
    step = (right - left) / n
    total = f(left) + f(right)
    total += 4.0 * sum(f(left + step * j) for j in range(1, n, 2))
    total += 2.0 * sum(f(left + step * j) for j in range(2, n, 2))
    return total * step / 3.0


def trial_q(u):
    # With r=2*sqrt(u)*t, q=(2/sqrt(pi))*int exp(-t^2)C(r)dt.
    root = math.sqrt(u)
    upper = min(2.0 / (2.0 * root), 9.0)
    integral = simpson(
        lambda t: math.exp(-t * t) * autocorrelation(2.0 * root * t),
        0.0,
        upper,
    )
    return 2.0 * integral / math.sqrt(math.pi)


def comparison_root(u):
    target = 1.0 / math.sqrt(u)
    lo, hi = 0.0, KAPPA
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if mid * math.tan(mid) < target:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


print(f"trial predicted limit = {TRIAL_LIMIT:.12f}")
print(f"comparison predicted limit = {UPPER_LIMIT:.12f}")
print("u            trial_scaled    comparison_scaled   q<=rho")
for u in (4e-2, 1e-2, 2.5e-3, 6.25e-4, 1.5625e-4):
    q = trial_q(u)
    k = comparison_root(u)
    rho = 1.0 / (1.0 + u * k * k)
    trial_scaled = (math.log(q) + A * u) / (u ** 1.5)
    upper_scaled = (math.log(rho) + A * u) / (u ** 1.5)
    print(f"{u:<12.7g} {trial_scaled:>14.9f} {upper_scaled:>20.9f}   {q <= rho}")

