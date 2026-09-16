# Exact finite certificate

The 35 files in `layers/` contain sorted, unique little-endian unsigned
64-bit integers. Bit `i` denotes the `i`th lexicographic four-subset of
vertices `0,...,6`. The decisive command is:

```text
python3 certificate/verify_layers.py certificate/layers \
  --output certificate/verification.json
```

Recorded environment: CPython 3.10.12, NumPy 2.2.6, Numba 0.67.0, x86-64
Linux. The verifier checks file hashes and sizes, strict layer uniqueness,
the exact successor relation, absence of dead proper states, and the unique
full terminal state. It exits nonzero on any failure.
