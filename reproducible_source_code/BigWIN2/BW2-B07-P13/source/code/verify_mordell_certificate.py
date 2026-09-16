#!/usr/bin/env python3
"""Independent, standard-library verifier for the Mordell filter certificate.

The checker starts from the two upstream PDFs, invokes ``pdftotext -raw``
(the discovery extraction used ``-layout``), parses with a character scanner,
checks every displayed Mordell identity, and performs exact trial-division
primality tests only on the 98 range-relevant points.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
from pathlib import Path


def digest_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def digest_path(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def raw_pdf_text(path: Path) -> str:
    result = subprocess.run(
        ["pdftotext", "-raw", str(path), "-"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8")


def scan_tokens(text: str):
    """Yield integers and (x,y) tuples without using a regular expression."""
    index = 0
    size = len(text)
    while index < size:
        char = text[index]
        if char == "[":
            end = text.find("]", index + 1)
            if end < 0:
                raise ValueError("unterminated point token")
            body = text[index + 1:end]
            fields = body.split(",")
            if len(fields) != 2:
                raise ValueError(f"malformed point token [{body}]")
            yield (int(fields[0]), int(fields[1]))
            index = end + 1
        elif char == "-" or char.isdigit():
            start = index
            if char == "-":
                index += 1
                if index == size or not text[index].isdigit():
                    continue
            while index < size and text[index].isdigit():
                index += 1
            yield int(text[start:index])
        else:
            index += 1


def parse_table(text: str, expected_sign: int):
    tokens = iter(scan_tokens(text))
    points: list[tuple[int, int, int]] = []
    keys: list[int] = []
    while True:
        try:
            k = next(tokens)
        except StopIteration:
            break
        try:
            count = next(tokens)
        except StopIteration as exc:
            raise ValueError("missing point count at final record") from exc
        if not isinstance(k, int) or not isinstance(count, int) or count < 0:
            raise ValueError(f"malformed record header {(k, count)}")
        if k == 0 or (k > 0) != (expected_sign > 0):
            raise ValueError(f"wrong-sign record key {k}")
        keys.append(k)
        for _ in range(count):
            try:
                point = next(tokens)
            except StopIteration as exc:
                raise ValueError(f"record k={k} ends early") from exc
            if not isinstance(point, tuple):
                raise ValueError(f"record k={k} contains non-point token {point}")
            x, y = point
            if y * y != x * x * x + k:
                raise ValueError(f"false identity at {(k, x, y)}")
            points.append((k, x, y))
    absolute_keys = [abs(k) for k in keys]
    if len(keys) != len(set(keys)):
        raise ValueError("duplicate k record")
    if absolute_keys != sorted(absolute_keys):
        raise ValueError("record keys not ordered by absolute value")
    return points, {
        "records": len(keys),
        "points": len(points),
        "first_k": keys[0],
        "last_k": keys[-1],
        "maximum_abs_k_present": max(absolute_keys),
    }


def trial_is_prime(n: int) -> bool:
    """Exact primality test by division through floor(sqrt(n))."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    limit = math.isqrt(n)
    while divisor <= limit:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def first_factor(n: int) -> int | None:
    if n % 2 == 0:
        return 2 if n != 2 else None
    divisor = 3
    limit = math.isqrt(n)
    while divisor <= limit:
        if n % divisor == 0:
            return divisor
        divisor += 2
    return None


def classify(k: int, x: int, y: int) -> dict:
    if not trial_is_prime(x):
        factor = first_factor(x)
        if factor is None or not (1 < factor < x) or x % factor:
            raise AssertionError(f"no compositeness witness for x={x}")
        return {"k": k, "x": x, "y": y, "status": "x_composite", "factor": factor}
    if not trial_is_prime(y):
        factor = first_factor(y)
        if factor is None or not (1 < factor < y) or y % factor:
            raise AssertionError(f"no compositeness witness for y={y}")
        return {"k": k, "x": x, "y": y, "status": "y_composite", "factor": factor}
    return {"k": k, "x": x, "y": y, "status": "both_prime"}


def verify_pocklington(entry: dict) -> None:
    n = entry["n"]
    product = 1
    distinct = set()
    for prime_string, exponent in entry["factorization_n_minus_1"].items():
        prime = int(prime_string)
        if not trial_is_prime(prime):
            raise AssertionError(f"nonprime factor {prime} in n-1 certificate")
        product *= prime ** exponent
        distinct.add(prime)
    if product != n - 1:
        raise AssertionError(f"incomplete n-1 factorization for {n}")
    witnesses = {item["prime_factor"]: item["base"] for item in entry["witnesses"]}
    if set(witnesses) != distinct:
        raise AssertionError(f"missing Pocklington witness for {n}")
    for prime in distinct:
        base = witnesses[prime]
        if pow(base, n - 1, n) != 1:
            raise AssertionError(f"Fermat condition fails for {(n, prime, base)}")
        if math.gcd(pow(base, (n - 1) // prime, n) - 1, n) != 1:
            raise AssertionError(f"gcd condition fails for {(n, prime, base)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--certificate", type=Path, required=True)
    parser.add_argument("--pocklington", type=Path, required=True)
    parser.add_argument("--negative-pdf", type=Path, required=True)
    parser.add_argument("--positive-pdf", type=Path, required=True)
    args = parser.parse_args()

    certificate_bytes = args.certificate.read_bytes()
    certificate = json.loads(certificate_bytes)
    pocklington_bytes = args.pocklington.read_bytes()
    pocklington = json.loads(pocklington_bytes)
    if certificate.get("schema") != "prime-cube-square-mordell-filter-v1":
        raise ValueError("unsupported filter certificate schema")
    if pocklington.get("schema") != "pocklington-incumbent-v1":
        raise ValueError("unsupported Pocklington certificate schema")

    file_specs = [
        ("negative_pdf", args.negative_pdf, -1),
        ("positive_pdf", args.positive_pdf, 1),
    ]
    all_points = []
    extraction_digests = {}
    for label, path, sign in file_specs:
        expected = certificate["upstream"][label]
        if digest_path(path) != expected["sha256"]:
            raise ValueError(f"PDF digest mismatch for {path}")
        raw = raw_pdf_text(path)
        extraction_digests[label] = digest_bytes(raw.encode("utf-8"))
        points, stats = parse_table(raw, sign)
        for field in ("records", "points", "first_k", "last_k", "maximum_abs_k_present"):
            if stats[field] != expected[field]:
                raise AssertionError(f"{label} field {field} disagrees with certificate")
        all_points.extend(points)

    bounds = certificate["bounds"]
    bounded = [row for row in all_points if abs(row[0]) <= bounds["maximum_abs_k"]]
    relevant_signed = [
        row for row in bounded
        if bounds["minimum_x"] <= row[1] <= bounds["maximum_x"]
    ]
    relevant = sorted({(k, x, abs(y)) for k, x, y in relevant_signed})
    classifications = [classify(*row) for row in relevant]
    if classifications != certificate["relevant_points"]:
        raise AssertionError("independent classification differs from discovery certificate")
    both_prime = [row for row in classifications if row["status"] == "both_prime"]
    if both_prime != certificate["both_prime_points"]:
        raise AssertionError("both-prime list differs from discovery certificate")
    expected_counts = {
        "signed_points_with_abs_k_at_most_bound": len(bounded),
        "signed_points_in_x_range": len(relevant_signed),
        "unique_points_after_y_sign_quotient": len(relevant),
        "unique_x_prime_points": sum(row["status"] != "x_composite" for row in classifications),
        "unique_both_prime_points": len(both_prime),
    }
    if expected_counts != certificate["filter_counts"]:
        raise AssertionError("filter counts disagree")
    if both_prime != [{"k": -49600, "status": "both_prime", "x": 1587809, "y": 2000771023}]:
        raise AssertionError("unexpected final both-prime list")

    for entry in pocklington["entries"]:
        verify_pocklington(entry)
    p = 1_587_809
    q = 2_000_771_023
    if {entry["n"] for entry in pocklington["entries"]} != {p, q}:
        raise AssertionError("Pocklington certificate covers the wrong integers")
    if p**3 - q**2 != 49_600:
        raise AssertionError("incumbent gap identity fails")
    if math.isqrt(p**3) != q:
        raise AssertionError("incumbent q is not floor(sqrt(p^3))")

    print(json.dumps({
        "status": "VERIFIED",
        "minimum": 49_600,
        "attaining_pair": [p, q],
        "certificate_sha256": digest_bytes(certificate_bytes),
        "pocklington_sha256": digest_bytes(pocklington_bytes),
        "raw_extraction_sha256": extraction_digests,
        "filter_counts": expected_counts,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
