#!/usr/bin/env python3
"""Fail-closed verifier for a complete 162-branch multiplier cover."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from collections import Counter
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "code"))

from verify_fixed_clique_certificate import rerun as rerun_fixed  # noqa: E402
from verify_fixed_clique_certificate import validate  # noqa: E402

V = 31


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_int(value: object, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")
    return value


def translate(block: tuple[int, ...], shift: int) -> tuple[int, ...]:
    return tuple(sorted((point + shift) % V for point in block))


def canonical(block: tuple[int, ...]) -> tuple[int, ...]:
    return min(translate(block, shift) for shift in range(V))


def reconstruct_instance(instance: object) -> list[object]:
    """Rebuild the proof-relevant finite instance from the definitions."""
    if not isinstance(instance, dict) or set(instance) != {
        "baseline_blocks", "columns", "counts", "schema", "triple_orbits", "v"
    }:
        raise ValueError("instance fields do not match the strict schema")
    if instance["schema"] != "cyclic-315-set-packing-v1" or instance["v"] != V:
        raise ValueError("unsupported exact instance header")

    triple_orbits = sorted({canonical(triple) for triple in combinations(range(V), 3)})
    if len(triple_orbits) != 145:
        raise ValueError("definition-level triple-orbit count is not 145")
    serialized_triples = instance["triple_orbits"]
    if serialized_triples != [list(triple) for triple in triple_orbits]:
        raise ValueError("serialized triple resources differ from the definition-level rebuild")
    triple_id = {triple: index for index, triple in enumerate(triple_orbits)}

    block_orbits = sorted({canonical(block) for block in combinations(range(V), 5)})
    if len(block_orbits) != 5481:
        raise ValueError("definition-level block-orbit count is not 5481")
    expected_columns: list[dict[str, object]] = []
    for block in block_orbits:
        resources = sorted(
            triple_id[canonical(triple)] for triple in combinations(block, 3)
        )
        if len(set(resources)) == 10:
            expected_columns.append({"block": list(block), "resources": resources})
    if len(expected_columns) != 4761:
        raise ValueError("definition-level valid-column count is not 4761")
    if instance["columns"] != expected_columns:
        raise ValueError("serialized columns differ from the definition-level rebuild")

    expected_counts = {
        "all_block_orbits": 5481,
        "all_triples": 4495,
        "developed_blocks": 279,
        "developed_triples": 2790,
        "internally_valid_block_orbits": 4761,
        "pair_incidence_developed_upper": 418,
        "pair_incidence_orbit_upper": 13,
        "triple_orbits": 145,
    }
    if instance["counts"] != expected_counts:
        raise ValueError("serialized instance counts are incorrect")
    return expected_columns


def reconstruct_orbits(columns: list[object]) -> dict[int, set[int]]:
    if len(columns) != 4761:
        raise ValueError("instance does not contain exactly 4761 columns")
    blocks = [tuple(column["block"]) for column in columns]
    if blocks != sorted(blocks) or len(set(blocks)) != 4761:
        raise ValueError("instance blocks are not a unique sorted canonical list")
    if any(canonical(block) != block for block in blocks):
        raise ValueError("instance contains a noncanonical translation representative")
    index = {block: variable for variable, block in enumerate(blocks, start=1)}
    unseen = set(index.values())
    result: dict[int, set[int]] = {}
    while unseen:
        representative = min(unseen)
        block = blocks[representative - 1]
        orbit = {
            index[canonical(tuple((unit * point) % V for point in block))]
            for unit in range(1, V)
        }
        if representative != min(orbit) or not orbit <= unseen:
            raise ValueError("multiplier orbits do not form a canonical partition")
        result[representative] = orbit
        unseen -= orbit
    return result


def verify(path: Path, rerun: bool, executable: Path | None = None) -> dict[str, int | str]:
    manifest = json.loads(path.read_text())
    required = {
        "schema", "target", "claim", "instance", "symmetry", "enumeration",
        "branches", "status"
    }
    if not isinstance(manifest, dict) or set(manifest) != required:
        raise ValueError("global manifest fields do not match the strict schema")
    if (manifest["schema"] != "cyclic-315-global-fixed-cover-v1"
            or manifest["target"] != 13
            or manifest["status"] != "CERTIFIED_GLOBAL_TARGET13_UNSAT"):
        raise ValueError("unsupported global manifest header")
    instance_entry = manifest["instance"]
    if set(instance_entry) != {"path", "sha256"}:
        raise ValueError("invalid instance entry")
    instance_path = ROOT / instance_entry["path"]
    if sha256(instance_path) != instance_entry["sha256"]:
        raise ValueError("instance hash mismatch")
    instance = json.loads(instance_path.read_text())
    rebuilt_columns = reconstruct_instance(instance)
    expected_orbits = reconstruct_orbits(rebuilt_columns)
    expected_distribution = Counter(map(len, expected_orbits.values()))
    if len(expected_orbits) != 162 or expected_distribution != Counter({30: 156, 15: 5, 6: 1}):
        raise ValueError("independently reconstructed symmetry quotient is unexpected")

    symmetry = manifest["symmetry"]
    if set(symmetry) != {
        "action", "orbit_count", "orbit_size_distribution", "covered_block_variables"
    }:
        raise ValueError("invalid symmetry entry")
    if (require_int(symmetry["orbit_count"], "orbit_count") != 162
            or require_int(symmetry["covered_block_variables"], "covered variables") != 4761
            or symmetry["orbit_size_distribution"] != {"6": 1, "15": 5, "30": 156}
            or symmetry["action"] != (
                "multiplication by every unit of Z_31 after translation canonicalization"
            )):
        raise ValueError("serialized symmetry totals are incorrect")
    if manifest["claim"] != (
        "Every target-13 packing is excluded by one certified multiplier block-orbit branch"
    ):
        raise ValueError("serialized global claim is incorrect")

    branches = manifest["branches"]
    if not isinstance(branches, list) or len(branches) != 162:
        raise ValueError("global manifest must contain exactly 162 branches")
    seen_representatives: set[int] = set()
    covered: set[int] = set()
    node_counts: list[int] = []
    source_hashes: set[str] = set()
    binary_hashes: set[str] = set()
    for entry in branches:
        if not isinstance(entry, dict) or set(entry) != {"fixed_variable", "path", "sha256"}:
            raise ValueError("invalid branch entry")
        variable = require_int(entry["fixed_variable"], "branch fixed variable")
        if variable in seen_representatives or variable not in expected_orbits:
            raise ValueError("duplicate or noncanonical branch representative")
        expected_path = f"certificates/negative/fixed{variable}_finite_manifest.json"
        if entry["path"] != expected_path:
            raise ValueError("branch manifest path does not match its variable")
        branch_path = ROOT / entry["path"]
        if sha256(branch_path) != entry["sha256"]:
            raise ValueError("branch manifest hash mismatch")
        branch = validate(branch_path)
        if (branch["fixed_variable"] != variable
                or set(branch["multiplier_orbit_variables"]) != expected_orbits[variable]):
            raise ValueError("branch certificate does not cover the reconstructed orbit")
        if covered & expected_orbits[variable]:
            raise ValueError("branch multiplier orbits overlap")
        covered |= expected_orbits[variable]
        seen_representatives.add(variable)
        node_counts.append(branch["enumeration"]["nodes"])
        source_hashes.add(branch["verifier"]["source_sha256"])
        binary_hashes.add(branch["verifier"]["binary_sha256"])
        if rerun:
            try:
                rerun_fixed(branch, executable)
            except (OSError, ValueError, json.JSONDecodeError) as exc:
                raise ValueError(
                    f"full replay failed for fixed variable {variable}: {exc}"
                ) from exc
    if seen_representatives != set(expected_orbits) or covered != set(range(1, 4762)):
        raise ValueError("branch manifests do not cover all 4761 block variables")
    enumeration = manifest["enumeration"]
    if not isinstance(enumeration, dict) or set(enumeration) != {
        "neighbor_target", "total_branching_nodes", "minimum_branching_nodes",
        "maximum_branching_nodes", "source_sha256", "binary_sha256"
    }:
        raise ValueError("invalid global enumeration entry")
    if (require_int(enumeration["neighbor_target"], "neighbor target") != 12
            or require_int(enumeration["total_branching_nodes"], "total nodes")
            != sum(node_counts)
            or require_int(enumeration["minimum_branching_nodes"], "minimum nodes")
            != min(node_counts)
            or require_int(enumeration["maximum_branching_nodes"], "maximum nodes")
            != max(node_counts)
            or source_hashes != {enumeration["source_sha256"]}
            or binary_hashes != {enumeration["binary_sha256"]}):
        raise ValueError("global enumeration aggregates do not match the branches")
    return {
        "status": "VERIFIED_GLOBAL_TARGET13_UNSAT",
        "branches": len(branches),
        "covered_block_variables": len(covered),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        type=Path,
        default=ROOT / "certificates/negative/target13_global_fixed_cover_manifest.json",
    )
    parser.add_argument("--rerun", action="store_true")
    parser.add_argument(
        "--rebuild-rerun",
        action="store_true",
        help="compile the locked definition-level source once and replay all 162 branches",
    )
    parser.add_argument("--cxx", default="c++", help="compiler used by --rebuild-rerun")
    args = parser.parse_args()
    try:
        if args.rerun and args.rebuild_rerun:
            raise ValueError("choose at most one full-replay mode")
        if args.rebuild_rerun:
            source = ROOT / "code/exact_clique.cpp"
            with tempfile.TemporaryDirectory(prefix="cyclic315-global-clique-build-") as directory:
                executable = Path(directory) / "exact_clique_rebuilt"
                process = subprocess.run(
                    [args.cxx, "-std=c++20", "-O3", str(source), "-o", str(executable)],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                if process.returncode != 0:
                    raise ValueError("clean verifier rebuild failed: " + process.stderr)
                result = verify(args.manifest, True, executable)
        else:
            result = verify(args.manifest, args.rerun)
    except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "REJECTED", "reason": str(exc)}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
