# Research proof and adversarial audit

Job: `win-00077-p01-research-92bec961d526` (research pass 1, 2026-09-09).

## Claim tested

Let `H = S_{2,1,1} disjoint-union K_2` have the injective, ordinary
non-induced interpretation fixed in `problem.md`.  For every integer `m >= 3`,
let

```
B_m = overline(K_2) + C_m,
```

where `a,b` are the nonadjacent vertices of `overline(K_2)` and
`v_0,...,v_{m-1}` are the rim vertices.  Colour precisely the `2m`
apex--rim edges red and the `m` rim-cycle edges blue.

## Uniform proof

Embed the rim as a Jordan cycle on the sphere and put `a` and `b` in its two
complementary discs.  Coning the rim from the apex in each disc gives the
`2m` triangular faces

```
a v_i v_{i+1},  b v_i v_{i+1}  (indices modulo m).
```

Thus `B_m` is planar.  It is simple, has `m+2 >= 5` vertices, and has
`2m+m = 3m = 3(m+2)-6` edges.  The planar edge bound therefore forbids adding
any missing edge while preserving planarity, so `B_m` is maximal planar.

The red graph is exactly `K_{2,m}` with parts `{a,b}` and the rim.  Consider
an injective red fork embedding and call its degree-three centre `s`, its
three neighbours `x,y,z`, and the distal vertex on the arm through `z` by
`w`.  The image of `s` has at least three distinct red neighbours.  Every
rim vertex has red degree two, so `s` maps to an apex.  Consequently `x,y,z`
map to three distinct rim vertices.  The only two red neighbours of the rim
vertex receiving `z` are the two apices.  Since one is already the image of
`s` and injectivity makes `w` distinct, `w` must map to the other apex.
Hence every red fork uses both apices.  Every red edge meets an apex, so no
red edge can be vertex-disjoint from such a fork.  There is therefore no red
copy of `H`.

The blue graph is exactly `C_m`, including `C_3` when `m=3`, and has maximum
degree two.  Since the fork centre requires three distinct blue neighbours,
there is no blue fork and hence no blue copy of `H`.

For every integer `n >= 5`, taking `m=n-2` supplies an `n`-vertex maximal
planar graph with an avoiding colouring.  Given any proposed threshold `N`,
choose `n=max(N,5)`.  This witnesses the formal negation in `problem.md`, so
the frozen eventual-unavoidability assertion is false.

## Directed attacks

1. **Could a red fork omit an apex?**  No.  The centre-degree argument forces
   its centre to one apex, and the length-two arm forces its distal vertex to
   the other.  This classifies every injective embedding; it does not assume
   an induced copy.
2. **Could extra host edges merge the nominal components?**  They do not
   matter for a non-induced copy, but injectivity still requires the `K_2`
   edge to have both endpoints outside the five fork vertices.  Both apices
   are already used, while every red edge meets one of them.
3. **Does the boundary `m=3` fail maximal planarity?**  No.  It is the
   triangular bipyramid `K_5-ab`, with the six displayed triangular faces and
   `9=3*5-6` edges.  The same spherical construction and edge-bound argument
   apply.  (It also has only five vertices, so cannot itself host the
   seven-vertex target.)
4. **Is the family merely finite or sparse in its orders?**  No.  Its orders
   are exactly `m+2`, hence every order at least five occurs.

The dependency-free program `evidence/research_independent_check.py` is a new
labelled-embedding implementation: for each tested `m` it enumerates every
injective image of the five fork labels, counts the red images, verifies that
each contains both apices, and searches for a disjoint same-colour edge.  Its
finite checks are encoding and boundary sanity checks, not the proof of the
universal parameter.

## Source and literature scope

The frozen source has SHA-256
`8dac979afd6c6ebb67e2f1b23bdb42cd5c37198b8c119d9f47d4f27a0e5be1d5`.
The locally identified primary-source PDF has SHA-256
`d2c05952bb165545210571a572678338e7766162141549adbf62411e3cf881b2`.
The PDF and official arXiv v1 were re-inspected: Definition 1 gives the
eventual quantifier, Section 1.2 fixes the fork and disjoint-union notation,
Theorem 12 settles the connected fork, and Problem 2 asks for the disconnected
diagonal classification.  The arXiv record showed only v1 on 2026-09-09.
Targeted arXiv searches found no separate exact-case primary result.  This is
only a bounded comparison; no priority or exhaustive novelty claim is made.

## Audit status

The mathematical gap list for the exact frozen disproof claim is empty in
this research pass.  Fresh referee review remains required by the workflow.
