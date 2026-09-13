#!/usr/bin/env python3
"""Fail-closed independent verifier for the strict finite #647 extension."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).resolve().parent
DEFAULT_INPUT = ROOT / "certificates" / "finite_extension_input.json"
C_SOURCE = HERE / "replay_open_subaps.c"


def require(condition: bool, message: str) -> None:
    """Raise explicitly when a certificate invariant is not satisfied."""
    if not condition:
        raise ValueError(message)


def require_fields(obj: object, fields: tuple[str, ...], context: str) -> dict:
    require(isinstance(obj, dict), f"{context} must be a JSON object")
    missing = [field for field in fields if field not in obj]
    require(not missing, f"{context} missing required field(s): {', '.join(missing)}")
    return obj


def validate_input_schema(cert: object) -> dict:
    cert = require_fields(cert, (
        "schema_version", "problem", "prior_frontier", "new_frontier",
        "parameterization", "sieve_definition", "sieve_pair_count",
        "pairs_file", "pairs_sha256", "discovery_log",
        "discovery_log_sha256", "imported_dependency",
    ), "input certificate")
    require(cert["schema_version"] == 1, "unsupported input schema")
    require_fields(cert["parameterization"],
                   ("A", "formula", "u_lo", "u_hi", "k_cover"),
                   "parameterization")
    require_fields(cert["sieve_definition"],
                   ("modulus", "coefficients", "sieve_primes", "rule",
                    "surviving_residue_count", "subprogression_modulus"),
                   "sieve_definition")
    require_fields(cert["imported_dependency"],
                   ("statement", "source", "scope_note"),
                   "imported_dependency")
    return cert


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def is_prime(n: int) -> bool:
    """Deterministic Miller--Rabin for 0 <= n < 2^64."""
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if a % n == 0:
            continue
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def pollard_rho(n: int) -> int:
    if n % 2 == 0:
        return 2
    if n % 3 == 0:
        return 3
    for c in range(1, 256):
        x = y = 2
        d = 1
        while d == 1:
            x = (x * x + c) % n
            y = (y * y + c) % n
            y = (y * y + c) % n
            d = math.gcd(abs(x - y), n)
        if d != n:
            return d
    raise RuntimeError(f"deterministic Pollard-rho failed on {n}")


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    stack = [n]
    while stack:
        x = stack.pop()
        if x == 1:
            continue
        if is_prime(x):
            out[x] = out.get(x, 0) + 1
            continue
        d = pollard_rho(x)
        stack.extend((d, x // d))
    return dict(sorted(out.items()))


def tau(n: int) -> tuple[int, dict[int, int]]:
    fac = factor(n)
    value = math.prod(e + 1 for e in fac.values())
    return value, fac


def validate_output_certificate(record: object) -> dict:
    """Validate a serialized or freshly generated decisive result record."""
    record = require_fields(record, (
        "status", "statement", "pairs", "cells",
        "cheap_exact_lower_bound_kills", "independently_factored_hard_cells",
        "hard_certificates", "sha256", "proof_assistant_used_by_this_verifier",
        "scope",
    ), "output certificate")
    require(record["status"] == "PASS", "output certificate status is not PASS")
    require(isinstance(record["statement"], str) and record["statement"],
            "output certificate statement is empty")
    require(isinstance(record["pairs"], int) and record["pairs"] > 0,
            "output certificate has invalid pair count")
    require(isinstance(record["cells"], int) and record["cells"] > 0,
            "output certificate has invalid cell count")
    require(isinstance(record["hard_certificates"], list),
            "hard_certificates must be a JSON array")
    hard = record["hard_certificates"]
    require(record["independently_factored_hard_cells"] == len(hard),
            "hard-certificate count mismatch")
    require(record["cheap_exact_lower_bound_kills"] + len(hard) == record["cells"],
            "output certificate accounting mismatch")
    require(record["proof_assistant_used_by_this_verifier"] is False,
            "unexpected proof-assistant flag")
    hashes = require_fields(record["sha256"],
                            ("input", "pairs", "c_replay_source",
                             "python_verifier", "discovery_log"),
                            "output certificate sha256")
    for name, digest in hashes.items():
        require(isinstance(digest, str) and
                re.fullmatch(r"[0-9a-f]{64}", digest) is not None,
                f"output certificate has invalid SHA-256 for {name}")

    seen = set()
    previous_sort_key = None
    for index, raw in enumerate(hard):
        item = require_fields(raw, (
            "r", "s", "u", "n", "kill_k", "tau", "factorization",
        ), f"hard certificate {index}")
        for field in ("r", "s", "u", "n", "kill_k", "tau"):
            require(isinstance(item[field], int) and not isinstance(item[field], bool),
                    f"hard certificate {index} has non-integer {field}")
        require(1 <= item["kill_k"] <= 16,
                f"hard certificate {index} has invalid killing shift")
        key = (item["r"], item["s"], item["u"], item["n"])
        require(key not in seen, f"duplicate serialized hard certificate {key}")
        seen.add(key)
        sort_key = (item["n"], item["r"], item["s"], item["u"])
        require(previous_sort_key is None or previous_sort_key < sort_key,
                "hard certificates are not in canonical order")
        previous_sort_key = sort_key

        raw_fac = item["factorization"]
        require(isinstance(raw_fac, dict) and raw_fac,
                f"hard certificate {index} has invalid factorization")
        fac: dict[int, int] = {}
        for raw_prime, raw_exp in raw_fac.items():
            try:
                prime = int(raw_prime)
            except (TypeError, ValueError) as exc:
                raise ValueError(
                    f"hard certificate {index} has non-integer prime key"
                ) from exc
            require(str(prime) == str(raw_prime),
                    f"hard certificate {index} has non-canonical prime key")
            require(isinstance(raw_exp, int) and not isinstance(raw_exp, bool)
                    and raw_exp > 0,
                    f"hard certificate {index} has invalid exponent")
            require(prime not in fac,
                    f"hard certificate {index} repeats a prime factor")
            require(is_prime(prime),
                    f"hard certificate {index} contains a composite factor")
            fac[prime] = raw_exp
        require(math.prod(prime ** exp for prime, exp in fac.items())
                == item["n"] - item["kill_k"],
                f"hard certificate {index} factor product mismatch")
        computed_tau = math.prod(exp + 1 for exp in fac.values())
        require(computed_tau == item["tau"],
                f"hard certificate {index} divisor count mismatch")
        require(computed_tau > item["kill_k"] + 2,
                f"hard certificate {index} does not kill its cell")
    return record


def expected_sieve_residues(cert: dict) -> list[int]:
    sd = cert["sieve_definition"]
    modulus = sd["modulus"]
    coeffs = sd["coefficients"]
    primes = sd["sieve_primes"]
    if modulus != math.prod(primes):
        raise ValueError("sieve modulus factorization mismatch")
    residues = [r for r in range(modulus)
                if all(d * r % q != 1 for d in coeffs for q in primes)]
    if len(residues) != sd["surviving_residue_count"]:
        raise ValueError("sieve survivor-count mismatch")
    return residues


def validate_pairs(path: Path, cert: dict) -> list[tuple[int, int, int]]:
    if sha256(path) != cert["pairs_sha256"]:
        raise ValueError("pairs SHA-256 mismatch")
    rows = []
    for line_no, line in enumerate(path.read_text().splitlines(), 1):
        cols = line.split()
        if len(cols) != 3:
            raise ValueError(f"malformed pair line {line_no}")
        r, s, B = map(int, cols)
        if not (0 <= r < 46189 and 0 <= s < 529):
            raise ValueError(f"out-of-range pair at line {line_no}")
        if B != 2520 * (46189 * s + r):
            raise ValueError(f"wrong B at line {line_no}")
        rows.append((r, s, B))
    if len(rows) != cert["sieve_pair_count"] or len(set(rows)) != len(rows):
        raise ValueError("pair count or uniqueness failure")
    residues = expected_sieve_residues(cert)
    submod = cert["sieve_definition"]["subprogression_modulus"]
    expected_pairs = {(r, s) for r in residues for s in range(submod)}
    actual_pairs = {(r, s) for r, s, _ in rows}
    if actual_pairs != expected_pairs:
        raise ValueError("pair set is not the full 96-residue x 529 product")
    return rows


def exactify_hard(lines: list[str], kmax: int, A: int, ulo: int, uhi: int,
                  pair_B: dict[tuple[int, int], int]) -> list[dict]:
    hard_re = re.compile(r"^HARD r=(\d+) s=(\d+) u=(\d+) n=(\d+)$")
    results = []
    seen = set()
    for line in lines:
        m = hard_re.match(line)
        if not m:
            continue
        r, s, u, n = map(int, m.groups())
        key = (r, s, u, n)
        if key in seen:
            raise ValueError("duplicate HARD record")
        seen.add(key)
        if (r, s) not in pair_B:
            raise ValueError(f"HARD record uses an unknown pair {key}")
        if not (ulo <= u <= uhi):
            raise ValueError(f"HARD record has out-of-range u {key}")
        if n != A * u + pair_B[r, s] or not (0 < n < 2**63):
            raise ValueError(f"HARD record parameterization failure {key}")
        for k in range(1, kmax + 1):
            t, fac = tau(n - k)
            if t > k + 2:
                results.append({"r": r, "s": s, "u": u, "n": n,
                                "kill_k": k, "tau": t,
                                "factorization": fac})
                break
        else:
            raise ValueError(f"unresolved HARD cell {key}; verifier fails closed")
    results.sort(key=lambda item: (item["n"], item["r"], item["s"], item["u"]))
    return results


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    ap.add_argument("--threads", type=int,
                    default=min(12, max(1, os.cpu_count() or 1)))
    ap.add_argument("--cc", default=os.environ.get("CC", "clang"))
    args = ap.parse_args()

    cert = validate_input_schema(json.loads(args.input.read_text()))
    p = cert["parameterization"]
    A, ulo, uhi = p["A"], p["u_lo"], p["u_hi"]
    if A != 2520 * 46189 * 529:
        raise ValueError("A identity failure")
    # Include the left boundary layer itself.  Since 0 is one of the sieve
    # residues, u=ulo contains n=A*ulo exactly; the extra point is harmless,
    # while every B>0 in that layer is needed to cover the full open interval
    # immediately to the right of the reported prior frontier.
    if cert["prior_frontier"] != A * ulo:
        raise ValueError("left endpoint does not join prior frontier")
    if cert["new_frontier"] != A * uhi:
        raise ValueError("new endpoint identity failure")
    if p["k_cover"] != list(range(1, 17)):
        raise ValueError("unexpected k cover")
    if not (0 < cert["new_frontier"] < 2**63):
        raise ValueError("certified interval is outside signed-64 safety domain")

    pairs_path = args.input.parent / cert["pairs_file"]
    rows = validate_pairs(pairs_path, cert)
    expected_cells = len(rows) * (uhi - ulo + 1)

    discovery = (args.input.parent / cert["discovery_log"]).resolve()
    if sha256(discovery) != cert["discovery_log_sha256"]:
        raise ValueError("discovery log SHA-256 mismatch")

    with tempfile.TemporaryDirectory(prefix="erdos647-verify-") as td:
        exe = Path(td) / "replay"
        subprocess.run([args.cc, "-O3", "-std=c11", "-pthread",
                        str(C_SOURCE), "-o", str(exe)], check=True)
        run = subprocess.run(
            [str(exe), str(pairs_path), str(ulo), str(uhi),
             str(args.threads), str(len(rows))],
            check=True, text=True, capture_output=True,
        )
    if run.stderr:
        print(run.stderr, end="", file=sys.stderr)
    output_lines = run.stdout.splitlines()
    summary_lines = [x for x in output_lines if x.startswith("SUMMARY ")]
    if len(summary_lines) != 1:
        raise ValueError("missing or duplicate SUMMARY")
    fields = dict(re.findall(r"(pairs|cells|cheap_kills|hard)=(\d+)",
                             summary_lines[0]))
    summary = {k: int(v) for k, v in fields.items()}
    if summary.get("pairs") != len(rows) or summary.get("cells") != expected_cells:
        raise ValueError("replay coverage mismatch")
    if summary.get("cheap_kills", -1) + summary.get("hard", -1) != expected_cells:
        raise ValueError("replay accounting mismatch")

    pair_B = {(r, s): B for r, s, B in rows}
    hard = exactify_hard(output_lines, 16, A, ulo, uhi, pair_B)
    if len(hard) != summary["hard"]:
        raise ValueError("HARD record count mismatch")

    record = {
        "status": "PASS",
        "statement": (f"no 12-form-sieve-frontier cell with {cert['prior_frontier']} < n <= "
                      f"{cert['new_frontier']} satisfies all local inequalities"),
        "pairs": len(rows),
        "cells": expected_cells,
        "cheap_exact_lower_bound_kills": summary["cheap_kills"],
        "independently_factored_hard_cells": len(hard),
        "hard_certificates": hard,
        "sha256": {
            "input": sha256(args.input),
            "pairs": sha256(pairs_path),
            "c_replay_source": sha256(C_SOURCE),
            "python_verifier": sha256(Path(__file__)),
            "discovery_log": sha256(discovery),
        },
        "proof_assistant_used_by_this_verifier": False,
        "scope": "new interval only; imported 2520-divisibility and 12-form implications audited separately"
    }
    validate_output_certificate(record)
    print(json.dumps(record, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"VERIFICATION FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
