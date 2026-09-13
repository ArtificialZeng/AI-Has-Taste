# BM2-B27-P02 — reproduction source and evidence

The Three-Neighbor Percolation Number of the 8 by 8 Torus

[Final PDF](../../../pdfs/BigMac2/BM2-B27-P02_The_Three_Neighbor_Percolation_Number_of_the_8_by_8_Torus.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B27-P02/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For the simple torus G=C_8 square C_8 and the synchronous three-neighbor process defined in source.md and problem.md, t_3(8,8)=22. The 22-element set and all exact synchronous infection layers are frozen in evidence/22-set-certificate.json; every percolating set has size at least 22 by the induced-forest degree count in evidence/proof.md.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging. Some historical wrappers contain machine-specific paths; see the per-package instructions before replay.

The package contains 9 scientific source/evidence files, including 2 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B27-P02 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: networkx, numpy, scipy. The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/search_22.py`](source/evidence/search_22.py)
- [`evidence/verify_22.py`](source/evidence/verify_22.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- `evidence/verify_22.py` (lines 5)

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B27-P02/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B27-P02/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/verify_22.py
```

<!-- END PACKAGING REPLAY -->
