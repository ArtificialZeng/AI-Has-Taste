# LaTeX audit

Date: 2026-08-29.  Status: **PASS**.

The post-timeout recovery audit repeated this clean build.  The skill's
required command
`python /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py paper/main.tex paper/references.bib --log paper/main.log`
exited zero and reported `cited=1 bib=1 missing=0 unused=0`.

The manuscript was rebuilt from a clean auxiliary state:

```bash
cd paper
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -silent main.tex
```

The build exited zero.  A strict scan of `main.log` and `main.blg` found no
undefined references/citations, BibTeX database failures, duplicate entries,
LaTeX errors, fatal stops, undefined control sequences, runaway arguments,
or overfull/underfull boxes.

`lacheck` exited zero.  ChkTeX's raw advisory output was manually triaged:
its warnings concerned conventional adjacent math atoms (for example
`u_i v_j`), use of `\bar i` as an index notation, and factorial punctuation.
They do not indicate malformed TeX or ambiguous rendered mathematics.  A
post-build PDF text scan and the full visual audit independently confirmed
the relevant output.

Final source hashes after verifier/reproduction disclosure was added:

```text
main.tex       b0fa15967cbf9c58def7173a9b4088919b6cd8571d36f6e0310b8463cf3795a7
references.bib 341394460190dd2f184a099c57b22fbcb51ec2dae96530764c93e0bdc2e19d3c
```
