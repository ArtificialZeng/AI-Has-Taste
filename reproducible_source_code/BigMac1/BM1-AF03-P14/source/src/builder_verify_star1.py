#!/opt/anaconda3/bin/python3
"""Fail-closed independent verifier for the exact Q5 star1 certificate."""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Any

import sympy as sp


class Rejected(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise Rejected(message)


def exact_keys(value: Any, keys: set[str], context: str) -> None:
    require(isinstance(value, dict), f"{context}: expected object")
    require(set(value) == keys, f"{context}: wrong fields")


def reject_duplicate_object_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    """Reject duplicate JSON keys instead of silently keeping the last."""
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise Rejected(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_int(value: Any, context: str) -> int:
    require(isinstance(value, int) and not isinstance(value, bool), f"{context}: expected integer")
    return value


def decode_poly(rows: Any, variables: tuple[sp.Symbol, ...], context: str) -> sp.Expr:
    require(isinstance(rows, list) and rows, f"{context}: expected nonempty sparse list")
    exponents_seen: set[tuple[int, ...]] = set()
    exponent_sequence: list[tuple[int, ...]] = []
    expression = 0
    for row_index, row in enumerate(rows):
        require(isinstance(row, list) and len(row) == len(variables) + 2, f"{context}[{row_index}]: bad row")
        exponents = tuple(strict_int(e, f"{context}[{row_index}] exponent") for e in row[:-2])
        require(all(e >= 0 for e in exponents), f"{context}[{row_index}]: negative exponent")
        numerator = strict_int(row[-2], f"{context}[{row_index}] numerator")
        denominator = strict_int(row[-1], f"{context}[{row_index}] denominator")
        require(denominator > 0, f"{context}[{row_index}]: nonpositive denominator")
        require(math.gcd(abs(numerator), denominator) == 1, f"{context}[{row_index}]: noncanonical rational")
        require(exponents not in exponents_seen, f"{context}: duplicate monomial")
        exponents_seen.add(exponents)
        exponent_sequence.append(exponents)
        monomial = sp.prod(variable**exponent for variable, exponent in zip(variables, exponents))
        expression += sp.Rational(numerator, denominator) * monomial
    require(exponent_sequence == sorted(exponent_sequence, reverse=True), f"{context}: noncanonical term order")
    if len(rows) == 1 and all(e == 0 for e in exponent_sequence[0]) and rows[0][-2] == 0:
        require(rows[0][-1] == 1, f"{context}: noncanonical zero")
    else:
        require(all(row[-2] != 0 for row in rows), f"{context}: embedded zero term")
    return sp.expand(expression)


def multinomial(degree: int, i: int, j: int) -> int:
    return math.factorial(degree) // (
        math.factorial(i) * math.factorial(j) * math.factorial(degree - i - j)
    )


def primitive_integer(expr: sp.Expr, variable: sp.Symbol) -> sp.Expr:
    poly = sp.Poly(expr, variable, domain=sp.QQ)
    denominator = sp.ilcm(1, *[sp.denom(c) for c in poly.all_coeffs()])
    integer = sp.Poly(sp.expand(denominator * poly.as_expr()), variable, domain=sp.ZZ)
    _, primitive = integer.primitive()
    result = primitive.as_expr()
    if sp.LC(sp.Poly(result, variable)) < 0:
        result = -result
    return sp.expand(result)


def algebraic_reduce_rational(expr: sp.Expr, modulus: sp.Expr, variable: sp.Symbol) -> sp.Expr:
    numerator, denominator = sp.fraction(sp.cancel(expr))
    numerator = sp.rem(numerator, modulus, variable, domain=sp.QQ)
    denominator = sp.rem(denominator, modulus, variable, domain=sp.QQ)
    require(sp.gcd(denominator, modulus) == 1, "Hessian denominator vanishes in the number field")
    inverse = sp.invert(denominator, modulus, domain=sp.QQ)
    return sp.factor(sp.rem(numerator * inverse, modulus, variable, domain=sp.QQ))


def verify(path: Path) -> None:
    try:
        certificate = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_object_keys,
        )
    except Exception as exc:
        raise Rejected(f"cannot parse certificate: {exc}") from exc

    exact_keys(
        certificate,
        {
            "schema",
            "normalization",
            "chamber",
            "chart",
            "critical_equations",
            "bernstein",
            "residual_necessary_ideal",
            "surviving_component",
            "hessian",
        },
        "root",
    )
    require(certificate["schema"] == "q5-star1-exact-v1", "wrong schema")
    require(certificate["normalization"] == "a4=1", "wrong normalization")
    require(certificate["chamber"] == "N={(0,1)} ordered closure", "wrong chamber")

    x, y, z, w, u = sp.symbols("x y z w u")
    coordinates = [1 + w + z + y + x, 1 + w + z + y, 1 + w + z, 1 + w, sp.Integer(1)]
    T = sum(coordinates) / 2
    S = sum(value**2 for value in coordinates)
    D = sp.prod(coordinates)
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
    gap_variables = (x, y, z, w)
    H = [
        sp.expand(
            sp.diff(S, variable) * P * D
            + 2 * S * sp.diff(P, variable) * D
            - 2 * S * P * sp.diff(D, variable)
        )
        for variable in gap_variables
    ]
    chart_substitution = {y: (1 - x - z) / 2 + u}
    Hc = [sp.expand(value.subs(chart_substitution)) for value in H]

    chart = certificate["chart"]
    exact_keys(chart, {"gap_order", "substitution", "domain", "pair_margins"}, "chart")
    require(
        chart["gap_order"] == ["x=a0-a1", "y=a1-a2", "z=a2-a3", "w=a3-a4"],
        "wrong gap chart",
    )
    require(chart["substitution"] == "y=(1-x-z)/2+u", "wrong chart substitution")
    require(chart["domain"] == ["x>=0", "z>=0", "x+z<=1", "u>=0", "w>=0"], "wrong domain")
    margins = chart["pair_margins"]
    require(isinstance(margins, list) and len(margins) == 10, "wrong pair-margin count")
    chart_coordinates = [sp.expand(value.subs(chart_substitution)) for value in coordinates]
    chart_total = sp.expand(sum(chart_coordinates))
    for row_index, row in enumerate(margins):
        exact_keys(row, {"pair", "kind", "polynomial_x_z_u_w"}, f"margin[{row_index}]")
        i, j = divmod(0, 1)  # overwritten below; keeps both names local and typed
        require(
            isinstance(row["pair"], list)
            and len(row["pair"]) == 2
            and all(isinstance(v, int) and not isinstance(v, bool) for v in row["pair"]),
            f"margin[{row_index}]: bad pair",
        )
        i, j = row["pair"]
        require(0 <= i < j < 5, f"margin[{row_index}]: invalid pair")
        expected_pair = [(i0, j0) for i0 in range(5) for j0 in range(i0 + 1, 5)][row_index]
        require((i, j) == expected_pair, f"margin[{row_index}]: wrong ordering")
        if (i, j) == (0, 1):
            require(row["kind"] == "high", "01 must be the high pair")
            expected = 2 * (chart_coordinates[i] + chart_coordinates[j]) - chart_total
        else:
            require(row["kind"] == "low", f"{i}{j} must be a low pair")
            expected = chart_total - 2 * (chart_coordinates[i] + chart_coordinates[j])
        observed = decode_poly(row["polynomial_x_z_u_w"], (x, z, u, w), f"margin[{row_index}]")
        require(sp.expand(observed - expected) == 0, f"margin[{row_index}]: polynomial mismatch")

    # These exact margins prove that the advertised five inequalities are
    # equivalent to the entire ordered star1 closure.
    margin_by_pair = {
        tuple(row["pair"]): decode_poly(row["polynomial_x_z_u_w"], (x, z, u, w), "margin repeat")
        for row in margins
    }
    require(margin_by_pair[0, 1] == 2 * u, "high-pair wall identity failed")
    require(margin_by_pair[0, 2] == 1 - x - z, "02 wall identity failed")
    for pair, expression in margin_by_pair.items():
        if pair in {(0, 1), (0, 2)}:
            continue
        # A linear polynomial on the (x,z)-simplex is nonnegative iff its
        # three degree-one Bernstein coefficients (its vertex values) are.
        for vertex in ({x: 0, z: 0}, {x: 1, z: 0}, {x: 0, z: 1}):
            vertex_value = sp.Poly(sp.expand(expression.subs(vertex)), u, w, domain=sp.QQ)
            require(
                all(coefficient >= 0 for _, coefficient in vertex_value.terms()),
                f"pair {pair} not implied by chart inequalities",
            )

    critical = certificate["critical_equations"]
    exact_keys(critical, {"variable_order", "cleared_derivative", "combination"}, "critical_equations")
    require(critical["variable_order"] == ["x", "y", "z", "w"], "wrong critical variable order")
    require(
        critical["cleared_derivative"] == "Hq=S_q*P*D+2*S*P_q*D-2*S*P*D_q",
        "wrong derivative convention",
    )
    require(critical["combination"] == [-6, 7, -8, 4], "wrong critical combination")
    K = sp.expand(sum(c * h for c, h in zip(critical["combination"], Hc)))

    bernstein = certificate["bernstein"]
    exact_keys(bernstein, {"degree", "basis", "parameter_order", "rows", "rows_sha256"}, "bernstein")
    require(bernstein["degree"] == 9, "wrong Bernstein degree")
    require(
        bernstein["basis"]
        == "multinomial(9;i,j,9-i-j)*x^i*z^j*(1-x-z)^(9-i-j)",
        "wrong Bernstein basis",
    )
    require(bernstein["parameter_order"] == ["u", "w"], "wrong Bernstein parameter order")
    rows = bernstein["rows"]
    require(isinstance(rows, list) and len(rows) == 55, "wrong Bernstein row count")
    expected_row_order = [(i, j) for i in range(10) for j in range(10 - i)]
    require(
        [
            (
                strict_int(row.get("i"), f"bernstein row {index} i"),
                strict_int(row.get("j"), f"bernstein row {index} j"),
            )
            if isinstance(row, dict)
            else (-1, -1)
            for index, row in enumerate(rows)
        ]
        == expected_row_order,
        "noncanonical Bernstein row order",
    )
    rows_blob = json.dumps(rows, separators=(",", ":"), sort_keys=True).encode()
    require(
        isinstance(bernstein["rows_sha256"], str)
        and len(bernstein["rows_sha256"]) == 64
        and hashlib.sha256(rows_blob).hexdigest() == bernstein["rows_sha256"],
        "Bernstein table digest mismatch",
    )
    coefficients: dict[tuple[int, int], sp.Expr] = {}
    for row_index, row in enumerate(rows):
        exact_keys(row, {"i", "j", "terms_u_w"}, f"bernstein row {row_index}")
        i = strict_int(row["i"], f"bernstein row {row_index} i")
        j = strict_int(row["j"], f"bernstein row {row_index} j")
        require(0 <= i <= 9 and 0 <= j <= 9 - i, f"bernstein row {row_index}: bad index")
        require((i, j) not in coefficients, "duplicate Bernstein index")
        coefficients[i, j] = decode_poly(row["terms_u_w"], (u, w), f"bernstein[{i},{j}]")
    require(set(coefficients) == {(i, j) for i in range(10) for j in range(10 - i)}, "incomplete table")
    require(coefficients[0, 0] == 0, "b_00 must vanish")
    for index, value in coefficients.items():
        if index == (0, 0):
            continue
        polynomial = sp.Poly(value, u, w, domain=sp.QQ)
        require(all(coefficient > 0 for _, coefficient in polynomial.terms()), f"{index}: nonpositive coefficient")
        require(polynomial.coeff_monomial(1) > 0, f"{index}: constant coefficient is not positive")
    reconstructed = sum(
        value
        * multinomial(9, i, j)
        * x**i
        * z**j
        * (1 - x - z) ** (9 - i - j)
        for (i, j), value in coefficients.items()
    )
    require(sp.expand(reconstructed - K) == 0, "Bernstein identity does not reconstruct K")

    residual = certificate["residual_necessary_ideal"]
    exact_keys(
        residual,
        {"variable_order", "A", "B", "complex_degree", "components", "resultant_u"},
        "residual ideal",
    )
    require(residual["variable_order"] == ["u", "w"], "wrong residual variable order")
    require(residual["complex_degree"] == 15, "wrong residual degree claim")
    observed_A = decode_poly(residual["A"], (u, w), "A")
    observed_B = decode_poly(residual["B"], (u, w), "B")
    H_at_face = [sp.factor(value.subs({x: 0, z: 0})) for value in Hc]
    expected_A = sp.cancel(16 * H_at_face[0] / ((w + 1) ** 2 * (2 * u + 2 * w + 3)))
    expected_B = sp.cancel(-16 * H_at_face[2] / ((w + 1) * (2 * u + 2 * w + 3)))
    require(sp.denom(expected_A) == sp.denom(expected_B) == 1, "face factor division failed")
    require(sp.expand(observed_A - expected_A) == 0, "A is not reconstructed from H_x")
    require(sp.expand(observed_B - expected_B) == 0, "B is not reconstructed from H_z")
    A, B = observed_A, observed_B

    resultant_data = residual["resultant_u"]
    exact_keys(resultant_data, {"content", "factors"}, "resultant")
    require(
        isinstance(resultant_data["content"], list) and len(resultant_data["content"]) == 2,
        "bad resultant content",
    )
    content_numerator = strict_int(resultant_data["content"][0], "resultant content numerator")
    content_denominator = strict_int(resultant_data["content"][1], "resultant content denominator")
    require(content_denominator > 0, "bad resultant content denominator")
    require(
        math.gcd(abs(content_numerator), content_denominator) == 1,
        "noncanonical resultant content",
    )
    encoded_resultant = sp.Rational(content_numerator, content_denominator)
    factors = resultant_data["factors"]
    require(isinstance(factors, list) and len(factors) == 5, "wrong resultant factor count")
    for factor_index, factor_row in enumerate(factors):
        exact_keys(factor_row, {"polynomial_w", "exponent"}, f"resultant factor {factor_index}")
        factor = decode_poly(factor_row["polynomial_w"], (w,), f"resultant factor {factor_index}")
        exponent = strict_int(factor_row["exponent"], f"resultant exponent {factor_index}")
        require(exponent > 0, "nonpositive resultant exponent")
        require(sp.Poly(factor, w, domain=sp.QQ).is_irreducible, "reducible resultant factor")
        encoded_resultant *= factor**exponent
    actual_resultant = sp.resultant(A, B, u)
    require(sp.expand(encoded_resultant - actual_resultant) == 0, "resultant factorization mismatch")

    groebner = sp.groebner([A, B], w, u, order="lex", domain=sp.QQ)
    require(len(groebner.polys) == 2, "residual basis is not triangular")
    univariate = [p.as_expr() for p in groebner.polys if sp.degree(p.as_expr(), w) == 0]
    graphs = [p.as_expr() for p in groebner.polys if sp.degree(p.as_expr(), w) == 1]
    require(len(univariate) == len(graphs) == 1, "residual basis is not a graph over u")
    U = sp.Poly(univariate[0], u, domain=sp.QQ).monic().as_expr()
    graph_raw = sp.Poly(graphs[0], w, u, domain=sp.QQ)
    graph_w_coefficient = graph_raw.coeff_monomial(w)
    require(graph_w_coefficient != 0, "zero graph coefficient")
    graph = sp.expand(graph_raw.as_expr() / graph_w_coefficient)
    factorization = sp.factor_list(U, u)[1]
    require(all(exponent == 1 for _, exponent in factorization), "univariate eliminant is not squarefree")
    require(sum(sp.degree(q, u) for q, _ in factorization) == 15, "wrong Groebner degree")
    derived_factors = {sp.srepr(primitive_integer(q, u)) for q, _ in factorization}

    component_rows = residual["components"]
    require(isinstance(component_rows, list) and len(component_rows) == 5, "wrong component count")
    components: list[tuple[sp.Expr, sp.Expr]] = []
    for component_index, component_row in enumerate(component_rows):
        exact_keys(component_row, {"u_factor", "w_relation"}, f"component {component_index}")
        q = decode_poly(component_row["u_factor"], (u,), f"component {component_index} q")
        relation = decode_poly(component_row["w_relation"], (w, u), f"component {component_index} relation")
        require(sp.Poly(q, u, domain=sp.QQ).is_irreducible, f"component {component_index}: q reducible")
        relation_poly = sp.Poly(relation, w, u, domain=sp.QQ)
        c = relation_poly.coeff_monomial(w)
        require(c > 0 and sp.degree(relation, w) == 1, f"component {component_index}: bad graph relation")
        relation_tail = sp.expand(relation.subs(w, 0))
        graph_tail = sp.expand(graph.subs(w, 0))
        require(
            sp.rem(c * graph_tail - relation_tail, q, u, domain=sp.QQ) == 0,
            f"component {component_index}: relation is not the Groebner graph",
        )
        # Direct membership check: every claimed graph lies in V(A,B).
        w_value = -relation_tail / c
        for name, polynomial in (("A", A), ("B", B)):
            numerator = sp.together(polynomial.subs(w, w_value)).as_numer_denom()[0]
            require(
                sp.rem(numerator, q, u, domain=sp.QQ) == 0,
                f"component {component_index}: {name} does not vanish",
            )
        components.append((q, relation))
    observed_factors = {sp.srepr(primitive_integer(q, u)) for q, _ in components}
    require(observed_factors == derived_factors, "component factors do not exhaust the eliminant")

    q1 = 4 * u**2 + 4 * u + 3
    q2 = 52 * u**2 - 36 * u - 15
    q3 = 84 * u**2 - 52 * u + 1
    q4 = 32 * u**3 + 48 * u**2 + 32 * u + 9
    q5 = 1280 * u**6 + 3840 * u**5 + 6720 * u**4 + 7072 * u**3 + 5056 * u**2 + 2160 * u + 525
    expected_components = {
        (sp.srepr(q1), sp.srepr(2 * w + 2 * u + 3)),
        (sp.srepr(q2), sp.srepr(w)),
        (sp.srepr(q3), sp.srepr(3 * w + 2)),
        (sp.srepr(q4), sp.srepr(2 * w + 2 * u + 3)),
        (sp.srepr(q5), sp.srepr(40 * w + 640 * u**5 + 1920 * u**4 + 2960 * u**3 + 2736 * u**2 + 1488 * u + 465)),
    }
    require({(sp.srepr(q), sp.srepr(l)) for q, l in components} == expected_components, "unexpected decomposition")

    # Exact semialgebraic rejection of four components.
    require(sp.discriminant(q1, u) < 0 and sp.LC(sp.Poly(q1, u)) > 0, "q1 real-root rejection failed")
    require(all(c > 0 for c in sp.Poly(q5, u).all_coeffs()), "q5 positivity rejection failed")
    # q3 has w=-2/3.  q4 has 2w+2u+3=0.  These relations visibly
    # contradict w>=0, respectively u,w>=0.
    require((3 * w + 2).subs(w, 0) > 0, "q3 relation rejection failed")
    require(all(c > 0 for _, c in sp.Poly(2 * w + 2 * u + 3, w, u).terms()), "q4 rejection failed")
    require(sp.Poly(q2, u).count_roots(0, sp.oo) == 1, "q2 does not have exactly one positive root")
    require(sp.Poly(q2, u).count_roots(-sp.oo, 0) == 1, "q2 does not have exactly one negative root")

    survivor = certificate["surviving_component"]
    exact_keys(
        survivor,
        {
            "w",
            "u_polynomial_ascending",
            "u_positive_root",
            "alpha",
            "alpha_polynomial_ascending",
            "alpha_isolating_interval",
            "normalized_coordinates",
        },
        "survivor",
    )
    require(strict_int(survivor["w"], "surviving w") == 0, "wrong surviving w")
    require(survivor["u_polynomial_ascending"] == [-15, -36, 52], "wrong surviving u polynomial")
    require(survivor["u_positive_root"] == "(9+2*sqrt(69))/26", "wrong u radical")
    require(survivor["alpha"] == "u+3/2=(24+sqrt(69))/13", "wrong alpha radical")
    require(survivor["alpha_polynomial_ascending"] == [39, -48, 13], "wrong alpha polynomial")
    require(survivor["alpha_isolating_interval"] == [[12, 5], [5, 2]], "wrong alpha interval")
    require(survivor["normalized_coordinates"] == ["alpha", "alpha", "1", "1", "1"], "wrong point")

    # Directly verify that the survivor satisfies all four equations, not
    # merely the two necessary residual equations.
    for equation_index, equation in enumerate(Hc):
        value = sp.expand(equation.subs({x: 0, z: 0, w: 0}))
        require(sp.rem(value, q2, u, domain=sp.QQ) == 0, f"survivor fails H[{equation_index}]")
    require(q2.subs(u, 0) < 0 < q2.subs(u, 1), "u isolating interval failed")
    # At x=z=w=0 and the positive q2 root, 01 has margin 2u>0,
    # top-small pairs have margin 1, and small-small pairs have 2(u+1).
    require(margin_by_pair[0, 1].subs({x: 0, z: 0, w: 0}) == 2 * u, "survivor 01 margin failed")
    require(margin_by_pair[0, 2].subs({x: 0, z: 0, w: 0}) == 1, "survivor 02 margin failed")

    # Independent exact tangent-Hessian audit at (alpha,alpha,1,1,1).
    alpha = sp.symbols("alpha")
    ambient = sp.symbols("a0:5")
    ambient_T = sum(ambient) / 2
    ambient_S = sum(value**2 for value in ambient)
    ambient_P = sp.expand(
        ambient_T**4
        - sum((ambient_T - value) ** 4 for value in ambient)
        + sum(
            (ambient_T - ambient[i] - ambient[j]) ** 4
            for i in range(5)
            for j in range(i + 1, 5)
        )
        - 2 * (ambient_T - ambient[0] - ambient[1]) ** 4
    )
    ambient_Pi = [sp.diff(ambient_P, value) for value in ambient]
    ambient_Pij = [[sp.diff(ambient_Pi[i], ambient[j]) for j in range(5)] for i in range(5)]
    point = {ambient[0]: alpha, ambient[1]: alpha, ambient[2]: 1, ambient[3]: 1, ambient[4]: 1}
    M = sp.zeros(5)
    for i in range(5):
        for j in range(5):
            M[i, j] = sp.cancel(
                (
                    (1 if i == j else 0) / ambient_S
                    - 2 * ambient[i] * ambient[j] / ambient_S**2
                    + ambient_Pij[i][j] / ambient_P
                    - ambient_Pi[i] * ambient_Pi[j] / ambient_P**2
                    + (1 if i == j else 0) / ambient[i] ** 2
                ).subs(point)
            )
    vectors = {
        "large_block": sp.Matrix([1, -1, 0, 0, 0]),
        "small_block": sp.Matrix([0, 0, 1, -1, 0]),
        "block_contrast": sp.Matrix([3, 3, -2 * alpha, -2 * alpha, -2 * alpha]),
    }
    alpha_modulus = 13 * alpha**2 - 48 * alpha + 39
    hessian_certificate = certificate["hessian"]
    exact_keys(
        hessian_certificate,
        {
            "matrix_formula",
            "tangent_vectors",
            "reduced_quadratic_forms_mod_13alpha2-48alpha+39",
            "symmetry_dimensions",
            "tangent_signature",
        },
        "hessian",
    )
    require(
        hessian_certificate["matrix_formula"]
        == "Mij=deltaij/S-2*ai*aj/S^2+Pij/P-Pi*Pj/P^2+deltaij/ai^2",
        "wrong Hessian formula",
    )
    require(
        hessian_certificate["tangent_vectors"]
        == {
            "large_block": ["1", "-1", "0", "0", "0"],
            "small_block": ["0", "0", "1", "-1", "0"],
            "block_contrast": ["3", "3", "-2*alpha", "-2*alpha", "-2*alpha"],
        },
        "wrong tangent vectors",
    )
    symmetry_dimensions = hessian_certificate["symmetry_dimensions"]
    exact_keys(symmetry_dimensions, set(vectors), "symmetry dimensions")
    require(
        {
            name: strict_int(value, f"symmetry dimension {name}")
            for name, value in symmetry_dimensions.items()
        }
        == {"large_block": 1, "small_block": 2, "block_contrast": 1},
        "wrong symmetry dimensions",
    )
    require(
        hessian_certificate["tangent_signature"]
        == ["negative", "negative", "negative", "positive"],
        "wrong tangent signature",
    )
    reduced_forms = {
        name: algebraic_reduce_rational((vector.T * M * vector)[0], alpha_modulus, alpha)
        for name, vector in vectors.items()
    }
    form_certificate = hessian_certificate["reduced_quadratic_forms_mod_13alpha2-48alpha+39"]
    exact_keys(form_certificate, set(vectors), "Hessian reduced forms")
    claimed_signs: dict[str, str] = {}
    for name in vectors:
        row = form_certificate[name]
        exact_keys(row, {"linear_numerator_ascending", "denominator", "sign"}, f"Hessian form {name}")
        coefficients_row = row["linear_numerator_ascending"]
        require(
            isinstance(coefficients_row, list)
            and len(coefficients_row) == 2
            and all(isinstance(c, int) and not isinstance(c, bool) for c in coefficients_row),
            f"Hessian form {name}: bad numerator",
        )
        denominator_row = strict_int(row["denominator"], f"Hessian form {name} denominator")
        require(denominator_row > 0, f"Hessian form {name}: nonpositive denominator")
        claimed_form = (coefficients_row[0] + coefficients_row[1] * alpha) / denominator_row
        require(sp.expand(reduced_forms[name] - claimed_form) == 0, f"Hessian form {name} mismatch")
        require(row["sign"] in {"negative", "positive"}, f"Hessian form {name}: bad sign label")
        claimed_signs[name] = row["sign"]
    left, right = sp.Rational(12, 5), sp.Rational(5, 2)
    require(alpha_modulus.subs(alpha, left) < 0 < alpha_modulus.subs(alpha, right), "alpha interval signs fail")
    require(sp.diff(alpha_modulus, alpha).subs(alpha, left) > 0, "alpha interval is not monotone")
    require(416 * right - 1367 < 0, "small-block negative sign failed")
    require(104 * left - 215 > 0, "block-contrast positive sign failed")
    require(
        claimed_signs
        == {"large_block": "negative", "small_block": "negative", "block_contrast": "positive"},
        "Hessian sign labels disagree with exact interval audit",
    )
    require(ambient_P.subs(point) == 3 * (32 * alpha - 13) / 4, "candidate P evaluation failed")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: builder_verify_star1.py CERTIFICATE.json", file=sys.stderr)
        return 2
    try:
        verify(Path(sys.argv[1]))
    except Rejected as exc:
        print("REJECT:", exc, file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"REJECT: unexpected verifier failure: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1
    print(
        "PASS: exact star1 closure has one critical orbit, "
        "((24+sqrt(69))/13)^2,1^3, and its tangent Hessian is indefinite"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
