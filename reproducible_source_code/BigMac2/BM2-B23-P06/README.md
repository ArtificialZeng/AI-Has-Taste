# BM2-B23-P06 — reproduction source and evidence

An Exact Computer-Assisted Perfectness Census for Integral Circulant Graphs Through Order 32

[Final PDF](../../../pdfs/BigMac2/BM2-B23-P06_An_Exact_Computer_Assisted_Perfectness_Census_for_Integral_Circulant_Graphs_Through_Order_32.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B23-P06/packaging-review.json)

## Mathematical scope

Partial result; original problem unresolved. For every integer n with 1 <= n <= 32 and every subset D of the strict positive divisors D_n, the canonical records in evidence/n32_manifest.json (records SHA-256 fe36f96a628851b9ef03d912c8d9ec451e48d4c7773ab12626aa36a52610357e) give the exact perfectness classification of ICG_n(D): 415 of the 539 inputs are perfect and 124 are imperfect; imperfect inputs occur only for n in {12,20,24,28,30}, with the complete divisor-mask list stated in evidence/n32-result.md. Every imperfect record has an exactly replayed induced odd hole in the graph or complement, and every perfect record has an exhaustive exact two-sided odd-hole-search certificate whose completeness follows from translation symmetry. No claim is made for 33 <= n <= 64, so the frozen original problem remains unresolved.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 14 scientific source/evidence files, including 4 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (1 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B23-P06 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: networkx. The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/referee_subset_check.py`](source/audit/referee_subset_check.py)
- [`evidence/n32_census.py`](source/evidence/n32_census.py)
- [`evidence/networkx_crosscheck_n32.py`](source/evidence/networkx_crosscheck_n32.py)
- [`evidence/replay_n32.py`](source/evidence/replay_n32.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B23-P06/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B23-P06/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/replay_n32.py evidence/n32_manifest.json replay-packaging.json
```

<!-- END PACKAGING REPLAY -->
