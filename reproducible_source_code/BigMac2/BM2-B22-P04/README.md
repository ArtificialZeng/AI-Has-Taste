# BM2-B22-P04 — reproduction source and evidence

Integral Homology of Singleton-Anchor Configuration Spaces of Finite Graphs

[Final PDF](../../../pdfs/BigMac2/BM2-B22-P04_Integral_Homology_of_Singleton_Anchor_Configuration_Spaces_of_Finite_Graphs.pdf) · [Catalog](../../../README.md#bigmac2) · [Gate provenance](../../../assets/BigMac2/gates/BM2-B22-P04/packaging-review.json)

## Mathematical scope

Partial result; original problem unresolved. For every nonempty finite graph G (possibly disconnected), every vertex k, and every integer n>=1, the integral homology of Sigma(G,{k},n) is torsion-free. More precisely, if c is the number of components and beta=rank H_1(G;Z), then rank H_q(Sigma(G,{k},n);Z)=binom(n,q) beta^q (c^(n-q)-(c-1)^(n-q)) for 0<=q<=n, with the rank at q=n equal to zero, and all higher homology zero. Consequently any torsion witness in the frozen problem must have |K|>=2 and n>=|K|+2.

## Reproduction coverage

Archived scientific programs and exact evidence; all original bytes preserved. Full computations not rerun during packaging.

The package contains 39 scientific source/evidence files, including 1 programs. Exact certificates, source/problem statements and independent verifier programs are included where archived. Search experiments and negative tests are not automatically proof validators. A file hash or syntax check is not mathematical verification.

## Prepare a working copy

Some large generated certificates are stored with lossless gzip compression (0 files). Do not run code against compressed filenames. From the repository root:

```sh
python3 reproducible_source_code/BigMac2/prepare.py BM2-B22-P04 --output /path/to/new-working-directory
```

This copies the selected source tree and decompresses data while verifying original SHA-256 hashes. The output must be a new directory. Run programs in that working copy, from the working directory specified by the individual script, to avoid changing the archive.

Python 3.12+ is recommended. Detected direct third-party imports: none (standard library for the archived Python programs). The optional requirements.txt records names, not a reproduced historical environment. C/C++ code and external tools (for example nauty, SAT solvers or Singular) must be rebuilt/installed separately when the script requires them. This packaging task installs nothing.

## Program entry points

- [`evidence/diamond_n3.py`](source/evidence/diamond_n3.py)

## Portability notes

Historical program text is unchanged; these path references require review or a documented local adapter before another machine can run the relevant wrapper:

- No machine-specific path detected in archived program text.

Do not bypass a binary-hash/provenance assertion and call the historical run reproduced. See [collection reproduction notes](../REPRODUCTION_NOTES.md) for specific tools and limitations. Historical `publication.json` and claim/audit records are provenance, not ready-made manifests of this reorganized subset; primary-source downloads, environment directories, compiled binaries and old PDFs are deliberately omitted.

[Matching LaTeX](../../../latex_source_code/BigMac2/BM2-B22-P04/) · [Per-file hashes and storage map](package.json) · [Omitted files](../../../assets/BigMac2/gates/BM2-B22-P04/omitted-files.json)

<!-- BEGIN PACKAGING REPLAY -->
## Actual packaging check

Bounded replay passed; Writes regenerated exact cellular matrices and Smith certificates into explicit replay-diamond output, leaving archived evidence intact in a disposable copy.

```sh
python3 evidence/diamond_n3.py --output replay-diamond
```

<!-- END PACKAGING REPLAY -->
