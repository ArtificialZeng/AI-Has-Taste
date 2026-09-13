# BM2-B14-P01 — reproduction source and evidence

Exact Invertibility Probability for Binary Matrices with Two Ones in Every Row and Column

[Final PDF](../../../pdfs/BigMac2/BM2-B14-P01_Exact_Invertibility_Probability_for_Binary_Matrices_with_Two_Ones_in_Every_Row_and_Column.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B14-P01/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For every integer N>=2, let A_N be uniform on the set of binary N by N matrices with every row and column sum equal to two, allowing diagonal ones, and set p_N=P(det(A_N)!=0) over the real numbers. With D(z)=exp(-z/2)(1-z)^(-1/2) and H(z)=exp(-z/2)(1+z)^(1/4)(1-z)^(-1/4), using the branches defined by their formal series at zero, p_N=[z^N]H(z)/[z^N]D(z). The denominator is positive for all N>=2. Moreover |M_(N,2)|=(N!)^2[z^N]D(z), and its invertible subset has size (N!)^2[z^N]H(z). The conditioned Ewens_N(1/2) representation A=P(I+Q) is justified by its weighted matching fibers, and A is invertible if and only if every cycle of Q is odd (necessarily of length at least three). The small cases are p_2=p_4=0 and p_3=1, with 0<p_N<1 for all N>=5. As N tends to infinity through all integers, p_N=C0*N^(-1/4)+(-1)^(N+1)*C1*(N^(-3/4)+N^(-7/4))+O(N^(-9/4)), where C0=2^(1/4)*sqrt(pi)/Gamma(1/4) and C1=e*sqrt(pi)/(2^(9/4)*Gamma(3/4)). In particular p_N is asymptotic to C0*N^(-1/4). This includes the contribution from z=-1 and proves cancellation of the nonoscillating N^(-5/4) term. No zero-diagonal or shifted-matrix claim is made.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 12 scientific source/evidence files, including 2 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B14-P01 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/verify_asymptotics.py`](source/evidence/verify_asymptotics.py)
- [`evidence/verify_exact.py`](source/evidence/verify_exact.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B14-P01/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B14-P01/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 evidence/verify_exact.py
```

<!-- END PACKAGING REPLAY -->
