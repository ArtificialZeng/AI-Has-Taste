# BM2-B27-P03 — reproduction source and evidence

No Weak Abelian Square of Total Length at Most 2745 in a Proposed Five-Letter Cyclic Morphic Word

[Final PDF](../../../pdfs/BigMac2/BM2-B27-P03_No_Weak_Abelian_Square_of_Total_Length_at_Most_2745_in_a_Proposed_Five_Letter_Cyclic_Morphic_Word.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B27-P03/packaging-review.json)

## Mathematical scope

Partial result; original problem unresolved. For the fixed point w=h^omega(0) defined in source.md, for every s in N_0 and all positive m,n with m+n <= 2745, n Psi(w_s...w_{s+m-1}) is not equal to m Psi(w_{s+m}...w_{s+m+n-1}). Consequently, if the frozen claim (C) is false, every counterexample has total length m+n >= 2746.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging. Some historical wrappers contain machine-specific paths; see the per-package instructions before replay.

The package contains 11 scientific source/evidence files, including 3 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B27-P03 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/exhaustive_h3.py`](source/evidence/exhaustive_h3.py)
- [`evidence/exhaustive_h4.cpp`](source/evidence/exhaustive_h4.cpp)
- [`evidence/verify_h4_certificate.py`](source/evidence/verify_h4_certificate.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- `evidence/exhaustive_h3.py` (lines 1)
- `evidence/verify_h4_certificate.py` (lines 1)

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B27-P03/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B27-P03/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; verify_h4_certificate.py checks metadata/counts/word digests and representative bounds only. It expressly does NOT repeat the1.48-billion-signature C++ sweep; label coverage accurately.

```sh
python3 evidence/verify_h4_certificate.py
```

<!-- END PACKAGING REPLAY -->
