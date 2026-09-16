# Clean-build audit

Verdict: **accept**. Job:
`primary-20260914-q-product-unimodality-release-a0a2d6a0e9ce`.
The source was rebuilt from clean generated TeX state after the final
publication-only parser corrections, using these commands in `manuscript/`:

```sh
latexmk -C -outdir=build main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
```

Both commands completed successfully. `audit/release-clean.log` and
`audit/release-build-command.log` retain their outputs. The latter includes
normal first-pass unresolved references that disappear on convergence;
acceptance uses the actual final compiler and BibTeX logs, copied to
`audit/release-final-tex.log` and `audit/release-final-bibtex.log`.
Those final logs contain no warnings, unresolved references or citations,
database failures, duplicate entries, overfull/underfull boxes, or fatal errors.
The build JSON binds the final compiler log's actual SHA-256.

`python3 /home/ailab/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py
manuscript/main.tex --aux manuscript/build/main.aux` reports three cited keys,
three database keys, and three resolved auxiliary keys, with no missing or
unused entries (`audit/bib-key-check.txt`). BibTeX used only `references.bib`.
The source dependency inventory is complete and agrees with the `.fls` record;
see `audit/release-preflight.json`. No package installation was required.

`pdfinfo` reports a readable four-page, unencrypted PDF with the intended title
and author; `audit/release-pdfinfo.txt` retains the record. `pdftotext -layout`
produces nonempty text, with resolved numbered citations and equations.
Every font reported by `pdffonts` is embedded, subsetted, and Unicode mapped
(`audit/pdf-fonts.txt`). The current PDF's extracted text is byte-identical to
the writer's pre-correction extraction, confirming the changes' presentation
and syntax scope. The separate visual audit inspected all four rendered pages.

After this build, `release_gate.py freeze-manuscript` succeeded and generated
the current `audit/manuscript-snapshot.json`. No source or PDF edits followed.
The original mathematical acceptance and all 16 protected files remain current.
