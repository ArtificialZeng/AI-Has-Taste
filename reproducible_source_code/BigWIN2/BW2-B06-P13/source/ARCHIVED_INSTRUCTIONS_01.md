# Build and verify

## Manuscript

From this directory, run:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The tested build used pdfTeX 1.40.22, LaTeX2e 2021-11-15, BibTeX 0.99d,
and latexmk 4.76. The document uses standard TeX Live packages only.

## Exact identities

With Python 3.10 and SymPy 1.14.0 installed, run from this directory:

```text
python3 code/certify_rectangular_pyramid.py
python3 code/verify_rectangular_pyramid_identity.py
python3 code/certify_rhombic_pyramid.py
python3 code/verify_rhombic_pyramid_identity.py
```

Each command must print `"identity_verified": true` and exit with status zero.
The two `certify` programs use coefficient convolution. The two `verify`
programs use direct projective values and a Vandermonde determinant.

The machine-readable summaries are in `certificates/`. Package versions are
pinned in `requirements-lock.txt`.
