#!/usr/bin/env python3
"""Destructive-input tests for the independent fiber verifier."""

import copy
import hashlib
import importlib.util
import json
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "certificates" / "verify_weight20.py"
SPEC = importlib.util.spec_from_file_location("weight20_verifier", VERIFIER)
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


def must_fail(action, label):
    try:
        action()
    except module.VerificationError:
        return
    raise AssertionError(f"mutation was accepted: {label}")


certificate = json.loads((ROOT / "certificates" / "weight20_certificate.json").read_text())
module.validate_serialized_certificate(certificate)

bad = copy.deepcopy(certificate)
bad["conductor"] = 106
must_fail(lambda: module.validate_serialized_certificate(bad), "wrong conductor")

bad = copy.deepcopy(certificate)
bad["unexpected"] = True
must_fail(lambda: module.validate_serialized_certificate(bad), "unknown top-level field")

bad = copy.deepcopy(certificate)
bad["matrix_sha256"] = "0" * 63
must_fail(lambda: module.validate_serialized_certificate(bad), "truncated digest")

must_fail(lambda: module.safe_sibling("../escape"), "path traversal")
must_fail(lambda: module.safe_sibling("/tmp/escape"), "absolute path")

with tempfile.TemporaryDirectory() as temporary:
    directory = Path(temporary)
    manifest = directory / "manifest.json"
    manifest.write_text("{}\n", encoding="utf-8")
    bad = copy.deepcopy(certificate)
    bad["finite_enumeration"]["path"] = "manifest.json"
    bad["finite_enumeration"]["sha256"] = "0" * 64
    certificate_file = directory / "certificate.json"
    certificate_file.write_text(json.dumps(bad), encoding="utf-8")
    must_fail(lambda: module.verify(certificate_file), "corrupted manifest digest")

# Mutating a listed exponent is detected independently by exact Phi_105 sums.
phi105 = module.cyclotomic(105)
columns105 = module.residue_columns(105, phi105)
mutated = tuple(certificate["representatives"][-1]["subset"][:-1] + [88])
assert any(module.vector_sum(mutated, columns105))

print("fail-closed mutation tests: PASS")
