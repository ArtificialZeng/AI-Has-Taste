# BM2-B25-P03 — reproduction source and evidence

Cross-part rainbow near-perfect matchings in the nine-element affine plane: an exact finite proof

[Final PDF](../../../pdfs/BigMac2/BM2-B25-P03_Cross_part_rainbow_near_perfect_matchings_in_the_nine_element_affine_plane_an_exact_finite_proof.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B25-P03/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. Let G = F_3^2 under componentwise addition. For every partition G = A dot-union B with part sizes 4 and 5, after naming the four-element part A there exist four pairwise vertex-disjoint cross edges {a_i,b_i}, one incident with each a_i in A, such that the multiset of their two oriented differences is exactly G minus {(0,0)}; equivalently, their four unoriented differences are the four antipodal nonzero direction classes exactly once.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging. Some historical wrappers contain machine-specific paths; see the per-package instructions before replay.

The package contains 10 scientific source/evidence files, including 2 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B25-P03 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/exhaustive_search.py`](source/evidence/exhaustive_search.py)
- [`evidence/independent_verify.py`](source/evidence/independent_verify.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- `evidence/exhaustive_search.py` (lines 1)
- `evidence/independent_verify.py` (lines 1)

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B25-P03/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B25-P03/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/independent_verify.py evidence/exhaustive_certificate.json --report replay-packaging.json
```

<!-- END PACKAGING REPLAY -->
