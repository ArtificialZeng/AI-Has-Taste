# Recovery sanity checks

This packaging pass did not rerun the full census. It performed the bounded
checks below on 2026-09-09 using the preserved artifacts.

- `source.md` retained SHA-256
  `e8d3f12668e1311cc09c0fb6df882dfb0726e649e17c394b04813b8d6b92fe1a`.
- All six SHA-256 values named in `research-recovery.md` matched their files.
  The remaining executable, solver-script, rooted-stream, cross-check-script,
  and tool hashes inspected from `run-metadata.json` also matched.
- The inventory has 11,094 newline-terminated six-byte graph6 records
  (77,658 bytes), and sorting followed by deduplication still gives 11,094
  records. The base and augmented canonical rooted streams have respectively
  88,752 and 1,204,584 records, as forced by their byte sizes.
- Re-executing `evidence/exact_regression.py` with
  `/Users/mac/4prove-or-disprove-math/.research-venv/bin/python` produced output
  byte-identical to `evidence/exact-regression.json`.
- Re-executing `evidence/graph6_crosscheck.py` with the same interpreter
  produced output byte-identical to `evidence/graph6-crosscheck.json`.
- Independent JSON assertions checked
  `11094*8*2 = 177504`, `150573*8 = 1204584`, equality of the direct augmented
  count and the nonedge count, zero singular systems, and direct zero-residue
  counts `[0,0]`. SymPy independently returned prime for both 1,000,003 and
  1,000,033.
- Recompiling `evidence/census_modular.cpp` with the recorded flags produced
  SHA-256
  `cd93ad1271c11a05a1eb411fab9ef6f3c57d5e3f047095ca6850f8c6bb5e2a75`,
  identical to the preserved executable.

These are integrity and structural checks, not a fresh mathematical review.
The frozen claim still requires an independent referee to audit completeness,
the rational-to-finite-field implication, both solver formulations, and direct
coverage of every marked instance.
