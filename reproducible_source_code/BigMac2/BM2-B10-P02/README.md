# BM2-B10-P02 — reproduction source and evidence

Sharp Consensus-Time Asymptotics for a Degenerate Monotone Aggregation Rule

[Final PDF](../../../pdfs/BigMac2/BM2-B10-P02_Sharp_Consensus_Time_Asymptotics_for_a_Degenerate_Monotone_Aggregation_Rule.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B10-P02/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. For the exact asynchronous with-replacement birth-death chain frozen in source.md and problem.md, let Phi(x)=integral_0^x exp(-t^2/2) dt, S=sqrt(pi/2), A(x)=integral_0^x Phi(y)exp(y^2/2)/y dy, and B(x)=integral_x^infinity (S-Phi(y))exp(y^2/2)/y dy. There is a unique x_*>0 satisfying A(x_*)=B(x_*). Uniformly on compact subsets of [0,infinity), N^(-3/2)u_N(floor(x sqrt(N))) converges to ((S-Phi(x))/S)A(x)+(Phi(x)/S)B(x), continuously extended by zero at x=0. Consequently C_*=lim_N N^(-3/2)max_{1<=s<N} u_N(s) exists and equals A(x_*)=B(x_*), every choice s_N in argmax_{1<=s<N}u_N(s) satisfies s_N/sqrt(N)->x_*, and the full extended-half-line limit set of scaled maximizers is exactly {x_*}, excluding +infinity.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 6 scientific source/evidence files, including 0 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B10-P02 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- No standalone program was archived; the mathematical proof/evidence is supplied below.

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B10-P02/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B10-P02/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: No short positive exact checker selected; see archived source/proof dossier. No code archived; mathematical proof is the manuscript and proof dossier.

<!-- END PACKAGING REPLAY -->
