# Rendered-page visual audit

**Verdict:** accept  
**PDF:** `manuscript/main.pdf`  
**Release job:** `win-00069-p01-release-f4ce9d811492`  
**Pages inspected:** 1, 2, 3, 4, 5

For attempt 3, every page of the refrozen PDF was freshly rendered at 150 dpi
with `pdftoppm` into a temporary directory and individually inspected at original
image detail, not merely through extracted text.  The current render was copied
to `audit/rendered-pages/` after inspection.

| Page | Content inspected | Result |
|---:|---|---|
| 1 | Title block, author/affiliation, abstract, introduction, start of definitions | Clean margins and baseline spacing; title, formulas, sign pattern, and citations are legible; no clipping or overlap |
| 2 | Coefficient formulas, semigroup display, theorem, support lemma | Displayed sums/products and cases fit the text block; theorem and equation labels are legible; no collision or cutoff |
| 3 | Proof reductions and start of Hilbert-basis certificate | Long formulas, proof boxes, citations, and prose render cleanly; no overfull visual defect |
| 4 | Degree table, exact-support certificate, theorem proof, reproducibility and disclosure | Table rules and all numerical values are legible; paths wrap within margins; no overlap or orphaned fragment |
| 5 | Complete bibliography | All seven entries, DOI/arXiv URLs, accents, labels, and line wraps are legible and inside margins |

The five pages use consistent typography and numbering.  There are no figures
or graphical data displays requiring value-by-value source comparison.  No
clipped text, overlapping elements, illegible symbol, blank page, malformed
URL, or visually missing reference was found.
