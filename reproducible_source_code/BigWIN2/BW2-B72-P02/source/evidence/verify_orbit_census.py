#!/usr/bin/env python3
"""Stand-alone verifier for the win-00072-p02 orbit certificate.

The verifier does not import orbit_census.py.  It represents words as literal
digit strings and implements conjugation, decimation, shift, and phase as four
separate operations before independently reconstructing and sorting the domain.
"""

from __future__ import annotations

import gzip
import hashlib
import json
import math
from pathlib import Path


N = 34
A = "2202202000022020222202000220200020"
B = "1133303133112311101113211331303331"
UNITS = [k for k in range(N) if math.gcd(k, N) == 1]
P = {"0": 1, "1": 1, "2": -1, "3": -1}
Q = {"0": 1, "1": -1, "2": -1, "3": 1}


def conjugate(word: str) -> str:
    return word.translate(str.maketrans("0123", "0321"))


def decimate(word: str, k: int) -> str:
    inverse = pow(k, -1, N)
    return "".join(word[(j * inverse) % N] for j in range(N))


def shift(word: str, r: int) -> str:
    return "".join(word[(j - r) % N] for j in range(N))


def phase(word: str, alpha: int) -> str:
    return "".join(str((int(symbol) + alpha) % 4) for symbol in word)


def image(word: str, alpha: int, r: int, k: int, epsilon: int) -> str:
    base = conjugate(word) if epsilon else word
    return phase(shift(decimate(base, k), r), alpha)


def expected_failure(encoded_pair: str) -> dict[str, int | str]:
    first, second = encoded_pair.split("|")
    rows = (
        ("first.p", [P[x] for x in first]),
        ("first.q", [Q[x] for x in first]),
        ("second.p", [P[x] for x in second]),
        ("second.q", [Q[x] for x in second]),
    )
    for label, row in rows:
        for j in range(N):
            reflected_j = (-j) % N
            if row[j] != row[reflected_j]:
                return {
                    "j": j,
                    "label": label,
                    "reflected_j": reflected_j,
                    "reflected_value": row[reflected_j],
                    "value": row[j],
                }
    raise AssertionError(f"fully reversible image encountered: {encoded_pair}")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    summary_path = root / "evidence" / "orbit_census_output.json"
    archive_path = root / "evidence" / "orbit_failure_witnesses.jsonl.gz"
    output_path = root / "evidence" / "orbit_census_verification.json"
    summary = json.loads(summary_path.read_text(encoding="utf-8"))

    images: set[str] = set()
    tuples = 0
    for alpha in range(4):
        for beta in range(4):
            for r in range(N):
                for t in range(N):
                    for k in UNITS:
                        for epsilon in range(2):
                            left = image(A, alpha, r, k, epsilon)
                            right = image(B, beta, t, k, epsilon)
                            for exchange in range(2):
                                encoded = left + "|" + right if exchange == 0 else right + "|" + left
                                images.add(encoded)
                                tuples += 1

    assert tuples == 1_183_744
    ordered = sorted(images)
    assert len(ordered) == tuples
    orbit_hash = hashlib.sha256()
    for encoded in ordered:
        orbit_hash.update((encoded + "\n").encode("ascii"))
    orbit_sha256 = orbit_hash.hexdigest()
    assert orbit_sha256 == summary["canonical_orbit_sha256"]

    uncompressed_hash = hashlib.sha256()
    checked_records = 0
    with gzip.open(archive_path, "rb") as stream:
        header_line = stream.readline()
        uncompressed_hash.update(header_line)
        header = json.loads(header_line)
        assert header["metadata"]["orbit_sha256"] == orbit_sha256
        assert header["metadata"]["image_count"] == len(ordered)
        for ordinal, encoded in enumerate(ordered):
            line = stream.readline()
            assert line
            uncompressed_hash.update(line)
            record = json.loads(line)
            assert record == {
                "image": encoded,
                "ordinal": ordinal,
                "witness": expected_failure(encoded),
            }
            checked_records += 1
        assert stream.readline() == b""

    uncompressed_sha256 = uncompressed_hash.hexdigest()
    compressed_sha256 = sha256_file(archive_path)
    assert uncompressed_sha256 == summary["witness_archive"]["uncompressed_jsonl_sha256"]
    assert compressed_sha256 == summary["witness_archive"]["compressed_sha256"]
    assert checked_records == summary["witness_archive"]["records"]

    result = {
        "all_checks_passed": True,
        "canonical_orbit_sha256": orbit_sha256,
        "distinct_ordered_images": len(ordered),
        "implementation_separation": "does not import orbit_census.py; literal string operations are composed separately",
        "parameter_tuples_reconstructed": tuples,
        "source_sha256": hashlib.sha256((root / "source.md").read_bytes()).hexdigest(),
        "witness_archive_compressed_sha256": compressed_sha256,
        "witness_records_recomputed": checked_records,
        "witness_stream_uncompressed_sha256": uncompressed_sha256,
    }
    output_path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
