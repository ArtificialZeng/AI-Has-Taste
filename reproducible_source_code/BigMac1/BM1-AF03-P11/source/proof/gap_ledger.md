# Gap ledger

| ID | Proposition/location | Missing step | Severity | Test/repair | Status |
|---|---|---|---|---|---|
| G01 | All-`n` terminal-deletion theorem: `pi in M_{2n}` iff `pi_{2n} in {n,...,2n}` and `std(pi_1...pi_{2n-1}) in M_{2n-1}`. | Proved only for the certified finite pair `(13,14)` by a complete skeleton-set comparison. | scope limitation for full conjecture; not a gap in the finite theorem | Seek an all-`n` proof of `Q_{2n}={wL:w in Q_{2n-1}}`. | open |
| G02 | Use of Zhang's maximum-order theorem and Berlow periodicity theorem. | Both original primary sources and exact theorem locations are now audited. | major | Source and small-case checks. | closed |
| G03 | Baseline `n<=6`. | Two independent exact enumerators and the no-import verifier reproduce every relation through `n=6`. | major | See certificate records for lengths 1..12. | closed |
| G04 | First unverified equality `|M_14|=8|M_13|`. | Exact counts, skeleton bijection, independent reconstruction, and integer equality are certified. | fatal | See certificate, verifier, and `proof/finite_result.md`. | closed |
| G05 | Conjecture 4.3 pruning. | Printed statement fails for lengths 3 and 4 and remains conjectural later. | fatal if used | Do not use it in certification without a separate proof for the entire certified range. | guarded |
| G06 | Large-label factorization. | Human proof must justify delaying large-caused pops, including next-small and final-flush cases. | major | Proof in `proof/finite_result.md`; 362,879 literal projection tests through length 8. | closed |
