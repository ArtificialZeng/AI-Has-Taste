# PDF audit

Status: not yet run.
# PDF audit

Artifact: `output/pdf/perfect_cuboid_lenhart_sieve.pdf`

## Mechanical checks

- Six letter-size pages, no encryption, forms, JavaScript, or suspicious PDF
  objects reported by `pdfinfo`.
- Final `latexmk` build completed with `-halt-on-error`.
- Final LaTeX/BibTeX logs contain no undefined citations or references,
  missing database entries, duplicate entries, overfull or underfull boxes,
  fatal errors, or emergency stops.
- Extracted text contains no placeholders and none of the forbidden digest-like
  labels requested by the author.
- PDF metadata title and author agree with the manuscript.

## Visual checks

All six pages were rendered at 150 dpi and inspected.  The review found:

- no clipped, overlapping, or missing text;
- no broken glyphs in equations, names, accents, or email addresses;
- the modulus-169 table fits the text block and follows its theorem proof;
- all three long residue lists remain inside the margins;
- DOI, arXiv, and web links wrap legibly in the bibliography;
- running heads, page numbers, section breaks, final affiliation, and both
  email addresses are aligned and readable.

Result: pass.
