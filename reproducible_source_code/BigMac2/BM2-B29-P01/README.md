# BM2-B29-P01 — reproduction source and evidence

Exact Rational Certificates for the Reverse LCD–LP Comparison at (20,8)

[Final PDF](../../../pdfs/BigMac2/BM2-B29-P01_Exact_Rational_Certificates_for_the_Reverse_LCDLP_Comparison_at_20_8.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B29-P01/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For the exact binary Gauss-phase and mixed joint-weight-enumerator LP systems frozen in source.md and interpreted in problem.md, all three assertions hold: G_2(20,8,7) is nonempty, M_2(20,8,7) is empty, and M_2(20,8,6) is nonempty. The Gauss nonemptiness is witnessed in the admissible (tau,beta,eta)=(O,0,0) branch.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging. Some historical wrappers contain machine-specific paths; see the per-package instructions before replay.

The package contains 29 scientific source/evidence files, including 8 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (3 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B29-P01 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: highspy, numpy, scipy. The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/build_d7_dyadic_farkas.py`](source/evidence/build_d7_dyadic_farkas.py)
- [`evidence/build_primal_certificates.py`](source/evidence/build_primal_certificates.py)
- [`evidence/export_d6_basis.py`](source/evidence/export_d6_basis.py)
- [`evidence/mixed_d7_farkas_search.py`](source/evidence/mixed_d7_farkas_search.py)
- [`evidence/mixed_lp_search.py`](source/evidence/mixed_lp_search.py)
- [`evidence/solve_basis_flint.c`](source/evidence/solve_basis_flint.c)
- [`evidence/verify_d7_farkas_independent.py`](source/evidence/verify_d7_farkas_independent.py)
- [`evidence/verify_primal_certificates_independent.py`](source/evidence/verify_primal_certificates_independent.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- `evidence/build_d7_dyadic_farkas.py` (lines 1)
- `evidence/build_primal_certificates.py` (lines 1)
- `evidence/export_d6_basis.py` (lines 1)
- `evidence/mixed_d7_farkas_search.py` (lines 1)
- `evidence/mixed_lp_search.py` (lines 1)
- `evidence/verify_d7_farkas_independent.py` (lines 1)
- `evidence/verify_primal_certificates_independent.py` (lines 1)

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B29-P01/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B29-P01/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: Reconstructs1771x1771 Hadamard transform and large exact Farkas sums; retained for full user-driven replay, not short smoke. Independent Farkas/primal verifier uses NumPy, exact integer/Fraction arithmetic, reconstructs1771x1771 transform; bounded timeout may be exceeded. Primal checker imports local verify_d7_farkas_independent.py. Optional discovery: highspy/NumPy/SciPy; solve_basis_flint.c needs FLINT (-lflint,with local compiler/header flags).

```sh
python3 evidence/verify_d7_farkas_independent.py
```

<!-- END PACKAGING REPLAY -->
