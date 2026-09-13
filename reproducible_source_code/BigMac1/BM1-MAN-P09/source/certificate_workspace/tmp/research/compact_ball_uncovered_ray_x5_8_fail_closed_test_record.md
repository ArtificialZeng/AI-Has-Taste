# Fail-closed record for the uncovered rational ray source

The normal definition-level source replay exits `0`.  The following attacks
were executed serially; each exits `1` at its intended exact gate.

| Attack | Expected gate | Result |
|---|---|---|
| `python -O` | optimized execution forbidden | exit 1 |
| `UNCOVERED_RAY_BAD_COVERAGE=1` | frozen coverage-note hash | exit 1 |
| `UNCOVERED_RAY_BAD_NORMALIZATION=1` | exact `W=373/576` normalization | exit 1 |
| `UNCOVERED_RAY_DROP_Q2=1` | fully conjugated/cyclic raw-gate identity | exit 1 |
| `UNCOVERED_RAY_FLIP_DANGER=1` | exact strict-danger identity | exit 1 |
| `UNCOVERED_RAY_BAD_EXPECTED=1` | exact terminal coefficient `C4` | exit 1 |

The matching atomic `.log` and `.exit` files are included in the source
manifest.  External-cache `py_compile` exits `0`.
