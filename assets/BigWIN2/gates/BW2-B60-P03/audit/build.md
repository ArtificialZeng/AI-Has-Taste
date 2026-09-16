# Build audit: accept

The manuscript was cleaned with `latexmk -C main.tex` and rebuilt from
`manuscript/main.tex` with
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`. BibTeX and the
subsequent LaTeX passes converged successfully to a five-page A4 PDF.

The exact certificate verifier was replayed from the project root and exited
successfully with `exact checks passed`. The final `manuscript/main.log` has
SHA-256 `eb62186fa682a27dd8042478497793492a6a90f23737e3dd12d0a74445eb3028`.
The final log and `.blg` have no LaTeX error, fatal stop, undefined citation or
reference, missing database entry, repeated entry, overfull box, underfull box,
or warning. The bibliography checker found four cited and four database keys,
with exact final-`.aux` agreement.

`pdfinfo` reports five A4 pages, unencrypted PDF 1.5 output, TeX as creator,
and pdfTeX as producer. Its PDF Info Title is `Exact Solution and Optimal Face
of a Four-Dimensional Boolean-Quadric Semidefinite Relaxation` and its Author
is `Xiaojian Zeng`, matching the rendered title and author block.
`pdffonts` reports all sixteen used fonts embedded and subsetted with Unicode
mapping.

Verdict: **accept**.
