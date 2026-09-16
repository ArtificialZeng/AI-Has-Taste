#!/usr/bin/env python3
"""Independent exact orbit census for win-00072-p02.

This program intentionally does not import the intake checker.  Quaternary
roots are represented by their exponents modulo 4, so every calculation is
integer and exact.  It enumerates the displayed seven-parameter domain,
canonically sorts distinct ordered images, and emits one checked Gray-row
reflection-failure witness for every image.
"""

from __future__ import annotations

from collections import Counter
import gzip
import hashlib
import json
import math
from pathlib import Path


JOB_ID = "win-00072-p02-research-d9e9a040870f"
N = 34
A_TEXT = "2202202000022020222202000220200020"
B_TEXT = "1133303133112311101113211331303331"
UNITS = tuple(k for k in range(N) if math.gcd(k, N) == 1)

# For z=i**d, these are Re(z)+Im(z) and Re(z)-Im(z).
GRAY_P = (1, 1, -1, -1)
GRAY_Q = (1, -1, -1, 1)


def transformed(word: bytes, phase: int, shift: int, k: int, epsilon: int) -> bytes:
    """Return phase*c_shift*d_k(word^epsilon), in the frozen order."""
    inverse = pow(k, -1, N)
    return bytes(
        (phase + ((-word[((j - shift) * inverse) % N]) if epsilon else
                  word[((j - shift) * inverse) % N])) % 4
        for j in range(N)
    )


def gaussian_mul(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def gaussian_conj(z: tuple[int, int]) -> tuple[int, int]:
    return z[0], -z[1]


ROOT = ((1, 0), (0, 1), (-1, 0), (0, -1))


def paf(word: bytes, lag: int) -> tuple[int, int]:
    real = 0
    imag = 0
    for j, digit in enumerate(word):
        term = gaussian_mul(ROOT[digit], gaussian_conj(ROOT[word[(j + lag) % N]]))
        real += term[0]
        imag += term[1]
    return real, imag


def audit_qlp_and_generators(a: bytes, b: bytes) -> dict[str, int | bool]:
    """Exhaustively check the exact PAF identities used in the paper proof."""
    base_a = tuple(paf(a, h) for h in range(N))
    base_b = tuple(paf(b, h) for h in range(N))
    assert all(
        (base_a[h][0] + base_b[h][0], base_a[h][1] + base_b[h][1]) == (-2, 0)
        for h in range(1, N)
    )

    phase_checks = 0
    shift_checks = 0
    decimation_checks = 0
    conjugation_checks = 0
    for word, base in ((a, base_a), (b, base_b)):
        for phase in range(4):
            image = transformed(word, phase, 0, 1, 0)
            for h in range(N):
                assert paf(image, h) == base[h]
                phase_checks += 1
        for shift in range(N):
            image = transformed(word, 0, shift, 1, 0)
            for h in range(N):
                assert paf(image, h) == base[h]
                shift_checks += 1
        for k in UNITS:
            image = transformed(word, 0, 0, k, 0)
            inverse = pow(k, -1, N)
            for h in range(N):
                assert paf(image, h) == base[(h * inverse) % N]
                decimation_checks += 1
        image = transformed(word, 0, 0, 1, 1)
        for h in range(N):
            expected = gaussian_conj(base[h])
            assert paf(image, h) == expected
            conjugation_checks += 1

    # Exhaust all pairs of alphabet symbols: equality of a quaternary symbol is
    # equivalent to equality of both Gray symbols.
    gray_symbol_checks = 0
    for x in range(4):
        for y in range(4):
            assert (x == y) == (GRAY_P[x] == GRAY_P[y] and GRAY_Q[x] == GRAY_Q[y])
            gray_symbol_checks += 1

    return {
        "qlp_nonzero_lags": N - 1,
        "phase_paf_identity_checks": phase_checks,
        "shift_paf_identity_checks": shift_checks,
        "decimation_paf_identity_checks": decimation_checks,
        "conjugation_paf_identity_checks": conjugation_checks,
        "gray_symbol_bijection_checks": gray_symbol_checks,
        "exchange_identity_checked": True,
    }


def ascii_pair(image: bytes) -> bytes:
    return bytes(d + 48 for d in image[:N]) + b"|" + bytes(d + 48 for d in image[N:])


def first_failure(image: bytes) -> tuple[str, int, int, int] | None:
    rows = (
        ("first.p", tuple(GRAY_P[d] for d in image[:N])),
        ("first.q", tuple(GRAY_Q[d] for d in image[:N])),
        ("second.p", tuple(GRAY_P[d] for d in image[N:])),
        ("second.q", tuple(GRAY_Q[d] for d in image[N:])),
    )
    for label, row in rows:
        for j in range(N):
            reflected = (-j) % N
            if row[j] != row[reflected]:
                return label, j, row[j], row[reflected]
    return None


def json_line(record: dict[str, object]) -> bytes:
    return (json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n").encode("ascii")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    project = Path(__file__).resolve().parents[1]
    summary_path = project / "evidence" / "orbit_census_output.json"
    witnesses_path = project / "evidence" / "orbit_failure_witnesses.jsonl.gz"

    a = bytes(int(c) for c in A_TEXT)
    b = bytes(int(c) for c in B_TEXT)
    assert len(a) == len(b) == N
    source_sha256 = hashlib.sha256((project / "source.md").read_bytes()).hexdigest()
    identity_audit = audit_qlp_and_generators(a, b)

    # An independent lookup table is only a speed optimization.  The nested
    # loops below still visit each displayed parameter tuple, including e.
    a_images = {
        (alpha, r, k, epsilon): transformed(a, alpha, r, k, epsilon)
        for alpha in range(4)
        for r in range(N)
        for k in UNITS
        for epsilon in (0, 1)
    }
    b_images = {
        (beta, t, k, epsilon): transformed(b, beta, t, k, epsilon)
        for beta in range(4)
        for t in range(N)
        for k in UNITS
        for epsilon in (0, 1)
    }

    multiplicity: Counter[bytes] = Counter()
    parameter_tuples = 0
    for alpha in range(4):
        for beta in range(4):
            for r in range(N):
                for t in range(N):
                    for k in UNITS:
                        for epsilon in (0, 1):
                            first = a_images[(alpha, r, k, epsilon)]
                            second = b_images[(beta, t, k, epsilon)]
                            for exchange in (0, 1):
                                image = first + second if exchange == 0 else second + first
                                multiplicity[image] += 1
                                parameter_tuples += 1

    expected_domain = 4 * 4 * N * N * len(UNITS) * 2 * 2
    assert expected_domain == 1_183_744
    assert parameter_tuples == expected_domain
    assert sum(multiplicity.values()) == expected_domain

    canonical_images = sorted(multiplicity)
    orbit_digest = hashlib.sha256()
    for image in canonical_images:
        orbit_digest.update(ascii_pair(image) + b"\n")
    orbit_sha256 = orbit_digest.hexdigest()

    witness_stream_digest = hashlib.sha256()
    label_counts: Counter[str] = Counter()
    failure_index_counts: Counter[int] = Counter()
    fully_reversible = 0
    header = {
        "format": "win-00072-p02 canonical orbit failure witnesses v1",
        "canonical_order": "lexicographic order of fixed-width ASCII first_word|second_word",
        "failure_rule": "first failing row in first.p,first.q,second.p,second.q order; then least j in 0..33",
        "image_count": len(canonical_images),
        "job_id": JOB_ID,
        "orbit_sha256": orbit_sha256,
    }
    with witnesses_path.open("wb") as raw:
        # Empty filename and mtime=0 make the gzip bytes reproducible.
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0) as zipped:
            line = json_line({"metadata": header})
            zipped.write(line)
            witness_stream_digest.update(line)
            for ordinal, image in enumerate(canonical_images):
                failure = first_failure(image)
                if failure is None:
                    fully_reversible += 1
                    record = {
                        "fully_reversible": True,
                        "image": ascii_pair(image).decode("ascii"),
                        "ordinal": ordinal,
                    }
                else:
                    label, j, value, reflected_value = failure
                    label_counts[label] += 1
                    failure_index_counts[j] += 1
                    record = {
                        "image": ascii_pair(image).decode("ascii"),
                        "ordinal": ordinal,
                        "witness": {
                            "j": j,
                            "label": label,
                            "reflected_j": (-j) % N,
                            "reflected_value": reflected_value,
                            "value": value,
                        },
                    }
                line = json_line(record)
                zipped.write(line)
                witness_stream_digest.update(line)

    assert fully_reversible == 0
    assert sum(label_counts.values()) == len(canonical_images)

    multiplicity_distribution = Counter(multiplicity.values())
    summary = {
        "canonical_encoding": "each ordered image is 34 ASCII digits, '|', 34 ASCII digits, newline; images lexicographically sorted",
        "canonical_orbit_sha256": orbit_sha256,
        "distinct_ordered_images": len(canonical_images),
        "fully_gray_reversible_images": fully_reversible,
        "identity_audit": identity_audit,
        "job_id": JOB_ID,
        "multiplicity_distribution": {
            str(value): count for value, count in sorted(multiplicity_distribution.items())
        },
        "parameter_domain": {
            "alpha": 4,
            "beta": 4,
            "r": N,
            "t": N,
            "units_k": list(UNITS),
            "epsilon": 2,
            "exchange_e": 2,
            "tuples_enumerated": parameter_tuples,
        },
        "source_sha256": source_sha256,
        "witness_archive": {
            "compressed_bytes": witnesses_path.stat().st_size,
            "compressed_sha256": file_sha256(witnesses_path),
            "failure_index_counts": {
                str(index): count for index, count in sorted(failure_index_counts.items())
            },
            "label_counts": dict(sorted(label_counts.items())),
            "records": len(canonical_images),
            "uncompressed_jsonl_sha256": witness_stream_digest.hexdigest(),
        },
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
