# Fail-closed record: recentered inward-Z lift to `X=9/10`

All tests below were run sequentially; no second proof process was started.

| Test | Expected | Observed classification |
|---|---:|---|
| `python -O` | nonzero | rejected because `__debug__` is false |
| `INWARD_Z_X9_10_BAD_DEPENDENCY=1` | nonzero | rejected at predecessor source hash |
| `INWARD_Z_X9_10_BAD_SPARSE_NORMALIZATION=1` | nonzero | rejected at exact sparse/direct `Z` identity |
| `INWARD_Z_X9_10_DROP_TERM=1` | nonzero | rejected at complete core coefficient table |

These are verifier-integrity tests.  None is a mathematical counterexample,
chart obstruction, or numerical result.
