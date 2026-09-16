# Clean build audit

Release job `win-00068-p04-release-8022f2ea8df8`. **PASS.**

The forced-clean command `cd manuscript && latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex` removed generated auxiliaries, ran BibTeX, and converged after the required PDFLaTeX reruns. `audit/build.log` is the converged final TeX log; it and `manuscript/main.blg` contain no undefined citation or reference, missing database entry, repeated entry, LaTeX/fatal error, runaway argument, undefined control sequence, or overfull/underfull box.

The bibliography checker resolved all seven ordinary body-flow keys, with no missing or unused BibTeX entries and exact agreement with `main.aux`. Both frozen exact SymPy scripts printed `PASS`. The six-page letter-size PDF has the requested title and author metadata, extractable text, and 15 embedded fonts with Unicode mappings.

Manuscript digest: `d1a03c75955f3aa01371c42b95585bab89bdf6bef16718050ecfc74d11ae1eb0`. PDF SHA-256: `3a72e85bd8acb27a4286cabcacc8af315a579c87a00e80f2bee2a00b0e88f6a8`.
