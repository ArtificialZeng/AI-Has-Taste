# SC258 ordered associative spectrum

The immutable original statement is `source.md` (SHA-256 recorded in `evidence/intake.json`). No correction or weakening is made.

Let A={0,1,2}, with binary operation given by rows indexed by the left operand and columns by the right operand:

| * | 0 | 1 | 2 |
|---|---|---|---|
| 0 | 0 | 0 | 0 |
| 1 | 1 | 1 | 0 |
| 2 | 1 | 0 | 1 |

For each integer n>=1, let B_n be the fully parenthesized binary terms whose leaves, read left to right, are exactly x_1,...,x_n, each occurring once. B_1={x_1}; recursively every element of B_n is (u*v), for a unique root split 1<=k<n, u on x_1,...,x_k and v on x_{k+1},...,x_n. No constants or variable permutations are allowed. Interpret each term by the table to give t^A:A^n -> A. Set a_n=|{t^A:t in B_n}|, where functions are equal precisely when their values agree on every tuple in A^n, even if some arguments are inessential.

The target is a_1=a_2=1, a_3=2, and, for every integer n>=4,

    a_n = 3 a_{n-1} - 2 a_{n-2} + a_{n-3}.

There is no a_0 in the claim. Equivalently, the generating function sum_{n>=1} a_n z^n is z(1-z)^2/(1-3z+2z^2-z^3). The n=1 term is the identity map and can take value 2; every n>=2 term has image contained in {0,1}. This is the associative spectrum, distinct from the associative-commutative spectrum allowing variable permutations.

Nearest inspected prior result: Huang–Lehtonen (2024), Definition 1.1, p. 1, and Section 7, p. 17, reports the finite list 1,1,2,5,12,28,65,151,351 for SC258 and several related groupoids, identifying agreement with initial terms of OEIS A034943, without a general result for these examples. See `evidence/primary-extract.md`. Those finite terms alone do not imply the quantified recurrence. Current literature status and bounded historical comparison are recorded in `evidence/triage-literature.md`.

Research-pass contribution proposed for fresh review: `evidence/pruning-proof.md` gives a complete proof of the exact original recurrence. It proves that increasing-label combs are recovered from their essential support and variable restrictions, then counts attainable pruned forms by their largest retained label. This preserves the original scope. The assertion is a proof candidate, not an accepted referee result.

Primary-source binding: the complete cached journal PDF and text have been copied without modification to `evidence/external/huang-lehtonen-2024.pdf` and `evidence/external/huang-lehtonen-2024.txt`; provenance and hashes are in `evidence/external/provenance.json`. Definition 1.1 and Section 7 were inspected again and compared with live author-preprint HTML. The bounded current comparison is in `evidence/research-literature.md`.

Verification: `evidence/verify_pruning.py` and `evidence/pruning-verification.json` record exact full-table preservation and reconstruction for every raw bracketing through n=8, all 1644 increasing-label combs on nonempty subsets of eight labels, raw pruned-set comparison through n=10, and syntactic set enumeration through n=14. These finite checks support the separately written all-n proof; they do not replace it.
