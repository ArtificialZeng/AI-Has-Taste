# Exact rank-ten bound for nonsingular induced bicyclic cores

## Theorem

Let `G` be a finite simple reduced graph whose real adjacency rank is ten.
If `G` contains a nonsingular induced subgraph `H` on ten vertices and `H`
is connected and bicyclic, then

```text
|V(G)| <= 62.
```

The bound is sharp within this structural class.

Here bicyclic means connected with cyclomatic number two, equivalently
`|E(H)|=|V(H)|+1=11`.

## Principal-core reduction

Order the vertices of `G` with the vertices of `H` first and write

```text
A(G) = [ B  V ] ,                 B=A(H).
       [V'  C ]
```

Because `B` is nonsingular of order ten and `rank A(G)=10`, exact block
elimination gives the zero Schur complement

```text
C = V' B^{-1} V.                                      (1)
```

Thus each vertex outside `H` has a nonzero binary core profile
`v in {0,1}^10` satisfying

```text
v' B^{-1} v = 0,                                      (2)
```

and two distinct outside profiles can coexist only when

```text
v' B^{-1} w in {0,1}.                                 (3)
```

The zero profile would give an isolated vertex.  Equal profiles would give
equal open neighbourhoods by (1), so reducedness excludes both.  The ten
profiles `Be_i` of the core vertices are also excluded from the outside set:
an outside vertex with that profile would have the same open neighbourhood
as core vertex `i`.  Moreover every `Be_i` is compatible with every binary
profile because

```text
(Be_i)' B^{-1}v = v_i in {0,1}.                        (4)
```

Consequently an order-at-least-63 graph satisfying the hypotheses would
produce a clique of at least `63-10=53` vertices in the compatibility graph
on the admissible noncore profiles.  Excluding a 53-clique for every possible
core proves the theorem.

All computations below replace `B^{-1}` by `adj(B)/det(B)`.  Conditions
(2)--(3) are therefore integer equalities and membership tests.

## Complete bicyclic domain

Every connected ten-vertex bicyclic graph can be generated in either of two
ways:

1. delete a non-bridge cycle edge, obtaining a connected unicyclic graph,
   and then add the deleted nonedge;
2. choose a spanning tree and add its two remaining edges.

The discovery implementation performs both constructions and obtains the
same isomorphism set.

For completeness of canonicalization, repeatedly delete leaves.  The
remaining two-core has minimum degree two and cyclomatic number two, hence

```text
sum(deg(v)-2) = 2.
```

It therefore has either one vertex of degree four or two vertices of degree
three.  The first case is a figure-eight core.  In the second case the two
branch vertices are joined by three internally disjoint paths (a theta core)
when the two-core has no bridge, and by a path between two cyclic blocks (a
dumbbell core) otherwise.  Rooted AHU words encode every tree attached to a
two-core vertex.  Canonical reversal, path permutation and cycle reversal
then give a complete structural code for each of the three core types.

The two independent generation routes agree on exactly 2,678 isomorphism
classes, distributed as

```text
dumbbell: 345,  figure-eight: 514,  theta: 1819.
```

Exact Bareiss determinants give 1,959 singular and 719 nonsingular cores.
The full determinant distribution is

```text
determinant:  -9  -5  -4   -1    0   3   4
count:          3   6  62  625 1959  17   6.
```

For every nonsingular core, the discovery computation reconstructs the
scaled inverse, checks all `2^10-1=1023` nonzero binary profiles, removes the
ten core columns, and constructs every compatibility edge with integer
arithmetic.  Twenty-nine cases are rejected at the root by a proper-colouring
upper bound.  Complete target-53 searches reject the remaining 690 cases.
Across all 719 nonsingular cores they visit 48,967,729 exact branch nodes and
find no 53-clique.  The principal-core reduction now gives `|V(G)|<=62`.

## Independent no-import audit

Frozen discovery certificate:

```text
work/builder/bicyclic_core_exact_search.json
SHA-256 286465529d9e1b65716790ac01e87b68f8a7593a5dadd3a415c247bc2f74c3df
```

Independent audit:

```text
work/linear_extension/bicyclic_core_family_audit.json
SHA-256 32883b6f42d1ced6a3cdce91c277cfdbf4b30f5ab2a835f74daaa37738647fb7
```

The audit imports no discovery or builder module.  It independently creates
the 106 free ten-vertex trees, adds two nonedges in all 66,780 labelled
instances, and deduplicates them with a separately written bracket-word
two-core code.  Its 2,678 canonical edge lists match the discovery set as an
isomorphism set.  It recomputes every Bareiss determinant and every cofactor
adjugate, checks both adjugate identities, and reconstructs all profile and
compatibility counts.

After a nontrivial cyclic relabelling of every compatibility graph, a
separate exact target-search engine again rejects 53 for all 719 nonsingular
cores, in 41,704,342 recursive calls.  Before use, that engine agrees with
literal exhaustive enumeration on every labelled graph through order five
and on 100 deterministic random graphs at each order six through nine, for
1,500 graph tests in total.

Five fail-closed attacks are all rejected: wrong source hash, a dropped
record, an edge list containing a self-loop, disabled exact search, and a
flipped top-level conclusion.  Their frozen record is

```text
work/builder/bicyclic_core_fail_closed_attacks.json
SHA-256 2b83ea31e639360b052adbfaf3c42e61842e36c79dbdad894476801127f84de1
```

No floating-point eigenvalue, rank, optimization result or heuristic clique
size is used in the theorem.

## Sharpness

The already certified reduced rank-ten graph of order 62 contains the
induced core on ambient vertex indices

```text
2,4,6,12,14,28,30,60,10,7.
```

In that order its eleven induced edges are

```text
01,08,09,23,29,38,39,45,49,67,69.
```

The core is connected and has ten vertices and eleven edges, so its
cyclomatic number is two.  Its exact Bareiss determinant is `-1`.  The
ambient 62-vertex graph was already verified to be simple, reduced and of
exact real adjacency rank ten.  The new bound is therefore attained within
the bicyclic-core class.  The core witness and its exact verifier output are

```text
certificates/standard_rank10_order62_bicyclic_core.json
SHA-256 a0f087da2719b7317300da82d4a3a240e2664beb21b54b4ddfd4bccd4bfc9200

certificates/standard_rank10_order62_bicyclic_core_verification.json
SHA-256 61356dd499e978dab8b4b4946a6d8dc1c3b0eb263e1b26d618946c2b07a8aa3d
```

## Scope

Together with the tree-core and unicyclic-core theorems, this proves the
sharp 62-vertex bound whenever a reduced rank-ten graph contains a connected
nonsingular induced ten-vertex core with at most eleven edges.  It does not
prove that every connected rank-ten graph possesses such a sparse full-rank
core.  Cores with twelve or more edges remain open, so the unrestricted
rank-ten rank--order conjecture is still neither proved nor disproved.
