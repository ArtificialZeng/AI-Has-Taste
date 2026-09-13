# BM2-B16-P02 — reproduction source and evidence

Exact Homological Invariants for Closed-Neighborhood Ideals of Cubes of Broom Graphs

[Final PDF](../../../pdfs/BigMac2/BM2-B16-P02_Exact_Homological_Invariants_for_Closed_Neighborhood_Ideals_of_Cubes_of_Broom_Graphs.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B16-P02/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For every field K and all integers n,m>=2, if I_{n,m}=NI(B(n,m)^3) is the closed-neighborhood ideal defined in source.md and interpreted in problem.md, then pd_S(S/I_{n,m})=floor(m/4)+1, reg_S(S/I_{n,m})=n+m-1-floor(m/4), and ht(I_{n,m})=floor(m/7)+1. Consequently S/I_{n,m} is Cohen--Macaulay exactly when m is 2, 3, or 7 (for every n>=2). There are no exceptional small-m values outside these uniform formulas.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging. Some historical wrappers contain machine-specific paths; see the per-package instructions before replay.

The package contains 8 scientific source/evidence files, including 1 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (1 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B16-P02 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/compute_exact_table.py`](source/evidence/compute_exact_table.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- `evidence/compute_exact_table.py` (lines 130)

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B16-P02/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B16-P02/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: No short positive exact checker selected; see archived source/proof dossier. Requires external Singular; supports --singular PATH. Full table default uses /opt/homebrew/bin/Singular. Preserve generated Singular inputs/results; computation is finite evidence, not a new proof.

<!-- END PACKAGING REPLAY -->
