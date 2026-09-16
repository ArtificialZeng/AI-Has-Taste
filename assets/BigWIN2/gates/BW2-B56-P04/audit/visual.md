# Fresh rendered-page audit

The five pages of `manuscript/main.pdf` were rendered independently to PNG at
144 dpi and each rendered page was inspected at original resolution.  The audit
is bound to PDF SHA-256
`0fa9bf6381c47f17b4ce7fc472f9ca5b4070beac99e2ad8bc8d8d9683836f1cf`.

| Page | Material inspected | Result |
|---|---|---|
| 1 | Title, author/affiliation, abstract, context, citations 1--3, Theorem 1 | Clear and complete; no clipping, overlap, broken glyph, or margin loss. |
| 2 | Component graph, Lemma 2 proof, assignment bullets, equation (3) | Clear and complete; mathematical symbols and proof-end marker render correctly. |
| 3 | Both antichain checks, cardinality equations, Corollary 3 and induction start | Clear and complete; links, equations, subscripts, and page break are legible. |
| 4 | Induction end, three-chain counterexample, exact-audit counts, citation 4, limitations | Clear and complete; long integers and scope limitations are legible and not clipped. |
| 5 | Assistance disclosure and all four bibliography entries | Clear and complete; accents, italics, page ranges, and line wrapping are legible. |

The PDF contains no charts, tables of data, figures, or external bitmap graphics
requiring value-by-value visual source comparison.  Page geometry, fonts,
mathematical symbols, hyperlink coloring, references, and page numbers are
consistent.  The intentionally short final page has ample whitespace but no
layout defect.

Verdict: **accept**; pages reviewed exactly once: 1, 2, 3, 4, 5.
