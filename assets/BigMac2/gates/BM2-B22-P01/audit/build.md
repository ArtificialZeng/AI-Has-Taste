# Fresh clean-build audit

Audit date: 2026-09-09. Release job:
`bigMac-00022-p01-release-c14619b2439d`.

I first ran `latexmk -C main.tex` in `manuscript/`, removing prior generated
intermediates, and then ran the publication command

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

from the same directory. The command exited zero. It ran pdfLaTeX, BibTeX, and
the required reruns; the final compiler transcript is
`manuscript/main.log`, SHA-256
`2bfb7cb03c8cae3e8d9e2978bd3dc90d77c617b2203b184fe5d2bef82ae99509`.

The final log and BibTeX log contain no compilation error, undefined citation,
undefined cross-reference, duplicate label, overfull/underfull box, or rerun
warning. The `.aux`, `.bbl`, and extracted PDF agree on all six citation keys.
The recorder shows that the only project-authored compilation inputs are the
two files declared in `publication.json`; all other inputs are system TeX
packages or generated intermediates.

`pdfinfo` reports a valid unencrypted six-page letter-size PDF with title
"The Sharp Queried-Gradient Constant of Nesterov's Fast Gradient Method at
Horizon Two" and author "Xiaojian Zeng". `pdftotext -layout` produced 19,728
bytes of nonempty text. `pdffonts` reports every listed font embedded and
subsetted. The rebuilt PDF SHA-256 is
`a94a4a29396791b6a8b98df1f5c9ffa4c4e3deaf7b0eb95eb8e75af85b47f422`.

Verdict: **accept**. The build is clean and reproducible from the declared
publication inputs.
