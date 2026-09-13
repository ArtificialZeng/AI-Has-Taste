# Fail-closed record: materially larger `x <= 7/10` source candidate

Normal execution and both source/verifier `py_compile` runs must exit `0`.
The following serial attacks must exit nonzero at their named gates:

| attack | trigger | gate |
|---|---|---|
| optimized asserts | `python -O -B` | startup rejection |
| predecessor hash | `XNEXT_BAD_PREDECESSOR=1` | predecessor binding |
| normalization | `XNEXT_BAD_NORMALIZATION=1` | compression determinant |
| remove `Q^2` | `XNEXT_DROP_Q2=1` | fully conjugated/cyclic identity |
| danger sign | `XNEXT_FLIP_DANGER=1` | strict-danger identity |
| coefficient corruption | `XNEXT_CORRUPT_COEFFICIENT=1` | exact minimum |
| control deletion | `XNEXT_DROP_CONTROL=1` | control count |
| `S` clearing | `XNEXT_BREAK_S_CLEARING=1` | exact `S` factor identity |
| parameter seam | `XNEXT_BREAK_SEAM=1` | left parameter seam |
| Hermitian seam | `XNEXT_BREAK_HERMITIAN_SEAM=1` | left Hermitian seam |
| control seam | `XNEXT_BREAK_CONTROL_SEAM=1` | left `C4` control seam |
| minus-z lift | `XNEXT_BREAK_MINUS_Z_LIFT=1` | minus signed-z reconstruction |

The freeze verifier also rejects `XNEXT_FREEZE_BAD_SOURCE_HASH=1` and
`XNEXT_FREEZE_BAD_MANIFEST=1`.  All normal, attack, root-replay, and
isolated-copy outputs are made stable before the manifest is generated for
the last time.  A delayed full replay then checks every record, and the
post-freeze attacks are written outside the frozen tree so they cannot mutate
the frozen normal log.
