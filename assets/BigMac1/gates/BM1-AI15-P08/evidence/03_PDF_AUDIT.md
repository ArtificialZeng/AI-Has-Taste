# Final PDF audit

Audit date: 2026-08-29 (Asia/Shanghai)

## Verdict

**PASS.**  The retained manuscript PDF was produced from the final audited
LaTeX source after a clean converged build.  It has eight US-letter pages.
Every page was rendered at 144 dpi and inspected individually.  No clipping,
overlap, missing glyph, leaked placeholder, broken formula, malformed
reference, or unreadable text was found.  The natural white space following
the bibliography on page 8 is intentional and not a layout defect.

## Retained artifact

```text
path: output/pdf/sheil_small_low_degree_covering.pdf
pages: 8
size: 352871 bytes
SHA-256: f5e502d6f122d8720a5871e6b435429102b9ca75eb2c58fa266f2da129be7260
title: The Sheil-Small covering problem for self-inversive polynomials in degrees two and three
author: Zijian Zeng
producer: pdfTeX-1.40.29
PDF version: 1.7
```

## Reproduction and inspection

```bash
cd paper
latexmk -C -outdir=../tmp/pdfs/build main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=../tmp/pdfs/build main.tex
cd ..
pdftoppm -png -r 144 tmp/pdfs/build/main.pdf \
  tmp/pdfs/final-render/page
pdfinfo tmp/pdfs/build/main.pdf
```

The converged `main.log` and `main.blg` were scanned after this build and had
no LaTeX/package warning, undefined citation/reference, BibTeX warning,
overfull/underfull box, or fatal error.  The citation-key checker reported
five cited keys, five bibliography keys, and five auxiliary-file keys, with
no missing or unused key.

## Page-by-page result

| Page | Result | Notes |
|---:|---|---|
| 1 | PASS | Title, abstract, definitions, metadata, and first display are clear. |
| 2 | PASS | Main theorem and residual strata are legible and correctly scoped. |
| 3 | PASS | Boundary/Schur lemmas and quadratic proof have no layout defect. |
| 4 | PASS | Cubic normal form and displayed inequalities are intact. |
| 5 | PASS | Cubic conclusion and quartic reduction are intact. |
| 6 | PASS | Quartic/quintic puncture arguments are intact. |
| 7 | PASS | Sparse subclass, verification scope, and disclosures are clear. |
| 8 | PASS | Package statement, five references, affiliation, and email are clear. |

Only the retained PDF above is a release artifact.  Temporary build and page
rendering files are not part of the release package.
