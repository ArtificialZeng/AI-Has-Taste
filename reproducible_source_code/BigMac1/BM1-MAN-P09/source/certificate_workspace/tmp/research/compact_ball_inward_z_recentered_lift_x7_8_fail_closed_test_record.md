# Fail-closed test record: recentered inward-Z adjacent cell to X=7/8

Date: 2026-08-25.

The final normal replay exits zero and prints PASS for the original
Hermitian `Q,Q^2` reconstruction, exact predecessor splice, `34/34/1659`,
40/40 strict controls, full-cell legality and 72/72 raw-gate diagnostics.

| Test | Expected | Observed artifact |
|---|---|---|
| optimized Python `-O` | reject | `compact_ball_inward_z_recentered_lift_x7_8_attack_optimized.txt` |
| `INWARD_Z_X7_8_BAD_DEPENDENCY=1` | reject | `compact_ball_inward_z_recentered_lift_x7_8_attack_bad_dependency.txt` |
| `INWARD_Z_X7_8_BAD_SPARSE_NORMALIZATION=1` | reject | `compact_ball_inward_z_recentered_lift_x7_8_attack_bad_sparse_normalization.txt` |
| `INWARD_Z_X7_8_DROP_TERM=1` | reject | `compact_ball_inward_z_recentered_lift_x7_8_attack_drop_term.txt` |

The observed gates were, respectively, the `__debug__` guard, a dependency
SHA mismatch, the exact sparse/direct recentered-`Z` identity, and the
complete 34-coefficient core-table check.  All four attack runs exited
nonzero.
