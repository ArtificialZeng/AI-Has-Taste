# Clean build audit

The manuscript build tree was cleaned with latexmk -C and rebuilt with
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex.  After the
scope-preserving PDF-metadata and citation-wording corrections, latexmk was
rerun to convergence from that clean build tree.  BibTeX and all required
pdflatex passes completed successfully.

The final manuscript/main.log is nonempty and bound by SHA-256
c85f5fabf60ef3a2d4f16d71fc351da173613290b272609bf134472e2321dea1.
Targeted scans of main.log and main.blg found no undefined citations or
references, missing database entries, duplicate entries, BibTeX warnings,
LaTeX errors, fatal errors, emergency stops, undefined control sequences, or
runaway arguments.  The read-only bibliography checker found three cited keys,
three matching bibliography and aux keys, and no unused entries.

The output is a valid three-page PDF.  pdfinfo reports US Letter pages, PDF
version 1.5, the manuscript title, and Xiaojian Zeng as author.  Build status:
PASS.
