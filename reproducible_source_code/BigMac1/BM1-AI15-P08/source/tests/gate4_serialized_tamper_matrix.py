#!/usr/bin/env python3
"""Run the Gate-4 serialized-certificate tamper matrix.

This standard-library-only driver invokes the verifier from a fresh external
working directory in normal, -O, -I, and -O -I modes.  It checks the genuine
artifact and four adversarial cases.  The change-expression case rewrites a
check to a self-consistent tautology and synchronizes the certificate digest
inside a copied manifest; the independently pinned manifest digest must still
reject the pair.
"""

import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


PROJECT_ROOT = Path(__file__).resolve().parents[1]
VERIFIER = PROJECT_ROOT / "tests" / "verify_serialized_low_degree_certificate.py"
CERTIFICATE = PROJECT_ROOT / "certificates" / "low_degree_identities.json"
MANIFEST = PROJECT_ROOT / "certificates" / "low_degree_certificate_manifest.json"
MODES = (
    ("normal", ()),
    ("-O", ("-O",)),
    ("-I", ("-I",)),
    ("-O -I", ("-O", "-I")),
)


def fail(message):
    raise SystemExit(f"GATE4 MATRIX FAILED: {message}")


def run(mode_flags, arguments, cwd):
    command = [sys.executable, *mode_flags, str(VERIFIER), *map(str, arguments)]
    return subprocess.run(
        command,
        cwd=cwd,
        text=True,
        capture_output=True,
        check=False,
    )


def require_result(result, should_pass, fragment, mode, case_name):
    combined = result.stdout + result.stderr
    if should_pass:
        if result.returncode != 0:
            fail(f"{mode}/{case_name}: exit {result.returncode}: {combined.strip()}")
    elif result.returncode == 0:
        fail(f"{mode}/{case_name}: tampered input exited zero")
    if fragment not in combined:
        fail(f"{mode}/{case_name}: missing diagnostic {fragment!r}: {combined.strip()}")
    print(f"PASS mode={mode!r} case={case_name!r} exit={result.returncode}")


def write_json(path, value):
    path.write_text(
        json.dumps(value, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def make_synced_change_expression(directory):
    certificate = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    boundary_check = certificate["groups"][1]["checks"][2]
    boundary_check["left"] = "0"
    boundary_check["right"] = "0"
    changed_certificate = directory / "changed_certificate.json"
    write_json(changed_certificate, certificate)
    changed_digest = hashlib.sha256(changed_certificate.read_bytes()).hexdigest()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest["certificate"]["sha256"] = changed_digest
    changed_manifest = directory / "changed_manifest.json"
    write_json(changed_manifest, manifest)
    return changed_certificate, changed_manifest


def main():
    with tempfile.TemporaryDirectory(prefix="sheil_gate4_matrix_") as directory_text:
        directory = Path(directory_text)
        badhash = directory / "badhash_certificate.json"
        badhash.write_bytes(CERTIFICATE.read_bytes() + b"\n")
        changed_certificate, changed_manifest = make_synced_change_expression(directory)

        for mode, flags in MODES:
            require_result(
                run(flags, (), directory),
                True,
                "serialized certificate: OK",
                mode,
                "genuine",
            )
            require_result(
                run(flags, (badhash,), directory),
                False,
                "certificate digest",
                mode,
                "badhash",
            )
            require_result(
                run(flags, ("--tamper-case", "extra-field"), directory),
                False,
                "certificate fields",
                mode,
                "extra-field",
            )
            require_result(
                run(flags, ("--tamper-case", "drop-check"), directory),
                False,
                "wrong check count",
                mode,
                "drop-check",
            )
            require_result(
                run(
                    flags,
                    (changed_certificate, "--manifest", changed_manifest),
                    directory,
                ),
                False,
                "manifest digest",
                mode,
                "change-expression",
            )
            require_result(
                run(flags, ("--tamper-case", "change-expression"), directory),
                False,
                "residual",
                mode,
                "change-expression-in-memory",
            )

    print("Gate-4 serialized-certificate matrix: OK (24/24 expected outcomes)")


if __name__ == "__main__":
    main()
