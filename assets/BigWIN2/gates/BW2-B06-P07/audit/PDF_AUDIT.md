# PDF and archive audit

Date: 2026-08-30 UTC

Status: PASS.

## Build

- The first authoring compilation exposed an escaped-inline-math source
  defect and did not produce a deliverable.  The source was reconstructed and
  the final `latexmk` build completed normally.
- The final log contains no LaTeX/package warnings, undefined references,
  overfull boxes, or underfull boxes.
- PDF metadata gives the requested author, the full paper title, eight pages,
  letter page size, and no encryption.
- Extracted text contains no unresolved markers, hash strings, internal route
  or role identifiers, completion/confidence fields, or internal audit prose.

## Visual inspection

- All eight pages were rasterized at 150 dpi after the final bibliography
  update.
- The contact sheet and every individual page were inspected at original
  detail.
- No clipping, overlap, broken glyph, illegible formula, table overflow,
  orphaned heading, or excess blank page was found.
- Title, abstract, theorem statements, proofs, the order-15 table,
  references, affiliation, and both email addresses are legible.
- A final root-level proofread removed the duplicated comma that the
  `amsart` address formatter inserted at the manual line break; the corrected
  PDF and archive were rebuilt and reinspected before release.

## Independent archive build

- `output/starlike_trees_multiset_dimension_latex.zip` was extracted into a
  fresh directory and built from source with
  `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
- The independent result is an eight-page PDF with no final warnings.
- From the extracted archive, `tests/test_exact_evaluators.py` passed and the
  fail-closed comparison of the split discovery reports against the
  independent report again passed for 13,188 trees through order 15.

Decision: the PDF and LaTeX archive satisfy the final artifact gates.

## Continuation preservation check

No manuscript endpoint strictly stronger than the accepted starlike theorem
passed the paper gate in the continuation round.  The PDF and LaTeX ZIP were
therefore neither regenerated nor modified.  Their pre-continuation hashes
were verified before the final manifest refresh, so the previous clean build
and page-by-page inspection remain the applicable PDF audit.
