# PDF audit, editorial round 2

Status: **passed** on 2026-08-22.

- Final artifact: `output/pdf/lehmer_totient_exact_prime_set_exclusion.pdf`.
- Build: converged `latexmk`/BibTeX build; eight letter-size pages and eleven
  bibliography items.
- Cross-references: all eleven citation keys occur in the auxiliary and
  bibliography outputs; no undefined citation or reference remains.
- Log review: no LaTeX error, BibTeX warning, overfull box, or underfull box.
  BibTeX's `duplicate$` and `missing$` lines are function-call statistics,
  not data warnings.  The sole pdfTeX font-expansion notice is non-actionable
  and produced no visible defect.
- Metadata: title and author are correct; the PDF is unencrypted and contains
  no forms, JavaScript, embedded raster images, or suspicious objects.
- Visual inspection: all eight pages were rendered at 150 dpi and inspected
  at original detail.  The title, abstract, equations, table, theorem
  environments, code path, references, address, and both email addresses are
  legible and inside the margins.  No clipping, overlap, broken glyph,
  orphaned heading, or unintended blank page was found.
- Text extraction confirms the open-problem disclaimer, the finite
  \(P^+(n)\ge349\) theorem, and the 38-set modulo-3 explanation.  The PDF
  contains no SHA-style hash, checksum, source digest, PB completion claim,
  or solver-trace identifier.
