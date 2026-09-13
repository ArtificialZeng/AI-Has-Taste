# Primary verifier fail-closed audit

## Outcome

**PASS for the specified fail-closed regression matrix.**

The patched `verification/primary_verify.py` accepts the unmodified
certificate in normal, `-O`, and `-O -I` modes.  In every one of those modes
it rejects each specified tampering with a nonzero exit code and does not emit
JSON status `PASS`.

Per the bounded audit instruction, this certifier did not edit
`primary_verify.py`.  The regression was rerun after the root agent replaced
correctness assertions with explicit `require`/`fail` checks and added strict
schema validation.

## Exact regression matrix

| Certificate case | normal | `-O` | `-O -I` |
|---|---:|---:|---:|
| valid source | exit 0, PASS | exit 0, PASS | exit 0, PASS |
| bad extension block `+++++++++` | exit 1, rejected | exit 1, rejected | exit 1, rejected |
| bad zero list `[7,8,12]` | exit 1, rejected | exit 1, rejected | exit 1, rejected |
| missing `schema_version` | exit 1, rejected | exit 1, rejected | exit 1, rejected |

All twelve cells meet their explicit expectation.  The bad zero list is now
rejected directly by `validate_schema`, rather than incidentally by a later
construction failure.

## Raw evidence and reproduction

Run:

```bash
python3 verification/test_primary_fail_closed.py \
  --output verification/primary_fail_closed_results.json
```

The current exit code is 0.  The harness uses explicit Boolean tests and would
return nonzero when any valid-input or tamper-rejection expectation fails.  It
contains no Python language correctness assertions.  Running the harness
itself under `python3 -O -I` also exited 0 and reproduced the same result-file
SHA-256.

The serialized raw evidence is
`verification/primary_fail_closed_results.json`.  For every cell it records
the normalized command, exact certificate hash, expected behavior, actual
exit code, timeout flag, PASS-status parse, and complete stdout/stderr.

Hashes for the audited state:

| Artifact | SHA-256 |
|---|---|
| `verification/primary_verify.py` | `a142f97841cc7e74dccd5cf951de21d3e4f54a569a9df9ebc23b261107828268` |
| `certificates/zero_set_certificate.json` | `ff2d77c2e21b883c6588036137c5482f72a2bbfff3723151d8ab5b72f66a677c` |
| `verification/test_primary_fail_closed.py` | `226022fc6ee40687e2e10445f05f19f1b412d1ee565de31497cca7e59cda90d3` |
| `verification/primary_fail_closed_results.json` | `214e68da395d7cbb96df1ae14159bf2f5f017bc9e9356cb647c143d4617d761c` |

## Repair verification and residual scope

No bare correctness assertion remains in either `primary_verify.py` or the
regression harness.  The verifier now explicitly checks the exact top-level
key set, graph definition, sign encoding, odd-family metadata, one-flip
subschema, seed-key set, special-word key set, zero list, literal extension
block, and all mathematical witness predicates.

No vulnerability remains within the user-specified adversarial cases and
interpreter modes.  This is a bounded fail-closed audit, not a proof that no
possible malformed JSON value or platform-level fault can exist.  The full
raw record reports empty `unmet_expectations` and
`remaining_vulnerabilities` arrays.
