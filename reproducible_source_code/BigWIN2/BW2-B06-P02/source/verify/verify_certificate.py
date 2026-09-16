#!/usr/bin/env python3
"""Fail-closed exact verifier for the L_8 shortest-superstring certificate.

Only Python integer/string operations are used.  The certificate's dual
numbers are never trusted as solver output: all assignment-dual inequalities
are regenerated and checked one by one.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import pathlib
import sys


ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_CERT = ROOT / "certificates" / "lyndon8_optimum.json"
TOP_KEYS = {
    "schema",
    "alphabet_order",
    "target_length",
    "target_count",
    "claimed_optimum_length",
    "witness",
    "target_order",
    "overlap_assignment_dual",
}
DUAL_KEYS = {"node_order", "u", "v", "claimed_dual_value"}


def fail(message: str) -> "None":
    raise SystemExit("FAIL: " + message)


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rotations(word: str) -> list[str]:
    return [word[k:] + word[:k] for k in range(1, len(word))]


def generate_targets() -> list[str]:
    ans = []
    for bits in itertools.product("01", repeat=8):
        word = "".join(bits)
        if all(word < other for other in rotations(word)):
            ans.append(word)
    return ans


def overlap(left: str, right: str) -> int:
    if left == right:
        fail("overlap called on identical target nodes")
    for size in range(7, 0, -1):
        if left[-size:] == right[:size]:
            return size
    return 0


def require_plain_int(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        fail(f"{label} is not a plain JSON integer")
    return value


def main() -> None:
    if len(sys.argv) > 2:
        fail("usage: verify_certificate.py [certificate.json]")
    cert_path = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else DEFAULT_CERT
    try:
        raw = cert_path.read_text(encoding="utf-8")
        cert = json.loads(raw)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        fail(f"cannot parse certificate: {exc}")

    if not isinstance(cert, dict) or set(cert) != TOP_KEYS:
        fail("unexpected or missing top-level keys")
    if cert["schema"] != "lyndon8-scs-certificate-v1":
        fail("unknown certificate schema")
    if cert["alphabet_order"] != "0<1":
        fail("wrong alphabet convention")
    if require_plain_int(cert["target_length"], "target_length") != 8:
        fail("wrong target length")
    if require_plain_int(cert["target_count"], "target_count") != 30:
        fail("wrong target count")

    targets = generate_targets()
    if len(targets) != 30 or targets != sorted(targets) or len(set(targets)) != 30:
        fail("independent Lyndon target generation failed")

    witness = cert["witness"]
    if not isinstance(witness, str) or set(witness) - {"0", "1"}:
        fail("witness is not a binary string")
    claimed_length = require_plain_int(cert["claimed_optimum_length"], "claimed_optimum_length")
    if claimed_length != 94 or len(witness) != claimed_length:
        fail("witness length does not equal the claimed endpoint 94")
    missing = [word for word in targets if word not in witness]
    if missing:
        fail("witness misses targets: " + ",".join(missing))

    order = cert["target_order"]
    if not isinstance(order, list) or any(not isinstance(x, str) for x in order):
        fail("target_order is not a string list")
    if len(order) != 30 or len(set(order)) != 30 or set(order) != set(targets):
        fail("target_order is not a permutation of the regenerated targets")
    rebuilt = order[0]
    path_overlap = 0
    for left, right in zip(order, order[1:]):
        amount = overlap(left, right)
        path_overlap += amount
        rebuilt += right[amount:]
    if rebuilt != witness:
        fail("maximal-overlap reconstruction does not equal the witness")

    dual = cert["overlap_assignment_dual"]
    if not isinstance(dual, dict) or set(dual) != DUAL_KEYS:
        fail("unexpected or missing dual keys")
    nodes = dual["node_order"]
    if nodes != targets + ["*"]:
        fail("dual node order is not regenerated lexicographic targets plus dummy")
    u = dual["u"]
    v = dual["v"]
    if not isinstance(u, list) or not isinstance(v, list) or len(u) != 31 or len(v) != 31:
        fail("dual arrays must each contain 31 integers")
    u = [require_plain_int(x, f"u[{i}]") for i, x in enumerate(u)]
    v = [require_plain_int(x, f"v[{i}]") for i, x in enumerate(v)]
    claimed_dual = require_plain_int(dual["claimed_dual_value"], "claimed_dual_value")
    if sum(u) + sum(v) != claimed_dual or claimed_dual != 146:
        fail("dual sum is not exactly 146")

    checked = 0
    tight = 0
    for i, left in enumerate(nodes):
        for j, right in enumerate(nodes):
            if i == j:
                continue
            weight = overlap(left, right) if left != "*" and right != "*" else 0
            slack = u[i] + v[j] - weight
            if slack < 0:
                fail(f"dual inequality fails at ({left},{right})")
            checked += 1
            tight += slack == 0

    if path_overlap != claimed_dual:
        fail("witness path does not attain dual value 146")
    lower_bound = 30 * 8 - claimed_dual
    if lower_bound != claimed_length:
        fail("dual lower bound does not meet witness length")

    print(
        "OK schema=lyndon8-scs-certificate-v1 "
        f"targets={len(targets)} length={len(witness)} overlap={path_overlap} "
        f"dual_inequalities={checked} tight={tight} lower_bound={lower_bound}"
    )
    print(f"certificate_sha256={sha256(cert_path)}")
    print(f"verifier_sha256={sha256(pathlib.Path(__file__).resolve())}")


if __name__ == "__main__":
    main()
