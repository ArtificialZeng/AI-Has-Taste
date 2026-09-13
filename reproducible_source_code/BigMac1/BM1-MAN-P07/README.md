# BM1-MAN-P07

A Finite Prime-Set Exclusion and an Odd-Modular Obstruction in Lehmer's Totient Problem

Original ID: `DMAC1-MAN-lehmer`. Batch: 手工课题（2026-08）.

[Final PDF](../../../pdfs/BigMac1/BM1-MAN-P07_A_Finite_Prime_Set_Exclusion_and_an_Odd_Modular_Obstruction_in_Lehmer_s_Totient_Problem.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-MAN-P07/review.json)

## Mathematical scope

Eight-page round-2 certified finite and structural result: every composite Lehmer solution has greatest prime factor at least 349, plus 38-survivor modular explanation and infinite odd-component obstruction. Does not improve global published bounds or solve Lehmer.

Historical submission gates reviewed; no fresh proof, citation or novelty audit in this packaging task.

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 24 selected source/evidence files, including 12 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- [`certificates/README.md`](source/certificates/README.md)

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`src/test_survivor_obstructions.py`](source/src/test_survivor_obstructions.py)
- [`src/verify_bounded_prime_sets.cpp`](source/src/verify_bounded_prime_sets.cpp)
- [`tests/test_search_bounded_prime_sets.sh`](source/tests/test_search_bounded_prime_sets.sh)
- [`tests/test_verify_bounded_prime_sets.sh`](source/tests/test_verify_bounded_prime_sets.sh)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-MAN-P07/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
