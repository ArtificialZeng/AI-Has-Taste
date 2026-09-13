# Writing checkpoint

## Evidence

- The accepted mathematical scope is preserved verbatim in the central
  theorem: the four classes are `8K1`, `2C4`, `K4,4`, and `K2,2,2,2`, with
  reduced binary nullities `7,4,6,4`.
- `manuscript/article.tex` and `manuscript/references.bib` form a concise,
  self-contained resolution paper with explicit witnesses, the exact census
  and coverage argument, the reduced-adjacency criterion, limitations, and
  computational/AI assistance disclosure.
- `literature/user_bibliography_check.md` records direct read-only extraction
  of two genuinely relevant methodological comparisons from the
  user-designated workbook and limits their citation scope.
- `manuscript/article.pdf` clean-builds with the command recorded in
  `publication.json`; the final LaTeX and BibTeX logs have no warnings,
  unresolved citations, or overfull/underfull boxes.
- The clean four-page PDF has SHA-256
  `87a3e3ede7f75a83090e7ac6b3a3821eb2c247fb3da5ebe1c2140649b1da0616`.
  All fonts are embedded, text extraction is complete, and a four-page raster
  inspection found no clipping, overlap, or malformed table content.
- `release_gate.py freeze-manuscript` succeeded with manuscript digest
  `bf140f05a0f6d9615d29dbe5f74dd4cf350ed144117522d2a63ba7a1de0ed8ef`
  against accepted mathematical snapshot
  `122bf07d8f886c1f74935c676467e6459e53ab3ccbc0fe1a6c404086e9e6b093`.

## Obstacle

The root `checkpoint.md` is itself part of the accepted mathematical snapshot.
Changing it during writing would invalidate the accepted audit and make the
required manuscript-freeze gate fail. It is therefore preserved as decisive
evidence; this phase-specific checkpoint records the writing update instead.

## One next test

Run the separate citation/build/visual release review against
`audit/manuscript-snapshot.json`, checking every citation placement and all
four rendered pages before local release.
