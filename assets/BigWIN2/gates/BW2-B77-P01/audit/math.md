# Fresh mathematical referee report

Referee job: `win-00077-p01-referee-d35aeadf4c82`  
Frozen snapshot: `ebd922193e2f098ecb66a32c89868ab4d61bdfe1170e7cce9d9f4668b72675b6`

## Scope reviewed

I reviewed the exact `resolution-paper` claim frozen in `claim.json`: for every
integer `m >= 3`, the bipyramid

```
B_m = overline(K_2) + C_m
```

with all apex--rim edges red and all rim edges blue is a maximal planar graph
with no monochromatic copy of
`H = S_{2,1,1} disjoint-union K_2`.  Copies are injective ordinary subgraphs,
so the extra edge in `H` must have both endpoints outside the five vertices of
the fork, while extra host edges are immaterial.

I recomputed every file hash in `audit/snapshot.json` and recomputed its
canonical digest.  They agree with the frozen snapshot above.

## Reconstruction of the decisive argument

Let the two nonadjacent apices be `a,b`, and let the rim be the Jordan cycle
`v_0,...,v_{m-1}`.  Put `a` and `b` in the two complementary discs of the rim
on the sphere and join each apex to every rim vertex within its own disc.
This is a planar embedding whose faces are

```
a v_i v_{i+1}  and  b v_i v_{i+1}
```

with indices modulo `m`.  The graph is simple, has `m+2` vertices, and has
`2m+m=3m=3(m+2)-6` edges.  Adding any missing edge would violate the simple
planar edge bound, so it is maximal planar.  The boundary value `m=3` is not a
degeneracy: this construction is the triangular bipyramid `K_5-ab`, with the
same six triangular faces.

The red graph is exactly `K_{2,m}`, with bipartition
`{a,b}` and the rim.  In any injective red fork, the image of the degree-three
centre must have at least three red neighbours.  Every rim vertex has red
degree two, so the centre is an apex.  Its three fork neighbours are distinct
rim vertices.  The rim vertex on the length-two arm has only the two apices as
red neighbours; injectivity therefore forces the distal endpoint of that arm
to be the other apex.  Thus every red fork uses both apices.  Every red edge
meets an apex, so no red edge is vertex-disjoint from such a fork.  There is no
red copy of `H`.

The blue graph is exactly `C_m`, including `C_3` at the boundary.  Its maximum
degree is two, so it has no copy of the fork and hence no blue copy of `H`.

Finally, the orders of these graphs are all integers `m+2 >= 5`.  Given any
proposed eventual threshold `N`, set `n=max(N,5)` and `m=n-2`.  The resulting
`n`-vertex maximal planar graph has an avoiding colouring.  This is precisely
the negation of the quantified assertion in `source.md`, not merely a finite
lower-bound example.

## Checks actually performed

- I inspected the supplied proof and verifier rather than treating their PASS
  line as proof.  The labelled search enforces injectivity and tests the
  required edges only, which matches the non-induced interpretation.
- I separately implemented a direct search for a five-vertex fork followed by
  a vertex-disjoint same-colour edge.  For every `3 <= m <= 40` it found no
  copy of `H` in either colour.  I also independently checked the triangular
  face incidences, Euler count, edge count, and the `m=3` boundary.  These
  finite computations are sanity checks; the universal conclusion follows
  from the reconstruction above.
- I inspected the supplied primary-source PDF (SHA-256
  `d2c05952bb165545210571a572678338e7766162141549adbf62411e3cf881b2`).
  Definition 1 has the eventual-unavoidability quantifier used here; its
  notation defines the fork and disjoint union as used in the frozen reading;
  Theorem 12 settles the connected fork with Ramsey number 9; and Problem 2
  leaves the disconnected diagonal classification open.  The exact
  fork-plus-edge case is not stated there.  Theorem 11 concerns linear forests
  and does not cover this degree-three graph.

## Contribution and gaps

The construction settles the frozen original assertion in its full scope and
does so uniformly at every order at least five.  It is not a subsidiary
counterexample and does not claim to classify all disconnected graphs.  The
supplied literature comparison is explicitly bounded and makes no priority or
exhaustive-novelty claim; the verified source comparison supports the stated
exact delta from the connected-fork result.  I found no mathematical gap,
quantifier mismatch, exceptional value of `m`, or hidden induced-copy
assumption in the frozen claim.

## Verdict

**Accept.**  Scope, correctness, exact counterexample evidence, and the stated
contribution all pass for the frozen `resolution-paper` claim.
