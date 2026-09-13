# BM2-B27-P04 — reproduction source and evidence

Regular Distance-Magic Graphs on Eight Vertices and Generating F2-Cubed Magic Maps

[Final PDF](../../../pdfs/BigMac2/BM2-B27-P04_Regular_Distance_Magic_Graphs_on_Eight_Vertices_and_Generating_F2_Cubed_Magic_Maps.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B27-P04/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. Among finite simple undirected regular ordinary distance-magic graphs on exactly eight vertices, with disconnected graphs and degree zero allowed, there are exactly four isomorphism classes: 8K1, 2C4, K4,4, and K2,2,2,2. Their reduced adjacency nullities over F_2 on F_2^8/<1> are respectively 7, 4, 6, and 4. Hence every graph in the frozen class admits a generating (Z/2Z)^3-magic map, so the universal assertion in source.md is true.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging. Some historical wrappers contain machine-specific paths; see the per-package instructions before replay.

The package contains 15 scientific source/evidence files, including 4 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B27-P04 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/referee_recheck.py`](source/audit/referee_recheck.py)
- [`evidence/enumerate_order8.py`](source/evidence/enumerate_order8.py)
- [`evidence/verify_order8_certificate.py`](source/evidence/verify_order8_certificate.py)
- [`evidence/verify_unlabeled_coverage.py`](source/evidence/verify_unlabeled_coverage.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- `audit/referee_recheck.py` (lines 1, 24)
- `evidence/enumerate_order8.py` (lines 1, 201)
- `evidence/verify_order8_certificate.py` (lines 1, 27, 37)
- `evidence/verify_unlabeled_coverage.py` (lines 1, 30)

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B27-P04/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B27-P04/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: No short positive exact checker selected; see archived source/proof dossier. All three evidence Python verifiers/producer and audit/referee_recheck.py enforce old absolute interpreter path. Evidence verify_order8_certificate.py also hardcodes /opt/homebrew/bin/showg. Do not classify original wrappers as portable or strip checks without disclosed patch provenance.

<!-- END PACKAGING REPLAY -->
