# Gap ledger

| ID | Proposition/location | Missing step | Severity | Test/repair | Status |
|---|---|---|---|---|---|
| G01 | N3 / projective normalisation | Confirm the two nonzero-row projective strata exhaust rank two and that the simultaneous `GL_2` action preserves `UV^T` without a hidden nonzero-coordinate assumption. | major | Homogeneous proof in `proof/n3_proof.md`; independent from-definitions reconstruction of factor-map injectivity, multiplicity partitions, PGL2 representatives, nonzero row scaling, and points at infinity in `audit/agents/referee_pgl2_equality.md`. | resolved |
| G02 | N3 / exact SOS identities | Discovery calculation must be rebuilt independently from permutation definitions. | major | `python certificates/verify_n3_sos.py` rebuilt both permanents and returned exact zero remainders; hashes recorded in verifier output. | resolved |
| G03 | N3 / equality classification | Prove that every vanishing SOS case is exactly rank one, a zero row/column, or a permuted `2 x 2` zero block, including homogeneous points at infinity. | major | Complete homogeneous case split in `proof/n3_proof.md`; exact symbolic family checks; independent referee exhaustion by `z=#\{j:c_j=0\}=0,1,2,3` and direct matching sufficiency in `audit/agents/referee_pgl2_equality.md`. | resolved |
| G05 | Certificate fail-closed behavior | Reject schema drift, byte changes, missing/extra keys, and altered theorem data rather than verifying a nearby certificate. | major | Both verifiers bind the canonical SHA-256 and enforce exact nested schemas; `certificates/test_fail_closed.py` rejects `badhash`, `extra`, `drop`, and `tamper` for both CLIs. | resolved |
| G04 | n=4 target | No proof or counterexample yet; a finite random search cannot decide the universal assertion. | fatal for any n=4 claim; not fatal for N3 | Structured normal form with cross-ratio plus exact search/SOS tests. | open |

All major gaps needed for the certified real `n=3` endpoint are closed.  G04
is deliberately outside that finite endpoint and prevents any claim for
`n=4` or general `n`.
