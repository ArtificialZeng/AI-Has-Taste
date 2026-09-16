# Build audit

After cleaning generated LaTeX artifacts, `latexmk -pdf
-interaction=nonstopmode -halt-on-error main.tex` converged successfully.
BibTeX processed the canonical `references.bib`; the final log contains no
undefined citations or references, BibTeX database failures, repeated entries,
LaTeX errors, fatal errors, emergency stops, undefined control sequences, or
runaway arguments.

The bibliography checker reports four cited keys, four bibliography keys, and
four matching AUX entries, with no missing or unused entries.  `pdfinfo`
recognizes a valid three-page letter-size PDF with extractable text.
