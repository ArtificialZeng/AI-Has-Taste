#!/usr/bin/env python3
"""Mutation tests: every damaged exact certificate must be rejected."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "verification" / "verify_n9_certificate.py"
CERTIFICATE = ROOT / "certificates" / "n9_exact_frames.json"


def accepted(payload: dict | str) -> bool:
    with tempfile.TemporaryDirectory(prefix="n9-certificate-mutation-") as folder:
        path = Path(folder) / "certificate.json"
        path.write_text(
            payload if isinstance(payload, str) else json.dumps(payload),
            encoding="utf-8",
        )
        result = subprocess.run(
            [sys.executable, str(VERIFIER), str(path)],
            text=True,
            capture_output=True,
            check=False,
        )
        return result.returncode == 0


def main() -> None:
    original = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    if not accepted(original):
        raise SystemExit("the undamaged certificate was rejected")

    mutations = []

    missing_witness = copy.deepcopy(original)
    missing_witness["frame_witnesses"].pop()
    mutations.append(("missing witness", missing_witness))

    damaged_weight = copy.deepcopy(original)
    old = Fraction(damaged_weight["frame_witnesses"][0]["weights"][0])
    new = old + 1
    damaged_weight["frame_witnesses"][0]["weights"][0] = f"{new.numerator}/{new.denominator}"
    mutations.append(("damaged exact weight", damaged_weight))

    bad_count = copy.deepcopy(original)
    bad_count["expected_route_counts"]["9"]["total"] += 1
    mutations.append(("wrong enumeration count", bad_count))

    bad_graph = copy.deepcopy(original)
    bad_graph["frame_witnesses"][0]["graph6"] = "not-graph6"
    mutations.append(("malformed graph6", bad_graph))

    unknown_key = copy.deepcopy(original)
    unknown_key["unreviewed"] = True
    mutations.append(("unknown top-level key", unknown_key))

    duplicate_key = json.dumps(original)
    duplicate_key = '{"schema":"invalid",' + duplicate_key[1:]
    mutations.append(("duplicate JSON key", duplicate_key))

    nonstandard_nan = copy.deepcopy(original)
    nonstandard_nan["discovery_provenance"] = float("nan")
    mutations.append(("non-standard NaN", nonstandard_nan))

    null_provenance = copy.deepcopy(original)
    null_provenance["discovery_provenance"] = None
    mutations.append(("null provenance", null_provenance))

    float_endpoint = copy.deepcopy(original)
    float_endpoint["frame_witnesses"][0]["edge_limit"] = float(
        float_endpoint["frame_witnesses"][0]["edge_limit"]
    )
    mutations.append(("float in integer endpoint", float_endpoint))

    boolean_permutation = copy.deepcopy(original)
    permutation = boolean_permutation["frame_witnesses"][0]["orthogonality_order"]
    one_index = permutation.index(1)
    permutation[one_index] = True
    mutations.append(("boolean in integer permutation", boolean_permutation))

    null_discovery = copy.deepcopy(original)
    null_discovery["frame_witnesses"][0]["discovery_only"] = None
    mutations.append(("null witness provenance", null_discovery))

    float_count = copy.deepcopy(original)
    float_count["expected_route_counts"]["9"]["total"] = 108.0
    mutations.append(("float route count", float_count))

    float_endpoint_order = copy.deepcopy(original)
    float_endpoint_order["endpoint"]["orders_certified"][-1] = 9.0
    mutations.append(("float endpoint order", float_endpoint_order))

    extended_graph6 = copy.deepcopy(original)
    extended_graph6["frame_witnesses"][0]["graph6"] = "~??F??Gw"
    mutations.append(("noncanonical extended graph6", extended_graph6))

    padding_graph6 = copy.deepcopy(original)
    padding_graph6["frame_witnesses"][0]["graph6"] = "F??Gx"
    mutations.append(("noncanonical graph6 padding", padding_graph6))

    for bad_decimal in ("1_0", "+1", "01"):
        malformed_decimal = copy.deepcopy(original)
        malformed_decimal["frame_witnesses"][0]["discovery_only"][
            "maximum_zero_residual"
        ] = bad_decimal
        mutations.append((f"noncanonical decimal {bad_decimal}", malformed_decimal))

    failures = [name for name, payload in mutations if accepted(payload)]
    if failures:
        raise SystemExit("mutations incorrectly accepted: " + ", ".join(failures))
    print(f"PASS: valid certificate accepted; {len(mutations)} damaged certificates rejected")


if __name__ == "__main__":
    main()
