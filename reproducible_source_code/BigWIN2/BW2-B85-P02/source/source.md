# Frozen source problem: determine the new zero-sum constant s_1(4)

Canonical id: win-00085-p02
Frozen on: 2026-09-10 (Asia/Shanghai)
Primary source:
- Sun, *On zero-sum problems of new types*, arXiv:2606.18234v5,
  Definition 1.3, Theorem 1.3, and Remark 1.4 on PDF p.3, and
  Conjecture 1.2 on PDF p.4.

## Definitions

Let s_1(4) be the least positive integer k such that every sequence of k
integers a_1,...,a_k satisfying `4 does not divide a_i` contains four terms,
with indices counted according to their multiplicities in the sequence, whose
sum is divisible by 4 but not divisible by 16.

Equivalently, the chosen four-term sum is congruent to 4, 8, or 12 modulo 16.
Repeated values are allowed, but a sequence position may be chosen at most
once.

## Statement

Determine the exact value of s_1(4).

## Scope and contribution boundary

The cited source proves only

```
9 <= s_1(4) <= 13
```

and conjectures the general formula `s_1(n)=2n+1` for `n>2`. The equality
`s_1(4)=9` is a Batch85 desktop-precheck candidate, not a fact supplied by the
source and not yet an independently audited proof.

The discovery materials

- `batches/bigWin-85-materials/s1_4_exact_precheck.py`, SHA-256
  `8d2975f3e89327d21bf68332ad9f2f26455234ceb7eb435cb8576fac99c31d19`,
  and
- `batches/bigWin-85-materials/s1_4_exact_precheck.report.md`

enumerate all 167,960 nondecreasing nine-element multisets over the twelve
allowed residue classes modulo 16 and check a proposed length-eight witness.
They are leads only. A complete proof must independently justify reduction
from arbitrary integers to residue multisets, regenerate the entire finite
domain without omissions or duplication, publish a compact replayable
coverage certificate, and verify the lower-bound witness. A single uncovered
nine-term multiset disproves the candidate equality but does not change the
frozen task of determining s_1(4).

This file is immutable. A statement for another n, another subsequence length,
or a squarefree rather than repeated sequence is a different problem.
