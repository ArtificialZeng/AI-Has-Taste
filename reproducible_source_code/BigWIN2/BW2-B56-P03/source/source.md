# The unique uncovered length-15 cell of Conjecture B on Hilbert schemes

## Immutable source statement

Let `R=C[x,y,z]`. Enumerate every zero-dimensional Borel-fixed monomial ideal `I` of colength 15. For each such ideal compute exactly

`T(I)=dim_C Hom_R(I,R/I)`.

Determine the maximum of `T(I)` and classify every maximizing ideal. In particular, prove or disprove:

> If `[I]` has maximal tangent-space dimension among Borel-fixed points of `Hilb^15(A^3)`, then `m_1(I)=3`, where the pure powers are ordered `m_1(I)<=m_2(I)<=m_3(I)` as in Conjecture B of the primary source.

## Quantifiers and scope

- All and only zero-dimensional Borel-fixed monomial ideals of colength exactly 15 over `C` are included.
- The conclusion concerns maximality within the Borel-fixed points specified by Conjecture B. Any extension to all points of the Hilbert scheme requires a separate argument.
- Enumeration completeness, ideal equality, tangent dimensions, and isomorphism/symmetry reductions must be exact.
- A single `m_1<=2` maximizer refutes the displayed necessary condition for this cell; it is not enough to find merely a singular example.

## Primary source and nearest result

- Fatemeh Rezaee and Parsa Saberi, *An obstruction to the maximal singularity of the Hilbert scheme of points on threefolds*, arXiv:2609.04054v1 (2026), https://arxiv.org/abs/2609.04054.
- Local PDF: `batches/inbox/bigWin-56-materials/2609.04054.pdf`.
- SHA-256: `736c9109d7ba9066f1fa77d5de4d411d2a1caf58c9583ef469f58800e102cc33`.
- Locators: Conjecture B and degree families (0.1)--(0.3), PDF p.2; Theorem B and strategy, pp.2--3; Borel-fixed definition and tangent bounded-component formula, p.4; Theorem 5.1, p.17.
- For `N=3,k=3`, Conjecture B concerns `10<=l<20`. The source covers `10,11,12,13`, `16,17,18,19`, and `10,14,17,19`; length 15 is the unique uncovered integer in this first interval.

## Proposed contribution boundary

The smallest acceptable result is a complete, independently replayable length-15 atlas and the resulting resolution of the Borel-fixed Conjecture-B cell. A census without a completeness proof or tangent dimensions from only one unverified implementation is evidence, not a theorem.

## Cheapest decisive test and certificates

Enumerate size-15 three-dimensional order ideals/Ferrers diagrams satisfying strong stability. Store canonical monomial bases and minimal generators. Compute `Hom_R(I,R/I)` by exact rational linear algebra and independently by the bounded-component formula of Definition 1.1 or Macaulay2. Save a digest and per-ideal witnesses; attack maximizers with a second implementation.

## Provenance

Prepared on 2026-09-07 from the primary PDF during the authorized fallback after the exact Chrome target could not be attached. This file freezes exactly the length-15 Borel-fixed problem.
