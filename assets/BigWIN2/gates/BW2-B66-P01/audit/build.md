# Clean build audit

Release job `win-00066-p01-release-0d8daa2815b8` cleaned the prior LaTeX auxiliary outputs and invoked `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`. The first post-clean invocation produced an unconverged intermediate pass and was not accepted. The same canonical invocation then ran BibTeX and a further LaTeX pass to convergence; a final canonical invocation reported `main.pdf` up to date.

The final `manuscript/main.log` is bound by SHA-256 in `audit/build.json`. Its final state has no undefined citations or references, missing BibTeX database entries, duplicate entries, LaTeX errors, fatal errors, emergency stops, undefined control sequences, or runaway arguments. The separate bibliography-key checker reports four cited keys, four bibliography keys, no missing or unused entry, and exact agreement with `main.aux`.

Verdict: accept.
