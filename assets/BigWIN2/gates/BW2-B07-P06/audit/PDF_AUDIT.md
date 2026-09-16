# PDF and source-archive audit

Status: **PASS**.

Audit date: 2026-08-30.

## Build

- Built from a fresh temporary directory with `latexmk`, BibTeX, and
  `pdflatex -halt-on-error`.
- Final log has no undefined citation/reference, warning, underfull box,
  overfull box, multiply-defined label, or error.
- PDF metadata has the correct title and author.
- Eight US-letter pages; no encryption, form fields, JavaScript, or rotation.
- All listed fonts are embedded and subsetted.

## Content and visual inspection

- Extracted text contains the open-status limitation, both finite totals,
  both included totals, bibliography, disclosure, affiliation, and emails.
- Extracted text contains no digest value, internal route/role identifier,
  completion/confidence field, or internal audit phrase.
- Every page was rendered at 144 dpi to 1224 by 1584 PNG.
- Pages 1--8 were inspected individually and in two four-page contact sheets.
- No clipping, overlap, broken glyph, black box, unreadable formula, table
  overflow, bad page break, missing header/footer, or reference defect was
  found.

## LaTeX ZIP

- Archive integrity test passes for all 45 entries.
- Root contains `main.tex`, `references.bib`, and build instructions.
- `ancillary/` contains source/formal statements, proof notes, exact code,
  fixed result JSON, environment pin, and reproduction instructions.
- Python caches, temporary files, build auxiliaries, audit files, role/route
  records, frozen literature PDFs, and digest values are excluded.
- The archive was extracted into a new directory and compiled from scratch;
  its final log is clean and its extracted PDF text is byte-identical to the
  delivered PDF text.
