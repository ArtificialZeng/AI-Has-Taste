# Frozen source problem: minimal graphic failure of coloop multiplication in the radial Möbius algebra

Canonical id: `win-00087-p04`

Frozen on: 2026-09-11 (Asia/Shanghai)

Primary source: Thomas Sinclair, *The radial derivative on the graded Möbius algebra*, arXiv:2608.18519v1, Proposition 2.4 on PDF p.6, Example 3.2 on p.8, and Question 6.3 on p.14.

## Definitions

For every connected simple graph `G` on at most five vertices, let `M(G)` be its cycle matroid. Flats are edge sets closed by adding every original graph edge whose endpoints lie in one connected component; `r(X)=|V(G)|-c(V(G),X)`.

On the rational vector space with basis `g_X` indexed by flats, define

```text
L_e g_Y = sum_{X lessdot Y, e in Y\X} g_X,
D g_Y = r(Y) sum_{X lessdot Y} |Y\X|/|E\X| g_X.
```

Let `C_0=Q g_E`, `C_(j+1)=D C_j + sum_e L_e C_j`, and `H_M(q)=sum_j dim(C_j) q^j`. Put `M^+=M direct-sum U_(1,1)` and

```text
Delta_G(q) = H_(M^+)(q) - (1+q) H_M(q).
```

The one-vertex empty-edge graph is included, with `H_M=1`.

## Statement to prove or disprove

Audit and prove the complete finite classification:

1. `Delta_G=0` for every connected simple graph with at most four vertices.
2. For five vertices, `Delta_G!=0` if and only if the complement of `G` is a linear forest, isolated vertices allowed.
3. The exact nonzero values are

```text
P5, P4+K1, P3+P2              -> 2 q^2 + 2 q^3
P3+2K1                         -> q^2 + 2 q^3
2P2+K1, P2+3K1, 5K1           -> 4 q^2.
```

4. The unique least-edge failure is the six-edge graph `K5-P5 = Theta(1,2,3)`, with Hilbert vectors `(1,6,11,6,1)` and `(1,7,19,19,7,1)` before and after adding the coloop.

## Contribution and scope boundary

The source already observes that simple formulas for operations may fail. Merely exhibiting a failure is not new enough. The only proposed contribution is the exact minimal order, least-edge uniqueness, and complete five-vertex graphic classification. It should be positioned as a finite result note, not as a solution to the general operation problem in Question 6.3.

## Evidence to replay

- `batches/inbox/bigWin-87.raw.md`
- `batches/inbox/bigWin-87.capture.json`
- `batches/normalized/bigWin-87.md`
- `batches/inbox/bigWin-87-materials/04_radial/exact_census.json`
- `batches/inbox/bigWin-87-materials/04_radial/verify.py`
- `batches/inbox/bigWin-87-materials/04_radial/check_classification.py`

The 31 graph classes and rational ranks must be recomputed exactly. Modular ranks are only a cross-check and cannot certify rational upper bounds. Referee must also verify the implementation matches the source's operators and grading.

Any manuscript must normally cite the source, standard graphic-matroid and Möbius-algebra definitions actually used, and the closest operation literature, plus one or two genuinely relevant user-library papers when available. The user-library minimum does not cap the bibliography.

This file is immutable. Enlarging the vertex range or claiming a general direct-sum theorem requires a new freeze and review.
