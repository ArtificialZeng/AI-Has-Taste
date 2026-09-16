# Frozen source problem: first multiset-permutation instability for consecutive pattern 21435

Canonical id: `win-00087-p05`

Frozen on: 2026-09-11 (Asia/Shanghai)

Primary source: Shaoshi Chen, Hanqian Fang, and Sergey Kitaev, *Stable patterns on permutations of multisets*, arXiv:2602.13566v2, definitions on PDF pp.3--5, Proposition 4.12 and Remark 4.13 on p.12, and Conjecture 6.1 on p.17.

## Definitions

For a positive multiplicity vector `alpha=(alpha_1,...,alpha_m)`, let `W_alpha` be the words in which letter `i` occurs exactly `alpha_i` times, and let `N=sum_i alpha_i`. For a word `w`, set

```text
c(w) = number of i with w_(i+1) < w_i < w_(i+3) < w_(i+2) < w_(i+4),
F_alpha(t) = sum_{w in W_alpha} t^(c(w)).
```

Call the multiplicity type stable when `F_alpha=F_(sigma alpha)` for every permutation `sigma` of the coordinates. Zero multiplicities may be deleted; cases `N<5` or `m<5` are trivial.

## Statement to prove or disprove

For the consecutive pattern `21435`, prove the exact first-instability classification:

1. Every positive multiplicity vector of total length `N<=8` is stable.
2. At `N=9`, the only unstable unordered multiplicity type is `{2,1^7}`.
3. When the repeated letter has rank `1,2,3,4`, the occurrence distribution is

```text
F(t) = 176026 + 5368 t + 46 t^2,
```

and for rank `5,6,7,8` it is

```text
F(t) = 176025 + 5370 t + 45 t^2.
```

There are no words with three or more occurrences in these cases.

## Required contribution boundary

The source's existing shortest-overlap criterion does not handle this pattern; Remark 4.13 explicitly highlights that obstruction. A complete contribution must give a mathematical explanation of the minimal length and uniqueness, preferably through the two possible nontrivial overlap separations, the resulting overlap posets, and coefficient extraction or binomial inversion. Exhaustive word generation may certify the finite classification but should not be the paper's only explanation.

The source's Conjecture 6.1 is broader. This project proves only the stated boundary case and must not be presented as resolving the full stable-pattern conjecture.

## Evidence to replay

- `batches/inbox/bigWin-87.raw.md`
- `batches/inbox/bigWin-87.capture.json`
- `batches/normalized/bigWin-87.md`
- `batches/inbox/bigWin-87-materials/05_pattern/verify.py`

The checker covers all 256 nontrivial content vectors through total length nine and directly counts every distinct word using the five strict inequalities. Referee must audit both coverage and the separate combinatorial proof.

Any manuscript must normally cite the primary source, the standard consecutive-pattern and cluster/overlap results actually used, and the closest multiset-pattern prior art, plus one or two genuinely relevant user-library papers when available. The user-library minimum does not cap the bibliography.

This file is immutable. A claim for another pattern, longer length, or the full conjecture requires a new freeze and review.
