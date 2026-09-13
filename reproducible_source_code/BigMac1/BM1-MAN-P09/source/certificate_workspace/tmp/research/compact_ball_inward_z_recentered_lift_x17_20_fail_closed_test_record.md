# Fail-closed test record: recentered inward-Z lift to X=17/20

Date: 2026-08-25.

Final normal replay: **PASS**, exit 0.

| Test | Expected | Observed artifact |
|---|---|---|
| `.venv/bin/python -O ...` | reject | `compact_ball_inward_z_recentered_lift_x17_20_attack_optimized.txt` |
| `INWARD_Z_RECENTER_BAD_DEPENDENCY=1 ...` | reject | `compact_ball_inward_z_recentered_lift_x17_20_attack_bad_dependency.txt` |
| `INWARD_Z_RECENTER_BAD_SPARSE_NORMALIZATION=1 ...` | reject | `compact_ball_inward_z_recentered_lift_x17_20_attack_bad_sparse_normalization.txt` |
| `INWARD_Z_RECENTER_DROP_TERM=1 ...` | reject | `compact_ball_inward_z_recentered_lift_x17_20_attack_drop_term.txt` |

Observed rejections were, respectively: the `__debug__` gate; dependency SHA
mismatch; failure of the exact sparse/direct `Z` identity; and failure of the
complete 34-coefficient core-table gate.  All four processes exited nonzero.

The final normal log records definition-level `Q,Q^2`, `degree_Z=4`,
`34/34/1659`, 40/40 strict controls, full-cell legality, 72/72 exact original
raw-gate diagnostics, the exact source SHA, and strict scope.
