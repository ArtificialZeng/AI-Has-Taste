# Checkpoint — release audit

## Accepted result and preserved scope

The mathematical gate passes for the accepted `resolution-paper` claim. The
result is only that no four-layer balanced directed Hamilton cycle exists in
`C_4(3)=Cay(Z_12,{1,2,3})`; therefore the original request with the additional
three development-colour conditions has a negative answer. Nothing is claimed
for any other `r congruent to 3 (mod 4)`, and no priority claim is made.

## Manuscript and build evidence

- `manuscript/main.tex` is a concise self-contained article with the exact
  accepted theorem, the orbit-choice bijection, the `6^4` permutation
  reduction, all 15 degree-survivor cycle decompositions, a compact replay
  program, the original-path corollary, limitations, and an accurate
  computational/AI-assistance disclosure.
- `manuscript/references.bib` cites the genuinely relevant user-cited primary
  paper by Jiang and Yang only for definitions and the neighboring construction
  boundary actually inspected.
- `manuscript/main.pdf` clean-builds with the recorded `latexmk` command. The
  final log has no warnings, undefined references, overfull boxes, or errors.
  The PDF has four nonempty text-extractable pages; every page was rendered and
  visually inspected with no clipping, overlap, or broken table/code layout.
- `publication.json` lists every TeX/BibTeX input and the draft PDF path.
- The immutable `source.md` remains at SHA-256
  `ea3d097839f8cdfdfcd8a59c1df8afb91c7c37250f6bef314a0a0f9eda58ff4f`.

## Replayed decisive evidence

A fresh run with the required research interpreter made
`evidence/crosscheck.py` pass again: 531441 balanced selections, 1296 with
outdegree one, 15 with both degrees one, and zero Hamilton cycles. The survivors
split as twelve of type `6+6` and three of type `4+8`. The independent
`audit/referee_recompute.py` replayed the reduced `6^4` domain and returned the
same survivor digest and histogram.

## Fresh release evidence

- A citation-check advisory two-pass audit fixed 23 manuscript claims before
  verification. All external attributions were checked against the official
  arXiv record and the local 23-page primary PDF. Definitions 2.1, Proposition
  2.2, Lemma 2.3, Theorem 4.7, and Section 9 support the four nearby citation
  uses at their exact scope. `literature/user_bibliography_check.md` remains
  absent; this was not treated as reference nonexistence. The one genuinely
  relevant user-cited primary paper is present in the PDF.
- Fresh exact runs of `evidence/crosscheck.py` and
  `audit/referee_recompute.py` again returned 531441 balanced selections, 1296
  outdegree-one selections, 15 degree survivors, cycle histogram `6+6:12`,
  `4+8:3`, and zero Hamilton cycles.
- A full cleanup and rebuild completed successfully. Final PDF SHA-256 is
  `c75ffad4013ac083705fe012b4fe30361eebae03896bb57206471489954bb020`;
  final build-log SHA-256 is
  `ace0c8e41e3b63aed9ab3909be6766da64398f51c6b1fb874828cf9a2d143db8`.
  The log has no errors, unresolved citations/references, warnings, or box
  problems, and all fonts are embedded.
- Every page 1--4 was rendered at 150 dpi and visually inspected. There is no
  clipping, overlap, illegible mathematics/code/table content, or broken
  bibliography layout. The current manuscript snapshot binds the unchanged
  source inputs to the rebuilt PDF.
- `release_gate.py check` passes for the current snapshot, all three fresh
  release audits, build log, and four-page PDF.
- `source.md` remains immutable at SHA-256
  `ea3d097839f8cdfdfcd8a59c1df8afb91c7c37250f6bef314a0a0f9eda58ff4f`.

No release-audit obstacle remains.

## One next test

Have the supervisor run `release_gate.py publish`, then verify that the active
manifest binds `release/main.pdf` to PDF digest
`c75ffad4013ac083705fe012b4fe30361eebae03896bb57206471489954bb020`.
