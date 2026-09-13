#!/usr/bin/env python3
"""Fail-closed exact audit of the proposed p(r) cube-section candidate."""

from itertools import combinations

import sympy as sp


r = sp.symbols("r", real=True)
LO = sp.Rational(3233, 1000)
HI = sp.Rational(1617, 500)

p = r**6 - 21*r**4 + 48*r**3 - 48*r**2 + 32
h = r**6 - 12*r**5 + 51*r**4 - 96*r**3 + 96*r**2 - 64
A = r**6 - 16*r**5 + 101*r**4 - 336*r**3 + 736*r**2 - 1280*r + 1088
B = (5*r**8 - 48*r**7 + 169*r**6 - 336*r**5 + 504*r**4
     - 384*r**3 + 64*r**2 + 512)
WRONG_A = r**6 - 19*r**4 + 96*r**3 - 272*r**2 + 576*r - 544
WRONG_B = (5*r**8 - 47*r**6 + 96*r**5 - 216*r**4 + 192*r**3
           - 32*r**2 - 256)


def exact_zero(expr):
    assert sp.cancel(sp.together(expr)) == 0


def sign_constant_on_interval(linear_form):
    """Return its nonzero sign, or fail if the interval meets a wall."""
    left = sp.sign(linear_form.subs(r, LO))
    right = sp.sign(linear_form.subs(r, HI))
    assert left in (-1, 1) and right == left
    return int(left)


def rebuild_one_variable_numerator():
    # Unnormalized coordinates; homogeneity makes their half-sum T=(r+4)/2.
    coords = [r, 1, 1, 1, 1]
    threshold = sum(coords) / 2
    numerator = 0
    active_masks = []
    triple_small_contribution = 0
    for mask in range(1 << 5):
        subset_sum = sum(coords[i] for i in range(5) if mask & (1 << i))
        form = sp.expand(threshold - subset_sum)
        sign = sign_constant_on_interval(form)
        if sign > 0:
            cardinality = mask.bit_count()
            term = (-1)**cardinality * form**4
            numerator += term
            active_masks.append(mask)
            if not (mask & 1) and cardinality == 3:
                triple_small_contribution += term

    expected_masks = {0}
    expected_masks.update(1 << i for i in range(5))
    expected_masks.update((1 << i) | (1 << j) for i, j in combinations(range(1, 5), 2))
    expected_masks.update(sum(1 << i for i in triple) for triple in combinations(range(1, 5), 3))
    assert set(active_masks) == expected_masks

    true_p = -(r**4 - 16*r**3 + 96*r**2 - 256*r + 64) / 8
    omitted_p = (r**4 - 48*r**2 + 192*r - 32) / 8
    exact_zero(numerator - true_p)
    exact_zero(numerator - triple_small_contribution - omitted_p)
    assert sp.factor(triple_small_contribution) == -(r - 2)**4 / 4
    return sp.expand(numerator), sp.expand(numerator - triple_small_contribution)


def verify_critical_polynomials(true_p, omitted_p):
    scale = sp.sqrt(r*r + 4)
    true_f = scale * true_p / (24*r)
    omitted_f = scale * omitted_p / (24*r)
    exact_zero(sp.diff(true_f, r) + h / (48*r*r*scale))
    exact_zero(sp.diff(omitted_f, r) - p / (48*r*r*scale))

    assert sp.Poly(p, r).count_roots(LO, HI) == 1
    assert p.subs(r, LO) < 0 < p.subs(r, HI)
    assert sp.Poly(h, r).count_roots(2, 4) == 0
    assert h.subs(r, 2) == 48
    assert sp.resultant(p, h, r) == -697143656448


def full_chamber_polynomial(variables):
    """P_N for N={01,02,03,04}, reconstructed from paired subsets."""
    threshold = sum(variables) / 2
    numerator = threshold**4 - sum((threshold - x)**4 for x in variables)
    numerator += sum(
        (threshold - variables[i] - variables[j])**4
        for i, j in combinations(range(5), 2)
    )
    numerator -= 2 * sum(
        (threshold - variables[0] - variables[j])**4 for j in range(1, 5)
    )
    return sp.expand(numerator)


def verify_full_gradient_and_hessian():
    variables = sp.symbols("a0:5", positive=True)
    numerator = full_chamber_polynomial(variables)
    norm = sp.sqrt(sum(x*x for x in variables))
    volume = norm * numerator / (24 * sp.prod(variables))
    point = {variables[0]: r, **{variables[j]: 1 for j in range(1, 5)}}
    scale = sp.sqrt(r*r + 4)

    gradient = [sp.factor(sp.diff(volume, x).subs(point)) for x in variables]
    exact_zero(gradient[0] + h / (48*r*r*scale))
    for component in gradient[1:]:
        exact_zero(component - h / (192*r*scale))
    exact_zero(r*gradient[0] + sum(gradient[1:]))

    hessian = sp.hessian(volume, variables).subs(point)
    sphere_scale = r*r + 4  # H at unit normalization is S times H at b.
    small_vector = sp.Matrix([0, 1, -1, 0, 0])
    block_vector = sp.Matrix([4, -r, -r, -r, -r])
    small_rayleigh = sp.factor(
        sphere_scale * (small_vector.T * hessian * small_vector)[0]
        / small_vector.dot(small_vector)
    )
    block_rayleigh = sp.factor(
        sphere_scale * (block_vector.T * hessian * block_vector)[0]
        / block_vector.dot(block_vector)
    )
    exact_zero(small_rayleigh + scale*A/(192*r))
    exact_zero(block_rayleigh + scale*B/(192*r**3))

    assert sp.Poly(A, r).count_roots(LO, HI) == 0
    assert sp.Poly(B, r).count_roots(LO, HI) == 0
    assert A.subs(r, LO) < 0
    assert B.subs(r, LO) > 0


def verify_omitted_formula_hessian():
    variables = sp.symbols("w0:5", positive=True)
    threshold = sum(variables) / 2
    # This is precisely the erroneous active-set sum: it stops after the six
    # small-small pairs and omits the four active small triples.
    omitted_numerator = threshold**4 - sum((threshold - x)**4 for x in variables)
    omitted_numerator += sum(
        (threshold - variables[i] - variables[j])**4
        for i, j in combinations(range(1, 5), 2)
    )
    norm = sp.sqrt(sum(x*x for x in variables))
    omitted_volume = norm * omitted_numerator / (24 * sp.prod(variables))
    point = {variables[0]: r, **{variables[j]: 1 for j in range(1, 5)}}
    scale = sp.sqrt(r*r + 4)
    sphere_scale = r*r + 4
    hessian = sp.hessian(omitted_volume, variables).subs(point)
    small_vector = sp.Matrix([0, 1, -1, 0, 0])
    block_vector = sp.Matrix([4, -r, -r, -r, -r])
    small_rayleigh = sp.factor(
        sphere_scale * (small_vector.T * hessian * small_vector)[0]
        / small_vector.dot(small_vector)
    )
    block_rayleigh = sp.factor(
        sphere_scale * (block_vector.T * hessian * block_vector)[0]
        / block_vector.dot(block_vector)
    )
    exact_zero(small_rayleigh - scale*WRONG_A/(192*r))
    exact_zero(block_rayleigh - scale*WRONG_B/(192*r**3))
    for polynomial in (WRONG_A, WRONG_B):
        assert sp.Poly(polynomial, r).count_roots(LO, HI) == 0
        assert polynomial.subs(r, LO) > 0


def verify_sum_normalized_formula(true_p, omitted_p):
    c = 2 / (r + 4)
    x, y = r*c, c
    direct = 1 - (1-x)**4 - 4*(1-y)**4 + 6*(1-2*y)**4 - 4*(1-3*y)**4
    direct_omitted = direct + 4*(1-3*y)**4
    exact_zero(direct - c**4 * true_p)
    exact_zero(direct_omitted - c**4 * omitted_p)


def main():
    true_p, omitted_p = rebuild_one_variable_numerator()
    verify_critical_polynomials(true_p, omitted_p)
    verify_sum_normalized_formula(true_p, omitted_p)
    verify_full_gradient_and_hessian()
    verify_omitted_formula_hessian()
    print("rebuttal exact checks: PASS")


if __name__ == "__main__":
    main()
