# Exact rank-ten bound for nonsingular induced unicyclic cores

## Theorem

Let `G` be a reduced graph whose real adjacency rank is ten.  If `G`
contains a nonsingular induced subgraph `H` on ten vertices and `H` is
connected and unicyclic, then

```text
|V(G)| <= 62.
```

The bound is sharp within this class.

## Principal-core reduction

Put `B=A(H)`.  Since `B` is a nonsingular principal matrix of order ten and
`rank A(G)=10`, block elimination gives, for the binary core profiles `v_u`,

```text
A(G)_{uv} = v_u' B^{-1} v_v.                 (1)
```

Looplessness gives `v_u' B^{-1}v_u=0`; simplicity gives
`v_u' B^{-1}v_v in {0,1}` for distinct vertices.  Reducedness excludes the
zero profile and repeated profiles.  The ten profiles belonging to the core
are the columns `Be_i`, and each is universal because

```text
(Be_i)' B^{-1}v = v_i in {0,1}.              (2)
```

Consequently, if `|V(G)|>=63`, the noncore compatibility graph contains a
clique of size `63-10=53`.

## Complete unicyclic domain

A connected unicyclic graph has a unique cycle.  Delete its cycle edges.
What remains is a rooted tree at each cycle vertex.  Hence every ten-vertex
unicyclic graph is obtained from a cycle of length `k`, `3<=k<=10`, by an
ordered cyclic list of rooted unlabelled trees whose orders sum to ten.
Conversely every such decorated cycle is connected and unicyclic.

The rooted-tree AHU words determine the rooted branches up to isomorphism.
An isomorphism of unicyclic graphs must preserve the unique cycle and acts on
it by a rotation or reflection.  Thus two decorated cycles are isomorphic
exactly when their cyclic word lists lie in the same dihedral orbit.  Taking
the lexicographically least rotation/reflection is therefore a complete
canonical label.

The discovery program also generates the domain by a different route: it
adds every possible nonedge to every one of the 106 unlabelled ten-vertex
trees.  Deleting any cycle edge proves completeness of this route.  The two
routes give the same 657 canonical objects.  Their distribution by unique
cycle length is

```text
cycle length:  3   4   5   6   7  8  9  10
graph count: 299 202  89  45  14  6  1   1.
```

Exact Bareiss determinants give 521 singular and 136 nonsingular cores.  The
determinant distribution is

```text
determinant:  -4   -1    0
count:          7  129  521.
```

For each nonsingular core, the discovery computation reconstructs the exact
scaled inverse, tests all `2^10-1=1023` nonzero binary profiles, deletes the
ten core columns, and builds every compatibility edge by integer arithmetic.
Every one of the 136 exact target searches excludes a clique of size 53.
Together they visit 9,987,213 branch nodes.  The required clique cannot
exist, proving the theorem.

## Independent no-import audit

Frozen discovery source:

```text
work/builder/unicyclic_core_exact_search.json
SHA-256 c36c4baa544b9e87616de5d70a7d5f09dc56b96f0b199d0a1b0f586eefa65afa
```

Independent audit:

```text
work/linear_extension/unicyclic_core_family_audit.json
SHA-256 5b8e6e8ef747350f142f159ee5ae2f6aada285e6f607bd172af8ec119069465f
```

The verifier imports no discovery module.  It independently generates
bracket-coded rooted trees, decorates cycles, canonicalizes by a separately
written dihedral word, and matches the 657 source edge lists as an
isomorphism set.  It recomputes every determinant and every integer adjugate
from cofactors, checking both adjugate identities.  It then rebuilds every
profile and edge using

```text
v' adj(B) w in {0,det(B)}.
```

After a nonzero cyclic relabelling of each compatibility graph, its separate
exact clique engine again rejects target 53 for all 136 nonsingular cores,
in 11,600,208 recursive calls.  Before use, that engine agrees with literal
subset enumeration on every labelled graph through order five and on 100
deterministic random graphs at each order six through nine, for every target
size: 1,500 graph tests in total.

Five fail-closed attacks--wrong source hash, a dropped record, an altered
edge list, disabled exact search, and a flipped top-level conclusion--are all
rejected.  The attack record is

```text
work/builder/unicyclic_core_fail_closed_attacks.json
SHA-256 9c987d46dbce8a4c6ef1b21f45aa5ffee4f5db742882ddbc41c333d11b9c584d
```

No floating-point spectral or optimization value is used in either path.

## Sharpness

The certified standard rank-ten graph of order 62 contains the nonsingular
unicyclic principal core with vertex indices

```text
1,2,4,6,12,14,28,30,60,10.
```

In this order its ten induced edges are

```text
01,03,05,07,12,19,34,49,56,78.
```

It is connected, its unique cycle is `0-1-9-4-3-0`, and its determinant is
`-1`.  The complete 62 by 62 adjacency certificate is

```text
certificates/standard_rank10_order62_unicyclic_core.json
SHA-256 7be572892364998e32fdf8882aa6d10303713ca58282641a0d51c6c1e4020fa2
```

The exact verifier checks symmetry, zero diagonal, all entries binary, no
isolates, no equal open neighbourhoods, the nonzero ten-order determinant,
and all 3,844 entries of the rank-ten factorisation.  Thus the upper bound is
attained inside the stated unicyclic-core class.

The separate shape verifier records the ten induced edges, connectedness,
the unique five-cycle, and determinant `-1` in
`certificates/standard_rank10_order62_unicyclic_core_shape_verification.json`
(SHA-256
`7a0e99d29cc3b60706ef18c58b286501868717ff89d59270c996afc5a939afb5`).

## Scope

Together with `proof/tree_core_theorem.md`, this settles all reduced
rank-ten graphs that contain a nonsingular induced ten-vertex core with at
most one cycle.  It does not prove that every connected rank-ten graph has
such a core.  Bicyclic and denser nonsingular cores remain open, so the full
rank-ten rank--order conjecture is still neither proved nor disproved.
