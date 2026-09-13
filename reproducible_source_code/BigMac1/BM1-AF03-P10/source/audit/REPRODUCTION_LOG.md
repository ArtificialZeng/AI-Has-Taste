# Reproduction log

Final audit date: 2026-08-29 (Asia/Shanghai).

## Independent exact verifier

Command:

```bash
python3 code/verifier/verify_tree_certificate.py certificates/trees_n2_n9.json
```

Output:

```json
{"certificate_sha256":"5be053e1f8e676769ad33237055bed21c76f9825fd373f7832fb2d21dc414fe6","counts":{"2":1,"3":1,"4":2,"5":3,"6":6,"7":11,"8":23,"9":47},"status":"VERIFIED","verifier_sha256":"6a4b61fc2fe3bcbd0caec0e3cdb8049eecd36034349ffc798f223019cfb431b4"}
```

The final full run took approximately 48 seconds on the recorded local
machine.  The verifier uses the standard library only.

## Destructive-input tests

Command:

```bash
python3 tests/test_verifier_rejects.py
```

Output:

```text
6 fail-closed mutations rejected
```

The six mutations remove a tree, duplicate a tree, insert a loop, forge the
reconstruction code, forge the circuit signature, and add an unexpected
schema field.

## Exact symbolic boundary

Command:

```bash
/opt/anaconda3/bin/python3.13 code/audit/check_three_vertex_boundary.py
```

Output:

```json
{"boundary_equation":"2*a_q - d_pq - d_rq","determinant":"-(a_p - d_qp)*(a_r - d_qr)*(2*a_q - d_pq - d_rq)","script_sha256":"d25b188589fd01835782e346a9606f958f42782c92826a015ab5b955d5c1cb0c","status":"VERIFIED"}
```

## Manuscript and bibliography

A clean `latexmk` build produced six pages and returned exit status zero.
Final scans of `main.log` and `main.blg` found no warning, undefined
reference, overflow, underflow, or error.  The bibliography checker returned
three cited keys, three database keys, and zero missing or unused keys.  The
LaTeX audit returned `cited=3 bib=3 missing=0 unused=0`.

All six PDF pages were rendered at 144 dpi and visually inspected.  See
`audit/PDF_AUDIT.md`.

## Release manifest behavior

An attempted manifest of the live workspace was correctly rejected after the
active session transcript changed between hashing and verification.  The
release manifest therefore targets `release/frozen`, which contains only
static release inputs and outputs.  The command is:

```bash
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/verify_manifest.py release/frozen release/manifest.json
```

This separation is intentional and fail closed; the mutable live transcript
is not treated as frozen evidence.
