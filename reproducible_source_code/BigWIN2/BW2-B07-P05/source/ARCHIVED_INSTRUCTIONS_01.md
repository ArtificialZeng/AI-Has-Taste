# Exact optimization of a ten-point Heilbronn family

This source archive accompanies the manuscript
`Exact Optimization of the Comellas--Yebra Three-Parameter Family for Ten
Points in the Square` by Zijian Zeng.

The theorem is an exact optimization result over the full three-parameter
Comellas--Yebra cube. It does not settle the unrestricted ten-point Heilbronn
problem in the unit square.

## Build the paper

From the archive root, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The tested toolchain was pdfTeX/LaTeX with BibTeX and `latexmk`.

## Verify the exact certificates

From the archive root, run:

```sh
python3 certificates/verify_incumbent_stdlib.py
python3 certificates/verify_incumbent_sympy.py
python3 certificates/verify_analytic_identities.py
python3 certificates/verify_family_cover.py certificates/family_cover.json
```

The first and fourth checks require only the Python standard library. The
second and third require SymPy. To regenerate the finite cover, run:

```sh
python3 certificates/generate_family_cover.py certificates/family_cover.json
```

The floating-point experiment in `experiments/` is diagnostic only and is not
used in the proof.

