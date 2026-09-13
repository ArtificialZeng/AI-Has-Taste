# Serial referee audit: unicyclic-core theorem

## Verdict

```text
PASS
fatal findings: 0
major findings: 0
minor findings: 0
scientific status: sharp partial theorem / certified finite result
full unrestricted rank-10 conjecture: OPEN
```

Audited theorem:

```text
proof/unicyclic_core_theorem.md
SHA-256 1f01680aeaafa1bb31146aed08c1c912b2f8019476a747029afd9849e6930426
```

This referee pass was performed serially after discovery, in accordance with
the instruction not to run the two mathematical projects simultaneously.
The decisive computation itself has an independently written no-import
implementation.

## Quantifier and reduction check

The theorem assumes exactly: a finite simple reduced graph `G`, real
adjacency rank ten, and a nonsingular induced connected unicyclic subgraph on
ten vertices.  The full-rank principal factorisation gives the compatibility
model without a numerical rank inference.  Zero and duplicate profiles are
excluded by reducedness, and the ten core columns are universal.  Therefore
an order-63 graph would force 53 distinct noncore profiles forming a clique.
No converse or existence of a unicyclic core is silently assumed.

## Domain-completeness check

The unique-cycle decomposition is lossless: removing the cycle edges leaves
one rooted tree at each cycle vertex, and an isomorphism acts on the unique
cycle through the dihedral group.  Rooted AHU words plus a least dihedral
rotation/reflection are therefore complete invariants for this graph class.
The independent bracket-code generator obtains the same 657-object set as
the discovery source edge lists.  The cycle-length distribution sums to 657,
and the determinant distribution `521+129+7` also sums to 657.

## Exact arithmetic and search check

Frozen source:

```text
work/builder/unicyclic_core_exact_search.json
SHA-256 c36c4baa544b9e87616de5d70a7d5f09dc56b96f0b199d0a1b0f586eefa65afa
```

The source treats all 657 objects, identifies 136 nonsingular cores, and
records a negative exact target-53 decision for each.  Its 9,987,213 branch
nodes use only integer compatibility predicates.

No-import audit:

```text
work/linear_extension/unicyclic_core_family_audit.json
SHA-256 5b8e6e8ef747350f142f159ee5ae2f6aada285e6f607bd172af8ec119069465f
```

The audit independently regenerates the isomorphism domain, computes
determinants and cofactor adjugates, checks both adjugate identities, rebuilds
all masks and edges, cyclically relabels every compatibility graph, and again
rejects target 53 in 11,600,208 calls.  Its exact clique engine passes 1,500
brute-force/random graph tests.  Five corrupted sources fail closed:

```text
work/builder/unicyclic_core_fail_closed_attacks.json
SHA-256 9c987d46dbce8a4c6ef1b21f45aa5ffee4f5db742882ddbc41c333d11b9c584d
```

The two exploratory verifier runs with more aggressive variable
permutations were deliberately interrupted because their greedy-colour
orders caused resource blow-up.  They produced no certificate and are not
used as evidence.  The completed cyclic-shift audit above is the frozen
independent proof object.

## Sharpness check

The 62-vertex equality certificate and its verifiers are:

```text
certificates/standard_rank10_order62_unicyclic_core.json
SHA-256 7be572892364998e32fdf8882aa6d10303713ca58282641a0d51c6c1e4020fa2

certificates/standard_rank10_order62_unicyclic_core_verification.json
SHA-256 c4fc8536d638e12821a224addc8c172d9e27f0dd26e0e0cebc7766635b62cc5b

certificates/standard_rank10_order62_unicyclic_core_shape_verification.json
SHA-256 7a0e99d29cc3b60706ef18c58b286501868717ff89d59270c996afc5a939afb5
```

The full graph is simple, reduced, order 62, and exact rank ten.  Its selected
ten-vertex principal core has ten edges, is connected, has a unique
five-cycle, and has determinant `-1`.  Thus the 62 bound is attained inside
the theorem's structural class.

## Scope check

The proof document explicitly leaves bicyclic and denser nonsingular cores
open and does not claim the complete rank-ten conjecture.  The result is a
sharp nontrivial structural-class theorem, which is one of the terminal
outcomes permitted by the original research request.
