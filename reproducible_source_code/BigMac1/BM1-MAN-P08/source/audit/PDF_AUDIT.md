# PDF audit

Audit date: 2026-08-22.  Final status: **PASS**.

## Released artifact

- Path: `output/pdf/integer_floor_lifting_union_closed.pdf`
- Title: *Integer-Floor Lifting for Frankl-Complete Uniform Configurations*
- Author metadata: Zijian Zeng
- Pages: 6
- Page size: 612 by 792 points (US Letter)
- File size: 338,837 bytes
- SHA-256 (release-record metadata only, not printed in the PDF):
  `e22bc052d7c361a41acdb9169b64a719f804a3db909262d46ced7813154af67d`

The released file was compared byte-for-byte with `paper/main.pdf`.

## Build and textual checks

- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` completed
  successfully.
- The final `.log` and `.blg` contain no undefined citation, missing database
  entry, repeated-entry, LaTeX error, fatal error, overfull-box, or
  underfull-box finding.
- The bibliography checker reports five cited keys, five bibliography
  entries, no missing key, no unused key, and an auxiliary-file match.
- PDF title and author metadata match the manuscript.
- Extracted PDF text contains no SHA-256 label or long hexadecimal hash-like
  string.  The release hash above is intentionally kept outside the paper.

## Visual inspection

The final PDF was rendered to one PNG per page with the PDF skill's Poppler
workflow.  All six current pages were inspected after the last source change.
The title block, displayed equations, theorem environments, comparison table,
bibliography, email addresses, page breaks, hyperlinks, and disclosure text
are legible.  No clipping, overlap, missing glyph, malformed table, or stray
artifact was found.
