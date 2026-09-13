# Exact-computation environment

- Host: macOS arm64 (workspace-provided machine)
- Python: CPython 3.14.7
- Virtual environment: `.venv`
- SymPy: 1.14.0
- z3-solver: 4.15.3.0
- Discovery random seed: 0 where the API exposes a seed
- Arithmetic: integer cyclotomic remainders and exact Boolean/linear constraints;
  no floating-point vanishing test
- Baseline source: TheoremDB R526 inline CC0 source, copied without algorithmic
  modification to `src/minimal105_replay.py`

The baseline's published source digest is checked before execution.  Its stdout
digest is expected to differ because the serialized environment field contains
the locally installed Z3 version; the matrix digest and mathematical payload
must agree.

## Certified finite route

- Fiber certificate builder: Python standard library and integer arithmetic
- Independent verifier: Python standard library only; no imports from builder
  or discovery code
- Fiber masks: 32,768
- Exact value classes: 14,221
- Normalized vanishing tuples through weight 20: 1,209,813
- Distinct affine blockers: 1,331
- Independent verification: 84.67 seconds wall time, 46,694,400 bytes maximum
  resident set size on the recorded host
- Full verifier result: `results/independent_verification.json`
- Randomness: none
