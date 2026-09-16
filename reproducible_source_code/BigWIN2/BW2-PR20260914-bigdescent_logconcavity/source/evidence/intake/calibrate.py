"""Exact intake calibration; not a uniform proof or independent referee."""
import hashlib
import itertools
import json
import platform
import time
from pathlib import Path

START = time.perf_counter()
PATTERNS = tuple(itertools.permutations((1, 2, 3)))
INDEX = {p: i for i, p in enumerate(PATTERNS)}
FAMILIES = tuple((i,) for i in range(6)) + tuple(itertools.combinations(range(6), 2))
KEY = lambda f: ",".join("".join(map(str, PATTERNS[i])) for i in f)
counts = {}
failures = []
permutations_checked = 0
for n in range(9):
    rows = {f: [0] * (n + 1) for f in FAMILIES}
    triples = tuple(itertools.combinations(range(n), 3))
    for p in itertools.permutations(range(1, n + 1)):
        permutations_checked += 1
        mask = 0
        for i, j, k in triples:
            a, b, c = p[i], p[j], p[k]
            patt = (1 + (b < a) + (c < a), 1 + (a < b) + (c < b), 1 + (a < c) + (b < c))
            mask |= 1 << INDEX[patt]
            if mask == 63:
                break
        if mask == 63:
            continue
        bd = sum(p[i] > p[i + 1] + 1 for i in range(n - 1))
        for f in FAMILIES:
            if not any(mask & (1 << i) for i in f):
                rows[f][bd] += 1
    for f, row in rows.items():
        for k in range(1, n):
            if row[k] ** 2 < row[k - 1] * row[k + 1]:
                failures.append({"method": "direct", "n": n, "patterns": KEY(f), "k": k, "row": row})
    counts[str(n)] = {KEY(f): row for f, row in rows.items()}

def add_to(dst, src, factor=1, shift=0):
    while len(dst) < len(src) + shift:
        dst.append(0)
    for i, v in enumerate(src):
        dst[i + shift] += factor * v

num = {0: [1], 1: [-1], 2: [1, -1], 3: [-1, 2, -1]}
polys = []
determinants_checked = 0
for n in range(501):
    row = list(num.get(n, [0]))
    if n >= 1:
        add_to(row, polys[n - 1], 2)
    if n >= 2:
        add_to(row, polys[n - 2], -1)
        add_to(row, polys[n - 2], 1, 1)
    if n >= 3:
        add_to(row, polys[n - 3], -1, 1)
        add_to(row, polys[n - 3], 1, 2)
    while len(row) > 1 and row[-1] == 0:
        row.pop()
    assert all(v >= 0 for v in row)
    if n:
        assert sum(row) == 2 ** (n - 1)
    for k in range(1, len(row) - 1):
        determinants_checked += 1
        if row[k] ** 2 < row[k - 1] * row[k + 1]:
            failures.append({"method": "source_rational_gf", "n": n, "k": k, "left": row[k] ** 2, "right": row[k - 1] * row[k + 1]})
    polys.append(row)

for n in range(9):
    for key in ("123,132", "123,213", "132,213"):
        direct = counts[str(n)][key][:]
        while len(direct) > 1 and direct[-1] == 0:
            direct.pop()
        assert direct == polys[n], (n, key, direct, polys[n])

binary_words_checked = 0
for n in range(1, 15):
    row = [0] * (n + 1)
    for prefix in itertools.product((0, 1), repeat=n - 1):
        w = prefix + (1,)
        binary_words_checked += 1
        bd = sum(w[i:i + 2] == (1, 0) for i in range(n - 1))
        bd += sum(w[i:i + 3] == (0, 1, 1) for i in range(n - 2))
        row[bd] += 1
    while len(row) > 1 and row[-1] == 0:
        row.pop()
    assert row == polys[n], (n, row, polys[n])

out = {
    "arithmetic": "exact Python integers",
    "python": platform.python_version(),
    "source_url": "https://link.springer.com/article/10.1007/s00026-026-00805-1",
    "target": "Conjecture4.6, all 21 singleton/doubleton pattern sets in S3",
    "direct_permutation_range": "0<=n<=8",
    "permutations_checked": permutations_checked,
    "pattern_families": len(FAMILIES),
    "direct_distribution_cases": len(counts) * len(FAMILIES),
    "direct_counts": counts,
    "exceptional_class": ["123,132", "123,213", "132,213"],
    "gf_range": "0<=n<=500",
    "gf_coefficients": "Theorem3.5 rational generating function; integer coefficient extraction",
    "gf_internal_logconcavity_tests": determinants_checked,
    "binary_range": "1<=n<=14, all words ending in1",
    "binary_words_checked": binary_words_checked,
    "binary_statistic": "occurrences10 plus occurrences011",
    "gf_binary_and_direct_consistent": True,
    "failures": failures,
    "seed": None,
    "randomness": "none; exhaustive bounded loops",
    "seconds": time.perf_counter() - START,
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "uniform_proof": False,
    "independent_referee": False,
    "qualification": "Finite calibration only. No claim for n outside stated ranges or real-rootedness."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in out.items() if k != "direct_counts"}, ensure_ascii=False))
