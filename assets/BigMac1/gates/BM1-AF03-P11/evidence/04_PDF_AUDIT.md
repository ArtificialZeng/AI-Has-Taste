# PDF audit

Audit date: 2026-08-29  
Status: **PASS**

The manuscript was built in a fresh temporary directory with `pdflatex`,
`bibtex`, and two final `pdflatex` passes. The final log contains no LaTeX
warning, undefined citation/reference, overfull box, underfull box, or error.

Poppler reports:

- title: *A Certified n=7 Case of a Generalized Stack-Sorting Enumeration
  Conjecture*;
- author: Zijian Zeng;
- 5 letter-size pages;
- no encryption, form, JavaScript, or suspect objects.

All five pages were rendered at 144 dpi and inspected at original detail.
The title block, theorem, displayed equations, Table 1, proof endings,
references, affiliation, emails, page numbers, running headers, and section
transitions are legible and aligned. No clipping, overlap, broken table,
missing glyph, or malformed hyperlink text was found.

The final PDF SHA-256 is
`76997d53c15fe7d7890f3e46a8276d3d5a00e5faf73ecb775d1ae8277f8ee17d`.
Its title and author metadata are correct, and all five final pages were
rendered at 144 dpi and inspected after the citation-wording correction.

The final source ZIP SHA-256 is
`8da2417940767f692f71e7cb8889413393c648c172e189b11f1e6c3731eadece`.
It was unpacked into a fresh temporary directory; its internal 15-file
manifest verified, and `pdflatex`, `bibtex`, and two final `pdflatex` passes
rebuilt a five-page PDF without errors. The outer two-file release manifest
also verifies.
