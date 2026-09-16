# Strict domination growth from J(8,4) to J(9,4)

Core exact verification:

```text
python3 code/verify_certificate.py
```

Manuscript build (from the `paper` directory):

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build main.tex
```

The theorem is the separated bound gamma(J(8,4)) <= 6 < 7 <= gamma(J(9,4)).
The CP-SAT files under `experiments/discovery` are discovery records only and
are not inputs to the proof.
