# Precise problem statement

Triage provenance: `win-00077-p01-triage-8ca907fc3a49` (2026-09-09).

## Frozen source and scope

The immutable statement is in `source.md` (SHA-256 at triage:
`8dac979afd6c6ebb67e2f1b23bdb42cd5c37198b8c119d9f47d4f27a0e5be1d5`).
This file fixes its mathematical reading; it does not alter the source.

All graphs are finite and simple.  A **maximal planar graph** is an
edge-maximal planar graph: no edge can be added between two nonadjacent
vertices while retaining planarity.  For the orders relevant here this is
equivalently the abstract graph of a plane triangulation.

Let the fork `S_{2,1,1}` have five distinct vertices
`s,x,y,z,w` and edges

```
sx, sy, sz, zw.
```

Thus `s` has degree three, and `s-z-w` is the arm of length two.  Let

```
H = S_{2,1,1} disjoint-union K_2.
```

Equivalently, `H` has seven vertices `s,x,y,z,w,u,v` and five edges
`sx,sy,sz,zw,uv`, with all seven labels distinct.

A red (respectively blue) **non-induced copy** means an injective placement of
these seven vertices for which the five displayed edges exist and all have the
specified colour.  Extra host edges among the seven selected vertices are
irrelevant, including extra edges between the two nominal components.  In
particular, the `K_2` component is an edge whose two endpoints are
vertex-disjoint from the five vertices used by the fork; it need not be
anticomplete to the fork.

## Quantified assertion and its negation

The assertion asks whether

```
there is N in the positive integers such that, for every integer n >= N,
for every n-vertex maximal planar graph G, and for every total map
c:E(G)->{red,blue}, G has a red copy of H or a blue copy of H.
```

Its exact negation is: for every positive integer `N`, there are an integer
`n >= N`, an `n`-vertex maximal planar graph `G`, and a red/blue colouring of
all of `E(G)` having neither a red nor a blue copy of `H`.  Hence an explicitly
proved avoiding family of unbounded order disproves the assertion; one finite
avoiding example does not.

## Prior result, exact delta, and triage target

Baldacchino--Caro--Mifsud, arXiv:2609.05268v1, Definition 1 uses exactly the
eventual quantifier above.  Its Theorem 12 states
`r_MP(S_{2,1,1},S_{2,1,1})=9`, and its Problem 2 asks for the disconnected
diagonal classification.  The exact individual graph in this file is not
stated separately in the inspected v1 text.  The bounded exact-case search on
2026-09-09 found no separate primary result, so the literature status is
`status-uncertain`: this is a sourced specialization of the open
classification, not an independently documented open problem and not a
novelty claim.  The nearest prior result is the connected fork; the delta is
one vertex-disjoint edge in the same monochromatic copy.

The proposed resolution target is the following unbounded construction.  For
each `m >= 3`, take the bipyramid

```
B_m = independent-set-on-{a,b} join C_m,
```

colour every apex--cycle edge red, and every cycle edge blue.  The verification
route is (i) certify that `B_m` is a maximal planar triangulation, (ii) classify
all red fork embeddings, and (iii) use the maximum degree of the blue graph.
This is a triage target, not yet an independently refereed resolution.
