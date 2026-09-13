# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `result-note` claim frozen in `claim.json`, bound to
snapshot digest
`6c3aafc069f23b0caea3344338d77416928671d17526b17b05f878bcd801b835`.
The claim classifies all pairs `(n,D)` only for `1 <= n <= 32`; it explicitly
leaves the original `n <= 64` problem unresolved.  I did not treat it as a
resolution of the original problem.

I recomputed every SHA-256 value in `audit/snapshot.json` and recomputed the
snapshot digest from its canonical file map.  All values matched.  In
particular, the immutable `source.md` hash remained
`9af585eacaa706a00b1b19a6b7e25c19ef77721221e340c3908f32c3a19abd8b`.

## Reconstruction of the decisive argument

For fixed `n`, the increasing strict-divisor list has `tau(n)-1` entries, and
the integer masks `0,...,2^(tau(n)-1)-1` are in bijection with all subsets
`D` of that list.  Summing these ranges for `1 <= n <= 32` gives 539 inputs.
The generator traverses these inputs in lexicographic `(n,dmask)` order and
constructs adjacency directly from `x != y` and `gcd(x-y,n) in D`, using only
integer operations.  Its complement operation toggles every off-diagonal
pair, which agrees with replacing `D` by `D_n \ D`.

It remains to justify the negative certificates for records labelled
perfect.  In either the graph or its complement, translation modulo `n` is an
automorphism.  Thus any induced cycle can be translated so that one of its
vertices is 0.  For every odd target length from 5 through `n`, the DFS starts
with 0 and every possible neighbor of 0.  Its invariant is that the current
list is an induced path: an extension must be adjacent to the last vertex and
nonadjacent to every earlier non-predecessor.  A later vertex adjacent to 0 is
not extended; it is accepted only at the target length and only when it has no
edge to any other earlier non-predecessor.  Consequently every accepted list
is an induced cycle of the target length.  Conversely, either orientation of
any induced cycle through 0 supplies one of the enumerated first neighbors,
and each successive cycle vertex passes exactly these tests, so the relevant
DFS branch is not pruned.  Exhausting all odd targets is therefore a complete
odd-hole test.  Applying it to both sides is a complete Berge test, and the
Strong Perfect Graph Theorem gives the recorded perfectness value.

The search stops on the graph side once a graph odd hole is found and otherwise
searches the complement.  This does not weaken a perfect record: both searches
must have been exhausted before such a record is emitted.  Nor does it weaken
an imperfect record, for one valid forbidden cycle already proves
imperfectness.  The optional structural labels are not used in this decisive
argument.

## Checks actually performed

- Running `evidence/n32_census.py` afresh produced
  `audit/referee_regenerated_manifest.json`, byte-for-byte identical to the
  frozen manifest.  It again reported 415 perfect records, 124 imperfect
  records, 2,789,071 search states, records digest
  `fe36f96a628851b9ef03d912c8d9ec451e48d4c7773ab12626aa36a52610357e`,
  and manifest digest
  `637121fe094a6321bd5c1abf182a215a24e42931d49507cc8d405c39e7e61188`.
- I reran the separate adjacency/witness verifier.  Its output
  `audit/referee_replay.json` matches the frozen replay and verifies the exact
  ordered 539-input domain, every adjacency digest, all 124 witnesses pair by
  pair, and all declared canonical forms.  The witnesses split into 105 on
  the graph side and 19 on the complement side, with lengths 5, 7, and 9.
- I reran the NetworkX 3.4.2 chordless-cycle implementation on every record.
  `audit/referee_networkx.json` reports 539 records checked, 1,602,322
  chordless cycles scanned until decisions, and no mismatch.
- As a third implementation check, I wrote
  `audit/referee_subset_check.py`.  It does not use translation symmetry or
  path DFS: it enumerates every odd-cardinality vertex subset and tests whether
  the induced subgraph is connected and 2-regular.  On all 109 manifest
  records with `n <= 16`, including all six imperfect records at `n=12`, its
  output `audit/referee_subset_check.json` reports no mismatch.
- I parsed the five mask rows in `evidence/n32-result.md` and compared them
  with the manifest.  All 124 imperfect masks agree exactly.  Independently
  grouping the manifest gives imperfect orders precisely
  `{12,20,24,28,30}` and counts 6, 6, 54, 6, and 52.
- Complement-paired masks have identical status in all 539 records.  For every
  `n`, masks 0 and `2^(tau(n)-1)-1` are perfect.  The `n=1` record is present
  and perfect.  Thus the empty, complete, disconnected, and one-vertex
  boundary cases have not been dropped.

No floating-point computation, division, limiting argument, probabilistic
step, or unchecked equality case enters the classification.  Witness
canonicalization affects only presentation and not the existence decision.

## Source comparison and contribution

I checked the locally frozen primary-source PDF itself.  Its Section 2 gives
the same arbitrary-divisor-set definition of `ICG_n(D)`, and its Section 5
states that the full perfect integral-circulant classification remains open
while identifying the unitary family as previously classified.  The collision
screen identifies that unitary result as the nearest proper subfamily and
also separates So's earlier spectral enumeration of integral-circulant
symbols from perfectness labels and forbidden-cycle certificates.  Under the
snapshot restriction, only the Basic PDF—not full copies of every other paper
summarized by the screen—was available for direct text inspection.  This is a
literature-limit disclosure, not mathematical support for priority.

The candidate makes no priority or first-enumeration claim: it reports only a
bounded negative source screen.  Its precise delta is an exact arbitrary-`D`
perfectness census, compressed mask table, and replayable two-sided
certification for the complete 539-input `n <= 32` layer, rather than a result
for `D={1}` or a spectral list of graph symbols.  This is a nontrivial finite
classification and a reproducible benchmark for the remaining `33 <= n <=
64` layer and for testing future structural classifications; it is not a
routine corollary of the nearest result identified in the available source.

## Limitations and verdict

The work proves nothing for `33 <= n <= 64` or unbounded `n`, gives no general
divisor-lattice characterization, and has 86 perfect records outside the short
list of optional structural classes.  These limitations are already explicit
in the frozen statement and do not undermine the exhaustive certificate at
the claimed scope.  The bounded literature screen cannot prove priority, so
future publication must retain its conservative novelty language.

**Verdict: accept the exact frozen scope as a `result-note`; the original
problem remains unresolved.**  Scope, correctness/evidence, and contribution
pass without revising the claim.
