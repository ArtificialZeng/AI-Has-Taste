# Build audit

The final manuscript was rebuilt from a cleaned auxiliary state with

```text
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

from `manuscript/`. BibTeX and the required subsequent pdfLaTeX pass completed successfully. The converged log is `manuscript/main.log`, SHA-256 `09f5d98ba4f3233b74c419eb6fc3a2671fc560830718418cd258b9d73ee278a7`. The final PDF SHA-256 is `6afdd98b484b01f18d8adf90c479ffb422b6b6c643eeba4a9d924e0ff7c5536a`.

The final log and `.blg` contain no undefined citations, undefined cross-references, missing database entries, duplicate BibTeX entries, `Warning--` records, LaTeX errors, fatal errors, emergency stops, undefined control sequences, or runaway arguments. `check_bib_keys.py` reports exactly two cited keys and two bibliography keys, with no missing, unused, or `.aux`-inconsistent key.

`pdfinfo` reports a valid unencrypted four-page letter-size PDF with extractable text and the intended title, author, and subject metadata. `pdffonts` reports all fonts embedded and subsetted. The build audit accepts the final snapshot.
