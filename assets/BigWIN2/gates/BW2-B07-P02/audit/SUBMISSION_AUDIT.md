# Submission-readiness audit

Status: PASS (2026-08-30 UTC).

## Mathematical gate

- [x] Formal theorem matches the literal source problem after the explicit
      reindexing \(m=n+1\).
- [x] Definitions, integer endpoints, and the empty-permutation convention
      are stated before use.
- [x] Boundary evaluations and all parity/end-point cases are justified by
      absolute convergence.
- [x] No equality or sharpness classification is claimed beyond strict
      negativity on the stated range.
- [x] The finite certificate has an independent outward-rounded checker.
- [x] All fatal and major gap-ledger entries are closed.
- [x] Diagnostics and the interrupted slow computation are not evidence.

## Novelty and citation gate

- [x] The original source and exact conjecture are cited.
- [x] Adjacent asymptotic results, later records, corrections, and exact
      fingerprints were searched before and after the result.
- [x] Every citation was checked against the nearby claim.
- [x] Publisher, DOI, journal, arXiv/full-text, and database metadata were
      checked as appropriate.
- [x] All five citation keys are defined and all five entries are used.
- [x] Novelty wording is explicitly bounded by query set and date.

## Reproducibility gate

- [x] Stable commands and paths are documented.
- [x] Versions are recorded; randomness and seeds are not applicable.
- [x] Fast and full verification targets are separated.
- [x] The fast clean run succeeds without cached bytecode.
- [x] The final manifest binds source, code, certificate, paper, PDF, and ZIP.
- [x] No formalization claim is made.

## Manuscript gate

- [x] Title and abstract state the proved result.
- [x] Prior work, the new result, and the limitation of prior non-effective
      asymptotics are separated.
- [x] Notation and endpoints were checked against the formal statement.
- [x] All decisive inequalities and certificate logic are readable in the
      paper.
- [x] Computational and language-model assistance is disclosed accurately.
- [x] Author name, affiliation, and both emails exactly match the data
      supplied by the author; no unsupported funding claim is inserted.
- [x] Standard AMS bibliography formatting is used because no target
      journal style was specified.
- [x] A clean source build has no undefined references, citations, or
      substantive warnings.

## PDF gate

- [x] Every rendered page is visually inspected.
- [x] There is no clipping, overlap, missing glyph, black box, or broken link.
- [x] PDF title and author metadata are correct.
- [x] Page count, file size, and SHA-256 are recorded outside the paper.

## Handoff gate

- [x] Scientific status and absence of proof-assistant use are stated.
- [x] Build, test, and citation results are reported.
- [x] Links to proof, certificate, audit, manuscript, PDF, and ZIP are prepared.
- [x] No acceptance or peer-review claim is made.
