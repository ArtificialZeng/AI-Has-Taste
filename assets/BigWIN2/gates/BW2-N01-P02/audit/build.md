# Fresh build audit

Verdict: accept. Job: `newwin-00001-p02-release-80f7dac713d2`. UTC date: 2026-09-12.

Executed `bash manuscript/build.sh`, which uses a clean `latexmk -pdf -gg`
pdfLaTeX/BibTeX build. Exit status was zero. The transcript is
`audit/release-build-transcript.log`. Initial unresolved keys in the first clean
pass were resolved by BibTeX and subsequent passes. The final engine log is
`audit/release-final-tex.log`; the final BibTeX log is
`audit/release-final-bibtex.log`. These final logs have no unresolved citations,
references, TeX errors, font warnings, or overfull/underfull boxes.

The bibliography checker command was
`python3 /home/ailab/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py manuscript/main.tex --aux manuscript/build/main.aux`.
It reports four cited keys, four entries, no missing/unused entries and exact
auxiliary-key agreement (`audit/release-bib-keys.txt`).

The PDF has five letter-size pages, expected title/author metadata, extractable
text, and embedded subset Type 1 fonts with Unicode maps. No packages were
installed. Latin Modern supplies scalable fonts for the standard microtype
setup. Metadata and font listings are retained under `audit/`.

The dependency list is complete: seven authored source/supplement files,
canonical bibliography, no figures or additional authored TeX inputs. Recorder
inputs other than `main.tex` are generated `.aux`, `.out`, and `.bbl` files.
The fresh verifier replay passed and its per-arity and all-comb records match
both the publication output and the accepted referee output exactly. This
checks reproducibility and declared finite coverage, not an all-arity proof.

All immutable input hashes still agree with the entry audit. The rebuilt PDF
was frozen before release review. Manuscript digest: `95aa4a634943aa99c9729bb42bd41f9c78b1d3e5b69c8d775a7f6353ade0a63a`.
PDF digest: `47c3e8c55bf25260d8fbaf373cfa13ed5da93bb4264008afdb218d7b4bd48874`.
