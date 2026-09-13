# BM1-AF04-P15

A Certified Finite Census for Additive-Square-Free Words on Four-Letter Integer Alphabets of Height at Most Five

Original ID: `af15b4_15_additive_square_infinite`. Batch: 原AI-friendly第04批.

[Final PDF](../../../pdfs/BigMac1/BM1-AF04-P15_A_Certified_Finite_Census_for_Additive_Square_Free_Words_on_Four_Letter_Integer_Alphabets_of_Height_at_Most_Five.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-AF04-P15/review.json)

## Mathematical scope

PDF为四字母高度≤5的7个规范字母表有限极值与受限2-uniform morphism no-go，不解决无限存在性；历史角色审计为串行，非本轮新上下文审计。

历史串行角色审计；非本次fresh审稿。

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 50 selected source/evidence files, including 8 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- [`release/README.md`](source/release/README.md)

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`certificates/verify_finite_census.py`](source/certificates/verify_finite_census.py)
- [`certificates/verify_uniform2_no_go.py`](source/certificates/verify_uniform2_no_go.py)
- [`tests/test_fail_closed.py`](source/tests/test_fail_closed.py)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-AF04-P15/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
