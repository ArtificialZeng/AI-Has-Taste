#!/usr/bin/env python3
"""Independent exact verifier for the n=7 geometric Max-Cut certificate.

Only the Python standard library is used.  All cut weights, difference
polynomials, factor removals, threshold signs, Descartes sign changes, and
Sturm root counts are recomputed from the locked definitions.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CERTIFICATE = ROOT / "certificates" / "n7_sturm_certificate.json"


class VerificationError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def require_keys(obj: dict, expected: set[str], location: str) -> None:
    require(isinstance(obj, dict), f"{location}: expected object")
    actual = set(obj)
    require(actual == expected, f"{location}: keys {sorted(actual)} != {sorted(expected)}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def trim(poly: list[Fraction]) -> list[Fraction]:
    if not poly:
        return [Fraction(0)]
    result = list(poly)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def as_poly(coefficients: object, location: str) -> list[Fraction]:
    require(isinstance(coefficients, list) and coefficients, f"{location}: bad coefficient list")
    require(all(type(c) is int for c in coefficients), f"{location}: coefficients must be integers")
    result = trim([Fraction(c) for c in coefficients])
    require([int(c) for c in result] == coefficients, f"{location}: noncanonical trailing zero")
    return result


def poly_sub(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    length = max(len(a), len(b))
    return trim(
        [
            (a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
            for i in range(length)
        ]
    )


def poly_scale_shift(poly: list[Fraction], scalar: int, shift: int) -> list[Fraction]:
    require(shift >= 0, "negative monomial shift")
    return trim([Fraction(0)] * shift + [Fraction(scalar) * c for c in poly])


def derivative(poly: list[Fraction]) -> list[Fraction]:
    if len(poly) <= 1:
        return [Fraction(0)]
    return trim([Fraction(i) * poly[i] for i in range(1, len(poly))])


def poly_divmod(
    numerator: list[Fraction], denominator: list[Fraction]
) -> tuple[list[Fraction], list[Fraction]]:
    numerator = trim(numerator)
    denominator = trim(denominator)
    require(denominator != [0], "polynomial division by zero")
    if len(numerator) < len(denominator):
        return [Fraction(0)], numerator
    quotient = [Fraction(0)] * (len(numerator) - len(denominator) + 1)
    remainder = list(numerator)
    while remainder != [0] and len(remainder) >= len(denominator):
        degree = len(remainder) - len(denominator)
        coefficient = remainder[-1] / denominator[-1]
        quotient[degree] += coefficient
        for i, value in enumerate(denominator):
            remainder[i + degree] -= coefficient * value
        remainder = trim(remainder)
    return trim(quotient), trim(remainder)


def evaluate(poly: list[Fraction], point: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(poly):
        value = value * point + coefficient
    return value


def sign(value: Fraction) -> int:
    return 1 if value > 0 else -1 if value < 0 else 0


def sign_variations(values: list[Fraction]) -> int:
    signs = [sign(value) for value in values if value != 0]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def sturm_chain(poly: list[Fraction]) -> list[list[Fraction]]:
    poly = trim(poly)
    require(poly != [0], "zero polynomial has no Sturm chain")
    if len(poly) == 1:
        return [poly]
    chain = [poly, derivative(poly)]
    while chain[-1] != [0]:
        _, remainder = poly_divmod(chain[-2], chain[-1])
        if remainder == [0]:
            break
        chain.append([-coefficient for coefficient in remainder])
    return chain


def sturm_root_count(poly: list[Fraction], left: Fraction, right: Fraction) -> tuple[int, int, int, int]:
    require(left < right, "Sturm interval is not increasing")
    require(evaluate(poly, left) != 0 and evaluate(poly, right) != 0, "root at Sturm endpoint")
    chain = sturm_chain(poly)
    left_variations = sign_variations([evaluate(item, left) for item in chain])
    right_variations = sign_variations([evaluate(item, right) for item in chain])
    count = left_variations - right_variations
    require(count >= 0, "negative Sturm root count")
    return count, left_variations, right_variations, len(chain)


def positive_sign_changes(poly: list[Fraction]) -> int:
    signs = [sign(c) for c in reversed(poly) if c != 0]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def mask_bits(mask: int) -> int:
    require(type(mask) is int and 0 <= mask < 64, f"bad canonical mask {mask!r}")
    return 1 | (mask << 1)


def weight_by_index_formula(mask: int) -> list[Fraction]:
    bits = mask_bits(mask)
    coefficients = [Fraction(0)] * 21
    for i in range(1, 8):
        for j in range(i + 1, 8):
            index = 7 * (i - 1) - (i * (i - 1)) // 2 + (j - i)
            exponent = 21 - index
            crosses = ((bits >> (i - 1)) & 1) ^ ((bits >> (j - 1)) & 1)
            coefficients[exponent] += crosses
    return trim(coefficients)


def weight_by_cut_vector(mask: int) -> list[Fraction]:
    """Second evaluator: combinations order is paired with exponents 20,...,0."""
    bits = mask_bits(mask)
    crossing_vector = [
        ((bits >> i) & 1) ^ ((bits >> j) & 1)
        for i, j in itertools.combinations(range(7), 2)
    ]
    require(len(crossing_vector) == 21, "bad cut-vector length")
    coefficients = [Fraction(0)] * 21
    for position, crosses in enumerate(crossing_vector):
        coefficients[20 - position] = Fraction(crosses)
    return trim(coefficients)


def strip_x_minus_one(poly: list[Fraction]) -> tuple[int, list[Fraction]]:
    factor = [Fraction(-1), Fraction(1)]
    multiplicity = 0
    residual = poly
    while evaluate(residual, Fraction(1)) == 0:
        quotient, remainder = poly_divmod(residual, factor)
        require(remainder == [0], "x-1 exact division failed")
        residual = quotient
        multiplicity += 1
    return multiplicity, residual


def parse_fraction(value: object, location: str) -> Fraction:
    require(isinstance(value, str), f"{location}: rational must be a string")
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise VerificationError(f"{location}: invalid rational") from exc
    require(str(result) == value or (result.denominator == 1 and value == str(result.numerator)),
            f"{location}: rational is not canonical")
    return result


def verify(certificate_path: Path) -> dict:
    try:
        certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise VerificationError(f"cannot parse certificate: {exc}") from exc

    require_keys(
        certificate,
        {
            "schema_version", "task_id", "n", "cut_count", "canonical_masks",
            "edge_order", "weight_exponents", "theorem_sha256", "generator",
            "thresholds", "regions",
        },
        "certificate",
    )
    require(certificate["schema_version"] == 1, "unsupported schema")
    require(certificate["task_id"] == "04_geometric_maxcut_n7", "wrong task")
    require(certificate["n"] == 7 and certificate["cut_count"] == 64, "wrong finite instance")
    require(certificate["canonical_masks"] == list(range(64)), "canonical masks are incomplete")

    expected_edges = [list(pair) for pair in itertools.combinations(range(1, 8), 2)]
    require(certificate["edge_order"] == expected_edges, "edge order mismatch")
    require(certificate["weight_exponents"] == list(range(20, -1, -1)), "weight exponents mismatch")
    require(
        certificate["theorem_sha256"] == sha256(ROOT / "problem" / "formal_statement.md"),
        "certificate is not bound to the current locked theorem",
    )
    require_keys(certificate["generator"], {"file", "sha256", "python", "sympy"}, "generator")

    weights = {}
    for mask in range(64):
        first = weight_by_index_formula(mask)
        second = weight_by_cut_vector(mask)
        require(first == second, f"independent weight evaluators disagree at mask {mask}")
        weights[mask] = first
    require(len({tuple(poly) for poly in weights.values()}) == 64, "cut polynomials are not unique")

    require_keys(certificate["thresholds"], {"alpha", "beta"}, "thresholds")
    threshold_polys = {}
    threshold_intervals = {}
    expected_threshold_coeffs = {
        "alpha": [-1, -1, -1, -1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        "beta": [-1, -1, -1, -1, -1, 0, 0, 0, 0, 0, 1],
    }
    for name in ("alpha", "beta"):
        data = certificate["thresholds"][name]
        require_keys(
            data,
            {"polynomial_coefficients", "isolating_interval", "endpoint_signs", "positive_sign_changes"},
            f"thresholds.{name}",
        )
        require(data["polynomial_coefficients"] == expected_threshold_coeffs[name], f"wrong {name} polynomial")
        poly = as_poly(data["polynomial_coefficients"], f"thresholds.{name}.polynomial")
        require(isinstance(data["isolating_interval"], list) and len(data["isolating_interval"]) == 2,
                f"bad {name} interval")
        left = parse_fraction(data["isolating_interval"][0], f"{name}.left")
        right = parse_fraction(data["isolating_interval"][1], f"{name}.right")
        require(Fraction(1) < left < right < Fraction(2), f"{name} isolator outside (1,2)")
        endpoint_signs = [sign(evaluate(poly, left)), sign(evaluate(poly, right))]
        require(data["endpoint_signs"] == [-1, 1] == endpoint_signs, f"{name} endpoint signs fail")
        changes = positive_sign_changes(poly)
        require(data["positive_sign_changes"] == 1 == changes, f"{name} Descartes uniqueness fails")
        threshold_polys[name] = poly
        threshold_intervals[name] = (left, right)
    require(threshold_intervals["alpha"][1] < threshold_intervals["beta"][0], "threshold order not certified")

    expected_regions = {
        "C3": (3, Fraction(1), Fraction(1079, 1000), Fraction(21, 20), {1: ("alpha", "left", -1, 6)}),
        "C2": (1, Fraction(539, 500), Fraction(123, 100), Fraction(23, 20),
               {3: ("alpha", "right", 1, 6), 0: ("beta", "left", -1, 10)}),
        "C1": (0, Fraction(1229, 1000), Fraction(2), Fraction(3, 2), {1: ("beta", "right", 1, 10)}),
    }
    require(isinstance(certificate["regions"], list) and len(certificate["regions"]) == 3,
            "expected exactly three regions")

    total_sturm = 0
    total_threshold = 0
    max_chain_length = 0
    max_degree = 0
    seen_region_ids = set()
    for region_index, region in enumerate(certificate["regions"]):
        require_keys(region, {"id", "target_mask", "superinterval", "sample", "records"},
                     f"regions[{region_index}]")
        region_id = region["id"]
        require(region_id in expected_regions and region_id not in seen_region_ids, "bad/duplicate region")
        seen_region_ids.add(region_id)
        target_mask, expected_left, expected_right, expected_sample, boundary_map = expected_regions[region_id]
        require(region["target_mask"] == target_mask, f"{region_id}: target mismatch")
        require(isinstance(region["superinterval"], list) and len(region["superinterval"]) == 2,
                f"{region_id}: bad superinterval")
        left = parse_fraction(region["superinterval"][0], f"{region_id}.left")
        right = parse_fraction(region["superinterval"][1], f"{region_id}.right")
        sample = parse_fraction(region["sample"], f"{region_id}.sample")
        require((left, right, sample) == (expected_left, expected_right, expected_sample),
                f"{region_id}: unexpected rational bounds/sample")
        require(left < sample < right, f"{region_id}: sample outside superinterval")
        require(isinstance(region["records"], list) and len(region["records"]) == 63,
                f"{region_id}: expected 63 records")
        seen_masks = set()
        for record_index, record in enumerate(region["records"]):
            location = f"{region_id}.records[{record_index}]"
            require(isinstance(record, dict), f"{location}: expected object")
            mode = record.get("mode")
            common = {"competitor_mask", "difference_coefficients", "mode"}
            if mode == "sturm":
                require_keys(
                    record,
                    common | {"removed_x_minus_one", "residual_coefficients", "sympy_root_count",
                              "residual_endpoint_signs"},
                    location,
                )
            elif mode == "threshold":
                require_keys(
                    record,
                    common | {"threshold", "orientation", "multiplier", "monomial_power"},
                    location,
                )
            else:
                raise VerificationError(f"{location}: unknown mode")

            competitor_mask = record["competitor_mask"]
            require(type(competitor_mask) is int and 0 <= competitor_mask < 64,
                    f"{location}: bad competitor mask")
            require(competitor_mask != target_mask and competitor_mask not in seen_masks,
                    f"{location}: duplicate/target mask")
            seen_masks.add(competitor_mask)
            difference = poly_sub(weights[target_mask], weights[competitor_mask])
            encoded_difference = as_poly(record["difference_coefficients"], f"{location}.difference")
            require(difference == encoded_difference, f"{location}: difference polynomial mismatch")
            require(sign(evaluate(difference, sample)) == 1, f"{location}: nonpositive exact sample")

            if mode == "threshold":
                total_threshold += 1
                require(competitor_mask in boundary_map, f"{location}: unauthorized threshold exception")
                expected_name, expected_orientation, expected_multiplier, expected_power = boundary_map[competitor_mask]
                require(
                    (record["threshold"], record["orientation"], record["multiplier"], record["monomial_power"])
                    == (expected_name, expected_orientation, expected_multiplier, expected_power),
                    f"{location}: wrong threshold identity metadata",
                )
                require(record["orientation"] in {"left", "right"}, f"{location}: bad orientation")
                expected_difference = poly_scale_shift(
                    threshold_polys[record["threshold"]], record["multiplier"], record["monomial_power"]
                )
                require(difference == expected_difference, f"{location}: threshold polynomial identity fails")
                required_multiplier = -1 if record["orientation"] == "left" else 1
                require(record["multiplier"] == required_multiplier,
                        f"{location}: boundary expression has wrong sign")
            else:
                total_sturm += 1
                require(competitor_mask not in boundary_map, f"{location}: boundary tie sent to Sturm")
                multiplicity, residual = strip_x_minus_one(difference) if region_id == "C3" else (0, difference)
                require(type(record["removed_x_minus_one"]) is int and record["removed_x_minus_one"] >= 0,
                        f"{location}: bad multiplicity")
                require(record["removed_x_minus_one"] == multiplicity,
                        f"{location}: x-1 multiplicity mismatch")
                encoded_residual = as_poly(record["residual_coefficients"], f"{location}.residual")
                require(residual == encoded_residual, f"{location}: residual mismatch")
                endpoint_signs = [sign(evaluate(residual, left)), sign(evaluate(residual, right))]
                require(record["residual_endpoint_signs"] == endpoint_signs,
                        f"{location}: residual endpoint signs mismatch")
                count, _, _, chain_length = sturm_root_count(residual, left, right)
                require(record["sympy_root_count"] == 0 == count,
                        f"{location}: a residual root exists")
                max_chain_length = max(max_chain_length, chain_length)
                max_degree = max(max_degree, len(residual) - 1)

        require(seen_masks == set(range(64)) - {target_mask}, f"{region_id}: incomplete comparison set")

    require(seen_region_ids == set(expected_regions), "region set incomplete")
    require(total_sturm == 185 and total_threshold == 4, "unexpected certificate case counts")

    return {
        "status": "VERIFIED",
        "task_id": certificate["task_id"],
        "cuts": 64,
        "comparisons": total_sturm + total_threshold,
        "sturm_comparisons": total_sturm,
        "threshold_identities": total_threshold,
        "maximum_sturm_chain_length": max_chain_length,
        "maximum_residual_degree": max_degree,
        "certificate_sha256": sha256(certificate_path),
        "verifier_sha256": sha256(Path(__file__)),
        "theorem_sha256": certificate["theorem_sha256"],
        "proof_assistant_used": False,
    }


def main() -> int:
    certificate_path = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else DEFAULT_CERTIFICATE
    if len(sys.argv) > 2:
        print("usage: verify_certificate.py [certificate.json]", file=sys.stderr)
        return 2
    try:
        result = verify(certificate_path)
    except VerificationError as exc:
        print(json.dumps({"status": "REJECTED", "reason": str(exc)}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
