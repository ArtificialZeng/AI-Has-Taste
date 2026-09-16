# Build and reproduce

Build the article with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The `ancillary/` directory in the release ZIP contains the exact derived
certificate, discovery code, independent verifier, and a downloader for the
two published Bennett--Ghadermarzi source tables.  To reproduce the filter:

```sh
cd ancillary
python3 fetch_upstream.py
python3 reproduce.py
```

The verifier requires CPython 3.10 or later and Poppler `pdftotext`.  The
discovery script additionally requires SymPy; the independent verification
does not.
