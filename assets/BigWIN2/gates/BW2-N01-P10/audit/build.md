# Fresh build audit

Verdict: accept. Job newwin-00001-p10-release-44a34dd73dbb. Checked 2026-09-12T11:16:42.970901+00:00.

The final build was run from manuscript/ after `latexmk -C -outdir=build main.tex`:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex

The final command exited 0 and ran pdfLaTeX/BibTeX to convergence. The complete
command transcript is `audit/release-build-command.log`; the final TeX and
BibTeX logs are joined verbatim in `audit/release-build.log`. Scanning the final
logs found no undefined citation/reference, missing/repeated database entry,
overfull/underfull box, LaTeX warning or fatal error. Interim first-pass reference
warnings in a clean-build transcript are not final unresolved diagnostics.

The prescribed check_bib_keys.py command passed: 6 cited keys, 6 bibliography
keys and 6 resolved aux keys, with no missing or extra key. Its output is
`audit/release-bib-check.txt`. All citations and cross-references are resolved.

The PDF has 5 letter-size pages and no encryption or JavaScript. Title, author,
subject and keywords now identify the actual result-note; see
`audit/release-pdfinfo.txt`. All 25 font entries are embedded, subset Type 1 fonts
with Unicode mappings; see `audit/release-pdffonts.txt`.

The .fls recorder confirms main.tex and generated aux/bbl/out are the only local
TeX inputs. references.bib is the listed canonical BibTeX input, and amsplain.bst
and all packages/fonts are installed system dependencies. There is no shell
escape, network build step, unlisted local figure or maintained external bbl.
The README and certificate script were read; the standalone coefficient
certificate was rerun successfully without touching frozen output files.

The earlier dry-run parser failure required literal notation expansion, spelling
out the partition relation, representing multiplicity union with a dotted union,
and expressing unchanged MSC metadata via thanks. These are mathematical-scope
preserving edits, recorded in `audit/release-notation-repair.json`. A preliminary
build was completed before the first dry-run repair succeeded; only the final
post-repair clean build supports this acceptance. The final PDF-metadata update
was followed by another clean build and render; the page pixels stayed identical.

Bound manuscript digest: a225a1f70e851c5d99ff55f694b4658da7f6817b346074c78a3ecc7838247f18.
Bound PDF SHA256: 79032ecd15478bde0f68a76fb829b29db438c3f0a46e008ef4cae98dfc59de29.
