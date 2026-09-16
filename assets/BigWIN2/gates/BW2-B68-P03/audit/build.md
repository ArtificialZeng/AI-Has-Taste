# Clean build audit — attempt 2

PASS. A forced clean rebuild used `latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex` in `manuscript/`. The command regenerated the bibliography and converged to a four-page PDF. Its complete console output is `audit/clean-build-attempt2.log`; the final TeX log and digest are bound in `audit/build.json`.

The installed `check_bib_keys.py manuscript/main.tex --aux manuscript/main.aux` reports six cited keys and six bibliography entries, with no missing bibliography, unused keys, or auxiliary citation mismatches. Scanning `main.log` and `main.blg` found no undefined citations or cross-references, missing database entries, repeated entries, BibTeX warnings, LaTeX errors, emergency stops, or overfull boxes. All 25 listed fonts are embedded Type 1 subsets with Unicode mappings. PDF metadata gives the intended title and Xiaojian Zeng as author; the PDF is four US-letter pages and contains extractable text.

The final build matches `audit/manuscript-snapshot.json`. Changes were limited to source-formula wording and the theorem locator; frozen mathematical evidence, claim, checkpoint and source were not modified.

Final typography repair: the strict hook rejected standard pmod and substack commands. Equivalent explicit mod notation and a single-line product index replaced them. The mathematical claims, citations and line intervals did not change. All four pages were rebuilt, rerendered, and viewed again; the final displays remain legible and no warning was found. The final extraction is round 3.
