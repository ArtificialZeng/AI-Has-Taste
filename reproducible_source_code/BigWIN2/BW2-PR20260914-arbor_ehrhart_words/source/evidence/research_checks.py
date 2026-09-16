"""Exact adversarial checks of the proof's local operators and word bijection.

Run from the project root: python3 evidence/research_checks.py
Writes evidence/research_checks.json atomically. Standard library only.
No triage code is imported. These finite tests are not an infinite proof.
"""
from collections import Counter
from itertools import combinations, product
from math import comb
from pathlib import Path
import hashlib
import json


def convolve(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def local_checks():
    identities = coefficients = 0
    for b in range(1, 9):
        for K in range(33):
            lhs = [0] * (K+b+1)
            for q in range(K+1):
                for j in range(K-q+1):
                    lhs[b+j] += comb(q+b-1, b-1)*comb(K-q, j)
            rhs = [0 if j < b else comb(K+b, j)
                   for j in range(K+b+1)]
            assert lhs == rhs, ("L", b, K, lhs, rhs)
            identities += 1
            coefficients += len(rhs)
    return dict(b=[1, 8], K=[0, 32], identities=identities,
                coefficients_compared=coefficients, all_passed=True)


def operator_checks():
    identities = coefficients = 0
    for b in range(1, 6):
        for N in range(b, b+9):
            for m in range(5):
                # Alternating signs and full allowed degree test that (O)
                # does not tacitly require positivity or cancellation-free R.
                R = [(-1)**s * ((s*s+3*s+1) % 11+1)
                     for s in range(m*(N-b)+1)]
                H = convolve([comb(q+b-1, b-1)
                              for q in range(m*N+1)], R)[:m*N+1]
                lhs = [0] * ((m+1)*N+1)
                for k, h in enumerate(H):
                    for j in range(m*N-k+1):
                        lhs[N+j] += h*comb(m*N-k, j)
                rhs = [0] * len(lhs)
                for s, r in enumerate(R):
                    for j in range(m*N+b-s+1):
                        rhs[N-b+j] += r*comb(m*N+b-s, j)
                rhs[:N] = [0]*N
                assert lhs == rhs, ("O", b, N, m)
                identities += 1
                coefficients += len(rhs)
    return dict(b=[1, 5], N_minus_b=[0, 8], m=[0, 4],
                R="full degree, deterministic nonzero alternating coefficients",
                identities=identities, coefficients_compared=coefficients,
                all_passed=True)


def box_checks():
    records = []
    total_subsets = total_word_tests = 0
    for n in range(1, 6):
        for m in range(5):
            slots = [(letter, box) for letter in range(1, n+1)
                     for box in range(m+1)]
            observed = Counter()
            for subset in combinations(slots, n):
                boxes = [[] for _ in range(m+1)]
                for letter, box in subset:
                    boxes[box].append(letter)
                boxes = [tuple(sorted(box, reverse=True)) for box in boxes]
                word = tuple(letter for box in boxes for letter in box)
                # Explicit inverse retains the positions of all empty boxes.
                recovered = {(letter, k) for k, box in enumerate(boxes)
                             for letter in box}
                assert recovered == set(subset)
                observed[word] += 1
            for w in product(range(1, n+1), repeat=n):
                d = sum(w[i] <= w[i+1] for i in range(n-1))
                expected = comb(m-d+n, n) if m >= d else 0
                assert observed[w] == expected, ("W", n, m, w)
                total_word_tests += 1
            assert sum(observed.values()) == comb(n*(m+1), n)
            total_subsets += sum(observed.values())
            records.append(dict(n=n, m=m, subset_objects=sum(observed.values()),
                                words_tested=n**n, all_passed=True))
    return dict(domain="all words of length n on [n], 1<=n<=5, 0<=m<=4",
                subset_objects=total_subsets, word_tests=total_word_tests,
                records=records, all_passed=True)


def weak_compositions(total, length):
    if length == 1:
        yield (total,)
        return
    for first in range(total+1):
        for rest in weak_compositions(total-first, length-1):
            yield (first,) + rest


def direct_checks():
    # Chosen for a large leaf block, internal branching, and interleaved labels.
    # D sets are supplied directly, independently of any tree recursion.
    cases = [
        dict(name="single_large_block", n=6,
             blocks=[[1,2,3,4,5,6]], parent=[-1], D=[[1,2,3,4,5,6]]),
        dict(name="nested_branch_interleaved_labels", n=6,
             blocks=[[3],[1],[4,6],[2],[5]], parent=[-1,0,0,1,1],
             D=[[1,2,3,4,5,6],[1,2,5],[4,6],[2],[5]]),
        dict(name="two_nonsingleton_leaves", n=6,
             blocks=[[2,5],[1,6],[3,4]], parent=[-1,0,0],
             D=[[1,2,3,4,5,6],[1,6],[3,4]])
    ]
    results = []
    for case in cases:
        n = case["n"]
        descendants = [tuple(i-1 for i in D) for D in case["D"]]
        content_set = [a for a in weak_compositions(n, n)
                       if all(sum(a[i] for i in D) >= len(D)
                              for D in descendants)]
        word_hist = [0]*n
        for word in product(range(n), repeat=n):
            counts = [word.count(i) for i in range(n)]
            if all(sum(counts[i] for i in D) >= len(D) for D in descendants):
                word_hist[sum(word[j] <= word[j+1] for j in range(n-1))] += 1
        samples = []
        for m in range(4):
            # Slack coordinate gives every nonnegative vector of total <=mn
            # exactly once; no upper-subtree recursion is used.
            lattice = sum(all(sum(x[i] for i in D) <= m*len(D)
                              for D in descendants)
                          for x in weak_compositions(m*n, n+1))
            binomial = 0
            for a in content_set:
                weight = 1
                for ai in a:
                    weight *= comb(m+1, ai) if ai <= m+1 else 0
                binomial += weight
            word_count = sum(c*comb(m-d+n, n)
                             for d, c in enumerate(word_hist) if m >= d)
            assert lattice == binomial == word_count, (case["name"], m)
            samples.append(dict(m=m, lattice=lattice, binomial_sum=binomial,
                                barred_words=word_count))
        results.append(dict(**case, admissible_contents=len(content_set),
                            word_polynomial=word_hist, samples=samples))
    return dict(cases=results, all_passed=True,
                qualification="Three selected boundary/branching cases; not a census.")


def main():
    result = dict(job_id="primary-20260914-arbor-ehrhart-words-research-9e9070b093b6",
                  arithmetic="exact integers", random_seed=None,
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  local_identity=local_checks(), operator_identity=operator_checks(),
                  word_bijection=box_checks(), direct_enumeration=direct_checks(),
                  qualification="Finite adversarial checks; the infinite proof is in research-proof.md.")
    output = Path("evidence/research_checks.json")
    temporary = output.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(result, indent=2)+"\n")
    temporary.replace(output)
    print(json.dumps(dict(all_passed=True,
                          local_identities=result["local_identity"]["identities"],
                          operator_identities=result["operator_identity"]["identities"],
                          subset_objects=result["word_bijection"]["subset_objects"],
                          word_tests=result["word_bijection"]["word_tests"],
                          direct_cases=len(result["direct_enumeration"]["cases"]),
                          output=str(output))))


if __name__ == "__main__":
    main()
