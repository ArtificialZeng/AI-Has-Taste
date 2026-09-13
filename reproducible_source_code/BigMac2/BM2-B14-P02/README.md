# BM2-B14-P02 — reproduction source and evidence

Fixed Sticky Refreshing Preserves the Exponent-Two Degree Laws in Range-Renewal Networks

[Final PDF](../../../pdfs/BigMac2/BM2-B14-P02_Fixed_Sticky_Refreshing_Preserves_the_Exponent_Two_Degree_Laws_in_Range_Renewal_Networks.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B14-P02/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. Let pi=(pi_i) be a nonincreasing strictly positive probability mass function with pi_k in RV_{-1/gamma} for some 0<gamma<1. For every fixed rho in [0,1), construct the stationary sticky-refresh sequence by retaining the current label with probability rho and otherwise drawing independently from pi. Form the directed and undirected loop-deleted simple graphs from consecutive observations, suppress repeated edges, and normalize degree counts by the observed range as in source.md and problem.md. Then, almost surely, simultaneously for every fixed integer k>=1, the four clock-time limits of the directed and undirected degree-k masses and degree-at-least-k tails equal the corresponding iid limits. Taking k to infinity only after each clock-time limit, the directed and undirected tails are asymptotic to pi_k^gamma and 2^gamma pi_k^gamma, respectively, while the directed and undirected local masses are asymptotic to pi_k^gamma/k and 2^gamma pi_k^gamma/k, respectively. Thus both local laws have exponent two, the undirected-to-directed amplitude ratio is 2^gamma, and no rho-dependent factor remains. No simultaneous k=k(n) limit or uniform rho-to-one assertion is included.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 6 scientific source/evidence files, including 0 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B14-P02 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- No standalone program was archived; the mathematical proof/evidence is supplied below.

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B14-P02/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B14-P02/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: No short positive exact checker selected; see archived source/proof dossier. No code archived; mathematical proof is the manuscript and proof dossier.

<!-- END PACKAGING REPLAY -->
