# PDF audit

Audit date: 2026-08-22.

Artifact: `output/pdf/one_sided_parity_es7_sat_encoding.pdf`

## Structural checks

- Thirteen letter-size pages; no encryption, forms, JavaScript, or suspicious
  objects reported by Poppler.
- All 23 listed fonts are embedded and subsetted.
- Full layout-preserving text extraction succeeded (5,340 words).
- Metadata title and four authors agree with the manuscript source.
- No SHA-256 string, release digest, checksum, watermark, or hexadecimal-style
  release identifier appears in the extracted paper text.

## Visual checks

All thirteen pages were rendered to PNG at 130 dpi and inspected individually.
The title page, theorem statements, displayed equations, count table,
bibliography, benchmark table, email addresses, and dual affiliation fit inside
the page bounds.  No clipping, overlap, missing glyph, blank page, or unreadable
reference was found.  Hyperlinked citation numbers are visually unobtrusive.

## Build-log checks

The converged `latexmk` run completed successfully.  The final `.log` and
`.blg` contain no undefined citations, missing bibliography records, duplicate
entries, overfull boxes, LaTeX errors, or fatal stops.  The key audit found 14
cited entries, 14 database entries, and complete agreement with the `.aux`
file.  One harmless underfull bibliography line was observed during
compilation; it does not affect the inspected layout.

Verdict: pass for the generic AMS submission layout.  A target venue may still
require its own class file and front-matter fields.
