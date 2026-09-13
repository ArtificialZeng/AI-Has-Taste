# BM1-AI15-P12

The Rank-Two Marcus Permanent Inequality for Real 3 by 3 Matrices

Original ID: `af15_12_rank2_marcus_permanent`. Batch: 历史第02批（AI15，2026-08-28/29）.

[Final PDF](../../../pdfs/BigMac1/BM1-AI15-P12_The_Rank_Two_Marcus_Permanent_Inequality_for_Real_3_by_3_Matrices.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-AI15-P12/review.json)

## Mathematical scope

Partial theorem: every real 3x3 matrix of rank <=2, with equality classification; n>=4/all-order conjecture and complex variants not resolved.

Historical submission gates reviewed; no fresh proof, citation or novelty audit in this packaging task.

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 65 selected source/evidence files, including 12 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- See the verifier/script index below and its inline usage comments.

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`certificates/verify_n3_sos.py`](source/certificates/verify_n3_sos.py)
- [`certificates/test_fail_closed.py`](source/certificates/test_fail_closed.py)
- [`certificates/verify_n3_sos_stdlib.py`](source/certificates/verify_n3_sos_stdlib.py)
- [`scripts/reproduce_clean.sh`](source/scripts/reproduce_clean.sh)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-AI15-P12/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
