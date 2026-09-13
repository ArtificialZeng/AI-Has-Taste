# Fresh build audit

Audit date: 2026-09-09.  I inspected the existing nonempty compiler log
`manuscript/main.log` (SHA-256
`3268adf87473c8de382727804e60d5bf1310e8b31dace4c9cad861b13d564587`),
the BibTeX log, auxiliary/reference files, PDF structure, extracted text, font
inventory, and the frozen source/PDF digests.

The recorded command is
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` in
`manuscript/`.  The log ends with a successful `pdfTeX` write of
`main.pdf`, 5 pages and 333175 bytes.  It contains no compilation failure,
undefined citation or reference, multiply defined label, overfull/underfull
box, or rerun-required diagnostic.  `main.blg` reports `warning$ -- 0`.
All five citation keys have matching `\bibcite` records, and all numbered
equations, theorem references, and section references are resolved.

`pdfinfo` recognizes a valid, unencrypted five-page letter-size PDF 1.7;
`pdftotext` extracts the complete nonempty manuscript.  `pdffonts` reports all
22 fonts embedded, subsetted, and Unicode-mapped.  A nonfatal Poppler font-type
diagnostic was checked against the font inventory and rendered pages and has
no missing-glyph or readability consequence.  PDF title/author metadata fields
are blank rather than contradictory; the visible title and author block are
correct, and creator/producer metadata identifies LaTeX/pdfTeX.

The exact-arithmetic certificate was rerun with
`/Users/mac/4prove-or-disprove-math/.research-venv/bin/python` and reproduced
all stated rational identities, cross-product signs, the second-iterate bound,
and the capture-threshold signs.  This is a reproducibility check, not a
substitute for the accepted mathematical proof.

The current PDF digest is
`411261c85eb5ff25765d14dcdfdf65ccfc68a9987620f5e6dd7aff59b0679e0f`,
and all source hashes match `audit/manuscript-snapshot.json`.  Verdict: accept;
the existing build is clean and provenance-consistent.
