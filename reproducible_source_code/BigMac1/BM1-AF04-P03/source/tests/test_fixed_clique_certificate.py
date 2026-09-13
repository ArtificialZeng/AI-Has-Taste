#!/usr/bin/env python3
"""Fail-closed corruption tests for every fixed-branch finite certificate."""

from __future__ import annotations

import copy
import json
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "code/verify_fixed_clique_certificate.py"


def run(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["python3", str(VERIFIER), "--manifest", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )


def main() -> int:
    manifests = sorted((ROOT / "certificates/negative").glob("fixed*_finite_manifest.json"))
    assert manifests
    with tempfile.TemporaryDirectory(prefix="cyclic315-fixed-cert-audit-") as directory:
        for manifest_path in manifests:
            baseline = run(manifest_path)
            assert baseline.returncode == 0 and "VERIFIED" in baseline.stdout
            manifest = json.loads(manifest_path.read_text())
            mutations = []
            changed_block = copy.deepcopy(manifest)
            changed_block["fixed_block"][-1] = (changed_block["fixed_block"][-1] + 1) % 31
            mutations.append(changed_block)
            changed_hash = copy.deepcopy(manifest)
            changed_hash["enumeration"]["sha256"] = "0" * 64
            mutations.append(changed_hash)
            shortened_orbit = copy.deepcopy(manifest)
            shortened_orbit["multiplier_orbit_variables"].pop()
            mutations.append(shortened_orbit)
            boolean_variable = copy.deepcopy(manifest)
            boolean_variable["fixed_variable"] = True
            mutations.append(boolean_variable)
            changed_scope = copy.deepcopy(manifest)
            changed_scope["scope"] = "unsupported global claim"
            mutations.append(changed_scope)
            for index, mutation in enumerate(mutations):
                path = Path(directory) / f"{manifest_path.stem}-mutation-{index}.json"
                path.write_text(json.dumps(mutation))
                rejected = run(path)
                assert rejected.returncode != 0, (index, rejected.stdout, rejected.stderr)
    print(f"{len(manifests)} fixed-branch finite certificates and corruption tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
