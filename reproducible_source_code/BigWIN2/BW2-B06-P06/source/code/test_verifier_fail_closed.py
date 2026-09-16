#!/usr/bin/env python3
"""Deliberate corruption tests for the independent certificate parser."""

from __future__ import annotations

import hashlib
import json
import shutil
import tempfile
from pathlib import Path

from verify_radius_certificate import verify


def rewrite_header(header_path: Path, **changes: object) -> None:
    header = json.loads(header_path.read_text(encoding="utf-8"))
    header.update(changes)
    header_path.write_text(json.dumps(header, indent=2) + "\n", encoding="utf-8")


def expect_failure(label: str, action, expected_fragment: str) -> dict[str, str]:
    try:
        action()
    except (ValueError, json.JSONDecodeError) as error:
        message = str(error)
        if expected_fragment not in message:
            raise AssertionError(
                f"{label}: expected {expected_fragment!r}, received {message!r}"
            ) from error
        return {"test": label, "status": "REJECTED", "reason": message}
    raise AssertionError(f"{label}: malformed certificate was accepted")


def main() -> None:
    project = Path(__file__).resolve().parent.parent
    source = project / "certificates" / "test_v2"
    source_header = source / "p4_radius_certificate.json"
    source_payload = source / "p4_radius_certificate.bin"
    source_exceptions = source / "p4_fractional_exceptions.json"
    baseline = verify(source_header, source_payload)
    results: list[dict[str, str]] = []

    with tempfile.TemporaryDirectory(prefix="path_hl_corruption_") as temporary:
        root = Path(temporary)

        def fresh() -> tuple[Path, Path, Path]:
            header = root / "p4_radius_certificate.json"
            payload = root / "p4_radius_certificate.bin"
            exceptions = root / "p4_fractional_exceptions.json"
            shutil.copyfile(source_header, header)
            shutil.copyfile(source_payload, payload)
            shutil.copyfile(source_exceptions, exceptions)
            return header, payload, exceptions

        header, payload, _ = fresh()
        altered = bytearray(payload.read_bytes())
        altered[0] ^= 1
        payload.write_bytes(altered)
        results.append(expect_failure(
            "digest_mismatch",
            lambda: verify(header, payload),
            "payload digest differs",
        ))

        header, payload, _ = fresh()
        altered = bytearray(payload.read_bytes())
        altered[0] = 255
        payload.write_bytes(altered)
        rewrite_header(header, payload_sha256=hashlib.sha256(altered).hexdigest())
        results.append(expect_failure(
            "illegal_radius_with_matching_digest",
            lambda: verify(header, payload),
            "radius is invalid",
        ))

        header, payload, _ = fresh()
        altered = payload.read_bytes()[:-1]
        payload.write_bytes(altered)
        rewrite_header(
            header,
            payload_bytes=len(altered),
            payload_sha256=hashlib.sha256(altered).hexdigest(),
        )
        results.append(expect_failure(
            "truncated_payload_with_matching_digest",
            lambda: verify(header, payload),
            "truncated payload",
        ))

        header, payload, _ = fresh()
        altered = payload.read_bytes() + b"\x00"
        payload.write_bytes(altered)
        rewrite_header(
            header,
            payload_bytes=len(altered),
            payload_sha256=hashlib.sha256(altered).hexdigest(),
        )
        results.append(expect_failure(
            "trailing_payload_with_matching_digest",
            lambda: verify(header, payload),
            "trailing payload bytes",
        ))

        header, payload, exceptions = fresh()
        malformed = {
            "schema": "path-hl-fractional-exceptions-v1",
            "n": 4,
            "exceptions": [{
                "chamber_index": 0,
                "negative_mixtures": [{
                    "vertex": 0,
                    "weights": [[0, 1, 2]],
                }],
            }],
        }
        raw = (json.dumps(malformed, separators=(",", ":")) + "\n").encode()
        exceptions.write_bytes(raw)
        rewrite_header(
            header,
            fractional_exception_count=1,
            exceptions_bytes=len(raw),
            exceptions_sha256=hashlib.sha256(raw).hexdigest(),
        )
        results.append(expect_failure(
            "wrong_fractional_mass_with_matching_digest",
            lambda: verify(header, payload),
            "wrong total weight",
        ))

    print(json.dumps({
        "baseline": baseline["status"],
        "corruption_tests": results,
        "status": "PASS",
    }, indent=2))


if __name__ == "__main__":
    main()
