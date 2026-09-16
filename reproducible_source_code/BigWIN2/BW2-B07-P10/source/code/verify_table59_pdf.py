#!/usr/bin/env python3
"""Check the serialized 121-entry histogram against the archived Table 59 PDF."""

import json
import pathlib
import re
import subprocess
import sys


def main(pdf_path: str, json_path: str) -> None:
    try:
        text = subprocess.run(
            ["pdftotext", "-layout", pdf_path, "-"],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        ).stdout
        expected = json.loads(pathlib.Path(json_path).read_text(encoding="utf-8"))[
            "u16_by_number_of_strict_relations"
        ]
    except (OSError, subprocess.CalledProcessError, ValueError, KeyError) as exc:
        raise SystemExit(f"VERIFY FAILED: unable to parse inputs: {exc}")

    found: dict[int, int] = {}
    active = False
    for line in text.splitlines():
        fields = re.findall(r"[0-9]+", line)
        if fields[:3] == ["0", "1", "41"]:
            active = True
        if active and "Table 59:" in line:
            break
        if active and len(fields) in (2, 4, 6):
            for offset in range(0, len(fields), 2):
                relation, count = map(int, fields[offset : offset + 2])
                found[relation] = count
    if set(found) != set(range(121)):
        raise SystemExit(f"VERIFY FAILED: parsed relation keys {sorted(found)}")
    got = [found[q] for q in range(121)]
    if got != expected:
        raise SystemExit("VERIFY FAILED: serialized histogram differs from archived Table 59")
    print("VERIFY PASSED: all 121 serialized entries match Brinkmann--McKay Table 59")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("VERIFY FAILED: usage: verify_table59_pdf.py PAPER.pdf CERTIFICATE.json")
    main(sys.argv[1], sys.argv[2])
