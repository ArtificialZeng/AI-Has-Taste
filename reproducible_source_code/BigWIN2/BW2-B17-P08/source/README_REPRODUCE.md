# Reproduce the certified result

Run from the project/archive root:

```sh
python3 code/verify_witness_a.py
python3 code/verify_witness_b.py
cd paper && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The verifiers use only the Python standard library. Both must print `PASS`,
2,587,336 eligible sets, and the same edge-size histogram. The LaTeX build
requires a standard TeX Live installation with `amsart`, `lmodern`, `xcolor`,
and `hyperref`.
