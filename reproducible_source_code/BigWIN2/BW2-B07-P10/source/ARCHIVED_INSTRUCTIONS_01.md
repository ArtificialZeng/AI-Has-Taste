# LaTeX source

Build the paper from this directory with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The document uses standard TeX Live packages and BibTeX.  Remove generated
files with `latexmk -C`.

The `supplement/` directory in the release archive contains the exact input
certificates, independent Python verifiers, malformed-input fixtures, and the
human proof summary.  Its programs require Python 3.10 or later and use only
the standard library.  The optional source-transcription check additionally
requires `pdftotext` and a local copy of the cited Brinkmann--McKay paper; the
third-party PDF is not redistributed in the archive.
