#!/usr/bin/env python3
"""A small directed-rounding feasibility probe for the two reported valleys.

This is not a certificate for the full target interval.  It encloses F at each
printed decimal abscissa by iterating the exact functional equation with Arb
balls.  At the terminal scale it uses

    |F(t)-1| <= 2*pi*|t|*sup(supp(mu)) <= (4*pi/3)|t|.

The same support bound gives |F'(x)| <= 4*pi/3, so a positive pointwise lower
bound also certifies the small neighborhood printed below.
"""

import flint
from flint import acb, arb, ctx


ctx.prec = 256
DEPTH = 120
P = (arb(5).sqrt() - 1) / 2
P2 = P * P
PI = arb.pi()
LIPSCHITZ = 4 * PI / 3


def enclose_f_and_q(x_text: str):
    """Enclose F(x), F(x/2), and q(x) for the exact printed decimal x."""
    x = arb(x_text)
    terminal = abs(x) / (arb(2) ** DEPTH)
    radius_n = LIPSCHITZ * terminal
    radius_n1 = radius_n / 2

    # Rectangles contain the disks |F(t)-1| <= radius.
    f_next = acb(arb(1, radius_n), arb(0, radius_n))
    f_next2 = acb(arb(1, radius_n1), arb(0, radius_n1))

    for k in range(DEPTH - 1, -1, -1):
        t = x / (arb(2) ** k)
        phase = acb(0, -PI * t).exp()
        f_here = P * f_next + P2 * phase * f_next2
        f_next2, f_next = f_next, f_here

    f_x, f_half = f_next, f_next2
    assert not f_half.contains(0), "q division was not certified"
    return f_x, f_half, f_x / f_half


CASES = (
    ("6580077.19160276", "1e-11"),
    ("5065070.60771886", "5e-12"),
)

print(f"python-flint={flint.__version__}; precision={ctx.prec} bits; depth={DEPTH}")
for x_text, neighborhood_radius in CASES:
    f_x, f_half, q_x = enclose_f_and_q(x_text)
    f_abs = abs(f_x)
    q_abs = abs(q_x)
    margin = f_abs.lower() - LIPSCHITZ * arb(neighborhood_radius)
    assert not f_x.contains(0)
    assert not q_x.contains(0)
    assert margin.lower() > 0
    print(f"x={x_text}")
    print(f"  |F(x)| in {f_abs}")
    print(f"  |F(x/2)| in {abs(f_half)}")
    print(f"  |q(x)| in {q_abs}")
    print(
        "  certified F != 0 for |t-x| <= "
        f"{neighborhood_radius}; lower margin {margin}"
    )

