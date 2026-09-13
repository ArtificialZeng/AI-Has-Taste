# Reproduction source: strict finite extension for Erdős #647

This archive supports only the terminal state `NEW_STRICT_BOUND` through
`9,180,628,549,092,000,000`.  It does not solve Erdős Problem 647.  The locally
decisive interval is

```text
9,174,471,185,880,000,000 < n <= 9,180,628,549,092,000,000.
```

From the archive root, first verify the frozen decisive inputs:

```text
shasum -a 256 -c verification/FROZEN_CODE_MANIFEST.sha256
```

Run the fail-closed adversarial checks:

```text
python3 verification/test_verifier.py
python3 -O verification/test_verifier.py
(cd /tmp && python3 -I /absolute/archive/path/verification/test_verifier.py)
(cd /tmp && python3 -O -I /absolute/archive/path/verification/test_verifier.py)
```

Reconstruct all `5,078,450,784` cells (this compiles the included C replay):

```text
python3 verification/verify_extension.py --threads 12
```

The canonical stdout must equal
`certificates/finite_extension_certificate.json`, SHA-256
`19f8f31a1d037ddae404448ba13863f10607a23f24414b57628bf13b6ecc83c3`.

Build the manuscript:

```text
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The new replay did not use a proof assistant.  The necessary 2520-divisibility
and elementary 96-residue reduction are imported from the fixed Lean 4 source
identified in `audit/DEPENDENCY_AUDIT.md`.  The earlier prefix through the left
endpoint was inspected but not fully rerun here.
