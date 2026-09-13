# BM2-B04-P01 — reproduction source and evidence

The Six-Point Type-II Bounded Ratio on Its Symmetric Locus, and Two Exact Obstructions

[Final PDF](../../../pdfs/BigMac2/BM2-B04-P01_The_Six_Point_Type_II_Bounded_Ratio_on_Its_Symmetric_Locus_and_Two_Exact_Obstructions.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B04-P01/packaging-review.json)

## Mathematical scope

Partial result; original problem unresolved. Let h=(-2,-1,1,1,1,1), q(h)_{ij}=h_i h_j, and alpha=q(h)/4. (i) On the full family of matrices in L^+_{6,1} invariant under permutations of indices 3,4,5,6, the supremum of P^alpha is exactly 8/(3 sqrt(3)), hence is strictly below 2. (ii) Entrywise geometric averaging over that permutation group does not preserve L^+_{6,1}: the explicit family P_r in the evidence has inertia (1,1,4), while its orbit-geometric average has inertia (2,4,0), and the type-II monomial is preserved with value 1. (iii) The inequality P^alpha<=2 cannot be derived by multiplying nonnegative real powers of all sharp lifted triangular and pentagonal inequalities together with p_ij>=1, even if the total normalized weight restriction is removed; the displayed integer functional Lambda exactly separates the target exponent from every generator of this proof cone.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 9 scientific source/evidence files, including 1 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B04-P01 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/check_typeII_product_dual.py`](source/evidence/check_typeII_product_dual.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B04-P01/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B04-P01/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/check_typeII_product_dual.py
```

<!-- END PACKAGING REPLAY -->
