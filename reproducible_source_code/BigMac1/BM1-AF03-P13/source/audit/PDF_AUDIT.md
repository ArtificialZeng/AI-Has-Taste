# PDF audit

Audit date: 2026-08-29 (Asia/Shanghai).

## Artifact identity

- File: `paper/main.pdf`
- SHA-256: `97bc0949eca16e0225e89b21ec451b5de92df66878900d4fcd24000e05bf0b55`
- Pages: 6
- Page size: US Letter, 612 by 792 points
- PDF version: 1.7
- Title metadata: *Exact counterexamples to an Ehrhart root-disk conjecture
  for generalized snake posets*
- Author metadata: Zijian Zeng

## Clean build and structural checks

The same final path was rebuilt from a clean LaTeX state; no intermediate PDF
version was retained.  `latexmk` completed successfully.  The final log has no
LaTeX warning, undefined citation/reference, overfull box, underfull box,
fatal error, or BibTeX warning.  The skill LaTeX audit reports
`cited=3 bib=3 missing=0 unused=0`.  `pdfinfo` reports an unencrypted six-page
document without forms or JavaScript.  Text extraction confirms the title,
author, required affiliation, both required email addresses, frozen Routh
verifier hash, and proof-assistant disclosure.

## Page-by-page visual inspection

The final PDF was rendered with

```text
pdftoppm -png -r 160 paper/main.pdf tmp/pdfs/final/page
```

and every rendered page was inspected at original image detail.

| Page | Content checked | Result |
|---:|---|---|
| 1 | title, author, abstract, source repair, theorem opening | PASS |
| 2 | theorem endpoint, definitions, radial lemma | PASS |
| 3 | length-10 h-star, factorization, Rouché certificate | PASS |
| 4 | independently certified length-9 result, verification opening | PASS |
| 5 | Cayley/Routh table, all reproduction commands and hashes | PASS |
| 6 | exact-scan scope, novelty limits, AI/formal-method disclosure, references, affiliation and emails | PASS |

No text, formula, link, page number, running head, or footer is clipped.  No
objects overlap.  Long exact integers and command lines remain inside the text
block and are legible.  Mathematical notation and accented names render
correctly.

`PDF_AUDIT = PASS`.
