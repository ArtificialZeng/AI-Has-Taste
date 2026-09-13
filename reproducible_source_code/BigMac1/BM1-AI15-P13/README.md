# BM1-AI15-P13

A Fixed-Point Counterexample to Condition-Number-Only Stability of Sherman–Morrison Iterative Refinement

Original ID: `af15_13_sherman_morrison_refinement`. Batch: 历史第02批（AI15，2026-08-28/29）.

[Final PDF](../../../pdfs/BigMac1/BM1-AI15-P13_A_Fixed_Point_Counterexample_to_Condition_Number_Only_Stability_of_ShermanMorrison_Iterative_Refinement.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-AI15-P13/review.json)

## Mathematical scope

Disproof of the precise uniform condition-number-only fixed-precision SM--IR conjecture; source conditional theorem and genuinely safeguarded variants not refuted.

Historical submission gates reviewed; no fresh proof, citation or novelty audit in this packaging task.

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 31 selected source/evidence files, including 7 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- [`verification/README.md`](source/verification/README.md)

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`verification/verify_stagnation.py`](source/verification/verify_stagnation.py)
- [`verification/verify_stagnation_2x2.py`](source/verification/verify_stagnation_2x2.py)
- [`verification/test_tamper_fail_closed.py`](source/verification/test_tamper_fail_closed.py)
- [`verification/verify_stagnation_hardware.c`](source/verification/verify_stagnation_hardware.c)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-AI15-P13/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
