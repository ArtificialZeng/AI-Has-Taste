# Release bundle

This release accompanies *A Sharp 3-Degree Erdős--Ko--Rado Theorem for
4-Uniform Families* by Zijian Zeng.

The human-readable proof is in `paper/main.tex` and `proof/main_proof.md`.
The original finite endpoints are independently certified by the canonical
CNFs and LRAT files under `instances/` and `certificates/`.  The fail-closed
verification entry points are:

```bash
python tests/test_verify_instance.py
python tests/test_verify_lrat.py
python verification/verify_lrat.py instances/ekr_k4d3_n9.cnf certificates/ekr_k4d3_n9.lrat --n 9
python verification/verify_lrat.py instances/ekr_k4d3_n10.cnf certificates/ekr_k4d3_n10.lrat --n 10
python discovery/breaker/test_verify_family.py
```

The wrapper needs a C99 compiler available as `cc`.  It does not trust or run
a prebuilt checker: it verifies the pinned `lrat-check.c` hash, snapshots the
source and inputs, builds a temporary executable, and runs only that fresh
executable.

`MANIFEST.json` binds every other file in the unpacked bundle.  Verify it with:

```bash
python /path/to/prove-or-disprove-math/scripts/verify_manifest.py . MANIFEST.json
```

No Lean, Coq, Isabelle, or other proof assistant was used.
