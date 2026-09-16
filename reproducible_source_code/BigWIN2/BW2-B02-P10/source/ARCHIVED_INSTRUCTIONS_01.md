# CRIM boundary-word classification

This source package accompanies the journal-neutral `amsart` manuscript
*A Boundary-Word Classification of Losing Positions in CRIM* by Zijian Zeng.

## Build the manuscript

From the package root, run:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography is processed automatically from `references.bib`.

## Run the exact checks

Fast regression tests:

```bash
python3 -m unittest tests/test_crim.py
```

Independent partition computations through size 50:

```bash
python3 code/discovery_dp.py --max-size 50 \
  --output results/discovery_n50.json
python3 code/independent_verify.py --max-size 50 \
  --expected results/discovery_n50.json \
  --output results/verification_n50.json
```

Independent canonical-word verification through perimeter 22:

```bash
python3 code/boundary_check.py --max-length 22 \
  --output results/boundary_check_p22.json
```

All programs use exact integer or Boolean arithmetic and only the Python
standard library.  The computations are supplementary checks; the theorem is
proved combinatorially in the manuscript.
