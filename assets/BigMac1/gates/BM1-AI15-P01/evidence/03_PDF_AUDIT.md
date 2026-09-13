# PDF audit

Audit date: 2026-08-29 (Asia/Shanghai). Status: **PASS**.

## Final artifact

- Path: `output/pdf/hadamard_rank22_rational_factorization.pdf`
- Pages: 3
- File size: 277,094 bytes
- SHA-256: `bd271cefe03202471b6b93fa8b7d9812e3da48cbc4bf7ec7bc1df23f8749d53a`
- Page size: US Letter, 612 by 792 points
- Producer: pdfTeX 1.40.29 (TeX Live 2026)

PDF metadata was checked with Poppler 26.04.0: the title matches the exact
matrix-specific result; author is `Zijian Zeng`; there is no encryption,
JavaScript, form, rotation, or suspect object.

## Clean build

The final source was built from a newly created empty temporary directory with
`latexmk -pdf -interaction=nonstopmode -halt-on-error`. The final TeX log has
no warnings, undefined references/citations, overfull or underfull boxes,
multiply defined labels, or errors. The citation audit reports
`cited=1 bib=1 missing=0 unused=0`.

Earlier failed/overfull builds are retained under `logs/` as negative audit
provenance; they are not the source of the released PDF.

## Page-by-page visual inspection

All pages were rendered with Poppler at 180 dpi and inspected at original
resolution.

1. Page 1: title, author, abstract, introductory matrix, theorem heading,
   date, and page number are aligned and legible.
2. Page 2: both exact factor matrices, fractions, row relations, proof square,
   parameter-family formulas, and continued proof are legible.
3. Page 3: continued proof, scope limitation, reproducibility and AI
   disclosure, bibliography, affiliation, email, running head, and page number
   are correctly placed; arXiv metadata is visible.

No clipping, overlap, missing glyphs, black boxes, broken links, margin
overflow, or unreadable elements were observed.

## Portability continuation

The source-archive repair did not edit `paper/main.tex`, `references.bib`, or
the released PDF.  A clean build from the corrected ZIP again produced three
pages with a warning-free final log, and its extracted text matched the
released PDF text exactly.  The PDF SHA-256 remains
`bd271cefe03202471b6b93fa8b7d9812e3da48cbc4bf7ec7bc1df23f8749d53a`;
therefore the page-by-page visual inspection above still applies to the exact
released bytes.
