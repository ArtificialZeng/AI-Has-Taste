# Gap ledger

| ID | Proposition/location | Potential gap | Severity | Test/repair | Status |
|---|---|---|---|---|---|
| G01 | Formal endpoint | Printed Conjecture 5.1 has incompatible sign and length conventions. | critical | Compare Definition 2.1, Theorem 2.9, fixed roots, and the same-sentence axis; state the actual-length repair explicitly. | closed |
| G02 | Reported baseline | “Verified through length 9” had no public certificate and could not be assumed. | critical | Reconstruct the regular length-9 poset from covers; exact factorization and rational Rouché disk give a counterexample. | closed by contradiction |
| G03 | Length-10 witness polynomial | Discovery recurrence might encode the source incorrectly. | critical | Primary verifier directly enumerates 13,860 linear extensions; independent verifier instead counts order-ideal multichains and obtains the same (h^*) and factor. | closed |
| G04 | Strict disk violation | Numerical roots cannot certify a closed-disk failure. | critical | Rational Rouché disk lies wholly outside (|y|=36); independent Cayley/Routh count also gives two outside roots. | closed |
| G05 | Routh interpretation | Two right-half-plane roots might be real or a transform artifact. | major | All coefficients of (P) are positive, excluding positive real roots; no Routh zero row/pivot; the Cayley real-part identity is exact and (Q(36)>0). | closed |
| G06 | Certificate trust boundary | A verifier could merely replay discovery coefficients. | critical | Rouché verifier rebuilds (h^*), (L), factor, Taylor data; independent Routh input has only six endpoint fields and rebuilds all coefficients. | closed |
| G07 | Fail-closed behavior | Malformed or adversarial serialized inputs might pass. | major | Strict schema/type checks plus three mutation suites; each accepts the witness and rejects 8/8 corruptions. | closed |
| G08 | Reversal quotient | Reversal was proposed without a source proof and is not generally a poset isomorphism. | minor for theorem | The discovery scan does not quotient; the witness proof needs no symmetry. No general reversal claim is made. | removed from dependency graph |
| G09 | First failing length | The project did not independently certify every shorter word as inside. | scope | Manuscript says only “failure no later than 9” and does not claim minimality. | explicitly limited |
| G10 | Novelty/priority | Database silence cannot prove absolute priority. | scope | Two bounded searches, including result fingerprints; manuscript uses bounded wording only. | explicitly limited |
| G11 | Proof-assistant coverage | No formal theorem prover binds the endpoint. | disclosure | State that no Lean, Coq, Isabelle, or other proof assistant was used; exact Python certificates cover the stated endpoints only. | closed by disclosure |

No unresolved critical or major proof gap remains for the terminal conclusion
`DISPROVED`.

