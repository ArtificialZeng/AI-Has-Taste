# BM2-B26-P03 — reproduction source and evidence

The Weak-EKR Difference-Set Condition for Irreducible Subgroups of GL(3,2)

[Final PDF](../../../pdfs/BigMac2/BM2-B26-P03_The_Weak_EKR_Difference_Set_Condition_for_Irreducible_Subgroups_of_GL_3_2.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B26-P03/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. Let V=F_2^3 and G=GL(3,2). Up to conjugacy in G, the irreducible subgroups L<=G are exactly three classes, of orders 7, 21, and 168, represented by the explicit matrix generators in evidence/result.md. For each of these three representatives, the universal property P(L) in problem.md is false: with W=span{(1,0,0)} and A={(0,0,0),(1,0,0),(0,1,0)}, one has union_{ell in L} W^ell=V, hence A-A is contained in that union, while |A|=3>2=|W|. Thus no irreducible subgroup of GL(3,2) satisfies the frozen implication.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 13 scientific source/evidence files, including 3 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (1 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B26-P03 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/enumerate_gl32_subgroups.py`](source/evidence/enumerate_gl32_subgroups.py)
- [`evidence/test_weak_ekr.py`](source/evidence/test_weak_ekr.py)
- [`evidence/verify_certificates.py`](source/evidence/verify_certificates.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B26-P03/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B26-P03/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: Default verifier exhausts subgroup saturation/conjugacy coverage; retained for full user-driven replay, not short smoke. Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/verify_certificates.py --subgroups evidence/gl32_subgroup_irreducibility.json --weak-ekr evidence/gl32_weak_ekr_classification.json --output replay-packaging.json
```

<!-- END PACKAGING REPLAY -->
