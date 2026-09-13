# Fresh mathematical audit

## Frozen scope and integrity

I reviewed the exact claim frozen by snapshot digest
`0ecbd967a46f945bd6835b7187032eedfcef4d2f0e168b18c9337c6ecc300ddd`:
for the simple graph `C_8 \square C_8`, under the synchronous threshold-three
process specified in `source.md` and `problem.md`, the claimed value is
`t_3(8,8)=22`. I recomputed SHA-256 for `claim.json` and every enumerated
evidence file; all values agree with `audit/snapshot.json`. The graph has the
64 labelled vertices `(i,j)` with coordinates modulo 8, and its four listed
neighbors are distinct at every vertex.

## Reconstruction of the lower bound

Fix an initially infected set `S`, and let `R` be the vertices still
uninfected at some round. Since the ambient graph is 4-regular, a vertex of
`R` has at least three infected neighbors if and only if its degree in the
induced graph `G[R]` is at most one. Thus one synchronous infection round is
exactly simultaneous deletion of all degree-zero and degree-one vertices
from `G[R]`.

Starting with `U=V\S`, this deletion exhausts `U` if and only if `G[U]` is a
forest. Indeed, the vertices of any cycle retain their two cycle neighbors
through every deletion round, while every nonempty finite forest has a vertex
of degree at most one and repeated leaf deletion empties it. This proves the
equivalence needed here without a limiting or ordering assumption.

Suppose now that `S` percolates, put `k=|S|` and `u=64-k`, and first take
`u>0`. If the forest `G[U]` has `c>=1` components, then it has `u-c` edges.
Writing `b` for the number of edges from `U` to `S`, degree counting on `U`
gives

`4u = 2(u-c)+b`, hence `b=2u+2c`.

Degree counting on `S` gives `4k=2e(S)+b>=b`. Consequently

`4k >= 2u+2c >= 2(64-k)+2`,

so `6k>=130` and the integrality of `k` yields `k>=22`. The omitted case
`u=0` has `k=64` and already satisfies the conclusion. This establishes the
lower bound for every initially infected set, including empty and degenerate
choices, with no symmetry assumption.

## Independent witness and trace checks

I first ran the frozen dependency-free verifier with the required research
interpreter. It reported successful exact checks, final infected size 64,
layer sizes

`[22,14,4,3,2,2,2,2,2,2,2,2,2,2,1]`,

and a 42-vertex complement having one component and 41 induced edges.

I then made a separate exact recomputation directly from the serialized JSON,
without importing either frozen Python program. That recomputation:

- parsed every coordinate and checked that all 64 displayed vertices occur
  exactly once across the layers;
- rebuilt the four-neighbor torus from modular arithmetic;
- at each of rounds 1 through 14 formed the full set of uninfected vertices
  with at least three infected neighbors and obtained exactly the certified
  layer;
- independently performed degree-at-most-one peeling on the initial
  42-vertex complement and obtained the same 14 layers; and
- independently counted 41 complement edges and reached all 42 complement
  vertices by breadth-first search, certifying that the complement is a tree.

The exact output was

`{"complement_connected":true,"complement_edges":41,"complement_vertices":42,"counting_lower_bound_minimum_k":22,"independent_verified":true,"layer_sizes":[22,14,4,3,2,2,2,2,2,2,2,2,2,2,1],"leaf_layers_match":true,"vertices_covered_once":64}`.

This verifies both the explicit 22-set and the stronger requirement that each
listed synchronous layer is equal to, rather than merely contained in, the
eligible set. The floating-point MILP witness finder in `evidence/search_22.py`
is therefore not used as proof and no negative certificate is needed for the
value 22.

## Scope, prior-result comparison, and gaps

Within the frozen evidence, `source.md` and `problem.md` identify the nearest
prior result as the one-unit bound `22<=t_3(8,8)<=23`. The submitted result
adds an explicit exact 22-vertex trace, while its self-contained counting
argument supplies the matching universal lower bound. It therefore resolves
the full fixed `8 x 8` question, not a subsidiary restriction. It asserts
nothing for other dimensions and makes no literature-priority claim. The
user-imposed evidence boundary did not include the cited primary PDF, so I do
not independently certify its bibliography or priority; neither is needed for
the mathematical claim submitted here.

I found no unresolved mathematical gap in the frozen claim. The decisive
proof is finite, exact, and independent of the heuristic search route.

## Verdict

**Accept.** The frozen `resolution-paper` scope, correctness/evidence, and
contribution all pass: the lower bound quantifies over every initial set, and
the exact 22-set settles the matching upper bound.
