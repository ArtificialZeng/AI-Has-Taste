# Submission audit (final)

Audit date: 2026-08-30 UTC.

## Mathematical gate

- [x] Formal theorem matches the final claimed family scope.
- [x] Hypotheses and the parameter cube appear in the first theorem.
- [x] Endpoints, repetitions, and degenerate parameter values are covered.
- [x] Equality parameters are classified.
- [x] Exact certificates are independently reproducible.
- [x] No fatal or major gap remains for the partial theorem.
- [x] Numerical search is labeled diagnostic and excluded from proof.

## Novelty and citation gate

- [x] Original construction and exact coordinates are cited.
- [x] Current adjacent global-optimization frontier was searched.
- [x] Every citation exists and supports its nearby claim.
- [x] Publisher/arXiv metadata was checked from primary records.
- [x] All four bibliography entries are cited; no key is missing.
- [x] Novelty wording is explicitly limited to the searches of 2026-08-30.

## Reproducibility gate

- [x] Stable commands and relative paths are stated.
- [x] Deterministic seed and environment versions are recorded where relevant.
- [x] Exact core checks are separate from floating-point diagnostics.
- [x] Clean exact checks and deterministic cover regeneration pass.
- [x] Release manifest was frozen after the final manuscript/PDF build and independently verified.
- [x] No proof-assistant claim is made.

## Manuscript gate

- [x] Title and abstract state the partial family result and limitation.
- [x] Prior work, new full-cube scope, and unrestricted gap are separated.
- [x] Notation and determinant/area factor-of-two conventions are consistent.
- [x] Human proof contains the decisive identities and certificate logic.
- [x] Computational and AI assistance is disclosed.
- [x] Author, affiliation, and both emails match the user's supplied metadata.
- [x] Journal-neutral AMS style is used because no target journal was named.
- [x] Static LaTeX citation audit passes with no missing/unused keys.

## Artifact gate

- [x] Final PDF was built from an empty temporary output directory.
- [x] The final six-page PDF was rendered after the last source edit and every page was visually inspected.
- [x] PDF text and metadata checks pass, including the prohibited-body-field scan.
- [x] The LaTeX ZIP contains no build artifacts, passes `unzip -t`, builds cleanly, and reproduces all exact checks.
- [x] `output/release_manifest.json` records the PDF and LaTeX ZIP and passes the independent manifest verifier.

Final submission gate: **PASS** for the explicitly scoped partial theorem.
The unrestricted value \(\Delta_{10}\) remains open and is not represented as
solved in any release artifact.
