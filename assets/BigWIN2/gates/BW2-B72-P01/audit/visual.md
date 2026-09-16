# Rendered-page visual and table audit

**Accept.**  After the final metadata-bearing build,
`manuscript/main.pdf` was freshly rendered page by page to PNG at 180 dpi.
Pages 1, 2, 3, and 4 were each inspected at original rendered resolution.

- Page 1: the title and author block, abstract, context citations, section
  headings, four displayed coefficient equations, equation numbers, and footer
  are sharp and fully inside the page; there is no clipping, collision, broken
  glyph, or margin overflow.
- Page 2: both signatures, the complete theorem and orbit display, signature
  lemma, composition count, exhaustive proposition, nested ranges, and footer
  are legible and correctly aligned.
- Page 3: Table 1, all prose, citations, bit-vector bounds, proof-ending marks,
  theorem proof, and the next section heading are legible.  The table float and
  whitespace are conventional and obscure no content.
- Page 4: reproducibility text, limitations, assistance disclosure, all three
  references, DOI/arXiv strings, and footer are fully visible with clean line
  wrapping.

The only data table was checked value by value against the frozen primary JSON
report:

| Visual row | Rendered values `(a,b,matches)` | Source values from `signature_join_61.json` | Status |
|---|---:|---:|---|
| sums 4--60 | `(487635,487635,0)` | `(521855-34220,521855-34220,4-4)` | Verified exact |
| sum 61 | `(34220,34220,4)` | final layer domain counts and match count `(34220,34220,4)` | Verified exact |
| sums 4--61 | `(521855,521855,4)` | aggregate counts and match count `(521855,521855,4)` | Verified exact |

There are no figures, charts, axes, legends, photographic elements, or visual
uncertainty marks.  All mathematical symbols, subscripts, superscripts,
inequality signs, table rules, citations, and page numbers render correctly.
No overlap, cropped content, illegible text, blank page, font substitution,
visual distortion, or misleading data presentation was found.
