# Fresh mathematical referee report

Job: `win-00086-p08-referee-d2d0691a5748`  
Frozen snapshot: `d7d252a694b3733567d7726a45ff437dce9282245aa72bbca547cd5cfdec30d9`

## Scope reviewed

I reviewed the exact `resolution-paper` claim frozen in `claim.json`: for every
nondegenerate scalene triangle with

```
0 < a < b < c < a+b,     c^2 >= a^2+b^2,
```

and either fixed orientation, no full-dimensional compact convex
three-polytope can have every facet a direct copy in the outward-normal cyclic
side-order sense. This is the full scope of `source.md`, with none of
convexity, full dimensionality, scaleneness, or the direct-copy condition
removed or weakened.

All files in `audit/snapshot.json` were rehashed before review. Every digest
matched the frozen mapping, including the source digest
`632785ab658794d69c91c6eab35d1b0a25c3920a2f2b9c8870597ba28ff4f9aa`.

## Reconstruction of the decisive argument

Let `psi` be the next-label permutation in the fixed positively oriented word
of the scalene triangle. It is one of the two nonidentity 3-cycles on
`{a,b,c}`.

At a vertex `v`, orient its cyclic link so that its incident facets have
positive vertex orders

```
(v,u_i,u_{i+1}).
```

This order is forced consistently because two positively oriented adjacent
facets traverse their common edge in opposite directions. With
`r_i=|vu_i|` and `q_i=|u_i u_{i+1}|`, the positive side word of this facet is
`(r_i,q_i,r_{i+1})`. Directness and scaleneness therefore force, rather than
merely permit,

```
q_i = psi(r_i),       r_{i+1} = psi^2(r_i).                 (1)
```

Thus successive radial labels advance by the same nontrivial 3-cycle.
Closing a link of degree `d` requires `psi^(2d)(r_0)=r_0`, which holds only
when `3 | d`. This treats both orientations because replacing `psi` by its
inverse does not change the conclusion. In particular, degree-four and
degree-five direct stars are impossible.

For the triangulated boundary sphere, Euler's relation and `3F=2E` give

```
sum_v (6-deg(v)) = 12.                                    (2)
```

Every polytope vertex has degree at least three, and every degree is now a
multiple of three. If all degrees were at least six, the left side of (2)
would be nonpositive. Hence a degree-three vertex exists.

At such a vertex, (1) gives

```
q_{i+1} = psi(r_{i+1}) = psi^3(r_i) = r_i.
```

Consequently each radial edge `vu_i` equals the opposite edge
`u_{i+1}u_{i+2}` in the four-vertex configuration. The three rays at `v` are
linearly independent: any two span a nondegenerate triangular facet; if all
three lay in one plane `H`, all three distinct incident triangular facets
would have affine hull `H`. But a facet plane of a convex three-polytope is a
supporting plane, and `P intersection H` is one face, so three distinct facets
cannot share that affine hull. The four vertices therefore form a
nondegenerate tetrahedron. Its three faces through `v` are copies of `T`, and
its fourth face has the three labels `q_0,q_1,q_2`, hence also the side set
`{a,b,c}`. It is a tetrahedron with three equal pairs of opposite edges and
all four faces congruent to `T`.

The final acuteness step is independently derivable and is not left as a
black-box citation. After translating the tetrahedron's centroid to zero, set

```
x=(A+B-C-D)/4,  y=(A-B+C-D)/4,  z=(A-B-C+D)/4.
```

Then its vertices are `x+y+z`, `x-y-z`, `-x+y-z`, and `-x-y+z`.
Equality of each opposite edge pair gives respectively
`y dot z=x dot z=x dot y=0`. Nondegeneracy makes `x,y,z` nonzero. Assigning
the three opposite-pair lengths to `a,b,c` and solving yields, up to the
corresponding coordinate permutation,

```
|x|^2=(b^2+c^2-a^2)/8,
|y|^2=(c^2+a^2-b^2)/8,
|z|^2=(a^2+b^2-c^2)/8.
```

All three squares are strictly positive. In particular
`a^2+b^2-c^2>0`, contradicting the frozen right-or-obtuse hypothesis. This
also independently verifies the necessary direction of Georgiou's Lemma 5.

## Checks performed

- I checked both possible reference cyclic words. The derivation uses only
  that `psi` is a nontrivial 3-cycle, so neither orientation is privileged.
- I reran both frozen exact enumerators successfully. I also used a separate
  brute-force encoding that independently chose every radial and link label
  for degrees three through five and tested membership in the three direct
  rotations. For each handedness its counts were exactly `3,0,0`; hence it
  found no legal degree-four or degree-five star. The calculation is ancillary
  to the direct proof of (1).
- I checked the degree-three indexing: the edge opposite `vu_i` is
  `u_{i+1}u_{i+2}=q_{i+1}`, exactly the edge shown equal above.
- I checked the potentially delicate flat-star case using the supporting-face
  property, so affine independence is not being assumed from degree alone.
- There is no division by a variable, limiting argument, compactness passage,
  numerical approximation, or unproved equality case in the proof. The right
  case gives a zero coordinate square and hence a degenerate tetrahedron, so
  strict acuteness is correctly obtained.
- The primary arXiv source was checked directly on 2026-09-10. The abstract
  page still lists only arXiv:2608.01109v1. Its Section 1 says ordinary
  congruence includes orientation reversal; Remark 3 distinguishes the two
  handedness classes by cyclic side order with respect to the outward normal
  and calls them direct versus mirror-image copies. For a scalene triangle
  this is exactly the frozen direct-copy convention. Its Lemma 5 contains the
  same disphenoid coordinate identities, and its concluding discussion says
  the orientation-preserving problem remains open precisely for right and
  obtuse scalene triangles.
- A bounded current search using the exact title, the remainder's wording,
  and the oriented edge-label formulation found no later equivalent primary
  result. This is only a dated literature screen, not a priority guarantee;
  the candidate likewise makes no claim of priority.

## Source comparison, gaps, and contribution

Georgiou's reflection-allowed construction does not prove the candidate: its
scalene facets split into four direct and four mirror-image copies. The
candidate supplies the missing orientation-sensitive local lemma, then uses
Euler curvature to reduce the global problem to the source's four-face
obstruction. The delta is full-scope, short but nonroutine, and directly
resolves the explicitly identified remainder. It does not claim the
reflection-allowed construction, acute case, isosceles case, or face-count
classification as new.

No mathematical or scope gap remains in the frozen candidate. The exact claim,
evidence, and stated contribution pass review.

## Verdict

**Accept.** The frozen argument proves the original statement in its full
quantified scope, its decisive local and tetrahedral steps withstand the
specified adversarial checks, and its contribution boundary is honest.
