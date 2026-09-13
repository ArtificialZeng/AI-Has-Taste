# BM1-AF03-P14

Local extrema of central hyperplane sections of the five-dimensional cube

Original ID: `af15b3_14_cube_section_q5`. Batch: 原AI-friendly第03批.

[Final PDF](../../../pdfs/BigMac1/BM1-AF03-P14_Local_extrema_of_central_hyperplane_sections_of_the_five_dimensional_cube.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-AF03-P14/review.json)

## Mathematical scope

Q5 局部极值分类记录为完整证明；不外推到任意维度。

历史审计；非本次fresh审稿。

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 92 selected source/evidence files, including 37 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- See the verifier/script index below and its inline usage comments.

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`tests/test_triangle_highpair_verifier.py`](source/tests/test_triangle_highpair_verifier.py)
- [`tests/test_empty_highpair_verifier.py`](source/tests/test_empty_highpair_verifier.py)
- [`tests/test_star2_bernstein_verifier.py`](source/tests/test_star2_bernstein_verifier.py)
- [`tests/test_q3_verifier.py`](source/tests/test_q3_verifier.py)
- [`tests/test_nonstar1_json_failclosed.py`](source/tests/test_nonstar1_json_failclosed.py)
- [`audit/independent_referee/test_parser_failclosed.py`](source/audit/independent_referee/test_parser_failclosed.py)
- [`src/verify_star2_bernstein.py`](source/src/verify_star2_bernstein.py)
- [`src/verify_empty_highpair_classification.py`](source/src/verify_empty_highpair_classification.py)
- [`src/verify_q3_classification.py`](source/src/verify_q3_classification.py)
- [`src/verify_triangle_highpair_no_go.py`](source/src/verify_triangle_highpair_no_go.py)
- [`src/verify_all.py`](source/src/verify_all.py)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-AF03-P14/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
