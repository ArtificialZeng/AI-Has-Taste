# BM1-AF03-P01

A Sharp 3-Degree Erdos–Ko–Rado Theorem for 4-Uniform Families

Original ID: `af15b3_01_d_degree_ekr_k4d3`. Batch: 原AI-friendly第03批.

[Final PDF](../../../pdfs/BigMac1/BM1-AF03-P01_A_Sharp_3_Degree_ErdosKoRado_Theorem_for_4_Uniform_Families.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-AF03-P01/review.json)

## Mathematical scope

原题指定 (k,d)=(4,3) 族已记录为完整证明；不是全部 (k,d) 的母猜想。

历史审计；非本次fresh审稿。

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 70 selected source/evidence files, including 15 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- [`README.md`](source/README.md)
- [`certificates/README.md`](source/certificates/README.md)
- [`discovery/breaker/README.md`](source/discovery/breaker/README.md)
- [`verification/third_party/drat-trim/Makefile`](source/verification/third_party/drat-trim/Makefile)
- [`verification/third_party/drat-trim/README.md`](source/verification/third_party/drat-trim/README.md)

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`discovery/breaker/verify_family.py`](source/discovery/breaker/verify_family.py)
- [`discovery/breaker/test_verify_family.py`](source/discovery/breaker/test_verify_family.py)
- [`tests/test_verify_instance.py`](source/tests/test_verify_instance.py)
- [`tests/test_verify_lrat.py`](source/tests/test_verify_lrat.py)
- [`code/reproduce_hz_baseline.py`](source/code/reproduce_hz_baseline.py)
- [`verification/verify_lrat.py`](source/verification/verify_lrat.py)
- [`verification/verify_instance.py`](source/verification/verify_instance.py)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-AF03-P01/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
