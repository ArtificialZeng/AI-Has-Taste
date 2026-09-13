# Checkpoint

- Immutable `source.md` remains SHA-256
  `62db45a34c5b7fcbc91aac4c9f4955563f752eebfc6f9969d4307d5e9230c9e4`.
- The frozen `resolution-paper` claim gives the all-fields counterexample
  `A=k x k[epsilon]/(epsilon^2)`, with `A_0=k x k`, `A_1=k epsilon`, and
  `J=k x 0`. The quotient has dimension 2, equal to `dim_k A_0`, while the
  natural map has nonzero kernel `J intersect A_0`. Thus the unrestricted
  original assertion is disproved; no minimality or priority claim is made.
- Fresh referee job `bigMac-00020-p01-referee-ceb7eb11c5a0` accepted evidence
  snapshot
  `3647bf565806d5d07c7d5aaeea1ea8148576e5430042ef81a177c2acfb6b78c6`.
- Release job `bigMac-00020-p01-release-80ff7c9383b6` inspected
  `literature/user_bibliography_check.md` and explicitly applied the advisory
  citation checker in two passes. The project has no Excel-derived list; its
  one user-designated relevant source is Darius Dramburg, *Isomorphisms of
  graded semiconnected algebras*, arXiv:2609.03288v1. The accessible local PDF
  matches the supplied SHA-256, and its primary text plus the official arXiv
  record verify the metadata, Definitions 1.1 and 4.1, Proposition 4.7, and
  Question 6.1. All rendered citation uses resolve and no citation limitation
  remains.
- Current manuscript digest is
  `488892484bc96d7b34bbff749318870b687f20d1f27eafaeeb7f79d6da6d1515`;
  current PDF digest is
  `367e110c905d90de5c2eb099cf1b67f3b2502ecd1643be94f530c6cd495f0542`.
  The complete authored dependency list is exactly `manuscript/main.tex` and
  `manuscript/references.bib`.
- The nonempty existing build log `manuscript/main.log` has SHA-256
  `4282196828d1be9e7c66403c69944fa6ccef1559084a05f9d695b663b4db137d`.
  A fresh `latexmk` state check reports all targets current. The log has no
  errors, undefined citations or references, box warnings, or BibTeX warnings;
  PDF text is extractable and every font is embedded.
- Both PDF pages were freshly rendered at 180 dpi and inspected directly at
  original image resolution. No clipping, overlap, illegible symbol, malformed
  bibliography, or other presentation defect was found.
- Fresh digest-bound release reports and JSON records are in
  `audit/citations.*`, `audit/build.*`, and `audit/visual.*`. The prior generated
  active release was invalidated because its audit provenance became stale;
  `manuscript/main.pdf` was preserved. The final `release_gate.py check` passed
  on the fresh state, reporting `resolution-paper`, original status `disproved`,
  two pages, and the current snapshot/manuscript/PDF digests above.
- Obstacles: none affecting mathematical scope, citation support, build
  integrity, provenance, or rendered-page readability.

Next test: the supervisor should run `release_gate.py publish` on this unchanged
state and verify that the new active manifest and PDF carry the current digests.
