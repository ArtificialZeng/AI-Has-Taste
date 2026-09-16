# Reproduction

From the project root:

```bash
python3 computation/sampled_bounds.py
python3 computation/verify_sampled_bounds.py
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The proof is human-readable and does not depend on the exhaustive comparison
over sample sizes.  The scripts use Python 3 standard-library exact integer
and rational arithmetic, with no randomness.  The recorded run used CPython
3.10.12 and TeX Live/pdfTeX 1.40.22.
