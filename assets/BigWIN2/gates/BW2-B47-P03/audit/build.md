# Build audit

Accepted.  From `manuscript/`, `latexmk -C main.tex` removed the prior derived
outputs and `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
completed successfully through BibTeX and the converged PDF pass.  The final PDF
has four letter-size pages and extractable text.

The final `.log` and `.blg` contain no undefined citation/reference, missing
database entry, repeated entry, BibTeX warning, LaTeX error, fatal error,
overfull box or underfull box.  The independent Bib-key checker reports four
cited keys, four database keys and identical source/aux citation sets.  All 16
fonts reported by `pdffonts` are embedded and have Unicode mappings.

PDF title, author, subject and keywords are populated and match the manuscript.
The release-hook user-bibliography validator also accepted the canonical
manuscript and bibliography layout with the issued attempt identity.

