# Build audit

**Verdict: accept.**  From `manuscript/`, `latexmk -C main.tex` followed by `latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex` converged successfully on 2026-09-06. The result is seven pages with PDF SHA-256 `25271cf7d915839c3df296f3ff745f3b8ff459764983fa4d89ac63f370bd4d48`.

The final LOG/BLG scan found no undefined citations or references, missing database entries, repeated entries, BibTeX warnings, LaTeX errors, fatal stops, runaway arguments, or overfull/underfull boxes. The bibliography checker reported nine cited keys, nine BibTeX keys, no unused or missing entries, and exact AUX agreement. `pdffonts` reports every font embedded. `pdfinfo` reports seven letter-size unrotated pages and the intended title, author, subject, and keywords.
