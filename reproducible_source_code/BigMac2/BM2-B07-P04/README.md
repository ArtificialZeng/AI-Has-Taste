# BM2-B07-P04 — reproduction source and evidence

Exact Verification of the Kasami Cyclic-Additive Identity at n=14

[Final PDF](../../../pdfs/BigMac2/BM2-B07-P04_Exact_Verification_of_the_Kasami_Cyclic_Additive_Identity_at_n_14.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B07-P04/packaging-review.json)

## Mathematical scope

Proof of the frozen original statement. Let K=GF(2^14). For each k in {3,5}, define F_k(t)=t^(2^(2k)-2^k+1) and Delta_k={F_k(t)+F_k(t+1)+1:t in K}. Then |Delta_3|=|Delta_5|=8192 and, for every rho in K\{0,1}, the number of ordered triples (x,y,z) in Delta_k^3 satisfying x+rho*y+(1+rho)*z=0 is exactly 2^25. The claim resolves only this frozen finite n=14 layer and asserts nothing for arbitrary n.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 11 scientific source/evidence files, including 2 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (1 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B07-P04 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/audit_n14.c`](source/evidence/audit_n14.c)
- [`evidence/verify_n14.c`](source/evidence/verify_n14.c)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B07-P04/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B07-P04/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Not rerun during packaging: No short positive exact checker selected; see archived source/proof dossier. Compile C11 verifier/auditor. Auditor recomputes large trace/correlation tables and direct 8192x8192 count checks; do not promise20 seconds. Retain n14_certificate.tsv and short n14_run.log/n14_audit.log.

<!-- END PACKAGING REPLAY -->
