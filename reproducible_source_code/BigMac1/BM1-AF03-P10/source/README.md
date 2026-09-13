# Generic Lotka--Volterra tree systems

This directory proves van der Kamp's generic tree-system conjecture for every
tree order, and therefore settles the requested first previously unreported
order (n=9).  It also contains an independent exact finite certificate for
all unlabeled trees of orders 2 through 9.

## Main result

For finite simple trees of the same order over a characteristic-zero field,
linear equivalence of their generic homogeneous Lotka--Volterra tree classes,
even after birational parameter remapping, implies isomorphism of the trees.
Special parameter subvarieties are deliberately outside this endpoint.

The human-readable proof is in `proof/main_proof.md`; the publication version
is `paper/main.tex` and `output/pdf/generic_lv_tree_systems_determine_trees.pdf`.

## Exact reproduction

Run from this directory:

```bash
python3 code/verifier/verify_tree_certificate.py certificates/trees_n2_n9.json
python3 tests/test_verifier_rejects.py
/opt/anaconda3/bin/python3.13 code/audit/check_three_vertex_boundary.py
```

The first two commands require only the Python standard library.  The third
uses SymPy and checks the exact three-vertex boundary factorization.  The
certificate verifier must report SHA-256
`5be053e1f8e676769ad33237055bed21c76f9825fd373f7832fb2d21dc414fe6`,
counts `1,1,2,3,6,11,23,47`, and status `VERIFIED`.

Build and audit the manuscript with:

```bash
cd paper
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
cd ..
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py paper/main.tex --aux paper/main.aux
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py paper/main.tex paper/references.bib
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py release/frozen release/manifest.json
```

No Lean, Coq, Isabelle, or other proof assistant was used.
