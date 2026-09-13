# BM1-AF04-P10

Certified radius-seven exchange rigidity for a binary subspace code

Original ID: `af15b4_10_subspace_code_a2_7_4`. Batch: 原AI-friendly第04批.

[Final PDF](../../../pdfs/BigMac1/BM1-AF04-P10_Certified_radius_seven_exchange_rigidity_for_a_binary_subspace_code.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-AF04-P10/review.json)

## Mathematical scope

PDF只证明指定333-plane code 删除至多7个平面的交换邻域精确最大值334；不是 A2(7,4) 全局解答，历史全局边界334–388。

历史审计；非本次fresh审稿。

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 22 selected source/evidence files, including 4 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- [`release/README.md`](source/release/README.md)

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`verification/verify_radius6.py`](source/verification/verify_radius6.py)
- [`tests/test_fail_closed.py`](source/tests/test_fail_closed.py)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-AF04-P10/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
