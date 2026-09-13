# Proof dependency graph

## Target

`THM11`: (\nu_3(11)=15).

## Human and exact-computational dependencies

1. `DEF-HG` (proved directly from the definitions): for a tournament (T),
   form the 3-uniform hypergraph whose vertices are the 55 unordered vertex
   pairs and whose hyperedges are the pair-sets of transitive vertex triples.
   Then (\nu_3(T)) is the matching number of this hypergraph.
2. `ISO` (proved directly): `DEF-HG` is preserved by tournament isomorphism,
   so it suffices to inspect one tournament from every isomorphism class.
3. `COUNT11` (exact computation): Davis's Burnside formula, evaluated with
   `fractions.Fraction` by `code/burnside_count.py`, gives exactly
   903,753,248 isomorphism classes at order 11.
4. `GEN11` (external generator contract plus checks): the pinned local
   `gentourng` canonical generator emits one representative from every class;
   its complete residue partition emits exactly the `COUNT11` total.  The
   canonical-generation theorem/implementation is in the trusted base.
5. `BUILDER-SOUND` (code-level lemma): `code/builder_scan.c` returns success
   on a tournament only after constructing and rechecking 15 mutually
   pair-disjoint transitive triples.  Its branching is exhaustive if it ever
   reports below target: after choosing a live pair (e), every extension
   either covers (e) by one of the enumerated available triples or leaves
   (e) uncovered.  Closure removes only pairs lying in no available triple;
   the only pruning inequality is the integer bound
   (d+\lfloor L/3\rfloor<15).
6. `CERTIFIER-SOUND` (independent code-level lemma):
   `code/certifier_scan.c` independently defines transitivity through the
   internal outdegree multiset, makes transitive triples the vertices of a
   compatibility graph, and tests for a clique of size 15 by exhaustive
   include/exclude recursion.  A clique is exactly a packing.  The pruning
   bound is only the number of remaining candidate vertices.
7. `SWEEP11-B` (verified): the complete Builder residue sweep has no failure,
   exact total `COUNT11`, and a SHA-256 digest for each tournament stream.
   The 192-slice aggregate is `certificates/n11_builder_full_m192.json`.
8. `SWEEP11-C` (verified): the complete no-import Certifier residue sweep has
   no failure, exact total `COUNT11`, and the same per-slice stream digests as
   `SWEEP11-B`.  The aggregate and comparison are
   `certificates/n11_certifier_full_m192.json` and
   `certificates/n11_sweeps_match.json`.
9. `LB11` (proved within the declared generator trust base): by `ISO`,
   `GEN11`, and the independently audited sweeps, every 11-vertex tournament
   has a 15-packing.
10. `MIN11-LB` (verified): `certificates/minimizer_11.json` contains 15
    pairwise arc-disjoint transitive triples.
11. `MIN11-UB` (verified human/exhaustive micro-certificate): the serialized
    tournament has cyclic cross-part orientation on parts (4,4,3).  Every
    transitive triple has a within-part pair; there are
    (\binom42+\binom42+\binom32=15) such pairs, and a packing cannot reuse
    one.  `code/verify_minimizer.py` also checks this property against all 117
    transitive triples of the literal tournament.
12. `UB11`: `MIN11-LB` and `MIN11-UB` give one tournament with packing number
    exactly 15, hence (\nu_3(11)\le15).
13. `THM11` (proved): follows from `LB11` and `UB11`, so
    (\nu_3(11)=15).

## Trusted base

- integer and bitwise operations of the compiled C programs;
- SHA-256 implementation supplied by macOS CommonCrypto (integrity only, not
  mathematical search soundness);
- correctness and completeness of nauty's `gentourng` canonical enumeration;
- OS process/pipeline semantics recorded by the driver.

The class total is not trusted to nauty: it is recomputed independently by
Burnside arithmetic.  No floating-point arithmetic, optimizer, SAT solver, or
proof assistant is used in the decisive lower-bound computation.
