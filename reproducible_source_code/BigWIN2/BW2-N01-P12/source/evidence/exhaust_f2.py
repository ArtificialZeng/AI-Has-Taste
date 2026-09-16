"""Independent exhaustive binary tensor count by polynomial maximal minors.

Run: python3 evidence/exhaust_f2.py
Only integer/bit arithmetic; NumPy batches distinct matrices, without floats.
No permutation sum, augmented-matrix code, or symbolic certificate is imported.
"""
from itertools import permutations, product
from pathlib import Path
import json
import numpy as np


def rank(m):
    basis = [0, 0, 0]
    for r in range(4):
        v = (m >> (3*r)) & 7
        for c in (2, 1, 0):
            if v & (1 << c):
                if basis[c]:
                    v ^= basis[c]
                else:
                    basis[c] = v
                    break
    return sum(v != 0 for v in basis)


def pmul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
    return out


def pgcd(a, b):
    while b:
        r = a
        while r and r.bit_length() >= b.bit_length():
            r ^= b << (r.bit_length() - b.bit_length())
        a, b = b, r
    return a


def main():
    full = np.array([rank(m) == 3 for m in range(4096)], dtype=bool)
    matrices = np.flatnonzero(full).astype(np.uint32)
    assert len(matrices) == 2520
    bitpos = np.arange(12, dtype=np.uint32).reshape(4, 3)
    b_entries = ((matrices[:, None, None] >> bitpos) & 1).astype(np.uint8)
    triple = np.array([[[pmul(pmul(a, b), c) for c in range(4)]
                        for b in range(4)] for a in range(4)], dtype=np.uint8)
    gcd_table = np.array([[pgcd(a, b) for b in range(16)]
                          for a in range(16)], dtype=np.uint8)
    shapes = []
    for a, b, c, d, e in product(range(4), range(3), range(2), range(3), range(2)):
        if a < b or b < c or d < e or d > a or e > b:
            continue
        lam, mu = (a, b, c), (d, e, 0)
        masks = [sum(1 << (3*r+j) for j in range(3)
                     for r in range(4-sh[j], 4)) for sh in (lam, mu)]
        lengths = [4-j-lam[j] for j in range(3)] + [3-j-mu[j] for j in range(3)]
        expected = 512
        for n in lengths:
            expected *= (1 << n) - 1
        shapes.append(dict(lambda_=lam, mu=mu, masks=masks, actual=0, expected=expected))
    assert len(shapes) == 55
    perms = list(permutations(range(3)))
    total = rational = falsepos = 0
    witness = None
    for a_np in matrices:
        a = int(a_np)
        entry = ((a >> bitpos) & 1).astype(np.uint8) + 2*b_entries
        minors = []
        common = np.zeros(len(matrices), dtype=np.uint8)
        for deleted in range(4):
            rows = [r for r in range(4) if r != deleted]
            minor = np.zeros(len(matrices), dtype=np.uint8)
            for p in perms:
                minor ^= triple[entry[:, rows[0], p[0]],
                                entry[:, rows[1], p[1]],
                                entry[:, rows[2], p[2]]]
            minors.append(minor)
            common = gcd_table[common, minor]
        # B full-rank covers infinity; common gcd=1 covers every finite
        # point of F2bar. This is the algebraic-closure criterion, not
        # merely rank(A), rank(B), rank(A+B) at the three rational points.
        good = common == 1
        rational_good = full[a ^ matrices]
        assert not np.any(good & ~rational_good)
        bad = rational_good & ~good
        total += int(np.count_nonzero(good))
        rational += int(np.count_nonzero(rational_good))
        falsepos += int(np.count_nonzero(bad))
        if witness is None and np.any(bad):
            ix = int(np.flatnonzero(bad)[0])
            b = int(matrices[ix])
            witness = {"A": [[(a >> (3*r+c)) & 1 for c in range(3)] for r in range(4)],
                       "B": [[(b >> (3*r+c)) & 1 for c in range(3)] for r in range(4)],
                       "ranks_at_three_rational_points": [rank(a), rank(b), rank(a^b)],
                       "minor_polynomial_bit_codes": [int(f[ix]) for f in minors],
                       "gcd_polynomial_bit_code": int(common[ix])}
        good_b = matrices[good]
        for s in shapes:
            if not a & s["masks"][0]:
                s["actual"] += int(np.count_nonzero((good_b & s["masks"][1]) == 0))
    assert total + falsepos == rational
    assert total == 3386880
    assert all(s["actual"] == s["expected"] for s in shapes)
    report = {"field_order": 2, "numpy_version": np.__version__,
              "total_tensor_domain": 2**24, "full_rank_slices": 2520,
              "pairs_after_necessary_rank_pruning": 2520**2,
              "nondegenerate_over_algebraic_closure": total,
              "passing_rational_points_only": rational,
              "rational_only_false_positives": falsepos,
              "rational_only_counterexample": witness,
              "all_55_counts_equal": True,
              "results": [{"lambda": s["lambda_"], "mu": s["mu"],
                           "actual": s["actual"], "expected": s["expected"]} for s in shapes]}
    target = Path(__file__).with_suffix('.json')
    tmp = target.with_suffix('.tmp')
    tmp.write_text(json.dumps(report, indent=2)+"\n")
    tmp.replace(target)
    print(json.dumps({k: v for k, v in report.items() if k != "results"}, indent=2))


if __name__ == '__main__':
    main()
