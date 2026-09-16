# Two-generation of the equal-sign fiber product

The theorem and proof are in `paper/main.tex`; `paper/main.pdf` is the built
article. The proof is deductive. The finite certificate is an independent
diagnostic audit of the exceptional groups.

Rebuild the article:

```text
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error paper/main.tex
```

Verify the exact finite certificate:

```text
python3 code/verify_finite_certificate.py certificates/finite_two_generator_certificate.json
```

No nonstandard Python packages and no proof assistant are required.
