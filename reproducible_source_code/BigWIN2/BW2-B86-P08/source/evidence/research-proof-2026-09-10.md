# Proof dossier: direct scalene triangular facets force acuteness

Provenance: research job `win-00086-p08-research-f04f813e430b`, pass 1,
2026-09-10.  This is a proposed full resolution for fresh referee review, not
an acceptance record.

## Theorem

Let `T` be a nondegenerate scalene triangle, fix either of its planar
orientations, and let `P` be a full-dimensional compact convex three-polytope
whose facets are all direct copies of `T`: on every facet, the cyclic order of
the side lengths with respect to the outward normal is the fixed cyclic order
of `T`.  Then `T` is acute.  Consequently, if its side lengths satisfy

```
0 < a < b < c < a+b,             c^2 >= a^2+b^2,
```

no such `P` exists.

## 1. Oriented-link three-cycle lemma

Give the boundary of `P` the orientation specified in `source.md`: an ordered
facet `(p0,p1,p2)` is positive when
`((p1-p0) x (p2-p0)) dot n_out > 0`.  Positive boundaries of two adjacent
facets traverse their common edge in opposite directions.

Fix a vertex `v` of degree `d`.  Its link in the triangular boundary sphere is
a cycle.  Start with a positive incident facet `(v,u_0,u_1)`.  Across the edge
`vu_1`, compatibility of the two oriented facet boundaries forces the next
positive facet to have the form `(v,u_1,u_2)`.  Continuing around the link
gives distinct cyclic neighbors `u_0,...,u_{d-1}` such that every incident
facet is positively ordered as

```
(v,u_i,u_{i+1})                  (indices modulo d).
```

Put `r_i=|vu_i|` and `q_i=|u_i u_{i+1}|`.  Let `psi` send each side label to
the next label in the fixed positively oriented cyclic word of `T`.  The two
possible choices of reference orientation give the two inverse nontrivial
three-cycles on `{a,b,c}`; the following argument treats both at once.

The positive boundary word of the `i`-th facet is

```
(r_i, q_i, r_{i+1}).
```

Directness says that this is a cyclic rotation of the reference word.  Since
`T` is scalene, the labels are distinct, and hence

```
q_i = psi(r_i),                  r_{i+1} = psi^2(r_i).       (1)
```

After one circuit, closure requires
`r_0=r_d=psi^(2d)(r_0)`.  A nontrivial three-cycle fixes no label under its
first or second power, so `3` divides `d`.  In particular no direct oriented
vertex star of degree four or five is legal.  This proves the required local
lemma without choosing one of the two handedness classes.

## 2. Euler forces a degree-three vertex

All facets are triangles, so the boundary complex is a triangulated
two-sphere.  If it has `V,E,F` vertices, edges, and facets, then
`V-E+F=2` and `3F=2E`.  Also `sum_v deg(v)=2E`.  Eliminating `E,F` gives

```
sum_v (6-deg(v)) = 12.                                  (2)
```

Every vertex of a three-polytope has degree at least three, and Section 1
shows that every degree is a multiple of three.  If no vertex had degree
three, all degrees would be at least six and the left side of (2) would be
nonpositive.  Thus some vertex `v` has degree exactly three.

## 3. The degree-three star is a nondegenerate disphenoid

Write its cyclic neighbors as `u_0,u_1,u_2`.  From (1),

```
q_{i+1} = psi(r_{i+1}) = psi^3(r_i) = r_i.               (3)
```

The edge `u_{i+1}u_{i+2}`, of length `q_{i+1}`, is opposite the edge
`vu_i`, of length `r_i`, in the four-point configuration
`v,u_0,u_1,u_2`.  Thus its six edges occur in three equal opposite pairs.

These four points are affinely independent.  Indeed, any two consecutive
edge vectors `u_i-v,u_{i+1}-v` are independent because they span a
nondegenerate triangular facet.  If all three edge vectors were dependent,
the four points would lie in one plane `H`.  Each of the three distinct
incident triangular facets would then have affine hull `H`.  Since the affine
hull of a facet is a supporting plane and `P` intersected with a supporting
plane is one face, all three would have to be the same facet, a contradiction.
Hence the four points form a nondegenerate tetrahedron `K`.

The three faces of `K` containing `v` are actual facets and are congruent to
`T`.  Its fourth face has side lengths `q_0,q_1,q_2`; by (1) the radial labels
`r_0,r_1,r_2` are all three distinct labels and `psi` permutes them, so the
fourth face also has side lengths `{a,b,c}`.  Thus all four faces of `K` are
congruent to `T`.

For completeness, here is the acuteness part of the disphenoid calculation,
independently reproducing the decisive direction of Georgiou's Lemma 5.  Name
the vertices `A,B,C,D`, translate their centroid to the origin, and set

```
x = (A+B-C-D)/4,
y = (A-B+C-D)/4,
z = (A-B-C+D)/4.
```

Then

```
A=x+y+z,  B=x-y-z,  C=-x+y-z,  D=-x-y+z.
```

Equality of `AB` with its opposite edge `CD` gives `y dot z=0`; the other two
opposite-pair equalities similarly give `x dot z=0` and `x dot y=0`.
Nondegeneracy makes all three mutually orthogonal vectors nonzero.  After an
orthogonal change of coordinates, write their positive lengths again as
`x,y,z`.  Assigning the three opposite-pair lengths as `a,b,c` yields

```
a^2=4(y^2+z^2),  b^2=4(x^2+z^2),  c^2=4(x^2+y^2),
```

up to a permutation of the coordinate names.  Therefore

```
x^2=(b^2+c^2-a^2)/8,
y^2=(c^2+a^2-b^2)/8,
z^2=(a^2+b^2-c^2)/8.                                  (4)
```

All three are strictly positive.  In particular (4) gives
`a^2+b^2-c^2>0`, so `c^2<a^2+b^2`: the common triangle is acute.  This
contradicts the frozen right-or-obtuse hypothesis and proves the theorem.

## 4. Adversarial checks and scope

`evidence/audit_oriented_link.py` independently enumerates every cyclic
starting point for every face in degrees 3 through 8, separately for the two
reference words `(a,b,c)` and `(a,c,b)`.  It finds no degree-four or
degree-five star and verifies (3) for every degree-three star.  The earlier
radial-word enumeration in `evidence/check_oriented_stars.py` agrees through
degree 12.

No floating-point or geometric realization computation is used.  Convexity is
used in the supporting-plane argument, full dimensionality in ruling out a
flat three-edge star, triangular facets in the link and Euler counts,
scaleneness in turning cyclic words into a deterministic three-cycle, and
directness in (1).  The proof does not cover the excluded isosceles,
reflection-allowed, nonconvex, or lower-dimensional cases.  Known gaps in the
displayed mathematical chain: none identified by this research pass; fresh
referee review remains required.
