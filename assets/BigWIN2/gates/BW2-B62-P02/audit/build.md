# Build audit

The refrozen manuscript was clean-built in `manuscript/` with:

`latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex`

The converged build exited successfully and produced a five-page PDF. BibTeX
ran against the canonical `references.bib`. The bibliography checker reported
three cited keys, three BibTeX keys, zero missing/unused keys, and exact AUX
agreement. A final scan of `main.log` and `main.blg` for undefined citations or
references, missing database entries, BibTeX warnings, repeated entries, LaTeX
errors, fatal stops, undefined controls, and runaway arguments returned no
matches. Cross-references to Theorem 1 and Table 1 resolve in the rendered PDF.

Toolchain: latexmk 4.76, pdfTeX 3.141592653-2.6-1.40.22, BibTeX 0.99d. The final
log SHA-256 is `edf30b07d2b4a9e5615bfe774bed10c1cd801f93f96b91e809940d838cbb0a60`.
