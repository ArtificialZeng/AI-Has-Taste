# PDF audit

Status: **PASS**, 2026-08-29.

The journal-neutral `amsart` manuscript was built with pdfTeX and BibTeX and
released as `output/pdf/04_geometric_maxcut_n7.pdf`.

## Build and metadata

- Final page count: 5.
- Final file size: 336,622 bytes.
- PDF title: *The Continuous n=7 Case of Geometrically Weighted Lexicographic Max-Cut*.
- PDF author: Zijian Zeng.
- Page size: US letter; PDF version 1.5; unencrypted; no JavaScript.
- PDF SHA-256: `190a3c3b73ad7272002f1a3c9ea51e8475f6c795b03886683cdd63744554d470`.
- The final LaTeX and BibTeX logs contain no warnings, undefined references,
  overfull boxes, or underfull boxes.

## Page-by-page visual inspection

The final PDF was rendered in full at 150 dpi with `pdftoppm`. Every rendered
page was inspected at original detail.

- Page 1: title, author, abstract, introduction, and metadata footnote are
  complete and unclipped.
- Page 2: definitions, displayed equations, and the comparison lemma are
  aligned and legible.
- Page 3: exact rational evaluations, theorem statement, and the first part of
  the certificate table fit without collision or clipping.
- Page 4: certificate verification, proof, limitations, and data-availability
  text are complete and correctly separated.
- Page 5: verifier command, computational disclosure, bibliography, affiliation,
  and both email addresses are legible. The remaining lower-page whitespace is
  ordinary short-final-page whitespace.

No cropping, overlap, black rectangle, missing glyph, broken table, placeholder,
or bad page number was observed.

## Extracted-text inspection

`pdftotext -layout` confirmed the exact author name, affiliation, both supplied
email addresses, and the arXiv identifier. A case-insensitive scan found no
SHA-256 label, hash label, placeholder author data, task-completion or confidence
score, internal route or role identifier, internal audit wording, fabricated
funding or acknowledgments, or OpenAI/Codex name in the PDF text.

