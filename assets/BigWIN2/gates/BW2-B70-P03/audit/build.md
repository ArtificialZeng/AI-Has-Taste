# Clean build audit

Release job: `win-00070-p03-release-f068e3c4ff94`  
Snapshot digest: `1cbfb3e8b6067c7adb8ebefab8352dc54203e27db8fad03a3b3f7b00393c8a2c`  
Manuscript digest: `958b2475c656fe84a6e44c214f3cf055df822d64317ed4a39a961e2963bc340b`  
PDF digest: `a876798d41a8d6fdae05279cf2446ffed848c2009e8fce796db542425f70af63`  
Result: PASS

The auxiliary products were cleaned and the canonical source was rebuilt from
the manuscript directory with pdfLaTeX, BibTeX, and the converging pdfLaTeX
pass.  The exact publication command was then replayed from the project root
and returned successfully with all targets current:

`latexmk -cd -pdf -interaction=nonstopmode -halt-on-error manuscript/main.tex`

The final `main.log` (SHA-256
`39dc6f5cb8ff43a2fc79b5d016da7929a8a17c40824cb40424f43ff63e10e414`)
and `main.blg` contain no undefined citations or
cross-references, missing database entries, BibTeX warnings, repeated entries,
LaTeX errors, fatal errors, emergency stops, undefined control sequences, or
runaway arguments.  The bibliography checker found 5 cited keys, 5 database
keys, and 5 `.aux` bibcite keys, with all three sets equal and no unused entry.
The PDF has 5 letter-size pages, is unencrypted, and all 20 reported fonts are
embedded and subsetted with Unicode maps.  Its pdfTeX producer metadata is
consistent and contains no misleading title or author data.
