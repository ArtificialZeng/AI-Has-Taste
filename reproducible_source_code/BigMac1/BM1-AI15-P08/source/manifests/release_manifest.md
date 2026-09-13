# Release manifest and reproduction commands

Release date: 2026-08-29 (Asia/Shanghai)

## Frozen mathematical scope

Terminal classification: `PARTIAL_THEOREM`, including a
`NEW_INFINITE_SUBCLASS` component.  The unrestricted Sheil--Small problem and
the degree-four/five all-unimodular, non-endpoint strata with
`2|a_n| < A` are not solved by this release.

## Retained PDF

```text
f5e502d6f122d8720a5871e6b435429102b9ca75eb2c58fa266f2da129be7260  output/pdf/sheil_small_low_degree_covering.pdf
```

The source archive is intentionally not self-hashed inside itself.  Its
archive-level SHA-256 is recorded in `FINAL_STATUS.md` after the one-time ZIP
creation and integrity test.  Every scientific source and audit file inside
the archive is bound by `manifests/source_files.sha256`.

## Verify source bindings

From the extracted archive root:

```bash
shasum -a 256 -c manifests/source_files.sha256
```

## Exact verification

```bash
python3 -m pip install -r requirements-verification.txt
python3 src/builder_symbolic_checks.py
python3 -O -I src/builder_symbolic_checks.py
python3 tests/referee_low_degree_identities.py
python3 -O -I tests/referee_low_degree_identities.py
python3 tests/verify_serialized_low_degree_certificate.py
python3 -O -I tests/verify_serialized_low_degree_certificate.py
python3 tests/gate4_serialized_tamper_matrix.py
```

Each verifier also accepts `--inject-failure`; that option must exit nonzero.
The complete normal/`-O`/`-I`/`-O -I` matrix and adversarial serialized-input
tests are recorded in `audit/fail_closed_dependency.md`.

The serialized certificate is also bound to
`certificates/low_degree_certificate_manifest.json`, which freezes the
canonical certificate plus the formal statement, builder proof/checker,
referee report/checker, and manuscript hashes.  The exact schema, independent
5-by-4 matrix, synchronized-expression test, and hash-chain audit are in
`audit/GATE4_SERIALIZED_CERTIFICATE.md`.  The independent post-referee source
diff is in `audit/BUILDER_NOTES_DIFF_AUDIT.md`.

## Clean manuscript build

```bash
cd paper
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The retained PDF is the separately audited release artifact; building inside
an extracted source archive is a reproducibility check and need not produce a
byte-identical PDF because standard PDF metadata contain build timestamps.

## Proof-assistant disclosure

No proof assistant was used.
