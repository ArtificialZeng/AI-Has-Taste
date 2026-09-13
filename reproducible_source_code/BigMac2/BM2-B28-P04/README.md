# BM2-B28-P04 — reproduction source and evidence

The Exact Label-Realization Radius nu(4,4)

[Final PDF](../../../pdfs/BigMac2/BM2-B28-P04_The_Exact_Label_Realization_Radius_nu_4_4.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B28-P04/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. Under Shin's label-level definition nu(h,4)=min{D>=0: R_D(h,4)=R(h,4)} with four-subsets of the literal interval [0,D], the exact value is nu(4,4)=15. Equivalently, R_15(4,4)=R(4,4), and 15 is minimal. The exhaustive spectra R_15(4,4) and R_16(4,4) both equal {13,16,17,19,21,23,24,25,26,27,29,30,31,32,33,34,35}.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 10 scientific source/evidence files, including 2 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B28-P04 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/coefficient_vector_recheck.py`](source/evidence/coefficient_vector_recheck.py)
- [`evidence/triage_enumeration.py`](source/evidence/triage_enumeration.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B28-P04/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B28-P04/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/coefficient_vector_recheck.py --output replay-packaging.json
```

<!-- END PACKAGING REPLAY -->
