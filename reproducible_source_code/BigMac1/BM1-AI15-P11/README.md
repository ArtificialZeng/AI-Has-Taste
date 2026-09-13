# BM1-AI15-P11

Tree independence sequences are unimodal through order 31

Original ID: `af15_11_erdos_993_tree_unimodality`. Batch: 历史第02批（AI15，2026-08-28/29）.

[Final PDF](../../../pdfs/BigMac1/BM1-AI15-P11_Tree_independence_sequences_are_unimodal_through_order_31.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-AI15-P11/review.json)

## Mathematical scope

Partial finite NEW_STRICT_BOUND: complete order-31 tree census; unrestricted tree independence-sequence unimodality conjecture remains open.

Historical submission gates reviewed; no fresh proof, citation or novelty audit in this packaging task.

## Reproduction coverage

**Source + 240 census records included. Historical aggregate wrappers bind omitted machine binaries and the nauty tarball; they do not run unchanged here. Full census replay requires fetching pinned upstream nauty, local compilation and a portability update. Not a fresh census rerun.**

This directory contains 353 selected source/evidence files, including 14 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- [`README.md`](source/README.md)
- [`experiments/README.md`](source/experiments/README.md)

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`experiments/crosscheck_c_checker.py`](source/experiments/crosscheck_c_checker.py)
- [`experiments/builder_gamma_verify.py`](source/experiments/builder_gamma_verify.py)
- [`experiments/build_order31_checker.sh`](source/experiments/build_order31_checker.sh)
- [`experiments/run_tree_sweep_worker.sh`](source/experiments/run_tree_sweep_worker.sh)
- [`experiments/order31_checker.c`](source/experiments/order31_checker.c)
- [`experiments/order31_plugin_decl.h`](source/experiments/order31_plugin_decl.h)
- [`experiments/run_tree_sweep_all.sh`](source/experiments/run_tree_sweep_all.sh)
- [`experiments/aggregate_tree_sweep.py`](source/experiments/aggregate_tree_sweep.py)
- [`discovery/breaker_verify.py`](source/discovery/breaker_verify.py)
- [`discovery/breaker_search.py`](source/discovery/breaker_search.py)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-AI15-P11/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
