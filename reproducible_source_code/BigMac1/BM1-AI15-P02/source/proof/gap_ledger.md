# Gap ledger

| ID | Proposition/location | Missing step | Severity | Test/repair | Status and evidence |
|---|---|---|---|---|---|
| G01 | Source phrase “all symmetry operations” at `n=2` | A square has eight geometric symmetries, but OEIS uses four | fatal | Compute both exact orbit counts and state the Klein-four convention | **resolved**: `problem/formal_statement.md`; exact counts 23 versus 14 in all three agent audits |
| G02 | Burnside transfer formula | Prove middle-edge and middle-state formulas for vertical and half-turn fixed words | major | Derive reversal-involution bijections and test parities | **resolved**: equations (2)–(4) in `proof/main_proof.md`; builder and root verifiers reconstruct all vectors |
| G03 | All-`n` recurrence | Finite agreement does not imply the scalar recurrence | fatal | Exact resolvent or finite-dimensional observable annihilation plus Cayley–Hamilton | **resolved twice**: builder polynomial identity `Z(I-yT)=D0*u^T`; root 68-dimensional certificate has 68 exact observable zeros |
| G04 | Claimed minimal order | Degree ten is insufficient if numerator and denominator cancel | major | Exact gcd/Bezout certificate | **resolved**: five factor remainders in the proof and serialized rational Bezout identity in root certificate |
| G05 | Novelty claim | Search pass 1 may miss a new/all-`n` proof | local | Repeat exact theorem/formula searches after endpoint freeze | **resolved**: endpoint-frozen second pass recorded in `literature/search_log.md`; no prior all-`n` proof found in the bounded searches |
| G06 | Citation integrity | Each source must exist and support its nearby claim | major | Primary-source metadata and citation audit | **resolved**: `audit/CITATION_AUDIT.md` verifies 20/20 claims with no open issue; LaTeX audit reports 4/4 used records |
| G07 | Release readiness | The live scheduler log made the first whole-tree manifest unstable; builder verifier and referee hashes needed post-hardening refresh | major | Cross-version fail-closed matrix, independent no-import audit, refreshed referee report, stable release manifest | **resolved**: three verifiers give 12 genuine PASS/24 tamper FAIL across Python 3.9/3.14 normal and `-O -I`; referee hashes are current; static `release/frozen` manifest verifies |

The independent referee's second round (`agents/referee_report.md`, Section 8)
found no remaining fatal or major mathematical gap for the repaired
four-operation theorem.  Novelty, citation, certificate, and release gates
are closed.
