# Rendered-page visual audit

The current PDF (SHA-256
`474f76ce0f5c756936656289753da6304b59e3704ca685da7457b553f1b96fde`)
was rendered with Poppler at 160 dpi.  I visually inspected each rendered page
at original image resolution, exactly once:

| Page | Material inspected | Observation |
|---|---|---|
| 1 | Title, author block, abstract, citations, convention, and Theorem 1 | All text and displayed mathematics are sharp and within the margins.  The theorem continues cleanly and the page number is visible. |
| 2 | Complete double-coset proof, numbered equation, subgroup table, and start of the cycle-index section | No clipping, overlap, crowding, broken table rule, or illegible symbol.  Equation number and subscripts/superscripts are clear. |
| 3 | Coefficient matrix, determinant, cycle-index identities, assistance disclosure, and both references | Matrix and fractions are legible; bibliography wraps cleanly; no content is clipped or orphaned. |

There are no figures or charts requiring a value-by-value visual-source check.
Page size and orientation are consistent, whitespace is balanced, page numbers
are present, and the two-page transition points do not omit text.  Fonts are
embedded and the PDF has nonempty extractable text.

Verdict: **accept**.  Pages reviewed: 1, 2, 3.
