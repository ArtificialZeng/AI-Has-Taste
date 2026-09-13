# Referee record

Role completed after Certifier: 2026-08-30T04:55Z.

## Independent reconstruction

Starting from the definition rather than the discovery output, the Referee
reconstructed the following chain.

1. Equal-length block-sum equality is exactly a zero second difference in the
   prefix sums.
2. Integer affine normalization with nonzero multiplier and reflection
   preserve the property.
3. Primitive normalized four-letter alphabets of height at most five have
   exactly seven reflection classes.
4. In a valid-prefix DFS, only suffix factors can be newly created after an
   append, so complete child testing closes the whole ASF tree.
5. A maximum-depth word gives the lower bound and a closed tree gives the
   upper bound.
6. A four-symbol 2-uniform endomorphism prolongable on a relabeled zero has
   exactly seven free image positions. An abelian-square witness under every
   one of the \(4^7\) assignments rules out every integer weighting in this
   class.

The manuscript theorem statements match this chain and do not claim an
infinite result.

## Defect found and remediation

The first coordinator revision recomputed every supplied v2 record but did
not require that all seven canonical alphabet records be present. A
scope-claiming certificate with one entire record deleted could therefore
have passed schema-only validation and, for the remaining records, full
replay.

The coordinator was changed to bind each supported schema to an exact scope
string and exact ordered alphabet list. A seventh corruption test now deletes
one canonical record and is rejected. The complete seven-tree verification
was rerun after this fix and returned VERIFIED with the same certificate and
independent C++ hashes.

## Scope and overclaim audit

- The original infinite finite-integer problem remains open in the checked
  corpus and in this work.
- The census stops at primitive normalized maximum 5 and four letters.
- The morphism no-go stops at four states and uniform length 2.
- The scalar projection screen is bounded by coefficient height 100 and
  prefix length 30,000.
- The failed modular route is not used in any conclusion.
- Search-based novelty wording is date- and database-bounded and contains no
  priority claim.

## Artifact audit

- Every cited item exists and supports the nearby statement.
- The bibliography has nine cited and nine defined entries, with no missing
  or unused keys.
- The clean LaTeX build has no undefined references, citation failures,
  overfull/underfull boxes, warnings, or errors.
- All five final PDF pages were rendered and inspected.
- PDF body and metadata contain only Zijian Zeng as author; the required UCSI
  affiliation and both required email addresses are present.
- No proof assistant or formalization claim is made.

## Referee disposition

ACCEPT as a certified finite computational result, subject to ordinary
external peer review. The two exact height-five maxima and the restricted
morphism no-go are supported by complete exact enumerations with independent
replay. REJECT any interpretation that this resolves the infinite existence
question.

Terminal class: CERTIFIED_FINITE_RESULT.
