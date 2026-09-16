"""Bounded consistency checks for the recovered triage; no universal proof."""
from pathlib import Path
from hashlib import sha256
from itertools import permutations
from fractions import Fraction
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
JOB = "primary-20260914-stirling-transition-triage-65861bc877d9"


def digest(path):
    return sha256((ROOT / path).read_bytes()).hexdigest()


def main():
    expected = {
        "source.md": "4a37fe8a21f41aac0b72c9da83e28e1aff2ce19676fe24c5d93befb9e2d99594",
        "evidence/ratio-reduction.md": "d4c90ab3e88c67cbdd73aff2e7cdcefc8e2f7d28b35401476089bba655250911",
        "evidence/triage_exact.py": "14d7ad6c99d875ba230b2c9fc624ab670669657b390f345a041f7eda63a7d6e5",
        "evidence/triage_exact.json": "d65112af6845eea476cfb546b091fb227e6d6b7ccf35191853becb637f764ea1",
        "literature/2408.02782v1.html": "6b4c97905f1fe95e002f603cb74c768b07180c9be9fa00bdba0414616b6e5a3b",
        "literature/2607.04217v1.html": "c2754444d71b8fb4bc3d6fc238a3bb42b65cc7008b39ceab8f82d8399394acb0",
    }
    actual = {path: digest(path) for path in expected}
    assert actual == expected
    old = json.loads((ROOT / "evidence/triage_exact.json").read_text())
    assert old["source_sha256"] == actual["source.md"]
    assert old["script_sha256"] == actual["evidence/triage_exact.py"]
    assert old["coverage"]["D_count"] == 150 * 1000
    assert old["coverage"]["q_count"] == sum(999-k for k in range(1, 151))
    assert len(old["columns"]) == 150
    for k, col in enumerate(old["columns"], 1):
        word = col["sign_word"]
        assert col["k"] == k and len(word) == 1000
        assert set(word) <= set("0+-")
        assert word[:k-1] == "0"*(k-1) and word[k-1] == "+"
        assert "0" not in word[k-1:]
        first = word.find("-") + 1
        assert first > 0 and first == col["first_negative"]
        assert col["first_nonpositive_on_support"] == first
        assert "+" not in word[first-1:]
        assert col["last_positive"] == word.rfind("+") + 1
        assert not col["supported_zeros"]

    # Fresh small recurrence computation, compared with retained sign words.
    # This is a partial replay, not an independent replay of the full rectangle.
    rows = [[1]]
    for n in range(1, 83):
        prev = rows[-1]
        row = [0] * (n+1)
        for j, value in enumerate(prev):
            row[j] += (n-1)*value
            row[j+1] += value
        rows.append(row)

    def c(n, k):
        return rows[n][k] if 0 <= k <= n else 0

    enum_count = 0
    for n in range(8):
        counts = [0]*(n+1)
        for p in permutations(range(n)):
            seen = [False]*n
            cycles = 0
            for j in range(n):
                if seen[j]:
                    continue
                cycles += 1
                while not seen[j]:
                    seen[j] = True
                    j = p[j]
            counts[cycles] += 1
            enum_count += 1
        assert counts == rows[n]

    d_count = ratio_count = identity_count = 0
    for k in range(1, 21):
        for n in range(1, 81):
            d = c(n,k)**2-c(n-1,k)*c(n+1,k)
            sign = "+" if d > 0 else "-" if d < 0 else "0"
            assert sign == old["columns"][k-1]["sign_word"][n-1]
            d_count += 1
            if n >= k+1:
                lhs = Fraction(d, c(n-1,k)*c(n,k))
                rhs = Fraction(c(n-1,k-1),c(n-1,k))-Fraction(c(n,k-1),c(n,k))-1
                assert lhs == rhs
                identity_count += 1
        for n in range(k, 79):
            q2 = sum(weight*Fraction(c(n+i,k-1),c(n+i,k))
                     for i, weight in enumerate((1,-2,1)))
            assert q2 >= 0
            ratio_count += 1

    # Symbolic identity check only: this does not establish positivity.
    n, A, B, C, E = sp.symbols("n A B C E")
    Q1 = n*A+B
    Q2 = n*(n+1)*A+(2*n+1)*B+C
    raw = B*Q1*Q2-2*(n*B+C)*A*Q2+(n*(n+1)*B+(2*n+1)*C+E)*A*Q1
    proposed = (n*A+B)*(B*B-A*C)+n*(2*B**3-3*A*B*C+A*A*E)+B*B*C-2*A*C*C+A*B*E
    residual = sp.expand(raw-proposed)
    assert residual == 0

    result = {
        "job_id": JOB,
        "date": "2026-09-14",
        "retained_artifact_hashes": actual,
        "retained_all_sign_words_structurally_consistent": True,
        "retained_full_rectangle_recomputed": False,
        "fresh_D_check": {"range": "1<=k<=20, 1<=n<=80", "count": d_count, "matches_retained": True},
        "fresh_q_check": {"range": "1<=k<=20, k<=n<=78", "count": ratio_count, "negative_count": 0},
        "fresh_D_ratio_identity_check": {"range": "1<=k<=20, k+1<=n<=80", "count": identity_count},
        "independent_permutation_check": {"range": "0<=n<=7", "permutations": enum_count, "matches": True},
        "symbolic_numerator_residual": str(residual),
        "sympy_version": sp.__version__,
        "script_sha256": digest("evidence/triage_recovery_check.py"),
        "limitation": "Finite replay and symbolic algebra verification only. Universal ratio convexity, novelty, and the source conjecture remain unproved here."
    }
    target = ROOT / "evidence/triage_recovery_check.json"
    tmp = target.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(result, indent=2)+"\n")
    tmp.replace(target)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
