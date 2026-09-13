#!/usr/bin/env python3
"""Cross-interpreter fail-closed tests for all three exact verifiers."""

import argparse
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def mutated_files(root, temporary):
    root_certificate = root / "certificate/a321614_certificate.json"
    builder_certificate = root / "agents/builder/certificate.json"

    root_bad = json.loads(root_certificate.read_text())
    root_bad["adjacency"][0][0] ^= 1
    root_bad_path = temporary / "root-badmatrix.json"
    root_bad_path.write_text(json.dumps(root_bad))
    root_drop = json.loads(root_certificate.read_text())
    del root_drop["adjacency"]
    root_drop_path = temporary / "root-dropkey.json"
    root_drop_path.write_text(json.dumps(root_drop))

    referee_bad = json.loads(root_certificate.read_text())
    referee_bad["global_representation"]["matrix"][0][0] ^= 1
    referee_bad_path = temporary / "referee-badmatrix.json"
    referee_bad_path.write_text(json.dumps(referee_bad))
    referee_drop = json.loads(root_certificate.read_text())
    del referee_drop["minimality_bezout"]
    referee_drop_path = temporary / "referee-dropkey.json"
    referee_drop_path.write_text(json.dumps(referee_drop))

    builder_bad = json.loads(builder_certificate.read_text())
    builder_bad["transfer_matrix"][0][0] ^= 1
    builder_bad_path = temporary / "builder-badmatrix.json"
    builder_bad_path.write_text(json.dumps(builder_bad))
    builder_drop = json.loads(builder_certificate.read_text())
    del builder_drop["identity_resolvent"]
    builder_drop_path = temporary / "builder-dropkey.json"
    builder_drop_path.write_text(json.dumps(builder_drop))

    return {
        "root": (root_certificate, root_bad_path, root_drop_path),
        "builder": (builder_certificate, builder_bad_path, builder_drop_path),
        "referee": (root_certificate, referee_bad_path, referee_drop_path),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--python", action="append", dest="pythons",
                        help="interpreter to test; repeat for several")
    args = parser.parse_args()
    pythons = args.pythons or [sys.executable]
    root = Path(__file__).resolve().parent.parent
    verifiers = {
        "root": root / "code/verify_certificate.py",
        "builder": root / "agents/builder/verify_certificate.py",
        "referee": root / "agents/referee/verify_no_import.py",
    }
    unexpected = expected_pass = expected_fail = 0
    with tempfile.TemporaryDirectory(prefix="a321614-failclosed-") as name:
        inputs = mutated_files(root, Path(name))
        for python in pythons:
            for flags in ([], ["-O", "-I"]):
                for verifier_name, verifier in verifiers.items():
                    genuine, badmatrix, dropkey = inputs[verifier_name]
                    for input_name, path, should_pass in (
                            ("genuine", genuine, True),
                            ("badmatrix", badmatrix, False),
                            ("drop-key", dropkey, False)):
                        result = subprocess.run(
                            [python] + flags + [str(verifier), str(path)],
                            text=True, capture_output=True)
                        correct = ((result.returncode == 0) == should_pass)
                        if not correct:
                            unexpected += 1
                            print("UNEXPECTED", python, flags, verifier_name,
                                  input_name, "exit=" + str(result.returncode))
                            print(result.stdout + result.stderr)
                        elif should_pass:
                            expected_pass += 1
                        else:
                            expected_fail += 1
    print("FAIL_CLOSED_SUMMARY unexpected=%d expected_pass=%d expected_fail=%d" %
          (unexpected, expected_pass, expected_fail))
    return 1 if unexpected else 0


if __name__ == "__main__":
    sys.exit(main())
