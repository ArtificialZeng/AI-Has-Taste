# PDF audit

Status: PASS.

- Final PDF: `paper/main.pdf`.
- Title metadata: `A Counterexample to the Positivity Conjecture for OEIS A071532`.
- Author metadata: `Xiaojian Zeng`.
- Pages: 2; final size after batch-level revision: 331543 bytes.
- Final log scan found no warnings, undefined references/citations, overfull or
  underfull boxes, or LaTeX errors.
- Both final pages were rendered again at 150 dpi to
  `audit/root_rendered_final/` and visually inspected. Equations, theorem,
  local trajectory table,
  bibliography, headers, author information, and final whitespace are clear;
  there is no clipping, overlap, missing glyph, black box, or broken layout.
- Text extraction confirms that the PDF contains no hash-algorithm labels,
  model/vendor names, prompt text, or placeholder tokens.
- A fresh temporary-directory ZIP extraction rebuilt the two-page PDF after
  the final source revision.
