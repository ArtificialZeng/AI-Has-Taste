# BM2-B22-P01 — reproduction source and evidence

The Sharp Queried-Gradient Constant of Nesterov's Fast Gradient Method at Horizon Two

[Final PDF](../../../pdfs/BigMac2/BM2-B22-P01_The_Sharp_Queried_Gradient_Constant_of_Nesterov_s_Fast_Gradient_Method_at_Horizon_Two.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B22-P01/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For every integer d >= 1, every L > 0, and every R >= 0, the horizon-two queried-gradient performance of the FGM recurrence frozen in source.md satisfies W_2(L,R,d) = c_2^2 L^2 R^2, where c_2 = 1/(3+beta) and beta = (sqrt(5)-1)/(1+sqrt(7+2sqrt(5))).

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 11 scientific source/evidence files, including 5 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B22-P01 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: cvxpy, numpy, scipy, sympy. The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/referee_recheck.py`](source/audit/referee_recheck.py)
- [`evidence/dual_search.py`](source/evidence/dual_search.py)
- [`evidence/full_dual_search.py`](source/evidence/full_dual_search.py)
- [`evidence/pep_sdp.py`](source/evidence/pep_sdp.py)
- [`evidence/verify_exact_dual.py`](source/evidence/verify_exact_dual.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B22-P01/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B22-P01/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Exact verifier has no numerical dependencies; optional SDP discovery uses NumPy/SciPy/CVXPY/SymPy. Do not treat SDP solver success as proof.

```sh
python3 evidence/verify_exact_dual.py
```

<!-- END PACKAGING REPLAY -->
