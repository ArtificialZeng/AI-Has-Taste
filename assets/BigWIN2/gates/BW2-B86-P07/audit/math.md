# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim in `claim.json`: for the
five-vertex tree with edges `ca, cb, cd, de`, with ordinary spanning-subgraph
comparability applied to every induced five-vertex subgraph, the asserted
value is `f(T*) = 8`.  I did not replace this by a weaker computational or
restricted statement.

The recorded snapshot digest is
`4cf87cb9ea162f6513208d0fb7f067f9d89b3118d6c8b3fdda7f2377eb1f899f`.
I recomputed every hash in its `files` mapping and recomputed the canonical
mapping digest; all values agree.  In particular, the immutable `source.md`
hash is
`0ef7e09d275314f53febd468b6f3933ff31d2255762112050dd71580ebc4b160`.

## Reconstruction of the mathematical argument

For the lower bound, a five-set in `2 K_4` has component sizes `4+1` or
`3+2`, so its induced graph is `K_4 + K_1` (six edges) or `K_3 + K_2`
(four edges).  Neither disconnected graph contains the connected spanning
tree `T*`.  The six-edge graph cannot be contained in the four-edge tree.  If
the four-edge graph were contained in `T*`, equality of edge counts would
make it isomorphic to `T*`, whereas their degree multisets differ.  Thus all
56 five-sets are legal and `f(T*) >= 8`.

For the upper bound, the 36 Boolean variables are in bijection with labeled
simple graphs on vertices `0,...,8`.  On five labeled vertices, `T*` has only
the automorphism interchanging its two equivalent leaves, hence it has
`5!/2 = 60` labeled copies.  My direct ten-bit reconstruction gave 226
patterns contained in a labeled copy of `T*`, 651 patterns containing one,
and an intersection consisting exactly of the 60 copies.  Thus there are 817
comparable patterns and 757 comparable noncopies.  As an additional census
check, the forbidden counts by edge number were

```
edges:       0   1   2    3    5    6    7   8   9  10
forbidden:   1  10  45  110  210  205  120  45  10   1
```

There are no forbidden four-edge patterns: comparability at the same edge
count forces isomorphism.

For each of the 126 five-sets and each forbidden pattern, the supplied clause
contains its ten local variables and is false on exactly that pattern.  The
sign is negative on a required edge and positive on a required nonedge.
Consequently an assignment satisfies the full CNF if and only if the
corresponding nine-vertex graph is `T*`-exact.  The supplied semantic checker
reconstructed all clauses, rather than sampling them, and I reran it.  It
verified 36 variables, `126 * 757 = 95,382` clauses, the local census, and all
56 five-sets of the lower construction.  The CNF hash was
`70b78d1ae0f25858dd024eda62addf5f7d623a410725026e7a37200bb79f8cc4`.

## Refutation audit

The proof hash was
`cdfb10845b6fc6c282095187e9f1af6ec2f02456bbfb32d04cacadfaaeadb760`.
I reran the frozen no-SAT-library checker, which parsed all 4,990 proof
operations, verified 3,993 RUP additions, applied 997 matched deletions, and
verified the final empty-clause addition.

I also wrote and ran `audit/referee_naive_rup.py`, a fresh replay using direct
fixed-point unit propagation on positive/negative 36-bit clause masks.  It
does not share the candidate checker's persistent two-watched-literal data
structure.  Its complete replay returned:

```
cnf_variables=36
cnf_input_clauses=95382
proof_operations=4990
rup_additions_verified=3993
deletions_applied=997
final_empty_clause_verified=true
result=VERIFIED
```

As non-certificate corroboration, four separately invoked installed solvers
also returned UNSAT on the frozen CNF: CaDiCaL 1.9.5, Lingeling, MiniSat 2.2,
and MapleCM.  The acceptance below rests on the checked refutation, not on
these solver status lines.

The logical use of the replay is sound: if unit propagation on the active
database together with the negation of an added clause reaches conflict, the
active database entails that clause.  Induction therefore makes every added
clause a consequence of the original CNF.  Deleting clauses cannot invalidate
that implication, and the final verified empty clause proves the original CNF
unsatisfiable.  Hence no nine-vertex `T*`-exact graph exists.  Exactness is
hereditary under induced subgraphs because every relevant five-set is
preserved, so a larger exact graph would contain an exact induced
nine-vertex graph.  Therefore `f(T*) <= 8`, and the lower construction gives
`f(T*) = 8`.

## Quantifier, hypothesis, and source checks

The encoding covers all 126 five-subsets and uses no symmetry-breaking
assumptions.  It tests ordinary, not induced, containment inside each induced
five-vertex graph.  The domains have order at least five; there are no empty
domain, division, limiting, compactness, or equality-case gaps.  The
hereditary step is invoked only after the nine-vertex refutation.

I checked the current primary arXiv record and full text for Caro, Tuza, and
Christina Zarb, [*Induced/Incomparable versus
Ramsey*](https://arxiv.org/abs/2605.22077), arXiv:2605.22077v2.  The record
still lists v2 (27 May 2026) as current.  Its definition agrees with the
ordinary-subgraph reading; Fact 2.1(4) supplies heredity; Theorems 5.1 and 6.1
give the applicable bounds `8 <= f(T*) <= 16`; and Section 7 asks for the
tree values.  Focused current searches using the title, identifier,
`H-exact`/`Exact(H)`, `fork`, and `subdivided claw` found no later primary
resolution of this case.  This is a bounded source comparison, not a claim of
priority.  The experimental HTML page's internal update-date inconsistency
does not change the arXiv version record or the cited mathematical statements.

## Verdict

**ACCEPT.**  The exact frozen scope is proved: the lower construction is
valid, the complete nine-vertex encoding matches the definition, the full
RUP refutation survives two structurally different complete replays, and
heredity closes every larger order.  I found no unresolved mathematical gap.
The literature conclusion remains appropriately limited to the searches
actually performed.
