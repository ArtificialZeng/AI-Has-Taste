# Certificate dossier: the five-vertex subdivided claw has exact value eight

## Exact statement

Let `T*` be the tree on `{c,a,b,d,e}` with edges
`{ca,cb,cd,de}`.  Comparability means ordinary spanning subgraph
comparability between graphs of order five, exactly as frozen in `source.md`
and interpreted in `problem.md`.  Then

```
f(T*) = 8.
```

The lower construction is prior art.  The new step submitted for review is
the certified nonexistence of a nine-vertex `T*`-exact graph.

## Lower bound

Take `G = 2 K_4`.  Every five-set meets the two components in sizes `4+1` or
`3+2`, and therefore induces `K_4 + K_1` (six edges) or `K_3 + K_2` (four
edges).  Neither disconnected graph contains the connected spanning tree
`T*`.  The six-edge graph cannot be contained in the four-edge tree.  If the
four-edge graph were contained in `T*`, equality of edge counts would make it
isomorphic to `T*`, which it is not.  Thus all 56 five-sets are incomparable
with `T*`, so `2 K_4` is `T*`-exact and `f(T*) >= 8`.

## Complete nine-vertex encoding

Order the 36 pairs `ij` with `0 <= i < j <= 8` lexicographically and let
`x_ij` say that `ij` is an edge.  On local vertices `0,...,4`, order the ten
pairs lexicographically.  Exhaustive explicit-bijection enumeration gives:

- 60 labeled copies of `T*` (also `5!/|Aut(T*)| = 5!/2`);
- 817 labeled graphs comparable with `T*`, copies included;
- 757 comparable labeled graphs not isomorphic to `T*`.

For each lexicographically ordered five-set `U` of `[9]` and each forbidden
local graph `P` in increasing ten-bit-mask order, the CNF has the clause

```
(OR_{e in P} not x_e) OR (OR_{e in K_U minus P} x_e).
```

Here local pairs are transported to their corresponding global pairs in
`U`.  This ten-literal clause is false exactly when `G[U]=P`.  Consequently,
an assignment satisfies every clause if and only if the corresponding
nine-vertex graph is `T*`-exact.  There are `binom(9,5)=126` five-sets and
therefore `126*757=95,382` clauses.  The DIMACS file has 36 variables, no
symmetry-breaking clauses, and SHA-256

```
70b78d1ae0f25858dd024eda62addf5f7d623a410725026e7a37200bb79f8cc4.
```

`evidence/generate_n9_cnf_and_proof.py` fixes all orderings above and
regenerates the file byte for byte.

## Refutation and independent replay

PySAT 1.8.dev24's proof-enabled `Glucose3` binding returned UNSAT and emitted
the complete textual DRUP/RUP trace `evidence/n9_tstar_exact.drup`.  It has
4,990 operations: 3,993 additions and 997 deletions, ending by adding the
empty clause.  Its SHA-256 is

```
cdfb10845b6fc6c282095187e9f1af6ec2f02456bbfb32d04cacadfaaeadb760.
```

The separately written `evidence/verify_n9_certificate.py` imports neither
the generator nor a SAT package.  It:

1. reconstructs ordinary containment by testing all 120 vertex bijections;
2. checks the 60/817/757 census and all 56 five-sets of `2 K_4`;
3. reconstructs and compares every one of the 95,382 DIMACS clauses;
4. checks the immutable-source, CNF, and proof digests;
5. tests its two-watched-literal propagator against a naive propagator on
   3,200 deterministic synthetic instances;
6. maintains the active clause database, explicitly applies every deletion,
   and verifies every addition by unit conflict under the negated clause;
7. verifies that the final operation is the RUP addition of the empty clause.

The saved replay log reports all checks as verified.  RUP soundness is the
elementary implication: if active clauses together with the negation of a
proposed clause unit-propagate to contradiction, those active clauses entail
the proposed clause.  Each retained or later deleted addition is therefore a
logical consequence of the original CNF.  The verified final empty clause
proves the original CNF unsatisfiable, independently of the solver's UNSAT
status line.

## Conclusion and scope

No nine-vertex `T*`-exact graph exists.  Exactness is hereditary for induced
subgraphs of order at least five: every five-set of an induced subgraph is
also a five-set of the original graph.  Hence a larger `T*`-exact graph would
induce a nine-vertex one, which is impossible.  Thus `f(T*) <= 8`; together
with `2 K_4`, this yields `f(T*)=8`.

The result concerns only this fixed five-vertex tree.  It does not determine
`f(T)` for every tree.  The bounded literature check is recorded separately
and does not assert priority.

## Reproduction

From the project root, with Python-SAT 1.8.dev24 installed:

```
python3 evidence/generate_n9_cnf_and_proof.py
python3 evidence/verify_n9_certificate.py
```

The first command refuses either unexpected supplied digest; the second
independently requires both digests and prints `result=VERIFIED` only after
the semantic audit and full replay.
