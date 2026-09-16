#!/usr/bin/env python3
"""Independent exact verifier for serialized divisors of recurrence terms."""

import hashlib
import json
import pathlib
import sys


def is_prime_trial(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: verify_factors.py CERTIFICATE.json")
    path = pathlib.Path(sys.argv[1])
    raw = path.read_bytes()
    data = json.loads(raw)
    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        raise SystemExit("FAIL: entries must be a nonempty list")
    checked = []
    for entry in entries:
        n, p = entry.get("n"), entry.get("prime_divisor")
        if not isinstance(n, int) or not isinstance(p, int) or n < 5:
            raise SystemExit("FAIL: malformed entry")
        if not is_prime_trial(p):
            raise SystemExit(f"FAIL: claimed divisor {p} is not prime")
        x = 1
        for _ in range(n):
            x = (x * x + 2) % p
        if x != 0:
            raise SystemExit(f"FAIL: {p} does not divide a_{n}")
        # Establish properness independently, stopping the exact monotone
        # recurrence as soon as its value exceeds p.
        y = 1
        for _ in range(n):
            y = y * y + 2
            if y > p:
                break
        if y <= p:
            raise SystemExit(f"FAIL: proper-divisor bound absent for {p}")
        checked.append([n, p])
    code_hash = hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()
    input_hash = hashlib.sha256(raw).hexdigest()
    print(json.dumps({"status": "PASS", "checked": checked,
                      "input_sha256": input_hash, "verifier_sha256": code_hash},
                     sort_keys=True))


if __name__ == "__main__":
    main()
