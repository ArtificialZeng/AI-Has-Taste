# Build audit

Accepted.  From `manuscript/`, `latexmk -C main.tex` removed prior derived
outputs and `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
completed through BibTeX and a converged second PDF pass.  The final PDF has
four letter-size pages and extractable text.

The final `.log` and `.blg` contain no undefined citation or reference,
database miss, duplicate entry, LaTeX or package warning, fatal error, overfull
box, or underfull box.  The independent Bib-key checker reports four cited
keys, four database keys, and identical source/aux citation sets.  All fonts
are embedded and mapped to Unicode.

PDF metadata now explicitly records the manuscript title, Xiaojian Zeng as
author, the Lonely Runner subject, and exact-certificate keywords.  The creator
is LaTeX with hyperref and the producer is pdfTeX.
