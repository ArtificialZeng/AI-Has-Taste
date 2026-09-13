#!/usr/bin/env python3
"""Independent exact verifier for the ordered star4 chamber no-go.

The verifier uses standard-library rational polynomial arithmetic to rebuild
the box-spline numerator and critical equations from the four high pairs.  It
then invokes Singular only as an exact Groebner/saturation engine and checks
six small ideal consequences by zero normal forms.  A separate standard-
library Sturm computation certifies the final univariate inequality.  No
discovery module or numerical root is imported.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import shutil
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path


N_GENERAL = 5


def reject(message: str) -> "None":
    raise SystemExit("REJECT: " + message)


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_booleans(value: object, path: str = "$") -> None:
    if type(value) is bool:
        reject(f"boolean forbidden in certificate at {path}")
    if type(value) is dict:
        for key, child in value.items():
            reject_booleans(child, f"{path}.{key}")
    elif type(value) is list:
        for index, child in enumerate(value):
            reject_booleans(child, f"{path}[{index}]")


class Poly:
    def __init__(self, terms=None, variables=N_GENERAL):
        self.variables = variables
        self.terms = {
            tuple(exponents): Fraction(coefficient)
            for exponents, coefficient in (terms or {}).items()
            if coefficient
        }

    @classmethod
    def constant(cls, value, variables=N_GENERAL):
        return cls({(0,) * variables: Fraction(value)}, variables)

    @classmethod
    def variable(cls, index, variables=N_GENERAL):
        exponent = [0] * variables
        exponent[index] = 1
        return cls({tuple(exponent): Fraction(1)}, variables)

    def _coerce(self, other):
        if isinstance(other, Poly):
            if other.variables != self.variables:
                reject("polynomial dimension mismatch")
            return other
        return Poly.constant(other, self.variables)

    def __add__(self, other):
        other = self._coerce(other)
        terms = dict(self.terms)
        for monomial, coefficient in other.terms.items():
            terms[monomial] = terms.get(monomial, Fraction(0)) + coefficient
            if terms[monomial] == 0:
                del terms[monomial]
        return Poly(terms, self.variables)

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -c for m, c in self.terms.items()}, self.variables)

    def __sub__(self, other):
        return self + (-self._coerce(other))

    def __rsub__(self, other):
        return self._coerce(other) - self

    def __mul__(self, other):
        other = self._coerce(other)
        terms = {}
        for left_monomial, left_coefficient in self.terms.items():
            for right_monomial, right_coefficient in other.terms.items():
                monomial = tuple(x + y for x, y in zip(left_monomial, right_monomial))
                terms[monomial] = terms.get(monomial, Fraction(0)) + left_coefficient * right_coefficient
        return Poly(terms, self.variables)

    __rmul__ = __mul__

    def __truediv__(self, scalar):
        scalar = Fraction(scalar)
        if scalar == 0:
            reject("division by zero")
        return Poly({m: c / scalar for m, c in self.terms.items()}, self.variables)

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            reject("invalid polynomial exponent")
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
            if monomial[index]:
                reduced = list(monomial)
                terms[tuple(reduced[:index] + [reduced[index] - 1] + reduced[index + 1 :])] = coefficient * monomial[index]
        return Poly(terms, self.variables)

    def set_last_to_one(self):
        if self.variables != 5:
            reject("gauge substitution expected five variables")
        terms = {}
        for monomial, coefficient in self.terms.items():
            reduced = monomial[:4]
            terms[reduced] = terms.get(reduced, Fraction(0)) + coefficient
        return Poly(terms, 4)

    def primitive_integer(self):
        if not self.terms:
            return self
        denominator = 1
        for coefficient in self.terms.values():
            denominator = math.lcm(denominator, coefficient.denominator)
        integers = [int(coefficient * denominator) for coefficient in self.terms.values()]
        content = 0
        for integer in integers:
            content = math.gcd(content, abs(integer))
        return Poly({m: int(c * denominator) // content for m, c in self.terms.items()}, self.variables)

    def singular(self, names):
        if len(names) != self.variables or not self.terms:
            reject("cannot serialize polynomial")
        pieces = []
        for monomial in sorted(self.terms, reverse=True):
            coefficient = self.terms[monomial]
            factors = []
            for name, exponent in zip(names, monomial):
                if exponent == 1:
                    factors.append(name)
                elif exponent > 1:
                    factors.append(f"{name}^{exponent}")
            body = "*".join(factors)
            magnitude = abs(coefficient)
            if body:
                if magnitude != 1:
                    body = f"{magnitude.numerator}/{magnitude.denominator}*{body}"
            else:
                body = f"{magnitude.numerator}/{magnitude.denominator}"
            sign = "-" if coefficient < 0 else "+"
            pieces.append((sign, body))
        first_sign, first_body = pieces[0]
        answer = ("-" if first_sign == "-" else "") + first_body
        for sign, body in pieces[1:]:
            answer += sign + body
        return answer


def rebuild_system(high_pairs):
    a = [Poly.variable(i) for i in range(5)]
    half_sum = sum(a, Poly.constant(0)) / 2
    norm_square = sum((x * x for x in a), Poly.constant(0))
    numerator = half_sum**4 - sum(((half_sum - x) ** 4 for x in a), Poly.constant(0))
    high = {tuple(pair) for pair in high_pairs}
    for pair in itertools.combinations(range(5), 2):
        sign = -1 if pair in high else 1
        numerator += sign * (half_sum - a[pair[0]] - a[pair[1]]) ** 4
    # A genuinely different reconstruction enumerates all 32 subsets and
    # selects positive parts using the exact interior sample (3,1,1,1,1).
    # This catches a flipped high/low-pair sign before any CAS computation.
    direct = Poly.constant(0)
    sample = [Fraction(3), Fraction(1), Fraction(1), Fraction(1), Fraction(1)]
    sample_half_sum = sum(sample) / 2
    for bits in itertools.product((0, 1), repeat=5):
        linear = half_sum - sum((a[index] for index, bit in enumerate(bits) if bit), Poly.constant(0))
        sample_value = sample_half_sum - sum(sample[index] for index, bit in enumerate(bits) if bit)
        if sample_value > 0:
            direct += (-1 if sum(bits) % 2 else 1) * linear**4
    if numerator.terms != direct.terms:
        reject("paired and 32-subset numerator reconstructions disagree")
    critical = [
        a[index] * norm_square * numerator.derivative(index)
        + (a[index] ** 2 - norm_square) * numerator
        for index in range(4)
    ]
    return numerator.set_last_to_one().primitive_integer(), [
        polynomial.set_last_to_one().primitive_integer() for polynomial in critical
    ]


def trim(coefficients):
    coefficients = list(map(Fraction, coefficients))
    while coefficients and coefficients[0] == 0:
        coefficients.pop(0)
    return coefficients


def derivative(coefficients):
    coefficients = trim(coefficients)
    degree = len(coefficients) - 1
    return trim([coefficient * (degree - index) for index, coefficient in enumerate(coefficients[:-1])])


def remainder(dividend, divisor):
    dividend, divisor = trim(dividend), trim(divisor)
    if not divisor:
        reject("zero divisor in Sturm computation")
    answer = dividend[:]
    while answer and len(answer) >= len(divisor):
        ratio = answer[0] / divisor[0]
        for index, coefficient in enumerate(divisor):
            answer[index] -= ratio * coefficient
        answer = trim(answer)
    return answer


def primitive_preserving_sign(coefficients):
    coefficients = trim(coefficients)
    if not coefficients:
        return []
    denominator = 1
    for coefficient in coefficients:
        denominator = math.lcm(denominator, coefficient.denominator)
    integers = [int(coefficient * denominator) for coefficient in coefficients]
    content = 0
    for integer in integers:
        content = math.gcd(content, abs(integer))
    return [integer // content for integer in integers]


def sturm_sequence(coefficients):
    sequence = [trim(coefficients), derivative(coefficients)]
    while sequence[-1]:
        next_polynomial = [-x for x in remainder(sequence[-2], sequence[-1])]
        if not next_polynomial:
            break
        sequence.append(next_polynomial)
    return sequence


def evaluate(coefficients, point):
    result = Fraction(0)
    for coefficient in coefficients:
        result = result * point + coefficient
    return result


def variations(signs):
    signs = [sign for sign in signs if sign]
    return sum(left != right for left, right in zip(signs, signs[1:]))


def polynomial_add(left, right):
    width = max(len(left), len(right))
    left = [Fraction(0)] * (width - len(left)) + list(map(Fraction, left))
    right = [Fraction(0)] * (width - len(right)) + list(map(Fraction, right))
    return trim([x + y for x, y in zip(left, right)])


def polynomial_multiply(left, right):
    output = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            output[i + j] += Fraction(x) * Fraction(y)
    return trim(output)


def parse_marker(output, marker):
    lines = [line.strip() for line in output.splitlines()]
    try:
        index = lines.index(marker)
    except ValueError:
        reject(f"Singular output missing {marker}")
    if index + 1 >= len(lines):
        reject(f"Singular output truncated after {marker}")
    return lines[index + 1]


def singular_check(P, critical, consequences, expected_dimension, expected_vdim):
    executable = shutil.which("Singular")
    if not executable:
        reject("Singular executable not found")
    names = ["a0", "a1", "a2", "a3"]
    lines = ["ring r=0,(a0,a1,a2,a3),dp;", f"poly P={P.singular(names)};"]
    lines.append("poly S=1+a0^2+a1^2+a2^2+a3^2;")
    for index, polynomial in enumerate(critical):
        lines.append(f"poly g{index}={polynomial.singular(names)};")
    lines.extend(
        [
            "ideal I=g0,g1,g2,g3;",
            'LIB "elim.lib";',
            "ideal Q=sat(I,a0*a1*a2*a3*P*S);",
            "option(redSB);",
            "ideal J=std(Q);",
            'print("MARK_DIM"); print(dim(J));',
            'print("MARK_VDIM"); print(vdim(J));',
        ]
    )
    for name, expression in consequences.items():
        lines.append(f"poly target_{name}={expression};")
        lines.append(f'print("MARK_NF_{name}"); print(reduce(target_{name},J));')
    lines.append("exit;")
    script = "\n".join(lines) + "\n"
    with tempfile.TemporaryDirectory(prefix="star4-verify-") as directory:
        script_path = Path(directory) / "verify.sing"
        script_path.write_text(script, encoding="utf-8")
        try:
            result = subprocess.run(
                [executable, "-q", str(script_path)],
                check=False,
                capture_output=True,
                text=True,
                timeout=300,
            )
        except subprocess.TimeoutExpired:
            reject("Singular computation timed out")
    if result.returncode != 0 or "?" in result.stdout or "error" in result.stderr.lower():
        reject("Singular failed: " + (result.stderr or result.stdout)[-500:])
    if parse_marker(result.stdout, "MARK_DIM") != str(expected_dimension):
        reject("wrong saturated ideal dimension")
    if parse_marker(result.stdout, "MARK_VDIM") != str(expected_vdim):
        reject("wrong saturated vector-space dimension")
    for name in consequences:
        if parse_marker(result.stdout, f"MARK_NF_{name}") != "0":
            reject(f"ideal consequence {name} has nonzero normal form")
    version_result = subprocess.run(
        [executable, "--version"],
        check=False,
        capture_output=True,
        text=True,
        stdin=subprocess.DEVNULL,
        timeout=10,
    )
    if version_result.returncode != 0 or not version_result.stdout.splitlines():
        reject("could not record Singular version")
    version = version_result.stdout.splitlines()[0]
    return version, hashlib.sha256(script.encode()).hexdigest()


def main():
    if len(sys.argv) != 2:
        reject("usage: breaker_star4_verify.py CERTIFICATE.json")
    certificate_path = Path(sys.argv[1])
    try:
        raw = certificate_path.read_bytes()
        data = json.loads(raw, object_pairs_hook=reject_duplicate_keys)
    except (OSError, json.JSONDecodeError, ValueError):
        reject("unreadable certificate")
    reject_booleans(data)
    expected_keys = {
        "schema",
        "gauge",
        "ordered_variables",
        "high_pairs",
        "expected_saturated_dimension",
        "expected_saturated_vector_dimension",
        "ideal_consequences",
        "all_leaves_one_polynomial_degree_descending",
        "sturm_sequence_primitive_degree_descending",
        "expected_sturm_variations_at_2",
        "expected_sturm_variations_at_positive_infinity",
        "ordered_chamber_reduction",
        "branch_margin_numerator_degree_descending",
        "conclusion",
    }
    if not isinstance(data, dict) or set(data) != expected_keys:
        reject("wrong or incomplete top-level schema")
    if data["schema"] != "q5-star4-no-critical-root-v1" or data["gauge"] != "a4=1":
        reject("unsupported schema or gauge")
    if data["ordered_variables"] != ["a0", "a1", "a2", "a3", "a4"]:
        reject("unexpected variable order")
    if data["high_pairs"] != [[0, 1], [0, 2], [0, 3], [0, 4]]:
        reject("certificate is not the star4 chamber")
    if (type(data["expected_saturated_dimension"]) is not int
            or type(data["expected_saturated_vector_dimension"]) is not int
            or data["expected_saturated_dimension"] != 0
            or data["expected_saturated_vector_dimension"] != 48):
        reject("unexpected ideal invariants")
    expected_consequences = {
        "h23": "(a2-1)*(a2-a3)*(a3-1)",
        "h13": "(a1-1)*(a1-a3)*(a3-1)",
        "h12": "(a1-1)*(a1-a2)*(a2-1)",
        "k3": "(a3-1)*(a0*a3+a0-a1*a3-a1-a2*a3-a2-a3^2+2*a3-1)",
        "k2": "(a2-1)*(a0*a2+a0-a1*a2-a1-a2^2+a2-a3^2-1)",
        "k1": "(a1-1)*(a0*a1+a0-a1^2-a2^2-a3^2-1)",
    }
    if data["ideal_consequences"] != expected_consequences:
        reject("altered ideal consequences")
    if data["ordered_chamber_reduction"] != "a0+1>a1+a2+a3":
        reject("altered ordered-chamber reduction")
    expected_margin_numerator = [-2, 2]
    if data["branch_margin_numerator_degree_descending"] != expected_margin_numerator:
        reject("altered branch margin numerator")
    # Check the three divisions forced by k3, k1, and k2.  After multiplying
    # the strict chamber margin by the positive denominator x+1, each branch
    # has numerator 2(1-x), hence is negative for x>1.
    branch_numerators = [
        polynomial_add([3, 0, 1], polynomial_multiply([1, 1], [-3, 1])),
        polynomial_add([1, 0, 3], [-1, -2, -1]),
        polynomial_add([2, 0, 2], [-2, -2, 0]),
    ]
    if any([int(value) for value in row] != expected_margin_numerator for row in branch_numerators):
        reject("branch margin identities failed")
    expected_conclusion = "no saturated critical root satisfies a0>=a1>=a2>=a3>=a4=1 and a0+1>a1+a2+a3"
    if data["conclusion"] != expected_conclusion:
        reject("altered conclusion")

    R = [1, -12, 51, -96, 96, 0, -64]
    if data["all_leaves_one_polynomial_degree_descending"] != R:
        reject("altered final univariate polynomial")
    sequence = sturm_sequence(R)
    primitive = [primitive_preserving_sign(polynomial) for polynomial in sequence]
    if primitive != data["sturm_sequence_primitive_degree_descending"]:
        reject("Sturm sequence mismatch")
    signs_at_two = [(evaluate(polynomial, Fraction(2)) > 0) - (evaluate(polynomial, Fraction(2)) < 0) for polynomial in sequence]
    signs_at_infinity = [(polynomial[0] > 0) - (polynomial[0] < 0) for polynomial in sequence]
    variation_two = variations(signs_at_two)
    variation_infinity = variations(signs_at_infinity)
    if variation_two != data["expected_sturm_variations_at_2"] or variation_infinity != data["expected_sturm_variations_at_positive_infinity"]:
        reject("Sturm variation mismatch")
    if variation_two - variation_infinity != 0:
        reject("final polynomial has a root in (2,+infinity)")

    P, critical = rebuild_system(data["high_pairs"])
    # Reconstruct the all-leaves-one specialization directly from the four
    # critical equations and check the claimed common polynomial.
    for index, polynomial in enumerate(critical):
        univariate = {}
        for monomial, coefficient in polynomial.terms.items():
            exponent = monomial[0]
            univariate[exponent] = univariate.get(exponent, Fraction(0)) + coefficient
        highest = max(univariate)
        coefficients = [univariate.get(exponent, Fraction(0)) for exponent in range(highest, -1, -1)]
        normalized = primitive_preserving_sign(coefficients)
        expected = [-4 * value for value in R] if index == 0 else R
        if normalized != primitive_preserving_sign(expected):
            reject("all-leaves-one specialization does not reconstruct R")

    version, script_hash = singular_check(
        P,
        critical,
        data["ideal_consequences"],
        data["expected_saturated_dimension"],
        data["expected_saturated_vector_dimension"],
    )
    output = {
        "status": "ACCEPT",
        "claim": "the corrected ordered star4 chamber contains no saturated critical root",
        "saturated_vector_dimension": 48,
        "sturm_roots_in_open_2_infinity": 0,
        "singular": version,
        "singular_script_sha256": script_hash,
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
