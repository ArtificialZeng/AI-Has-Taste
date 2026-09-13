# Exact verification

The primary verifier reconstructs the binary64 trace using only exact Python
integers and `Fraction`; it does not use the host floating-point arithmetic:

```bash
python3 verification/verify_stagnation.py certificates/binary64_stagnation.json
```

It is fail-closed: the top-level object and every `arithmetic`, `inputs`,
`exact_system`, `expected_trace`, and nested rational object must have exactly
the documented keys and exact JSON types. Duplicate keys, unknown keys,
missing keys, booleans masquerading as integers, floats or strings in integer
fields, and non-standard `NaN`/`Infinity` constants are rejected. The default
SHA-256 trust anchor is embedded in the verifier. To verify an identical copy
against an external trust anchor, use:

```bash
python3 verification/verify_stagnation.py CERTIFICATE.json \
  --expect-certificate-sha256 LOWERCASE_SHA256
```

The adversarial suite supplies each semantic mutant with its own correct hash,
so schema and mathematical rejection are tested independently of the hash
gate:

```bash
python3 verification/test_tamper_fail_closed.py
```

It covers `badhash`, `extra`, `drop`, `change-input`, `change-trace`, and
`change-arithmetic`, plus duplicate-key, exact-type, nested-extra, `NaN`, and
changed-exact-system attacks. Every tamper must exit nonzero; the suite itself
exits zero only when all negative tests are rejected.

An independent C implementation checks the same serialized inputs on an
IEEE-754 binary64 host.  Contraction and unsafe algebraic rewrites are disabled:

```bash
cc -std=c11 -O0 -frounding-math -ffp-contract=off \
  verification/verify_stagnation_hardware.c -lm -o verification/verify_stagnation_hardware
./verification/verify_stagnation_hardware certificates/binary64_stagnation.json
```

The mathematical induction is finite: the verifier establishes that Algorithm
1 returns `x=0` and that one Algorithm 2 transition maps `0` to `0` exactly.
Determinism then gives `x_k=0` for every iteration count.  The additional 32
iterations in each verifier are diagnostic redundancy, not the proof basis.

The main verifier implements the residual evaluation graph derived in the
source paper's residual lemma: compute `p=fl(b-fl(A*x))`, compute
`q=fl(fl(v*x)*u)`, then `r=fl(p-q)`. It uses the literal left-associated
Algorithm 2 update `fl(fl(x+y_r)-fl(theta_r*z))` and separately checks the
right-associated `fl(x+fl(y_r-fl(theta_r*z)))`; both are exactly zero on the
certificate.
