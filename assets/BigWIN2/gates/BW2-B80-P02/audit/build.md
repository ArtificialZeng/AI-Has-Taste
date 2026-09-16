# Build audit

Release job `win-00080-p02-release-a55bfbfd3569` performed a fresh clean build from the canonical source set after the citation audit.

Clean-build command sequence:

```text
cd manuscript
latexmk -C main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

The sequence exited successfully and produced a six-page PDF. A scan of `main.log` and `main.blg` found no undefined citation/reference, missing BibTeX database entry, repeated entry, BibTeX warning, LaTeX error, fatal error, emergency stop, undefined control sequence, or runaway argument. The bibliography checker found exact TeX/BibTeX/AUX agreement (5 keys in each active set). The exact checker `python3 evidence/verify_cubic_rewrites.py` passed its stated cubic identities and finite congruence box.

`pdfinfo` reports the correct title, author Xiaojian Zeng, subject, keywords, six pages, letter size, and no encryption. `pdffonts` reports every listed font embedded and subsetted. The frozen publication-set digest is `6f1eb0591a56b9c880856c52737c918fb1bef8058abf8c0090a7aaa633a7c4ff`; the final PDF digest is `bb643283f21a8d2e5bacbfd4c69c37a2411503d9658bfc4df14808d2143e4801`.

Build status: **PASS**.
