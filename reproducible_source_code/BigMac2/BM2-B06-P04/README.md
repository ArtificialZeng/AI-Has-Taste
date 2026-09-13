# BM2-B06-P04 — reproduction source and evidence

A Product Formula and All-Degree Positivity for the (6,(0,1))-Core Bipartition Series

[Final PDF](../../../pdfs/BigMac2/BM2-B06-P04_A_Product_Formula_and_All_Degree_Positivity_for_the_6_0_1_Core_Bipartition_Series.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B06-P04/packaging-review.json)

## Mathematical scope

Partial result; original problem unresolved. Under the charged-bipartition and (e,s)-core definitions fixed in problem.md, for every integer n >= 0 one has [q^n] c_{6,(0,1)}(q) > 0. More precisely, c_{6,(0,1)}(q) = (q^2;q^2)_infinity^3 (q^6;q^6)_infinity^2 (q^12;q^12)_infinity^2 / (q;q)_infinity^2 = psi(q)^2 c_3(q^2) psi(q^6). No assertion is made that the (0,3) branch is proved; the original conjunction remains unresolved.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 16 scientific source/evidence files, including 4 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B06-P04 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/certify_sturm.py`](source/evidence/certify_sturm.py)
- [`evidence/check_factorization.py`](source/evidence/check_factorization.py)
- [`evidence/enumerate_series.py`](source/evidence/enumerate_series.py)
- [`evidence/independent_theta_audit.py`](source/evidence/independent_theta_audit.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B06-P04/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B06-P04/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/independent_theta_audit.py
```

<!-- END PACKAGING REPLAY -->
