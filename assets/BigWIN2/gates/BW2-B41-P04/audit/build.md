# Build audit

## Verdict

**Accept.** The canonical command

`cd manuscript && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`

converged successfully after a clean auxiliary-file removal and a final
bibliography-only rebuild. The final PDF has four US-letter pages, extractable
text, and the configured title, author, and subject metadata.

The final `manuscript/main.log` SHA-256 is
`b77bb580c3722ad483fbc155067f507f9867d397696f97effccd97be75ac94ea`.
Scanning `main.log` and `main.blg` found no undefined citations or references,
missing database entries, repeated entries, BibTeX warnings, LaTeX errors,
fatal errors, emergency stops, undefined control sequences, or runaway
arguments.

The bibliography consistency checker found four cited keys, four BibTeX keys,
no missing or unused entries, and exact `.aux` agreement.
