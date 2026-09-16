# Clean build audit

**Verdict:** accept  
**Release job:** `win-00069-p01-release-f4ce9d811492`

The canonical manuscript was cleaned and rebuilt from source with

```text
cd manuscript
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`latexmk` converged after BibTeX and the required LaTeX rerun.  The final
`main.log` and `main.blg` contain no undefined citation or reference, missing
database entry, repeated entry, LaTeX error, fatal error, emergency stop,
undefined control sequence, runaway argument, or BibTeX warning.  The
bibliography checker reports seven cited keys, seven bibliography entries, and
the same seven final AUX keys, with no missing or unused key.

`pdfinfo` reports a valid five-page letter-size PDF with the intended title,
author, subject, and keywords.  `pdffonts` reports every listed font embedded
and subsetted.  The build changed no frozen mathematical input.

For attempt 3, the compatibility-edited canonical source was cleaned and rebuilt
before the manuscript snapshot was refrozen.  The new PDF has five pages and
SHA-256 `8daae221db6c2b2c83d69c64bb178a121818372ff427e694858e15ce3997b378`;
the recomputed `main.log` SHA-256 is
`2af774dadd25b23fdbe8bb7db3fa80d2c3fc832220d4d471aedf3dd90ad38d20`.
The final log/BLG diagnostic scan and BibTeX/BIB/AUX seven-key comparison pass.
One logged overfull box is the pair of monospaced ancillary paths; direct page-4
inspection confirms both wrap legibly inside the visible text area without
clipping or overlap.
