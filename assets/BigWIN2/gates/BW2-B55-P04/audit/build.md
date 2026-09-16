# Build audit

Verdict: **accept**.  From `manuscript/`, a clean build was run with
`latexmk -C` followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.  After the
metadata-only repair, `latexmk` was run again and converged successfully.

The final `manuscript/main.log` is nonempty and contains no fatal error,
undefined citation/reference, emergency stop, or undefined-control-sequence
diagnostic.  `manuscript/main.blg` contains no missing database entry, duplicate
entry, or BibTeX warning.  The bibliography checker reports three cited keys,
three bibliography entries, no missing/unused keys, and exact agreement with
the final auxiliary file.  Cross-references and equation numbers (1)--(4)
resolve.  `pdfinfo` reports a valid three-page PDF with embedded title and
author metadata.

