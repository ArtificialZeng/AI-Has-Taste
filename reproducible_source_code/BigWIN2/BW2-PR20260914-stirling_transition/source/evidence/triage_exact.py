"""Exact, bounded screening; no infinite statement is certified."""
from pathlib import Path
from itertools import permutations
from math import factorial
from hashlib import sha256
import json
import time

ROOT = Path(__file__).resolve().parents[1]
JOB = "primary-20260914-stirling-transition-triage-fc44a4f8547e"
N, K = 1000, 150


def run():
    started = time.monotonic()
    rows = [[0] * (K + 1) for _ in range(N + 2)]
    rows[0][0] = 1
    for n in range(1, N + 2):
        for k in range(1, min(n, K) + 1):
            rows[n][k] = (n - 1) * rows[n - 1][k] + rows[n - 1][k - 1]

    # Independent combinatorial check, including n=0 and the zero column.
    permutation_count = 0
    for n in range(9):
        counts = [0] * (n + 1)
        for p in permutations(range(n)):
            seen = set()
            cycles = 0
            for i in range(n):
                if i not in seen:
                    cycles += 1
                    j = i
                    while j not in seen:
                        seen.add(j)
                        j = p[j]
            counts[cycles] += 1
            permutation_count += 1
        assert counts == rows[n][:n + 1], (n, counts)
        assert sum(counts) == factorial(n)

    words = []
    reversals = []
    convexity_failures = []
    persistence_failures = []
    ratios_checked = 0
    signs_checked = 0
    for k in range(1, K + 1):
        first_negative = None
        first_nonpositive_on_support = None
        last_positive = None
        supported_zeros = []
        sign_word = []
        prior_sign = None
        for n in range(1, N + 1):
            d = rows[n][k] ** 2 - rows[n - 1][k] * rows[n + 1][k]
            sign = (d > 0) - (d < 0)
            sign_word.append("+" if sign > 0 else "-" if sign < 0 else "0")
            signs_checked += 1
            if sign < 0 and first_negative is None:
                first_negative = n
            if n >= k and sign <= 0 and first_nonpositive_on_support is None:
                first_nonpositive_on_support = n
            if sign > 0:
                last_positive = n
                if first_negative is not None:
                    reversals.append([k, first_negative, n])
            if n >= k and sign == 0:
                supported_zeros.append(n)
            if n > k and prior_sign <= 0 and sign > 0:
                persistence_failures.append([k, n - 1, n])
            prior_sign = sign

        # q(n)-2q(n+1)+q(n+2), cleared by strictly positive denominators.
        for n in range(k, N - 1):
            a, b, c = rows[n][k], rows[n + 1][k], rows[n + 2][k]
            x, y, z = rows[n][k - 1], rows[n + 1][k - 1], rows[n + 2][k - 1]
            numerator = x*b*c - 2*y*a*c + z*a*b
            ratios_checked += 1
            if numerator < 0:
                convexity_failures.append([k, n])
        words.append({"k": k, "last_positive": last_positive,
                      "first_negative": first_negative,
                      "first_nonpositive_on_support": first_nonpositive_on_support,
                      "supported_zeros": supported_zeros,
                      "sign_word": "".join(sign_word)})

    output = {
        "job_id": JOB,
        "arithmetic": "Python arbitrary-precision integers only; no floating-point sign tests",
        "coverage": {"D": "1<=k<=150, 1<=n<=1000", "D_count": signs_checked,
                     "rows_generated_through": N+1,
                     "q_second_difference": "1<=k<=150, k<=n<=998",
                     "q_count": ratios_checked},
        "independent_check": {"method": "enumerate every permutation for 0<=n<=8 and count cycles",
                              "permutations": permutation_count, "passed": True},
        "negative_then_positive_pairs": reversals,
        "nonpositive_then_positive_adjacent_on_support": persistence_failures,
        "q_convexity_failures": convexity_failures,
        "columns": words,
        "source_sha256": sha256((ROOT / "source.md").read_bytes()).hexdigest(),
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": round(time.monotonic() - started, 3),
        "limitation": "Exact finite observations; no all-k or infinite-tail proof, no novelty certification."
    }
    target = ROOT / "evidence/triage_exact.json"
    temporary = target.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(output, indent=2) + "\n")
    temporary.replace(target)
    print(json.dumps({key: output[key] for key in output if key != "columns"}, indent=2))
    print("First 20 (k,last_positive,first_negative):",
          [(w["k"], w["last_positive"], w["first_negative"]) for w in words[:20]])
    print("Last column:", {key: words[-1][key] for key in words[-1] if key != "sign_word"})


if __name__ == "__main__":
    run()
