# Exact rank-ten bound for nonsingular induced tree cores

## Theorem

Let `G` be a reduced graph whose real adjacency rank is ten.  If `G`
contains a nonsingular induced subgraph `H` on ten vertices and `H` is a
tree, then

```text
|V(G)| <= 62.
```

## Proof

Let `B=A(H)`.  Since `B` is a nonsingular principal matrix of order ten and
`rank A(G)=10`, it is a full-rank principal core.  Write `v_u` for the binary
adjacency profile of a vertex `u` on the ten core vertices.  The exact
principal-core identity is

```text
A(G)_{uv} = v_u' B^{-1} v_v.                 (1)
```

Looplessness and simplicity imply

```text
v_u' B^{-1} v_u = 0,
v_u' B^{-1} v_v in {0,1} for u != v.         (2)
```

No profile is zero, because (1) would then make the full adjacency row zero.
No two profiles are equal, because (1) would make their full adjacency rows
equal.  These conclusions use reducedness, not a numerical rank test.

The ten core vertices have as profiles the ten columns of `B`.  These
profiles are distinct and universal in the compatibility graph: for every
binary profile `v` and every core column `b_i=Be_i`,

```text
b_i' B^{-1} v = v_i in {0,1}.                (3)
```

Thus the profiles of vertices outside `H` form a clique in the noncore
compatibility graph obtained after removing those ten universal columns.  If
`|V(G)|>=63`, that graph contains a clique of size at least 53.

There are exactly 106 isomorphism classes of trees on ten vertices.  The
frozen exact computation enumerates all of them.  Exact determinants show
that 91 have singular adjacency matrix and 15 are nonsingular.  For each of
the 15 nonsingular matrices, every one of the `2^10-1=1023` nonzero binary
profiles and every pairwise compatibility edge is rebuilt exactly, and an
exhaustive target-clique search proves that no 53 noncore profiles are
mutually compatible.  Therefore the clique forced by `|V(G)|>=63` cannot
exist.  This proves the theorem.

## Independent definition-level certificate

Discovery source:

```text
work/builder/tree_core_exact_search.json
SHA-256 1bdc9e089030ae02b67042e437fcb5cc9249cd841aeb85fac4cfc4858d4072d4
```

Independent no-import verifier and audit:

```text
src/linear_verify_tree_core_family.py
SHA-256 74b88115c292328d5509cf713a17e0213063b0e56f2532f369b5834d4272fd1b

work/linear_extension/tree_core_family_audit.json
SHA-256 f7ccf3e4d5a9500ea6f7c479f78b5a630b8b2ccce2bd47ac92db32eb6d91dbc8
```

The independent verifier does not import the builder and does not trust its
AHU codes, graph6 strings, tree indices, determinants, compatibility counts,
or branch transcripts.

1. Starting with one vertex, it adds a leaf at every possible vertex and
   deduplicates using a separately written center-rooted AHU code.  The free
   tree layer counts are

   ```text
   1,1,1,2,3,6,11,23,47,106.
   ```

   Rooting every independently generated free tree at every vertex gives the
   independent rooted-tree counts

   ```text
   1,1,2,4,9,20,48,115,286,719.
   ```

   The 106 source edge lists are checked to be trees and are matched as a set
   to the 106 independent canonical codes.  Duplicates or omissions fail.
2. It computes every determinant by fraction-free Bareiss elimination and
   independently counts perfect matchings.  For every ten-vertex tree it
   verifies `det A(T)=-(number of perfect matchings)^2`; hence the 15
   nonsingular trees each have determinant `-1` and a unique perfect
   matching.
3. For each nonsingular core it reconstructs `adj(B)` from integer cofactors,
   checks both `B adj(B)=det(B)I` and `adj(B)B=det(B)I`, enumerates all 1,023
   masks, verifies the core columns and their universality, removes them, and
   reconstructs every compatibility edge using

   ```text
   v' adj(B) w in {0,det(B)}.
   ```

4. The independent tree representative already changes the coordinate/mask
   order.  The verifier additionally applies a nonzero cyclic relabelling to
   each compatibility graph before its exact target search, so it does not
   replay the source branch transcript.  Greedy proper colourings give only
   rigorous clique upper bounds; every unpruned branch is explored.  The 15
   searches make 760,220 recursive calls and all return `false` for target
   53.

The clique engine is first checked against literal subset enumeration for
every labelled graph through order five and 100 deterministic random graphs
at each order six through nine, with every target size tested.  All 1,500
graph tests pass.  A bad frozen-source hash fails before output is written.

All determinant, profile, edge, and search decisions use integer arithmetic.
No floating-point spectrum is used as proof.

## Scope

The theorem covers every reduced rank-ten graph that contains a nonsingular
induced ten-vertex **tree** core.  It does not prove that every connected
rank-ten graph has a tree core: Wang--Guo guarantees a connected
nonsingular ten-vertex induced core, but that core may contain cycles.  Thus
the full rank-ten rank--order conjecture remains open after this result.

