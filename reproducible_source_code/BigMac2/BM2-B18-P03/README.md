# BM2-B18-P03 — reproduction source and evidence

The Three-Halves Endpoint Remainder for a Truncated Gaussian Heat Kernel

[Final PDF](../../../pdfs/BigMac2/BM2-B18-P03_The_Three_Halves_Endpoint_Remainder_for_a_Truncated_Gaussian_Heat_Kernel.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B18-P03/packaging-review.json)

## Mathematical scope

Disproof of the frozen original statement. For the exact Gaussian truncated heat-kernel operator in source.md, let lambda(u) be its largest eigenvalue, Phi(u)=log(lambda(u)), and A=pi^2/4. There exist constants c,C,u_0>0 such that c*u^(3/2) <= Phi(u)+A*u <= C*u^(3/2) for every 0<u<u_0. Consequently 2[Phi(u)+A*u]/u^2 tends to +infinity, and the finite classical right second derivative lim_{u downarrow 0}[Phi'(u)+A]/u does not exist. The correct pure-power scale of the signed first-order remainder is u^(3/2); no exact coefficient for the optimized eigenvalue remainder is claimed.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 8 scientific source/evidence files, including 1 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B18-P03 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/numerical_sanity.py`](source/evidence/numerical_sanity.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B18-P03/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B18-P03/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: No short positive exact checker selected; see archived source/proof dossier. Archived numerical_sanity.py is explicitly floating-point sanity only; no exact replay interface is claimed.

<!-- END PACKAGING REPLAY -->
