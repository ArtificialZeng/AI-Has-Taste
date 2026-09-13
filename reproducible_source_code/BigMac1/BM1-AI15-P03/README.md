# BM1-AI15-P03

The proper three-colouring zero set of generalized chorded cycles is {7,8,12,16}

Original ID: `af15_03_a383733_zero_set`. Batch: 历史第02批（AI15，2026-08-28/29）.

[Final PDF](../../../pdfs/BigMac1/BM1-AI15-P03_The_proper_three_colouring_zero_set_of_generalized_chorded_cycles_is_7_8_12_16.pdf) · [Archive catalog](../../../README.md#bigmac1) · [Gate provenance](../../../assets/BigMac1/gates/BM1-AI15-P03/review.json)

## Mathematical scope

Complete claimed zero-set theorem: generalized chorded cycles lack proper three-colourings exactly at n in {7,8,12,16}.

Historical submission gates reviewed; no fresh proof, citation or novelty audit in this packaging task.

## Reproduction coverage

**Archived code and exact evidence; full mathematical computations not rerun during packaging.**

This directory contains 40 selected source/evidence files, including 8 code/script files. Source preservation is not a claim that every archived wrapper runs without external dependencies. The packaging review checks bytes and Python syntax, not the truth of all mathematical claims.

## Archived instructions and dependencies

- [`verifier/README.md`](source/verifier/README.md)
- [`release/frozen/README.md`](source/release/frozen/README.md)

## Selected verifier / program entry points

Read each program before running it; some files are search tools or adversarial negative tests, not positive proof validators. Run from the working directory specified by its archived instructions. Large computations have not been restarted by the packaging process.

- [`certificates/verify_builder_construction.py`](source/certificates/verify_builder_construction.py)
- [`release/frozen/verify_static_manifest.py`](source/release/frozen/verify_static_manifest.py)
- [`verification/test_primary_fail_closed.py`](source/verification/test_primary_fail_closed.py)
- [`verification/verify_transfer_automata.py`](source/verification/verify_transfer_automata.py)
- [`verifier/verify_zero_set.py`](source/verifier/verify_zero_set.py)

## Portability and manifests

- The new [package manifest](../../../assets/BigMac1/package-manifest.json) binds the actual copied subset.
- Historical manifests, audit records and release wrappers inside `source/` are provenance. They can bind omitted PDFs, upstream downloads, binaries or machine-specific paths; they are **not** automatically valid manifests for this reorganized subset. Do not suppress missing-input checks or treat them as a pass.
- Executable binaries, environments, browser/account files, third-party paper downloads, render caches and duplicate manuscript PDFs are omitted. Rebuild external tools locally where needed; obey their upstream licenses.
- Historical source files may retain absolute paths in audit metadata or old execution helpers. Those paths are not portable instructions. Prefer the relative code/certificate interfaces and document any adaptation.
- The definitive manuscript PDF is linked above. Rebuilding or rerunning research does not silently replace it.

LaTeX is retained locally, not uploaded. [Git upload policy](../../../UPLOAD_GUIDE.md) · [Omitted file inventory](../../../assets/BigMac1/gates/BM1-AI15-P03/omitted-files.json)

[Known dependency and wrapper limitations / 已知复现限制](../../../assets/BigMac1/REPRODUCTION_NOTES.md). Use Python 3.12+ for full archived Python syntax coverage.
