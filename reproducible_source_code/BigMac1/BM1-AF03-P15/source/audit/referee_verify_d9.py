#!/usr/bin/env python3
"""Independent exact referee verifier for the frozen D9 flow certificate.

This file intentionally imports only the Python standard library.  It does
not import the release verifier, discovery code, source code, or tests.  Its
only mathematical input is certificates/d9_normalized_flow.json.

The quotient cover graph is reconstructed directly: one canonical signed
permutation is built for each signed-cycle type and is right-multiplied by
all 72 D9 reflections.  The same enumeration is made from both ranks of each
adjacent pair, so source and target degrees are obtained independently.
"""

from __future__ import annotations

import copy
import hashlib
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import sys


N = 9
GROUP_ORDER = (2 ** (N - 1)) * math.factorial(N)
EXPECTED_CERTIFICATE_SHA256 = (
    "d8fe947906c577f3a7c585fc07e0bcb6648e2555056a756af98bf307ab72ea7f"
)
ENDPOINT = "Abs(D_9) admits a normalized flow with unit vertex weights"
ROOT = Path(__file__).resolve().parent.parent
CERTIFICATE_PATH = ROOT / "certificates" / "d9_normalized_flow.json"


class AuditError(ValueError):
    """A fail-closed certificate or mathematical-consistency error."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AuditError(message)


def exact_keys(value: object, expected: set[str], where: str) -> dict[str, object]:
    require(type(value) is dict, f"{where}: expected object")
    obj = value
    actual = set(obj)
    require(actual == expected, f"{where}: keys {sorted(actual)} != {sorted(expected)}")
    return obj


def integer(value: object, where: str) -> int:
    require(type(value) is int, f"{where}: expected JSON integer")
    return value


def duplicate_rejecting_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    obj: dict[str, object] = {}
    for key, value in pairs:
        if key in obj:
            raise AuditError(f"duplicate JSON key: {key!r}")
        obj[key] = value
    return obj


def reject_float(token: str) -> object:
    raise AuditError(f"floating-point JSON number is forbidden: {token}")


def reject_constant(token: str) -> object:
    raise AuditError(f"non-finite JSON constant is forbidden: {token}")


def parse_json(raw: bytes) -> dict[str, object]:
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise AuditError("certificate is not UTF-8") from exc
    try:
        value = json.loads(
            text,
            object_pairs_hook=duplicate_rejecting_object,
            parse_float=reject_float,
            parse_constant=reject_constant,
        )
    except (json.JSONDecodeError, AuditError) as exc:
        raise AuditError(f"invalid strict JSON: {exc}") from exc
    require(type(value) is dict, "certificate root must be an object")
    return value


def require_primary_hash(raw: bytes) -> str:
    digest = hashlib.sha256(raw).hexdigest()
    require(
        digest == EXPECTED_CERTIFICATE_SHA256,
        f"primary certificate SHA-256 mismatch: {digest}",
    )
    return digest


def partitions(total: int, ceiling: int | None = None):
    """Generate integer partitions as nonincreasing tuples."""
    if total == 0:
        yield ()
        return
    if ceiling is None or ceiling > total:
        ceiling = total
    for first in range(ceiling, 0, -1):
        for rest in partitions(total - first, first):
            yield (first,) + rest


def all_types() -> list[tuple[tuple[int, ...], tuple[int, ...]]]:
    result = []
    for positive_sum in range(N + 1):
        for positive in partitions(positive_sum):
            for negative in partitions(N - positive_sum):
                if len(negative) % 2 == 0:
                    result.append((positive, negative))
    return result


def encode_partition(partition: tuple[int, ...]) -> str:
    return ",".join(str(part) for part in partition) if partition else "-"


def encode_type(cycle_type: tuple[tuple[int, ...], tuple[int, ...]]) -> str:
    positive, negative = cycle_type
    return f"{encode_partition(positive)}|{encode_partition(negative)}"


def z_value(partition: tuple[int, ...]) -> int:
    multiplicities: dict[int, int] = defaultdict(int)
    for part in partition:
        multiplicities[part] += 1
    value = 1
    for part, multiplicity in multiplicities.items():
        value *= (part ** multiplicity) * math.factorial(multiplicity)
    return value


def orbit_size(cycle_type: tuple[tuple[int, ...], tuple[int, ...]]) -> int:
    positive, negative = cycle_type
    centralizer = (
        (2 ** (len(positive) + len(negative)))
        * z_value(positive)
        * z_value(negative)
    )
    b9_order = (2 ** N) * math.factorial(N)
    require(b9_order % centralizer == 0, f"nonintegral orbit for {cycle_type}")
    return b9_order // centralizer


def rank_of(cycle_type: tuple[tuple[int, ...], tuple[int, ...]]) -> int:
    return N - len(cycle_type[0])


def canonical_signed_permutation(
    cycle_type: tuple[tuple[int, ...], tuple[int, ...]],
) -> tuple[int, ...]:
    """Return window notation for a canonical representative of a type."""
    window = [0] * N
    next_letter = 1
    for sign, partition in ((1, cycle_type[0]), (-1, cycle_type[1])):
        for length in partition:
            support = list(range(next_letter, next_letter + length))
            for left, right in zip(support, support[1:]):
                window[left - 1] = right
            window[support[-1] - 1] = sign * support[0]
            next_letter += length
    require(next_letter == N + 1, f"representative does not use {N} letters")
    require(
        sum(entry < 0 for entry in window) % 2 == 0,
        "canonical representative is not in D9",
    )
    return tuple(window)


def apply_signed(window: tuple[int, ...], letter: int) -> int:
    if letter > 0:
        return window[letter - 1]
    return -window[-letter - 1]


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    """Composition left after right; hence w*t is compose(w, t)."""
    return tuple(apply_signed(left, entry) for entry in right)


def signed_cycle_type(
    window: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    require(len(window) == N, "signed permutation has wrong degree")
    require(sorted(abs(entry) for entry in window) == list(range(1, N + 1)),
            "window is not a signed permutation")
    seen: set[int] = set()
    positive: list[int] = []
    negative: list[int] = []
    for start in range(1, N + 1):
        if start in seen:
            continue
        current = start
        length = 0
        sign_product = 1
        while current not in seen:
            seen.add(current)
            image = window[current - 1]
            sign_product *= 1 if image > 0 else -1
            current = abs(image)
            length += 1
        require(current == start, "underlying permutation cycle failed to close")
        (positive if sign_product == 1 else negative).append(length)
    positive.sort(reverse=True)
    negative.sort(reverse=True)
    return tuple(positive), tuple(negative)


def reflections() -> list[tuple[int, ...]]:
    result = []
    identity = list(range(1, N + 1))
    for left in range(1, N + 1):
        for right in range(left + 1, N + 1):
            for sign in (1, -1):
                reflection = identity.copy()
                reflection[left - 1] = sign * right
                reflection[right - 1] = sign * left
                require(
                    sum(entry < 0 for entry in reflection) % 2 == 0,
                    "constructed reflection is not in D9",
                )
                result.append(tuple(reflection))
    require(len(result) == N * (N - 1), "wrong D9 reflection count")
    require(len(set(result)) == len(result), "duplicate D9 reflection")
    return result


def reconstruct() -> dict[str, object]:
    cycle_types = all_types()
    require(len(cycle_types) == 150, "wrong signed-cycle-type count")
    require(len(set(cycle_types)) == len(cycle_types), "duplicate cycle type")

    enc_to_type = {encode_type(item): item for item in cycle_types}
    require(len(enc_to_type) == len(cycle_types), "nonunique type encoding")
    masses = {encode_type(item): orbit_size(item) for item in cycle_types}
    ranks = {encode_type(item): rank_of(item) for item in cycle_types}

    types_by_rank: list[list[str]] = [[] for _ in range(N + 1)]
    for encoded in enc_to_type:
        types_by_rank[ranks[encoded]].append(encoded)
    for layer in types_by_rank:
        layer.sort()
    rank_sizes = [sum(masses[item] for item in layer) for layer in types_by_rank]
    rank_orbit_counts = [len(layer) for layer in types_by_rank]
    require(sum(rank_sizes) == GROUP_ORDER, "orbit masses do not conserve D9 order")

    all_reflections = reflections()
    upward: dict[tuple[str, str], int] = defaultdict(int)
    downward: dict[tuple[str, str], int] = defaultdict(int)
    for encoded, cycle_type in enc_to_type.items():
        representative = canonical_signed_permutation(cycle_type)
        require(
            signed_cycle_type(representative) == cycle_type,
            f"canonical representative has wrong type: {encoded}",
        )
        current_rank = ranks[encoded]
        up_count = 0
        down_count = 0
        for reflection in all_reflections:
            neighbor_type = signed_cycle_type(compose(representative, reflection))
            neighbor = encode_type(neighbor_type)
            require(neighbor in enc_to_type, f"reflection leaves D9 types: {neighbor}")
            difference = ranks[neighbor] - current_rank
            require(abs(difference) == 1, f"reflection rank jump {difference}")
            if difference == 1:
                upward[(encoded, neighbor)] += 1
                up_count += 1
            else:
                downward[(neighbor, encoded)] += 1
                down_count += 1
        require(up_count + down_count == len(all_reflections),
                f"reflection conservation failed at {encoded}")

    require(set(upward) == set(downward), "up/down quotient supports disagree")
    edge_counts: dict[tuple[str, str], int] = {}
    for edge, degree_from in upward.items():
        lower, upper = edge
        degree_to = downward[edge]
        from_count = masses[lower] * degree_from
        to_count = masses[upper] * degree_to
        require(from_count == to_count, f"biregularity count fails on {edge}")
        require(from_count > 0, f"empty reconstructed support {edge}")
        edge_counts[edge] = from_count

    allowed_by_layer = [0] * N
    covers_by_layer = [0] * N
    for (lower, upper), edge_count in edge_counts.items():
        rank = ranks[lower]
        require(ranks[upper] == rank + 1, "support is not rank-adjacent")
        allowed_by_layer[rank] += 1
        covers_by_layer[rank] += edge_count

    return {
        "cycle_types": cycle_types,
        "enc_to_type": enc_to_type,
        "masses": masses,
        "ranks": ranks,
        "types_by_rank": types_by_rank,
        "rank_sizes": rank_sizes,
        "rank_orbit_counts": rank_orbit_counts,
        "upward": upward,
        "downward": downward,
        "edge_counts": edge_counts,
        "allowed_by_layer": allowed_by_layer,
        "covers_by_layer": covers_by_layer,
    }


TOP_KEYS = {
    "claim",
    "environment",
    "failure_cut",
    "layers",
    "n",
    "orbit_count",
    "orbit_encoding",
    "quotient_action",
    "rank_orbit_counts",
    "rank_sizes",
    "schema_version",
    "status",
}
ENVIRONMENT_KEYS = {"algorithm", "platform", "python"}
LAYER_KEYS = {"flows", "rank"}
FLOW_KEYS = {
    "degree_from",
    "degree_to",
    "denominator",
    "edge_count",
    "edge_denominator",
    "edge_numerator",
    "from",
    "numerator",
    "to",
}


def canonical_positive_fraction(numerator: object, denominator: object, where: str) -> Fraction:
    top = integer(numerator, f"{where}.numerator")
    bottom = integer(denominator, f"{where}.denominator")
    require(top > 0, f"{where}: only positive serialized flows are allowed")
    require(bottom > 0, f"{where}: denominator must be positive")
    require(math.gcd(top, bottom) == 1, f"{where}: rational is not canonical")
    return Fraction(top, bottom)


def integer_list(value: object, length: int, where: str) -> list[int]:
    require(type(value) is list, f"{where}: expected list")
    require(len(value) == length, f"{where}: wrong length")
    return [integer(entry, f"{where}[{index}]") for index, entry in enumerate(value)]


def verify_document(document: dict[str, object], model: dict[str, object]) -> dict[str, object]:
    top = exact_keys(document, TOP_KEYS, "certificate")
    require(top["claim"] == ENDPOINT, "wrong endpoint claim")
    require(integer(top["n"], "n") == N, "wrong n")
    require(integer(top["schema_version"], "schema_version") == 1, "wrong schema")
    require(top["status"] == "feasible", "certificate does not claim feasibility")
    require(top["failure_cut"] is None, "failure_cut must be null")
    require(top["orbit_encoding"] ==
            "positive_partition|negative_partition; negative partition has even length",
            "wrong orbit encoding declaration")
    require(top["quotient_action"] == "conjugation by B_9 on D_9",
            "wrong quotient action declaration")
    environment = exact_keys(top["environment"], ENVIRONMENT_KEYS, "environment")
    for key in ENVIRONMENT_KEYS:
        require(type(environment[key]) is str and environment[key],
                f"environment.{key}: expected nonempty string")

    masses = model["masses"]
    ranks = model["ranks"]
    types_by_rank = model["types_by_rank"]
    rank_sizes = model["rank_sizes"]
    rank_orbit_counts = model["rank_orbit_counts"]
    upward = model["upward"]
    downward = model["downward"]
    edge_counts = model["edge_counts"]

    require(integer(top["orbit_count"], "orbit_count") == len(masses),
            "wrong orbit_count")
    claimed_counts = integer_list(top["rank_orbit_counts"], N + 1, "rank_orbit_counts")
    claimed_sizes = integer_list(top["rank_sizes"], N + 1, "rank_sizes")
    require(claimed_counts == rank_orbit_counts, "altered rank orbit counts")
    require(claimed_sizes == rank_sizes, "altered rank sizes")
    require(sum(claimed_sizes) == GROUP_ORDER, "claimed ranks do not conserve group order")

    layers = top["layers"]
    require(type(layers) is list, "layers: expected list")
    require(len(layers) == N, "missing or extra adjacent-rank layer")

    positive_by_layer: list[int] = []
    total_positive = 0
    for expected_rank, layer_value in enumerate(layers):
        layer = exact_keys(layer_value, LAYER_KEYS, f"layers[{expected_rank}]")
        rank = integer(layer["rank"], f"layers[{expected_rank}].rank")
        require(rank == expected_rank, f"missing, duplicate, or reordered layer {expected_rank}")
        flows = layer["flows"]
        require(type(flows) is list, f"layers[{rank}].flows: expected list")
        seen_edges: set[tuple[str, str]] = set()
        row: dict[str, Fraction] = defaultdict(Fraction)
        column: dict[str, Fraction] = defaultdict(Fraction)
        lifted_row: dict[str, Fraction] = defaultdict(Fraction)
        lifted_column: dict[str, Fraction] = defaultdict(Fraction)
        cleared_row: dict[str, int] = defaultdict(int)
        cleared_column: dict[str, int] = defaultdict(int)
        scale = math.lcm(rank_sizes[rank], rank_sizes[rank + 1])

        for index, flow_value in enumerate(flows):
            where = f"layers[{rank}].flows[{index}]"
            flow = exact_keys(flow_value, FLOW_KEYS, where)
            lower = flow["from"]
            upper = flow["to"]
            require(type(lower) is str and lower in masses, f"{where}: wrong from endpoint")
            require(type(upper) is str and upper in masses, f"{where}: wrong to endpoint")
            require(ranks[lower] == rank, f"{where}: from endpoint has wrong rank")
            require(ranks[upper] == rank + 1, f"{where}: to endpoint has wrong rank")
            edge = (lower, upper)
            require(edge not in seen_edges, f"{where}: duplicate orbit-pair flow")
            seen_edges.add(edge)
            require(edge in upward, f"{where}: endpoint pair is not an upward cover support")

            amount = canonical_positive_fraction(
                flow["numerator"], flow["denominator"], where,
            )
            per_edge = canonical_positive_fraction(
                flow["edge_numerator"], flow["edge_denominator"], f"{where}.edge",
            )
            degree_from = integer(flow["degree_from"], f"{where}.degree_from")
            degree_to = integer(flow["degree_to"], f"{where}.degree_to")
            edge_count = integer(flow["edge_count"], f"{where}.edge_count")
            require(degree_from == upward[edge], f"{where}: wrong source multiplicity")
            require(degree_to == downward[edge], f"{where}: wrong target multiplicity")
            require(edge_count == edge_counts[edge], f"{where}: wrong full edge count")
            require(edge_count == masses[lower] * degree_from,
                    f"{where}: source edge conservation failed")
            require(edge_count == masses[upper] * degree_to,
                    f"{where}: target edge conservation failed")
            require(per_edge == amount / edge_count, f"{where}: wrong F/E lift")

            cleared = amount * scale
            require(cleared.denominator == 1, f"{where}: flow is not integral at LCM scale")
            cleared_value = cleared.numerator
            require(cleared_value > 0, f"{where}: cleared flow is not positive")

            row[lower] += amount
            column[upper] += amount
            cleared_row[lower] += cleared_value
            cleared_column[upper] += cleared_value
            lifted_row[lower] += degree_from * per_edge
            lifted_column[upper] += degree_to * per_edge

        for lower in types_by_rank[rank]:
            expected = Fraction(masses[lower], rank_sizes[rank])
            require(row[lower] == expected, f"layer {rank}: wrong row marginal at {lower}")
            require(cleared_row[lower] == (scale * masses[lower]) // rank_sizes[rank],
                    f"layer {rank}: wrong cleared row at {lower}")
            require(lifted_row[lower] == Fraction(1, rank_sizes[rank]),
                    f"layer {rank}: wrong lifted vertex row at {lower}")
        for upper in types_by_rank[rank + 1]:
            expected = Fraction(masses[upper], rank_sizes[rank + 1])
            require(column[upper] == expected,
                    f"layer {rank}: wrong column marginal at {upper}")
            require(cleared_column[upper] == (scale * masses[upper]) // rank_sizes[rank + 1],
                    f"layer {rank}: wrong cleared column at {upper}")
            require(lifted_column[upper] == Fraction(1, rank_sizes[rank + 1]),
                    f"layer {rank}: wrong lifted vertex column at {upper}")
        require(sum(row.values(), Fraction()) == 1, f"layer {rank}: row mass not one")
        require(sum(column.values(), Fraction()) == 1, f"layer {rank}: column mass not one")
        require(sum(cleared_row.values()) == scale,
                f"layer {rank}: cleared integer mass does not equal LCM")

        positive_by_layer.append(len(flows))
        total_positive += len(flows)

    return {
        "positive_by_layer": positive_by_layer,
        "total_positive": total_positive,
    }


def expect_rejected(name: str, operation) -> str:
    try:
        operation()
    except AuditError:
        return "REJECTED"
    raise AuditError(f"mutation unexpectedly accepted: {name}")


def mutation_suite(
    raw: bytes, document: dict[str, object], model: dict[str, object]
) -> dict[str, str]:
    results: dict[str, str] = {}
    results["hash_mismatch"] = expect_rejected(
        "hash_mismatch", lambda: require_primary_hash(raw + b"\n")
    )

    def changed(mutator):
        altered = copy.deepcopy(document)
        mutator(altered)
        verify_document(altered, model)

    results["missing_layer"] = expect_rejected(
        "missing_layer", lambda: changed(lambda doc: doc["layers"].pop())
    )
    results["missing_flow"] = expect_rejected(
        "missing_flow", lambda: changed(lambda doc: doc["layers"][0]["flows"].pop())
    )

    wrong_rank_endpoint = model["types_by_rank"][2][0]
    results["wrong_orbit_endpoint"] = expect_rejected(
        "wrong_orbit_endpoint",
        lambda: changed(
            lambda doc: doc["layers"][0]["flows"][0].__setitem__(
                "from", wrong_rank_endpoint
            )
        ),
    )
    results["wrong_multiplicity"] = expect_rejected(
        "wrong_multiplicity",
        lambda: changed(
            lambda doc: doc["layers"][0]["flows"][0].__setitem__(
                "degree_from", doc["layers"][0]["flows"][0]["degree_from"] + 1
            )
        ),
    )
    results["wrong_edge_count"] = expect_rejected(
        "wrong_edge_count",
        lambda: changed(
            lambda doc: doc["layers"][0]["flows"][0].__setitem__(
                "edge_count", doc["layers"][0]["flows"][0]["edge_count"] + 1
            )
        ),
    )
    results["negative_rational"] = expect_rejected(
        "negative_rational",
        lambda: changed(
            lambda doc: doc["layers"][0]["flows"][0].__setitem__("numerator", -1)
        ),
    )

    def make_noncanonical(doc):
        flow = doc["layers"][0]["flows"][0]
        flow["numerator"] *= 2
        flow["denominator"] *= 2

    results["noncanonical_rational"] = expect_rejected(
        "noncanonical_rational", lambda: changed(make_noncanonical)
    )
    results["altered_rank_size"] = expect_rejected(
        "altered_rank_size",
        lambda: changed(
            lambda doc: doc["rank_sizes"].__setitem__(4, doc["rank_sizes"][4] + 1)
        ),
    )
    return results


def main() -> int:
    try:
        raw = CERTIFICATE_PATH.read_bytes()
        input_hash = require_primary_hash(raw)
        document = parse_json(raw)
        model = reconstruct()
        certificate_summary = verify_document(document, model)
        mutations = mutation_suite(raw, document, model)
        verifier_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        rank_sizes = model["rank_sizes"]
        summary = {
            "status": "VERIFIED",
            "endpoint": ENDPOINT,
            "input_sha256": input_hash,
            "verifier_sha256": verifier_hash,
            "n": N,
            "group_order": GROUP_ORDER,
            "reflections": N * (N - 1),
            "orbits": len(model["cycle_types"]),
            "rank_orbit_counts": model["rank_orbit_counts"],
            "rank_sizes": rank_sizes,
            "rank_symmetric": rank_sizes == list(reversed(rank_sizes)),
            "allowed_orbit_pairs": len(model["edge_counts"]),
            "allowed_pairs_by_layer": model["allowed_by_layer"],
            "positive_orbit_flows": certificate_summary["total_positive"],
            "positive_flows_by_layer": certificate_summary["positive_by_layer"],
            "integer_scales_by_layer": [
                math.lcm(rank_sizes[rank], rank_sizes[rank + 1])
                for rank in range(N)
            ],
            "full_hasse_covers": sum(model["edge_counts"].values()),
            "full_hasse_covers_by_layer": model["covers_by_layer"],
            "mutation_tests": mutations,
        }
        print(json.dumps(summary, sort_keys=True, separators=(",", ":")))
        return 0
    except (AuditError, OSError) as exc:
        print(f"REFEREE VERIFICATION FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
