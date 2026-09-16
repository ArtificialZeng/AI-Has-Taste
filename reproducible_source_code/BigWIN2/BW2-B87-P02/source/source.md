# Frozen source problem: classification of restricted-sumset saturation with two missing sums

Canonical id: `win-00087-p02`

Frozen on: 2026-09-11 (Asia/Shanghai)

Primary source: Jiantao Li and Xinyi Liang, *A Counterexample to a Conjecture of Liu and Qian and a Refined Inverse Theorem for Restricted Sumsets in Z_p*, arXiv:2609.10148v1, definitions and Theorems 1.1--1.2 on PDF pp.1--2 and Example 2.1 on pp.2--3.

## Definitions and statement

For subsets `A,B` of the prime field `F_p`, define

```text
A dotplus B = {a+b : a in A, b in B, and a != b}.
```

For every prime `p>=11` and every integer `3<=ell<=(p-3)/2`, classify all ordered pairs with

```text
|B|=ell, |A|=p-ell, and |A dotplus B|=p-2,
```

up to a simultaneous affine map `z -> u z+v`, `u!=0`.

The proposed classification normalizes the two missing sums to `{0,2}`. For integers `a,b>=0` with `a+b=ell`, put

```text
B_(a,b) = {-2j : 0<=j<a} union {1+2j : 0<=j<b},
C_(a,b) = {2+2j : 0<=j<a} union {-1-2j : 0<=j<b},
A_(a,b) = F_p \ C_(a,b),
```

with empty segments allowed and arithmetic modulo `p`. Prove or refute that every critical ordered pair is affinely equivalent to exactly one such form modulo `(a,b)~(b,a)`, hence that the number of affine classes is `floor(ell/2)+1`.

## Required proof obligations

A complete proof must establish the missing-sum normalization, the inclusion

```text
U = ((-B)\{0}) union ((2-B)\{1}) subset C = F_p\A,
```

the step-two cyclic run count and both endpoint corrections, the exclusion of wrap-around alternatives in the stated parameter range, the converse verification, and the affine-equivalence classification. Ordinary integer maximum/minimum arguments cannot be imported into `F_p` without a separate wrap-around proof.

## Status and novelty limits

The source gives a particular boundary counterexample and says the overall inverse problem remains open, but it does not pose this exact all-parameter classification. Liu--Qian's original paper was not available in the first screening and must be checked in full, together with later papers, before asserting novelty or openness. The proof should be self-contained and should not rely on any potentially order-sensitive step in the source's later section.

## Evidence to replay

- `batches/inbox/bigWin-87.raw.md`
- `batches/inbox/bigWin-87.capture.json`
- `batches/normalized/bigWin-87.md`
- `batches/inbox/bigWin-87-materials/02_restricted_sumset/verify.py`

The supplied exact enumerator checks all legal `ell` for `p=11,13,17,19`; it is a counterexample screen, not a universal proof.

Any manuscript must normally cite the primary source, Liu--Qian, all standard restricted-sumset inverse results actually used, and the closest prior art, plus one or two genuinely relevant user-library papers when available. The user-library minimum does not cap the bibliography.

This file is immutable. Replacing prime fields, dropping ordered-pair classification, or proving only the displayed examples is a different claim.
