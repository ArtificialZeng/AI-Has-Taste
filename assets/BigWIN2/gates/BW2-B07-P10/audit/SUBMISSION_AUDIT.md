# Submission audit

Audit date: 2026-08-31.

## Pre-PDF gates

| Gate | Evidence | Status |
|---|---|---|
| Scope and source-statement preservation | literal `problem/source_statement.md`; locked `problem/formal_statement.md` | pass |
| Mathematical proof | `audit/PROOF_AUDIT.md`; serial Referee reconstruction | pass for partial theorem |
| Falsification symmetry | `roles/breaker.md`; small exhaustive and malformed-input attacks | pass |
| Independent certification | `roles/certifier.md`; clean `code/certificate_gate.py` run | pass |
| Citation completeness | six cited/six bibliography entries, no missing or unused keys | pass |
| Primary-source and metadata checks | `audit/CITATION_AUDIT.md`; archived PDFs/metadata | pass |
| Novelty wording | repeated exact-fingerprint search; explicitly bounded negative claim | pass |
| Honest endpoint | abstract, introduction, and limitations say exact \(U(17)\) remains open | pass |
| Reproducibility | standard-library integer checkers plus archived Table 59 comparison | pass |

The mathematical, citation, novelty, reproducibility, and manuscript-scope
gates pass for a partial-result submission.  PDF build quality, text-policy
checks, all-page visual inspection, and clean LaTeX-archive reconstruction
also pass; see `audit/PDF_AUDIT.md`.  The release manifest was frozen over the
PDF and source ZIP and then independently verified with the skill-provided
manifest verifier.

Scientific terminal status: **partial theorem**.  The audit does not promote
the work to an exact solution of the original problem.

Overall status: **passed for submission of the stated partial theorem**.
