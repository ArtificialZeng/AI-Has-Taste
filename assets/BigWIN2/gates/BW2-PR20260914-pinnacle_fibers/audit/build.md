# Build audit

**Verdict: accept.** Release job:
`primary-20260914-pinnacle-fibers-release-9c1ceac429e4`.
UTC date: 2026-09-14.

The active selection parser rejects `xurl` and requires exactly
`\bibliography{references}`. The two setup declarations were corrected;
mathematical prose, tables and all five BibTeX entries were preserved.
Compilation now runs from the `manuscript` directory. The initial mechanical
checker's duplicated `manuscript/manuscript` path is therefore also resolved.

A clean build was actually run, with commands and exit codes retained in
`release-build-commands.json`. First, `latexmk -C -outdir=build main.tex`
removed generated outputs. The old generated `build/main.bbl` was explicitly
removed before the next step, so the database was read afresh. Then:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
```

Both commands exited zero. `release-clean.log` and
`release-build-driver.log` retain the real output. The multipass driver
contains expected transient first-pass undefined-reference diagnostics;
they are absent from the final compiler log bound by `build.json`.

I inspected `manuscript/build/main.log`, `main.blg` and `main.bbl`.
There are no fatal errors, unresolved references/citations, duplicate or
missing bibliography entries, overfull boxes, underfull boxes, or final
LaTeX/BibTeX warnings. `warning$ -- 0` is a BibTeX function-call counter,
and `infwarerr` is a loaded package name; neither is a diagnostic.

`check_bib_keys.py manuscript/main.tex --aux manuscript/build/main.aux`
exits zero with five matching source/database/auxiliary keys and no unused
entry (`release-bib-keys.txt`). The recorder and bibliography log confirm
the three declared publication sources, generated auxiliaries and system
TeX dependencies (`release-dependencies.json`). No authored dependency is
omitted.

`pdfinfo` confirms an unencrypted, text-bearing three-page letter-size PDF
with the intended title and author (`release-pdfinfo.txt`). `pdffonts` shows
13 embedded, subsetted Latin Modern font resources with Unicode mappings
(`release-fonts.txt`). `release-extracted.txt` contains nonempty layout-aware
text with the expected theorem, tables, equation references and bibliography.
All three pages were separately rendered and visually inspected.

The post-build `freeze-manuscript` command succeeded (`release-freeze.json`).
`build.json` binds the current research snapshot, manuscript, PDF and final
compiler-log bytes. The original source, checkpoint, claim, decisive
evidence and accepted mathematical audit remain unchanged.
