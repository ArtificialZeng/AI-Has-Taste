#!/usr/bin/env python3
"""Independent exact audit of the star2 Bernstein no-go certificate.

This script deliberately does not import SymPy or either star2 constructor /
verifier.  It implements sparse multivariate arithmetic over Fraction,
rebuilds the chamber numerator both from all 32 subsets and from paired signs,
recomputes the critical combination and Bernstein conversion, audits all
pair/order/polygon margins, and performs deterministic exact point checks.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import platform
import random
from fractions import Fraction
from pathlib import Path


def fail(message: str) -> "None":
    raise SystemExit("AUDIT FAIL: " + message)


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            fail(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_booleans(value: object, path: str = "$") -> None:
    if type(value) is bool:
        fail(f"boolean forbidden in certificate at {path}")
    if type(value) is dict:
        for key, child in value.items():
            reject_booleans(child, f"{path}.{key}")
    elif type(value) is list:
        for index, child in enumerate(value):
            reject_booleans(child, f"{path}[{index}]")


class Poly:
    def __init__(self, terms=None, variables=4):
        self.variables = variables
        self.terms = {
            tuple(monomial): Fraction(coefficient)
            for monomial, coefficient in (terms or {}).items()
            if coefficient
        }

    @classmethod
    def constant(cls, value, variables=4):
        return cls({(0,) * variables: Fraction(value)}, variables)

    @classmethod
    def variable(cls, index, variables=4):
        exponents = [0] * variables
        exponents[index] = 1
        return cls({tuple(exponents): Fraction(1)}, variables)

    def coerce(self, other):
        if isinstance(other, Poly):
            if other.variables != self.variables:
                fail("polynomial dimension mismatch")
            return other
        return Poly.constant(other, self.variables)

    def __add__(self, other):
        other = self.coerce(other)
        terms = dict(self.terms)
        for monomial, coefficient in other.terms.items():
            terms[monomial] = terms.get(monomial, Fraction(0)) + coefficient
            if not terms[monomial]:
                del terms[monomial]
        return Poly(terms, self.variables)

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -c for m, c in self.terms.items()}, self.variables)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        terms = {}
        for m1, c1 in self.terms.items():
            for m2, c2 in other.terms.items():
                monomial = tuple(x + y for x, y in zip(m1, m2))
                terms[monomial] = terms.get(monomial, Fraction(0)) + c1 * c2
                if not terms[monomial]:
                    del terms[monomial]
        return Poly(terms, self.variables)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        scalar = Fraction(scalar)
        if not scalar:
            fail("division by zero")
        return Poly({m: c / scalar for m, c in self.terms.items()}, self.variables)

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            fail("invalid polynomial exponent")
        result = Poly.constant(1, self.variables)
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power //= 2
        return result

    def derivative(self, index):
        terms = {}
        for monomial, coefficient in self.terms.items():
            exponent = monomial[index]
            if exponent:
                reduced = list(monomial)
                reduced[index] -= 1
                terms[tuple(reduced)] = coefficient * exponent
        return Poly(terms, self.variables)

    def substitute(self, replacements):
        if len(replacements) != self.variables:
            fail("wrong substitution length")
        target_variables = replacements[0].variables
        if any(item.variables != target_variables for item in replacements):
            fail("inconsistent substitution target")
        answer = Poly.constant(0, target_variables)
        for monomial, coefficient in self.terms.items():
            term = Poly.constant(coefficient, target_variables)
            for replacement, exponent in zip(replacements, monomial):
                term *= replacement**exponent
            answer += term
        return answer

    def evaluate(self, values):
        if len(values) != self.variables:
            fail("wrong evaluation dimension")
        result = Fraction(0)
        for monomial, coefficient in self.terms.items():
            term = coefficient
            for value, exponent in zip(values, monomial):
                term *= Fraction(value) ** exponent
            result += term
        return result


def choose(n, k):
    return math.comb(n, k)


def bernstein_rows(poly: Poly, v_index: int):
    degree = max(monomial[v_index] for monomial in poly.terms)
    parameter_indices = [index for index in range(poly.variables) if index != v_index]
    power = [{} for _ in range(degree + 1)]
    for monomial, coefficient in poly.terms.items():
        exponent = monomial[v_index]
        parameter_monomial = tuple(monomial[index] for index in parameter_indices)
        power[exponent][parameter_monomial] = coefficient
    rows = []
    for k in range(degree + 1):
        terms = {}
        for i in range(k + 1):
            factor = Fraction(choose(k, i), choose(degree, i))
            for monomial, coefficient in power[i].items():
                terms[monomial] = terms.get(monomial, Fraction(0)) + factor * coefficient
                if not terms[monomial]:
                    del terms[monomial]
        rows.append(terms)
    return degree, rows


def serialized_rows(rows):
    output = []
    for k, terms in enumerate(rows):
        serialized = []
        for monomial in sorted(terms, reverse=True):
            coefficient = terms[monomial]
            serialized.append([*monomial, str(coefficient.numerator), str(coefficient.denominator)])
        output.append({"k": k, "terms": serialized})
    return output


def rows_to_polynomial(rows, degree):
    # Target order is (u,y,w,v), with v last.
    u, y, w, v = [Poly.variable(index, 4) for index in range(4)]
    parameters = (u, y, w)
    answer = Poly.constant(0, 4)
    for k, terms in enumerate(rows):
        coefficient_poly = Poly.constant(0, 4)
        for monomial, coefficient in terms.items():
            term = Poly.constant(coefficient, 4)
            for parameter, exponent in zip(parameters, monomial):
                term *= parameter**exponent
            coefficient_poly += term
        answer += choose(degree, k) * coefficient_poly * v**k * (1 - v) ** (degree - k)
    return answer


def parse_certificate_rows(serialized):
    rows = []
    for expected_k, row in enumerate(serialized):
        if row.get("k") != expected_k or set(row) != {"k", "terms"}:
            fail("noncanonical Bernstein row")
        terms = {}
        for entry in row["terms"]:
            if not isinstance(entry, list) or len(entry) != 5:
                fail("malformed coefficient entry")
            monomial = tuple(entry[:3])
            if any(not isinstance(exponent, int) or exponent < 0 for exponent in monomial):
                fail("invalid parameter monomial")
            try:
                coefficient = Fraction(entry[3]) / Fraction(entry[4])
            except (ValueError, ZeroDivisionError):
                fail("invalid rational coefficient")
            if monomial in terms:
                fail("duplicate parameter monomial")
            terms[monomial] = coefficient
        rows.append(terms)
    return rows


def affine_nonnegative_basis(poly: Poly):
    """Represent affine p(u,y,w,v) in basis u,y,w,v,(1-v)."""
    if any(sum(monomial) > 1 for monomial in poly.terms):
        fail("margin is not affine")
    zero = (0, 0, 0, 0)
    constant = poly.terms.get(zero, Fraction(0))
    coefficients = [poly.terms.get(tuple(1 if i == j else 0 for i in range(4)), Fraction(0)) for j in range(4)]
    # c + d*v = (c+d)*v + c*(1-v).
    representation = {
        "u": coefficients[0],
        "y": coefficients[1],
        "w": coefficients[2],
        "v": constant + coefficients[3],
        "1-v": constant,
    }
    if any(value < 0 for value in representation.values()):
        fail("claimed chamber margin has a negative domain-basis coefficient")
    reconstructed = (
        representation["u"] * Poly.variable(0, 4)
        + representation["y"] * Poly.variable(1, 4)
        + representation["w"] * Poly.variable(2, 4)
        + representation["v"] * Poly.variable(3, 4)
        + representation["1-v"] * (1 - Poly.variable(3, 4))
    )
    if reconstructed.terms != poly.terms:
        fail("margin domain-basis reconstruction failed")
    return {name: str(value) for name, value in representation.items() if value}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=220260829)
    parser.add_argument("--random-checks", type=int, default=64)
    args = parser.parse_args()
    raw = args.certificate.read_bytes()
    data = json.loads(raw, object_pairs_hook=reject_duplicate_keys)
    reject_booleans(data)
    expected_top_keys = {
        "schema",
        "claim",
        "coordinate_order",
        "high_pairs",
        "normalization",
        "gaps",
        "domain",
        "critical_numerators",
        "direction_coefficients_xyzw",
        "bernstein",
        "chamber_margin_identities",
        "proof_assistants",
    }
    if not isinstance(data, dict) or set(data) != expected_top_keys:
        fail("wrong or incomplete top-level schema")
    if data.get("schema") != "q5-star2-bernstein-v1":
        fail("wrong schema")
    if data.get("claim") != "the ordered full-support star2 chamber closure has no critical direction":
        fail("altered claim")
    if data.get("coordinate_order") != ["a0", "a1", "a2", "a3", "a4"]:
        fail("wrong coordinate order")
    if data.get("high_pairs") != [[0, 1], [0, 2]]:
        fail("wrong high-pair graph")
    if data.get("normalization") != {"a4": 1}:
        fail("wrong normalization")
    expected_gaps = {
        "a0": "1+w+z+y+x",
        "a1": "1+w+z+y",
        "a2": "1+w+z",
        "a3": "1+w",
        "a4": "1",
        "x": "u+v",
        "z": "u+1-v",
    }
    if data.get("gaps") != expected_gaps:
        fail("wrong gap chart")
    if data.get("domain") != ["u>=0", "y>=0", "w>=0", "0<=v<=1"]:
        fail("wrong chart domain")
    if data.get("critical_numerators") != "Hq=S_q*P*D+2*S*P_q*D-2*S*P*D_q":
        fail("altered critical-numerator declaration")
    if data.get("direction_coefficients_xyzw") != [-2, 2, -2, 1]:
        fail("wrong direction combination")
    expected_margins = {
        "high_02": "x+z-1=2*u",
        "low_03": "1+z-x=2*(1-v)",
        "low_12": "1+x-z=2*v",
    }
    if data.get("chamber_margin_identities") != expected_margins:
        fail("altered chamber-margin declarations")
    if data.get("proof_assistants") != []:
        fail("altered proof-assistant declaration")
    expected_bernstein_keys = {
        "parameter_order",
        "P_degree",
        "P_coefficients",
        "H_degree",
        "H_coefficients",
        "canonical_tables_sha256",
    }
    if not isinstance(data.get("bernstein"), dict) or set(data["bernstein"]) != expected_bernstein_keys:
        fail("wrong Bernstein schema")
    if data["bernstein"]["parameter_order"] != ["u", "y", "w"]:
        fail("wrong Bernstein parameter order")
    if data["bernstein"]["P_degree"] != 4 or data["bernstein"]["H_degree"] != 8:
        fail("wrong claimed Bernstein degrees")

    # Gap variables are ordered (x,y,z,w).
    x, y, z, w = [Poly.variable(index, 4) for index in range(4)]
    one = Poly.constant(1, 4)
    a = [
        one + w + z + y + x,
        one + w + z + y,
        one + w + z,
        one + w,
        one,
    ]
    total = sum(a, Poly.constant(0, 4))
    half_sum = total / 2

    # Direct 32-subset reconstruction uses a strict rational chamber point.
    sample = [Fraction(3, 2), Fraction(1), Fraction(3, 2), Fraction(1)]
    direct_P = Poly.constant(0, 4)
    active_subsets = 0
    for bits in itertools.product((0, 1), repeat=5):
        linear = half_sum - sum((a[index] for index, bit in enumerate(bits) if bit), Poly.constant(0, 4))
        value = linear.evaluate(sample)
        if value == 0:
            fail("audit sample lies on a subset-sum wall")
        if value > 0:
            active_subsets += 1
            direct_P += (-1 if sum(bits) % 2 else 1) * linear**4
    high_pairs = {(0, 1), (0, 2)}
    paired_P = half_sum**4 - sum(((half_sum - coordinate) ** 4 for coordinate in a), Poly.constant(0, 4))
    for pair in itertools.combinations(range(5), 2):
        paired_P += (-1 if pair in high_pairs else 1) * (half_sum - a[pair[0]] - a[pair[1]]) ** 4
    if direct_P.terms != paired_P.terms:
        fail("32-subset and paired-sign P reconstructions disagree")

    S = sum((coordinate * coordinate for coordinate in a), Poly.constant(0, 4))
    D = a[0] * a[1] * a[2] * a[3]
    H = []
    squared_numerator = S * direct_P**2
    for index in range(4):
        critical_numerator = (
            S.derivative(index) * direct_P * D
            + 2 * S * direct_P.derivative(index) * D
            - 2 * S * direct_P * D.derivative(index)
        )
        # Independent quotient-rule check for F^2=S*P^2/D^2:
        # D*(S*P^2)_q-2*S*P^2*D_q = P*H_q.
        if (
            D * squared_numerator.derivative(index)
            - 2 * squared_numerator * D.derivative(index)
            - direct_P * critical_numerator
        ).terms:
            fail("critical numerator fails independent F^2 quotient-rule identity")
        H.append(critical_numerator)
    combo = -2 * H[0] + 2 * H[1] - 2 * H[2] + H[3]

    # Target variables are (u,y,w,v).
    u2, y2, w2, v2 = [Poly.variable(index, 4) for index in range(4)]
    chart = [u2 + v2, y2, u2 + 1 - v2, w2]
    P_chart = direct_P.substitute(chart)
    H_chart = combo.substitute(chart)
    p_degree, p_rows = bernstein_rows(P_chart, 3)
    h_degree, h_rows = bernstein_rows(H_chart, 3)
    if (p_degree, h_degree) != (4, 8):
        fail("unexpected degrees")
    if rows_to_polynomial(p_rows, p_degree).terms != P_chart.terms:
        fail("independent P Bernstein reconstruction failed")
    if rows_to_polynomial(h_rows, h_degree).terms != H_chart.terms:
        fail("independent H Bernstein reconstruction failed")

    certificate_p_rows = parse_certificate_rows(data["bernstein"]["P_coefficients"])
    certificate_h_rows = parse_certificate_rows(data["bernstein"]["H_coefficients"])
    if p_rows != certificate_p_rows or h_rows != certificate_h_rows:
        fail("independently recomputed Bernstein table differs from certificate")
    if serialized_rows(p_rows) != data["bernstein"]["P_coefficients"]:
        fail("P table is not canonically serialized")
    if serialized_rows(h_rows) != data["bernstein"]["H_coefficients"]:
        fail("H table is not canonically serialized")
    if rows_to_polynomial(certificate_p_rows, p_degree).terms != P_chart.terms:
        fail("serialized P table does not reconstruct P")
    if rows_to_polynomial(certificate_h_rows, h_degree).terms != H_chart.terms:
        fail("serialized H table does not reconstruct H")

    canonical = json.dumps(
        {"P": data["bernstein"]["P_coefficients"], "H": data["bernstein"]["H_coefficients"]},
        sort_keys=True,
        separators=(",", ":"),
    ).encode()
    canonical_digest = hashlib.sha256(canonical).hexdigest()
    if canonical_digest != data["bernstein"]["canonical_tables_sha256"]:
        fail("canonical table digest mismatch")

    p_coefficients = [coefficient for row in p_rows for coefficient in row.values()]
    h_coefficients = [coefficient for row in h_rows for coefficient in row.values()]
    if len(p_coefficients) != 70 or len(h_coefficients) != 1125:
        fail("wrong coefficient count")
    if min(p_coefficients) != 16 or min(h_coefficients) != 32:
        fail("wrong minimum positive coefficient")
    if any(coefficient <= 0 for coefficient in p_coefficients + h_coefficients):
        fail("nonpositive coefficient found")
    if any(row.get((0, 0, 0), Fraction(0)) <= 0 for row in p_rows + h_rows):
        fail("a Bernstein coefficient polynomial lacks a positive constant")

    # Exhaust all pair signs, order gaps, and polygon inequalities under the chart.
    chart_a = [coordinate.substitute(chart) for coordinate in a]
    chart_total = sum(chart_a, Poly.constant(0, 4))
    margin_chart = {}
    for i, j in itertools.combinations(range(5), 2):
        if (i, j) in high_pairs:
            margin = 2 * (chart_a[i] + chart_a[j]) - chart_total
            kind = "high"
        else:
            margin = chart_total - 2 * (chart_a[i] + chart_a[j])
            kind = "low"
        margin_chart[f"pair_{i}{j}_{kind}"] = affine_nonnegative_basis(margin)
    for i in range(4):
        margin_chart[f"order_{i}{i+1}"] = affine_nonnegative_basis(chart_a[i] - chart_a[i + 1])
    for i in range(5):
        margin_chart[f"polygon_{i}"] = affine_nonnegative_basis(chart_total - 2 * chart_a[i])

    # Deterministic exact randomized and boundary evaluations.
    rng = random.Random(args.seed)
    checks = [
        (Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
        (Fraction(0), Fraction(2), Fraction(3), Fraction(0)),
        (Fraction(5), Fraction(0), Fraction(0), Fraction(1)),
    ]
    for _ in range(args.random_checks):
        denominators = [rng.randint(1, 9) for _ in range(4)]
        checks.append(
            (
                Fraction(rng.randint(0, 30), denominators[0]),
                Fraction(rng.randint(0, 30), denominators[1]),
                Fraction(rng.randint(0, 30), denominators[2]),
                Fraction(rng.randint(0, denominators[3]), denominators[3]),
            )
        )
    minimum_p_value = None
    minimum_h_value = None
    for point in checks:
        p_value = P_chart.evaluate(point)
        h_value = H_chart.evaluate(point)
        if p_value <= 0 or h_value <= 0:
            fail("nonpositive exact point evaluation found")
        minimum_p_value = p_value if minimum_p_value is None else min(minimum_p_value, p_value)
        minimum_h_value = h_value if minimum_h_value is None else min(minimum_h_value, h_value)

    result = {
        "status": "PASS",
        "method": "standard-library Fraction sparse polynomials; no SymPy or project imports",
        "python": platform.python_version(),
        "seed": args.seed,
        "random_exact_checks": args.random_checks,
        "boundary_checks": 4,
        "active_subsets_at_strict_sample": active_subsets,
        "paired_equals_32_subset": True,
        "critical_numerator_F_squared_identities": 4,
        "P_degree_v": p_degree,
        "H_degree_v": h_degree,
        "P_positive_coefficients": len(p_coefficients),
        "H_positive_coefficients": len(h_coefficients),
        "P_minimum_coefficient": str(min(p_coefficients)),
        "H_minimum_coefficient": str(min(h_coefficients)),
        "P_block_term_counts": [len(row) for row in p_rows],
        "H_block_term_counts": [len(row) for row in h_rows],
        "minimum_exact_P_point_value": str(minimum_p_value),
        "minimum_exact_H_point_value": str(minimum_h_value),
        "margin_chart": margin_chart,
        "canonical_tables_sha256": canonical_digest,
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "audit_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in result.items() if key != "margin_chart"}, indent=2))


if __name__ == "__main__":
    main()
