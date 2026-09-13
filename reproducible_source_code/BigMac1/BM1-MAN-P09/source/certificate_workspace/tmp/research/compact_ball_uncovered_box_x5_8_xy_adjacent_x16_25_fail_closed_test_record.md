# Fail-closed record: adjacent `x <= 16/25` source candidate

All commands are run serially from the workspace root.  Normal execution and
`py_compile` exit `0`.  Each mutation below must exit nonzero at its named
gate:

| attack | environment / command | expected gate |
|---|---|---|
| optimized asserts | `python -O -B` | startup rejection |
| predecessor hash | `XNEXT_BAD_PREDECESSOR=1` | predecessor binding |
| normalization | `XNEXT_BAD_NORMALIZATION=1` | compression determinant |
| remove `Q^2` | `XNEXT_DROP_Q2=1` | fully conjugated/cyclic identity |
| danger sign | `XNEXT_FLIP_DANGER=1` | strict-danger identity |
| coefficient corruption | `XNEXT_CORRUPT_COEFFICIENT=1` | exact frozen minimum |
| control deletion | `XNEXT_DROP_CONTROL=1` | full control count |
| parameter seam | `XNEXT_BREAK_SEAM=1` | left parameter seam |
| Hermitian seam | `XNEXT_BREAK_HERMITIAN_SEAM=1` | left Hermitian seam |
| minus-z lift | `XNEXT_BREAK_MINUS_Z_LIFT=1` | minus signed-z reconstruction |

The freeze verifier additionally has `XNEXT_FREEZE_BAD_SOURCE_HASH=1` and
`XNEXT_FREEZE_BAD_MANIFEST=1` attacks.  The manifest is generated only after
all normal, attack, root-replay, and isolated-copy-replay outputs have reached
stable final bytes.  It is then replayed from the workspace root and a fresh
isolated directory; neither post-freeze attack may modify any frozen normal
record.
