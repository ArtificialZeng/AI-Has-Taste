# PDF audit

Status: **passed**, 2026-08-30.

Final artifact:
`output/pdf/cyclic-315-packing-M12.pdf`

SHA-256:
`1f72dfdde2bf58cc3c77795510056a563d35816fa152ab722211c4c09db37426`

## Build checks

- `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` completed
  successfully after the final bibliography normalization.
- The final log scan found no undefined citations/references, missing BibTeX
  entries, repeated entries, LaTeX errors, overfull boxes, or underfull boxes.
- The BibTeX key audit reports 4 cited keys, 4 database keys, no missing keys,
  no unused keys, and exact agreement with the `.aux` file.
- `pdfinfo` reports a five-page, unencrypted letter-size PDF with no forms or
  JavaScript.

## Metadata and identity checks

- Title: `The Largest Cyclic 3-(31,5,1) Packing Has Twelve Base-Block Orbits`.
- Author: `Zijian Zeng`.
- Subject contains the authorized affiliation and both authorized email
  addresses.
- Extracted body text and the rendered final page contain:
  `Institute of Computer Science and Digital Innovation, UCSI University,
  Kuala Lumpur, 56000, MALAYSIA`, `zijianzeng@foxmail.com`, and
  `1002266693@ucsiuniversity.edu.my`.
- No additional author is named.

## Every-page visual inspection

The final PDF was rendered at 150 dpi with Poppler and all five current page
PNGs were inspected at original image detail.

1. Page 1: title, author, abstract, theorem, equations, and footer are centered
   and legible; no clipping or collision.
2. Page 2: orbit equations, 12-block array, proof, and section transition are
   aligned; no overflow.
3. Page 3: leave equations and exact-enumerator lemma are complete; the proof
   and proposition break cleanly.
4. Page 4: proposition proof, SHA-256 table, command block, and audit paragraph
   are readable; long hashes wrap within the table and no rule/text collision
   occurs.
5. Page 5: disclosure, bibliography, affiliation, and two emails are complete,
   correctly spaced, and unclipped.

## Source archive

`output/source/cyclic-315-packing-M12-source.zip` has SHA-256
`e1aba6aec4ddf17311ed15f1e78032b2729e64721f6b09e275ffabd40a2ac311`.
It contains exactly `main.tex`, `references.bib`, `main.bbl`, and `README.md`.

Verdict: the final PDF and compact source archive pass the publication artifact
gate.
