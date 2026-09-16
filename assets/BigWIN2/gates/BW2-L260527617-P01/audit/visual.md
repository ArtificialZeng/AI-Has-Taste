# Rendered-page visual audit

## Binding and verdict

- Release job: `lit-260527617-p01-release-4b162acd588d`
- Frozen mathematical snapshot: `95cd9fcb261ad6fe4df05945af76955e312cda7ba75fce350ac973bbca29f6cf`
- Manuscript digest: `9a63259426e3187bf462df2c2662be51389cb663c1ee497f22834586b3fec9b5`
- PDF digest: `b1523fd8749b16a0c9b2baee2c29b7251c8f6f9887af37614338aa38a6843646`

**Verdict: accept.** Every one of the six final PDF pages was rendered at 144
dpi and individually viewed at original resolution. No clipping, overlap,
missing glyph, illegible text, malformed formula/table, broken citation, or
page-order defect was found.

| Page | Content inspected | Finding |
|---|---|---|
| 1 | Title, abstract, definitions, projection conditions, Theorem 1 | Metadata and margins are balanced; symbols, citations, and theorem are complete |
| 2 | Scope paragraph, explicit word, residual table, count and cyclic lemmas | Long word and table fit; proof endings and superscripts are intact |
| 3 | Occurrence table, symmetry reduction, interval grammar, Lemma 5 | Table and half-open interval notation are clear; grammar display is aligned and unclipped |
| 4 | Grammar proof, certificate table, DRAT/RUP discussion | Dense table and prose remain readable; all columns and markers fit |
| 5 | Main proof, scope, next frontier, disclosure, references 1--2 | Bounds, seven length-20 patterns, disclosure, and references render cleanly |
| 6 | References 3--8 | Names, accents, mathematical italics, and titles are legible; trailing white space is clean |

The rendered evidence is `audit/rendered-pages/page-1.png` through
`page-6.png`. PDF text and metadata independently confirm six pages in the
expected order and no missing publication content.
