# Rendered-page visual audit

Release job: `bigMac-00003-p01-release-288b9c70330b`.  Audit date:
2026-09-06.  Current PDF SHA-256:
`3cfe689095e44a9b1e0d5193fbedc15b900446887c5d524b4ff9553126952b0a`.
All three pages were freshly rendered from this PDF at 160 dpi and individually
inspected at original rendered resolution.  The page list reviewed was exactly
`[1, 2, 3]`.

| Page | Render | Pixel-file SHA-256 | Result |
|---:|---|---|---|
| 1 | `audit/rendered/page-1.png` | `3d3c71b0fc9f6f678cd64429109d8e6d0884b204a378e7143fe566331c5794d7` | Title, author block, abstract, context, definitions, and theorem are fully visible; no clipping, overlap, crowded margin, or illegible math. |
| 2 | `audit/rendered/page-2.png` | `b06afc76b38716078c8650d7d5fac38d04f54e379e747f2a821bbb67928cf4c9` | All lattice sums, equation tags, prose, and cross-reference links are aligned and legible; no clipping or collision. |
| 3 | `audit/rendered/page-3.png` | `d5c0fe9f091186aa1d5866f2d398d887ef9aa6fb7026eb747862698bd4eb0e98` | Equality proof, assistance disclosure, and both bibliography entries are fully legible; the long SSRN URL wraps safely inside the text block. |

There are no figures, charts, tables, or raster data graphics requiring a
separate value-by-value visual-data audit.  Page numbering is consecutive and
all content stays within the physical page bounds.  The long SSRN hyperlink
wraps safely without entering the margin, and no mathematical symbol is
missing or visually ambiguous.  Overall visual verdict: pass.
