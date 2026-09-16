# Exact finite disproof dossier

Job: `win-00068-p02-research-353357b39b59` (research, 2026-09-07).
Independent census, encoding, and unified replay validation:
`win-00068-p02-research-5cb899a40f40` (research pass 3, 2026-09-08).

## Claimed resolution

The frozen assertion is false. Exactly 16 isomorphism classes of connected
simple cubic graphs of order 16 are Type 1 but have no equitable proper
4-total coloring. No such graph has smaller order. In the canonical geng
output order, the least-order counterexamples are:

```
Os?GOCF@O??ACBCBL?B?O
Ot?GOCA?WB@?ODOBC_?g@
Os?GO?C?_MAECKOOCGJO?
Os?GOKE??@`?CDCBKABA?
Os?GGOB@OO?OGBCBGEB_?
Ot?GOKFA??_A?B?BK?Q_A
Ov?GW?@?OM?E?KA?G?h?E
Os?GOGA?AOgoGWGWAA?_`
Os??WWK?@CaGCGOCCAI?K
Ov?GO???WB?k?c?a?_ZO?
Os??WWA?W@?ACBCBL?BG?
Os??WOB?OW?ACBCDKCBG?
Os??WOC?@@cEOSQOAO?g@
Os???[AAGH@_C@GEIOB?C
Os?GG???WBD_CcCaGKBO?
Os?GW?@?OMA?E@OKCEB?G
```

Their complete proper-coloring arrays are the 16
`A_sat_E_unsat_observed` rows in `evidence/coloring_witnesses.jsonl`.
`evidence/scripts/verify_witnesses.py` decodes each graph and directly checks
all adjacent-vertex, adjacent-edge, and incident vertex-edge inequalities.
Each displayed proper coloring has sorted class profile `(9,10,10,11)`, hence
is itself nonequitable; nonequitable witnesses alone are not used to infer the
nonexistence of an equitable coloring.

## Exact encoding and certificates

For a decoded graph on `n` vertices, edges are sorted lexicographically and
the `5n/2` total-graph elements are ordered as vertices `0,...,n-1`, followed
by those edges. For every element `a` and color `c` in `0,...,3`, the primary
Boolean variable is `x[a,c]` (allocated in element-major order). The CNF has:

1. one four-literal at-least-one clause and all six binary at-most-one clauses
   for each element;
2. `(-x[a,c] or -x[b,c])` for every color and every conflict pair in the
   total graph;
3. the harmless color-symmetry unit `x[0,0]`; and
4. for `E(G)`, PySAT's sequential-counter clauses imposing
   `floor((5n/2)/4) <= sum_a x[a,c] <= ceil((5n/2)/4)` for every color.

Because all elements receive exactly one color, these four bounds are exactly
pairwise equitability. At order 16 they impose ten occurrences of every color.
Fixing element 0 to color 0 loses no coloring because colors may be permuted.
`evidence/scripts/sweep_colorings.py` is the complete deterministic encoder.

For each graph reported `A_unsat_observed`, the retained `A` DIMACS omits item
4. For each of the 16 claimed counterexamples, the retained `E` DIMACS includes
it. PySAT Glucose 3 emitted DRAT traces. A locally compiled copy of the
April 21, 2024 `drat-trim.c` independently replayed every DIMACS/trace pair.
`evidence/unsat_certification.json` binds each of 329 pairs to its graph6 row,
predicate, dimensions, hashes, proof length, and successful replay result.

## Exhaustive coverage and least order

The canonical connected cubic census counts are
`1,2,5,19,85,509,4060,41301` at orders `4,6,...,18`, totaling 45,982.
Generation, hashes, commands, provenance and limitations are in
`evidence/census_generation.md`; independent graph property and count checks
are in `evidence/census_verification.json`.

The exhaustive result join through order 16 is:

| order | equitable witness | A-UNSAT certificate | A witness + E-UNSAT certificate |
|---:|---:|---:|---:|
| 4 | 0 | 1 | 0 |
| 6 | 1 | 1 | 0 |
| 8 | 4 | 1 | 0 |
| 10 | 9 | 10 | 0 |
| 12 | 60 | 25 | 0 |
| 14 | 461 | 48 | 0 |
| 16 | 3817 | 227 | 16 |

Thus every graph of order below 16 either has an explicit equitable coloring
or is proved not Type 1. At order 16 every one of the 4,060 census rows has
exactly one of the three outcomes, and the last column is precisely the 16
counterexamples. Orders 18 need no coloring classification to disprove the
universal statement or establish the least order, but their 41,301 canonical
representatives are included to satisfy the required below-20 census.

`evidence/scripts/audit_resolution.py` independently rejoins every result row
to the census, verifies every stored hash, and replays all 329 DRAT proofs.
Its final report is `evidence/resolution_audit.json`.

## Independent checks added after the initial computation

An exhaustive C canonizer independent of nauty found no isomorphic duplicate
among all 45,982 rows.  For every order, the orbit sum obtained from its
automorphism counts equals an independently derived exact recurrence count of
labeled connected simple cubic graphs, proving census completeness.  The
pinned generator was also rerun at every order and reproduced all census files
byte for byte (`evidence/independent_census.json` and
`evidence/census_regeneration.json`).

For the 16 decisive E-UNSAT cases, a second encoder uses no NetworkX, primary
encoder, or cardinality library.  At order 16 the local four-color star identity
shows equitability is equivalent to exactly four vertices of each color; the
second CNFs impose at most four through explicit five-subset clauses.  All 16
CNFs were rebound to their census rows and all 16 DRAT traces replayed
(`evidence/second_encoding_replay.json`).

`python3 evidence/scripts/final_verify.py` is the single verification entry
point.  It rebuilds the generator and both checkers, byte-regenerates the
census, reruns the independent completeness proof, checks all 4,368 positive
colorings, binds all certified CNFs, and replays 329 primary plus 16 secondary
DRAT proofs.  Its run report is `evidence/final_verification.json`.

The nauty 2.8.9 source archive is not retained; only the hashed objects and a
byte-reproducible relink are present.  This is a provenance limitation, not a
substitute for the independent completeness proof above.  The research job
requests fresh mathematical review and does not treat its own checks as review
acceptance.
