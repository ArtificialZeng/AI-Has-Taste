#!/usr/bin/env python3
"""Cross-verifier attacks for canonical, fail-closed JSON decoding.

Every non-star1 decisive primary is attacked with a duplicate top-level key
and a boolean in a non-boolean field.  Every format containing a nested JSON
object is additionally attacked with a duplicate key inside that object.
The duplicate-key attacks put a bad first value before the valid serialized
value, so a permissive ``json.loads`` would silently accept the certificate.
"""

from __future__ import annotations

import copy
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


CASES = [
    {
        "name": "q3",
        "certificate": "results/q3_classification_certificate.json",
        "verifier": "src/verify_q3_classification.py",
        "top_key": "schema",
        "nested": None,
        "boolean_mutation": lambda obj: obj["positive_saturation"].__setitem__(0, True),
    },
    {
        "name": "empty",
        "certificate": "results/empty_highpair_classification_certificate.json",
        "verifier": "src/verify_empty_highpair_classification.py",
        "top_key": "certificate_type",
        "nested": ("theorem", "claim"),
        "boolean_mutation": lambda obj: obj.__setitem__("format_version", True),
    },
    {
        "name": "star2",
        "certificate": "results/star2_bernstein_no_go_certificate.json",
        "verifier": "src/verify_star2_bernstein.py",
        "top_key": "schema",
        "nested": ("normalization", "a4"),
        "boolean_mutation": lambda obj: obj["normalization"].__setitem__("a4", True),
    },
    {
        "name": "star3",
        "certificate": "certificates/star3_decomposition.json",
        "verifier": "src/builder_verify_star3.py",
        "top_key": "schema_version",
        "nested": ("ordered_chamber", "weak_order"),
        "boolean_mutation": lambda obj: obj.__setitem__("schema_version", True),
    },
    {
        "name": "star4",
        "certificate": "results/breaker_star4_certificate.json",
        "verifier": "src/breaker_star4_verify.py",
        "top_key": "schema",
        "nested": ("ideal_consequences", "h23"),
        "boolean_mutation": lambda obj: obj.__setitem__("expected_saturated_dimension", False),
    },
    {
        "name": "triangle",
        "certificate": "results/triangle_highpair_no_go_certificate.json",
        "verifier": "src/verify_triangle_highpair_no_go.py",
        "top_key": "certificate_type",
        "nested": ("theorem", "claim"),
        "boolean_mutation": lambda obj: obj.__setitem__("format_version", True),
    },
]


def add_top_duplicate(raw: str, key: str) -> str:
    return re.sub(r"\{", '{"' + key + '":"__bad_first_value__",', raw, count=1)


def add_nested_duplicate(raw: str, object_key: str, nested_key: str) -> str:
    pattern = r'("' + re.escape(object_key) + r'"\s*:\s*\{)'
    replacement = r'\1"' + nested_key + r'":"__bad_first_value__",'
    changed, count = re.subn(pattern, replacement, raw, count=1)
    if count != 1:
        raise RuntimeError(f"could not locate nested object {object_key}")
    return changed


def invoke(verifier: Path, certificate: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(verifier), str(certificate)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=30,
        check=False,
    )


def require_rejection(name: str, result: subprocess.CompletedProcess[str]) -> None:
    if result.returncode == 0:
        raise RuntimeError(f"{name}: malformed JSON was accepted")


def main() -> int:
    attacks = 0
    with tempfile.TemporaryDirectory(prefix="q5-json-failclosed-") as directory:
        temp = Path(directory)
        for case in CASES:
            source = ROOT / case["certificate"]
            verifier = ROOT / case["verifier"]
            raw = source.read_text(encoding="utf-8")
            obj = json.loads(raw)

            path = temp / f"{case['name']}-duplicate-top.json"
            path.write_text(add_top_duplicate(raw, case["top_key"]), encoding="utf-8")
            require_rejection(f"{case['name']} duplicate top-level key", invoke(verifier, path))
            attacks += 1

            if case["nested"] is not None:
                object_key, nested_key = case["nested"]
                path = temp / f"{case['name']}-duplicate-nested.json"
                path.write_text(add_nested_duplicate(raw, object_key, nested_key), encoding="utf-8")
                require_rejection(f"{case['name']} duplicate nested key", invoke(verifier, path))
                attacks += 1

            malformed = copy.deepcopy(obj)
            case["boolean_mutation"](malformed)
            path = temp / f"{case['name']}-boolean.json"
            path.write_text(json.dumps(malformed), encoding="utf-8")
            require_rejection(f"{case['name']} boolean field", invoke(verifier, path))
            attacks += 1

    print(f"PASS: all {attacks} non-star1 duplicate-key/boolean attacks rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
