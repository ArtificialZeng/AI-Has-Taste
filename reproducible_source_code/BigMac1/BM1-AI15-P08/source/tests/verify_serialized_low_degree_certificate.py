#!/usr/bin/env python3
"""Fail-closed verifier for certificates/low_degree_identities.json.

The certificate is serialized input.  This program rebuilds a multivariate
Laurent ring over the rationals, parses only a small arithmetic grammar, and
recomputes every listed Schur transform and conjugation identity.  It uses no
CAS and no floating-point arithmetic.  A separately serialized, digest-pinned
manifest binds the certificate to the frozen statement, builder proof/checker,
referee proof/checker, proof audit, and manuscript.
"""

import argparse
import ast
from fractions import Fraction
import hashlib
import json
from pathlib import Path


EXPECTED_CERTIFICATE_SHA256 = (
    "92a5280a7380c140ad758b9d2f346adf3ba4072393890c778056cd50acde8720"
)
EXPECTED_MANIFEST_SHA256 = (
    "a6a5ad4f655b315cf3def4e8f37d4bf89e993a63d0efbb3e3b7007fa480753c3"
)
EXPECTED_CERTIFICATE_PATH = "certificates/low_degree_identities.json"
EXPECTED_FROZEN_ARTIFACTS = {
    "formal_statement": (
        "problem/formal_statement.md",
        "c0cc95ed9411c7ee5751aa37969bb2315440839b3219a3ff166980e7bf88a2be",
    ),
    "builder_proof": (
        "proof/builder_notes.md",
        "126ec4120fd2984a300d35805f074fa932a37b79bf555925f53b12c1d34001df",
    ),
    "builder_checker": (
        "src/builder_symbolic_checks.py",
        "fd8e983f79b22ec2dd2be056e2ae4515f9a46e8321ac89bd6c73f6c5d1775a99",
    ),
    "referee_report": (
        "audit/referee_low_degree.md",
        "4e171752e1dc030ffe2856d22b915e37bcbf2f8ed62ed667003bcf2962dd3fd3",
    ),
    "referee_checker": (
        "tests/referee_low_degree_identities.py",
        "e8e37c700e625342a46bcf15778237f2bc182a66e60c4399166c51750564d3a4",
    ),
    "manuscript_proof": (
        "paper/main.tex",
        "ca929d47781190a84937445afecf5bfa63888e02476316a7b3694395642d86d4",
    ),
}
EXPECTED_CHECKS = {
    "(3.3) first Schur identity",
    "(3.8) derivative Schur coefficients",
    "(3.6) displayed part is real",
    "(3.6) discarded part is pure imaginary",
    "(4.4) first Schur identity",
    "(4.6) second Schur endpoint coefficients",
    "(4.8) boundary decomposition",
    "(5.2) first Schur identity",
    "(5.4) unit-phase transformation",
    "(5.5) second Schur endpoint coefficients",
    "(5.6) boundary decomposition",
}
EXPECTED_GROUPS = (
    (
        "degree_three",
        {"z", "p", "real_part", "full_expression", "remainder"},
        (
            ("(3.3) first Schur identity", "schur"),
            ("(3.8) derivative Schur coefficients", "schur"),
            ("(3.6) displayed part is real", "conjugation"),
            ("(3.6) discarded part is pure imaginary", "conjugation"),
        ),
    ),
    (
        "degree_four",
        {"z", "p", "u", "S"},
        (
            ("(4.4) first Schur identity", "schur"),
            ("(4.6) second Schur endpoint coefficients", "schur"),
            ("(4.8) boundary decomposition", "equal"),
        ),
    ),
    (
        "degree_five",
        {
            "z", "p", "k0", "k1", "k2", "k3", "BB", "CC", "S",
            "ell0", "ell1", "ell2", "ell3",
        },
        (
            ("(5.2) first Schur identity", "schur"),
            ("(5.4) unit-phase transformation", "list_equal"),
            ("(5.5) second Schur endpoint coefficients", "schur_coefficients"),
            ("(5.6) boundary decomposition", "equal"),
        ),
    ),
)


def fail(message):
    raise SystemExit(f"VERIFICATION FAILED: {message}")


def check(condition, message):
    if not condition:
        fail(message)


def exact_keys(value, expected, label):
    check(type(value) is dict, f"{label} is not an object")
    actual = set(value)
    expected = set(expected)
    missing = sorted(expected - actual)
    extra = sorted(actual - expected)
    check(not missing and not extra, f"{label} fields: missing={missing}, extra={extra}")


def expression_text(value, label):
    check(type(value) is str and bool(value.strip()), f"{label} is not a nonempty string")


def expression_list(value, label):
    check(type(value) is list, f"{label} is not a list")
    for index, item in enumerate(value):
        expression_text(item, f"{label}[{index}]")


def sha256_file(path):
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError as error:
        fail(f"cannot read frozen artifact {path}: {error}")


def validate_manifest(manifest, project_root):
    exact_keys(manifest, {"schema_version", "certificate", "frozen_artifacts"}, "manifest")
    check(type(manifest["schema_version"]) is int, "manifest schema_version is not an integer")
    check(manifest["schema_version"] == 1, "unsupported manifest schema")

    certificate = manifest["certificate"]
    exact_keys(certificate, {"path", "sha256"}, "manifest.certificate")
    expression_text(certificate["path"], "manifest.certificate.path")
    expression_text(certificate["sha256"], "manifest.certificate.sha256")
    check(certificate["path"] == EXPECTED_CERTIFICATE_PATH, "unexpected certificate path")
    check(certificate["sha256"] == EXPECTED_CERTIFICATE_SHA256, "unexpected certificate digest")

    artifacts = manifest["frozen_artifacts"]
    check(type(artifacts) is list, "manifest.frozen_artifacts is not a list")
    check(len(artifacts) == len(EXPECTED_FROZEN_ARTIFACTS), "wrong frozen-artifact count")
    seen_roles = set()
    for index, artifact in enumerate(artifacts):
        label = f"manifest.frozen_artifacts[{index}]"
        exact_keys(artifact, {"role", "path", "sha256"}, label)
        for field in ("role", "path", "sha256"):
            expression_text(artifact[field], f"{label}.{field}")
        role = artifact["role"]
        check(role not in seen_roles, f"duplicate frozen-artifact role {role!r}")
        seen_roles.add(role)
        check(role in EXPECTED_FROZEN_ARTIFACTS, f"unexpected frozen-artifact role {role!r}")
        expected_path, expected_digest = EXPECTED_FROZEN_ARTIFACTS[role]
        check(artifact["path"] == expected_path, f"{role}: unexpected path")
        check(artifact["sha256"] == expected_digest, f"{role}: unexpected declared digest")
        actual_digest = sha256_file(project_root / expected_path)
        check(actual_digest == expected_digest, f"{role}: frozen artifact digest {actual_digest}")
    check(seen_roles == set(EXPECTED_FROZEN_ARTIFACTS), "incomplete frozen-artifact roles")
    return certificate


def validate_certificate_schema(certificate):
    exact_keys(
        certificate,
        {"schema_version", "description", "variables", "conjugation", "groups"},
        "certificate",
    )
    check(type(certificate["schema_version"]) is int, "certificate schema_version is not an integer")
    check(certificate["schema_version"] == 1, "unsupported certificate schema")
    expression_text(certificate["description"], "certificate.description")
    check(
        certificate["variables"] == ["q", "d", "D", "b", "B", "c", "C", "r"],
        "unexpected variable inventory or order",
    )

    conjugation = certificate["conjugation"]
    exact_keys(conjugation, {"invert", "swap", "fixed"}, "certificate.conjugation")
    check(conjugation["invert"] == ["q"], "unexpected inverted variables")
    check(
        conjugation["swap"] == [["d", "D"], ["b", "B"], ["c", "C"]],
        "unexpected conjugation swaps",
    )
    check(conjugation["fixed"] == ["r"], "unexpected fixed variables")

    groups = certificate["groups"]
    check(type(groups) is list, "certificate.groups is not a list")
    check(len(groups) == len(EXPECTED_GROUPS), "wrong group count")
    for group_index, (group, expected) in enumerate(zip(groups, EXPECTED_GROUPS)):
        expected_name, expected_definitions, expected_checks = expected
        group_label = f"certificate.groups[{group_index}]"
        exact_keys(group, {"name", "definitions", "checks"}, group_label)
        check(group["name"] == expected_name, f"{group_label}: unexpected name or order")
        definitions = group["definitions"]
        exact_keys(definitions, expected_definitions, f"{group_label}.definitions")
        for name, expression in definitions.items():
            expression_text(expression, f"{group_label}.definitions[{name!r}]")

        checks = group["checks"]
        check(type(checks) is list, f"{group_label}.checks is not a list")
        check(len(checks) == len(expected_checks), f"{group_label}: wrong check count")
        for check_index, (item, expected_check) in enumerate(zip(checks, expected_checks)):
            expected_label, expected_kind = expected_check
            item_label = f"{group_label}.checks[{check_index}]"
            check(type(item) is dict, f"{item_label} is not an object")
            check(item.get("label") == expected_label, f"{item_label}: unexpected label or order")
            check(item.get("kind") == expected_kind, f"{item_label}: unexpected kind")
            kind = expected_kind
            if kind == "schur":
                exact_keys(item, {"kind", "label", "input", "expected"}, item_label)
                expression_list(item["input"], f"{item_label}.input")
                expression_list(item["expected"], f"{item_label}.expected")
            elif kind == "list_equal":
                exact_keys(item, {"kind", "label", "left", "right"}, item_label)
                expression_list(item["left"], f"{item_label}.left")
                expression_list(item["right"], f"{item_label}.right")
            elif kind == "schur_coefficients":
                exact_keys(item, {"kind", "label", "input", "expected"}, item_label)
                expression_list(item["input"], f"{item_label}.input")
                exact_keys(item["expected"], {"0", "-1"}, f"{item_label}.expected")
                for key, expression in item["expected"].items():
                    expression_text(expression, f"{item_label}.expected[{key!r}]")
            elif kind == "equal":
                exact_keys(item, {"kind", "label", "left", "right"}, item_label)
                expression_text(item["left"], f"{item_label}.left")
                expression_text(item["right"], f"{item_label}.right")
            elif kind == "conjugation":
                exact_keys(item, {"kind", "label", "expression", "sign"}, item_label)
                expression_text(item["expression"], f"{item_label}.expression")
                check(type(item["sign"]) is int and item["sign"] in {-1, 1}, f"{item_label}: invalid sign")
            else:
                fail(f"{item_label}: unsupported schema kind {kind!r}")


class Laurent:
    def __init__(self, ring, terms=None):
        self.ring = ring
        self.terms = {
            monomial: Fraction(value)
            for monomial, value in (terms or {}).items()
            if value
        }

    def constant(self, value):
        return Laurent(self.ring, {(0,) * self.ring.rank: Fraction(value)})

    def coerce(self, value):
        return value if isinstance(value, Laurent) else self.constant(value)

    def __add__(self, other):
        other = self.coerce(other)
        out = dict(self.terms)
        for monomial, value in other.terms.items():
            out[monomial] = out.get(monomial, 0) + value
            if not out[monomial]:
                del out[monomial]
        return Laurent(self.ring, out)

    __radd__ = __add__

    def __neg__(self):
        return Laurent(self.ring, {m: -v for m, v in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        out = {}
        for left_monomial, left_value in self.terms.items():
            for right_monomial, right_value in other.terms.items():
                monomial = tuple(
                    left + right
                    for left, right in zip(left_monomial, right_monomial)
                )
                out[monomial] = (
                    out.get(monomial, 0) + left_value * right_value
                )
        return Laurent(self.ring, out)

    __rmul__ = __mul__

    def __truediv__(self, other):
        check(isinstance(other, (int, Fraction)), "division by a non-scalar")
        check(other != 0, "division by zero")
        return self * Fraction(1, other)

    def __pow__(self, power):
        check(isinstance(power, int), "noninteger Laurent exponent")
        if power < 0:
            check(len(self.terms) == 1, "negative power of a nonmonomial")
            (monomial, coefficient), = self.terms.items()
            return Laurent(
                self.ring,
                {
                    tuple(power * exponent for exponent in monomial):
                    coefficient ** power
                },
            )
        result = self.constant(1)
        base = self
        exponent = power
        while exponent:
            if exponent & 1:
                result *= base
            base *= base
            exponent //= 2
        return result

    def __eq__(self, other):
        return self.terms == self.coerce(other).terms

    def __repr__(self):
        return repr(self.terms)


class Ring:
    def __init__(self, variables, conjugation):
        self.variables = tuple(variables)
        self.rank = len(self.variables)
        self.index = {name: i for i, name in enumerate(self.variables)}
        check(len(self.index) == self.rank, "duplicate variable name")
        self.inverted = {self.index[name] for name in conjugation["invert"]}
        self.conjugate_index = list(range(self.rank))
        for left, right in conjugation["swap"]:
            left_index, right_index = self.index[left], self.index[right]
            self.conjugate_index[left_index] = right_index
            self.conjugate_index[right_index] = left_index
        covered = set(conjugation["invert"]) | set(conjugation["fixed"])
        covered |= {name for pair in conjugation["swap"] for name in pair}
        check(covered == set(self.variables), "incomplete conjugation metadata")

    def variable(self, name):
        monomial = [0] * self.rank
        monomial[self.index[name]] = 1
        return Laurent(self, {tuple(monomial): Fraction(1)})

    def conjugate(self, expression):
        out = {}
        for monomial, coefficient in expression.terms.items():
            transformed = [0] * self.rank
            for source, exponent in enumerate(monomial):
                target = self.conjugate_index[source]
                transformed[target] += -exponent if source in self.inverted else exponent
            transformed = tuple(transformed)
            out[transformed] = out.get(transformed, 0) + coefficient
        return Laurent(self, out)


def exponent_value(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, int):
        return node.value
    if (
        isinstance(node, ast.UnaryOp)
        and isinstance(node.op, ast.USub)
        and isinstance(node.operand, ast.Constant)
        and isinstance(node.operand.value, int)
    ):
        return -node.operand.value
    fail("power is not a literal integer")


def evaluate(text, environment):
    try:
        tree = ast.parse(text, mode="eval")
    except SyntaxError as error:
        fail(f"invalid certificate expression {text!r}: {error}")

    def walk(node):
        if isinstance(node, ast.Expression):
            return walk(node.body)
        if isinstance(node, ast.Name):
            check(node.id in environment, f"unknown name {node.id!r}")
            return environment[node.id]
        if isinstance(node, ast.Constant) and isinstance(node.value, int):
            return next(iter(environment.values())).constant(node.value)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
            return -walk(node.operand)
        if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.UAdd):
            return walk(node.operand)
        if isinstance(node, ast.BinOp):
            if isinstance(node.op, ast.Pow):
                return walk(node.left) ** exponent_value(node.right)
            left, right = walk(node.left), walk(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            if isinstance(node.op, ast.Sub):
                return left - right
            if isinstance(node.op, ast.Mult):
                return left * right
            if isinstance(node.op, ast.Div):
                check(
                    isinstance(node.right, ast.Constant)
                    and isinstance(node.right.value, int),
                    "certificate division denominator is not an integer literal",
                )
                return left / node.right.value
        fail(f"disallowed certificate syntax: {ast.dump(node)}")

    return walk(tree)


def schur(coefficients, ring):
    reversed_conjugate = [ring.conjugate(value) for value in reversed(coefficients)]
    leading_conjugate = ring.conjugate(coefficients[-1])
    numerator = [
        leading_conjugate * value - coefficients[0] * reversed_value
        for value, reversed_value in zip(coefficients, reversed_conjugate)
    ]
    check(numerator[0] == 0, "Schur numerator has nonzero constant term")
    return numerator[1:]


def compare_lists(actual, expected, label):
    check(len(actual) == len(expected), f"{label}: length mismatch")
    for index, (left, right) in enumerate(zip(actual, expected)):
        check(left == right, f"{label}: coefficient {index}, residual {left-right}")


def verify(certificate):
    ring = Ring(certificate["variables"], certificate["conjugation"])
    base_environment = {name: ring.variable(name) for name in ring.variables}
    passed = 0
    seen_labels = set()
    for group in certificate["groups"]:
        environment = dict(base_environment)
        for name, expression in group["definitions"].items():
            check(name not in environment, f"definition shadows variable {name}")
            environment[name] = evaluate(expression, environment)
        for item in group["checks"]:
            kind = item["kind"]
            label = item["label"]
            check(label not in seen_labels, f"duplicate check label {label!r}")
            seen_labels.add(label)
            if kind == "schur":
                actual = schur([evaluate(x, environment) for x in item["input"]], ring)
                expected = [evaluate(x, environment) for x in item["expected"]]
                compare_lists(actual, expected, label)
            elif kind == "list_equal":
                actual = [evaluate(x, environment) for x in item["left"]]
                expected = [evaluate(x, environment) for x in item["right"]]
                compare_lists(actual, expected, label)
            elif kind == "schur_coefficients":
                actual = schur([evaluate(x, environment) for x in item["input"]], ring)
                for index_text, expected_text in item["expected"].items():
                    index = int(index_text)
                    expected = evaluate(expected_text, environment)
                    check(actual[index] == expected, f"{label}: coefficient {index}")
            elif kind == "equal":
                left = evaluate(item["left"], environment)
                right = evaluate(item["right"], environment)
                check(left == right, f"{label}: residual {left-right}")
            elif kind == "conjugation":
                expression = evaluate(item["expression"], environment)
                expected = item["sign"] * expression
                check(ring.conjugate(expression) == expected, label)
            else:
                fail(f"unknown check kind {kind!r}")
            print("PASS", label)
            passed += 1
    check(seen_labels == EXPECTED_CHECKS, "incomplete or unexpected check inventory")
    check(passed == len(EXPECTED_CHECKS), "incorrect verified-check count")
    return passed


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        check(key not in result, f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def parse_json(raw, label):
    try:
        return json.loads(raw, object_pairs_hook=no_duplicate_keys)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        fail(f"invalid {label} JSON: {error}")


def apply_tamper_case(raw, certificate, tamper_case):
    if tamper_case == "badhash":
        return raw + b"\n", certificate
    if tamper_case == "extra-field":
        certificate["unexpected_root_field"] = "must be rejected"
    elif tamper_case == "drop-check":
        del certificate["groups"][0]["checks"][-1]
    elif tamper_case == "change-expression":
        certificate["groups"][0]["checks"][0]["expected"][0] = "p*z**-2 + 1"
    return raw, certificate


def main():
    parser = argparse.ArgumentParser()
    project_root = Path(__file__).resolve().parents[1]
    default_certificate = project_root / EXPECTED_CERTIFICATE_PATH
    default_manifest = project_root / "certificates" / "low_degree_certificate_manifest.json"
    parser.add_argument("certificate", nargs="?", type=Path, default=default_certificate)
    parser.add_argument("--manifest", type=Path, default=default_manifest)
    parser.add_argument("--inject-failure", action="store_true")
    parser.add_argument(
        "--tamper-case",
        choices=("badhash", "extra-field", "drop-check", "change-expression"),
    )
    args = parser.parse_args()

    manifest_raw = args.manifest.read_bytes()
    manifest_digest = hashlib.sha256(manifest_raw).hexdigest()
    check(
        manifest_digest == EXPECTED_MANIFEST_SHA256,
        f"manifest digest {manifest_digest} is not the audited canonical digest",
    )
    manifest = parse_json(manifest_raw, "manifest")
    manifest_certificate = validate_manifest(manifest, project_root)

    raw = args.certificate.read_bytes()
    certificate = parse_json(raw, "certificate")
    raw, certificate = apply_tamper_case(raw, certificate, args.tamper_case)
    digest = hashlib.sha256(raw).hexdigest()
    check(
        digest == manifest_certificate["sha256"] == EXPECTED_CERTIFICATE_SHA256,
        f"certificate digest {digest} is not the audited canonical digest",
    )
    check(
        args.certificate.resolve() == (project_root / manifest_certificate["path"]).resolve(),
        "certificate path is not the manifest-bound canonical path",
    )
    validate_certificate_schema(certificate)
    if args.inject_failure:
        fail("injected fail-closed self-test")
    count = verify(certificate)
    print(
        "serialized certificate: OK "
        f"({count} checks, certificate_sha256={digest}, manifest_sha256={manifest_digest})"
    )


if __name__ == "__main__":
    main()
