#!/opt/anaconda3/bin/python3
"""Build the exact certificate for the ordered Q5 star1 chamber.

This is a prover, not a numerical search.  It starts with the subset-sum
polynomial, differentiates it over QQ, converts one necessary linear
combination of the four critical equations to the degree-nine simplex
Bernstein basis, and decomposes a residual zero-dimensional ideal over QQ.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import sympy as sp


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def encode_poly(expr: sp.Expr, variables: tuple[sp.Symbol, ...]) -> list[list[int]]:
    """Sparse QQ polynomial: exponents, numerator, positive denominator."""
    out: list[list[int]] = []
    for exponents, coefficient in sp.Poly(sp.cancel(expr), *variables, domain=sp.QQ).terms():
        coefficient = sp.Rational(coefficient)
        out.append([*map(int, exponents), int(coefficient.p), int(coefficient.q)])
    return out


def primitive_integer(expr: sp.Expr, variable: sp.Symbol) -> sp.Expr:
    poly = sp.Poly(expr, variable, domain=sp.QQ)
    denominator = sp.ilcm(1, *[sp.denom(c) for c in poly.all_coeffs()])
    integer_poly = sp.Poly(sp.expand(denominator * poly.as_expr()), variable, domain=sp.ZZ)
    content, primitive = integer_poly.primitive()
    del content
    result = primitive.as_expr()
    if sp.LC(sp.Poly(result, variable)) < 0:
        result = -result
    return sp.expand(result)


def multinomial(degree: int, i: int, j: int) -> int:
    return math.factorial(degree) // (
        math.factorial(i) * math.factorial(j) * math.factorial(degree - i - j)
    )


def simplex_bernstein(
    polynomial: sp.Expr,
    x: sp.Symbol,
    z: sp.Symbol,
    degree: int,
) -> dict[tuple[int, int], sp.Expr]:
    power = sp.Poly(polynomial, x, z)
    require(power.total_degree() <= degree, "Bernstein degree is too small")
    answer: dict[tuple[int, int], sp.Expr] = {}
    for i in range(degree + 1):
        for j in range(degree + 1 - i):
            value = 0
            for p in range(i + 1):
                for q in range(j + 1):
                    value += (
                        power.coeff_monomial(x**p * z**q)
                        * sp.binomial(i, p)
                        * sp.binomial(j, q)
                        / multinomial(degree, p, q)
                    )
            answer[i, j] = sp.cancel(value)
    reconstructed = sum(
        value
        * multinomial(degree, i, j)
        * x**i
        * z**j
        * (1 - x - z) ** (degree - i - j)
        for (i, j), value in answer.items()
    )
    require(sp.expand(reconstructed - polynomial) == 0, "Bernstein reconstruction failed")
    return answer


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: builder_build_star1_certificate.py OUTPUT.json", file=sys.stderr)
        return 2
    output = Path(sys.argv[1])

    x, y, z, w, u = sp.symbols("x y z w u")
    coordinates = [
        1 + w + z + y + x,
        1 + w + z + y,
        1 + w + z,
        1 + w,
        sp.Integer(1),
    ]
    total = sum(coordinates)
    T = total / 2
    S = sum(value**2 for value in coordinates)
    D = sp.prod(coordinates)

    # N={(0,1)}.  This is reconstructed directly from the paired
    # truncated-power formula; no discovery polynomial is imported.
    P = sp.expand(
        T**4
        - sum((T - value) ** 4 for value in coordinates)
        + sum(
            (T - coordinates[i] - coordinates[j]) ** 4
            for i in range(5)
            for j in range(i + 1, 5)
        )
        - 2 * (T - coordinates[0] - coordinates[1]) ** 4
    )
    variables = (x, y, z, w)
    H = [
        sp.expand(
            sp.diff(S, variable) * P * D
            + 2 * S * sp.diff(P, variable) * D
            - 2 * S * P * sp.diff(D, variable)
        )
        for variable in variables
    ]

    chart = {y: (1 - x - z) / 2 + u}
    Hc = [sp.expand(value.subs(chart)) for value in H]
    K = sp.expand(-6 * Hc[0] + 7 * Hc[1] - 8 * Hc[2] + 4 * Hc[3])
    bernstein = simplex_bernstein(K, x, z, 9)
    require(bernstein[0, 0] == 0, "the exceptional Bernstein coefficient is not zero")
    for index, value in bernstein.items():
        if index == (0, 0):
            continue
        terms = sp.Poly(value, u, w, domain=sp.QQ).terms()
        require(terms, f"empty Bernstein coefficient {index}")
        require(all(coefficient > 0 for _, coefficient in terms), f"nonpositive term at {index}")
        require(sp.Poly(value, u, w).coeff_monomial(1) > 0, f"missing constant at {index}")

    bernstein_rows = [
        {
            "i": i,
            "j": j,
            "terms_u_w": encode_poly(bernstein[i, j], (u, w)),
        }
        for i in range(10)
        for j in range(10 - i)
    ]
    bernstein_blob = json.dumps(bernstein_rows, separators=(",", ":"), sort_keys=True).encode()

    # At x=z=0 the first and third original gap equations have positive
    # factors on u,w>=0.  Divide those factors exactly to obtain A and B.
    residual = [sp.factor(value.subs({x: 0, z: 0})) for value in Hc]
    A = sp.cancel(16 * residual[0] / ((w + 1) ** 2 * (2 * u + 2 * w + 3)))
    B = sp.cancel(-16 * residual[2] / ((w + 1) * (2 * u + 2 * w + 3)))
    require(sp.denom(A) == 1 and sp.denom(B) == 1, "residual division was not exact")
    A, B = sp.expand(A), sp.expand(B)

    groebner = sp.groebner([A, B], w, u, order="lex", domain=sp.QQ)
    require(len(groebner.polys) == 2, "unexpected residual Groebner basis length")
    univariate_candidates = [
        value.as_expr() for value in groebner.polys if sp.degree(value.as_expr(), w) == 0
    ]
    graph_candidates = [
        value.as_expr() for value in groebner.polys if sp.degree(value.as_expr(), w) == 1
    ]
    require(len(univariate_candidates) == len(graph_candidates) == 1, "basis is not a graph")
    U = sp.Poly(univariate_candidates[0], u, domain=sp.QQ).monic().as_expr()
    graph_raw = sp.Poly(graph_candidates[0], w, u, domain=sp.QQ)
    graph_w_coefficient = graph_raw.coeff_monomial(w)
    require(graph_w_coefficient != 0, "graph equation has zero w coefficient")
    graph = sp.expand(graph_raw.as_expr() / graph_w_coefficient)
    factor_data = sp.factor_list(U, u)[1]
    require(all(exponent == 1 for _, exponent in factor_data), "univariate basis is not squarefree")
    require(sum(sp.degree(factor, u) for factor, _ in factor_data) == 15, "wrong residual degree")

    components: list[dict[str, object]] = []
    graph_tail = sp.expand(graph.subs(w, 0))
    for rational_factor, exponent in factor_data:
        del exponent
        q = primitive_integer(rational_factor, u)
        remainder = sp.rem(graph_tail, q, domain=sp.QQ)
        relation = w + remainder
        relation_poly = sp.Poly(relation, w, u, domain=sp.QQ)
        denominator = sp.ilcm(1, *[sp.denom(c) for c in relation_poly.coeffs()])
        relation_integer = sp.Poly(sp.expand(denominator * relation), w, u, domain=sp.ZZ)
        _, relation_primitive = relation_integer.primitive()
        relation = relation_primitive.as_expr()
        if sp.Poly(relation, w, u).coeff_monomial(w) < 0:
            relation = -relation
        components.append(
            {
                "u_factor": encode_poly(q, (u,)),
                "w_relation": encode_poly(sp.expand(relation), (w, u)),
            }
        )
    components.sort(key=lambda row: (len(row["u_factor"]), row["u_factor"]))

    resultant = sp.factor(sp.resultant(A, B, u))
    resultant_content, resultant_factors = sp.factor_list(resultant, w)

    # Exact chamber margins.  The sign convention is positive in the
    # closure: high margin for 01, low margin for every other pair.
    chart_coordinates = [sp.expand(value.subs(chart)) for value in coordinates]
    chart_total = sp.expand(sum(chart_coordinates))
    margins: list[dict[str, object]] = []
    for i in range(5):
        for j in range(i + 1, 5):
            if (i, j) == (0, 1):
                margin = 2 * (chart_coordinates[i] + chart_coordinates[j]) - chart_total
                kind = "high"
            else:
                margin = chart_total - 2 * (chart_coordinates[i] + chart_coordinates[j])
                kind = "low"
            margins.append(
                {
                    "pair": [i, j],
                    "kind": kind,
                    "polynomial_x_z_u_w": encode_poly(sp.expand(margin), (x, z, u, w)),
                }
            )

    certificate = {
        "schema": "q5-star1-exact-v1",
        "normalization": "a4=1",
        "chamber": "N={(0,1)} ordered closure",
        "chart": {
            "gap_order": ["x=a0-a1", "y=a1-a2", "z=a2-a3", "w=a3-a4"],
            "substitution": "y=(1-x-z)/2+u",
            "domain": ["x>=0", "z>=0", "x+z<=1", "u>=0", "w>=0"],
            "pair_margins": margins,
        },
        "critical_equations": {
            "variable_order": ["x", "y", "z", "w"],
            "cleared_derivative": "Hq=S_q*P*D+2*S*P_q*D-2*S*P*D_q",
            "combination": [-6, 7, -8, 4],
        },
        "bernstein": {
            "degree": 9,
            "basis": "multinomial(9;i,j,9-i-j)*x^i*z^j*(1-x-z)^(9-i-j)",
            "parameter_order": ["u", "w"],
            "rows": bernstein_rows,
            "rows_sha256": hashlib.sha256(bernstein_blob).hexdigest(),
        },
        "residual_necessary_ideal": {
            "variable_order": ["u", "w"],
            "A": encode_poly(A, (u, w)),
            "B": encode_poly(B, (u, w)),
            "complex_degree": 15,
            "components": components,
            "resultant_u": {
                "content": [int(sp.numer(resultant_content)), int(sp.denom(resultant_content))],
                "factors": [
                    {
                        "polynomial_w": encode_poly(primitive_integer(factor, w), (w,)),
                        "exponent": int(exponent),
                    }
                    for factor, exponent in resultant_factors
                ],
            },
        },
        "surviving_component": {
            "w": 0,
            "u_polynomial_ascending": [-15, -36, 52],
            "u_positive_root": "(9+2*sqrt(69))/26",
            "alpha": "u+3/2=(24+sqrt(69))/13",
            "alpha_polynomial_ascending": [39, -48, 13],
            "alpha_isolating_interval": [[12, 5], [5, 2]],
            "normalized_coordinates": ["alpha", "alpha", "1", "1", "1"],
        },
        "hessian": {
            "matrix_formula": "Mij=deltaij/S-2*ai*aj/S^2+Pij/P-Pi*Pj/P^2+deltaij/ai^2",
            "tangent_vectors": {
                "large_block": ["1", "-1", "0", "0", "0"],
                "small_block": ["0", "0", "1", "-1", "0"],
                "block_contrast": ["3", "3", "-2*alpha", "-2*alpha", "-2*alpha"],
            },
            "reduced_quadratic_forms_mod_13alpha2-48alpha+39": {
                "large_block": {
                    "linear_numerator_ascending": [-54388, -71136],
                    "denominator": 864435,
                    "sign": "negative",
                },
                "small_block": {
                    "linear_numerator_ascending": [-5468, 1664],
                    "denominator": 66495,
                    "sign": "negative",
                },
                "block_contrast": {
                    "linear_numerator_ascending": [-2580, 1248],
                    "denominator": 169,
                    "sign": "positive",
                },
            },
            "symmetry_dimensions": {"large_block": 1, "small_block": 2, "block_contrast": 1},
            "tangent_signature": ["negative", "negative", "negative", "positive"],
        },
    }
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(
        "WROTE",
        output,
        "bernstein_rows=55",
        "bernstein_terms=" + str(sum(len(row["terms_u_w"]) for row in bernstein_rows)),
        "components=" + str(len(components)),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
