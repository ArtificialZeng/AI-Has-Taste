# Frozen source problem: the ternary ASP(6,4,3) one-bit gap

Canonical id: win-00084-p06
Frozen on: 2026-09-09 (Asia/Shanghai)
Primary source: Boruchovsky--Gruica--Niemann--Yaakobi,
Serving Every Symbol: All-Symbol PIR and Batch Codes,
arXiv:2601.04041v2, Definitions 1--2 on PDF p.3, Notation 4 p.4,
Problem 1 p.5, Theorem 23 p.13, and the discussion pp.14--15.
Local copy: batches/inbox/bigWin-84-materials/2601.04041v2.pdf,
SHA-256 64d12f7e49d474c8db407ff341cc2e8cab800a88ad8cbf078244579068933062.

## Definitions

Let G=[g1,...,gn] be a rank-six matrix over F_3. A set R of column indices
recovers gi when gi lies in the F_3-span of {gj:j in R}. The matrix is
four-all-symbol PIR when, for every i, there are four pairwise disjoint
recovery sets for gi. ASP(6,4,3) is the minimum possible n.

## Statement

Decide the exact alternative

> ASP(6,4,3)=11 or ASP(6,4,3)=12.

Equivalently, decide whether a rank-six 6 by 11 matrix over F_3 with the
four-all-symbol PIR property exists.

## Scope and contribution boundary

Theorem 23 gives

  11 <= ASP(6,4,3) <= ASB(6,4,3) <= 12.

The fixed ternary cell is not separately named as an open problem in the
source, so novelty/open status remains to be rechecked before publication.
Remark 25 explains a characteristic obstruction but does not itself prove the
reported binary equality; the following unnumbered paragraph reports that
exhaustive binary computation.

A positive certificate must give G, its rank witness, four disjoint recovery
sets for every column, and exact coefficients. A negative result must cover
all length-eleven matrices modulo justified row operations, column
permutations, and projective scaling, with a replayable SAT/LRAT or equivalent
complete certificate. Solver UNKNOWN or an uncertified search is not a result.

This file is immutable. An ASB claim or a claim over another field must be
frozen separately.
