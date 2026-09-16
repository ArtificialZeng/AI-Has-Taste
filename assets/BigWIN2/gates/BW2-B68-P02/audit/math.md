# Fresh mathematical referee report

## Frozen scope and verdict

I reviewed the `resolution-paper` claim bound to snapshot
`6ebf6a4b339f4a87c2b63142612231678887ada948c0e75159e5f4bc90707b4b`.
The original assertion is the existential statement that every connected
Type 1 cubic graph of order below 20 has at least one equitable proper
4-total coloring. The candidate asserts a full disproof: the least
counterexample order is 16, and exactly 16 isomorphism classes occur at that
least order.

**Verdict: accept.** The frozen evidence establishes the claimed disproof at
its exact scope. The positive witnesses prove all required satisfiable cases,
the replayed proof certificates establish the required unsatisfiable cases,
and an independent finite counting argument establishes census completeness.

## Reconstruction of the decisive mathematics

For a cubic graph on `n` vertices there are `3n/2` edges and hence `5n/2`
objects to color. A proper 4-total coloring is represented by one of four
Boolean color variables for every vertex and edge. Exact-one clauses give
each object one color. Conflict clauses forbid a common color on adjacent
vertices, on incident vertex-edge pairs, and on edges sharing an endpoint.
These are exactly the three proper-total-coloring conditions. Fixing vertex
0 to color 0 is harmless: any existing coloring can have its four color names
permuted to satisfy the unit clause. Thus UNSAT for an `A` formula is
equivalent to the absence of any proper 4-total coloring.

The secondary equitable encoding has a particularly transparent
specialization at order 16. At every cubic vertex, the vertex and its three
incident edges are pairwise conflicting and therefore use all four colors.
For a fixed color `c`, let `S_c` be its vertices and `M_c` its edges. Counting
color `c` around all 16 vertex-stars gives

`16 = |S_c| + 2|M_c|`,

so its total color-class size is

`|S_c| + |M_c| = (16 + |S_c|)/2`.

There are 40 objects at order 16, so equitability is exactly four total color
classes of size 10, equivalently `|S_c|=4` for every color. The secondary CNF
uses the direct total-coloring clauses and, for each color, one negative
clause for every five-vertex subset. Those clauses impose `|S_c|<=4`.
Because all 16 vertices receive exactly one of four colors, all four bounds
must be equalities. Hence this CNF is satisfiable exactly when an equitable
proper 4-total coloring exists. Its color-symmetry unit is again harmless.

The classification join through order 16 is:

| order | equitable witness | `A`-UNSAT | proper witness + `E`-UNSAT |
|---:|---:|---:|---:|
| 4 | 0 | 1 | 0 |
| 6 | 1 | 1 | 0 |
| 8 | 4 | 1 | 0 |
| 10 | 9 | 10 | 0 |
| 12 | 60 | 25 | 0 |
| 14 | 461 | 48 | 0 |
| 16 | 3817 | 227 | 16 |

Thus every census class below order 16 either has a directly checked
equitable coloring or is not Type 1. At order 16 the same alternatives cover
4,044 classes, while the remaining 16 have directly checked proper
4-total-coloring witnesses and certified-UNSAT equitable formulas. This both
disproves the original universal assertion and proves minimality and the
exact least-order classification. Classification at order 18 is not needed
for those conclusions; its full canonical census is nevertheless included,
as the frozen source requires a census at every eligible order below 20.

The 16 least-order canonical graph6 codes, in the retained census order, are:

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

## Checks actually performed

I first verified every one of the 760 snapshot file hashes. The immutable
`source.md` retained SHA-256
`6ce58a7ef27abff3de2371ca219430179879b43f26e8da5e94927a140aa70a75`.
I then wrote and ran `audit/referee_verify.py`, which imports neither
NetworkX, PySAT, nor any researcher verification module.

The fresh verifier independently decoded and checked every graph6 row for
order, padding, edge count, cubicity, and connectedness. It found the exact
order counts

`1, 2, 5, 19, 85, 509, 4060, 41301`,

totaling 45,982. I inspected the exhaustive individualization/refinement
canonizer. Its branch rule is isomorphism-invariant, it performs no pruning,
and every discrete leaf supplies a labeling; the least adjacency string is
therefore canonical, while leaves attaining it count automorphisms. A fresh
compilation produced distinct canonical strings for all retained rows.

For completeness, I also checked the exact labeled-graph recurrence. If
`F(c1,c2,c3)` counts completions of a labeled residual degree sequence, remove
a fixed maximum-residual-degree vertex and choose its neighbors by residual
degree class. Every simple labeled completion is obtained exactly once. The
connected count follows by subtracting graphs according to the component
containing a fixed label. For every eligible order, the census orbit sum
`sum_G n!/|Aut(G)|` equaled that independently computed connected labeled
count. At orders 4 through 18 the values were respectively

`1`, `70`, `19320`, `11166120`, `11543439600`,
`19491385914000`, `50233275604512000`, and
`187663723374359232000`.

Pairwise nonisomorphism plus these exact orbit-sum equalities proves that no
isomorphism class is missing. I also checked the retained generator's help
text: its `-l` option canonically labels output graphs, consistent with the
reported graph6 convention.

I independently joined all 4,681 classification rows to their exact census
indices. I directly checked all vertex, edge, and incidence inequalities and
class sizes for 4,352 equitable witnesses, and checked the 16 proper
nonequitable witnesses for the counterexamples. Each counterexample witness
has sorted total-class profile `(9,10,10,11)`; this proves Type 1 but was not
used to infer equitable nonexistence.

For all 313 `A`-UNSAT cases, I independently reconstructed the exact DIMACS
formula from the graph6 row and compared its variables and ordered clauses to
the retained CNF. For all 16 counterexamples, I independently reconstructed
the secondary 18,233-clause equitable CNF described above and obtained exact
byte equality. I freshly compiled the snapshot-listed `drat-trim.c` and
replayed all 329 primary DRAT pairs and all 16 secondary pairs; every replay
returned `VERIFIED`. The detailed machine-readable results are in
`audit/referee_checks.json`.

## Quantifiers, boundaries, and source comparison

The handshaking lemma restricts cubic order to even `n`; simplicity excludes
orders below 4, so the enumerated orders `4,6,...,18` exhaust the frozen
domain. The computation treats `A(G)` and `E(G)` as existential assertions.
It does not confuse a nonequitable coloring with failure of equitable
colorability. In particular, each of the 16 decisive failures has both a
proper-coloring witness and a separate UNSAT certificate for equitable
colorability. No conclusion is asserted for order 20 or above, and the result
does not concern the stronger every-coloring statement.

I compared the claim with the supplied primary source, Adauto, de Figueiredo,
Sasaki, and Schneider, arXiv:2609.05259v1. Its Lemma 3.1 gives the same
vertex/edge color-class identity used above. Its Theorem 4.1 concerns the
different assertion that every 4-total coloring is equitable at orders
6, 8, 10, and 14. Most importantly, its Question 7.1 asks verbatim whether
every Type 1 cubic graph below order 20 has at least one equitable coloring
and proposes a complete catalogue computation by integer programming or SAT.
The candidate therefore supplies a substantive, exact resolution of the
nearest cited open question rather than a toy restriction or a corollary.
This source comparison is limited to the frozen supplied literature and is
not a broader priority claim.

## Limitations assessed

The nauty source archive used to build the retained generator is absent; only
the pinned executable, object files, hashes, command, and relink script remain.
That provenance limitation does not create a mathematical gap here because
the independent canonizer and exact orbit-sum argument establish
nonisomorphism and completeness without assuming `geng` completeness. The
secondary equitable encoding likewise removes dependence on the primary
cardinality library for the 16 decisive counterexamples. I found no remaining
scope, correctness, certificate, or contribution gap requiring revision.
