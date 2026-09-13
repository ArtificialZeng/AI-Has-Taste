# Submission audit

Audit date: 2026-08-29 (Asia/Shanghai).

## Mathematical gate

- [x] Formal theorem matches the matrix-specific source problem and final scope.
- [x] Every family hypothesis is stated at its endpoint.
- [x] Zero patterns, denominators, rank boundaries, and degeneracies are audited.
- [x] Three exact witnesses and independent serialized verifiers reproduce the endpoint.
- [x] No fatal or major proof gap remains for the stated theorem.
- [x] Numerical work is not used as proof.

## Novelty and citation gate

- [x] Original source and exact candidate are cited and transcribed correctly.
- [x] Later versions, corrections, citing work, and nearby work were searched.
- [x] The single citation exists and supports each nearby attribution.
- [x] Metadata was checked against primary/formal records.
- [x] BibTeX audit has no missing or unused entries.
- [x] Novelty wording is database- and date-bounded; no absolute priority claim.

## Reproducibility gate

- [x] Stable paths and fast/full commands are documented.
- [x] Exact verification uses no random seed or floating point.
- [x] Environment and tool versions are recorded.
- [x] A clean LaTeX build succeeds without stale artifacts.
- [x] The release manifest binds statement, code, certificates, source, ZIP, and PDF.
- [x] The source ZIP is built from `release/SOURCE_FILELIST.txt`, contains no
      `__pycache__`, `*.pyc`, virtual-environment, `.lake`, or temporary entries,
      and passes `unzip -t`.
- [x] Two independent certificate verifiers and the breaker verifier pass from
      a fresh ZIP extraction under `python3 -I`.
- [x] LaTeX audit and a warning-free three-page build pass from the same clean
      extraction; extracted-build PDF text matches the released PDF text.
- [x] No formalization claim is made.

## Manuscript gate

- [x] Title and abstract state the exact result and limitation.
- [x] Prior work, new result, and unresolved universal question are separated.
- [x] Notation and dimensions are consistent.
- [x] Decisive rational data and the proof appear in the paper.
- [x] Computational and AI assistance is disclosed.
- [x] Author metadata was preserved from the pre-existing project scaffold; the author should recheck it before external submission.
- [x] Final source has no undefined references/citations or warnings.

## PDF and handoff gate

- [x] Every rendered page was inspected.
- [x] PDF layout and metadata pass; hash, size, and page count are recorded.
- [x] Terminal status is `DISPROVED`, explicitly limited to candidate nonexpressibility.
- [x] Proof-assistant use is disclosed as none.
- [x] Test, build, citation, proof, novelty, and PDF audits are included.

The bundle is technically release-ready for the stated theorem. Actual
journal submission remains an author decision and should begin with a final
human check of author/affiliation metadata and journal-specific formatting.
