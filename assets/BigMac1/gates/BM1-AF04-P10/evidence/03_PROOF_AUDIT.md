# Proof audit

Audit date: **2026-08-30 Asia/Shanghai**.

## Claim under audit

For the specifically serialized Appendix C 333-plane code \(C_0\), every
minimum-distance-four code obtained by deleting at most seven members of
\(C_0\) and adding arbitrary ambient subspaces has at most 334 members.  The
claim includes additions in all dimensions 0 through 7.  It does not assert a
global upper bound on \(A_2(7,4)\).

## Logical reconstruction

1. Appendix data reconstruct 333 distinct rank-three subspaces of pairwise
   distance at least four.
2. Canonical RREF enumeration reconstructs every ambient subspace and the
   exact layer census summing to 29,212.
3. For an outside word \(X\), its blocker set is exactly the baseline words
   incompatible with \(X\).
4. In any feasible exchange, the union of blocker sets of the additions is a
   subset of the deletions.  Restoring every unused deletion preserves
   feasibility and weakly improves size.
5. It suffices to enumerate all blocker unions of cardinality at most seven.
   Independent closure finds 2,561,563 such unions.
6. For a fixed union \(R\), allowable additions are exactly the cliques of the
   compatibility graph on candidates with blocker set contained in \(R\).
7. These graphs have at most 15 vertices.  Exhaustive testing of all subsets
   gives exact best assembled sizes 334,333,333,333,334,333,333,333 for
   removal sizes 0 through 7.
8. Adding the full space at removal size zero attains 334.

The argument proves both the upper and lower sides of the finite claim.

## Independence and exactness

- Discovery uses 128-bit membership masks, intersection cardinalities, an
  overlap-index union closure, and coloring branch-and-bound.
- Verification imports no discovery module.  It uses RREF row tuples, rank of
  concatenated bases for distance, a split-union closure, and exhaustive
  subset dynamic programming.
- All decisive operations are integer/bit arithmetic over \(\mathbb F_2\).
  Timings, the HiGHS diagnostic, and floating solver bounds are excluded from
  the proof.
- `certificates/radius7_verification.json` binds the Appendix data, 334-word
  code certificate, radius-seven report, and verifier by SHA-256 and records
  `proof_assistant_used: false`.

## Adversarial audit

The first verification pass rejected a discovery serializer that printed
pivot snapshots instead of final reduced rows.  Although its membership masks
and search result were correct, the output was not canonical RREF.  The bug was
fixed, discovery artifacts were regenerated, and both finite radii were
reverified.

The final fail-closed suite rejects duplicate codewords, unknown schema keys,
a singular generator, malformed JSON, and a forged optimum 335.  Each failure
has a nonzero verifier exit and `VERIFY_FAIL` diagnostic; see
`audit/fail_closed_tests.log`.

## Referee conclusion

No unresolved gap remains in the finite radius-seven statement.  The global
endpoint and an independent exact SDP upper certificate remain unresolved and
are explicitly excluded.  Verdict: **accept as `CERTIFIED_FINITE_RESULT`**.
No proof assistant was used.
