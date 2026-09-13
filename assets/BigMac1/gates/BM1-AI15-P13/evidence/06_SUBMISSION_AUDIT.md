# Submission-readiness audit

Audit date: 2026-08-29 (Asia/Shanghai)

Outcome: **PASS for a project-level preprint release; no external submission
was attempted.**

- Precise theorem status: `DISPROVED`, with source ambiguity and scope limits
  stated in the abstract, introduction, and final section.
- Proof: independently reconstructed and exact-certified; no open fatal gap.
- Novelty: checked before and after theorem freeze and refreshed once more
  after verifier hardening; wording remains bounded to the named databases and
  queries.
- Citations: one of one verified; official arXiv BibTeX used; `.bbl`
  regenerated cleanly.
- LaTeX/PDF: clean build, log audit, metadata check, text extraction, and
  six-page visual review passed.
- Reproducibility: serialized scalar and 2-by-2 certificates, two strict exact
  Python verifiers, a 12-case fail-closed tamper suite, and an IEEE binary64 C
  cross-check are included. The release ZIP was rebuilt in an isolated
  directory; see `audit/CLEAN_REPRODUCIBILITY.md`.
- Disclosure: the manuscript states that generative-AI agents assisted with
  search, proof development, verification, literature work, and adversarial
  review. It explicitly states that no proof assistant was used and that
  numerical search is not proof.
- Authorship metadata: the existing workspace-supplied author, affiliations,
  and email were preserved in TeX and PDF metadata. They were not altered or
  independently identity-verified during this audit; the owner should confirm
  them before any external submission.
- Contribution trace: discovery/proof synthesis is represented in
  `proof/main_proof.md`; independent builder, breaker, referee, and citation
  records are in `notes/` and `audit/`; executable verification is in
  `verification/` and the root-level breaker scripts.

The release does not claim peer review, formal verification, publisher
acceptance of this counterexample, or a theorem for safeguarded variants of
SM--IR. In particular, the scale/no-lost-addend/contraction-guarded repaired
conjecture remains open.
