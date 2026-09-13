#!/usr/bin/env python3
"""Optimization- and isolation-safe adversarial tests for the #647 verifier."""

from __future__ import annotations

import ast
import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
from collections.abc import Callable
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
VERIFIER_PATH = HERE / "verify_extension.py"
INPUT = ROOT / "certificates" / "finite_extension_input.json"
CERTIFICATE = ROOT / "certificates" / "finite_extension_certificate.json"


class TestFailure(RuntimeError):
    """An explicit test failure that remains active under Python -O."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise TestFailure(message)


def load_verifier():
    """Load by absolute file path so Python -I needs no sys.path mutation."""
    spec = importlib.util.spec_from_file_location("erdos647_verify_extension",
                                                  VERIFIER_PATH)
    require(spec is not None and spec.loader is not None,
            "could not create import specification for verifier")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


v = load_verifier()


def expect_exception(name: str, fn: Callable[[], object], phrases: tuple[str, ...]) -> None:
    try:
        fn()
    except Exception as exc:
        message = str(exc)
        require(any(phrase in message for phrase in phrases),
                f"{name}: wrong failure message: {message!r}")
        print(f"PASS negative {name}: {message}")
        return
    raise TestFailure(f"{name}: invalid input was accepted")


def expect_process_failure(name: str, cmd: list[str], phrase: str) -> None:
    run = subprocess.run(cmd, text=True, capture_output=True)
    require(run.returncode != 0,
            f"{name}: subprocess unexpectedly returned success\n{run.stdout}")
    require(phrase in run.stderr,
            f"{name}: expected {phrase!r} in stderr\n{run.stderr}")
    print(f"PASS negative {name}: exit={run.returncode}, matched={phrase!r}")


def write_json(path: Path, obj: object) -> None:
    path.write_text(json.dumps(obj, sort_keys=True), encoding="utf-8")


def reject_source_assert_statements() -> None:
    for path in (VERIFIER_PATH, Path(__file__).resolve()):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        count = sum(isinstance(node, ast.Assert) for node in ast.walk(tree))
        require(count == 0, f"{path.name} contains {count} optimization-sensitive assert statements")
    print("PASS source audit: no optimization-sensitive assert statements")


def main() -> None:
    reject_source_assert_statements()

    cert_input = v.validate_input_schema(json.loads(INPUT.read_text(encoding="utf-8")))
    pairs = INPUT.parent / cert_input["pairs_file"]
    rows = v.validate_pairs(pairs, cert_input)
    require(len(rows) == 96 * 529 == 50_784,
            f"wrong reconstructed pair count: {len(rows)}")
    require(len(v.expected_sieve_residues(cert_input)) == 96,
            "wrong reconstructed sieve-residue count")
    print("PASS positive pair reconstruction: 96 x 529 = 50,784")

    exact = v.validate_output_certificate(
        json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    )
    require(exact["status"] == "PASS", "stored output status is not PASS")
    require(exact["cells"] == 5_078_450_784,
            f"wrong stored cell count: {exact['cells']}")
    require(exact["independently_factored_hard_cells"] == 21,
            "wrong stored hard-certificate count")
    artifact_paths = {
        "input": INPUT,
        "pairs": pairs,
        "c_replay_source": HERE / "replay_open_subaps.c",
        "python_verifier": VERIFIER_PATH,
        "discovery_log": ROOT / "experiments" / "raw" /
                         "discovery_extension_u149000001_149100000.log",
    }
    for name, path in artifact_paths.items():
        require(exact["sha256"][name] == v.sha256(path),
                f"stored output has stale {name} SHA-256")
    print("PASS positive output certificate: 5,078,450,784 cells and 21 exact hard records")

    pair_B = {(r, s): B for r, s, B in rows}
    expect_exception(
        "hard-coordinate parameterization",
        lambda: v.exactify_hard(
            ["HARD r=0 s=0 u=149000000 n=1"], 16,
            cert_input["parameterization"]["A"],
            cert_input["parameterization"]["u_lo"],
            cert_input["parameterization"]["u_hi"], pair_B,
        ),
        ("parameterization",),
    )

    bad_hash = copy.deepcopy(cert_input)
    bad_hash["pairs_sha256"] = "0" * 64
    expect_exception(
        "pair hash",
        lambda: v.validate_pairs(pairs, bad_hash),
        ("SHA-256",),
    )

    with tempfile.TemporaryDirectory(prefix="e647-negative-tests-") as td_raw:
        td = Path(td_raw)

        lines = pairs.read_text(encoding="ascii").splitlines()
        require(len(lines) == 50_784, "fixture pair table has wrong line count")
        lines[-1] = lines[0]
        dup_pairs = td / "pairs.tsv"
        dup_pairs.write_text("\n".join(lines) + "\n", encoding="ascii")
        dup_input = copy.deepcopy(cert_input)
        dup_input["pairs_sha256"] = hashlib.sha256(dup_pairs.read_bytes()).hexdigest()
        expect_exception(
            "duplicate pair",
            lambda: v.validate_pairs(dup_pairs, dup_input),
            ("uniqueness", "full"),
        )

        # The subprocess negative tests deliberately use both -O and -I.
        # They fail before resolving relative artifact paths or launching C.
        bad_endpoint = copy.deepcopy(cert_input)
        bad_endpoint["new_frontier"] += 1
        endpoint_path = td / "bad_endpoint.json"
        write_json(endpoint_path, bad_endpoint)
        expect_process_failure(
            "endpoint identity",
            [sys.executable, "-O", "-I", str(VERIFIER_PATH),
             "--input", str(endpoint_path)],
            "new endpoint identity failure",
        )

        unsafe = copy.deepcopy(cert_input)
        A = unsafe["parameterization"]["A"]
        unsafe_u = (2**63 - 1) // A + 1
        unsafe["parameterization"]["u_lo"] = unsafe_u
        unsafe["parameterization"]["u_hi"] = unsafe_u
        unsafe["prior_frontier"] = A * unsafe_u
        unsafe["new_frontier"] = A * unsafe_u
        unsafe_path = td / "unsafe.json"
        write_json(unsafe_path, unsafe)
        expect_process_failure(
            "signed-64 overflow",
            [sys.executable, "-O", "-I", str(VERIFIER_PATH),
             "--input", str(unsafe_path)],
            "signed-64 safety domain",
        )

        missing = copy.deepcopy(cert_input)
        del missing["sieve_definition"]
        missing_path = td / "missing_field.json"
        write_json(missing_path, missing)
        expect_process_failure(
            "deleted required field",
            [sys.executable, "-O", "-I", str(VERIFIER_PATH),
             "--input", str(missing_path)],
            "missing required field(s): sieve_definition",
        )

    bad_factor = copy.deepcopy(exact)
    first_fac = bad_factor["hard_certificates"][0]["factorization"]
    first_prime = next(iter(first_fac))
    first_fac[first_prime] += 1
    expect_exception(
        "modified hard factor",
        lambda: v.validate_output_certificate(bad_factor),
        ("factor product mismatch",),
    )

    print("PASS ALL: explicit fail-closed checks survived this interpreter mode")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"TEST FAILURE: {exc}", file=sys.stderr)
        raise SystemExit(1)
