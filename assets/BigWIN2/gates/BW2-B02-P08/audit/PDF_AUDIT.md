# PDF audit

Status: **PASS**. Stable final file:
`output/pdf/08_phylogenetic_delta4.pdf`.

- Build: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
- LaTeX log: no warnings, overfull/underfull boxes, or undefined references.
- Citation audit: 7 cited keys, 7 bibliography entries, none missing/unused.
- Metadata title: *A square-root obstruction to the k=4 phylogenetic-network
  enumeration conjecture*.
- Metadata author: `Zijian Zeng`.
- Pages: 7.
- File size: 375520 bytes.
- SHA-256: `e6d3423cd02ca03b35f692ece77f796455f11798b776daa7fa97761c74db6ec6`.
- Text audit: author, affiliation, and both email addresses are present; no
  manuscript hash, placeholder author data, internal route/role ID,
  completion/confidence field, or internal audit wording is present.

## Page-by-page visual review

| Page | Content checked | Result |
|---|---|---|
| 1 | Title, author, abstract, introduction, footnotes, equation (1) | PASS |
| 2 | Main and corrected theorems, polynomial displays, definitions | PASS |
| 3 | Component formula, recurrence, seed values, Cauchy inversion, \(N_4\) | PASS |
| 4 | Highest-exponent proof, star coefficient, basis obstruction | PASS |
| 5 | Tree-child formula, main contradiction, full Laurent EGF | PASS |
| 6 | Coefficient extraction, graph certificate, exact finite residual, commands | PASS |
| 7 | Continued command explanation, limitations/disclosure, all references, affiliation, and both emails | PASS |

No clipping, overlap, missing glyph, black box, placeholder, broken link
appearance, bad header, or abnormal final-page whitespace was found. The
stable final PDF was rendered with `pdftoppm` into `tmp/pdfs/`, and all seven
pages were inspected after the last source change.
