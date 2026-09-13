# Fail-closed record: recentered inward-Z lift to `X=15/16`

All tests ran sequentially with no second proof process.

| Test | Expected | Observed classification |
|---|---:|---|
| `python -O` | nonzero | rejected because `__debug__` is false |
| `INWARD_Z_X15_16_BAD_DEPENDENCY=1` | nonzero | rejected at predecessor source hash |
| `INWARD_Z_X15_16_BAD_SPARSE_NORMALIZATION=1` | nonzero | rejected at exact sparse/direct `Z` identity |
| `INWARD_Z_X15_16_DROP_TERM=1` | nonzero | rejected at complete core coefficient table |

These are verifier-integrity checks, not mathematical counterexamples,
chart obstructions, or numerical evidence.
