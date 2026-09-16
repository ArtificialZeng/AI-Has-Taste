"""Exact checks of the proposed transfer and original permutation reduction.

Standard library only; imports no prior project arithmetic. Run from any cwd.
Finite checks supplement, and do not replace, protected-minimum-proof.md.
"""
from bisect import bisect_right
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json
import platform
import time

ROOT = Path(__file__).resolve().parents[2]
JOB = "primary-20260913-qdescent-logconcavity-research-8293ab93d85b"
SOURCE_SHA = "09b28e35bf37a42405472803e963d8cd37dce27edee55c075e7689eab2781fcb"


def add(*polys):
    z = defaultdict(int)
    for p in polys:
        for e, c in p.items():
            z[e] += c
    return {e: c for e, c in z.items() if c}


def negative(p):
    return {e: -c for e, c in p.items()}


def shift(p, d):
    return {e + d: c for e, c in p.items()}


def mul(p, v):
    z = defaultdict(int)
    for e, c in p.items():
        for f, d in v.items():
            z[e + f] += c * d
    return {e: c for e, c in z.items() if c}


@lru_cache(None)
def gaussian(n, k):
    if not 0 <= k <= n:
        return {}
    if k == 0 or k == n:
        return {0: 1}
    return add(gaussian(n - 1, k), shift(gaussian(n - 1, k - 1), n - k))


@lru_cache(None)
def H(m, k, r):
    if not 1 <= k <= m:
        return {}
    # Direct subset enumeration, not the Gaussian difference formula.
    return dict(Counter(sum(U) - k * (k + 1) // 2
                        for U in combinations(range(1, m + 1), k)
                        if U[0] <= r))


@lru_cache(None)
def K(m, k, r):
    if not 1 <= k <= m:
        return {}
    return shift(add(gaussian(m, k), negative(gaussian(m - r, k))), k * k)


def transfer(A, B, delta, m, protect=True):
    left = {a + delta for a in A}
    right = set(B)
    if protect:
        right.remove(min(B))
    current = sum(a <= delta for a in left) - sum(b <= delta for b in right)
    values = {delta: current}
    for t in range(delta + 1, m + delta + 1):
        current += int(t in left) - int(t in right)
        values[t] = current
    high = max(values.values())
    last = max(t for t, v in values.items() if v == high)
    e = last + 1
    assert delta < e <= m and e in right and e not in left
    C = tuple(sorted(set(A) | {e - delta}))
    D = tuple(sorted(set(B) - {e}))
    return C, D, e


def recover(C, D, delta, m):
    # Independent prefix counts via binary search in sorted sets.
    left = sorted(c + delta for c in C)
    right = sorted(set(D) - {min(D)})
    values = [(bisect_right(left, t) - bisect_right(right, t), t)
              for t in range(delta, m + delta + 1)]
    high = max(v for v, t in values)
    e = min(t for v, t in values if v == high)
    return (tuple(c for c in C if c != e - delta),
            tuple(sorted(set(D) | {e})), e)


def desc(p):
    return tuple(t for t in range(1, len(p)) if p[t - 1] > p[t])


def inv(p):
    return sum(a > b for t, a in enumerate(p) for b in p[t + 1:])


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def main():
    start = time.monotonic()
    assert sha("source.md") == SOURCE_SHA
    transfer_counts = {}
    for m in range(1, 11):
        count = 0
        for i in range(1, m):
            for j in range(i, m):
                delta = j - i + 1
                images = set()
                for A in combinations(range(1, m + 1), i - 1):
                    for B in combinations(range(1, m + 1), j + 1):
                        C, D, e = transfer(A, B, delta, m)
                        assert len(C) == i and len(D) == j
                        assert len(set(C)) == i and len(set(D)) == j
                        assert all(1 <= t <= m for t in C + D)
                        assert min(D) == min(B)
                        assert not A or min(C) <= min(A)
                        assert sum(C) + sum(D) == sum(A) + sum(B) - delta
                        assert (sum(C) - i * (i + 1) // 2
                                + sum(D) - j * (j + 1) // 2
                                == sum(A) - (i - 1) * i // 2
                                + sum(B) - (j + 1) * (j + 2) // 2)
                        assert recover(C, D, delta, m) == (A, B, e)
                        assert (C, D) not in images
                        images.add((C, D))
                        count += 1
        transfer_counts[str(m)] = count
        print(f"transfer m={m}: {count}", flush=True)

    # Compare different definitions, then test directed inequalities on a new
    # range beyond the exploratory directed check m<=9.
    kernel_identity_count = 0
    directed = {"strict": 0, "diagonal": 0}
    directed_by_m = {}
    for m in range(1, 13):
        for k in range(1, m + 1):
            for r in range(1, m + 1):
                h = H(m, k, r)
                assert h == add(gaussian(m, k),
                                negative(shift(gaussian(m - r, k), k * r)))
                assert {m * k - e: c for e, c in h.items()} == K(m, k, r)
                assert h and min(h) == 0 and all(c > 0 for c in h.values())
                kernel_identity_count += 1
        local = {"strict": 0, "diagonal": 0}
        for i in range(1, m + 1):
            for j in range(i, m + 1):
                for r in range(1, m + 1):
                    for s in range(1, m + 1):
                        z = add(mul(H(m, i, r), H(m, j, s)),
                                negative(mul(H(m, i - 1, r), H(m, j + 1, s))))
                        assert all(c >= 0 for c in z.values()), (m, i, j, r, s, z)
                        case = "strict" if i < j else "diagonal"
                        local[case] += 1
                        directed[case] += 1
        directed_by_m[str(m)] = local
        print(f"directed m={m}: {local}", flush=True)

    # Enumerate the frozen original permutation definition for every S with
    # max S<=4. Separately reconstruct permutations from (sigma,U).
    direct_cases = reconstruction_count = permutation_count = 0
    for m in range(1, 5):
        x = {}
        for sigma in permutations(range(1, m + 1)):
            T = desc(sigma)
            x.setdefault(T, [Counter() for _ in range(m)])
            x[T][sigma[-1] - 1][inv(sigma)] += 1
            for k in range(1, m + 1):
                for U in combinations(range(1, m + 1), k):
                    if U[0] > sigma[-1]:
                        continue
                    pool = sorted(set(range(1, m + k + 1)) - set(U))
                    pi = tuple(pool[t - 1] for t in sigma) + U
                    assert desc(pi) == T + (m,)
                    assert set(range(m + 1, m + k + 1)) <= set(pi[:m])
                    cross = m * k - sum(U) + k * (k + 1) // 2
                    assert inv(pi) == inv(sigma) + cross
                    reconstruction_count += 1
        for k in range(1, m + 1):
            direct = {T: Counter() for T in x}
            for pi in permutations(range(1, m + k + 1)):
                permutation_count += 1
                S = desc(pi)
                if not S or S[-1] != m:
                    continue
                if not set(range(m + 1, m + k + 1)) <= set(pi[:m]):
                    continue
                direct[S[:-1]][inv(pi)] += 1
            for T, xr in x.items():
                reduced = add(*(mul(K(m, k, r), xr[r - 1]) for r in range(1, m + 1)))
                assert direct[T] == reduced and reduced
                direct_cases += 1

    A, B = (2,), (2, 3, 4)
    old = transfer(A, B, 1, 4, protect=False)
    new = transfer(A, B, 1, 4, protect=True)
    assert old == ((1, 2), (3, 4), 2)
    assert new == ((2, 3), (2, 3), 4)
    assert min(old[1]) > 2 and min(new[1]) <= 2
    witness_determinant = add(mul(H(4, 2, 2), H(4, 2, 2)),
                              negative(mul(H(4, 1, 2), H(4, 3, 2))))
    assert all(c >= 0 for c in witness_determinant.values())
    files = ["source.md", "evidence/external/gaetz-gao-1912.04933v2.html",
             "evidence/research/protected-minimum-proof.md",
             "evidence/research/protected-minimum-check.py"]
    result = {
        "job_id": JOB,
        "arithmetic": "exact integer polynomials and exhaustive finite sets; standard library only",
        "python": platform.python_version(),
        "transfer_range": "all 1<=i<=j<m<=10; all (i-1)-subsets A and (j+1)-subsets B of [m]",
        "transfer_checks_by_m": transfer_counts,
        "transfer_checks_total": sum(transfer_counts.values()),
        "transfer_properties": ["sizes and ground set", "distinct elements", "sum shift", "normalized weight",
                                "min D = min B", "min C <= min A when A nonempty",
                                "explicit inverse", "no collisions for fixed m,i,j"],
        "kernel_identity_range": "all 1<=k,r<=m<=12; subset H vs q-Pascal Gaussian difference vs reversed K",
        "kernel_identity_checks": kernel_identity_count,
        "directed_range": "all 1<=i<=j<=m<=12 and all ordered 1<=r,s<=m, including zero boundaries",
        "directed_checks": directed,
        "directed_checks_by_m": directed_by_m,
        "direct_permutation_range": "all nonempty S with max S<=4, and all 1<=k<=max S",
        "direct_a_cases": direct_cases,
        "permutations_enumerated": permutation_count,
        "sigma_U_reconstructions": reconstruction_count,
        "unmodified_map_obstruction": {
            "scope": "failure of the unmodified map to preserve a cutoff; not a negative determinant",
            "m": 4, "i": 2, "j": 2, "r": 2, "s": 2,
            "A": A, "B": B, "unmodified_output": old[:2], "protected_output": new[:2],
            "H_determinant_coefficients": dict(sorted(witness_determinant.items()))},
        "failures": [],
        "sha256": {p: sha(p) for p in files},
        "elapsed_seconds": time.monotonic() - start,
        "conclusion": "Finite checks passed; the uniform argument is in the proof artifact and requires fresh review."
    }
    assert result["sha256"]["source.md"] == SOURCE_SHA
    out = Path(__file__).with_suffix(".json")
    temp = out.with_suffix(".json.tmp")
    temp.write_text(json.dumps(result, indent=2) + "\n")
    temp.replace(out)
    print(json.dumps({"result": str(out.relative_to(ROOT)),
                      "transfer_checks": result["transfer_checks_total"],
                      "directed_checks": directed, "direct_a_cases": direct_cases,
                      "elapsed_seconds": result["elapsed_seconds"]}, indent=2))


if __name__ == "__main__":
    main()
