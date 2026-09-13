# BM2-B12-P02 — reproduction source and evidence

An Exact Type D4 Alternating Normal Form and Condition A for All Garside Powers

[Final PDF](../../../pdfs/BigMac2/BM2-B12-P02_An_Exact_Type_D4_Alternating_Normal_Form_and_Condition_A_for_All_Garside_Powers.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B12-P02/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. In the spherical Artin monoid of type D_4 with S_1={sigma'_0,sigma_1} and S_2={sigma_0,sigma_1,sigma_2}, the (S_2,S_1)-alternating normal form of the standard Garside element is (sigma_2 sigma_0, sigma_1 sigma'_0, sigma_0 sigma_1 sigma_2 sigma_1 sigma_0, sigma'_0 sigma_1 sigma'_0). Hence L*(Delta,S)={sigma_0,sigma_2}=Phi_Delta(S_2 boxminus S_1), and for every p,t>=1, dpt(Delta^(pt))-1=t(dpt(Delta^p)-1); equivalently, the covering satisfies Condition A with respect to every Delta^p.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 9 scientific source/evidence files, including 2 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B12-P02 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/referee_d4_check.py`](source/audit/referee_d4_check.py)
- [`evidence/verify_d4_alternating.py`](source/evidence/verify_d4_alternating.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B12-P02/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B12-P02/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/verify_d4_alternating.py
```

<!-- END PACKAGING REPLAY -->
