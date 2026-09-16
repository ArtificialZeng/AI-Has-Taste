# Build audit

Verdict: **accept**.

The canonical command `cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` was run after `latexmk -C main.tex`, rebuilding the PDF, auxiliary files, BibTeX output, and final converged log from the current sources. The final PDF has four letter-size pages. `pdfinfo` reports the expected title and author metadata, no encryption, and PDF 1.5. `pdffonts` reports every listed font embedded and subsetted with Unicode mapping.

Final `manuscript/main.log` SHA-256: `303506f4d3cc99f2567245801e0f0f28027b611a5048bba9b7f47c82d40f0378`.

The final citation checker reports five cited keys, five BibTeX keys, no missing or unused entries, and exact `.aux` agreement. Scans of `main.log` and `main.blg` found no undefined citations or references, missing database entries, BibTeX warnings, repeated entries, LaTeX errors, fatal errors, emergency stops, undefined control sequences, or runaway arguments.
