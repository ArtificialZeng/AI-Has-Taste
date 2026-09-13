# BM1-AI15-P02

An Exact Transfer-Matrix Proof of Barker's Order-Ten Recurrence for OEIS A321614

Original ID: `af15_02_barker_a321614_recurrence`. Batch: 历史第02批（AI15，2026-08-28/29）.

[Final PDF](../../../pdfs/BigMac1/BM1-AI15-P02_An_Exact_Transfer_Matrix_Proof_of_Barker_s_Order_Ten_Recurrence_for_OEIS_A321614.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-AI15-P02/review.json)

## Mathematical scope

All-n recurrence and minimal order 10 for the fixed four-element rectangle symmetry group; not full D4 at the n=2 square exception.

Historical submission gates reviewed; no fresh proof, citation or novelty audit in this packaging task.

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 33 selected source/evidence files, including 7 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- [`Makefile`](source/Makefile)
- [`certificate/README.md`](source/certificate/README.md)
- [`release/README.md`](source/release/README.md)

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`code/test_fail_closed.py`](source/code/test_fail_closed.py)
- [`code/verify_certificate.py`](source/code/verify_certificate.py)
- [`agents/referee/verify_no_import.py`](source/agents/referee/verify_no_import.py)
- [`agents/breaker/verify_audit.py`](source/agents/breaker/verify_audit.py)
- [`agents/builder/verify_certificate.py`](source/agents/builder/verify_certificate.py)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-AI15-P02/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
