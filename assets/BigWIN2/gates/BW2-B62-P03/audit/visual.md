# Rendered-page visual audit

The final `manuscript/main.pdf` was rendered at 144 dpi with `pdftoppm`, and every page was inspected as a raster image at original rendered resolution. The rendered evidence is retained in `audit/rendered/`.

| Page | Rendered evidence | Checks and result |
|---:|---|---|
| 1 | `audit/rendered/page-1.png` | Title/author block, abstract, definitions, theorem table, citations, and section transition are fully visible. No clipping, collision, bad wrapping, or margin overflow. |
| 2 | `audit/rendered/page-2.png` | Lemma and proof, construction formula, vertex/edge table, rooted histogram, and both ordered-pair histogram tables are legible; all columns and boundary rules remain inside the text block. No overlapping values or truncated symbols. |
| 3 | `audit/rendered/page-3.png` | Histogram conclusion, all nine hashes, replay command, scope/disclosure, and the first explicit path render cleanly. Monospace hashes and commands fit within the margins. Cross-references resolve visibly. |
| 4 | `audit/rendered/page-4.png` | All remaining explicit paths, arrow labels, endpoints, and both bibliography entries are readable. The arXiv and DOI URLs fit without clipping or collision. |

Additional checks: the document has four pages in natural order, consistent headers/footers and page numbers, embedded legible fonts, no figures requiring separate source validation, no rasterized mathematical text, no blank pages, no overprinted objects, and no visually misleading chart or axis. Hyperref link borders are visible but do not obscure any glyph. PDF metadata identifies the title, author, and mathematical subject.

Rendered SHA-256 values:

- page 1: `6e27d75f51b60cac9dc1037ad0c31c0ec83a991b1e3677c08fc8a2682903a884`
- page 2: `95fe76723814221680d54ee00ad7da74ac197f9a24d725635e024d865549d533`
- page 3: `6ee06aab8a2bf705725ebaa3b7a1770a74ee4d40471055e2a5170a16c6acfacc`
- page 4: `f96d941108373d26d45e96b08a626ab32883f43b0ff6c073e843287685923102`

Overall visual status: **accept**.
