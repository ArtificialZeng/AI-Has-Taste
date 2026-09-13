#!/usr/bin/env python3
"""Fail-closed mutation tests for breaker_enumerate.verify_outputs."""

from __future__ import annotations

import hashlib
import json
import tempfile
from pathlib import Path

from breaker_enumerate import encode_graph6, verify_outputs


HERE = Path(__file__).resolve().parent


def write_fixture(target: Path) -> tuple[dict[str, object], list[str]]:
    manifest = json.loads((HERE / "breaker_enumeration_manifest.json").read_text())
    lines = (HERE / "breaker_n9_nonbip_e_le6.g6").read_text(encoding="ascii").splitlines()
    (target / "breaker_n9_nonbip_e_le6.g6").write_text(
        "".join(line + "\n" for line in lines), encoding="ascii"
    )
    (target / "breaker_enumeration_manifest.json").write_text(
        json.dumps(manifest), encoding="utf-8"
    )
    return manifest, lines


def replace_fixture(target: Path, manifest: dict[str, object], lines: list[str]) -> None:
    raw = "".join(line + "\n" for line in lines).encode("ascii")
    manifest["graph6_sha256"] = hashlib.sha256(raw).hexdigest()
    (target / "breaker_n9_nonbip_e_le6.g6").write_bytes(raw)
    (target / "breaker_enumeration_manifest.json").write_text(
        json.dumps(manifest), encoding="utf-8"
    )


def must_reject(label: str, mutation) -> None:
    with tempfile.TemporaryDirectory(prefix="n9-breaker-test-") as name:
        target = Path(name)
        manifest, lines = write_fixture(target)
        mutation(target, manifest, lines)
        try:
            verify_outputs(target)
        except (ValueError, KeyError, TypeError) as exc:
            print(f"PASS reject {label}: {type(exc).__name__}: {exc}")
        else:
            raise AssertionError(f"verifier accepted mutation: {label}")


def main() -> None:
    verify_outputs(HERE)

    def stale_hash(target, manifest, lines):
        path = target / "breaker_n9_nonbip_e_le6.g6"
        path.write_bytes(path.read_bytes() + b"H????CB\n")

    must_reject("stale hash", stale_hash)

    def duplicate(target, manifest, lines):
        lines.append(lines[0])
        replace_fixture(target, manifest, lines)

    must_reject("duplicate canonical graph", duplicate)

    def bad_length(target, manifest, lines):
        lines[0] = lines[0][:-1]
        replace_fixture(target, manifest, lines)

    must_reject("truncated graph6", bad_length)

    def bad_byte(target, manifest, lines):
        lines[0] = " " + lines[0][1:]
        replace_fixture(target, manifest, lines)

    must_reject("invalid graph6 byte", bad_byte)

    def bipartite_intruder(target, manifest, lines):
        # The empty graph on 9 vertices is a valid small graph6 record but is
        # outside the declared nonbipartite set.
        lines[0] = encode_graph6(tuple(0 for _ in range(9)))
        replace_fixture(target, manifest, lines)

    must_reject("bipartite intruder", bipartite_intruder)

    def coordinated_deletion(target, manifest, lines):
        removed = lines.pop()
        removed_record = manifest["records"].pop()
        edge = str(removed_record["edges"])
        manifest["counts_by_edges"][edge]["nonbipartite"] -= 1
        manifest["counts_total"]["nonbipartite"] -= 1
        replace_fixture(target, manifest, lines)

    must_reject("coordinated deletion plus manifest rewrite", coordinated_deletion)
    print("PASS: all enumeration verifier mutation tests rejected")


if __name__ == "__main__":
    main()
