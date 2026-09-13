# BM2-B15-P01 — reproduction source and evidence

Exact Joint ANF Leap for Raw Finite-Field Inversion

[Final PDF](../../../pdfs/BigMac2/BM2-B15-P01_Exact_Joint_ANF_Leap_for_Raw_Finite_Field_Inversion.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B15-P01/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For every integer n >= 2 and every monic irreducible degree-n polynomial p over F_2, let F=F_2[t]/(p), use the polynomial coordinate basis (1,t,...,t^(n-1)), and let J_{n,p} be field inversion in coordinates with J_{n,p}(0)=0. For every P in Mat_n(F_2), including singular P, and u in F_2^n, set G(P,u)=adj(P)J_{n,p}(Pu), with adj(P)_{ab} equal to the determinant after deleting row b and column a. Write the unique multilinear vector ANF as G=XOR_{A subset V} c_A product_{v in A}v on the n^2+n matrix-entry and operand variables V, let S={A:c_A is nonzero}, and define L(G)=min over orderings (A_1,...,A_s) of S of max_j |A_j minus union_{i<j}A_i|. Then L(G)=n.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 14 scientific source/evidence files, including 2 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B15-P01 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/referee_verify.py`](source/audit/referee_verify.py)
- [`evidence/exact_triage.py`](source/evidence/exact_triage.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B15-P01/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B15-P01/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/exact_triage.py
```

<!-- END PACKAGING REPLAY -->
