# Fresh mathematical audit of the frozen order-16 counterexample

## Scope and verdict

I reviewed the exact `resolution-paper` claim frozen at snapshot digest
`f9c68aabbc292cf2fd8e90b5635b9baef672e7c87ad17d46d177e0d4d622b153`.
The claim is accepted at its stated scope: the supplied order-16 graph is a
connected simple cubic Type-1 graph and has no equitable proper 4-total
coloring.  It therefore disproves the universal statement in `source.md`.

The claim does not say that order 16 is minimal and does not claim literature
priority.  Neither the additional census assertions in the evidence README nor
any unlisted census files are dependencies of this verdict.

## Frozen-input and graph checks

I recomputed every SHA-256 hash in `audit/snapshot.json` and recomputed the
canonical mapping digest.  All 12 frozen files and the snapshot digest match.
The graph6 record is

```text
O???CB?wB@F?@o@oB_?s?
```

My fresh graph6 decoder gives the following lexicographically ordered edges:

```text
07 08 09 18 19 1a 29 2a 2b 3b 3e 3f 4b 4e 4f 5c 5d 5e 6c 6d 6f 7c 7d 8a
```

Here `a,...,f` denote vertices `10,...,15`.  This edge list agrees with the
serialized JSON and the retained `showg` output.  It has 16 vertices and 24
distinct non-loop edges, every vertex has degree three, and a graph search from
vertex 0 reaches all 16 vertices.  Thus the graph is connected, simple, cubic,
and has order 16, which is strictly less than 20.

## Direct 4-total-coloring witness

For vertices `0,...,15`, the serialized colors are

```text
0 3 3 1 1 0 3 2 1 1 0 2 1 1 3 0
```

For the 24 edges in the order displayed above, the colors are

```text
1 2 3 0 2 1 0 2 1 0 2 3 3 0 2 3 2 1 2 0 1 0 3 3
```

I checked directly that the endpoints of every edge have different colors,
each edge differs from both endpoints, and the three incident edges at each
vertex have pairwise different colors.  The resulting four class sizes are
`[10,11,9,10]`, as recorded.  Hence this is a proper 4-total coloring (it need
not itself be equitable).  At any cubic vertex, the vertex together with its
three incident edges are four pairwise conflicting objects, so every total
coloring needs at least four colors.  The witness therefore proves
`chi''(G)=4`, not merely `chi''(G)<=4`.

## Equitable-CNF reconstruction

There are `16+24=40` colored objects.  An equitable partition of 40 objects
among four colors must have class sizes exactly `[10,10,10,10]`.

I independently reconstructed the retained DIMACS formula.  For each object
and color, base variable `4*object+color+1` asserts that color assignment.  The
formula contains:

- an at-least-one clause and all six pairwise at-most-one clauses for every
  object;
- same-color exclusion clauses for every adjacent vertex pair, incident
  vertex-edge pair, and pair of edges sharing a vertex;
- units fixing vertex 0 and its three incident edges to the four distinct
  colors; and
- four exact-cardinality networks.

The symmetry units lose no coloring: in any proper 4-total coloring, vertex 0
and its three incident edges use all four colors, so one global permutation of
the palette maps those four colors to the prescribed units.

For each color, auxiliary `q(i,j)` is constrained biconditionally to mean “at
least `j` of the first `i` objects have this color,” using

```text
q(i,j) <-> q(i-1,j) OR (q(i-1,j-1) AND x(i)).
```

The boundary clauses for `j=1` and `j=i` are the corresponding exact
biconditionals.  Induction on `i` establishes the stated threshold semantics.
The final units `q(40,10)` and `not q(40,11)` therefore impose exactly ten
occurrences of that color.  Repeating this for all four colors is equivalent to
equitable 4-total coloring.

My reconstruction has exactly 3,040 variables and 9,408 clauses.  After
normalizing literal and clause order while preserving clause multiplicity, it
is identical to `evidence/order16/cnf/equitable/g044.cnf`.  Thus the retained
formula is satisfiable exactly when the graph has an equitable proper 4-total
coloring; it is not merely a one-way relaxation or an overconstrained proxy.

## Unsatisfiability-certificate check

I wrote and ran the separate referee-side checker `audit/referee_check.py`; its
machine-readable result is `audit/referee_check.json`.  The checker does not
import the proposer's verifier.  Starting with the reconstructed DIMACS
formula, it processed all 3,459 proof deletions and independently tested every
one of the 2,498 additions by reverse unit propagation.  Every addition is RUP
(no RAT step is needed), and the last accepted addition is the empty clause.

This is a sound unsatisfiability certificate: if `F` is the current active
formula and unit propagation on `F` together with the negation of clause `C`
derives a conflict, then `F` entails `C`.  Adding `C` preserves all models;
deleting a clause cannot turn a satisfiable predecessor into the final RUP
derivation of the empty clause under this invariant.  Consequently the
original equitable-coloring CNF is unsatisfiable.

As secondary checks, the supplied verifier completed successfully with the
same 2,498 RUP additions, 3,459 deletions, and empty-clause conclusion.  CaDiCaL,
Kissat, and CryptoMiniSat also each reported `UNSATISFIABLE` on the retained
CNF.  These solver status lines are only corroboration; the checked RUP proof,
not solver status, is the decisive evidence.

## Quantifier and source comparison

The frozen source asserts that every finite simple cubic graph of order below
20 with `chi''=4` has an equitable proper 4-total coloring.  The checked graph
has order 16, satisfies all graph hypotheses, has `chi''=4`, and fails the
conclusion.  A single such graph negates the exact universal assertion.
Connectedness only strengthens the witness, so no disconnected-component
balancing argument is needed.  Likewise, a complete census is unnecessary for
this disproof.

No external theorem is used beyond the elementary four-object lower bound
proved above.  The frozen candidate makes no novelty, priority, or minimum-order
claim, so the absence of such conclusions is not a scope gap.  I found no
unresolved mathematical gap in the exact submitted claim.

## Verdict

**Accept.**  Scope, correctness of the witness and certificate, and the claimed
full disproof all pass.
