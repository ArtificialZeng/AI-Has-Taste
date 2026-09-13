# BM1-AF04-P07

A certified determination of nu3(11)=15 for arc-disjoint transitive triples in tournaments

Original ID: `af15b4_07_tournament_tt3_n11`. Batch: 原AI-friendly第04批.

[Final PDF](../../../pdfs/BigMac1/BM1-AF04-P07_A_certified_determination_of_nu3_11_15_for_arc_disjoint_transitive_triples_in_tournaments.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-AF04-P07/review.json)

## Mathematical scope

nu3(11)=15 指定有限端点已认证；一般 n 不因本结果而解决。

历史串行角色审计；非本次fresh审稿。

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 976 selected source/evidence files, including 14 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- [`README.md`](source/README.md)
- [`certificates/README.md`](source/certificates/README.md)
- [`code/Makefile`](source/code/Makefile)
- [`code/README.md`](source/code/README.md)

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`tests/test_compare_fail_closed.py`](source/tests/test_compare_fail_closed.py)
- [`tests/test_sweep_fail_closed.py`](source/tests/test_sweep_fail_closed.py)
- [`tests/test_fail_closed.py`](source/tests/test_fail_closed.py)
- [`tests/test_small_baseline.py`](source/tests/test_small_baseline.py)
- [`code/verify_minimizer.py`](source/code/verify_minimizer.py)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-AF04-P07/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
