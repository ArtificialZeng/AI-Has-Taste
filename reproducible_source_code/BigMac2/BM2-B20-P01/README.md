# BM2-B20-P01 — reproduction source and evidence

A Three-Dimensional Counterexample to a Split-Ideal Question

[Final PDF](../../../pdfs/BigMac2/BM2-B20-P01_A_Three_Dimensional_Counterexample_to_a_Split_Ideal_Question.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B20-P01/packaging-review.json)

## Mathematical scope

Disproof of the frozen original statement. For every field k, let A = k × k[ε]/(ε²) with A_0 = {(a,b): a,b ∈ k}, A_1 = {(0,cε): c ∈ k}, and A_i = 0 for i ≥ 2, and let J = k × 0. Then A is a standard graded, locally finite, semiconnected unital k-algebra, J is a two-sided ideal, and dim_k(A/J) = 2 = dim_k(A_0), but the natural map A_0 → A/J has kernel k × 0 and is not an isomorphism. Therefore the universal assertion in source.md is false and Question 6.1 under the precise reading in problem.md has a negative answer.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 6 scientific source/evidence files, including 0 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B20-P01 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- No standalone program was archived; the mathematical proof/evidence is supplied below.

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B20-P01/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B20-P01/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: No short positive exact checker selected; see archived source/proof dossier. No code archived; mathematical proof is the manuscript and proof dossier.

<!-- END PACKAGING REPLAY -->
