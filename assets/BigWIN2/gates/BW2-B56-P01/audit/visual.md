# Rendered-page visual release audit

The bound PDF was rendered with `pdftoppm -png -r 150` and every page was
inspected at original rendered resolution. Pages reviewed exactly once: 1, 2,
3, 4, 5.

| Page | Content inspected | Result |
|---|---|---|
| 1 | title/author, abstract, definitions, contextual citations, Theorem 1.1 | clean; no clipping, overflow, overlap, broken symbols, or illegible text |
| 2 | Gram comparison, Section 2, optimization formulas (1)--(2), Lemma 2.1 and proof through (5) | clean; matrices, subscripts, absolute values, and equation numbers are legible |
| 3 | completion of cloning proof, Section 3, sign normalization and cell moment matrix | clean; displayed sums, norms, set notation, and proof-end marker render correctly |
| 4 | conic reduction (7), support reduction, conclusion, scope/assistance disclosure, reference [1] | clean; page transition into bibliography is natural and no citation text is cut off |
| 5 | references [2]--[8] | clean; author names, accents, journal titles, arXiv text, DOI, and page number are legible |

The document has no figures, charts, tables, color-dependent content, or
external bitmap assets. Fonts are embedded/rendered consistently. Margins are
ample; no content enters the crop boundary. Page numbering is continuous. The
PDF title metadata is blank but the visible title and author block are complete;
this is not a release defect for the present article build. No visual text
strengthens or contradicts the accepted claim.

Bindings: manuscript digest
`71c77700622ed5d01e9a1ae9c788c703cd36cf40f86845a79e9143f0780c6442`,
PDF digest
`52699207f152303b07fe9b202740581463652bd8bde38fe6a4172838d09373c2`.

Verdict: **accept**.
