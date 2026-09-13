# Gate 4 fail-closed execution audit

## Outcome

**PASS.**  The original three scripts used decisive `assert` statements and
were unsafe under `python -O`.  That implementation was rejected.  The
current files use explicit conditions, raise typed exceptions on failure,
print a JSON `FAIL` record to standard error, and exit nonzero.  AST inspection
finds zero `Assert` nodes in all three target programs.

The compact execution record is `logs/fail_closed_matrix.json`; the full
serialized record, including every command, stdout/stderr body, exit code,
and per-stream hash, is `logs/fail_closed_matrix_full.json`.

## Bound artifacts

| Artifact | SHA-256 |
|---|---|
| `certificate/verify_sparse_gap.py` | `6bbe60889ba2d5d8fc2ab9f62255237cf8f77b874f62f0efd446f7a4cf823ae5` |
| `certificate/sparse_gap_claim.json` | `00713a6115905a8fb56b2c4fc4c67654aacdace17236eb4cb4ee35ad469c37a6` |
| `certificate/verify_equilateral_witnesses.py` | `c05022faa74457ac3b57dfa53c6d2e5fa5c564a0745b02b48fd76412c3b8dc96` |
| `certificate/equilateral_witnesses.json` | `48bab7651de14addcc4fcddce0431707607426476e5084d97179d2e36b6a127d` |
| `experiments/proof_cut_frame_audit.py` | `eb1c5627359cee682693ae904b249c16c42f01324790ca2be94d4dd7b3e0789a` |
| `audit/run_fail_closed_matrix.py` | `772a51b17f9c88fb391fa494433a913f0fdfba22415d8a16459ded175cbe9a54` |
| `logs/fail_closed_matrix.json` | `948c38a191cff81ea55bb6b7c64f6bd6343a6dd1eb3a0ce0573d333c6a60a129` |
| `logs/fail_closed_matrix_full.json` | `06c14c25caa3eab24a7a8b3e835524bad1a97fc70b0a7c177fbdb6749301fc25` |

## Execution matrix

The runner used an external directory
`/private/tmp/kusner_fail_closed_srii_y11`, not the project tree.  Each of 12
cases was run with the same absolute artifact paths in four modes:

1. `python SCRIPT ...`
2. `python -O SCRIPT ...`
3. `python -I SCRIPT ...`
4. `python -O -I SCRIPT ...`

The three genuine artifacts returned exit code 0 plus `status=PASS` in all
four modes.  Each of the following tampered cases returned exit code 1 plus
`status=FAIL`, and none printed `PASS`, in all four modes:

- delete sparse-certificate field `m`;
- change `m` from 11 to 10;
- change `d` from 5 to 6;
- change excluded gap counts from `[10,11]` to `[10,12]`;
- delete the first witness's `points` field;
- change its dimension from 5 to 4;
- change its claimed common distance from 2 to 3;
- change one coordinate from 1 to 2;
- change the frame-audit program's bound constant from `M=11` to `M=12`.

This is 48/48 expected process outcomes.  The runner itself returned `PASS`.
An independent referee reran the matrix and obtained the same 48/48 result;
see `audit/referee_round1.md`.

## Scope limitation

`verify_sparse_gap.py` certifies the serialized endpoint and all finite
cut-intersection arithmetic used in the proof.  It does **not** machine-check
the human Parseval rank-one or Naimark-complement implications.  Its success
output now says this explicitly.  Those implications were separately
reconstructed from definitions by the referee.  No proof assistant was used.

## Reproduction

From any directory outside the project, run:

```bash
python /Users/mac/Documents/ChatGPT/ai15-open-math-2026-08-28-batch/06_kusner_l1_5_equilateral/audit/run_fail_closed_matrix.py
```

The temporary tampered inputs are created outside the project and removed
after the run.  The stable outcome summary and per-case output hashes are in
`logs/fail_closed_matrix.json`; the byte-for-byte full run is retained in
`logs/fail_closed_matrix_full.json`.
