# Checkpoint — release audit ready

## Accepted scope

The accepted `result-note` proves the $d=4$ Hypercube Inequality for every
$x\in\mathbb R_{\ge0}^{16}$ with $|\operatorname{supp}x|\le5$, with equality
in this restricted domain exactly when the support is contained in a cube
facet. Supports of size at least six and the original universal HC4 remain
unresolved. The accepted evidence snapshot is
`b42d07e55381f1aed86686332fad090211b685092fa115590503ef0c9cb29a06`.

## Fresh release evidence

- Explicit advisory `$citation-check-skill` two-pass review is recorded in
  `audit/citations.md`. All three references and nearby claims were checked
  against official pages and the user-designated workbook record; the two
  workbook papers are used only as relevant methodological comparisons. All
  citation keys resolve and the declared source dependency scope is complete.
- A fresh full `latexmk` rebuild succeeded. `manuscript/main.log` has SHA-256
  `bf61186bc860d81b863fce890226a653ffaa24dca317a670628bf24831641342`;
  the final build has no unresolved citation/reference, compiler failure,
  overfull box, or BibTeX warning. The informational longtable page-split
  diagnostic was visually checked and has no rendered defect.
- Every page of the four-page PDF was rendered at 180 dpi and inspected;
  observations are in `audit/visual.md`, with retained images in
  `audit/rendered-pages/`. No clipping, overlap, missing glyph, illegible
  equation/table/reference, or unintended blank page was found. All fonts
  are embedded and PDF title/author metadata are correct.
- The exact verifier was rerun successfully: 4,368 supports, 27 orbits, 17
  independent orbits, and zero negative coefficients.
- Current manuscript digest:
  `6a27a105cfe15d18e8a5d983daf40f7a0172efee30eab0bd76d80aa3c249e61f`.
  Current PDF digest:
  `dbb918ed658ee709bf1cb4f431f80e5cf699aafe2619a8a2b113aee247f80fe5`.
- `release_gate.py check` passes with four pages and all fresh audit bindings
  under job `bigMac-00022-p03-release-c6aa32d34094`.
- `source.md` remains unchanged at SHA-256
  `68215e4f5db3f2e45b59e4565f391a19bd6956fe740e2cd2400cf38fce32aeb7`.

## Obstacles and limitations

No release blocker remains. Citation and build success do not extend the
accepted mathematical scope or establish priority, journal acceptance, or
peer review. Local publication activation is reserved for the supervisor.

## One next test

The supervisor should run `release_gate.py publish` and verify that the active
`release/main.pdf` and manifest retain PDF digest
`dbb918ed658ee709bf1cb4f431f80e5cf699aafe2619a8a2b113aee247f80fe5`.
