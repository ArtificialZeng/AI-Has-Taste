# Experiment provenance

## Discovery scan

The discovery run used `extend647.c` from commit
`f727ab831abd533d36260f36f0b3433d8db0715e` of
<https://github.com/bentrd/erdos647-frontier-extension>.  The inspected source
had SHA-256
`72d23c4210c693020706ea21bf5bb6700b8406f74967691f3feaa563f289fbbd`.
It was compiled with Apple clang 21.0.0 and run as

```text
./extend647 pairs.txt 0 15140 149000001 149100000 12 discovery.log
```

The raw log is `raw/discovery_extension_u149000001_149100000.log` (SHA-256
`cfea6953a57d56a08b3ad6bc26ecbf97dfeffc18c74e23e7f42c96171eb97603`).
It contains one aggregate line for each of 15,140 open subprogressions.  The
run took 28.54 wall-clock seconds on the host recorded in `manifest.json` and
reported zero survivors among 1,514,000,000 cells.  This log is discovery
provenance, not the final certificate.

## Independent certification

`../verification/generate_sieve96_pairs.py` first reconstructs all 96 residues
of the published 12-form sieve and their complete \(96\times529=50,784\)
subprogressions.  Thus the final replay does not trust the more elaborate
55-residue and 6,549-subprogression closure layers used by discovery.
`../verification/replay_open_subaps.c` then uses a separate segmented
exact-division implementation and only makes lower-bound kills that are valid
without any primality assumption on the residual cofactor.
`../verification/verify_extension.py` factors every undecided cell from scratch
using a different deterministic 64-bit Miller--Rabin/Pollard--rho
implementation.  The one-command replay is

```text
python3 verification/verify_extension.py --threads 12
```

It re-enumerates all 5,078,450,784 cells from the serialized input, including
the partial layer immediately above the left endpoint, and fails closed on a
malformed pair list, coverage mismatch, unsafe endpoint, duplicate hard cell,
stale artifact hash, inconsistent hard-cell coordinates, or unresolved exact
factorization.

## Gate 4 optimization/isolation matrix

`test_verifier.py` loads `verify_extension.py` by absolute file path using
`importlib.util`; it does not depend on the current working directory or
`sys.path`.  Neither file contains a Python `assert` statement.  Both the fast
adversarial suite and the full decisive replay passed in all four modes:

```text
python3 test_verifier.py
python3 -O test_verifier.py
python3 -I /absolute/path/to/test_verifier.py
python3 -O -I /absolute/path/to/test_verifier.py
```

The negative suite corrupts the pair hash, duplicates a pair, changes an
endpoint, crosses the signed-64 boundary, deletes a required field, changes a
hard factor, and supplies inconsistent hard-cell coordinates.  All are
explicitly rejected even under `-O -I`.  Logs and hashes are recorded in
`../audit/GATE4_AUDIT.md`.
