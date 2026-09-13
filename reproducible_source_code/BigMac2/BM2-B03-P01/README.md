# BM2-B03-P01 — reproduction source and evidence

A Fixed-Periodic Bound for Signed Affine Copies of {0,1,3}

[Final PDF](../../../pdfs/BigMac2/BM2-B03-P01_A_Fixed_Periodic_Bound_for_Signed_Affine_Copies_of_0_1_3.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B03-P01/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For every integer q >= 2 with gcd(q,6)=1 and every nonempty R subset of Z/qZ, if A_N={1 <= n <= N : n mod q lies in R} and M(A) counts signed ordered pairs (x,d) with d != 0 and x,x+d,x+3d in A, then the limit L(q,R)=lim_{N->infinity} M(A_N)/|A_N|^2 exists, satisfies L(q,R) <= 1/3, and equals 1/3 if and only if R is a coset of an additive subgroup of Z/qZ. More precisely, L(q,R)=T_q(R)/(3|R|^2), where T_q(R)=#{(u,v) in (Z/qZ)^2 : u,u+v,u+3v in R}.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 9 scientific source/evidence files, including 1 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B03-P01 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`audit/referee_check.py`](source/audit/referee_check.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B03-P01/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B03-P01/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Finite exact supporting checks only; consult the proof dossier for the full quantified claim.

```sh
python3 audit/referee_check.py
```

<!-- END PACKAGING REPLAY -->
