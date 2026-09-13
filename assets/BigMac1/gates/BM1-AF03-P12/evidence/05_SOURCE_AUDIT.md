# LaTeX source-package audit

Date: 2026-08-29 (Asia/Shanghai)  
Artifact: `output/source/Stability_of_3-Packed_Words-source.zip`  
Status: **PASS**

The package contains exactly the three submission-source files:

```text
main.tex
references.bib
main.bbl
```

Archive integrity (`unzip -t`) reports no errors.  The ZIP was unpacked into
the newly allocated directory `/tmp/plactic3-source-audit.dYxcF5`, where no
workspace auxiliary file was available.  A clean `latexmk -C` followed by
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` succeeded and
converged through BibTeX.

Independent checks on the unpacked source report:

- cited keys: 2;
- bibliography keys: 2;
- missing keys: 0;
- unused keys: 0;
- final `.aux` mismatch: 0;
- citation, BibTeX, LaTeX, overfull, and underfull warning matches: 0;
- PDF pages: 10;
- PDF title and author: correct.

The rebuilt PDF has the same 397656-byte size and same document structure as
the release build.  Its byte hash differs because pdfTeX writes a new creation
timestamp into PDF metadata; no claim of byte-reproducible PDF metadata is
made.

```text
54cfa052462a4d963817592af0e499ed0d07f09cf1ddf5682b2d42df11e837ed  output/source/Stability_of_3-Packed_Words-source.zip
```

Verdict: **PASS; the source-package gate is closed.**
