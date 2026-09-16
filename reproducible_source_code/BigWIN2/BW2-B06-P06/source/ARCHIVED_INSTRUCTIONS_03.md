# Exact finite result for the path maximal-variation problem

This project proves the certified finite result

\[
\mathbf C_{P_{11}}=\frac{10}{11}.
\]

It does **not** claim the conjectured formula for every path length.

## Decisive exact verification

The verifier requires Python 3.10 or newer and only the standard library.
From the project root run:

```bash
python3 code/verify_radius_certificate.py \
  certificates/p11_radius_certificate.json \
  certificates/p11_radius_certificate.bin
```

The expected result is `VERIFIED` with 5,874,849 chambers, 45,011,088
radius slots, and 10 rational-mixture exceptions. The verifier reconstructs
all signed measures and checks all prefix-flux inequalities with exact
`Fraction` arithmetic.

## Fast integrity tests

```bash
python3 code/test_verifier_fail_closed.py
python3 -m py_compile code/*.py
```

The first command checks a small valid baseline and deliberate digest,
radius, truncation, trailing-data, and mixture-mass corruptions. These tests
exercise rejection behavior; they do not replace the full verification.

## Diagnostic counterexample search

```bash
python3 code/breaker_search.py 11 --levels 3 \
  --random-trials 50000 --seed 20260830
```

The saved run used the explicit seed `20260830` and exact rational input
evaluation. Its failure to find a counterexample is diagnostic only and is
not used for the upper bound.

## Environment

- Decisive verifier: Python 3.10.12, standard library only.
- Discovery/generation: Python 3.10.12, NumPy 2.2.6, SciPy 1.15.3, WSL2.
- Floating-point linear programming was used only to discover supports for
  ten exceptions. The final rational data and all decisive inequalities are
  checked exactly by the independent verifier.

See `certificates/README.md` for the certificate format and
`paper/main.tex` for the human-readable proof.
