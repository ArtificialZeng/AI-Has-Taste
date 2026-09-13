# BM1-AF03-P15

A certified normalized flow for the absolute order of type D9

Original ID: `af15b3_15_type_d9_normalized_flow`. Batch: 原AI-friendly第03批.

[Final PDF](../../../pdfs/BigMac1/BM1-AF03-P15_A_certified_normalized_flow_for_the_absolute_order_of_type_D9.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-AF03-P15/review.json)

## Mathematical scope

D9 normalized flow 指定有限端点已认证；不证明所有 Dn。

历史审计；非本次fresh审稿。

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 55 selected source/evidence files, including 12 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- [`REPRODUCE.md`](source/REPRODUCE.md)
- [`certificates/README.md`](source/certificates/README.md)

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`certificates/verify_d9_flow.py`](source/certificates/verify_d9_flow.py)
- [`tests/verify_breaker_orbit_candidate.py`](source/tests/verify_breaker_orbit_candidate.py)
- [`tests/test_breaker_crosscheck.py`](source/tests/test_breaker_crosscheck.py)
- [`tests/test_verify_d9_flow.py`](source/tests/test_verify_d9_flow.py)
- [`tests/verify_breaker_element_certificate.py`](source/tests/verify_breaker_element_certificate.py)
- [`discovery/test_verifier_rejects.py`](source/discovery/test_verifier_rejects.py)
- [`discovery/verify_orbit_flow.py`](source/discovery/verify_orbit_flow.py)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-AF03-P15/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
