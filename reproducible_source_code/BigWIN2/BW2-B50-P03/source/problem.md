# Precise problem: the four-color game on `M_3(C_3)`

## Frozen source and interpretation

The source statement is preserved verbatim in `source.md` (SHA-256
`c0d0c081d5a1c93fc6ff6d0ce06f2d863e7eae66def156bda26d1cd85a0f6b1c`).
This file fixes the following mathematical reading of it.

Let indices lie in `Z/3Z`. Define the finite simple graph

`H = M_3(C_3)`

with

`V(H) = {v_i^m : i in Z/3Z, 0 <= m <= 3} union {omega}`

and edge set

1. `{v_i^0 v_j^0 : i != j}`;
2. `{v_i^m v_j^(m+1) : 0 <= m <= 2 and i != j}`; and
3. `{v_i^3 omega : i in Z/3Z}`.

Here the inequalities between indices are in `Z/3Z`, and unordered edges are
listed only once. Thus `H` has 13 vertices and 24 edges. The nine vertices in
layers 0, 1, and 2 have degree 4; the three vertices in layer 3 and `omega`
have degree 3. In particular, `Delta(H)=4`.

For a positive integer `q`, let the common color set be `[q]={1,...,q}`. A
position is a partial proper coloring `phi:S->[q]`, where `S` is a subset of
`V(H)`. Alice moves first; thereafter Alice and Bob alternate. A legal move
chooses one vertex `v` outside `S` and one color absent from the already
colored neighbors of `v`, and extends `phi` by that assignment. Alice wins if
all 13 vertices are colored. Bob wins as soon as some uncolored vertex has no
legal color. Since the game is finite and has perfect information, every
position has a determined winner.

The requested proposition is the dichotomy

`Alice has a winning strategy from the empty position when q=4`

versus

`Bob has a winning strategy from the empty position when q=4`.

No assertion is made for any other layer parameter `k`. By Mou--Sun--Zhang,
Theorems 3.1 and 5.1(1), `4 <= chi_g(H) <= 5`. Consequently an Alice win for
`q=4` proves `chi_g(H)=4`, while a Bob win for `q=4`, together with their
five-color upper bound, proves `chi_g(H)=5`.

## Prior result, delta, and verification route

Nearest verified prior result: Yushuang Mou, Qiang Sun, and Chao Zhang, *The
game chromatic number of generalized Mycielski graphs of paths and cycles*,
arXiv:2609.02283v1 (2026), Definition 2.1 (PDF page 4), Theorem 3.1 (PDF pages
6--7), and Theorem 5.1(1) (PDF page 14), proves only
`4 <= chi_g(M_k(C_3)) <= 5` for every `k>=2`. The exact `k=3` value is not
given. The paper's Proposition 2.1 records exact results only for the classical
one-layer construction among the triangular cases.

Proposed delta: determine the exact value for the fixed 13-vertex `k=3` graph.

Verification route: perform exact minimax search for `q=4` and emit the
reachable winning strategy DAG for the winning player. A replay checker must
reconstruct the graph independently and verify every move's legality, every
terminal label, the appropriate existential/universal minimax condition at
each node, completeness of opponent replies, color-renaming canonicalization,
and graph-automorphism canonicalization. Sample plays or a numerical solver
summary do not suffice. The graph has six automorphisms (simultaneous
permutations of the three indices), as independently enumerated by
`evidence/validate_graph.py`; a verifier should enumerate rather than assume
that group.

## Scope and source-status caution

This is a precise generated refinement of a gap in a primary paper, not a
claim that the authors explicitly advertised the single `k=3` case as an open
problem. Exact-assertion and equivalent-language searches on 2026-09-07 found
no primary paper settling it, but absence from those searches is not proof of
priority or open status. The working source status is therefore `new-question`
with novelty still to be rechecked before any release claim.
