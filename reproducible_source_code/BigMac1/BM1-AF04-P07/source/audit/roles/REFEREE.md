# Referee record

The Referee restarts from the definitions, checks quantifiers, finite coverage,
certificate semantics, novelty, and failure controls, without treating the
Builder's search intuition as evidence.

## Preliminary reconstruction (2026-08-30)

1. The source and formal statements agree at the exact endpoint (n=11); the
   formula evaluates to (15), not by an asymptotic or fractional convention.
2. The (4+4+3) upper bound is human-readable and independently executable.
3. The class total 903,753,248 is reproduced by exact Burnside arithmetic and
   appears in OEIS A000568.  Count agreement does not itself prove that a buggy
   generator emits no duplicate isomorphism classes; `gentourng` completeness
   remains an explicitly declared trusted-base item.
4. Builder and Certifier have genuinely different formulations (resource
   branching versus compatibility-graph clique search) and different
   transitivity predicates.
5. An early zsh regression loop accidentally passed target zero for some
   small orders.  Explicit reruns with targets (0,1,2,3,5,7) corrected the
   diagnostic; the incident is retained in `proof/gap_ledger.md`.
6. The complete Builder sweep, complete different-algorithm Certifier sweep,
   192-slice comparison, and post-certification novelty pass have passed.  The
   exact finite theorem is established within the declared generator trust
   base.  Only the clean LaTeX build, citation/PDF audits, and release manifest
   remain open.
