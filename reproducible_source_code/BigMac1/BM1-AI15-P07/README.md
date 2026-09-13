# BM1-AI15-P07

A certified finite verification of Erdos–Szekeres #699 for i=3 and n at most 100 million

Original ID: `af15_07_erdos_szekeres_699_binomial_prime`. Batch: 历史第02批（AI15，2026-08-28/29）.

[Final PDF](../../../pdfs/BigMac1/BM1-AI15-P07_A_certified_finite_verification_of_ErdosSzekeres_699_for_i_3_and_n_at_most_100_million.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-AI15-P07/review.json)

## Mathematical scope

Partial certified finite endpoint: i=3 and 8<=n<=100000000 only; full Erdos-Szekeres #699 open.

Historical submission gates reviewed; no fresh proof, citation or novelty audit in this packaging task.

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 43 selected source/evidence files, including 5 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- [`code/README.md`](source/code/README.md)

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`code/verify_i3.cpp`](source/code/verify_i3.cpp)
- [`code/verify_release_binding.py`](source/code/verify_release_binding.py)
- [`code/test_release_binding.py`](source/code/test_release_binding.py)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-AI15-P07/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
