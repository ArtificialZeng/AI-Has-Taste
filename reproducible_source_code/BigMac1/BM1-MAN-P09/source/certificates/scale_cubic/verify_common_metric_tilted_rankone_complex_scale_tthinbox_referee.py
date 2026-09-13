#!/usr/bin/env python3
"""Isolated exact referee for the derivative-certified active-block t layer.

No source or discovery module is imported.  The scale cubic is extracted from
the original fully conjugated gate, and all eight derivative majorants are
rebuilt from independent exact power coefficients.
"""

if not __debug__:
    raise RuntimeError("fail closed: run without python -O")

from hashlib import sha256
from math import prod
from pathlib import Path
import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
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
    assert sha256((ROOT / relative_path).read_bytes()).hexdigest() == expected_hash


def square_modulus(value):
    return sp.expand_complex(value * sp.conjugate(value))


def raw_gate(matrix):
    a = sp.Rational(3, 5)
    c = sp.Rational(4, 5)
    vector = sp.Matrix([a, 0, c])
    image = matrix * vector
    square = matrix**2
    return sp.expand(
        a**2 * square_modulus(image[1])
        + sp.Rational(1, 4) * square_modulus(
            c * sp.conjugate(image[0]) + a * image[2]
            + sp.I * (a * c - square[2, 0])
        )
        + sp.Rational(1, 4) * square_modulus(
            c * sp.conjugate(image[1]) - sp.I * square[2, 1]
        )
        - 8 * a**2 * sp.re(image[0]) ** 2
    )


ell, w, k, z, r, t, tau, T, qfree = sp.symbols(
    "ell w k z r t tau T qfree", real=True
)
variables = (ell, w, k, z, r, t)
a = sp.Rational(3, 5)
c = sp.Rational(4, 5)
I = sp.I
Delta = r * t - z**2 - w**2
n = t * (k**2 + ell**2) + r - 2 * (k * z + ell * w)
qmin = tau**2 * n / Delta
matrix = sp.Matrix([
    [r, tau * (k + I * ell), z + I * w],
    [tau * (k - I * ell), qmin, tau],
    [z - I * w, tau, t],
])

active = matrix.extract([0, 2], [0, 2])
column = matrix.extract([0, 2], [1])
assert sp.factor(active.det() - Delta) == 0
assert sp.factor(
    (sp.conjugate(column).T * active.inv() * column)[0] - qmin
) == 0
assert sp.factor(matrix.det()) == 0
danger = sp.factor(sp.re((matrix * sp.Matrix([a, 0, c]))[0]))
assert sp.factor(danger - (a * r + c * z)) == 0

free_matrix = matrix.copy()
free_matrix[1, 1] = qfree
free_image = free_matrix * sp.Matrix([a, 0, c])
leak = sp.expand(
    c * sp.conjugate(free_image[1])
    - I * (free_matrix**2)[2, 1]
)
g = a * c * ell - z * k - w * ell - t
assert sp.factor(sp.im(leak) + tau * (qfree - g)) == 0
assert sp.factor(qmin - g - (tau**2 * n - Delta * g) / Delta) == 0

raw_tau = sp.Poly(sp.expand(4 * Delta**2 * raw_gate(matrix)), tau)
assert all(monomial[0] % 2 == 0 for monomial, _ in raw_tau.terms())
scale_poly = sp.Poly(sum(
    coefficient * T ** (monomial[0] // 2)
    for monomial, coefficient in raw_tau.terms()
), T)
assert scale_poly.degree() == 3
P = scale_poly.as_expr()
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

bb, d2, d1, d0, X = sp.symbols("bb d2 d1 d0 X", real=True)
generic_cubic = bb * X**3 + d2 * X**2 + d1 * X + d0
generic_discriminant = (
    18 * bb * d2 * d1 * d0 - 4 * d2**3 * d0 + d2**2 * d1**2
    - 4 * bb * d1**3 - 27 * bb**2 * d0**2
)
assert sp.factor(
    sp.discriminant(generic_cubic, X) - generic_discriminant
) == 0
pn = sp.Poly(n, *variables, domain=sp.QQ)
p0 = sp.Poly(C0, *variables, domain=sp.QQ)
p1 = sp.Poly(C1, *variables, domain=sp.QQ)
p2 = sp.Poly(C2, *variables, domain=sp.QQ)
minus_discriminant = -(
    18 * pn**2 * p2 * p1 * p0
    - 4 * p2**3 * p0
    + p2**2 * p1**2
    - 4 * pn**2 * p1**3
    - 27 * pn**4 * p0**2
)
disc_den, disc_integer = minus_discriminant.clear_denoms(convert=True)
assert disc_den == 244140625
ND = disc_integer.as_expr()

sign_polynomials = (
    ("danger", -danger), ("Delta", Delta), ("n", n),
    ("C0", C0), ("C1", C1), ("N0", N0), ("N1", N1), ("ND", ND),
)
claimed_degrees = {
    "danger": (0, 0, 0, 1, 1, 0),
    "Delta": (0, 2, 0, 2, 1, 1),
    "n": (2, 1, 2, 1, 1, 1),
    "C0": (0, 6, 0, 6, 4, 4),
    "C1": (2, 6, 2, 6, 3, 4),
    "N0": (5, 10, 5, 10, 6, 6),
    "N1": (4, 7, 4, 7, 4, 4),
    "ND": (10, 20, 10, 20, 12, 13),
}
direct_counts = {}
for name, expression in sign_polynomials:
    poly = sp.Poly(expression, *variables, domain=sp.QQ)
    degrees = tuple(poly.degree(variable) for variable in variables)
    assert degrees == claimed_degrees[name]
    direct_counts[name] = prod(degree + 1 for degree in degrees)
assert direct_counts["ND"] == 9711702
assert sum(direct_counts.values()) == 9975375

centers = {
    "r_low": {
        "danger": sp.Rational(93, 500),
        "Delta": sp.Rational(14219, 5000),
        "n": sp.Rational(1456753, 5000),
        "C0": sp.Rational(420515573041543529, 1250000000000000),
        "C1": sp.Rational(1195599356262447793, 1250000000000000),
        "N0": sp.Rational(544257743489740893611366179477411, 1250000000000000000000),
        "N1": sp.Rational(3448220588099013077412457, 20000000000000000),
        "ND": sp.Rational(16659627721252625696244381239255705449827376815068142600603001925331, 3200000000000000000000000000000000000000000),
    },
    "r_high": {
        "danger": sp.Rational(87, 500),
        "Delta": sp.Rational(14619, 5000),
        "n": sp.Rational(1456853, 5000),
        "C0": sp.Rational(448500662246821401, 1250000000000000),
        "C1": sp.Rational(1261378431909517593, 1250000000000000),
        "N0": sp.Rational(4642466069575661682742742534193063, 10000000000000000000000),
        "N1": sp.Rational(3637314850248595682332957, 20000000000000000),
        "ND": sp.Rational(18942501765434648654554516142706963646914690725542726020966050250291, 3200000000000000000000000000000000000000000),
    },
}
dependency_texts = {
    "r_low": (ROOT / "tmp/research/common_metric_tilted_rankone_complex_scale_rbox_theorem.md").read_text(),
    "r_high": (ROOT / "tmp/research/common_metric_tilted_rankone_complex_scale_r_adjacent_theorem.md").read_text(),
}
for cell_name, values in centers.items():
    assert all(str(value) in dependency_texts[cell_name] for value in values.values())

claimed_term_counts = {
    "danger": 1, "Delta": 1, "n": 2, "C0": 62,
    "C1": 67, "N0": 1851, "N1": 326, "ND": 84595,
}
claimed_majorants = {
    "danger": sp.Integer(0),
    "Delta": sp.Rational(103, 100),
    "n": sp.Rational(1090601, 10000),
    "C0": sp.Rational(3591519308424373, 3125000000000),
    "C1": sp.Rational(32111117681043527, 5000000000000),
    "N0": sp.Rational(98448296054638286971718220153709637, 12800000000000000000000),
    "N1": sp.Rational(452887170660359886538671, 256000000000000),
    "ND": sp.Rational(107209382767024034160962381222448011318186558450015706249449102691599869001, 51200000000000000000000000000000000000000000000),
}
claimed_minimum_reserves = {
    "danger": sp.Rational(87, 500),
    "Delta": sp.Rational(142087, 50000),
    "n": sp.Rational(1455662399, 5000000),
    "C0": sp.Rational(2088211787974020153, 6250000000000000),
    "C1": sp.Rational(2359087594843852059, 2500000000000000),
    "N0": sp.Rational(2688151350612835088318476618770634683, 6400000000000000000000000),
    "N1": sp.Rational(108078622965866619044505269, 640000000000000000),
    "ND": sp.Rational(26067639002996971408992668691597632280432456070529434555374912711048130999, 25600000000000000000000000000000000000000000000000),
}
coordinate_caps = (
    sp.Integer(10), sp.Rational(31, 100), sp.Rational(301, 100),
    sp.Rational(101, 100), sp.Rational(103, 100), sp.Rational(401, 100),
)
wide_left, wide_right = sp.Rational(399, 100), sp.Rational(401, 100)
radius = sp.Rational(1, 500)
target_left, target_right = 4 - radius, 4 + radius
assert (target_left, target_right) == (sp.Rational(1999, 500), sp.Rational(2001, 500))
assert wide_left <= target_left and target_right <= wide_right


def independent_power_majorant(expression):
    term_list = sp.Poly(sp.diff(expression, t), *variables, domain=sp.QQ).terms()
    total = sp.S.Zero
    for powers, coefficient in term_list:
        monomial_cap = sp.S.One
        for cap, power in zip(coordinate_caps, powers):
            monomial_cap *= cap**power
        total += abs(coefficient) * monomial_cap
    return len(term_list), sp.factor(total)


for name, expression in sign_polynomials:
    term_count, majorant = independent_power_majorant(expression)
    assert term_count == claimed_term_counts[name]
    assert majorant == claimed_majorants[name]
    cell_reserves = [
        sp.factor(values[name] - radius * majorant)
        for values in centers.values()
    ]
    assert all(value > 0 for value in cell_reserves)
    assert min(cell_reserves) == claimed_minimum_reserves[name]

shape_numerator_lower = (
    sp.Rational(99, 100) * wide_left
    - sp.Rational(99, 100)**2
    - 2 * (sp.Rational(101, 100)**2 + sp.Rational(31, 100)**2)
)
assert shape_numerator_lower == sp.Rational(461, 625) > 0

witness_data = {
    ell: 9, w: -sp.Rational(31, 100), k: -sp.Rational(301, 100),
    z: -sp.Rational(101, 100), r: sp.Rational(103, 100),
    t: sp.Rational(2001, 500), tau: 1,
}
witness = matrix.subs(witness_data)
assert sp.factor(witness.det()) == 0
assert Delta.subs(witness_data) == sp.Rational(150293, 50000)
assert n.subs(witness_data) == sp.Rational(1804751601, 5000000)
assert g.subs(witness_data) == sp.Rational(679, 10000)
assert witness[1, 1] == sp.Rational(1804751601, 15029300)
assert danger.subs(witness_data) == -sp.Rational(19, 100)
witness_gate = sp.factor(raw_gate(witness))
assert witness_gate == sp.Rational(414461983319631411704949, 112939929245000000000) > 0
real_witness = witness.applyfunc(sp.re)
assert sp.factor(4 * (witness_gate - raw_gate(real_witness))) == -sp.Rational(
    585660171418319979, 375732500000000
) < 0
assert sp.im(witness[0, 1]) * sp.im(witness[0, 2]) == -sp.Rational(279, 100)

print("PASS isolated audited-center dependency hashes and minima binding")
print("PASS isolated original-gate, PSD, cubic, and legal-half-line reconstruction")
print("PASS isolated eight-polynomial derivative majorants and exact reserves")
print("PASS isolated nonredundancy and phase-integrity witness")
print("scope=thin t partial theorem depending on audited center boxes; unrestricted gate open")
