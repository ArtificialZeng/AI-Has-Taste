#!/usr/bin/env python3
from fractions import Fraction
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from builder_coinvariant import CoinvariantModel, Field, SparseReducer, expected_ambient_dimension


def test_artin_reduction_n2():
    model = CoinvariantModel(2)
    assert model.reduce_polynomial_monomial((1, 0)) == {(0, 1): -1}
    assert model.reduce_polynomial_monomial((0, 2)) == {}
    assert model.reduce_polynomial_monomial((1, 1)) == {}


def test_exterior_signs():
    model = CoinvariantModel(3)
    one = (0, 0, 0)
    theta_2 = (one, 1 << 1, 0)
    xi_3 = (one, 0, 1 << 2)
    assert model.multiply_monomials(theta_2, xi_3) == {((0, 0, 0), 2, 4): 1}
    assert model.multiply_monomials(xi_3, theta_2) == {((0, 0, 0), 2, 4): -1}
    assert model.multiply_monomials(theta_2, theta_2) == {}


def test_sparse_rational_reducer():
    rr = SparseReducer(Field())
    assert rr.add({0: 2, 1: 4})
    assert not rr.add({0: 1, 1: 2})
    assert rr.add({1: 3})
    assert rr.rank == 2
    assert rr.reduce({0: Fraction(7, 3), 1: -9}) == {}


def test_candidate_cardinalities_and_bounds():
    for n in range(1, 6):
        model = CoinvariantModel(n)
        candidate = model.candidate_monomials()
        assert len(candidate) == (1 << (n - 1)) * __import__("math").factorial(n)
        assert len(set(candidate)) == len(candidate)
        for exponent, theta, xi in candidate:
            assert not (theta & 1)
            assert not (xi & 1)
            assert all(exponent[i] <= i for i in range(n))
        assert len(model.poly_basis) * (1 << (2 * n)) == expected_ambient_dimension(n)


def test_reynolds_is_invariant_small():
    model = CoinvariantModel(3)
    field = Field()
    block = (1, 1, 0)
    basis = model.block_basis(block)
    reynolds = model.reynolds(basis[1], block, field)
    # Reynolds is unchanged after multiplying its coefficients by |S_n| via
    # another Reynolds application; this checks the signed action convention.
    accumulated = {}
    for col, coeff in reynolds.items():
        image = model.reynolds(basis[col], block, field)
        for target, value in image.items():
            accumulated[target] = accumulated.get(target, 0) + coeff * value
    assert accumulated == {col: 6 * coeff for col, coeff in reynolds.items()}


def test_symmetric_group_action_small():
    model = CoinvariantModel(3)
    block = (2, 1, 1)
    basis = model.block_basis(block)
    index = model.block_index(block)
    adjacent = [(1, 0, 2), (0, 2, 1)]
    # Apply each adjacent transposition twice to every basis monomial.
    for perm in adjacent:
        for monomial in basis:
            first = {}
            sign_t, theta = model.permute_mask(monomial[1], perm)
            sign_s, xi = model.permute_mask(monomial[2], perm)
            for exponent, coeff in model.permute_polynomial(monomial[0], perm).items():
                first[(exponent, theta, xi)] = sign_t * sign_s * coeff
            second = {}
            for image_monomial, scalar in first.items():
                sign_t, theta = model.permute_mask(image_monomial[1], perm)
                sign_s, xi = model.permute_mask(image_monomial[2], perm)
                for exponent, coeff in model.permute_polynomial(image_monomial[0], perm).items():
                    target = (exponent, theta, xi)
                    second[target] = second.get(target, 0) + scalar * sign_t * sign_s * coeff
            assert {key: value for key, value in second.items() if value} == {monomial: 1}


def test_total_invariant_dimension_small():
    # C_n's polynomial factor is the regular S_n representation, hence
    # dim(C_n^S_n) = dim Exterior(theta,xi) = 4^n.
    for n in (2, 3):
        model = CoinvariantModel(n)
        total = 0
        for block in model.all_blocks():
            total += len(model.invariant_basis(block, Field()))
        assert total == 4**n


def test_signed_stabilizer_can_kill_reynolds_sum():
    model = CoinvariantModel(2)
    field = Field()
    top_theta = ((0, 0), 0b11, 0)
    assert model.reynolds(top_theta, (0, 2, 0), field) == {}
    theta_1 = ((0, 0), 0b01, 0)
    assert model.reynolds(theta_1, (0, 1, 0), field) != {}


def test_coxeter_relations_on_full_small_model():
    model = CoinvariantModel(3)

    def act(vector, perm, block):
        basis = model.block_basis(block)
        index = model.block_index(block)
        out = {}
        for col, scalar in vector.items():
            monomial = basis[col]
            sign_t, theta = model.permute_mask(monomial[1], perm)
            sign_s, xi = model.permute_mask(monomial[2], perm)
            for exponent, coeff in model.permute_polynomial(monomial[0], perm).items():
                target = index[(exponent, theta, xi)]
                out[target] = out.get(target, 0) + scalar * sign_t * sign_s * coeff
        return {col: coeff for col, coeff in out.items() if coeff}

    s1, s2 = (1, 0, 2), (0, 2, 1)
    for block in model.all_blocks():
        basis = model.block_basis(block)
        for col in range(len(basis)):
            vector = {col: 1}
            assert act(act(vector, s1, block), s1, block) == vector
            assert act(act(vector, s2, block), s2, block) == vector
            left = act(act(act(vector, s1, block), s2, block), s1, block)
            right = act(act(act(vector, s2, block), s1, block), s2, block)
            assert left == right


if __name__ == "__main__":
    tests = [value for name, value in sorted(globals().items()) if name.startswith("test_")]
    for test in tests:
        test()
    print(f"PASS {len(tests)} builder tests")
