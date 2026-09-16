# Build audit

From a cleaned generated-file state, `latexmk -pdf
-interaction=nonstopmode -halt-on-error main.tex` converged successfully with
BibTeX and produced a five-page PDF.  The rebuilt PDF was refrozen through the
manuscript gate before the release audits were bound to it.

The final log contains no undefined citations or references, BibTeX database
failures, repeated entries, LaTeX errors, fatal errors, emergency stops,
undefined control sequences, runaway arguments, overfull or underfull boxes,
or rerun warnings.  The bibliography checker reports three cited keys, three
BibTeX keys, and three matching AUX entries with no missing or unused entry.
All PDF fonts are embedded and subsetted; `pdfinfo` recognizes an unencrypted,
extractable, letter-size PDF with five pages.  The solver-free exact
certificate verifier also replayed successfully.
