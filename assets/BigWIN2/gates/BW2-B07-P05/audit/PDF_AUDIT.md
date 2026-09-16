# PDF and source-archive audit

Audit date: 2026-08-30 UTC.

## Final PDF

- Path: `output/pdf/Zeng_Heilbronn_Square_10_Full_Parameter_Family.pdf`
- SHA-256: `a20a1cdbae41f5f6d3f2511e2f02a46acbc7dfdd5ed931ca01a2bb262f53d437`
- Size: 354,817 bytes.
- Format: PDF 1.5, letter size, six pages, unencrypted.
- Metadata title: `Exact Optimization of the Comellas--Yebra
  Three-Parameter Family for Ten Points in the Square`.
- Metadata author: `Zijian Zeng`.

The final PDF was produced by `latexmk` from an empty temporary output
directory. The terminal build log has no undefined citation or reference, no
LaTeX or package warning, and no overfull or underfull box. A `pdftotext` scan
found none of the forbidden release-body fields: hashes, internal route/role
identifiers, completion/confidence fields, or internal audit wording.

## Page-by-page visual inspection

The final PDF was rendered at 150 dpi after the last source edit. Every latest
rendered page was inspected individually.

| Page | Inspection result |
|---|---|
| 1 | Title, author, abstract, first formulas, citations, footer, and margins are clear; no collision or clipping. |
| 2 | Main theorem and exact constants are readable; displays remain within margins. |
| 3 | Normalization and ordered-cell proof are clear; no broken symbols or overflow. |
| 4 | Proof continuation, product lemma, and certificate proposition are clear; page break is natural. |
| 5 | Certificate table, theorem conclusion, and reproduction commands are legible; no overlap. |
| 6 | Limitations, disclosure, references, affiliation, and both emails are complete and unclipped. |

Visual result: **PASS**; zero substantive defects found.

## LaTeX source archive

- Path: `output/latex/Zeng_Heilbronn_Square_10_LaTeX.zip`
- SHA-256: `4ce84474c7384e8a7ceeea29210a58be0f8f4432f7398d6d0d14234244f86fa5`
- Size: 38,483 bytes.
- Contents: manuscript source and bibliography, README, exact certificate
  data and programs, diagnostic experiment, literature log, proof notes, and
  the source/formal statements; no build artifacts.

`unzip -t` reports no compressed-data error. The staged archive contents were
built independently with `latexmk`; the terminal log has no warning or
unresolved reference. All four exact verification commands also return PASS
inside the staged archive.

PDF/source-archive gate: **PASS**.
