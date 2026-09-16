# Length-eight binary Lyndon shortest superstring

This archive accompanies the exact finite result `L_8 = 94`.

## Build the paper

Requirements: a LaTeX installation with `latexmk`, `pdflatex`, and `bibtex`.

```bash
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The output is `paper/main.pdf`.

## Verify the exact certificate

Requirements: Python 3 standard library only.

```bash
python3 verify/verify_certificate.py
python3 verify/independent_checker.py
python3 verify/test_verifiers.py
```

The primary checker verifies the literal word, attaining target order, and all
930 integer assignment-dual inequalities. The independent checker ignores the
stored dual and target order, regenerates the targets by cyclic orbits, checks
coverage by rolling windows, and recomputes the assignment optimum with an
integer Hungarian algorithm.

## Optional discovery replay

The diagnostic discovery script requires SciPy and NumPy:

```bash
python3 experiments/discover_overlap_milp.py
```

The optimizer output is not a proof dependency.
