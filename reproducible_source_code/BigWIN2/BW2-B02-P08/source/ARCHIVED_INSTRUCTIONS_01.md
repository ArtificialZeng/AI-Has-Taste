# Source archive for the k=4 phylogenetic-network disproof

This archive accompanies Zijian Zeng's journal-neutral `amsart` manuscript,
"A square-root obstruction to the k=4 phylogenetic-network enumeration
conjecture."

## Contents

- `main.tex`: manuscript source.
- `references.bib`: the seven source-audited bibliography records cited by
  the manuscript.
- `certificates/delta4_laurent.json`: exact Laurent-polynomial and corrected
  closed-form certificate.
- `code/verify_delta4_certificate.py`: independent exact verifier using only
  the Python standard library.
- `code/discover_delta4_sympy.py`: the separate symbolic implementation used
  to cross-check the decisive generating-function computation; it requires
  SymPy.

## Build

From the archive root, run:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

A standard TeX Live installation with `amsart`, `lmodern`, `mathtools`,
`xcolor`, and `hyperref` is sufficient.

## Exact verification

From the archive root, run:

```text
python3 code/verify_delta4_certificate.py
```

The verifier reads `certificates/delta4_laurent.json`, regenerates the
component graphs independently, performs exact rational-arithmetic checks,
and exits unsuccessfully if any required field or equality fails.  It uses no
third-party Python package and does not rely on cached discovery output.

The discovery implementation is not trusted by the verifier.  To rerun that
separate implementation, install SymPy and run:

```text
python3 code/discover_delta4_sympy.py
```

## Scope

The proved result disproves Batle's proposed two-basis polynomial form at
`k=4` and supplies the corrected exact formula for every integer number of
leaves `ell >= 5`.  The manuscript does not claim a result for every larger
reticulation number and has not undergone journal peer review.  No proof
assistant was used.
