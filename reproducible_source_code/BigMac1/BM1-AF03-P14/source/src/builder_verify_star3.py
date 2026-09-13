#!/usr/bin/env python3
"""Independent exact verifier for certificates/star3_decomposition.json.

The verifier reconstructs the box-spline chamber system without importing
discovery output, proves the saturated-ideal decomposition with Singular,
checks the algebraic parametrizations and real-root isolation with SymPy exact
arithmetic, and runs fail-closed mutation tests.
"""

from __future__ import annotations

import copy
import hashlib
import itertools
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
CERTIFICATE = PROJECT / "certificates" / "star3_decomposition.json"
EXPECTED_PAIRS = [[0, 1], [0, 2], [0, 3]]
EXPECTED_VARIABLES = ["a0", "a1", "a2", "a3"]
EXPECTED_COMPONENT_IDS = {
    "equal_branch", "large_at_a1", "large_at_a2", "large_at_a3"
}


class CertificateRejected(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CertificateRejected(message)


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_noncanonical_booleans(
    value: object, path: tuple[object, ...] = ()
) -> None:
    if type(value) is bool:
        require(
            path == ("classification", "radical") and value is True,
            f"boolean forbidden in certificate at {path}",
        )
        return
    if type(value) is dict:
        for key, child in value.items():
            reject_noncanonical_booleans(child, (*path, key))
    elif type(value) is list:
        for index, child in enumerate(value):
            reject_noncanonical_booleans(child, (*path, index))


def rational(text: str) -> sp.Rational:
    value = sp.sympify(text)
    require(bool(value.is_Rational), f"non-rational endpoint: {text}")
    return sp.Rational(value)


def parse_expr(text: str, names: dict[str, sp.Symbol]) -> sp.Expr:
    allowed = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_+-*/() .")
    require(set(text) <= allowed, f"disallowed character in expression: {text}")
    try:
        expr = sp.sympify(text, locals=names, evaluate=True)
    except Exception as exc:  # fail closed on malformed input
        raise CertificateRejected(f"cannot parse expression {text!r}: {exc}") from exc
    require(not (expr.free_symbols - set(names.values())), f"unknown symbol in {text}")
    return expr


def reconstruct_system(negative_pairs: list[list[int]]):
    require(negative_pairs == EXPECTED_PAIRS, "certificate is not the star3 chamber")
    a = sp.symbols("a0:5")
    squared_norm = sum(x*x for x in a)
    threshold = sum(a) / 2
    numerator = threshold**4 - sum((threshold - x)**4 for x in a)
    numerator += sum(
        (threshold - a[i] - a[j])**4
        for i, j in itertools.combinations(range(5), 2)
    )
    numerator -= 2 * sum(
        (threshold - a[i] - a[j])**4 for i, j in negative_pairs
    )
    numerator = sp.expand(numerator)
    critical = [
        sp.expand(a[i]*squared_norm*sp.diff(numerator, a[i])
                  + (a[i]**2-squared_norm)*numerator)
        for i in range(5)
    ]
    substitution = {a[4]: 1}
    variables = a[:4]
    polynomials = [
        sp.Poly(sp.expand(expr.subs(substitution)), *variables, domain=sp.QQ)
        for expr in [numerator, *critical[:4]]
    ]
    denominator = sp.ilcm(*[
        coefficient.denominator
        for polynomial in polynomials
        for _, coefficient in polynomial.terms()
    ])
    polynomials = [
        sp.Poly(sp.expand(polynomial.as_expr()*denominator), *variables, domain=sp.ZZ)
        for polynomial in polynomials
    ]
    common = 0
    for polynomial in polynomials:
        common = sp.igcd(common, int(sp.gcd_list(polynomial.coeffs())))
    if common > 1:
        polynomials = [
            sp.Poly(polynomial.as_expr()/common, *variables, domain=sp.ZZ)
            for polynomial in polynomials
        ]
    p, *g = polynomials
    s = sp.Poly(sp.expand(squared_norm.subs(substitution)), *variables, domain=sp.ZZ)
    payload = {
        "variables": [str(x) for x in variables],
        "P": str(p.as_expr()),
        "S": str(s.as_expr()),
        "A4": "1",
        "G": [str(polynomial.as_expr()) for polynomial in g],
    }
    digest = hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    return variables, p, g, s, digest


def remainder_zero(expr: sp.Expr, minimal: sp.Poly, parameter: sp.Symbol) -> bool:
    numerator, denominator = sp.cancel(expr).as_numer_denom()
    require(sp.gcd(sp.Poly(denominator, parameter), minimal).degree() == 0,
            "parameter denominator can vanish on the component")
    return sp.rem(sp.Poly(numerator, parameter), minimal).is_zero


def verify_components(data, variables, p, g, s):
    components = data.get("components")
    require(isinstance(components, list) and len(components) == 4,
            "expected exactly four components")
    require({entry.get("id") for entry in components} == EXPECTED_COMPONENT_IDS,
            "component IDs mismatch")
    total_degree = 0
    total_real = 0
    parsed = []
    a4 = sp.Integer(1)
    threshold = (sum(variables) + a4) / 2
    pair_forms = [
        sp.expand(threshold - ([*variables, a4][i]) - ([*variables, a4][j]))
        for i, j in itertools.combinations(range(5), 2)
    ]
    critical_jacobian = sp.Matrix([polynomial.as_expr() for polynomial in g]).jacobian(variables)

    for entry in components:
        require(set(entry) == {
            "id", "degree", "parameter", "minimal_polynomial",
            "real_isolating_intervals", "coordinates", "ideal_generators"
        }, f"unexpected component schema in {entry.get('id')}")
        parameter = sp.Symbol(entry["parameter"])
        names = {str(x): x for x in variables}
        names[str(parameter)] = parameter
        minimal_expr = parse_expr(entry["minimal_polynomial"], names)
        minimal = sp.Poly(minimal_expr, parameter, domain=sp.QQ)
        require(minimal.degree() == entry["degree"], "component degree mismatch")
        require(sp.gcd(minimal, minimal.diff()).degree() == 0,
                "component minimal polynomial is not squarefree")
        coordinates = [parse_expr(text, names) for text in entry["coordinates"]]
        require(len(coordinates) == 4, "component must specify four coordinates")
        substitution = dict(zip(variables, coordinates))

        for polynomial in g:
            require(remainder_zero(polynomial.as_expr().subs(substitution), minimal, parameter),
                    f"component {entry['id']} does not solve the critical system")

        # The original four critical equations, not just the decomposed ideal,
        # have full Jacobian rank at every component root.
        jacobian_entries = []
        for jacobian_entry in critical_jacobian.subs(substitution):
            numerator, denominator = sp.cancel(jacobian_entry).as_numer_denom()
            inverse = sp.invert(sp.Poly(denominator, parameter), minimal).as_expr()
            jacobian_entries.append(
                sp.rem(sp.Poly(numerator*inverse, parameter), minimal).as_expr()
            )
        determinant = sp.Matrix(4, 4, jacobian_entries).det()
        determinant_remainder = sp.rem(sp.Poly(determinant, parameter), minimal)
        require(sp.gcd(determinant_remainder, minimal).degree() == 0,
                f"multiple or Jacobian-degenerate root in {entry['id']}")

        # Saturation multiplier must be a unit in Q[parameter]/(minimal).
        multiplier = sp.prod(coordinates) * p.as_expr().subs(substitution) * s.as_expr().subs(substitution)
        multiplier_num, multiplier_den = sp.cancel(multiplier).as_numer_denom()
        require(sp.gcd(sp.Poly(multiplier_den, parameter), minimal).degree() == 0,
                "saturation denominator meets component")
        require(sp.gcd(sp.Poly(multiplier_num, parameter), minimal).degree() == 0,
                "saturation multiplier vanishes on component")

        # No component root is on a pair-sum wall.
        for form in pair_forms:
            wall_num = sp.cancel(form.subs(substitution)).as_numer_denom()[0]
            require(sp.gcd(sp.Poly(wall_num, parameter), minimal).degree() == 0,
                    f"component {entry['id']} meets a subset-sum wall")

        intervals = entry["real_isolating_intervals"]
        require(isinstance(intervals, list), "isolating intervals must be a list")
        last_right = None
        for left_text, right_text in intervals:
            left, right = rational(left_text), rational(right_text)
            require(left < right, "reversed isolating interval")
            if last_right is not None:
                require(last_right < left, "overlapping isolating intervals")
            require(minimal.count_roots(left, right) == 1,
                    "interval does not isolate exactly one real root")
            require(minimal.eval(left) != 0 and minimal.eval(right) != 0,
                    "root lies on isolating endpoint")
            last_right = right
        real_count = int(minimal.count_roots(-sp.oo, sp.oo))
        require(real_count == len(intervals), "real isolating intervals are incomplete")
        total_real += real_count
        total_degree += minimal.degree()
        generators = [parse_expr(text, names) for text in entry["ideal_generators"]]
        require(len(generators) == 4, "each component needs four ideal generators")
        for generator in generators:
            require(remainder_zero(generator.subs(substitution), minimal, parameter),
                    f"component parametrization does not satisfy {entry['id']} generators")
        # The parameter itself occurs as a coordinate, so distinct roots of
        # the squarefree minimal polynomial give distinct points.
        require(any(sp.simplify(x-parameter) == 0 for x in coordinates),
                "component parametrization does not expose its parameter")
        parsed.append((entry, minimal, coordinates, generators))

    require(total_degree == data["expected_complex_points"] == 14,
            "complex point count mismatch")
    require(total_real == data["expected_real_points"] == 8,
            "real point count mismatch")
    return parsed


def singular_text(expr: sp.Expr) -> str:
    return str(sp.expand(expr)).replace("**", "^")


def verify_ideal_equality(variables, p, g, s, parsed, expected_dimension):
    singular = shutil.which("Singular")
    require(singular is not None, "Singular executable is unavailable")
    lines = [
        f"ring r=0,({','.join(map(str, variables))}),dp;",
        f"poly P={singular_text(p.as_expr())};",
        f"poly S={singular_text(s.as_expr())};",
    ]
    for index, polynomial in enumerate(g):
        lines.append(f"poly g{index}={singular_text(polynomial.as_expr())};")
    lines += [
        "ideal I=g0,g1,g2,g3;",
        'LIB "elim.lib";',
        "ideal M=a0*a1*a2*a3*P*S;",
        "ideal Q=sat(I,M);",
    ]
    component_names = []
    for index, (_, _, _, generators) in enumerate(parsed):
        name = f"J{index}"
        component_names.append(name)
        lines.append(f"ideal {name}=" + ",".join(singular_text(x) for x in generators) + ";")
        lines.append(f"ideal {name}S=std({name});")
    intersection = component_names[-1]
    for name in reversed(component_names[:-1]):
        intersection = f"intersect({name},{intersection})"
    lines += [
        f"ideal K={intersection};",
        "ideal QS=std(Q); ideal KS=std(K);",
        "ideal RQ=simplify(reduce(QS,KS),2);",
        "ideal RK=simplify(reduce(KS,QS),2);",
        'print("BEGIN_CERT");',
        'print("DIMQ"); print(dim(QS));',
        'print("VDIMQ"); print(vdim(QS));',
        'print("DIMK"); print(dim(KS));',
        'print("VDIMK"); print(vdim(KS));',
        'print("REM_QK"); print(size(RQ));',
        'print("REM_KQ"); print(size(RK));',
    ]
    for index, (entry, _, _, _) in enumerate(parsed):
        lines += [
            f'print("DIMJ{index}"); print(dim(J{index}S));',
            f'print("VDIMJ{index}"); print(vdim(J{index}S));',
        ]
    lines.append('print("END_CERT");')
    with tempfile.TemporaryDirectory(prefix="star3_verify_") as temp_dir:
        program = Path(temp_dir) / "verify.sing"
        program.write_text("\n".join(lines) + "\n", encoding="utf-8")
        process = subprocess.run(
            [singular, "-q", str(program)], capture_output=True, text=True,
            timeout=120, check=False,
        )
    require(process.returncode == 0, f"Singular failed: {process.stderr}\n{process.stdout}")
    require("?" not in process.stdout and "error" not in process.stderr.lower(),
            f"Singular reported an error: {process.stderr}\n{process.stdout}")
    segment = process.stdout.split("BEGIN_CERT\n", 1)
    require(len(segment) == 2 and "\nEND_CERT" in segment[1], "missing Singular sentinels")
    values = segment[1].split("\nEND_CERT", 1)[0].strip().splitlines()
    expected = [
        "DIMQ", "0", "VDIMQ", str(expected_dimension),
        "DIMK", "0", "VDIMK", str(expected_dimension),
        "REM_QK", "0", "REM_KQ", "0",
    ]
    for index, (entry, _, _, _) in enumerate(parsed):
        expected += [f"DIMJ{index}", "0", f"VDIMJ{index}", str(entry["degree"])]
    require(values == expected, f"ideal-decomposition certificate failed: {values}")


def verify_real_classification(data, parsed):
    # The positive equal-branch root has t in (1/2,2/3), hence a3=t<1.
    equal = next(item for item in parsed if item[0]["id"] == "equal_branch")
    require(equal[0]["real_isolating_intervals"][1] == ["1/2", "2/3"],
            "unexpected positive equal-branch isolator")

    # Every positive quartic-branch root has s in (2/5,1/2).  Two of
    # a1,a2,a3 equal s in each permutation, so a3>=1 (indeed all three >=1)
    # cannot hold after fixing a4=1.  Negative roots fail positivity.
    for entry, _, coordinates, _ in parsed:
        if entry["id"] == "equal_branch":
            continue
        require(entry["real_isolating_intervals"][1] == ["2/5", "1/2"],
                "unexpected positive quartic-branch isolator")
        parameter = sp.Symbol(entry["parameter"])
        occurrences = sum(sp.simplify(x-parameter) == 0 for x in coordinates[1:])
        require(occurrences == 2, "quartic branch does not have two small coordinates")

    classification = data.get("classification")
    require(classification == {
        "radical": True,
        "multiple_complex_roots": 0,
        "subset_sum_wall_roots": 0,
        "ordered_star3_closure_roots": 0,
    }, "classification metadata mismatch")


def verify_certificate(data, run_singular=True):
    reject_noncanonical_booleans(data)
    require(set(data) == {
        "schema_version", "endpoint", "variables", "fixed_coordinate",
        "negative_pairs", "saturation_factors", "system_sha256",
        "expected_quotient_dimension", "expected_complex_points",
        "expected_real_points", "ordered_chamber", "components", "classification"
    }, "unexpected top-level certificate schema")
    require(type(data["schema_version"]) is int and data["schema_version"] == 1,
            "unsupported schema")
    require(data["variables"] == EXPECTED_VARIABLES, "variable order mismatch")
    require(data["fixed_coordinate"] == "a4=1", "normalization mismatch")
    require(data["saturation_factors"] == ["a0", "a1", "a2", "a3", "P", "S"],
            "saturation multiplier mismatch")
    variables, p, g, s, digest = reconstruct_system(data["negative_pairs"])
    require(digest == data["system_sha256"], "reconstructed system hash mismatch")
    parsed = verify_components(data, variables, p, g, s)
    verify_real_classification(data, parsed)
    if run_singular:
        verify_ideal_equality(
            variables, p, g, s, parsed, data["expected_quotient_dimension"]
        )


def mutation_tests(original):
    mutations = []

    changed_edge = copy.deepcopy(original)
    changed_edge["negative_pairs"] = [[0, 1], [0, 2]]
    mutations.append(("removed_star_edge", changed_edge, False))

    changed_polynomial = copy.deepcopy(original)
    changed_polynomial["components"][1]["minimal_polynomial"] = "2*s**4+6*s**2-1"
    mutations.append(("changed_minpoly_coefficient", changed_polynomial, False))

    changed_generator = copy.deepcopy(original)
    changed_generator["components"][3]["ideal_generators"][2] = "2*a1*a3-a1**2-2"
    mutations.append(("changed_component_generator", changed_generator, True))

    changed_hash = copy.deepcopy(original)
    changed_hash["system_sha256"] = "0" * 64
    mutations.append(("changed_system_hash", changed_hash, False))

    for name, mutated, needs_singular in mutations:
        try:
            verify_certificate(mutated, run_singular=needs_singular)
        except CertificateRejected:
            print(f"mutation rejected: {name}")
        else:
            raise CertificateRejected(f"mutation was incorrectly accepted: {name}")


def main():
    if len(sys.argv) > 2:
        raise SystemExit("usage: builder_verify_star3.py [CERTIFICATE.json]")
    certificate = Path(sys.argv[1]) if len(sys.argv) == 2 else CERTIFICATE
    try:
        data = json.loads(
            certificate.read_text(encoding="utf-8"),
            object_pairs_hook=reject_duplicate_keys,
        )
        verify_certificate(data, run_singular=True)
        mutation_tests(data)
    except (CertificateRejected, json.JSONDecodeError, OSError,
            subprocess.SubprocessError) as exc:
        raise SystemExit(f"star3 verifier: FAIL: {exc}") from exc
    print("star3 verifier: PASS")


if __name__ == "__main__":
    main()
