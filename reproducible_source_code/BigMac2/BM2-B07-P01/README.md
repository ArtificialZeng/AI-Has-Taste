# BM2-B07-P01 — reproduction source and evidence

Pure Periodicity for the Three-Move Subtraction Games {2,5,c}

[Final PDF](../../../pdfs/BigMac2/BM2-B07-P01_Pure_Periodicity_for_the_Three_Move_Subtraction_Games_2_5_c.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B07-P01/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For every integer c>5 with c!=7, the full wall-convention Sprague--Grundy sequence of S={2,5,c} is purely periodic from n=0 if and only if c mod 7 lies in Theta_7 union Theta_{c+2} union Theta_{c+5}, where Manabe's source predicates specialize to Theta_7={2,5}, Theta_{c+2}={1,5}, and Theta_{c+5}={2,3,6}. Equivalently, pure periodicity holds exactly for residues {1,2,3,5,6}. In those cases the least period is c+2 for residue 1, 7 for residues 2 and 5, and c+5 for residues 3 and 6, with no proper-divisor exception for this primitive non-harmonic shape. For the excluded residues, exact full-nim word formulae prove non-pure periodicity: if c=7k+4 then G=B^k E (A C^{k-1} D)^omega, and if c=7k then G=B^k F (H^{k-1} I J)^omega, with the blocks defined in evidence/fixed_shape_proof.md.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 9 scientific source/evidence files, including 2 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B07-P01 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/fixed_shape_certificate.py`](source/evidence/fixed_shape_certificate.py)
- [`evidence/triage_scan.py`](source/evidence/triage_scan.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B07-P01/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B07-P01/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Suggested max-k20 is an explicitly REDUCED smoke test, not replay of every archived default-k200 instance nor proof of the all-k formula.

```sh
python3 evidence/fixed_shape_certificate.py --max-k 20
```

<!-- END PACKAGING REPLAY -->
