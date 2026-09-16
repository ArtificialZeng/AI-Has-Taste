# Frozen source problem: orientation-preserving monohedral nonexistence for right or obtuse scalene triangles

Canonical id: win-00086-p08
Frozen on: 2026-09-10 (Asia/Shanghai)
Batch source: `batches/inbox/bigWin-86.raw.md`, item 8 (preserved verbatim there)
Primary source:
- George M. Georgiou, *Congruent Triangular Faces, Reflections Allowed: Universal Realization and the Minimum Face Count in Problem B22*, arXiv:2608.01109v1. See Theorems 1--2, Remark 3, Lemma 5, and the discussion of the orientation-preserving case.

## Definitions

Fix a nondegenerate scalene triangle `T` whose side lengths satisfy

```
0 < a < b < c < a+b,   c^2 >= a^2+b^2.
```

Give `T` one of its two planar orientations. A triangular facet of a full-dimensional convex three-polytope is oriented by its outward normal. It is a *direct copy* of `T` when the cyclic order of the three side lengths around its positively oriented boundary agrees with that of `T` (up to cyclic rotation, not reversal).

An orientation-preserving monohedral realization of `T` is a full-dimensional compact convex three-polytope all of whose facets are direct copies of `T`.

## Statement

Prove that no orientation-preserving monohedral realization exists for any right or obtuse scalene triangle `T` as above.

Equivalently: if a full-dimensional convex three-polytope has triangular facets all directly congruent to one scalene triangle, then that triangle is acute.

## Required proof certificate

The proposed route must be checked rather than assumed:

1. Label each polytope edge by its length `a`, `b`, or `c`. Prove from the common boundary orientation that, around the oriented link of every vertex, successive radial-edge labels advance by the same nontrivial three-cycle. Deduce `3 | deg(v)` for every vertex.
2. Use the Euler relation for a triangulated sphere to prove that some vertex has degree three.
3. For a degree-three vertex `v` with neighbors `x,y,z`, prove that the three edge rays are linearly independent and that the six edges of the tetrahedron `vxyz` occur in three equal opposite pairs. Hence all four faces of this nondegenerate tetrahedron are congruent to `T`.
4. Verify and invoke Georgiou's Lemma 5: a nondegenerate tetrahedron with four faces congruent to `T` exists only when `T` is acute. This contradicts `c^2 >= a^2+b^2`.

The audit must explicitly check that the source's meaning of “without reflected copies” is exactly the direct-copy convention above. Any legal degree-four or degree-five oriented vertex star, or any failure of the degree-three opposite-edge conclusion, refutes this proof route and must be reported.

## Scope and contribution boundary

This project addresses only the orientation-preserving right/obtuse scalene remainder identified by the primary source. The reflection-allowed eight-face construction, the acute case, and the isosceles case are prior results and must not be claimed as new.

Before asserting novelty, check the latest version of arXiv:2608.01109 and later literature for this exact statement or an equivalent oriented-triangulation lemma. Any manuscript must cite the primary source and the directly relevant polyhedral and triangulation literature actually used. It must additionally include one or two genuinely relevant papers from the user's Excel library when available; that is a minimum, not a bibliography cap, and unrelated entries must never be padding.

This file is immutable. Dropping convexity, full dimensionality, scaleneness, or the direct-copy condition changes the problem.
