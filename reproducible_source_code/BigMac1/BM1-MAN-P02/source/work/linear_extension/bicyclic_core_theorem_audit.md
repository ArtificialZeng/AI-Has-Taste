# Serial referee audit: bicyclic-core theorem

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
proof/bicyclic_core_theorem.md
SHA-256 bf6ede3694d7b29c56e1b7192affd4d561384cc2e1200836f5d228afde188e19
```

Machine-checkable document consistency audit:

```text
work/linear_extension/bicyclic_core_theorem_checks.json
SHA-256 849427baa87dfbebf39effd12cfb406de0820f51eadc5eb48ee27ebaf79944e7
```

The decisive finite result has an independently written no-import
implementation.  All work was performed serially after the first research
topic was stopped, in accordance with the user's instruction.

## Reduction and quantifier check

The theorem assumes a finite simple reduced graph of real adjacency rank ten
and the existence of a connected nonsingular induced ten-vertex bicyclic
core.  Since the principal core already has full rank, the Schur complement
vanishes exactly.  Looplessness, simplicity and reducedness give the stated
nonzero, distinct isotropic binary profiles and their compatibility rule.
An order-63 graph would have 53 noncore vertices, hence a 53-clique.  The
proof neither assumes that every rank-ten graph has a bicyclic core nor uses
the converse construction.

## Domain-completeness check

Deleting a suitable non-bridge edge from a connected bicyclic graph gives a
connected unicyclic graph; choosing a spanning tree leaves exactly two
additional edges.  These give two complete discovery routes.  The structural
classification of the leaf-pruned two-core follows from
`sum(deg(v)-2)=2`: figure-eight, theta and dumbbell are exhaustive.  Rooted
attachment words plus the relevant reversals and path permutations provide
complete invariants.

The discovery routes agree on 2,678 isomorphism classes.  The independent
implementation instead starts from 106 free trees, adds two nonedges in
66,780 labelled cases, and uses a separately written bracket-word
canonicalizer.  Its isomorphism set matches all 2,678 frozen source edge
lists.  Counts `345+514+1819=2678` and
`3+6+62+625+1959+17+6=2678` check.

## Exact arithmetic and target-search check

Frozen discovery source:

```text
work/builder/bicyclic_core_exact_search.json
SHA-256 286465529d9e1b65716790ac01e87b68f8a7593a5dadd3a415c247bc2f74c3df
```

It identifies exactly 719 nonsingular cores.  Twenty-nine are closed by a
root proper-colouring bound; 690 complete target searches close the rest in
48,967,729 integer branch nodes.

Independent audit:

```text
work/linear_extension/bicyclic_core_family_audit.json
SHA-256 32883b6f42d1ced6a3cdce91c277cfdbf4b30f5ab2a835f74daaa37738647fb7
```

It recomputes Bareiss determinants, cofactor adjugates and both adjugate
identities, then reconstructs every profile graph.  After cyclic relabelling,
its separate exact engine rejects target 53 for all 719 nonsingular cores in
41,704,342 calls.  The engine passes 1,500 exhaustive/random cross-checks.
No floating-point rank, spectrum or optimization result enters the claim.

Five corrupted certificates fail closed:

```text
work/builder/bicyclic_core_fail_closed_attacks.json
SHA-256 2b83ea31e639360b052adbfaf3c42e61842e36c79dbdad894476801127f84de1
```

During pre-freeze harness development, a nominal edge substitution was found
to be merely another labelling of the same isomorphism class and was therefore
correctly accepted.  The final adversarial edge mutation inserts a self-loop,
which is unambiguously outside the simple-graph domain and is rejected.  This
was an attack-design correction, not a mathematical or verifier failure.

## Sharpness check

The witness and verification are

```text
certificates/standard_rank10_order62_bicyclic_core.json
SHA-256 a0f087da2719b7317300da82d4a3a240e2664beb21b54b4ddfd4bccd4bfc9200

certificates/standard_rank10_order62_bicyclic_core_verification.json
SHA-256 61356dd499e978dab8b4b4946a6d8dc1c3b0eb263e1b26d618946c2b07a8aa3d
```

The ambient graph is the previously exact-certified reduced rank-ten graph
of order 62.  The selected induced ten-vertex core has eleven edges, is
connected, and has determinant `-1`.  Therefore it is nonsingular bicyclic,
and the class bound is attained.

## Scope check

The proof explicitly limits itself to graphs possessing a connected
nonsingular induced full-rank core with exactly eleven edges.  Together with
the frozen tree and unicyclic results, cores with at most eleven edges are
covered.  No assertion is made for denser full-rank cores.  Hence this is a
sharp nontrivial structural-class theorem, not a proof or disproof of the
unrestricted rank-ten conjecture.
