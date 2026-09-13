# Fresh rendered-page visual audit

Date: 2026-09-08. Job: bigMac-00014-p04-release-05b975bda9df.
Verdict: accept. All four current PDF pages were rendered at 130 DPI with `pdftoppm -r 130 -png manuscript/main.pdf audit/rendered/page` and each PNG was actually opened with the image-viewing tool. Text extraction was supplementary, not the visual audit.

| Page | Inspected image | Actual observations |
| --- | --- | --- |
| 1 | audit/rendered/page-1.png | Two-line title, author, affiliation and email fit; abstract and Section 1 have consistent spacing. Boolean-lattice superscript, set-inclusion sign, summation, relative-frequency formula and Theorem 1 are sharp. Footer 1 is clear; no overlap or clipping. |
| 2 | audit/rendered/page-2.png | All eight element encodings and all three PLE lines are within the margins. Coverage lemma and nested summation display are legible. Weight definitions and heavy orientations fit; footer 2 is separate. Section 3 continues naturally on the next page. |
| 3 | audit/rendered/page-3.png | Fractions, binomial coefficients, q bound, cycle and equation (1) render correctly. The two proof cases and proof of Theorem 1 are complete, with visible proof-end symbols. Literature paragraphs and both reference numbers fit before footer 3. |
| 4 | audit/rendered/page-4.png | Size/count table has labels 1..8 and exactly 8,37,114,240,348,336,192,48. All values match the replay. The command line fits within the page width. AI disclosure and both bibliography entries are readable, including Polish/German accents and the wrapped arXiv URL. DOI is intact. Footer 4 is visible. |

No clipping, collisions, illegible symbols, broken reference placeholders, missing table cells, or substantive presentation defects were observed. The final page has ordinary spare whitespace after the references. There are no external data plots or images requiring a data-source audit. All fonts are embedded as corroborated by audit/pdffonts.txt. Images and PDF digest are bound in audit/visual.json.
