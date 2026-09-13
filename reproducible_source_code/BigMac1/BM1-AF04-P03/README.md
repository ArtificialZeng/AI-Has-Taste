# BM1-AF04-P03

The Largest Cyclic 3-(31,5,1) Packing Has Twelve Base-Block Orbits

Original ID: `af15b4_03_cyclic_31_5_packing`. Batch: 原AI-friendly第04批.

[Final PDF](../../../pdfs/BigMac1/BM1-AF04-P03_The_Largest_Cyclic_3_31_5_1_Packing_Has_Twelve_Base_Block_Orbits.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-AF04-P03/review.json)

## Mathematical scope

精确最大值 M=12（372个展开块）记录已证；当前 research_state.json 仍残留 queued，采用较新 TASK_STATUS 与 FINAL_STATUS。

历史审计；非本次fresh审稿。

## Reproduction coverage

**Exact C++ search, positive certificate and 162 branch records included. About 2.09 GB of stored graphs and old binary omitted. Historical wrappers cannot run unchanged; fresh source replay needs local compilation/rebuilt graphs and an adapter. Not a complete immediate replay bundle.**

This directory contains 340 selected source/evidence files, including 7 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- [`README.md`](source/README.md)
- [`REPRODUCE.md`](source/REPRODUCE.md)

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`code/verify_fixed_clique_certificate.py`](source/code/verify_fixed_clique_certificate.py)
- [`code/verify_global_fixed_cover.py`](source/code/verify_global_fixed_cover.py)
- [`code/verify_packing_certificate.py`](source/code/verify_packing_certificate.py)
- [`tests/test_fixed_clique_certificate.py`](source/tests/test_fixed_clique_certificate.py)
- [`tests/test_global_fixed_cover.py`](source/tests/test_global_fixed_cover.py)
- [`tests/test_positive_verifier.py`](source/tests/test_positive_verifier.py)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-AF04-P03/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.

Direct definition-level C++ search: [`code/exact_clique.cpp`](source/code/exact_clique.cpp). See the linked reproduction notes for compilation and the one-branch interface; all 162 branches have not been rerun in this packaging task.
