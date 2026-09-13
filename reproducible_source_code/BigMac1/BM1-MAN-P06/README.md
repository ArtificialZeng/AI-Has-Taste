# BM1-MAN-P06

One-Sided Parity Compression for Certified SAT Attacks on the 33-Point Erdős–Szekeres Problem

Original ID: `DMAC1-MAN-es7`. Batch: 手工课题（2026-08）.

[Final PDF](../../../pdfs/BigMac1/BM1-MAN-P06_One_Sided_Parity_Compression_for_Certified_SAT_Attacks_on_the_33_Point_ErdosSzekeres_Problem.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-MAN-P06/review.json)

## Mathematical scope

Submission-ready partial methods paper: one-sided parity-compressed refutation-sound SAT encoding, exact 33-point counts, ES5 regression and known ES6 sanity certificates; ES(7)=33 not solved.

Historical submission gates reviewed; no fresh proof, citation or novelty audit in this packaging task.

## Reproduction coverage

**Encoding/count scripts and small ES5 CNF/DRAT/LRAT included. About 1.41 GB of large ES6 proof traces and third-party checker binaries omitted; full certificate replay requires regeneration and local DRAT/LRAT checkers.**

This directory contains 28 selected source/evidence files, including 12 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- See the verifier/script index below and its inline usage comments.

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`code/verify_benchmark_records.py`](source/code/verify_benchmark_records.py)
- [`code/verify_direct_six_encoding.py`](source/code/verify_direct_six_encoding.py)
- [`code/verify_encoding_certificate.py`](source/code/verify_encoding_certificate.py)
- [`code/verify_es17_cube_certificate.py`](source/code/verify_es17_cube_certificate.py)
- [`code/verify_parity_encoding.py`](source/code/verify_parity_encoding.py)
- [`code/verify_parity_independent.py`](source/code/verify_parity_independent.py)
- [`code/verify_sat_certificates.py`](source/code/verify_sat_certificates.py)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-MAN-P06/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
