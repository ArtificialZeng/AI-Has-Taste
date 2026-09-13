# Submission-readiness audit

Date: 2026-08-30 CST.  Status: PASS.  The release manifest was regenerated from
the stable `release_manifest_root` staging tree and independently verified using
absolute paths.  The live research log is preserved in the project tree but is
excluded from both the staging tree and the frozen manifest.

## Mathematical gate

- [x] Formal theorem matches the source problem and final scope.
- [x] All hypotheses are stated at the theorem endpoint.
- [x] Branch, zero, boundary, singular, and starting-index cases are covered.
- [x] Exact certificate is independently reproducible.
- [x] No fatal or major proof gap remains.
- [x] Finite computations are diagnostics, not the universal proof.

## Novelty and citation gate

- [x] Original EGF source and exact OEIS conjecture are cited.
- [x] Publisher/DOI/arXiv metadata and later citations were searched.
- [x] Two-pass novelty search is bounded by databases and date.
- [x] Frozen manuscript claim extraction and separate verification passed 12/12.
- [x] Citation keys: 2 cited, 2 defined, 0 missing, 0 unused.

## Reproducibility gate

- [x] Stable certificate, verifier, tests, proof, and commands are present.
- [x] No random seed is applicable; environment versions are recorded.
- [x] Clean build and exact fast tests pass.
- [x] Mutation rejection tests demonstrate fail-closed parsing/checking.
- [x] Release manifest binds 33 stable final artifacts and passes the independent
      manifest checker from absolute paths; it contains no `logs/` entry.

## Manuscript and PDF gate

- [x] Title and abstract state the proved result.
- [x] Prior EGF, new recurrence proof, and limitations are separated.
- [x] Proof and exact coefficient table are human-readable.
- [x] AI/computational disclosure is accurate.
- [x] Sole author, affiliation, and two emails match the user authorization.
- [x] LaTeX/BibTeX clean build has no substantive warnings.
- [x] All four PDF pages, metadata, fonts, and final whitespace were inspected.

## Handoff gate

- [x] Terminal mathematical status: `PROVED`.
- [x] Explicit statement: no proof assistant was used.
- [x] Proof, certificate, audit, manuscript source, and PDF are release targets.
- [x] No claim of peer review, journal acceptance, or absolute priority is made.
