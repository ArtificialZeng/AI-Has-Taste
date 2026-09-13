# BM2-B24-P02 — reproduction source and evidence

The Exact Minimax Two-Step Schedule for Smooth Convex Gradient Descent

[Final PDF](../../../pdfs/BigMac2/BM2-B24-P02_The_Exact_Minimax_Two_Step_Schedule_for_Smooth_Convex_Gradient_Descent.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B24-P02/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For every L>0, inf_{eta_1,eta_2>0} R_2^L(eta_1,eta_2) = 1/(5+4*sqrt(2)+sqrt(9+8*sqrt(2))), with attainment by the ordered normalized schedule (L eta_1,L eta_2)=(sqrt(2),(3+sqrt(9+8*sqrt(2)))/4). No uniqueness is asserted.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 10 scientific source/evidence files, including 3 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B24-P02 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: numpy, scipy, sympy. The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/referee_verify.py`](source/audit/referee_verify.py)
- [`evidence/exact_resolution_verify.py`](source/evidence/exact_resolution_verify.py)
- [`evidence/pep_four_sample.py`](source/evidence/pep_four_sample.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B24-P02/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B24-P02/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Exact-resolution verifier distinct from NumPy/SciPy numerical PEP discovery; smoke check does not replace analytic quantified case argument.

```sh
python3 evidence/exact_resolution_verify.py
```

<!-- END PACKAGING REPLAY -->
