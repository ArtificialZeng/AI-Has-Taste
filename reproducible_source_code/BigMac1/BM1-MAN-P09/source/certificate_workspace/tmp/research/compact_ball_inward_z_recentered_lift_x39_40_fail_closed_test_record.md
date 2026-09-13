# Fail-closed record: recentered inward-Z lift to `X=39/40`

All tests ran sequentially with no second proof process.

| Test | Expected | Observed classification |
|---|---:|---|
| `python -O` | nonzero | rejected because `__debug__` is false |
| `INWARD_Z_X39_40_BAD_DEPENDENCY=1` | nonzero | rejected at predecessor source hash |
| `INWARD_Z_X39_40_BAD_SPARSE_NORMALIZATION=1` | nonzero | rejected at exact sparse/direct `Z` identity |
| `INWARD_Z_X39_40_DROP_TERM=1` | nonzero | rejected at complete core coefficient table |

These checks test verifier integrity.  None is a mathematical
counterexample, chart obstruction, or numerical result.
