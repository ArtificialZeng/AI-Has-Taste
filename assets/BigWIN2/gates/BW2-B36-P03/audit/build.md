# Clean build audit

Job: `win-00036-p03-release-d28fdfe5f3a8`  
Verdict: **accept**

From `manuscript/`, `latexmk -C main.tex` was followed by `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`. BibTeX and the required rerun converged successfully to a four-page PDF.

The final log scan found no undefined citations or references, missing database entries, BibTeX warnings, repeated entries, LaTeX errors, fatal stops, undefined control sequences, runaway arguments, box warnings, or package warnings. The bibliography checker reports six cited keys, six BibTeX entries, and six AUX keys with empty set differences. All PDF fonts are embedded. `pdfinfo` reports A4 pages, no encryption, and PDF 1.5.

Final digests: PDF `2fd6875bacca0bb9d7566659705062d6a7b45cc03488ae3e03f90f63c9860361`; log `ccd2f7d6f0e4a0abedc5a37e11b743991f362d880b3a9dbe259db3fec13fb19a`; BLG `8773102ee9e1873bffbae6865c1db6a9982f955c25dc7b1ed040a15b32a1018c`; BBL `b52c5814a4e618b295dd072dd7af4a1beb72bc2c5d1f6df5b7c02062180c6d0b`.
