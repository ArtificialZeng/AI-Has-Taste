# Proof audit

Audit role: Referee, performed serially after the Builder and Breaker records.
The audit restarts from `problem/formal_statement.md` and does not infer the
theorem from timing, heuristic search, a solver return code, or the number of
generated PDFs.

Current status: **PASS**.  The lower and upper bounds, independent full sweep,
negative controls, and declared trusted base have all been reconstructed.

## Statement and quantifiers

- The target is the universal assertion over all order-11 tournaments, not a
  random, regular, score-sequence, or fractional variant.
- A tournament arc is in bijection with its unordered endpoint pair, so the
  hypergraph matching reduction preserves exactly the requested
  arc-disjointness convention.
- Relabeling preserves transitivity and pair intersections.  It is therefore
  logically sufficient to inspect one representative of every isomorphism
  class, provided the canonical-generator contract holds.
- The formula at the endpoint is exactly `ceil(110/6 - 11/3) = 15`.

## Upper bound reconstructed without discovery code

The literal certificate partitions the vertices as `0123|4567|8,9,10` and
has cyclic cross-part arcs.  Any triple meeting all three parts is cyclic;
therefore a transitive triple consumes at least one of the `6+6+3=15`
within-part pairs.  Pair-disjoint copies cannot reuse that resource, so the
packing number is at most 15.  The serialized witness lists 15 transitive
triples and 45 distinct pairs, proving equality for that tournament.

`code/verify_minimizer.py` reconstructs these facts from the literal JSON and
checks every transitive triple rather than importing `exact_max` output.  It
reports 117 transitive triples checked.  Six corruptions of the JSON are
rejected.

## Lower-bound search logic

The Builder's state recursion is exhaustive.  For its chosen live pair `e`,
any completing matching either uses exactly one currently available
hyperedge through `e` or uses none.  These are precisely the cover branches
and the dead-pair branch.  Availability can only decrease as blocked pairs
increase, so closure is monotone and safe.  Each further triple requires
three live pairs, making `depth + floor(live/3)` an integer upper bound.
Every success is rechecked for transitivity and pair disjointness.

The full Builder certificate has 192 successful residue summaries, verified
total 903,753,248, 14,481,704,095 search nodes, and no below-target literal.
The class total is independently obtained with `fractions.Fraction` from the
Davis/Burnside formula.  Count equality supports but does not prove the
absence of an isomorphic duplicate paired with an omitted class; canonical
generation remains in the trusted base.

## Independent algorithm

The Certifier does not import Builder output.  It recomputes transitivity by
internal outdegrees, builds a compatibility graph on transitive triples, and
uses include/exclude clique recursion.  Including the first candidate and
intersecting with later compatible vertices, or excluding it, partitions all
cliques without duplication.  Candidate cardinality is an exact upper bound.
Every reported clique is independently rechecked.

This source-level argument has been checked.  The decisive full Certifier run
then passed all final requirements:

1. 192/192 zero statuses and exactly one strict summary per residue;
2. exact total 903,753,248;
3. equality of every residue count and regenerated stream SHA-256 with the
   Builder certificate;
4. different Builder and Certifier executable SHA-256 values.

The Certifier used 16,972,027,052 exact search nodes and its largest single
instance used 203,790.  The comparison artifact
`certificates/n11_sweeps_match.json` binds Builder certificate SHA-256
`dfd409434c400a52e146e0908226c90a70c4dd5784d18170eb054cea7a1112da`
to Certifier certificate SHA-256
`19c9c393b693d7844d3b3bbba216709e04e95d6e7ab099ae86da65ac565ae98a`.

## Baselines and adversarial controls

- Both exact programs accept the full known order-9 and order-10 baselines;
  their slice counts and stream digests match in
  `certificates/baseline_n9_sweeps_match.json` and
  `certificates/baseline_n10_sweeps_match.json`.
- Explicit correct targets `0,1,2,3,5,7` were rerun at orders 3--8 after the
  earlier zsh word-splitting diagnostic error.
- AddressSanitizer and UndefinedBehaviorSanitizer accepted all 6,880
  canonical order-8 inputs for both programs.
- Structured cyclic blow-ups and 100,000 seeded random tournaments were
  attacked by both search formulations.  These diagnostics do not enter the
  universal proof.
- Twenty-one malformed-artifact controls exercise the scanners, aggregator,
  sweep comparator, and minimizer verifier; every corruption is rejected.

## Exactness and trusted base

The decisive algorithms use integer and bitwise operations only.  There is
no floating-point tolerance, modular surrogate, optimizer incumbent, or
unreplayed SAT result.  No proof assistant is used.  The declared trusted
base is the correctness/completeness of nauty 2.9.3 `gentourng`, the compiled
C/Python/OS semantics, and SHA-256 for integrity binding.  The searcher itself
is substantially cross-checked by the different Certifier design.

## Referee conclusion

Within that explicit trusted base, the complete lower-bound computation proves
that every order-11 tournament has a 15-packing.  The independently verified
cyclic `4+4+3` tournament has packing number exactly 15.  Therefore the
audited mathematical conclusion is `nu_3(11)=15`.  The appropriate terminal
classification is `CERTIFIED_FINITE_RESULT`, not a proof of Yuster's formula
for any order beyond 11.
