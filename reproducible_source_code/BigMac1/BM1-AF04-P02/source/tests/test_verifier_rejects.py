#!/usr/bin/env python3
"""Adversarial corruption tests: the full verifier must fail closed."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

FILES = [
    "representatives.json",
    "quotient_edges.json",
    "switch_occurrences.json",
    "result.json",
]


def load(path):
    with open(path, encoding="utf-8") as stream:
        return json.load(stream)


def write(path, value):
    with open(path, "w", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write("\n")


def copy_certificate(source, target):
    target.mkdir()
    for name in FILES:
        shutil.copy2(source / name, target / name)


def run(verifier, directory):
    return subprocess.run(
        [sys.executable, str(verifier), str(directory)],
        text=True,
        capture_output=True,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", default="certificate")
    parser.add_argument("--verifier", default="code/independent_verifier.py")
    parser.add_argument("--output", default="certificate/negative_tests.json")
    args = parser.parse_args()
    source = Path(args.certificate).resolve()
    verifier = Path(args.verifier).resolve()

    baseline = run(verifier, source)
    if baseline.returncode != 0 or '"status": "VERIFIED"' not in baseline.stdout:
        raise SystemExit(f"baseline verification failed: {baseline.stderr}")

    cases = []
    with tempfile.TemporaryDirectory(prefix="sts15-corruption-") as temp:
        root = Path(temp)

        def execute(name, filename, mutation):
            case_dir = root / name
            copy_certificate(source, case_dir)
            path = case_dir / filename
            document = load(path)
            mutation(document)
            write(path, document)
            outcome = run(verifier, case_dir)
            if outcome.returncode == 0:
                raise SystemExit(f"corruption {name} was incorrectly accepted")
            cases.append(
                {
                    "case": name,
                    "mutated_file": filename,
                    "returncode": outcome.returncode,
                    "rejected": True,
                    "diagnostic": outcome.stderr.strip().splitlines()[-1],
                }
            )

        execute(
            "repeated_point_in_block",
            "representatives.json",
            lambda d: d["vertices"][0]["blocks"][0].__setitem__(1, 0),
        )
        execute(
            "missing_vertex",
            "representatives.json",
            lambda d: d["vertices"].pop(),
        )
        execute(
            "deleted_edge",
            "quotient_edges.json",
            lambda d: d["edges"].pop(),
        )
        execute(
            "duplicate_edge",
            "quotient_edges.json",
            lambda d: d["edges"].insert(1, list(d["edges"][0])),
        )
        execute(
            "wrong_diameter",
            "result.json",
            lambda d: d.__setitem__("diameter", d["diameter"] - 1),
        )
        execute(
            "wrong_switch_target",
            "switch_occurrences.json",
            lambda d: d["rows"]["V000"]["switches"][0].__setitem__(
                "target", "V079"
            ),
        )

    output = {
        "schema": "sts15-verifier-negative-tests-v1",
        "baseline_accepted": True,
        "corruptions_tested": len(cases),
        "all_corruptions_rejected": True,
        "cases": cases,
    }
    write(Path(args.output), output)
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
