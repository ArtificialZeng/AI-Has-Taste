"""Exact, bounded checks; run with python3 evidence/triage_check.py."""
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json
import math


def compositions(n):
    if n == 0:
        yield ()
    else:
        for first in range(1, n + 1):
            for tail in compositions(n - first):
                yield (first,) + tail


def encode(parts):
    result = []
    offset = 0
    for d in parts:
        result.extend(offset + x for x in list(range(2, d + 1)) + [1])
        offset += d
    return tuple(result)


def cube(p):
    return tuple(p[p[p[i] - 1] - 1] for i in range(len(p)))


def avoids_base(p):
    # 312 and 321 are exactly the triples whose first entry is largest.
    return not any(p[i] > max(p[j], p[k])
                   for i, j, k in combinations(range(len(p)), 3))


def avoids_2143(p):
    return not any(p[j] < p[i] < p[l] < p[k]
                   for i, j, k, l in combinations(range(len(p)), 4))


def formal_coefficients(N):
    # A=1/(1-z-z^3); B=A+(z^2+z^4/(1-z))*A^2.
    a = [0] * (N + 1)
    a[0] = 1
    for n in range(1, N + 1):
        a[n] = a[n - 1] + (a[n - 3] if n >= 3 else 0)
    a2 = [sum(a[i] * a[n - i] for i in range(n + 1))
          for n in range(N + 1)]
    return [a[n] + sum(a2[n - d] for d in range(1, n + 1)
                      if d not in (1, 3)) for n in range(N + 1)]


def main():
    rows = []
    gf = formal_coefficients(12)
    for n in range(13):
        parts = list(compositions(n))
        encoded = [encode(d) for d in parts]
        assert len(set(encoded)) == len(parts)
        c = 0
        b = 0
        for d, p in zip(parts, encoded):
            assert avoids_base(p), (n, d, p)
            expected = sum(x not in (1, 3) for x in d) <= 1
            actual = avoids_2143(cube(p))
            assert expected == actual, (n, d, p, cube(p))
            c += expected
            b += actual
        assert b == c == gf[n]
        row = {"n": n, "compositions_checked": len(parts),
               "cube_avoiders": b, "restricted_compositions": c,
               "generating_function_coefficient": gf[n]}
        if n <= 8:
            base = [p for p in permutations(range(1, n + 1))
                    if avoids_base(p)]
            assert set(base) == set(encoded)
            brute_b = sum(avoids_2143(cube(p)) for p in base)
            assert brute_b == b
            row.update(all_permutations_checked=math.factorial(n),
                       brute_force_cube_avoiders=brute_b)
        rows.append(row)
    for d in range(1, 41):
        q = cube(encode((d,)))
        expected = tuple(1 + ((i + 3) % d) for i in range(d))
        assert q == expected
        assert (q == tuple(range(1, d + 1))) == (d in (1, 3))
        assert avoids_2143(q)
    result = {
        "job_id": "newwin-00001-p07-triage-19444324da60",
        "kind": "exact_finite_observation",
        "source_sha256": hashlib.sha256(Path("source.md").read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "rows": rows,
        "single_block_sizes_checked": [1, 40],
        "counterexamples_found": 0,
        "limitations": "Finite checks do not establish the all-n assertion or novelty."
    }
    out = Path("evidence/triage_check.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
