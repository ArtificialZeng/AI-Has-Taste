# Proof audit

Final status: **passed**, 2026-08-30.

## Positive endpoint

- `certificates/packing12.json` has SHA-256
  `23dc758771e6dce03b943a48aab50077a5ee00c36e24cde02f74aa2468f8cf45`.
- The no-import verifier reconstructs all 31 translations and accepts exactly
  372 developed blocks and 3,720 distinct triples.
- `tests/test_positive_verifier.py` passes and rejects malformed schemas,
  duplicate orbits, range/sorting errors, Boolean integers, and a deliberate
  triple collision.

## Structural reduction

- Translation canonicalization from the definitions gives exactly 145
  triple resources and 5,481 five-subset classes; internal triple collisions
  remove 720 and leave 4,761 valid block variables.
- Two valid variables are compatible exactly when their ten reconstructed
  resource IDs are disjoint.
- Pair-distance incidence proves the sound cap `pair_sum[d] <= 9` used by the
  enumerator. It is necessary for every feasible packing, so it cannot remove
  a solution.
- Multiplication by every unit modulo 31 is reconstructed after translation
  canonicalization. The 4,761 variables split into exactly 162 disjoint
  orbits with distribution `30^156,15^5,6^1`.

## Complete target-13 exclusion

- Fixing a canonical representative is complete: any nonempty target-13
  packing has a multiplier image containing one of the 162 representatives.
  Its remaining twelve blocks must be a 12-clique in that representative's
  exact compatibility neighborhood.
- `code/exact_clique.cpp` reconstructs the instance rather than importing the
  discovery graph. Its SHA-256 is
  `ae549763147bd579353d3b91fcbad4e9afb4e2e404c97f915115d8b6e84458c9`.
- Source inspection checked the resource definition, exact disjointness
  adjacency, sound pair cap, greedy-color upper bound, prefix adjacency
  intersection, exhaustive include/exclude branching, and strict recursive
  decrease. Details are in `proof/exact_clique_algorithm.md`.
- All 162 fixed-neighborhood searches returned
  `UNSAT_BY_COMPLETE_BRANCHING`. Their deterministic node counts total
  68,377,851,660, ranging from 251,805,613 (representative 537) to
  636,752,470 (representative 12).
- The branch scopes cover 4,761/4,761 variables exactly once. The locked
  global manifest has SHA-256
  `ae259e64de1793421a7e5e4bd525fec405133f3f277074a222badf6ac5d522b3`.
- `code/verify_global_fixed_cover.py` independently rebuilds the instance,
  multiplier partition, scopes, hashes, statuses, and aggregate counts. It
  returns `VERIFIED_GLOBAL_TARGET13_UNSAT`.

## Independent replay and rejection tests

- `tests/test_fixed_clique_certificate.py` accepts all 162 strict manifests
  and rejects changed block data, result hashes, scope/action text, truncated
  multiplier orbits, and Boolean-as-integer inputs.
- `tests/test_global_fixed_cover.py` accepts the locked global cover and
  rejects modified claim/action/status fields, branch/hash changes, missing or
  duplicated coverage, and aggregate-count corruptions.
- Fresh source rebuild/replays passed for representative 537 (minimum node
  count) and representative 362 (the unique size-six multiplier orbit).
- The compiler's strict-warning audit found only safe sign-conversion and
  aggregate-initializer warnings on validated ranges/default members; no
  undefined behavior or narrowing affected the proof logic.
- The full enumeration, encoding, exact-cover, OPB, leave, pattern, symmetry,
  fixed-reduction, positive, fixed, global, and LRAT regression tests pass.
- Two auxiliary LRAT refutations pass the official `lrat-check` built from
  drat-trim commit `2e3b2dc0ecf938addbd779d42877b6ed69d9a985`; truncation
  and semantic mutation tests are rejected. These LRATs are cross-checks, not
  the global target-13 certificate.

## Excluded material and residual limitations

- Every SAT/PB/CP-SAT/ILP/clique timeout, UNKNOWN status, interrupted run,
  incomplete proof stream, floating bound, and local-search failure is
  excluded from the proof.
- The exact upper bound is a certified finite computation checked by ordinary
  C++/Python code. No proof assistant was used, so the result is not a
  Lean/Coq/Isabelle formalization.
- The novelty conclusion is bounded by the databases and indexed code searched;
  it is not part of the mathematical proof.

## Verdict

The positive certificate proves \(M\ge12\). The complete multiplier cover and
exact branch enumerations prove \(M<13\). Therefore the audited conclusion is
\(M=12\), with no remaining mathematical branch.
