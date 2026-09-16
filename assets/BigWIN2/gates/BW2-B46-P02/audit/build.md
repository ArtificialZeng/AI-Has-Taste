# Build audit

Accepted.  From `manuscript/`, `latexmk -C main.tex` removed prior derived
outputs and `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
completed successfully through BibTeX and the converged second PDF pass.  The
final PDF has four letter-size pages and extractable text.  The final `.log`
and `.blg` contain no undefined citation/reference, database miss, duplicate
entry, LaTeX error, fatal error, overfull box, or underfull box.  The independent
Bib-key checker reports four cited keys, four database keys, and identical
source/aux citation sets.

PDF metadata was checked after adding explicit title, author, subject, and
keywords; the creator is LaTeX with hyperref and the producer is pdfTeX.
