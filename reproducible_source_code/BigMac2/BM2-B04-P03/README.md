# BM2-B04-P03 — reproduction source and evidence

Exact Maximum Loneliness in the Family (1,4,5,6,7,m)

[Final PDF](../../../pdfs/BigMac2/BM2-B04-P03_Exact_Maximum_Loneliness_in_the_Family_1_4_5_6_7_m.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B04-P03/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For every positive integer m not in {1,4,5,6,7}, define L(m) and A(m) as in problem.md. If 11 does not divide m, then L(m)=2/11; for r=m mod 11, A(m)={4/11,7/11} when r is 2 or 9, A(m)={5/11,6/11} when r is 3 or 8, and A(m)={4/11,5/11,6/11,7/11} when r is in {1,4,5,6,7,10}. At m=11, L=2/13 and A={4/13,9/13}. At m=22, L=2/13 and A={4/13,6/13,7/13,9/13}. If m=11n with n>=3, then L(m)=2n/(11n+4) and A(m)={(5n+2)/(11n+4),(6n+2)/(11n+4)}. Consequently, the parameters satisfying the strict inequalities 1/7<L(m)<1/6 are exactly {11,22,33}.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 8 scientific source/evidence files, including 2 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B04-P03 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/triage_exact_scan.py`](source/evidence/triage_exact_scan.py)
- [`evidence/verify_family_formula.py`](source/evidence/verify_family_formula.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B04-P03/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B04-P03/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/verify_family_formula.py
```

<!-- END PACKAGING REPLAY -->
