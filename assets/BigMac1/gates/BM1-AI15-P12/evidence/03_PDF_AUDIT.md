# PDF audit

Date: 2026-08-29.  Status: **PASS**, including post-timeout clean rebuild and
second full-page inspection at 144 dpi.

`paper/main.pdf` was rendered at 144 dpi with Poppler and every page was
inspected at full-page scale.  The final artifact has six letter-sized pages,
no encryption, and no PDF parser suspects.

| Page | Visual check |
|---:|---|
| 1 | Title, author block, abstract, theorem opening, and display formulas are complete and aligned. |
| 2 | Factorization/gauge discussion and both normal forms are legible; no collisions or clipped equations. |
| 3 | SOS identities and first equality analysis render correctly; matrix and bracket notation are intact. |
| 4 | Equality completion and binary-form reduction render without broken math or margin overflow. |
| 5 | Discriminant, repeated-root formula, and all four reproduction commands fit inside the text block. |
| 6 | Verification prose, disclosure, author address, and bibliography are complete; whitespace is intentional. |

Post-render text extraction found none of the earlier literal-token defect
patterns (`qquad`, `undefined`, `Warning--`, `LaTeX Error`).  Final metadata:

```text
Pages: 6
Page size: 612 x 792 pts (letter)
File size: 368770 bytes
SHA-256: 7f89daee40e5dec6bd334b284af8bbb27f39c4a294c73a3a0e7d3b3bafff4f43
```

No clipping, overlap, missing glyph, blank page, or unreadable small text was
found.  The stable release copy is `output/pdf/rank2_marcus_n3.pdf`.
