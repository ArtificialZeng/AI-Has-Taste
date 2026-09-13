# Checkpoint

## Current conclusion

The frozen 24-vertex minimum-degree-three assertion remains unresolved.
Research pass 2 produced a narrowly scoped `result-note` candidate: every
24-vertex simple graph with degree sequence `(5,3^23)` contains a simple cycle
of length 4, 8, or 16.  This subsidiary finite exclusion does not cover
`(4,4,3^22)` or higher degree excess and therefore does not prove the original
claim.

## New decisive evidence

`evidence/audit_excess2_A.md` proves the reduction around the unique degree-5
vertex and records a clean rebuild and exact reproduction of all three nauty
enumerations.  For neighborhood-matching sizes `m=0,1,2`, the new logs again
exhaust respectively 294,693, 835,745, and 1,087,732 residual graphs and
27,540,135, 5,486,880, and 45,900 reconstructed attachments.  Every attachment
is rejected by a C4 or C8 after residual graphs already containing a C8 or C16
are soundly discarded; no witness remains.

Three separate component tests materially reduce the pass-1 audit gaps:

- brute-force labeled attachment enumeration agrees exactly with the 945,
  420, and 45 gadget-orbit representatives;
- the production cycle detector agrees with an unpruned reference detector on
  57,234 cases, including all graphs on six vertices for C4 and fixed boundary
  fixtures for C4/C8/C16;
- the graph6 parser agrees byte-for-byte with nauty `showg` on 21 deterministic
  shard samples.

Sources, commands, hashes, exact counts, and limitations are in
`evidence/audit_excess2_A.md`; raw new counts are in
`evidence/pass2_A_m0.log`, `evidence/pass2_A_m1.log`, and
`evidence/pass2_A_m2.log`.  `source.md` remains unchanged with SHA-256
`8c3b64806f2471c61924f4be72e1873a67a03633e8fc843b70d0916afd0aba1e`.

## Obstacles and remaining gap

The requested certificate-producing SAT route did not reach an UNSAT proof;
the retained CryptoMiniSat CNFs remain `UNKNOWN` search state and are not used
for the candidate.  The exact enumeration is still conditional on a fresh
referee validating the reduction, nauty generation semantics, and rerun.
Family `(4,4,3^22)` is untouched in this pass, and the supplied local primary
source PDF was not present inside `PROJECT_DIR`, so no new literature-priority
claim is made.

## One next test

Give `claim.json` and every listed evidence file to a fresh referee.  The
referee should independently prove the reduction, clean-build all three audit
harnesses, and rerun the three `geng` pipelines; any mismatch rejects the
candidate.  Only after that scope decision should research split and attack
the `(4,4,3^22)` family.
