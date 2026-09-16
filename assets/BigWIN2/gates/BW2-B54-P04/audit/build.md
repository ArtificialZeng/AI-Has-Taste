# Clean build audit

Verdict: **accept**.

On 2026-09-07 the manuscript was cleaned and rebuilt with `latexmk -C main.tex`
followed by two invocations of
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`. The converged
build succeeded and the second invocation reported all targets up to date.

The final PDF has three unrotated US-letter pages, SHA-256
`de65a14bd1509405bf3200188ddeef492a981cf18b5391cb533afbe003fe52f5`,
title *A Roman-Domination Bound for the Graph Burning Number*, and author
Xiaojian Zeng. `audit/build.log` is the final converged TeX log.

The bibliography checker found four cited keys and four BibTeX entries with no
missing, unused, or AUX-inconsistent key. The final log scan found no undefined
citation/reference, missing database entry, repeated entry, BibTeX warning,
LaTeX error, fatal error, emergency stop, undefined control sequence, runaway
argument, or overfull box. Cross-references and the bibliography resolve.
