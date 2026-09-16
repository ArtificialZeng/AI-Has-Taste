# PDF and source-package audit

Date: 2026-08-29.  Status: **PASS**.

## Final PDF

- Path: `output/pdf/02_resoca115_odd.pdf`.
- Pages: 6, US letter, no rotation, no encryption.
- Size: 364,938 bytes.
- SHA-256: `12ead4441ca213eb0c88525815f3bcbae88b19c52ffd5522c013c44aa16cfdc0`.
- Metadata title: *Exact odd-parameter periods for reversible elementary
  second-order cellular automaton rule 115*.
- Metadata author: Zijian Zeng.
- All fonts reported by `pdffonts` are embedded; Unicode extraction is
  available.

The final `latexmk` build completed without errors, undefined
references/citations, substantive package warnings, or overfull/underfull
boxes.

## Page-by-page rendering

`pdftoppm -png -r 180` rendered all six pages under `tmp/pdfs/`.  Every page
was inspected at original rendered resolution.

| Page | Material inspected | Result |
|---:|---|---|
| 1 | title, author, abstract, main formula, introduction, date and footer | PASS |
| 2 | rule table, definitions, equations (2.1)--(2.7), running header | PASS |
| 3 | exterior proof conclusion, reduced-word tree, Proposition 3.1 | PASS |
| 4 | local toggle identity, contour lemma and proof, vertex count | PASS |
| 5 | exact-period theorem and proof, computational verification | PASS |
| 6 | reproducibility/assistance disclosure, reference, affiliation, both emails | PASS |

No clipping, overlap, black square, missing glyph, broken equation, unreadable
table, placeholder, or abnormal final-page whitespace was found.  Headers,
footers, page numbers, section transitions, theorem styling, and references
are consistent.

## Extracted-text hygiene

`pdftotext -layout` recovered all six pages.  A case-insensitive check found
the confirmed author, affiliation, UCSI University, and both email addresses.
It found no SHA-256 label, hash/digest string, anonymous or placeholder
identity, internal role or route identifier, completion/confidence field,
funding statement, or acknowledgment statement.

## LaTeX ZIP

- Path: `output/latex/02_resoca115_odd_latex.zip`.
- Size: 22,889 bytes.
- SHA-256: `ad9b3d4848a88022a44b2c3753c518b9f32591a5b5b376b409bc16ae730fbe7d`.

`unzip -l` lists the manuscript, bibliography, README, formal statement,
serialized certificate, verifier, two tree implementations, and two orbit
simulators.  `unzip -t` passed.  After extraction, byte comparisons of the
manuscript and bibliography passed, the exact verifier returned `PASS`, and a
fresh `latexmk` build completed with a clean final log.
