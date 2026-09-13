# BM2-B25-P01 — reproduction source and evidence

Nonexistence of a Four-Layer Balanced Hamilton Starter in Cay(Z₁₂,{1,2,3})

[Final PDF](../../../pdfs/BigMac2/BM2-B25-P01_Nonexistence_of_a_Four_Layer_Balanced_Hamilton_Starter_in_Cay_Z12_1_2_3.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B25-P01/packaging-review.json)

## Mathematical scope

Disproof of the frozen original statement. For C_4(3)=Cay(Z_12,{1,2,3}) with four-layer balance as frozen in problem.md, no four-layer balanced directed Hamilton cycle exists. Consequently there are no such H and permutation pi in S_3 for which 0->2, 2->4, and 4->6 lie in three distinct developed translates H, H+4, H+8; the original existential question has a negative answer.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 11 scientific source/evidence files, including 4 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B25-P01 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/referee_recompute.py`](source/audit/referee_recompute.py)
- [`evidence/crosscheck.py`](source/evidence/crosscheck.py)
- [`evidence/enumerate_balanced.py`](source/evidence/enumerate_balanced.py)
- [`evidence/enumerate_replay.py`](source/evidence/enumerate_replay.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B25-P01/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B25-P01/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; 3^12 enumeration is finite but may exceed20 seconds depending on implementation/hardware; enforce timeout and label timeout, not failure of the theorem.

```sh
python3 audit/referee_recompute.py
```

<!-- END PACKAGING REPLAY -->
