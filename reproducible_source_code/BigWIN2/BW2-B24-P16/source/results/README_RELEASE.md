# A071532 counterexample release

Build the paper from the extracted archive with:

```text
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

From the archive root, rerun the exact certificate with:

```text
python3 certificate/certifier_verify.py certificate/certifier_claim.json
```

The certificate uses CPython's standard library only. No randomness, solver,
floating-point arithmetic, or proof assistant is used.
