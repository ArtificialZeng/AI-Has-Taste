# Exact verification environment

The independent verifier uses only the Python standard library:

```bash
python3 tests/referee_low_degree_identities.py
python3 -O -I tests/referee_low_degree_identities.py
```

The builder-side CAS cross-check was audited with CPython 3.13.5 and the
exact packages in `requirements-verification.txt`.  In a clean environment:

```bash
python3 -m pip install -r requirements-verification.txt
python3 src/builder_symbolic_checks.py
python3 -O -I src/builder_symbolic_checks.py
```

Both programs implement `--inject-failure`; that option must exit nonzero in
normal, `-O`, `-I`, and combined `-O -I` modes.  The complete external-CWD
matrix and its bound hashes are recorded in
`audit/fail_closed_dependency.md`.

The canonical serialized certificate is reconstructed without third-party
packages.  Its strict schema, certificate SHA-256, and the frozen
formal/builder/referee/manuscript hashes are bound by the separately
digest-pinned `certificates/low_degree_certificate_manifest.json`:

~~~bash
python3 tests/verify_serialized_low_degree_certificate.py
python3 -O -I tests/verify_serialized_low_degree_certificate.py
~~~

The verifier authenticates the manifest and certificate digests, rejects
unknown or missing fields at every schema level, verifies every frozen
artifact hash, and requires the exact 11-check inventory before
recomputation.  A coefficient tamper, an incomplete certificate, a
tautology-only certificate, a duplicate key/label, or `--inject-failure`
must exit nonzero.

The complete genuine/badhash/extra-field/drop-check/change-expression matrix
in normal, `-O`, `-I`, and `-O -I` modes is reproducible from an external
working directory with:

~~~bash
python3 tests/gate4_serialized_tamper_matrix.py
~~~

The serialized layer is supporting exact evidence, not a substitute for the
analytic proof, independent human-style referee reconstruction, or the
hard-coded standard-library referee checker.  See
`audit/GATE4_SERIALIZED_CERTIFICATE.md`.

The optional search programs are diagnostics, not proof certificates.  Their
separate pins are in `requirements-diagnostics.txt`.
