# BM2-B11-P03 — reproduction source and evidence

The independent-row K(2,2) molecular species product

[Final PDF](../../../pdfs/BigMac2/BM2-B11-P03_The_independent_row_K_2_2_molecular_species_product.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B11-P03/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. Under the independent-row convention frozen in problem.md, with H=< (12),(34) > isomorphic to C_2^2 and K_lambda=X^4/G_lambda, there is a natural isomorphism of species K_(2,2) x K_(2,2) ~= K_(2,2) coproduct K_(2,2) coproduct K_(1,1,1,1). Hence the coefficient vector in the partition order (4),(3,1),(2,2),(2,1,1),(1,1,1,1) is (0,0,2,0,1). The five displayed species are integrally linearly independent, so the expansion is unique; separately, their five cycle indices are also integrally linearly independent.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 9 scientific source/evidence files, including 1 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B11-P03 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/s4_certificate.py`](source/evidence/s4_certificate.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B11-P03/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B11-P03/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/s4_certificate.py
```

<!-- END PACKAGING REPLAY -->
