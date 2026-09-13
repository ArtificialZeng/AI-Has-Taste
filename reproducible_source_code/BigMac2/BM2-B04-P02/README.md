# BM2-B04-P02 — reproduction source and evidence

Strict Positive Square Energy for Two-Connected Noncycle Graphs

[Final PDF](../../../pdfs/BigMac2/BM2-B04-P02_Strict_Positive_Square_Energy_for_Two_Connected_Noncycle_Graphs.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B04-P02/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For every finite simple undirected graph G of order n, if G is 2-connected and is not isomorphic to the cycle C_n, then s^+(G)>n. Consequently, there is no 2-connected noncycle G satisfying s^+(G)=|V(G)|, so the equality class requested in source.md is empty.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 9 scientific source/evidence files, including 1 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B04-P02 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: mpmath, networkx, sympy. The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/enumerate_n4_n8.py`](source/evidence/enumerate_n4_n8.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B04-P02/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B04-P02/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: No short positive exact checker selected; see archived source/proof dossier. Full n=4..8 biconnected census invokes geng plus high-precision spectral computations; not a small smoke test. Dependencies: nauty geng, NetworkX, mpmath, SymPy.

<!-- END PACKAGING REPLAY -->
