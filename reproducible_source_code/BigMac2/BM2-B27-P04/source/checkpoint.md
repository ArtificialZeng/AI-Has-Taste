# Checkpoint

## Current claim

The frozen universal assertion is proved by an exact finite classification.
Up to isomorphism, the regular ordinary distance-magic graphs on eight vertices
are exactly \(8K_1,2C_4,K_{4,4},K_{2,2,2,2}\). Their reduced adjacency
nullities over \(\mathbb F_2\) are respectively \(7,4,6,4\), all at least two.
The criterion in `problem.md` therefore gives a generating
\((\mathbb Z/2\mathbb Z)^3\)-magic map for each class.

## Decisive evidence

- `source.md` remains unchanged with SHA-256
  `59a054758e876b4f40c2ad469819dc925ef8f259f2d23eeafa4a82b8d2f04053`.
- `evidence/enumerate_order8.py` generates the 1, 3, 6, and 1 nauty graph6
  representatives in degrees 0, 2, 4, and 6; exhausts all 40320 labelings of
  each (443520 total); and performs exact quotient-matrix row reduction.
  `evidence/order8_classification.json` stores all adjacency matrices, edge
  lists, ordinary-label counts and witnesses, quotient matrices, elementary
  row-operation transcripts, RREFs, and kernel bases.
- Exactly four of the eleven classes are ordinary distance-magic. Their graph6
  records are `G?????`, ``G?r@`_``, `G?~vf_`, and `G]~v~w`; witness
  neighborhood constants are 0, 9, 18, and 27.
- `evidence/verify_order8_certificate.py` uses `showg` rather than the producer's
  graph6 decoder, repeats all 443520 integer labeling checks, independently
  recomputes all binary ranks, checks kernel vectors, and replays row operations.
  `evidence/verification_report.json` records `status: pass`.
- `evidence/verify_unlabeled_coverage.py` provides an independent coverage
  certificate. It computes canonical codes and automorphism orders from all
  8! relabelings, then compares orbit-size sums with a separate exact recursion
  over all labeled regular graphs. Both sides equal 1, 3507, 19355, and 105 in
  degrees 0, 2, 4, and 6. `evidence/coverage_report.json` records `status: pass`.
- `evidence/classification.md` gives the compact proof and certificate map.

## Obstacles and failed routes

The first coverage-recursion run used an invalid index-dependent pruning bound
and returned zero degree-2 graphs. It was classified as an implementation
failure, corrected to the valid unprocessed-suffix bound, and rerun successfully.
No mathematical gap is presently known. Novelty remains `status-uncertain`:
the earlier limited primary-source screen found no exact classification but did
not establish priority. The bibliographic author/title mismatch in immutable
`source.md` remains documented in `problem.md` and does not alter the theorem.

## One next test

Freeze `claim.json` and give a fresh referee the exact statement plus
`evidence/order8_classification.json`, `evidence/verification_report.json`, and
`evidence/coverage_report.json`; ask it to attack quotient-basis correctness,
ordinary-label exhaustiveness, and the orbit-sum isomorphism-coverage argument.
