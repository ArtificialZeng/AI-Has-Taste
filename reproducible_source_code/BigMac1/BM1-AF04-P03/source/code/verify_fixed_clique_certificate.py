#!/usr/bin/env python3
"""Fail-closed wrapper for the independent fixed-block exact enumeration."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(block: tuple[int, ...]) -> tuple[int, ...]:
    return min(tuple(sorted((point + shift) % 31 for point in block)) for shift in range(31))


def require_int(value: object, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")
    return value


def validate(manifest_path: Path) -> dict[str, object]:
    manifest = json.loads(manifest_path.read_text())
    required = {
        "schema", "scope", "target", "fixed_variable", "fixed_block",
        "multiplier_orbit_variables", "instance", "graph", "enumeration",
        "verifier", "status",
    }
    if set(manifest) != required:
        raise ValueError("manifest fields do not match the strict schema")
    if manifest["schema"] != "cyclic-315-fixed-clique-enumeration-v1":
        raise ValueError("unsupported manifest schema")
    if manifest["status"] != "CERTIFIED_FIXED_BRANCH_UNSAT" or manifest["target"] != 13:
        raise ValueError("unexpected scope or status")
    fixed_variable = require_int(manifest["fixed_variable"], "fixed_variable")
    if not 1 <= fixed_variable <= 4761:
        raise ValueError("fixed variable is outside the exact column range")

    instance_entry = manifest["instance"]
    if set(instance_entry) != {"path", "sha256"}:
        raise ValueError("invalid instance entry")
    instance_path = ROOT / instance_entry["path"]
    if sha256(instance_path) != instance_entry["sha256"]:
        raise ValueError("instance hash mismatch")
    instance = json.loads(instance_path.read_text())
    columns = instance["columns"]
    block = columns[fixed_variable - 1]["block"]
    if block != manifest["fixed_block"]:
        raise ValueError("fixed block does not match the exact instance")

    block_to_variable = {
        tuple(column["block"]): variable
        for variable, column in enumerate(columns, start=1)
    }
    block_tuple = tuple(block)
    orbit = sorted({
        block_to_variable[canonical(tuple((unit * point) % 31 for point in block_tuple))]
        for unit in range(1, 31)
    })
    if orbit != manifest["multiplier_orbit_variables"] or len(orbit) not in {6, 15, 30}:
        raise ValueError("multiplier orbit mismatch")
    current_scope = (
        f"Only target-13 packings containing block variable {fixed_variable} or one of the "
        f"{len(orbit)} distinct variables in its multiplier orbit; this is not a global proof "
        "that M < 13"
    )
    legacy_scope = (
        f"Only target-13 packings containing block variable {fixed_variable} or one of its "
        f"{len(orbit)} multiplier images; this is not a global proof that M < 13"
    )
    if manifest["scope"] not in {current_scope, legacy_scope}:
        raise ValueError("fixed-branch scope text does not match its exact orbit")

    graph = manifest["graph"]
    if set(graph) != {"path", "sha256", "vertices", "edges"}:
        raise ValueError("invalid graph entry")
    graph_path = ROOT / graph["path"]
    if sha256(graph_path) != graph["sha256"]:
        raise ValueError("graph hash mismatch")
    graph_vertices = require_int(graph["vertices"], "graph vertices")
    graph_edges = require_int(graph["edges"], "graph edges")
    if graph_vertices < 12 or graph_edges < 0:
        raise ValueError("invalid fixed-neighborhood dimensions")
    header = graph_path.open(encoding="ascii").readline().split()
    if header != ["p", "edge", str(graph_vertices), str(graph_edges)]:
        raise ValueError("graph header does not match the manifest")

    enumeration = manifest["enumeration"]
    if set(enumeration) != {"path", "sha256", "neighbor_target", "nodes"}:
        raise ValueError("invalid enumeration entry")
    result_path = ROOT / enumeration["path"]
    if sha256(result_path) != enumeration["sha256"]:
        raise ValueError("enumeration result hash mismatch")
    result_lines = result_path.read_text().splitlines()
    if len(result_lines) != 1:
        raise ValueError("enumeration result must contain exactly one record")
    result = json.loads(result_lines[0])
    if (result.get("status") != "UNSAT_BY_COMPLETE_BRANCHING"
            or require_int(result.get("fixed_variable"), "result fixed variable") != fixed_variable
            or require_int(result.get("neighbor_vertices"), "neighbor vertices") != graph_vertices
            or require_int(result.get("nodes"), "nodes") != enumeration["nodes"]
            or enumeration["neighbor_target"] != 12):
        raise ValueError("enumeration record mismatch")

    verifier = manifest["verifier"]
    if set(verifier) != {"source_path", "source_sha256", "binary_path", "binary_sha256"}:
        raise ValueError("invalid verifier entry")
    if sha256(ROOT / verifier["source_path"]) != verifier["source_sha256"]:
        raise ValueError("verifier source hash mismatch")
    binary_path = ROOT / verifier["binary_path"]
    if sha256(binary_path) != verifier["binary_sha256"]:
        raise ValueError("verifier binary hash mismatch")
    return manifest


def rerun(manifest: dict[str, object], executable: Path | None = None) -> None:
    verifier = manifest["verifier"]
    if executable is None:
        executable = ROOT / verifier["binary_path"]
    expected_nodes = manifest["enumeration"]["nodes"]
    expected_vertices = manifest["graph"]["vertices"]
    fixed_variable = manifest["fixed_variable"]
    with tempfile.TemporaryDirectory(prefix="cyclic315-fixed-clique-") as directory:
        temporary = Path(directory)
        result_path = temporary / "result.jsonl"
        witness_path = temporary / "witness.json"
        process = subprocess.run(
            [str(executable), str(result_path), str(witness_path), str(fixed_variable)],
            capture_output=True,
            text=True,
            check=False,
        )
        if process.returncode != 20 or witness_path.exists():
            raise ValueError("independent exact verifier did not return UNSAT")
        lines = result_path.read_text().splitlines()
        if len(lines) != 1:
            raise ValueError("rerun emitted an invalid result record")
        result = json.loads(lines[0])
        if (result.get("status") != "UNSAT_BY_COMPLETE_BRANCHING"
                or result.get("fixed_variable") != fixed_variable
                or result.get("neighbor_vertices") != expected_vertices
                or result.get("nodes") != expected_nodes):
            raise ValueError("rerun is not deterministic or does not match the certificate")


def rebuild_and_rerun(manifest: dict[str, object], compiler: str) -> None:
    source = ROOT / manifest["verifier"]["source_path"]
    with tempfile.TemporaryDirectory(prefix="cyclic315-fixed-clique-build-") as directory:
        executable = Path(directory) / "exact_clique_rebuilt"
        process = subprocess.run(
            [compiler, "-std=c++20", "-O3", str(source), "-o", str(executable)],
            capture_output=True,
            text=True,
            check=False,
        )
        if process.returncode != 0:
            raise ValueError("clean verifier rebuild failed: " + process.stderr)
        rerun(manifest, executable)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        type=Path,
        default=ROOT / "certificates/negative/fixed390_finite_manifest.json",
    )
    parser.add_argument("--rerun", action="store_true", help="repeat the full exact search")
    parser.add_argument(
        "--rebuild-rerun",
        action="store_true",
        help="compile the locked source in a temporary directory and repeat the full exact search",
    )
    parser.add_argument("--cxx", default="c++", help="compiler used by --rebuild-rerun")
    args = parser.parse_args()
    manifest = validate(args.manifest)
    if args.rerun:
        rerun(manifest)
    if args.rebuild_rerun:
        rebuild_and_rerun(manifest, args.cxx)
    print(f"fixed-variable-{manifest['fixed_variable']} exact enumeration certificate: VERIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
