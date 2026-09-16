# Starlike Trees and the Diameter Conjecture for Multiset Dimension

This archive contains the LaTeX source, exact verification programs, and the
JSON reports supporting the manuscript.  The general conjecture for arbitrary
trees remains open; the paper proves it for all starlike trees and certifies
the finite range through order 15.

## Build the paper

From this directory, run:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The build uses standard TeX Live packages and BibTeX.  It produces
`main.pdf`.

## Verify the recorded computations

Python 3.10 or later is recommended.  Install the discovery dependency with:

```sh
python3 -m pip install -r requirements.txt
```

Run the lightweight evaluator tests and compare the two independently
generated finite reports:

```sh
python3 tests/test_exact_evaluators.py
python3 scripts/compare_finite_reports.py \
  --discovery experiments/discovery_n1_10.json \
    experiments/discovery_n11_13.json experiments/discovery_n14.json \
    experiments/discovery_n15.json \
  --independent experiments/independent_verify_n1_15.json \
  --output finite_comparison_check.json
```

The first finite enumerator, `scripts/explore_trees.py`, uses NetworkX's
nonisomorphic-tree generator, BFS distances, sphere masks, and a literal
sorted-multiset check.  The independent verifier,
`scripts/verify_finite_range.py`, uses its own rooted-tree generator, AHU
center codes, Floyd--Warshall distances, and literal sorted multisets; it does
not import NetworkX or the first enumerator.  The exact reports agree on all
13,188 nonisomorphic trees of orders 1 through 15.

The starlike construction can be checked independently against all recorded
capacity-valid arm tuples with:

```sh
python3 scripts/verify_starlike_construction.py \
  --max-arms 12 --max-length 8 \
  --output experiments/starlike_construction_check_m12_l8.json
```

That bounded run checks implementation details only.  The infinite starlike
theorem follows from the symbolic proof in the paper.
