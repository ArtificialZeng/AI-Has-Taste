# Clean-build audit

On 2026-09-07, `latexmk -C main.tex` followed by `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` completed successfully in `manuscript/`. BibTeX and all required LaTeX reruns converged. The final PDF has four letter-size pages.

The final `main.log` and `main.blg` contain no undefined citation/reference, missing database entry, repeated entry, LaTeX error, fatal error, emergency stop, undefined control sequence, runaway argument, overfull box, underfull box, or BibTeX warning. The bibliography checker reported 8 cited keys, 8 BibTeX keys, no missing/unused keys, and exact AUX agreement. `pdfinfo` reports four unencrypted letter-size pages and the intended title, author, subject, and keywords; every listed font is embedded.

Final PDF SHA-256: `d948e7890369db2f1d73ae94e379c0de14b949466ccc0c2066d0f0c4f9eeedd3`.
