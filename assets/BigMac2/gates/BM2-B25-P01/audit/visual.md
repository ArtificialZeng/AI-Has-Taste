# Fresh rendered-page visual audit

The current four-page `manuscript/main.pdf` was rendered page by page at
150 dpi with Poppler and every PNG was inspected at original image resolution.
This was a visual review, not a text-extraction proxy.

| Page | Material reviewed | Observation |
|---:|---|---|
| 1 | Title/author block, abstract, context, theorem and corollary, opening orbit display | All text, subscripts, arrows, congruences, citations, and display mathematics are sharp and within margins; no clipping, collision, or orphaned heading. |
| 2 | Both lemmas and proofs, displayed successor equation, exact-count table, theorem proof | Equation number and proof-end marks are positioned correctly; table rules and all six count rows are legible; no overlap or overflow. |
| 3 | Corollary proof, assistance disclosure, all 15 survivor rows, beginning of verifier code | The longtable has clear columns and all rows/types are readable; monospaced code begins cleanly and remains inside the text block. |
| 4 | Remaining verifier code and bibliography | Indentation and symbols are legible, assertions are uncut, and the sole bibliography entry wraps cleanly.  The unused lower-page space is ordinary end-of-article whitespace, not missing or clipped content. |

Across pages 1--4, typography and line spacing are consistent, every page
number is present, fonts render correctly, and there are no figures whose
labels or data require separate review.  The visualized PDF is the one bound
to digest `c75ffad4013ac083705fe012b4fe30361eebae03896bb57206471489954bb020`.

**Verdict: accept.**

