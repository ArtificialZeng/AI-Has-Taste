# PDF audit

Status: **PASS**  
Date: 2026-08-30  
Artifact checked: `paper/main.pdf`  
SHA-256: `183ff0236e53de460de80a9c97ace776aba06eb681bd79315ab344827a55d7eb`

## Build and structure

- Two independent clean `latexmk` builds converged from no auxiliary files.
- With `SOURCE_DATE_EPOCH=1788048000`, both builds produced the identical
  8-page PDF hash above.
- Final PDF metadata: title correct; author exactly `Zijian Zeng`; no
  encryption, JavaScript, forms, or suspect objects.
- All 24 listed font subsets are embedded.
- Final `main.log` and `main.blg` contain no undefined citation/reference,
  missing BibTeX database entry, repeated entry, LaTeX error, fatal stop,
  undefined control sequence, runaway argument, multiply defined label,
  overfull box, or underfull box.
- Citation reconciliation is 5 cited keys = 5 database keys = 5 auxiliary
  `bibcite` keys, with zero missing or unused keys.

## Pagewise visual inspection

All pages were rendered to PNG at 144 dpi and inspected individually.

| page | checked content | result |
|---:|---|---|
| 1 | title, sole author, abstract, introduction, date/keywords footer | PASS |
| 2 | citation wording, main theorem, truncated-power formula | PASS |
| 3 | global polynomial, critical equations, six chamber list | PASS |
| 4 | full-support theorem, empty and star1 derivation | PASS |
| 5 | star2/star3/star4/triangle arguments and displayed equations | PASS |
| 6 | Hessian signs, support strata, corrected (a^3(a-1)^2) Q3 equation | PASS |
| 7 | (d_3,d_4,d_5) endpoints, one-row-per-endpoint certificate table, disclosure | PASS |
| 8 | data/code statement, exactly five references, affiliation and two emails | PASS |

No page has clipping, overlap, illegible type, broken glyphs, bad line wraps,
misplaced floats, anomalous margins, or unintended blank pages.
