# Clean build audit

Verdict: accept. Job: `newwin-00001-p09-release-9807a7157078`. Reviewed 2026-09-12T10:20:03.678817+00:00.

Removed only the generated `manuscript/build` directory, then ran `sh manuscript/build.sh` to completion (exit 0): pdfLaTeX, BibTeX, and two final pdfLaTeX passes. Command output is `audit/release-build-command.log`; final converged LaTeX and BibTeX logs are combined in `audit/release-build-final.log`. Initial first-pass unresolved labels are superseded by the final logs. A scan of the final logs found no undefined citations/cross-references, missing or repeated BibTeX entries, TeX errors, warnings, or overfull/underfull boxes.

Ran `python3 /home/ailab/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py manuscript/main.tex --aux manuscript/build/main.aux`: five cited keys, five canonical BibTeX entries and five auxiliary bibliography labels; every missing/unused/inconsistent count is zero. No key or bibliography changes were required. The generated `.bbl` remains byte-identical to the prior input.

The final TeX recorder's authored inputs are main.tex and the generated bibliography; its auxiliary/out files are generated. All six publication source files were read: main.tex, references.bib, build/main.bbl, build.sh, README.md and verify_sc229.py. No extra authored dependency is omitted. System TeX classes/styles/fonts and Python standard-library imports are runtime dependencies.

`pdfinfo` reports six pages, correct title and author, no encryption and no JavaScript. Every listed font is embedded and has a Unicode map. Saved metadata/fonts and dependency diagnostics are under `audit/release-pdfinfo.txt`, `audit/release-fonts.txt`, and `audit/release-build-inspection.json`.

The actual fresh command `python3 manuscript/verify_sc229.py` exited 0 and reproduced the accepted scope: census through n=6, decoder through n=5, formula arithmetic through n=12, and all 81 identity assignments. This is a reproduction of the companion program, not an independent new mathematical implementation. See `audit/release-reproduction.json` and its run log.

Mathematical snapshot: `18815edf6e7f240c1b5c28e90cced864fbed61ffa4fc3c27160e18c4b9bfea38`.
Manuscript digest: `8cb6c3e3d2db41fb4bc023cd68b3ce2ff4d3d04e9f4d543a53b00a298d8effc9`.
PDF digest: `cf142e53197b0ce22401ec43cca40de534ebd52252a00477e83b63d4b14db7fd`.
