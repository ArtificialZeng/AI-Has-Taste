# LaTeX source and exact certificate

Build the article from this directory with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The archive also contains the exact certificate in `certificates/`. Verify it
from this directory with:

```bash
python3 certificates/certify_exact.py
python3 certificates/verify_symbolic.py
```

The first verifier uses the Python standard library only. The second requires
SymPy; it was tested with SymPy 1.14.0. Both use exact integer and rational
arithmetic and do not import the floating-point discovery program.

The article was built with pdfTeX and BibTeX through Latexmk 4.76.
