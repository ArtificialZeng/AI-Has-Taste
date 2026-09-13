#!/usr/bin/env python3
"""Fresh-referee malformed-input attacks for every decisive verifier."""

from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "evidence/witness-31862.json"
CLAIM = "For the reduced harmonic number H_n=U_n/V_n, gcd(U_n,n!)=179."
VERIFIERS = {
    "candidate-lcm": {
        "command": [sys.executable, str(ROOT / "verification/verify_lcm_sum.py")],
        "stdin_path": False,
    },
    "candidate-recurrence": {
        "command": [sys.executable, str(ROOT / "verification/verify_recurrence.py")],
        "stdin_path": False,
    },
    "submitted-audit-tree": {
        "command": [
            sys.executable,
            "-I",
            "-S",
            str(ROOT / "audit/verify_independent_no_import.py"),
        ],
        "stdin_path": True,
    },
    "fresh-referee-factorial": {
        "command": [
            sys.executable,
            "-I",
            "-S",
            str(ROOT / "audit/referee_verify_no_import.py"),
        ],
        "stdin_path": True,
    },
}


def encoded(changes: dict[str, object], remove: str | None = None) -> bytes:
    value = json.loads(SOURCE.read_text(encoding="utf-8"))
    value.update(changes)
    if remove is not None:
        del value[remove]
    return (json.dumps(value, sort_keys=True) + "\n").encode("utf-8")


def run(specification: dict[str, object], path: pathlib.Path) -> subprocess.CompletedProcess[str]:
    command = list(specification["command"])
    if specification["stdin_path"]:
        return subprocess.run(
            command,
            cwd=ROOT,
            input=str(path) + "\n",
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
    return subprocess.run(
        command + [str(path)],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def main() -> int:
    original = SOURCE.read_bytes()
    stripped = original.lstrip()
    attacks = {
        "truncated-json": original[:-2],
        "array-root": b"[]\n",
        "null-root": b"null\n",
        "empty-object": b"{}\n",
        "missing-claim": encoded({}, remove="claim"),
        "unexpected-key": encoded({"unexpected": 1}),
        "schema-version-2": encoded({"schema_version": 2}),
        "schema-version-bool": encoded({"schema_version": True}),
        "schema-version-float": encoded({"schema_version": 1.0}),
        "n-off-by-one": encoded({"n": 31863}),
        "n-zero": encoded({"n": 0}),
        "n-negative": encoded({"n": -31862}),
        "n-huge": encoded({"n": 10**100}),
        "n-as-string": encoded({"n": "31862"}),
        "n-as-bool": encoded({"n": True}),
        "n-as-float": encoded({"n": 31862.0}),
        "n-as-exponent": original.replace(b'"n": 31862', b'"n": 3.1862e4'),
        "n-as-nan": original.replace(b'"n": 31862', b'"n": NaN'),
        "wrong-p": encoded({"p": 181}),
        "wrong-expected-h": encoded({"expected_h": 181}),
        "expected-h-bool": encoded({"expected_h": True}),
        "empty-claim": encoded({"claim": ""}),
        "integer-claim": encoded({"claim": 179}),
        "contradictory-claim": encoded({"claim": "gcd(U_n,n!)=1."}),
        "claim-with-trailing-space": encoded({"claim": CLAIM + " "}),
        "claim-with-nul": encoded({"claim": CLAIM + "\u0000"}),
        "duplicate-n-last-correct": b'{"n":1,' + stripped[1:],
        "duplicate-n-last-wrong": original.rstrip()[:-1] + b',"n":1}\n',
        "duplicate-escaped-n": b'{"\\u006e":1,' + stripped[1:],
        "duplicate-claim-last-correct": b'{"claim":"gcd(U_n,n!)=1.",' + stripped[1:],
        "duplicate-escaped-claim": b'{"\\u0063laim":"wrong",' + stripped[1:],
        "trailing-json": original + b"{}\n",
        "invalid-utf8": original.replace(b'"claim": "', b'"claim": "\xff', 1),
        "surrogate-escape": encoded({"claim": "placeholder"}).replace(
            b'"placeholder"', b'"\\ud800"'
        ),
    }

    report: dict[str, object] = {
        "baseline": {},
        "attacks": {},
        "attack_count": len(attacks),
    }
    with tempfile.TemporaryDirectory(prefix="mac01-p15-referee-fc-") as directory:
        temporary = pathlib.Path(directory)
        baseline_path = temporary / "baseline.json"
        baseline_path.write_bytes(original)
        baseline_ok = True
        for name, specification in VERIFIERS.items():
            completed = run(specification, baseline_path)
            passed = completed.returncode == 0
            report["baseline"][name] = {
                "result": "PASS" if passed else "REJECT",
                "stdout": completed.stdout.strip(),
            }
            baseline_ok = baseline_ok and passed

        accepted_attacks: dict[str, list[str]] = {}
        for attack_name, payload in attacks.items():
            attack_path = temporary / (attack_name + ".json")
            attack_path.write_bytes(payload)
            accepted_by = []
            for verifier_name, specification in VERIFIERS.items():
                if run(specification, attack_path).returncode == 0:
                    accepted_by.append(verifier_name)
            report["attacks"][attack_name] = {
                "expected": "REJECT",
                "accepted_by": accepted_by,
            }
            if accepted_by:
                accepted_attacks[attack_name] = accepted_by

    report["baseline_passed"] = baseline_ok
    report["fail_closed"] = baseline_ok and not accepted_attacks
    report["accepted_attacks"] = accepted_attacks
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0 if report["fail_closed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
