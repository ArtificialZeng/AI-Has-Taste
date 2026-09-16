# Least two-variable PI degree for M3(F2)

The exact result is `d = 7`. The proof consists of an explicit 18-word identity
and a full-rank degree-six evaluation minor.

## One-command exact verification

```bash
python3 src/verify_certificate.py certificates/min_degree_7.json
```

This command uses only Python's standard library and exhaustively checks all
262144 ordered matrix pairs.

## Cross-checks

```bash
python3 src/breaker_independent.py
python3 -m unittest -v tests/test_exact.py
```

The tests require the versions in `requirements-discovery.txt`. The manuscript
is built with `latexmk -pdf -interaction=nonstopmode -halt-on-error paper/main.tex`.
