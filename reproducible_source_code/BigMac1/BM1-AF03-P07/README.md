# BM1-AF03-P07

The K-Knuth Shape-Interval Conjecture Holds on Alphabets of Size at Most Eight: An Exact Finite Certification

Original ID: `af15b3_07_k_knuth_n8`. Batch: 原AI-friendly第03批.

[Final PDF](../../../pdfs/BigMac1/BM1-AF03-P07_The_K_Knuth_Shape_Interval_Conjecture_Holds_on_Alphabets_of_Size_at_Most_Eight_An_Exact_Finite_Certification.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-AF03-P07/review.json)

## Mathematical scope

字母表大小≤8 的指定有限端点已认证；无界字母表母猜想仍开放。

历史审计；非本次fresh审稿。

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 35 selected source/evidence files, including 6 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- [`REPRODUCE.md`](source/REPRODUCE.md)

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`src/verify_certificate.py`](source/src/verify_certificate.py)
- [`scripts/verify_n8.sh`](source/scripts/verify_n8.sh)
- [`tests/test_discovery.sh`](source/tests/test_discovery.sh)
- [`tests/test_fail_closed.py`](source/tests/test_fail_closed.py)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-AF03-P07/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
