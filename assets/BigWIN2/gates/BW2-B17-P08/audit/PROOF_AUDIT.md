# Proof audit

Status: **PASS for the finite theorem `F(4)>=202`**.

- Formal quantifiers, distinct-generator convention, eligibility endpoint,
  and subset-sum collisions are explicit.
- Proof and disproof routes were pursued symmetrically; the exact witness
  refutes the `F(4)=201` route.
- Independent verifiers use different generator and sumset decompositions.
- Both scan all 2,587,336 eligible sets and agree on the full histogram.
- No SAT/UNSAT verdict, floating-point number, randomness, sampling, or timeout
  enters the proof.
- All major/fatal entries in `proof/gap_ledger.md` are closed.
- Scope is limited to `F(4)>=202`; the exact value is not claimed.
