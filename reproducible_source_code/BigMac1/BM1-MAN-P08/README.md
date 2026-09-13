# BM1-MAN-P08

Integer-Floor Lifting for Frankl-Complete Uniform Configurations

Original ID: `DMAC1-MAN-unionclosed`. Batch: 手工课题（2026-08）.

[Final PDF](../../../pdfs/BigMac1/BM1-MAN-P08_Integer_Floor_Lifting_for_Frankl_Complete_Uniform_Configurations.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-MAN-P08/review.json)

## Mathematical scope

Partial theorems on integer-floor lifting for Frankl-complete uniform configurations; fixed-power weighting no-go and exact five-point census. Frankl's full conjecture remains open; novelty only bounded searched nonfinding.

Historical submission gates reviewed; no fresh proof, citation or novelty audit in this packaging task.

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 19 selected source/evidence files, including 9 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- See the verifier/script index below and its inline usage comments.

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`src/verify_fc_deletion_lift.py`](source/src/verify_fc_deletion_lift.py)
- [`src/verify_power_chain_no_go.py`](source/src/verify_power_chain_no_go.py)
- [`src/verify_small_union_closed.py`](source/src/verify_small_union_closed.py)
- [`tests/run_all_fast.sh`](source/tests/run_all_fast.sh)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-MAN-P08/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
