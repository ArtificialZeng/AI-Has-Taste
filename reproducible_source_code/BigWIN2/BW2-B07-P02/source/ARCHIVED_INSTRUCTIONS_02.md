# Submission source

This archive contains the LaTeX source and the deterministic certificate
programs accompanying *The distinct-cycle-length probability is strictly
decreasing after 30* by Zijian Zeng.

## Build the paper

With a standard TeX Live installation:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography is stored in `references.bib` and uses `amsplain`.

## Verify the certificates

Python 3 and its standard library are the only program dependencies.

```bash
bash code/run_certificates.sh --fast
```

The fast target checks the structural factorization, the exact rational tail
constants, and the finite prefix at two independently rounded fixed-point
scales.  To also recompute the common-denominator integer expansion through
5000, use:

```bash
bash code/run_certificates.sh --full
```

The full common-denominator step took about 101 seconds in the recorded
Python 3.10.12/WSL2 environment.  No random seeds, external data files,
third-party Python packages, or proof assistants are used.
