# Rendered-page visual audit

Job: `win-00064-p02-release-0573327856cc`

The final PDF digest is
`1ee9e9baeed42b40221b37c89ad7dd98c600c565be0fe7833f7c265acedc617b`.
`pdfinfo` reports exactly three letter-size pages.  Every page was rendered at
144 dpi to the following evidence and inspected at readable resolution:

| Page | Render evidence | SHA-256 | Inspection |
|---|---|---|---|
| 1 | `audit/rendered-pages/page-1.png` | `939c5c88c47c8934d34b38189d612a0c54e8e1f2314a58ea9de179dac315be83` | Title, author, abstract, equations (1)--(2), citations, and page number are sharp and within margins. |
| 2 | `audit/rendered-pages/page-2.png` | `4b6e61a3771eef01cac3d9b560fb95df07a27341cbf0822cdad162542f4375cd` | Theorem, numbered items, tensor reduction, displayed equations, proof text, and page number are legible with no collision or clipping. |
| 3 | `audit/rendered-pages/page-3.png` | `ca739fbe97e70613bfe02d806cb0c0e876e85b64d9b3a6b251ed9fa10bb042dc` | Proof conclusion, disclosure, all four references, wrapped URLs, and page number are legible and within margins. |

There are no figures or tables requiring data-point verification.  No text or
formula is clipped, overlapped, occluded, too small to read, or rendered with a
missing glyph.  Page breaks are coherent.  The title and author are present in
both the rendered first page and the PDF metadata.  The authored theorem and
abstract match the accepted claim without strengthening it.

**Verdict: accept.**
