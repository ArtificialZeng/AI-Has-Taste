# Precise problem reading

Provenance: triage job `win-00086-p08-triage-d046b1acf988` on
2026-09-10 (Asia/Shanghai). The frozen statement remains in `source.md`
(SHA-256 `632785ab658794d69c91c6eab35d1b0a25c3920a2f2b9c8870597ba28ff4f9aa`).

## Objects and conventions

Let `a,b,c` be real numbers satisfying

```
0 < a < b < c < a+b,        c^2 >= a^2+b^2.
```

Thus there is a nondegenerate scalene Euclidean triangle `T` with these side
lengths, and, because `c` is its longest side, `T` is right or obtuse. Fix one
of the two orientations of the plane of `T`.  Its positively oriented cyclic
side-length word is one of the two cyclic order classes represented by
`(a,b,c)` and `(a,c,b)`.  Let `psi` be the corresponding next-label
permutation.  Thus `psi` is one of the two nontrivial three-cycles on
`{a,b,c}`; reversing the chosen orientation replaces `psi` by `psi^(-1)`.

A candidate realization is a full-dimensional compact convex polytope
`P` in `R^3`. “Facet” means a two-dimensional face of `P`, not a triangle in
an auxiliary subdivision. Each facet is required to be triangular. Its outward
normal orients its affine plane: an ordered vertex triple `(p0,p1,p2)` is
positive when

```
((p1-p0) x (p2-p0)) dot n_out > 0.
```

The corresponding boundary side word is
`(|p0p1|,|p1p2|,|p2p0|)`. The facet is a **direct copy** of `T` exactly when
this word is a cyclic rotation of the actual positively oriented word of `T`;
the reverse cyclic class is forbidden.  In the first of the two reference
orientations these rotations are `(a,b,c)`, `(b,c,a)`, `(c,a,b)`, and in the
other they are the three reversed words.  This is the “without reflected
copies” convention used in Remark 3 of the cited paper: handedness is read
cyclically with respect to the outward normal. Adjacent facets carry the
compatible boundary orientation of the oriented sphere and hence traverse
their common edge in opposite directions.

For a vertex `v`, `deg(v)` is the number of incident polytope edges. Since all
facets are triangles, the boundary complex is a simplicial two-sphere.

## Quantified assertion

For every real triple `(a,b,c)` satisfying the displayed inequalities and for
either orientation of a triangle `T` with those side lengths, there does not
exist a full-dimensional compact convex three-polytope every facet of which is
a direct copy of `T`.

Equivalently within the scalene setting: if such an orientation-preserving
monohedral convex three-polytope exists, then its common triangle is acute,
i.e. its largest squared side satisfies `c^2 < a^2+b^2`.

## Status, nearest result, and proposed delta

George M. Georgiou, *Congruent Triangular Faces, Reflections Allowed:
Universal Realization and the Minimum Face Count in Problem B22*,
arXiv:2608.01109v1 (2026), proves universal realization when reflections are
allowed (Theorem 1), determines the reflection-allowed minimum (Theorem 2),
and proves that a tetrahedron has four congruent triangular faces exactly for
an acute triangle (Lemma 5). Remarks 3 and the concluding discussion state
that the eight-face construction mixes the two handedness classes and leave
the orientation-preserving right/obtuse scalene case open. As checked on
2026-09-10, the arXiv submission history still listed only v1.

Source status is therefore **open-supported**, not independently established
priority. Exact-phrase and equivalent-language searches on 2026-09-10 found
no later primary result beyond Georgiou, but that negative search is not proof
of novelty.

The proposed delta is to resolve precisely this remainder. The bounded route
is: prove the oriented-link three-cycle lemma; combine it with
`sum_v (6-deg(v))=12` to obtain a degree-three vertex; show its three edge rays
are independent and its six induced tetrahedral edges come in equal opposite
pairs; then apply Georgiou's Lemma 5. Exact local enumeration is an available
verifier, and a legal degree-four or degree-five direct-copy star would refute
the route.

## Scope exclusions

No claim is made here about reflected-copy realizations, acute triangles,
isosceles triangles, nonconvex or lower-dimensional objects, polygonal facets,
or classifications of attainable face counts. Changing any of convexity, full
dimensionality, scaleneness, or the direct-copy condition changes the problem.
