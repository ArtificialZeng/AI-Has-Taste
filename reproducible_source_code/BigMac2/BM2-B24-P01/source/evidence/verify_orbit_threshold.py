#!/usr/bin/env python3
"""Exact rational certificate for the n=18 free-critical orbit.

The script uses only Python integer arithmetic and fractions.Fraction. It does
not use floating point arithmetic.
"""

from fractions import Fraction as F


def a(t: F) -> F:
    return 12654 * t * t + 684 * t - 306


def q(t: F) -> F:
    return t * a(t) / (2 * (19 * t + 1) ** 3)


def p(t: F) -> F:
    return 13186 * t**3 + 1425 * t**2 - 96 * t + 1


t0 = F(17, 703)
q0 = q(t0)
assert q0 == F(-10693, 9747)

# Direct integer cross-products for 16/125 < t1 < 13/100.
orbit_num = 17 * 10693**18
orbit_den = 703 * 9747**18
t1 = F(orbit_num, orbit_den)
lower_gap = 125 * orbit_num - 16 * orbit_den
upper_gap = 13 * orbit_den - 100 * orbit_num
assert lower_gap > 0
assert upper_gap > 0
assert F(16, 125) < t1 < F(13, 100)

# A is increasing for t>0, and A(13/100)<0, so q(t1)<0.
assert a(F(13, 100)) == F(-16137, 5000)
assert q(t1) < 0

# q(t)+1/50 = H(t)/(50(19t+1)^3). H is increasing on the
# interval because H'(16/125)>0 and H''(t)>0 for t>=0.
def h(t: F) -> F:
    return 323209 * t**3 + 18183 * t**2 - 7593 * t + 1


def h_prime(t: F) -> F:
    return 3 * (323209 * t**2 + 12122 * t - 2531)


assert h(F(16, 125)) == F(9423189, 1953125) > 0
assert h_prime(F(16, 125)) == F(202315887, 15625) > 0
assert q(t1) > F(-1, 50)

t2 = t1 * q(t1) ** 18
assert 0 < t2 < F(13, 100) * F(1, 50) ** 18 < F(1, 100)

# On [0,1/100], P'(t)=6g(t), where g is increasing and remains
# negative. Thus P decreases there and stays positive. A sign change
# by 1/70 proves a positive root exists strictly above 1/100.
def g(t: F) -> F:
    return 6593 * t**2 + 475 * t - 16


assert g(F(1, 100)) == F(-105907, 10000) < 0
assert p(F(1, 100)) == F(97843, 500000) > 0
assert p(F(1, 70)) == F(-1808, 42875) < 0

print("q(t0) = -10693/9747")
print("lower cross-product gap =", lower_gap)
print("upper cross-product gap =", upper_gap)
print("16/125 < t1 < 13/100")
print("-1/50 < q(t1) < 0")
print("0 < t2 < (13/100)(1/50)^18 < 1/100")
print("P is positive on [0,1/100] and P(1/70) < 0")

