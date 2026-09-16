# PDF audit

Status: PASS for the journal-neutral publication artifact.

Audit date: 2026-08-29.

## Mechanical checks

- Artifact: `output/pdf/10_crim_odd_rank.pdf`.
- Pages: 6; page size: US letter; encryption: none.
- Title metadata: *A Boundary-Word Classification of Losing Positions in
  CRIM*; author metadata: `Zijian Zeng`.
- File size: 333020 bytes.
- SHA-256:
  `0f18d1d9c65bcbd71082658d0568c0e9462d2e3d4421924def8f88e5716567d4`.
- Final `latexmk` build completed successfully.  The final log contains no
  `Warning`, `Overfull`, `Underfull`, `undefined`, or `Error` match.
- PDF text extraction contains Theorem 1.1, Corollary 1.2, the references
  heading, and the arXiv identifier.

## Visual page review

All six final pages were rendered at 150 dpi to `tmp/pdfs/` and inspected at
original rendered resolution.  No clipping, overlap, black block, missing
glyph, malformed formula, placeholder, blank page, or unreadable table was
found.  Headers, page numbers, section transitions, the proof table,
bibliography, affiliation, and both email addresses were checked.

`pdftotext` confirms that the PDF contains no SHA-256/hash text, anonymous
placeholder, internal role or route identifier, completion/confidence field,
funding placeholder, or acknowledgment placeholder.  It contains the supplied
affiliation and both supplied email addresses.

## Scope qualification

The PDF is a complete journal-neutral `amsart` manuscript by Zijian Zeng.  It
is not claimed to follow an unspecified journal's house style, and no claim of
external peer review, journal acceptance, funding, or acknowledgment is made.
