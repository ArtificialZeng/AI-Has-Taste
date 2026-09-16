# win-00079-p01 — ideal-endpoint rigidity of the equiangular hyperbolic 4-cube

## Immutable primary-source record

- Andrey Egorov, *Minimal-Volume Equiangular Hyperbolic 4-Polytopes*,
  arXiv:2609.04258v1.
- Official HTML: <https://arxiv.org/html/2609.04258v1>
- Official PDF: <https://arxiv.org/pdf/2609.04258v1>
- Local full text: `bigWin-79-materials/2609.04258.pdf`, SHA-256
  `1e6b85a758b8e4a3b380d633d74fc54722bc1dfa1edef79b87a589a2ec7e346a`.
- Locators: Proposition 2.1 and Proposition 2.3 (PDF pp.4--5), Proposition
  5.1 and Remark 5.2 (PDF p.9).

## Frozen assertion

Put `alpha_0=arccos(1/3)`. Prove or disprove:

> Every finite-volume convex hyperbolic 4-polytope combinatorially equivalent
> to the 4-cube and having all dihedral angles equal to `alpha_0` is isometric
> to the regular ideal equiangular cube `C^4_(alpha_0)`.

The word cube fixes the full face lattice, including four specified pairs of
opposite facets. All vertices are allowed to be ideal but no hyperideal or
truncated substitute is included.

## Nearest result and exact delta

Proposition 2.1 proves that every vertex at `alpha_0` is ideal. Proposition
2.3 constructs the regular model and proves combinatorial-cube uniqueness only
for `alpha>alpha_0`, using compact non-obtuse Andreev rigidity; it explicitly
states that no uniqueness claim at the ideal endpoint is needed there.
Proposition 5.1 and Remark 5.2 use the same restricted equality discussion.

The target fills only this endpoint. It does not claim a new volume bound,
right-angled result, Coxeter classification, or higher-dimensional theorem.
Search ideal noncompact rigidity results before claiming novelty.

## Cheapest decisive attack and certificate

Let `u_i^+,u_i^-` be outward unit spacelike normals for the four opposite
facet pairs and put `x_i=<u_i^+,u_i^->`, `s_i=u_i^++u_i^-`, and
`d_i=u_i^+-u_i^-`. The cube incidences and common angle give every cross-pair
inner product as `-1/3`.

Audit the proposed implication that the four mutually orthogonal positive
vectors `d_i` span a positive 4-space, all `s_i` lie on its one-dimensional
negative orthogonal complement, and `s_i.s_j=-4/3` for `i!=j` forces
`s_i^2=-4/3` and hence `x_i=-5/3` for all `i`. A positive solution must supply
the full 8-by-8 Gram matrix, its rank/signature, sign consistency of the
collinear `s_i`, and a precise Lorentz-isometry-to-halfspaces argument. A
negative solution must give an explicit realizable Gram/halfspace system with
the frozen incidences and a different opposite-facet entry.

A matching Gram matrix alone is not enough unless realization and equality of
the resulting convex half-space intersection are justified.
