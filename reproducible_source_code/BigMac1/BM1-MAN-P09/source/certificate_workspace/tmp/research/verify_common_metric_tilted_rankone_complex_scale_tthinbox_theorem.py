#!/usr/bin/env python3
"""Fail-closed exact source verifier for the derivative-certified t layer."""

if not __debug__:
    raise RuntimeError("fail closed: run without python -O")

from hashlib import sha256
from math import prod
from pathlib import Path
import sympy as sp


ROOT = Path(__file__).resolve().parents[2]
DEPENDENCIES = {
    "tmp/research/common_metric_tilted_rankone_complex_scale_rbox_theorem.md":
        "b049ead438ebbe295d39d76608afdba9d23cd0e5e1bb61f2a5fc346259387742",
    "tmp/research/common_metric_tilted_rankone_complex_scale_r_adjacent_theorem.md":
        "3e2dcc40cb2997499ac29f735c9956278fa2c40c10bd9068c441ed8c3b5bbe15",
    "tmp/research/verify_common_metric_tilted_rankone_complex_scale_rbox_theorem.py":
        "4dbcb35560800abc11ef9016438df186aa37462e1b53d1c25c29098f0b637efe",
    "audit/verify_common_metric_tilted_rankone_complex_scale_rbox_referee.py":
        "5836cc5e45d13bccb8a2111affdf1579fd1bd3a5da2a1bfec0f2c33dea6c3a09",
    "audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_SCALE_RBOX_REFEREE_AUDIT.md":
        "81de7f859652face01fd3f760085d28956a0c61fab2c6f3c5c392ba12693859f",
    "audit/COMMON_METRIC_TILTED_RANKONE_COMPLEX_SCALE_R_ADJACENT_REFEREE_AUDIT.md":
        "4fb0e88fc357ab443269935262b6e21c65838511f75b1fcb31ae09366cee721c",
}
for relative_path, expected_hash in DEPENDENCIES.items():
    payload = (ROOT / relative_path).read_bytes()
    assert sha256(payload).hexdigest() == expected_hash, relative_path


def modulus_square(value):
    return sp.expand_complex(value * sp.conjugate(value))


def original_gate(matrix, a, c):
    vector = sp.Matrix([a, 0, c])
    image = matrix * vector
    square = matrix**2
    return sp.factor(
        a**2 * modulus_square(image[1])
        + sp.Rational(1, 4) * modulus_square(
            c * sp.conjugate(image[0]) + a * image[2]
            + sp.I * (a * c - square[2, 0])
        )
        + sp.Rational(1, 4) * modulus_square(
            c * sp.conjugate(image[1]) - sp.I * square[2, 1]
        )
        - 8 * a**2 * sp.re(image[0]) ** 2
    )


ell, w, k, z, r, t, T, s, qfree = sp.symbols(
    "ell w k z r t T s qfree", real=True
)
variables = (ell, w, k, z, r, t)
a = sp.Rational(3, 5)
c = sp.Rational(4, 5)
Delta = sp.factor(r * t - z**2 - w**2)
n = sp.factor(t * (k**2 + ell**2) + r - 2 * (k * z + ell * w))
g = sp.factor(a * c * ell - z * k - w * ell - t)
qmin = s**2 * n / Delta
Q = sp.Matrix([
    [r, s * (k + sp.I * ell), z + sp.I * w],
    [s * (k - sp.I * ell), qmin, s],
    [z - sp.I * w, s, t],
])

active = Q.extract([0, 2], [0, 2])
coupling = Q.extract([0, 2], [1])
assert sp.factor(active.det() - Delta) == 0
assert sp.factor(
    (sp.conjugate(coupling).T * active.inv() * coupling)[0] - qmin
) == 0
assert sp.factor(Q.det()) == 0
danger = sp.factor(sp.re((Q * sp.Matrix([a, 0, c]))[0]))
assert sp.factor(danger - (a * r + c * z)) == 0

free_matrix = Q.copy()
free_matrix[1, 1] = qfree
free_image = free_matrix * sp.Matrix([a, 0, c])
last_leak = sp.expand(
    c * sp.conjugate(free_image[1])
    - sp.I * (free_matrix**2)[2, 1]
)
assert sp.factor(sp.im(last_leak) + s * (qfree - g)) == 0
assert sp.factor(qmin - g - (s**2 * n - Delta * g) / Delta) == 0

x = a * r + c * z
L = a * k + c
A = a * c * (r + t) + z - w * (r + t)
B = a * c - w - z * (r + t)
C = c * L + z * ell - w * k
P = sp.expand(
    Delta**2 * (
        (A - T * ell) ** 2 + (B - T * k) ** 2 - 32 * a**2 * x**2
        + T * (4 * a**2 * (L**2 + a**2 * ell**2) + C**2)
    )
    + T * (T * n - Delta * g) ** 2
)
assert sp.factor(4 * Delta**2 * original_gate(Q, a, c) - P.subs(T, s**2)) == 0
scale_poly = sp.Poly(P, T)
C0 = sp.factor(scale_poly.coeff_monomial(1))
C1 = sp.factor(scale_poly.coeff_monomial(T))
C2 = sp.factor(scale_poly.coeff_monomial(T**2))
assert sp.factor(scale_poly.coeff_monomial(T**3) - n**2) == 0
assert sp.factor(C2 - (
    Delta**2 * (k**2 + ell**2) - 2 * Delta * g * n
)) == 0
TL = sp.factor(Delta * g / n)
N0, D0 = sp.cancel(P.subs(T, TL)).as_numer_denom()
N1_raw, D1 = sp.cancel(sp.diff(P, T).subs(T, TL)).as_numer_denom()
N1 = -N1_raw
assert sp.factor(D0 - 15625 * n**2) == 0
assert sp.factor(D1 + 625 * n) == 0
assert sp.factor(C2 + 3 * n**2 * TL - (
    Delta**2 * (k**2 + ell**2) + Delta * g * n
)) == 0

pn = sp.Poly(n, *variables, domain=sp.QQ)
p0 = sp.Poly(C0, *variables, domain=sp.QQ)
p1 = sp.Poly(C1, *variables, domain=sp.QQ)
p2 = sp.Poly(C2, *variables, domain=sp.QQ)
negative_disc = -(
    18 * pn**2 * p2 * p1 * p0
    - 4 * p2**3 * p0
    + p2**2 * p1**2
    - 4 * pn**2 * p1**3
    - 27 * pn**4 * p0**2
)
disc_den, disc_integer = negative_disc.clear_denoms(convert=True)
assert disc_den == 244140625
ND = disc_integer.as_expr()

polynomials = {
    "danger": -danger,
    "Delta": Delta,
    "n": n,
    "C0": C0,
    "C1": C1,
    "N0": N0,
    "N1": N1,
    "ND": ND,
}
expected_degrees = {
    "danger": (0, 0, 0, 1, 1, 0),
    "Delta": (0, 2, 0, 2, 1, 1),
    "n": (2, 1, 2, 1, 1, 1),
    "C0": (0, 6, 0, 6, 4, 4),
    "C1": (2, 6, 2, 6, 3, 4),
    "N0": (5, 10, 5, 10, 6, 6),
    "N1": (4, 7, 4, 7, 4, 4),
    "ND": (10, 20, 10, 20, 12, 13),
}
expected_direct_counts = {
    name: prod(degree + 1 for degree in degrees)
    for name, degrees in expected_degrees.items()
}
assert expected_direct_counts["ND"] == 9711702
assert sum(expected_direct_counts.values()) == 9975375
for name, expression in polynomials.items():
    degree = tuple(
        sp.Poly(expression, *variables, domain=sp.QQ).degree(variable)
        for variable in variables
    )
    assert degree == expected_degrees[name], name

center_margins = {
    "r_low": {
        "danger": sp.Rational(93, 500),
        "Delta": sp.Rational(14219, 5000),
        "n": sp.Rational(1456753, 5000),
        "C0": sp.Rational(420515573041543529, 1250000000000000),
        "C1": sp.Rational(1195599356262447793, 1250000000000000),
        "N0": sp.Rational(
            544257743489740893611366179477411,
            1250000000000000000000,
        ),
        "N1": sp.Rational(
            3448220588099013077412457, 20000000000000000
        ),
        "ND": sp.Rational(
            16659627721252625696244381239255705449827376815068142600603001925331,
            3200000000000000000000000000000000000000000,
        ),
    },
    "r_high": {
        "danger": sp.Rational(87, 500),
        "Delta": sp.Rational(14619, 5000),
        "n": sp.Rational(1456853, 5000),
        "C0": sp.Rational(448500662246821401, 1250000000000000),
        "C1": sp.Rational(1261378431909517593, 1250000000000000),
        "N0": sp.Rational(
            4642466069575661682742742534193063,
            10000000000000000000000,
        ),
        "N1": sp.Rational(
            3637314850248595682332957, 20000000000000000
        ),
        "ND": sp.Rational(
            18942501765434648654554516142706963646914690725542726020966050250291,
            3200000000000000000000000000000000000000000,
        ),
    },
}
center_notes = {
    "r_low": (ROOT / "tmp/research/common_metric_tilted_rankone_complex_scale_rbox_theorem.md").read_text(),
    "r_high": (ROOT / "tmp/research/common_metric_tilted_rankone_complex_scale_r_adjacent_theorem.md").read_text(),
}
for cell_name, margins in center_margins.items():
    for margin in margins.values():
        assert str(margin) in center_notes[cell_name]

expected_term_counts = {
    "danger": 1, "Delta": 1, "n": 2, "C0": 62,
    "C1": 67, "N0": 1851, "N1": 326, "ND": 84595,
}
expected_majorants = {
    "danger": sp.Integer(0),
    "Delta": sp.Rational(103, 100),
    "n": sp.Rational(1090601, 10000),
    "C0": sp.Rational(3591519308424373, 3125000000000),
    "C1": sp.Rational(32111117681043527, 5000000000000),
    "N0": sp.Rational(
        98448296054638286971718220153709637,
        12800000000000000000000,
    ),
    "N1": sp.Rational(
        452887170660359886538671, 256000000000000
    ),
    "ND": sp.Rational(
        107209382767024034160962381222448011318186558450015706249449102691599869001,
        51200000000000000000000000000000000000000000000,
    ),
}
expected_minimum_reserves = {
    "danger": sp.Rational(87, 500),
    "Delta": sp.Rational(142087, 50000),
    "n": sp.Rational(1455662399, 5000000),
    "C0": sp.Rational(2088211787974020153, 6250000000000000),
    "C1": sp.Rational(2359087594843852059, 2500000000000000),
    "N0": sp.Rational(
        2688151350612835088318476618770634683,
        6400000000000000000000000,
    ),
    "N1": sp.Rational(
        108078622965866619044505269, 640000000000000000
    ),
    "ND": sp.Rational(
        26067639002996971408992668691597632280432456070529434555374912711048130999,
        25600000000000000000000000000000000000000000000000,
    ),
}
absolute_coordinate_bounds = (
    sp.Integer(10), sp.Rational(31, 100), sp.Rational(301, 100),
    sp.Rational(101, 100), sp.Rational(103, 100), sp.Rational(401, 100),
)
wide_t_left = sp.Rational(399, 100)
wide_t_right = sp.Rational(401, 100)
epsilon = sp.Rational(1, 500)
narrow_t_left = 4 - epsilon
narrow_t_right = 4 + epsilon
assert wide_t_left <= narrow_t_left < narrow_t_right <= wide_t_right

for name, expression in polynomials.items():
    derivative_terms = sp.Poly(
        sp.diff(expression, t), *variables, domain=sp.QQ
    ).terms()
    assert len(derivative_terms) == expected_term_counts[name], name
    majorant = sum(
        abs(coefficient) * prod(
            bound**exponent
            for bound, exponent in zip(absolute_coordinate_bounds, monomial)
        )
        for monomial, coefficient in derivative_terms
    )
    assert majorant == expected_majorants[name], name
    reserves = [
        sp.factor(margins[name] - epsilon * majorant)
        for margins in center_margins.values()
    ]
    assert all(reserve > 0 for reserve in reserves), name
    assert min(reserves) == expected_minimum_reserves[name], name

spectral_shape_derivative_margin = (
    sp.Rational(99, 100) * wide_t_left
    - sp.Rational(99, 100)**2
    - 2 * (sp.Rational(101, 100)**2 + sp.Rational(31, 100)**2)
)
assert spectral_shape_derivative_margin == sp.Rational(461, 625) > 0

witness_values = {
    ell: 9,
    w: -sp.Rational(31, 100),
    k: -sp.Rational(301, 100),
    z: -sp.Rational(101, 100),
    r: sp.Rational(103, 100),
    t: sp.Rational(2001, 500),
    s: 1,
}
witness = sp.simplify(Q.subs(witness_values))
assert sp.factor(witness.det()) == 0
assert Delta.subs(witness_values) == sp.Rational(150293, 50000)
assert n.subs(witness_values) == sp.Rational(1804751601, 5000000)
assert g.subs(witness_values) == sp.Rational(679, 10000)
assert witness[1, 1] == sp.Rational(1804751601, 15029300)
assert danger.subs(witness_values) == -sp.Rational(19, 100)
witness_gate = original_gate(witness, a, c)
assert witness_gate == sp.Rational(
    414461983319631411704949, 112939929245000000000
) > 0
real_witness = witness.applyfunc(sp.re)
assert sp.factor(4 * (
    witness_gate - original_gate(real_witness, a, c)
)) == -sp.Rational(585660171418319979, 375732500000000) < 0
assert sp.im(witness[0, 1]) * sp.im(witness[0, 2]) == -sp.Rational(279, 100)

print("PASS audited t=4 center dependencies and exact minima binding")
print("PASS original Hermitian gate, rank-two PSD, and complete legal half-line")
print("PASS eight exact center-margin/t-derivative reserves on t=[1999/500,2001/500]")
print("PASS exact nonredundancy and phase-integrity witness")
print("scope=derivative-certified thin t partial theorem; unrestricted gate open")
