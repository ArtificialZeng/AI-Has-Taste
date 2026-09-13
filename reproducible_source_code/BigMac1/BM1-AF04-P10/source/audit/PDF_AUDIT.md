# PDF audit

Status: **PASS**.

Audited file: `paper/main.pdf`

- SHA-256: `9427e0ec397d0b0ef2064e73c574951767799c0fb9d7a8ecabacadecd0a05eb4`
- Pages: 5
- Page size: US Letter, 612 by 792 points
- PDF version: 1.7
- Title metadata: `Certified radius-seven exchange rigidity for a binary subspace code`
- Author metadata: `Zijian Zeng`
- Subject metadata: `Exact finite certification for A2(7,4)`
- Encryption/JavaScript/forms: none

## Text and identity checks

`pdftotext` confirms the title, finite theorem, limitation, unique author,
affiliation, and both required email addresses.  The body contains no extra
author.  The exact affiliation is:

`Institute of Computer Science and Digital Innovation, UCSI University, Kuala Lumpur, 56000, MALAYSIA`

The emails are `zijianzeng@foxmail.com` and
`1002266693@ucsiuniversity.edu.my`.

## Page-by-page visual inspection

The final PDF was rendered with Poppler at 150 dpi.  Every page was inspected
at original rendered resolution.

| Page | Inspection result |
|---:|---|
| 1 | title, author, abstract, equation, citations, and foot matter are aligned; no clipping or overlap |
| 2 | orbit table, layer census, exchange definition, and normalization lemma are legible; proof box and displayed formulas are intact |
| 3 | objective, enumeration table, theorem, proof, and section transition fit within margins; all eight data columns are visible |
| 4 | independent verification, limitations, reproducibility commands, and bibliography items 1--4 are legible; monospaced commands do not overflow |
| 5 | bibliography item 5 and the `amsart` author address block are complete; remaining whitespace is intentional and contains no missing object |

No cropped glyphs, overlapping objects, broken equations, unreadable tables,
or raster artifacts were found.

## Build checks

The final build began from `latexmk -C` and completed with `latexmk -pdf
-interaction=nonstopmode -halt-on-error`.  The final log has no undefined
citations or references, no overfull/underfull box messages, and no BibTeX
warnings.  The citation checker reports five cited keys, five bibliography
entries, and zero missing, unused, or unresolved AUX keys.
