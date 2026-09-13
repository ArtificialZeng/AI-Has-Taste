# BM1-MAN-P03

Exact finite certificates for the four-dimensional ternary Borsuk problem and five-dimensional ternary kissing codes

Original ID: `DMAC1-MAN-borsuk`. Batch: 手工课题（2026-08）.

[Final PDF](../../../pdfs/BigMac1/BM1-MAN-P03_Exact_finite_certificates_for_the_four_dimensional_ternary_Borsuk_problem_and_five_dimensional_ternary_kissing_codes.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-MAN-P03/review.json)

## Mathematical scope

One joint finite-library paper: ternary four-cube Borsuk maximum 4 and normalized ternary five-dimensional kissing maximum 40 with unique weight-two maximum; unrestricted Borsuk minimum dimension and kissing numbers in dimensions 5/6 remain open. Kissing row merged here.

Historical submission gates reviewed; no fresh proof, citation or novelty audit in this packaging task.

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 14 selected source/evidence files, including 5 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- See the verifier/script index below and its inline usage comments.

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`code/run_all_verifiers.py`](source/code/run_all_verifiers.py)
- [`code/verify_borsuk_ternary4.py`](source/code/verify_borsuk_ternary4.py)
- [`code/verify_kissing_ternary5.py`](source/code/verify_kissing_ternary5.py)
- [`code/verify_kissing_ternary5_independent.py`](source/code/verify_kissing_ternary5_independent.py)
- [`code/verify_known_kissing_constructions.py`](source/code/verify_known_kissing_constructions.py)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-MAN-P03/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
