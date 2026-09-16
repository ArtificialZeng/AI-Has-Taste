# Rendered-page visual audit

Release job: `win-00085-p01-release-dc2c5030af7e`

The current PDF (SHA-256
`befe85db1e0a1a7d9ece21c75daeee9d6508c59f2c1eacaf25e31d324af2c943`)
was rasterized with `pdftoppm -png -r 150`.  I opened and visually inspected
each rendered page, in order, exactly once for this audit.

| Page | Content checked | Result |
|---|---|---|
| 1 | Title/author metadata, abstract, context, generators, permutation convention | Clear and fully inside margins; equations and citations legible. |
| 2 | Main theorem, prior-invariant attribution, both lemmas and proofs | No clipping, overlap, broken symbols, or unresolved reference marks. |
| 3 | Complete signed Pauli/support longtable | All 32 rows, signs, subscripts, headers, and bottom rule are visible and legible. |
| 4 | Complete rank profiles, proof of the theorem, start of verification section, replay commands | Lists and displays are aligned; proof endings and commands are visible; no footer collision. |
| 5 | Method citation, scope/disclosure, and all four bibliography entries | Text and identifiers are legible; references fit within the page and margins. |

Across pages 1--5, page numbering is correct and there are no blank pages,
cropped lines, overlapping objects, illegible fonts, missing glyphs, distorted
tables, or misleading figures.  The document contains no charts or graphical
data requiring value-by-value visual-source comparison.

Verdict: **ACCEPT**.
