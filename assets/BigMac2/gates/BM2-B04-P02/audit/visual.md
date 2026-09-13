# Fresh rendered-page visual audit

**Verdict:** ACCEPT

`manuscript/main.pdf` was rendered with Poppler at 160 dpi into four distinct
1360-by-1760 RGB PNGs.  I inspected every rendered page at original image
resolution, exactly once for the release decision.

| Page | Contents inspected | Result |
|---:|---|---|
| 1 | Title/author block, abstract, definitions, cited prior bounds, Theorem 1 | No clipping, overlap, malformed glyph, bad break, or margin violation. |
| 2 | Spectral decomposition, deletion proof, start of strict triangle lemma, equations (1)--(4) | Symbols and subscripts are legible; equation numbers and matrices are aligned; no defect. |
| 3 | End of triangle proof, main theorem proof, corollary, enumeration table and scope paragraph | QED marks, inequalities, table rules, headers, and all values are legible and aligned; no defect. |
| 4 | Reproducibility/AI disclosures and three bibliography entries | Text and references are complete, legible, and within margins; whitespace is intentional and unobjectionable. |

Rendered files and SHA-256 digests:

- `audit/rendered/page-1.png`: `0cf70128874143c58bfd9d2ceb4d5df363411484bedcbc6ad26e0a7378b6c855`
- `audit/rendered/page-2.png`: `1b0bd2c07e61666588f93f3e109f5cf3267b99c85a8f558acd59341a61e8106a`
- `audit/rendered/page-3.png`: `2c048faa424973de92264380018ca590ac3191b05612bff51c711165b5b23515`
- `audit/rendered/page-4.png`: `00a8bf2aaafea8e1c25cbae604b1165a7bdfc9c71b26661c3f09860e48557493`

The only data visual is the page-3 table.  Value-by-value comparison with
`evidence/enumeration_n4_n8.json` gives exact matches:

| Order | PDF: two-connected / noncycles / candidates | Source values | Status |
|---:|---:|---:|---|
| 4 | 3 / 2 / 0 | 3 / 2 / 0 | Verified |
| 5 | 10 / 9 / 0 | 10 / 9 / 0 | Verified |
| 6 | 56 / 55 / 0 | 56 / 55 / 0 | Verified |
| 7 | 468 / 467 / 0 | 468 / 467 / 0 | Verified |
| 8 | 7123 / 7122 / 0 | 7123 / 7122 / 0 | Verified |
| Total | 7660 / 7655 / 0 | 7660 / 7655 / 0 | Verified |

The table has no truncated axis, 3-D effect, hidden uncertainty, or other
visual distortion.
