# One high junction still cannot beat `39/8`

Provenance: `win-00044-p02-research-26df39e7c80a`  
Date: 2026-09-06

## Exact subsidiary theorem

Consider a cyclic weighted graph with 13 nonempty layers, at most four
vertices per layer, and edges only within a layer or between consecutive
layers. Suppose every vertex has weighted open-neighborhood at least one,
all weights are nonnegative, and the graph is `K_7`-free. Let `c_i` be the
number of vertices in layer `i`. If exactly one of the 13 boundaries has
`c_i+c_(i+1) >= 7`, then the total weight is at least

```text
4154/851 = 39/8 + 43/6808 > 39/8.
```

Thus a strict-mass witness in this four-slot, 13-layer model must have at
least two high boundaries. Allowing zero weights only strengthens the
statement as a lower bound for the intended positive-weight model.

## Reduction to 480 exact dual certificates

Rotate the unique high boundary to `{0,1}`. Its counts are `3+4`, `4+3`, or
`4+4`; reflection normalizes the unequal case to `3+4`. All other adjacent
count sums are at most six.

Complete every allowed edge outside the high two-layer union. This creates no
`K_7`, because every clique is contained in two consecutive layers and all
other such unions have at most six vertices. Inside a `3+4` union, an
edge-maximal `K_7`-free supergraph is the complete graph minus one edge. Up to
permutations within the two layers, the missing edge has three types: inside
the 3-layer, inside the 4-layer, or crossing.

For a `4+4` union, let `F` be the set of missing edges. `K_7`-freeness says
that for every vertex, `F` contains an edge not incident with that vertex;
equivalently, the edges of `F` have empty common intersection. Every such
`F` contains an inclusion-minimal subfamily which is either two disjoint
edges or the three edges of a triangle. Enumeration under `S_4 x S_4` gives
ten types. The script independently regenerates all 266 labeled minimal
families and checks that the ten hard-coded representatives are exhaustive.
Any original graph is a subgraph of one of these edge-maximal supergraphs, so
its feasible mass cannot be smaller.

Only coordinatewise-maximal count patterns need be checked. Enlarge any
ordinary layer while preserving the one-high-boundary condition. A feasible
weighting on the smaller complete-off-junction graph extends by giving each
new vertex weight zero: a new vertex's neighborhood contains the neighborhood
of an old vertex in its layer together with that old vertex, so its weighted
degree is at least one. Hence the minimum mass can only decrease when an
ordinary layer count is enlarged. A pattern is maximal exactly when every
ordinary coordinate below four lies on an ordinary boundary whose count sum
is six.

Direct integer enumeration gives 60 anchored maximal `3+4` patterns and 51
anchored maximal `4+4` patterns. Reflection fixing the high edge reduces the
latter to 30 representatives. This gives `60*3 + 30*10 = 480` linear
programs. For adjacency matrix `A`, each program is

```text
min 1^T w  subject to A w >= 1 and w >= 0.
```

Its dual is `max 1^T y` subject to `A^T y <= 1` and `y >= 0`. SciPy/HiGHS is
used only to discover `y`. Every coordinate is reconstructed as a
`fractions.Fraction`, after which nonnegativity, all dual inequalities, and
`1^T y >= 39/8` are checked exactly. The weakest of the 480 checked duals has
value `4154/851`; the script prints one such certificate.

## Reproduction and limits

Run `python3 evidence/one_high_junction.py`. The 2026-09-06 run checked all
480 certificates and reported the weakest case as count pattern

```text
3 4 2 3 3 3 3 3 3 3 3 3 3
```

with the missing edge inside the 3-layer. This is an exact exhaustive result
for the stated one-high-junction layered class. It says nothing about patterns
with two or more high boundaries, more than four vertices in a layer, edges
outside the layered locality rule, or general `K_7`-free graphs. The frozen
original problem therefore remains unresolved.
