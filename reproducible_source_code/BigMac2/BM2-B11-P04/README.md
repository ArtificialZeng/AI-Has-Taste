# BM2-B11-P04 — reproduction source and evidence

Sign Reversal and the Exact Zero Set for the Covariance of Competing Bulk and Surface Stopping in the Three-Ball

[Final PDF](../../../pdfs/BigMac2/BM2-B11-P04_Sign_Reversal_and_the_Exact_Zero_Set_for_the_Covariance_of_Competing_Bulk_and_Surface_Stopping_in_the_Three_Ball.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B11-P04/packaging-review.json)

## Mathematical scope

Disproof of the frozen original statement. For T and L defined in source.md and problem.md (unit three-ball, D=1, volume-uniform initial point, and independent Exp(p) bulk-time and Exp(q) boundary-local-time thresholds), set x=sqrt(p), A=x cosh(x)-sinh(x), and B=A+q sinh(x). For every p,q>0, Cov(T,L)=3[xi_1(p)+q xi_2(p)]/(4 x^6 B^2), with xi_1 and xi_2 exactly as in Appendix F. Moreover xi_1(p)>0 and xi_2(p)<0 for every p>0. Hence the complete positive-quadrant zero set is q=-xi_1(p)/xi_2(p), the covariance is positive below this graph and negative above it, and in particular Cov_{1,200}(T,L)<0. Thus the frozen universal positivity assertion is false.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 8 scientific source/evidence files, including 2 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B11-P04 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: sympy. The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/referee_verify.py`](source/audit/referee_verify.py)
- [`evidence/verify_symbolic.py`](source/evidence/verify_symbolic.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B11-P04/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B11-P04/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/verify_symbolic.py
```

<!-- END PACKAGING REPLAY -->
